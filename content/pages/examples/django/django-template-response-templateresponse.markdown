title: django.template.response TemplateResponse Example Code
category: page
slug: django-template-response-templateresponse-examples
sortorder: 500013510
toc: False
sidebartitle: django.template.response TemplateResponse
meta: Python code examples for the TemplateResponse class that is part of Django's django.template.response module.


[TemplateResponse](https://docs.djangoproject.com/en/stable/ref/template-response/)
([source code](https://github.com/django/django/blob/master/django/template/response.py))
is a class provided by [Django](/django.html) that retains context for the
HTTP request that caused the view to generate the response. TemplateResponse 
is useful for modifying a response before it is rendered, which cannot be
done with a traditional static 
[HttpResponse](/django-http-httpresponse-examples.html) object.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / placeholderadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/placeholderadmin.py)

```python
# -*- coding: utf-8 -*-
import uuid
import warnings

from django.conf.urls import url
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.utils import get_deleted_objects
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import get_list_or_404, get_object_or_404, render
~~from django.template.response import TemplateResponse
from django.utils import six
from django.utils.six.moves.urllib.parse import parse_qsl, urlparse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_POST

from cms import operations
from cms.admin.forms import PluginAddValidationForm
from cms.constants import SLUG_REGEXP
from cms.exceptions import PluginLimitReached
from cms.models.placeholdermodel import Placeholder
from cms.models.placeholderpluginmodel import PlaceholderReference
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.signals import (pre_placeholder_operation, 
                         post_placeholder_operation)
from cms.toolbar.utils import get_plugin_tree_as_json
from cms.utils import copy_plugins, get_current_site
from cms.utils.compat import DJANGO_2_0
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import get_language_code, get_language_list
from cms.utils.plugins import (has_reached_plugin_limit, 
                               reorder_plugins)
from cms.utils.urlutils import admin_reverse


## ... source code abbreviated here to get to the examples ...


    @xframe_options_sameorigin
    def delete_plugin(self, request, plugin_id):
        plugin = self._get_plugin_from_id(plugin_id)

        if not self.has_delete_plugin_permission(request, plugin):
            return HttpResponseForbidden(force_text(
                _("You do not have permission "
                  "to delete this plugin")))

        opts = plugin._meta
        using = router.db_for_write(opts.model)
        if DJANGO_2_0:
            get_deleted_objects_additional_kwargs = {
                'opts': opts,
                'using': using,
                'user': request.user,
            }
        else:
            get_deleted_objects_additional_kwargs = {'request': \
                                                     request}
        deleted_objects, __, perms_needed, 
            protected = get_deleted_objects(
            [plugin], admin_site=self.admin_site,
            **get_deleted_objects_additional_kwargs
        )

        if request.POST:  # The user has already confirmed deletion.
            if perms_needed:
                raise PermissionDenied(_("You do not have permission "
                                         "to delete this plugin"))
            obj_display = force_text(plugin)
            placeholder = plugin.placeholder
            plugin_tree_order = placeholder.get_plugin_tree_order(
                language=plugin.language,
                parent_id=plugin.parent_id,
            )

            operation_token = self._send_pre_placeholder_operation(
                request,
                operation=operations.DELETE_PLUGIN,
                plugin=plugin,
                placeholder=placeholder,
                tree_order=plugin_tree_order,
            )

            plugin.delete()
            placeholder.mark_as_dirty(plugin.language, 
                                      clear_cache=False)
            reorder_plugins(
                placeholder=placeholder,
                parent_id=plugin.parent_id,
                language=plugin.language,
            )

            self.log_deletion(request, plugin, obj_display)
            self.message_user(request, 
                              _('The %(name)s plugin "%(obj)s" '
                                'was deleted successfully.') % {
                'name': force_text(opts.verbose_name), 
                'obj': force_text(obj_display)})

            # Avoid query by removing the plugin being deleted
            # from the tree order list
            new_plugin_tree_order = list(plugin_tree_order)
            new_plugin_tree_order.remove(plugin.pk)

            self._send_post_placeholder_operation(
                request,
                operation=operations.DELETE_PLUGIN,
                token=operation_token,
                plugin=plugin,
                placeholder=placeholder,
                tree_order=new_plugin_tree_order,
            )
            return HttpResponseRedirect(admin_reverse(\
                    'index', current_app=self.admin_site.name))

        plugin_name = force_text(plugin.get_plugin_class().name)

        if perms_needed or protected:
            title = _("Cannot delete %(name)s") % {"name": plugin_name}
        else:
            title = _("Are you sure?")
        context = {
            "title": title,
            "object_name": plugin_name,
            "object": plugin,
            "deleted_objects": deleted_objects,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": opts.app_label,
        }
        request.current_app = self.admin_site.name
~~        return TemplateResponse(
~~            request, "admin/cms/page/plugin/"
~~                     "delete_confirmation.html", context
~~        )

    @xframe_options_sameorigin
    def clear_placeholder(self, request, placeholder_id):
        placeholder = get_object_or_404(Placeholder, pk=placeholder_id)
        language = request.GET.get('language')

        if placeholder.pk == request.toolbar.clipboard.pk:
            # User is clearing the clipboard, no need for permission
            # checks here as the clipboard is unique per user.
            # There could be a case where a plugin has relationship to
            # an object the user does not have permission to delete.
            placeholder.clear(language)
            return HttpResponseRedirect(admin_reverse('index', 
                    current_app=self.admin_site.name))

        if not self.has_clear_placeholder_permission(request, 
                                                     placeholder, 
                                                     language):
            return HttpResponseForbidden(force_text(_(\
                "You do not have permission to clear this placeholder")))

        opts = Placeholder._meta
        using = router.db_for_write(Placeholder)
        plugins = placeholder.get_plugins_list(language)

        if DJANGO_2_0:
            get_deleted_objects_additional_kwargs = {
                'opts': opts,
                'using': using,
                'user': request.user,
            }
        else:
            get_deleted_objects_additional_kwargs = {'request': request}
        deleted_objects, __, perms_needed, protected = get_deleted_objects(
            plugins, admin_site=self.admin_site,
            **get_deleted_objects_additional_kwargs
        )

        obj_display = force_text(placeholder)

        if request.POST:
            # The user has already confirmed the deletion.
            if perms_needed:
                return HttpResponseForbidden(force_text(_("You "
                    "do not have permission to clear this placeholder")))

            operation_token = self._send_pre_placeholder_operation(
                request,
                operation=operations.CLEAR_PLACEHOLDER,
                plugins=plugins,
                placeholder=placeholder,
            )

            placeholder.clear(language)
            placeholder.mark_as_dirty(language, clear_cache=False)

            self.log_deletion(request, placeholder, obj_display)
            self.message_user(request, 
                              _('The placeholder "%(obj)s" '
                                'was cleared successfully.') % {
                'obj': obj_display})

            self._send_post_placeholder_operation(
                request,
                operation=operations.CLEAR_PLACEHOLDER,
                token=operation_token,
                plugins=plugins,
                placeholder=placeholder,
            )
            return HttpResponseRedirect(admin_reverse('index', 
                                        current_app=self.admin_site.name))

        if perms_needed or protected:
            title = _("Cannot delete %(name)s") % {"name": obj_display}
        else:
            title = _("Are you sure?")

        context = {
            "title": title,
            "object_name": _("placeholder"),
            "object": placeholder,
            "deleted_objects": deleted_objects,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": opts.app_label,
        }
        request.current_app = self.admin_site.name
~~        return TemplateResponse(request, 
~~                                "admin/cms/page/plugin/"
~~                                "delete_confirmation.html", 
~~                                context)

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse
from warnings import warn

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Substr
from django.http import Http404
~~from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import ugettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, 
    get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import (WAGTAIL_APPEND_SLASH, 
                                camelcase_to_underscore, 
                                resolve_model_string)
from wagtail.search import index
from wagtail.utils.deprecation import RemovedInWagtail29Warning


logger = logging.getLogger('wagtail.core')

PAGE_TEMPLATE_VAR = 'page'


class SiteManager(models.Manager):
    def get_by_natural_key(self, hostname, port):
        return self.get(hostname=hostname, port=port)


## ... source code abbreviated here to get to the examples ...


    def get_template(self, request, *args, **kwargs):
        if request.is_ajax():
            return self.ajax_template or self.template
        else:
            return self.template

    def serve(self, request, *args, **kwargs):
        request.is_preview = getattr(request, 'is_preview', False)

~~        return TemplateResponse(
~~            request,
~~            self.get_template(request, *args, **kwargs),
~~            self.get_context(request, *args, **kwargs)
~~        )

    def is_navigable(self):
        """
        Return true if it's meaningful to browse subpages 
        of this page - i.e. it currently has subpages,
        or it's at the top level (this rule necessary for 
        empty out-of-the-box sites to have working navigation)
        """
        return (not self.is_leaf()) or self.depth == 2


## ... source code abbreviated here to get to the examples ...


    def serve_password_required_response(self, request, form, action_url):
        """
        Serve a response indicating that the user has been 
        denied access to view this page, and must supply a password.
        form = a Django form object containing the password input
            (and zero or more hidden fields that 
             also need to be output on the template)
        action_url = URL that this form should be POSTed to
        """
        context = self.get_context(request)
        context['form'] = form
        context['action_url'] = action_url
~~        return TemplateResponse(request, 
~~                                self.password_required_template, 
~~                                context)

    def with_content_json(self, content_json):
        """
        Returns a new version of the page with field 
        values updated to reflect changes in the provided 
        ``content_json`` (which usually comes from a 
        previously-saved page revision).

        Certain field values are preserved in order 
        to prevent errors if the returned page is saved, such as 
        ``id``, ``content_type`` and some tree-related values. The 
        following field values are also preserved, as they 
        are considered to be meaningful to the page as a 
        whole, rather than to a specific revision:

        * ``draft_title``
        * ``live``
        * ``has_unpublished_changes``
        * ``owner``
        * ``locked``
        * ``latest_revision_created_at``
        * ``first_published_at``
        """

        obj = self.specific_class.from_json(content_json)

        # These should definitely never change between revisions
        obj.pk = self.pk
        obj.content_type = self.content_type

        # Override possibly-outdated tree parameter fields
        obj.path = self.path
        obj.depth = self.depth
        obj.numchild = self.numchild

        # Update url_path to reflect potential slug changes, but 
        # maintining the page's
        # existing tree position
        obj.set_url_path(self.get_parent())

        # Ensure other values that are meaningful for the 
        # page as a whole (rather than
        # to a specific revision) are preserved
        obj.draft_title = self.draft_title
        obj.live = self.live
        obj.has_unpublished_changes = self.has_unpublished_changes
        obj.owner = self.owner
        obj.locked = self.locked
        obj.latest_revision_created_at = self.latest_revision_created_at
        obj.first_published_at = self.first_published_at

        return obj

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')

## ... source code continues from here with no further examples ...
```
