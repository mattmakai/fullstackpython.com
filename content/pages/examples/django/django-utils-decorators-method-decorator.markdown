title: django.utils.decorators method_decorator Example Code
category: page
slug: django-utils-decorators-method-decorator-examples
sortorder: 500011436
toc: False
sidebartitle: django.utils.decorators method_decorator
meta: Python example code for the method_decorator callable from the django.utils.decorators module of the Django project.


method_decorator is a callable within the django.utils.decorators module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / views.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py)

```python
# views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import (
    Http404,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
~~from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.edit import FormView

from ..exceptions import ImmediateHttpResponse
from ..utils import get_form_class, get_request_param
from . import app_settings, signals
from .adapter import get_adapter
from .forms import (
    AddEmailForm,
    ChangePasswordForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    SetPasswordForm,
    SignupForm,
    UserTokenForm,
)
from .models import EmailAddress, EmailConfirmation, EmailConfirmationHMAC
from .utils import (
    complete_signup,
    get_login_redirect_url,
    get_next_redirect_url,
    logout_on_password_change,
    passthrough_next_redirect_url,
    perform_login,
    sync_user_email_addresses,
    url_str_to_user_pk,
)


INTERNAL_RESET_URL_KEY = "set-password"
INTERNAL_RESET_SESSION_KEY = "_password_reset_key"


~~sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'oldpassword', 'password', 'password1', 'password2'))


def _ajax_response(request, response, form=None, data=None):
    adapter = get_adapter(request)
    if adapter.is_ajax(request):
        if (isinstance(response, HttpResponseRedirect) or isinstance(
                response, HttpResponsePermanentRedirect)):
            redirect_to = response['Location']
        else:
            redirect_to = None
        response = adapter.ajax_response(
            request,
            response,
            form=form,
            data=data,
            redirect_to=redirect_to)
    return response


class RedirectAuthenticatedUserMixin(object):

    def dispatch(self, request, *args, **kwargs):


## ... source file continues with no further method_decorator examples...

```


## Example 2 from django-cms
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
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
~~from django.utils.decorators import method_decorator
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
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import get_language_code, get_language_list


## ... source file abbreviated to get to method_decorator examples ...


            'placeholder': plugin_data['placeholder_id'],
            'parent': plugin_data.get('plugin_parent', None),
            'plugin_type': plugin_data['plugin_type'],
            'position': plugin_data['position'],
        }

        response = plugin_instance.add_view(request)

        plugin = getattr(plugin_instance, 'saved_object', None)

        if plugin:
            plugin.placeholder.mark_as_dirty(plugin.language, clear_cache=False)

        if plugin_instance._operation_token:
            tree_order = placeholder.get_plugin_tree_order(plugin.parent_id)
            self._send_post_placeholder_operation(
                request,
                operation=operations.ADD_PLUGIN,
                token=plugin_instance._operation_token,
                plugin=plugin,
                placeholder=plugin.placeholder,
                tree_order=tree_order,
            )
        return response

