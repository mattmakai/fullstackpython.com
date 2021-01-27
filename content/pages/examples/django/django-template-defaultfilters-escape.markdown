title: django.template.defaultfilters escape Example Code
category: page
slug: django-template-defaultfilters-escape-examples
sortorder: 500011383
toc: False
sidebartitle: django.template.defaultfilters escape
meta: Python example code that shows how to use the escape callable from the django.template.defaultfilters module of the Django project.


`escape` is a callable within the `django.template.defaultfilters` module of the Django project.

<a href="/django-template-defaultfilters-filesizeformat-examples.html">filesizeformat</a>,
<a href="/django-template-defaultfilters-safe-examples.html">safe</a>,
<a href="/django-template-defaultfilters-slugify-examples.html">slugify</a>,
<a href="/django-template-defaultfilters-striptags-examples.html">striptags</a>,
<a href="/django-template-defaultfilters-title-examples.html">title</a>,
and <a href="/django-template-defaultfilters-truncatechars-examples.html">truncatechars</a>
are several other callables with code examples from the same `django.template.defaultfilters` package.

## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / pageadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/pageadmin.py)

```python
# pageadmin.py
import uuid


import django
from django.contrib.admin.helpers import AdminForm
from django.conf import settings
from django.urls import re_path
from django.contrib import admin, messages
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import get_deleted_objects
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import (ObjectDoesNotExist,
                                    PermissionDenied, ValidationError)
from django.db import router, transaction
from django.db.models import Q, Prefetch
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    Http404,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)
from django.shortcuts import render, get_object_or_404
~~from django.template.defaultfilters import escape
from django.template.loader import get_template
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.utils.encoding import force_text
from django.utils.translation import gettext, gettext_lazy as _, get_language
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import QueryDict

from cms import operations
from cms.admin.forms import (
    AddPageForm,
    AddPageTypeForm,
    AdvancedSettingsForm,
    ChangePageForm,
    ChangeListForm,
    CopyPageForm,
    CopyPermissionForm,
    DuplicatePageForm,
    MovePageForm,
    PagePermissionForm,
    PublicationDatesForm,
)
from cms.admin.permissionadmin import PERMISSION_ADMIN_INLINES
from cms.admin.placeholderadmin import PlaceholderAdminMixin


## ... source file abbreviated to get to escape examples ...


        site = self.get_site(request)
        language = get_site_language_from_request(request, site_id=site.pk)
        languages = self._get_site_languages(request, obj)
        context.update({
            'language': language,
            'language_tabs': languages,
            'show_language_tabs': len(list(languages)) > 1 and not context.get('publishing_dates', False),
        })
        return context

    def get_preserved_filters(self, request):
        preserved_filters_encoded = super().get_preserved_filters(request)
        preserved_filters = QueryDict(preserved_filters_encoded).copy()
        lang = request.GET.get('language')

        if lang:
            preserved_filters.update({
                'language': lang
            })

        return preserved_filters.urlencode()

    def _get_404_exception(self, object_id):
        exception = Http404(_('%(name)s object with primary key %(key)r does not exist.') % {
            'name': force_text(self.opts.verbose_name),
~~            'key': escape(object_id),
        })
        return exception

    def _has_add_permission_from_request(self, request):
        site = self.get_site(request)
        parent_node_id = request.GET.get('parent_node', None)

        if parent_node_id:
            try:
                parent_item = self.get_queryset(request).get(node=parent_node_id)
            except self.model.DoesNotExist:
                return False
        else:
            parent_item = None

        if parent_item:
            has_perm = page_permissions.user_can_add_subpage(
                request.user,
                target=parent_item,
                site=site,
            )
        else:
            has_perm = page_permissions.user_can_add_page(request.user, site=site)
        return has_perm


## ... source file continues with no further escape examples...

```

