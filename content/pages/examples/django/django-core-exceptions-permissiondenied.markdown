title: django.core.exceptions PermissionDenied Example Code
category: page
slug: django-core-exceptions-permissiondenied-examples
sortorder: 500011105
toc: False
sidebartitle: django.core.exceptions PermissionDenied
meta: Python example code for the PermissionDenied class from the django.core.exceptions module of the Django project.


PermissionDenied is a class within the django.core.exceptions module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / models.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/models.py)

```python
# models.py
from __future__ import absolute_import

from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
~~from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

import allauth.app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import get_next_redirect_url, setup_user_email
from allauth.utils import get_user_model

from ..utils import get_request_param
from . import app_settings, providers
from .adapter import get_adapter
from .fields import JSONField


class SocialAppManager(models.Manager):
    def get_current(self, provider, request=None):
        cache = {}
        if request:
            cache = getattr(request, '_socialapp_cache', {})
            request._socialapp_cache = cache
        app = cache.get(provider)
        if not app:


## ... source file abbreviated to get to PermissionDenied examples ...


    def get_redirect_url(self, request):
        url = self.state.get('next')
        return url

    @classmethod
    def state_from_request(cls, request):
        state = {}
        next_url = get_next_redirect_url(request)
        if next_url:
            state['next'] = next_url
        state['process'] = get_request_param(request, 'process', 'login')
        state['scope'] = get_request_param(request, 'scope', '')
        state['auth_params'] = get_request_param(request, 'auth_params', '')
        return state

    @classmethod
    def stash_state(cls, request):
        state = cls.state_from_request(request)
        verifier = get_random_string()
        request.session['socialaccount_state'] = (state, verifier)
        return verifier

    @classmethod
    def unstash_state(cls, request):
        if 'socialaccount_state' not in request.session:
~~            raise PermissionDenied()
        state, verifier = request.session.pop('socialaccount_state')
        return state

    @classmethod
    def verify_and_unstash_state(cls, request, verifier):
        if 'socialaccount_state' not in request.session:
~~            raise PermissionDenied()
        state, verifier2 = request.session.pop('socialaccount_state')
        if verifier != verifier2:
~~            raise PermissionDenied()
        return state



## ... source file continues with no further PermissionDenied examples...

```


