title: django.shortcuts get_list_or_404 Example Code
category: page
slug: django-shortcuts-get-list-or-404-examples
sortorder: 500011345
toc: False
sidebartitle: django.shortcuts get_list_or_404
meta: Python example code for the get_list_or_404 callable from the django.shortcuts module of the Django project.


get_list_or_404 is a callable within the django.shortcuts module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / placeholderadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/placeholderadmin.py)

```python
# placeholderadmin.py
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
~~from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_POST

from six.moves.urllib.parse import parse_qsl, urlparse

from six import get_unbound_function, get_method_function

from cms import operations
from cms.admin.forms import PluginAddValidationForm
from cms.constants import SLUG_REGEXP
from cms.exceptions import PluginLimitReached
from cms.models.placeholdermodel import Placeholder
from cms.models.placeholderpluginmodel import PlaceholderReference
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.signals import pre_placeholder_operation, post_placeholder_operation
from cms.toolbar.utils import get_plugin_tree_as_json
from cms.utils import copy_plugins, get_current_site
from cms.utils.compat import DJANGO_2_0


## ... source file abbreviated to get to get_list_or_404 examples ...


            operation=operation,
            request=request,
            language=self._get_operation_language(request),
            token=token,
            origin=self._get_operation_origin(request),
            **kwargs
        )
        return token

    def _send_post_placeholder_operation(self, request, operation, token, **kwargs):
        if not request.GET.get('cms_path'):
            return

        post_placeholder_operation.send(
            sender=self.__class__,
            operation=operation,
            request=request,
            language=self._get_operation_language(request),
            token=token,
            origin=self._get_operation_origin(request),
            **kwargs
        )

    def _get_plugin_from_id(self, plugin_id):
        queryset = CMSPlugin.objects.values_list('plugin_type', flat=True)
~~        plugin_type = get_list_or_404(queryset, pk=plugin_id)[0]
        plugin_class = plugin_pool.get_plugin(plugin_type)
        real_queryset = plugin_class.get_render_queryset().select_related('parent', 'placeholder')
        return get_object_or_404(real_queryset, pk=plugin_id)

    def get_urls(self):
        info = "%s_%s" % (self.model._meta.app_label, self.model._meta.model_name)
        pat = lambda regex, fn: url(regex, self.admin_site.admin_view(fn), name='%s_%s' % (info, fn.__name__))
        url_patterns = [
            pat(r'copy-plugins/$', self.copy_plugins),
            pat(r'add-plugin/$', self.add_plugin),
            pat(r'edit-plugin/(%s)/$' % SLUG_REGEXP, self.edit_plugin),
            pat(r'delete-plugin/(%s)/$' % SLUG_REGEXP, self.delete_plugin),
            pat(r'clear-placeholder/(%s)/$' % SLUG_REGEXP, self.clear_placeholder),
            pat(r'move-plugin/$', self.move_plugin),
        ]
        return url_patterns + super(PlaceholderAdminMixin, self).get_urls()

    def has_add_plugin_permission(self, request, placeholder, plugin_type):
        return placeholder.has_add_plugin_permission(request.user, plugin_type)

    def has_change_plugin_permission(self, request, plugin):
        placeholder = plugin.placeholder
        return placeholder.has_change_plugin_permission(request.user, plugin)



## ... source file continues with no further get_list_or_404 examples...

```