~~    @method_decorator(require_POST)
    @xframe_options_sameorigin
    @transaction.atomic
    def copy_plugins(self, request):
        source_placeholder_id = request.POST['source_placeholder_id']
        target_language = request.POST['target_language']
        target_placeholder_id = request.POST['target_placeholder_id']
        source_placeholder = get_object_or_404(Placeholder, pk=source_placeholder_id)
        target_placeholder = get_object_or_404(Placeholder, pk=target_placeholder_id)

        if not target_language or not target_language in get_language_list():
            return HttpResponseBadRequest(force_text(_("Language must be set to a supported language!")))

        copy_to_clipboard = target_placeholder.pk == request.toolbar.clipboard.pk
        source_plugin_id = request.POST.get('source_plugin_id', None)

        if copy_to_clipboard and source_plugin_id:
            new_plugin = self._copy_plugin_to_clipboard(
                request,
                source_placeholder,
                target_placeholder,
            )
            new_plugins = [new_plugin]
        elif copy_to_clipboard:
            new_plugin = self._copy_placeholder_to_clipboard(


## ... source file abbreviated to get to method_decorator examples ...


        obj = self._get_plugin_from_id(plugin_id)

        plugin_instance = obj.get_plugin_class_instance(admin=self.admin_site)

        if not self.has_change_plugin_permission(request, obj):
            return HttpResponseForbidden(force_text(_("You do not have permission to edit this plugin")))

        response = plugin_instance.change_view(request, str(plugin_id))

        plugin = getattr(plugin_instance, 'saved_object', None)

        if plugin:
            plugin.placeholder.mark_as_dirty(plugin.language, clear_cache=False)

        if plugin_instance._operation_token:
            self._send_post_placeholder_operation(
                request,
                operation=operations.CHANGE_PLUGIN,
                token=plugin_instance._operation_token,
                old_plugin=obj,
                new_plugin=plugin,
                placeholder=plugin.placeholder,
            )
        return response

~~    @method_decorator(require_POST)
    @xframe_options_sameorigin
    @transaction.atomic
    def move_plugin(self, request):
        try:
            plugin_id = get_int(request.POST.get('plugin_id'))
        except TypeError:
            raise RuntimeError("'plugin_id' is a required parameter.")

        plugin = self._get_plugin_from_id(plugin_id)

        try:
            placeholder_id = get_int(request.POST.get('placeholder_id'))
        except TypeError:
            raise RuntimeError("'placeholder_id' is a required parameter.")
        except ValueError:
            raise RuntimeError("'placeholder_id' must be an integer string.")

        placeholder = Placeholder.objects.get(pk=placeholder_id)

        parent_id = get_int(request.POST.get('plugin_parent', ""), None)
        target_language = request.POST['target_language']
        move_a_copy = request.POST.get('move_a_copy')
        move_a_copy = (move_a_copy and move_a_copy != "0" and
                       move_a_copy.lower() != "false")


## ... source file continues with no further method_decorator examples...

```


## Example 3 from django-import-export
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
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
~~from django.utils.decorators import method_decorator
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


class ImportExportMixinBase:
    def get_model_info(self):
        app_label = self.model._meta.app_label


## ... source file abbreviated to get to method_decorator examples ...


                name='%s_%s_process_import' % info),
            url(r'^import/$',
                self.admin_site.admin_view(self.import_action),
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

~~    @method_decorator(require_POST)
    def process_import(self, request, *args, **kwargs):
        if not self.has_import_permission(request):
            raise PermissionDenied

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


## ... source file continues with no further method_decorator examples...

```


## Example 4 from django-oauth-toolkit
[django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)
([project website](http://dot.evonove.it/) and
[PyPI package information](https://pypi.org/project/django-oauth-toolkit/1.2.0/))
is a code library for adding and handling [OAuth2](https://oauth.net/)
flows within your [Django](/django.html) web application and
[API](/application-programming-interfaces.html).

The django-oauth-toolkit project is open sourced under the
[FreeBSD license](https://github.com/jazzband/django-oauth-toolkit/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-oauth-toolkit / oauth2_provider / views / introspect.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/views/introspect.py)

```python
# introspect.py
import calendar
import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
~~from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.models import get_access_token_model
from oauth2_provider.views import ClientProtectedScopedResourceView


~~@method_decorator(csrf_exempt, name="dispatch")
class IntrospectTokenView(ClientProtectedScopedResourceView):
    required_scopes = ["introspection"]

    @staticmethod
    def get_token_response(token_value=None):
        try:
            token = get_access_token_model().objects.select_related(
                "user", "application"
                ).get(token=token_value)
        except ObjectDoesNotExist:
            return HttpResponse(
                content=json.dumps({"active": False}),
                status=401,
                content_type="application/json"
            )
        else:
            if token.is_valid():
                data = {
                    "active": True,
                    "scope": token.scope,
                    "exp": int(calendar.timegm(token.expires.timetuple())),
                }
                if token.application:
                    data["client_id"] = token.application.client_id


## ... source file continues with no further method_decorator examples...

```


## Example 5 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / views.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./views.py)

```python
# views.py
import re
import six
from collections import Counter

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy

import django
from django.db import DatabaseError
from django.db.models import Count
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
~~from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView

from explorer import app_settings
from explorer.connections import connections
from explorer.exporters import get_exporter_class
from explorer.forms import QueryForm
from explorer.models import Query, QueryLog, MSG_FAILED_BLACKLIST
from explorer.tasks import execute_query
from explorer.utils import (
    url_get_rows,
    url_get_query_id,
    url_get_log_id,
    url_get_params,
    safe_login_prompt,
    fmt_sql,
    allowed_query_pks,
    url_get_show,
    url_get_fullscreen


## ... source file abbreviated to get to method_decorator examples ...


class StreamQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id, *args, **kwargs):
        query = get_object_or_404(Query, pk=query_id)
        return _export(request, query, download=False)


class EmailCsvQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def post(self, request, query_id, *args, **kwargs):
        if request.is_ajax():
            email = request.POST.get('email', None)
            if email:
                execute_query.delay(query_id, email)
                return JsonResponse({'message': 'message was sent successfully'})
        return JsonResponse({}, status=403)


class SchemaView(PermissionRequiredMixin, View):
    permission_required = 'change_permission'

~~    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, *args, **kwargs):
        return super(SchemaView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        connection = kwargs.get('connection')
        if connection not in connections:
            raise Http404
        schema = schema_info(connection)
        if schema:
            return render(None, 'explorer/schema.html',
                                      {'schema': schema_info(connection)})
        else:
            return render(None, 'explorer/schema_building.html')


@require_POST
def format_sql(request):
    sql = request.POST.get('sql', '')
    formatted = fmt_sql(sql)
    return JsonResponse({"formatted": formatted})


class ListQueryView(PermissionRequiredMixin, ExplorerContextMixin, ListView):



## ... source file continues with no further method_decorator examples...

```


## Example 6 from django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).

[**django-wiki / src/wiki / views / article.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/views/article.py)

```python
# article.py
import difflib
import logging
from urllib.parse import urljoin

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
~~from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.utils.translation import ngettext
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic import View
from wiki import editors
from wiki import forms
from wiki import models
from wiki.conf import settings
from wiki.core import permissions
from wiki.core.diff import simple_merge
from wiki.core.exceptions import NoRootURL
from wiki.core.paginator import WikiPaginator
from wiki.core.plugins import registry as plugin_registry
from wiki.core.utils import object_to_json_response
from wiki.decorators import get_article
from wiki.views.mixins import ArticleMixin

log = logging.getLogger(__name__)


class ArticleView(ArticleMixin, TemplateView):

    template_name = "wiki/view.html"

~~    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["selected_tab"] = "view"
        return ArticleMixin.get_context_data(self, **kwargs)


class Create(FormView, ArticleMixin):
    form_class = forms.CreateForm
    template_name = "wiki/create.html"

~~    @method_decorator(get_article(can_write=True, can_create=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        initial = kwargs.get("initial", {})
        initial["slug"] = self.request.GET.get("slug", None)
        kwargs["initial"] = initial
        form = form_class(self.request, self.urlpath, **kwargs)
        form.fields["slug"].widget = forms.TextInputPrepend(
            prepend="/" + self.urlpath.path,
            attrs={
                "pattern": "[a-z0-9_-]+"
                if not settings.URL_CASE_SENSITIVE
                else "[a-zA-Z0-9_-]+",
                "title": "Lowercase letters, numbers, hyphens and underscores"
                if not settings.URL_CASE_SENSITIVE
                else "Letters, numbers, hyphens and underscores",
            },
        )
        return form



## ... source file abbreviated to get to method_decorator examples ...


                messages.error(
                    self.request, _("There was an error creating this article.")
                )
            return redirect("wiki:get", "")

        return self.get_success_url()

    def get_success_url(self):
        return redirect("wiki:get", self.newpath.path)

    def get_context_data(self, **kwargs):
        c = ArticleMixin.get_context_data(self, **kwargs)
        c["form"] = self.get_form()
        c["parent_urlpath"] = self.urlpath
        c["parent_article"] = self.article
        c["create_form"] = c.pop("form", None)
        c["editor"] = editors.getEditor()
        return c


class Delete(FormView, ArticleMixin):

    form_class = forms.DeleteForm
    template_name = "wiki/delete.html"

~~    @method_decorator(get_article(can_write=True, not_locked=True, can_delete=True))
    def dispatch(self, request, article, *args, **kwargs):
        return self.dispatch1(request, article, *args, **kwargs)

    def dispatch1(self, request, article, *args, **kwargs):
        urlpath = kwargs.get("urlpath", None)
        self.next = ""
        self.cannot_delete_root = False
        if urlpath and urlpath.parent:
            self.next = reverse("wiki:get", kwargs={"path": urlpath.parent.path})
        elif urlpath:
            self.cannot_delete_root = True
        else:
            for art_obj in article.articleforobject_set.filter(is_mptt=True):
                if art_obj.content_object.parent:
                    self.next = reverse(
                        "wiki:get",
                        kwargs={"article_id": art_obj.content_object.parent.article.id},
                    )
                else:
                    self.cannot_delete_root = True

        return super().dispatch(request, article, *args, **kwargs)

    def get_initial(self):


## ... source file abbreviated to get to method_decorator examples ...


        return self.get_success_url()

    def get_success_url(self):
        return redirect(self.next)

    def get_context_data(self, **kwargs):
        cannot_delete_children = False
        if self.children_slice and not self.article.can_moderate(self.request.user):
            cannot_delete_children = True

        kwargs["delete_form"] = self.get_form()
        kwargs["form"] = kwargs["delete_form"]
        kwargs["cannot_delete_root"] = self.cannot_delete_root
        kwargs["delete_children"] = self.children_slice[:20]
        kwargs["delete_children_more"] = len(self.children_slice) > 20
        kwargs["cannot_delete_children"] = cannot_delete_children
        return super().get_context_data(**kwargs)


class Edit(ArticleMixin, FormView):


    form_class = forms.EditForm
    template_name = "wiki/edit.html"

~~    @method_decorator(get_article(can_write=True, not_locked=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.orig_content = kwargs.pop("content", None)
        self.sidebar_plugins = plugin_registry.get_sidebar()
        self.sidebar = []
        return super().dispatch(request, article, *args, **kwargs)

    def get_initial(self):
        initial = FormView.get_initial(self)

        for field_name in ["title", "content"]:
            session_key = "unsaved_article_%s_%d" % (field_name, self.article.id)
            if session_key in self.request.session:
                content = self.request.session[session_key]
                initial[field_name] = content
                del self.request.session[session_key]
        return initial

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        if (
            self.request.POST.get("save", "") != "1"
            and self.request.POST.get("preview") != "1"


## ... source file abbreviated to get to method_decorator examples ...


        self.article.add_revision(revision)
        messages.success(
            self.request, _("A new revision of the article was successfully added.")
        )
        return self.get_success_url()

    def get_success_url(self):
        if self.urlpath:
            return redirect("wiki:get", path=self.urlpath.path)
        return redirect("wiki:get", article_id=self.article.id)

    def get_context_data(self, **kwargs):
        kwargs["form"] = self.get_form()
        kwargs["edit_form"] = kwargs["form"]
        kwargs["editor"] = editors.getEditor()
        kwargs["selected_tab"] = "edit"
        kwargs["sidebar"] = self.sidebar
        return super().get_context_data(**kwargs)


class Move(ArticleMixin, FormView):

    form_class = forms.MoveForm
    template_name = "wiki/move.html"

~~    @method_decorator(login_required)
~~    @method_decorator(get_article(can_write=True, not_locked=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        return form_class(**kwargs)

    def get_context_data(self, **kwargs):
        kwargs["form"] = self.get_form()
        kwargs["root_path"] = models.URLPath.root()
        return super().get_context_data(**kwargs)

    @transaction.atomic
    def form_valid(self, form):
        if not self.urlpath.parent:
            messages.error(
                self.request,
                _("This article cannot be moved because it is a root article."),
            )
            return redirect("wiki:get", article_id=self.article.id)

        dest_path = get_object_or_404(


## ... source file abbreviated to get to method_decorator examples ...


                    _("Created redirect (auto)"),
                )
                urlpath_new.moved_to = descendant
                urlpath_new.save()

            messages.success(
                self.request,
                ngettext(
                    "Article successfully moved! Created {n} redirect.",
                    "Article successfully moved! Created {n} redirects.",
                    len(descendants),
                ).format(n=len(descendants)),
            )

        else:
            messages.success(self.request, _("Article successfully moved!"))
        return redirect("wiki:get", path=self.urlpath.path)


class Deleted(Delete):


    template_name = "wiki/deleted.html"
    form_class = forms.DeleteForm

~~    @method_decorator(get_article(can_read=True, deleted_contents=True))
    def dispatch(self, request, article, *args, **kwargs):

        self.urlpath = kwargs.get("urlpath", None)
        self.article = article

        if self.urlpath:
            deleted_ancestor = self.urlpath.first_deleted_ancestor()
            if deleted_ancestor is None:
                return redirect("wiki:get", path=self.urlpath.path)
            elif deleted_ancestor != self.urlpath:
                return redirect("wiki:deleted", path=deleted_ancestor.path)

        else:
            if not article.current_revision.deleted:
                return redirect("wiki:get", article_id=article.id)

        if request.GET.get("restore", False):
            can_restore = not article.current_revision.locked and article.can_delete(
                request.user
            )
            can_restore = can_restore or article.can_moderate(request.user)

            if can_restore:
                revision = models.ArticleRevision()


## ... source file abbreviated to get to method_decorator examples ...


                    _('The article "%s" and its children are now restored.')
                    % revision.title,
                )
                if self.urlpath:
                    return redirect("wiki:get", path=self.urlpath.path)
                else:
                    return redirect("wiki:get", article_id=article.id)

        return super().dispatch1(request, article, *args, **kwargs)

    def get_initial(self):
        return {
            "revision": self.article.current_revision,
            "purge": True,
        }

    def get_context_data(self, **kwargs):
        kwargs["purge_form"] = self.get_form()
        kwargs["form"] = kwargs["purge_form"]
        return super().get_context_data(**kwargs)


class Source(ArticleMixin, TemplateView):
    template_name = "wiki/source.html"

~~    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["selected_tab"] = "source"
        return super().get_context_data(**kwargs)


class History(ListView, ArticleMixin):

    template_name = "wiki/history.html"
    allow_empty = True
    context_object_name = "revisions"
    paginator_class = WikiPaginator
    paginate_by = 10

    def get_queryset(self):
        return models.ArticleRevision.objects.filter(article=self.article).order_by(
            "-created"
        )

    def get_context_data(self, **kwargs):
        kwargs_article = ArticleMixin.get_context_data(self, **kwargs)
        kwargs_listview = ListView.get_context_data(self, **kwargs)
        kwargs.update(kwargs_article)
        kwargs.update(kwargs_listview)
        kwargs["selected_tab"] = "history"
        return kwargs

~~    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)


class Dir(ListView, ArticleMixin):

    template_name = "wiki/dir.html"
    allow_empty = True
    context_object_name = "directory"
    model = models.URLPath
    paginator_class = WikiPaginator
    paginate_by = 30

~~    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.filter_form = forms.DirFilterForm(request.GET)
        if self.filter_form.is_valid():
            self.query = self.filter_form.cleaned_data["query"]
        else:
            self.query = None
        return super().dispatch(request, article, *args, **kwargs)

    def get_queryset(self):
        children = self.urlpath.get_children().can_read(self.request.user)
        if self.query:
            children = children.filter(
                Q(article__current_revision__title__icontains=self.query)
                | Q(slug__icontains=self.query)
            )
        if not self.article.can_moderate(self.request.user):
            children = children.active()
        children = children.select_related_common().order_by(
            "article__current_revision__title"
        )
        return children

    def get_context_data(self, **kwargs):
        kwargs_article = ArticleMixin.get_context_data(self, **kwargs)


## ... source file abbreviated to get to method_decorator examples ...


            articles = articles.active().can_read(self.request.user)
        return articles.order_by("-current_revision__created")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["search_form"] = self.search_form
        kwargs["search_query"] = self.query
        kwargs["urlpath"] = self.urlpath
        return kwargs


class Plugin(View):
    def dispatch(self, request, path=None, slug=None, **kwargs):
        kwargs["path"] = path
        for plugin in list(plugin_registry.get_plugins().values()):
            if getattr(plugin, "slug", None) == slug:
                return plugin.article_view(request, **kwargs)
        raise Http404()


class Settings(ArticleMixin, TemplateView):

    permission_form_class = forms.PermissionsForm
    template_name = "wiki/settings.html"

~~    @method_decorator(login_required)
~~    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_form_classes(self):
        settings_forms = []
        if permissions.can_change_permissions(self.article, self.request.user):
            settings_forms.append(self.permission_form_class)
        plugin_forms = [F for F in plugin_registry.get_settings_forms()]
        plugin_forms.sort(key=lambda form: form.settings_order)
        settings_forms += plugin_forms
        for i in range(len(settings_forms)):
            setattr(settings_forms[i], "action", "form%d" % i)

        return settings_forms

    def post(self, *args, **kwargs):
        self.forms = []
        for form_class in self.get_form_classes():
            if form_class.action == self.request.GET.get("f", None):
                form = form_class(self.article, self.request, self.request.POST)
                if form.is_valid():
                    form.save()
                    usermessage = form.get_usermessage()
                    if usermessage:


## ... source file abbreviated to get to method_decorator examples ...


    def get(self, *args, **kwargs):
        self.forms = []

        new_article = models.Article.objects.get(id=self.article.id)

        for Form in self.get_form_classes():
            self.forms.append(Form(new_article, self.request))

        return super().get(*args, **kwargs)

    def get_success_url(self):
        if self.urlpath:
            return redirect("wiki:settings", path=self.urlpath.path)
        return redirect("wiki:settings", article_id=self.article.id)

    def get_context_data(self, **kwargs):
        kwargs["selected_tab"] = "settings"
        kwargs["forms"] = self.forms
        return super().get_context_data(**kwargs)


class ChangeRevisionView(RedirectView):

    permanent = False

~~    @method_decorator(get_article(can_write=True, not_locked=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.article = article
        self.urlpath = kwargs.pop("kwargs", False)
        self.change_revision()

        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        if self.urlpath:
            return reverse("wiki:history", kwargs={"path": self.urlpath.path})
        else:
            return reverse("wiki:history", kwargs={"article_id": self.article.id})

    def change_revision(self):
        revision = get_object_or_404(
            models.ArticleRevision, article=self.article, id=self.kwargs["revision_id"]
        )
        self.article.current_revision = revision
        self.article.save()
        messages.success(
            self.request,
            _(
                "The article %(title)s is now set to display revision #%(revision_number)d"
            )
            % {"title": revision.title, "revision_number": revision.revision_number},
        )


class Preview(ArticleMixin, TemplateView):

    template_name = "wiki/preview_inline.html"

~~    @method_decorator(xframe_options_sameorigin)
~~    @method_decorator(get_article(can_read=True, deleted_contents=True))
    def dispatch(self, request, article, *args, **kwargs):
        revision_id = request.GET.get("r", None)
        self.title = None
        self.content = None
        self.preview = False
        if revision_id:
            try:
                revision_id = int(revision_id)
            except ValueError:
                raise Http404()
            self.revision = get_object_or_404(
                models.ArticleRevision, article=article, id=revision_id
            )
        else:
            self.revision = None
        return super().dispatch(request, article, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        edit_form = forms.EditForm(
            request, self.article.current_revision, request.POST, preview=True
        )
        if edit_form.is_valid():
            self.title = edit_form.cleaned_data["title"]
            self.content = edit_form.cleaned_data["content"]


## ... source file abbreviated to get to method_decorator examples ...


        other_revision = revision.previous_revision

        baseText = other_revision.content if other_revision is not None else ""
        newText = revision.content

        differ = difflib.Differ(charjunk=difflib.IS_CHARACTER_JUNK)
        diff = differ.compare(
            baseText.splitlines(keepends=True), newText.splitlines(keepends=True)
        )
        other_changes = []

        if not other_revision or other_revision.title != revision.title:
            other_changes.append((_("New title"), revision.title))

        return object_to_json_response(
            {"diff": list(diff), "other_changes": other_changes}
        )


class MergeView(View):
    preview = False
    template_name = "wiki/preview_inline.html"
    template_error_name = "wiki/error.html"
    urlpath = None

~~    @method_decorator(get_article(can_write=True))
    def dispatch(self, request, article, revision_id, *args, **kwargs):
        return super().dispatch(request, article, revision_id, *args, **kwargs)

    def get(self, request, article, revision_id, *args, **kwargs):
        revision = get_object_or_404(
            models.ArticleRevision, article=article, id=revision_id
        )

        current_text = (
            article.current_revision.content if article.current_revision else ""
        )
        new_text = revision.content

        content = simple_merge(current_text, new_text)

        if not self.preview:
            old_revision = article.current_revision

            if revision.deleted:
                c = {
                    "error_msg": _("You cannot merge with a deleted revision"),
                    "article": article,
                    "urlpath": self.urlpath,
                }


## ... source file continues with no further method_decorator examples...

```