## Example 2 from django-axes
[django-axes](https://github.com/jazzband/django-axes/)
([project documentation](https://django-axes.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-axes/)
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT license](https://github.com/jazzband/django-axes/blob/master/LICENSE)
and maintained by the group of developers known as
[Jazzband](https://jazzband.co/).

[**django-axes / axes / exceptions.py**](https://github.com/jazzband/django-axes/blob/master/axes/./exceptions.py)

```python
# exceptions.py
~~from django.core.exceptions import PermissionDenied


~~class AxesBackendPermissionDenied(PermissionDenied):


class AxesBackendRequestParameterRequired(ValueError):



## ... source file continues with no further PermissionDenied examples...

```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / api.py**](https://github.com/divio/django-cms/blob/develop/cms/./api.py)

```python
# api.py
import datetime

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.exceptions import FieldError
~~from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
from django.db import transaction
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.utils.translation import activate

from six import string_types

from cms import constants
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from cms.constants import TEMPLATE_INHERITANCE_MAGIC
from cms.models.pagemodel import Page
from cms.models.permissionmodels import (PageUser, PagePermission, GlobalPagePermission,
                                         ACCESS_PAGE_AND_DESCENDANTS)
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.models.titlemodels import Title
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils import copy_plugins, get_current_site
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import get_language_list
from cms.utils.page import get_available_slug


## ... source file abbreviated to get to PermissionDenied examples ...


        'can_add': can_add or grant_all,
        'can_change': can_change or grant_all,
        'can_delete': can_delete or grant_all,
        'can_change_advanced_settings': can_change_advanced_settings or grant_all,
        'can_publish': can_publish or grant_all,
        'can_change_permissions': can_change_permissions or grant_all,
        'can_move_page': can_move_page or grant_all,
        'can_view': can_view or grant_all,
    }

    page_permission = PagePermission(page=page, user=user,
                                     grant_on=grant_on, **data)
    page_permission.save()
    if global_permission:
        page_permission = GlobalPagePermission(
            user=user, can_recover_page=can_recover_page, **data)
        page_permission.save()
        page_permission.sites.add(get_current_site())
    return page_permission


def publish_page(page, user, language):
    page = page.reload()

    if not page.has_publish_permission(user):
~~        raise PermissionDenied()
    with current_user(user.get_username()):
        page.publish(language)
    return page.reload()


def publish_pages(include_unpublished=False, language=None, site=None):
    qs = Page.objects.drafts()

    if not include_unpublished:
        qs = qs.filter(title_set__published=True).distinct()

    if site:
        qs = qs.filter(node__site=site)

    output_language = None
    for i, page in enumerate(qs):
        add = True
        titles = page.title_set
        if not include_unpublished:
            titles = titles.filter(published=True)
        for lang in titles.values_list("language", flat=True):
            if language is None or lang == language:
                if not output_language:
                    output_language = lang


## ... source file continues with no further PermissionDenied examples...

```


## Example 4 from django-downloadview
[django-downloadview](https://github.com/benoitbryon/django-downloadview)
([project documentation](https://django-downloadview.readthedocs.io/en/1.9/)
and
[PyPI package information](https://pypi.org/project/django-downloadview/))
is a [Django](/django.html) extension for serving downloads through your
web application. While typically you would use a web server to handle
[static content](/static-content.html), sometimes you need to control
file access, such as requiring a user to register before downloading a
PDF. In that situations, django-downloadview is a handy library to avoid
boilerplate code for common scenarios.

[**django-downloadview / django_downloadview / decorators.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/./decorators.py)

```python
# decorators.py

from functools import wraps

from django.conf import settings
~~from django.core.exceptions import PermissionDenied
from django.core.signing import BadSignature, SignatureExpired, TimestampSigner


class DownloadDecorator(object):

    def __init__(self, middleware_factory):
        self.middleware_factory = middleware_factory

    def __call__(self, view_func, *middleware_args, **middleware_kwargs):

        def decorated(request, *view_args, **view_kwargs):
            response = view_func(request, *view_args, **view_kwargs)
            middleware = self.middleware_factory(*middleware_args, **middleware_kwargs)
            return middleware.process_response(request, response)

        return decorated


def _signature_is_valid(request):

    signer = TimestampSigner()
    signature = request.GET.get("X-Signature")
    expiration = getattr(settings, "DOWNLOADVIEW_URL_EXPIRATION", None)

    try:
        signature_path = signer.unsign(signature, max_age=expiration)
    except SignatureExpired as e:
~~        raise PermissionDenied("Signature expired") from e
    except BadSignature as e:
~~        raise PermissionDenied("Signature invalid") from e
    except Exception as e:
~~        raise PermissionDenied("Signature error") from e

    if request.path != signature_path:
~~        raise PermissionDenied("Signature mismatch")


def signature_required(function):

    @wraps(function)
    def decorator(request, *args, **kwargs):
        _signature_is_valid(request)
        return function(request, *args, **kwargs)

    return decorator



## ... source file continues with no further PermissionDenied examples...

```


## Example 5 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / tools.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/tools.py)

```python
# tools.py
from __future__ import absolute_import, unicode_literals

from django.contrib.admin.options import IS_POPUP_VAR
~~from django.core.exceptions import PermissionDenied
from django.utils.http import urlencode


ALLOWED_PICK_TYPES = ('folder', 'file')


def check_files_edit_permissions(request, files):
    for f in files:
        if not f.has_edit_permission(request):
~~            raise PermissionDenied


def check_folder_edit_permissions(request, folders):
    for f in folders:
        if not f.has_edit_permission(request):
~~            raise PermissionDenied
        check_files_edit_permissions(request, f.files)
        check_folder_edit_permissions(request, f.children.all())


def check_files_read_permissions(request, files):
    for f in files:
        if not f.has_read_permission(request):
~~            raise PermissionDenied


def check_folder_read_permissions(request, folders):
    for f in folders:
        if not f.has_read_permission(request):
~~            raise PermissionDenied
        check_files_read_permissions(request, f.files)
        check_folder_read_permissions(request, f.children.all())


def userperms_for_request(item, request):
    r = []
    ps = ['read', 'edit', 'add_children']
    for p in ps:
        attr = "has_%s_permission" % p
        if hasattr(item, attr):
            x = getattr(item, attr)(request)
            if x:
                r.append(p)
    return r


def popup_status(request):
    return (
        IS_POPUP_VAR in request.GET
        or 'pop' in request.GET
        or IS_POPUP_VAR in request.POST
        or 'pop' in request.POST
    )



## ... source file continues with no further PermissionDenied examples...

```


## Example 6 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / mixins.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./mixins.py)

```python
# mixins.py
from collections.abc import Iterable

from django.conf import settings
from django.contrib.auth.decorators import login_required, REDIRECT_FIELD_NAME
~~from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from guardian.utils import get_user_obj_perms_model
UserObjectPermission = get_user_obj_perms_model()
from guardian.utils import get_40x_or_None, get_anonymous_user
from guardian.shortcuts import get_objects_for_user


class LoginRequiredMixin:
    redirect_field_name = REDIRECT_FIELD_NAME
    login_url = settings.LOGIN_URL

    def dispatch(self, request, *args, **kwargs):
        return login_required(redirect_field_name=self.redirect_field_name,
                              login_url=self.login_url)(
            super().dispatch
        )(request, *args, **kwargs)


class PermissionRequiredMixin:
    login_url = settings.LOGIN_URL
    permission_required = None
    redirect_field_name = REDIRECT_FIELD_NAME
    return_403 = False
    return_404 = False
    raise_exception = False


## ... source file abbreviated to get to PermissionDenied examples ...


                                       % self.permission_required)
        return perms

    def get_permission_object(self):
        if hasattr(self, 'permission_object'):
            return self.permission_object
        return (hasattr(self, 'get_object') and self.get_object() or
                getattr(self, 'object', None))

    def check_permissions(self, request):
        obj = self.get_permission_object()

        forbidden = get_40x_or_None(request,
                                    perms=self.get_required_permissions(
                                        request),
                                    obj=obj,
                                    login_url=self.login_url,
                                    redirect_field_name=self.redirect_field_name,
                                    return_403=self.return_403,
                                    return_404=self.return_404,
                                    accept_global_perms=self.accept_global_perms
                                    )
        if forbidden:
            self.on_permission_check_fail(request, forbidden, obj=obj)
        if forbidden and self.raise_exception:
~~            raise PermissionDenied()
        return forbidden

    def on_permission_check_fail(self, request, response, obj=None):

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if response:
            return response
        return super().dispatch(request, *args, **kwargs)


class GuardianUserMixin:

    @staticmethod
    def get_anonymous():
        return get_anonymous_user()

    def add_obj_perm(self, perm, obj):
        return UserObjectPermission.objects.assign_perm(perm, self, obj)

    def del_obj_perm(self, perm, obj):


## ... source file continues with no further PermissionDenied examples...

```


## Example 7 from django-haystack
[django-haystack](https://github.com/django-haystack/django-haystack)
([project website](http://haystacksearch.org/) and
[PyPI page](https://pypi.org/project/django-haystack/))
is a search abstraction layer that separates the Python search code
in a [Django](/django.html) web application from the search engine
implementation that it runs on, such as
[Apache Solr](http://lucene.apache.org/solr/),
[Elasticsearch](https://www.elastic.co/)
or [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html).

The django-haystack project is open source under the
[BSD license](https://github.com/django-haystack/django-haystack/blob/master/LICENSE).

[**django-haystack / haystack / admin.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./admin.py)

```python
# admin.py
from django.contrib.admin.options import ModelAdmin, csrf_protect_m
from django.contrib.admin.views.main import SEARCH_VAR, ChangeList
~~from django.core.exceptions import PermissionDenied
from django.core.paginator import InvalidPage, Paginator
from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.translation import ungettext

from haystack import connections
from haystack.constants import DEFAULT_ALIAS
from haystack.query import SearchQuerySet
from haystack.utils import get_model_ct_tuple


class SearchChangeList(ChangeList):
    def __init__(self, **kwargs):
        self.haystack_connection = kwargs.pop("haystack_connection", DEFAULT_ALIAS)
        super(SearchChangeList, self).__init__(**kwargs)

    def get_results(self, request):
        if SEARCH_VAR not in request.GET:
            return super(SearchChangeList, self).get_results(request)

        sqs = (
            SearchQuerySet(self.haystack_connection)
            .models(self.model)
            .auto_query(request.GET[SEARCH_VAR])


## ... source file abbreviated to get to PermissionDenied examples ...


        )

        can_show_all = result_count <= self.list_max_show_all
        multi_page = result_count > self.list_per_page

        try:
            result_list = paginator.page(self.page_num + 1).object_list
            result_list = [result.object for result in result_list]
        except InvalidPage:
            result_list = ()

        self.result_count = result_count
        self.full_result_count = full_result_count
        self.result_list = result_list
        self.can_show_all = can_show_all
        self.multi_page = multi_page
        self.paginator = paginator


class SearchModelAdminMixin(object):
    haystack_connection = DEFAULT_ALIAS

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        if not self.has_change_permission(request, None):
~~            raise PermissionDenied

        if SEARCH_VAR not in request.GET:
            return super(SearchModelAdminMixin, self).changelist_view(
                request, extra_context
            )

        indexed_models = (
            connections[self.haystack_connection]
            .get_unified_index()
            .get_indexed_models()
        )

        if self.model not in indexed_models:
            return super(SearchModelAdminMixin, self).changelist_view(
                request, extra_context
            )

        list_display = list(self.list_display)

        kwargs = {
            "haystack_connection": self.haystack_connection,
            "request": request,
            "model": self.model,
            "list_display": list_display,


## ... source file continues with no further PermissionDenied examples...

```


## Example 8 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / admin.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./admin.py)

```python
# admin.py
from datetime import datetime

import django
from django import forms
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin, messages
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.contrib.auth import get_permission_codename
from django.contrib.contenttypes.models import ContentType
~~from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_str
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from .formats.base_formats import DEFAULT_FORMATS
from .forms import ConfirmImportForm, ExportForm, ImportForm, export_action_form_factory
from .resources import modelresource_factory
from .results import RowResult
from .signals import post_export, post_import
from .tmp_storages import TempFolderStorage

SKIP_ADMIN_LOG = getattr(settings, 'IMPORT_EXPORT_SKIP_ADMIN_LOG', False)
TMP_STORAGE_CLASS = getattr(settings, 'IMPORT_EXPORT_TMP_STORAGE_CLASS',
                            TempFolderStorage)


if isinstance(TMP_STORAGE_CLASS, str):
    TMP_STORAGE_CLASS = import_string(TMP_STORAGE_CLASS)



## ... source file abbreviated to get to PermissionDenied examples ...


                name='%s_%s_import' % info),
        ]
        return my_urls + urls

    def get_resource_kwargs(self, request, *args, **kwargs):
        return {}

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        return self.get_resource_kwargs(request, *args, **kwargs)

    def get_resource_class(self):
        if not self.resource_class:
            return modelresource_factory(self.model)
        else:
            return self.resource_class

    def get_import_resource_class(self):
        return self.get_resource_class()

    def get_import_formats(self):
        return [f for f in self.formats if f().can_import()]

    @method_decorator(require_POST)
    def process_import(self, request, *args, **kwargs):
        if not self.has_import_permission(request):
~~            raise PermissionDenied

        form_type = self.get_confirm_import_form()
        confirm_form = form_type(request.POST)
        if confirm_form.is_valid():
            import_formats = self.get_import_formats()
            input_format = import_formats[
                int(confirm_form.cleaned_data['input_format'])
            ]()
            tmp_storage = self.get_tmp_storage_class()(name=confirm_form.cleaned_data['import_file_name'])
            data = tmp_storage.read(input_format.get_read_mode())
            if not input_format.is_binary() and self.from_encoding:
                data = force_str(data, self.from_encoding)
            dataset = input_format.create_dataset(data)

            result = self.process_dataset(dataset, confirm_form, request, *args, **kwargs)

            tmp_storage.remove()

            return self.process_result(result, request)

    def process_dataset(self, dataset, confirm_form, request, *args, **kwargs):

        res_kwargs = self.get_import_resource_kwargs(request, form=confirm_form, *args, **kwargs)
        resource = self.get_import_resource_class()(**res_kwargs)


## ... source file abbreviated to get to PermissionDenied examples ...



    def get_confirm_import_form(self):
        return ConfirmImportForm

    def get_form_kwargs(self, form, *args, **kwargs):
        return kwargs

    def get_import_data_kwargs(self, request, *args, **kwargs):
        form = kwargs.get('form')
        if form:
            kwargs.pop('form')
            return kwargs
        return {}

    def write_to_tmp_storage(self, import_file, input_format):
        tmp_storage = self.get_tmp_storage_class()()
        data = bytes()
        for chunk in import_file.chunks():
            data += chunk

        tmp_storage.save(data, input_format.get_read_mode())
        return tmp_storage

    def import_action(self, request, *args, **kwargs):
        if not self.has_import_permission(request):
~~            raise PermissionDenied

        context = self.get_import_context_data()

        import_formats = self.get_import_formats()
        form_type = self.get_import_form()
        form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
        form = form_type(import_formats,
                         request.POST or None,
                         request.FILES or None,
                         **form_kwargs)

        if request.POST and form.is_valid():
            input_format = import_formats[
                int(form.cleaned_data['input_format'])
            ]()
            import_file = form.cleaned_data['import_file']
            tmp_storage = self.write_to_tmp_storage(import_file, input_format)

            try:
                data = tmp_storage.read(input_format.get_read_mode())
                if not input_format.is_binary() and self.from_encoding:
                    data = force_str(data, self.from_encoding)
                dataset = input_format.create_dataset(data)
            except UnicodeDecodeError as e:


## ... source file abbreviated to get to PermissionDenied examples ...



        ChangeList = self.get_changelist(request)
        changelist_kwargs = {
            'request': request,
            'model': self.model,
            'list_display': list_display,
            'list_display_links': list_display_links,
            'list_filter': list_filter,
            'date_hierarchy': self.date_hierarchy,
            'search_fields': search_fields,
            'list_select_related': self.list_select_related,
            'list_per_page': self.list_per_page,
            'list_max_show_all': self.list_max_show_all,
            'list_editable': self.list_editable,
            'model_admin': self,
        }
        if django.VERSION >= (2, 1):
            changelist_kwargs['sortable_by'] = self.sortable_by
        cl = ChangeList(**changelist_kwargs)

        return cl.get_queryset(request)

    def get_export_data(self, file_format, queryset, *args, **kwargs):
        request = kwargs.pop("request")
        if not self.has_export_permission(request):
~~            raise PermissionDenied

        resource_class = self.get_export_resource_class()
        data = resource_class(**self.get_export_resource_kwargs(request)).export(queryset, *args, **kwargs)
        export_data = file_format.export_data(data)
        return export_data

    def get_export_context_data(self, **kwargs):
        return self.get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        return {}

    def export_action(self, request, *args, **kwargs):
        if not self.has_export_permission(request):
~~            raise PermissionDenied

        formats = self.get_export_formats()
        form = ExportForm(formats, request.POST or None)
        if form.is_valid():
            file_format = formats[
                int(form.cleaned_data['file_format'])
            ]()

            queryset = self.get_export_queryset(request)
            export_data = self.get_export_data(file_format, queryset, request=request)
            content_type = file_format.get_content_type()
            response = HttpResponse(export_data, content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="%s"' % (
                self.get_export_filename(request, queryset, file_format),
            )

            post_export.send(sender=None, model=self.model)
            return response

        context = self.get_export_context_data()

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Export")


## ... source file continues with no further PermissionDenied examples...

```


## Example 9 from django-loginas
[django-loginas](https://github.com/skorokithakis/django-loginas)
([PyPI package information](https://pypi.org/project/django-loginas/))
is [Django](/django.html) code library for admins to log into an application
as another user, typically for debugging purposes.

django-loginas is open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/skorokithakis/django-loginas/blob/master/LICENSE).

[**django-loginas / loginas / views.py**](https://github.com/skorokithakis/django-loginas/blob/master/loginas/./views.py)

```python
# views.py
from django.contrib import messages
from django.contrib.admin.utils import unquote
~~from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from . import settings as la_settings
from .utils import login_as, restore_original_login

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module  # type: ignore


try:
    from django.contrib.auth import get_user_model

    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User  # type: ignore


def _load_module(path):



## ... source file abbreviated to get to PermissionDenied examples ...


    except ValueError:
        raise ImproperlyConfigured("Error importing CAN_LOGIN_AS" " function. Is CAN_LOGIN_AS a" " string?")

    try:
        can_login_as = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured("Module {0} does not define a {1} " "function.".format(module, attr))
    return can_login_as


@csrf_protect
@require_POST
def user_login(request, user_id):
    user = User.objects.get(pk=unquote(user_id))

    if isinstance(la_settings.CAN_LOGIN_AS, str):
        can_login_as = _load_module(la_settings.CAN_LOGIN_AS)
    elif hasattr(la_settings.CAN_LOGIN_AS, "__call__"):
        can_login_as = la_settings.CAN_LOGIN_AS
    else:
        raise ImproperlyConfigured("The CAN_LOGIN_AS setting is neither a valid module nor callable.")
    no_permission_error = None
    try:
        if not can_login_as(request, user):
            no_permission_error = _("You do not have permission to do that.")
~~    except PermissionDenied as e:
        no_permission_error = str(e)
    if no_permission_error is not None:
        messages.error(request, no_permission_error, extra_tags=la_settings.MESSAGE_EXTRA_TAGS, fail_silently=True)
        return redirect(request.META.get("HTTP_REFERER", "/"))

    try:
        login_as(user, request)
    except ImproperlyConfigured as e:
        messages.error(request, str(e), extra_tags=la_settings.MESSAGE_EXTRA_TAGS, fail_silently=True)
        return redirect(request.META.get("HTTP_REFERER", "/"))

    return redirect(la_settings.LOGIN_REDIRECT)


def user_logout(request):
    restore_original_login(request)

    return redirect(la_settings.LOGOUT_REDIRECT)



## ... source file continues with no further PermissionDenied examples...

```


## Example 10 from django-rest-framework
[Django REST Framework](https://github.com/encode/django-rest-framework)
([project homepage and documentation](https://www.django-rest-framework.org/),
[PyPI package information](https://pypi.org/project/djangorestframework/)
and [more resources on Full Stack Python](/django-rest-framework-drf.html)),
often abbreviated as "DRF", is a popular [Django](/django.html) extension
for building [web APIs](/application-programming-interfaces.html).
The project has fantastic documentation and a wonderful
[quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
that serve as examples of how to make it easier for newcomers
to get started.

The project is open sourced under the
[Encode OSS Ltd. license](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md).

[**django-rest-framework / rest_framework / metadata.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./metadata.py)

```python
# metadata.py
from collections import OrderedDict

~~from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils.encoding import force_str

from rest_framework import exceptions, serializers
from rest_framework.request import clone_request
from rest_framework.utils.field_mapping import ClassLookupDict


class BaseMetadata:
    def determine_metadata(self, request, view):
        raise NotImplementedError(".determine_metadata() must be overridden.")


class SimpleMetadata(BaseMetadata):
    label_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'boolean',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'string',
        serializers.UUIDField: 'string',
        serializers.URLField: 'url',
        serializers.EmailField: 'email',
        serializers.RegexField: 'regex',
        serializers.SlugField: 'slug',


## ... source file continues with no further PermissionDenied examples...

```


## Example 11 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / auth.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/auth.py)

```python
# auth.py
import types
from functools import wraps

import l18n

from django.contrib.auth import get_user_model
from django.contrib.auth.views import redirect_to_login as auth_redirect_to_login
~~from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.timezone import activate as activate_tz
from django.utils.translation import gettext as _
from django.utils.translation import override

from wagtail.admin import messages
from wagtail.core.models import GroupPagePermission


def users_with_page_permission(page, permission_type, include_superusers=True):
    User = get_user_model()

    ancestors_and_self = list(page.get_ancestors()) + [page]
    perm = GroupPagePermission.objects.filter(permission_type=permission_type, page__in=ancestors_and_self)
    q = Q(groups__page_permissions__in=perm)

    if include_superusers:
        q |= Q(is_superuser=True)

    return User.objects.filter(is_active=True).filter(q).distinct()


def permission_denied(request):
    if request.is_ajax():
~~        raise PermissionDenied

    from wagtail.admin import messages

    messages.error(request, _('Sorry, you do not have permission to access this area.'))
    return redirect('wagtailadmin_home')


def user_passes_test(test):
    def decorator(view_func):

        @wraps(view_func)
        def wrapped_view_func(request, *args, **kwargs):
            if test(request.user):
                return view_func(request, *args, **kwargs)
            else:
                return permission_denied(request)

        return wrapped_view_func

    return decorator


def permission_required(permission_name):
    def test(user):


## ... source file abbreviated to get to PermissionDenied examples ...


        return user_passes_test(test)

    def require_any(self, *actions):
        def test(user):
            return self.policy.user_has_any_permission(user, actions)

        return user_passes_test(test)


def user_has_any_page_permission(user):
    if not user.is_active:
        return False

    if user.is_superuser:
        return True

    if GroupPagePermission.objects.filter(group__in=user.groups.all()).exists():
        return True


    return False


def reject_request(request):
    if request.is_ajax():
~~        raise PermissionDenied

    return auth_redirect_to_login(
        request.get_full_path(), login_url=reverse('wagtailadmin_login'))


def require_admin_access(view_func):
    def decorated_view(request, *args, **kwargs):

        user = request.user

        if user.is_anonymous:
            return reject_request(request)

        if user.has_perms(['wagtailadmin.access_admin']):
            preferred_language = None
            if hasattr(user, 'wagtail_userprofile'):
                preferred_language = user.wagtail_userprofile.get_preferred_language()
                l18n.set_language(preferred_language)
                time_zone = user.wagtail_userprofile.get_current_time_zone()
                activate_tz(time_zone)
            if preferred_language:
                with override(preferred_language):
                    response = view_func(request, *args, **kwargs)
                if hasattr(response, "render"):


## ... source file continues with no further PermissionDenied examples...

```

