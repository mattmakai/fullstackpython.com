title: django.views.generic.base View Example Code
category: page
slug: django-views-generic-base-view-examples
sortorder: 500011532
toc: False
sidebartitle: django.views.generic.base View
meta: Python example code for the View class from the django.views.generic.base module of the Django project.


View is a class within the django.views.generic.base module of the Django project.


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
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
~~from django.views.generic.base import TemplateResponseMixin, TemplateView, View
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


## ... source file abbreviated to get to View examples ...


    def get_context_data(self, **kwargs):
        ret = super(SignupView, self).get_context_data(**kwargs)
        form = ret['form']
        email = self.request.session.get('account_verified_email')
        if email:
            email_keys = ['email']
            if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
                email_keys.append('email2')
            for email_key in email_keys:
                form.fields[email_key].initial = email
        login_url = passthrough_next_redirect_url(self.request,
                                                  reverse("account_login"),
                                                  self.redirect_field_name)
        redirect_field_name = self.redirect_field_name
        redirect_field_value = get_request_param(self.request,
                                                 redirect_field_name)
        ret.update({"login_url": login_url,
                    "redirect_field_name": redirect_field_name,
                    "redirect_field_value": redirect_field_value})
        return ret


signup = SignupView.as_view()


~~class ConfirmEmailView(TemplateResponseMixin, View):

    template_name = "account/email_confirm." + app_settings.TEMPLATE_EXTENSION

    def get(self, *args, **kwargs):
        try:
            self.object = self.get_object()
            if app_settings.CONFIRM_EMAIL_ON_GET:
                return self.post(*args, **kwargs)
        except Http404:
            self.object = None
        ctx = self.get_context_data()
        return self.render_to_response(ctx)

    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        get_adapter(self.request).add_message(
            self.request,
            messages.SUCCESS,
            'account/messages/email_confirmed.txt',
            {'email': confirmation.email_address.email})
        if app_settings.LOGIN_ON_EMAIL_CONFIRMATION:
            resp = self.login_on_confirm(confirmation)
            if resp is not None:


## ... source file abbreviated to get to View examples ...


            'account/messages/password_changed.txt')
        signals.password_reset.send(sender=self.reset_user.__class__,
                                    request=self.request,
                                    user=self.reset_user)

        if app_settings.LOGIN_ON_PASSWORD_RESET:
            return perform_login(
                self.request, self.reset_user,
                email_verification=app_settings.EMAIL_VERIFICATION)

        return super(PasswordResetFromKeyView, self).form_valid(form)


password_reset_from_key = PasswordResetFromKeyView.as_view()


class PasswordResetFromKeyDoneView(TemplateView):
    template_name = (
        "account/password_reset_from_key_done." +
        app_settings.TEMPLATE_EXTENSION)


password_reset_from_key_done = PasswordResetFromKeyDoneView.as_view()


~~class LogoutView(TemplateResponseMixin, View):

    template_name = "account/logout." + app_settings.TEMPLATE_EXTENSION
    redirect_field_name = "next"

    def get(self, *args, **kwargs):
        if app_settings.LOGOUT_ON_GET:
            return self.post(*args, **kwargs)
        if not self.request.user.is_authenticated:
            response = redirect(self.get_redirect_url())
            return _ajax_response(self.request, response)
        ctx = self.get_context_data()
        response = self.render_to_response(ctx)
        return _ajax_response(self.request, response)

    def post(self, *args, **kwargs):
        url = self.get_redirect_url()
        if self.request.user.is_authenticated:
            self.logout()
        response = redirect(url)
        return _ajax_response(self.request, response)

    def logout(self):
        adapter = get_adapter(self.request)
        adapter.add_message(


## ... source file continues with no further View examples...

```


## Example 2 from django-downloadview
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

[**django-downloadview / django_downloadview / views / base.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/views/base.py)

```python
# base.py
import calendar

from django.http import Http404, HttpResponseNotModified
~~from django.views.generic.base import View
from django.views.static import was_modified_since

from django_downloadview import exceptions
from django_downloadview.response import DownloadResponse


class DownloadMixin(object):

    response_class = DownloadResponse

    attachment = True

    basename = None

    mimetype = None

    encoding = None

    def get_file(self):
        raise NotImplementedError()

    def get_basename(self):
        return self.basename



## ... source file abbreviated to get to View examples ...



    def download_response(self, *response_args, **response_kwargs):
        response_kwargs.setdefault("file_instance", self.file_instance)
        response_kwargs.setdefault("attachment", self.attachment)
        response_kwargs.setdefault("basename", self.get_basename())
        response_kwargs.setdefault("file_mimetype", self.get_mimetype())
        response_kwargs.setdefault("file_encoding", self.get_encoding())
        response = self.response_class(*response_args, **response_kwargs)
        return response

    def file_not_found_response(self):
        raise Http404()

    def render_to_response(self, *response_args, **response_kwargs):
        try:
            self.file_instance = self.get_file()
        except exceptions.FileNotFound:
            return self.file_not_found_response()
        since = self.request.META.get("HTTP_IF_MODIFIED_SINCE", None)
        if since is not None:
            if not self.was_modified_since(self.file_instance, since):
                return self.not_modified_response(**response_kwargs)
        return self.download_response(*response_args, **response_kwargs)


~~class BaseDownloadView(DownloadMixin, View):

    def get(self, request, *args, **kwargs):
        return self.render_to_response()



## ... source file continues with no further View examples...

```


## Example 3 from django-sql-explorer
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
from django.utils.decorators import method_decorator
from django.views.generic import ListView
~~from django.views.generic.base import View
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
)



## ... source file abbreviated to get to View examples ...




class SafeLoginView(LoginView):
    template_name = 'admin/login.html'


def _export(request, query, download=True):
    format = request.GET.get('format', 'csv')
    exporter_class = get_exporter_class(format)
    query.params = url_get_params(request)
    delim = request.GET.get('delim')
    exporter = exporter_class(query)
    try:
        output = exporter.get_output(delim=delim)
    except DatabaseError as e:
        msg = "Error executing query %s: %s" % (query.title, e)
        return HttpResponse(msg, status=500)
    response = HttpResponse(output, content_type=exporter.content_type)
    if download:
        response['Content-Disposition'] = 'attachment; filename="%s"' % (
            exporter.get_filename()
        )
    return response


~~class DownloadQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id, *args, **kwargs):
        query = get_object_or_404(Query, pk=query_id)
        return _export(request, query)


~~class DownloadFromSqlView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def post(self, request, *args, **kwargs):
        sql = request.POST.get('sql')
        connection = request.POST.get('connection')
        query = Query(sql=sql, connection=connection, title='')
        ql = query.log(request.user)
        query.title = 'Playground - %s' % ql.id
        return _export(request, query)


~~class StreamQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id, *args, **kwargs):
        query = get_object_or_404(Query, pk=query_id)
        return _export(request, query, download=False)


~~class EmailCsvQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def post(self, request, query_id, *args, **kwargs):
        if request.is_ajax():
            email = request.POST.get('email', None)
            if email:
                execute_query.delay(query_id, email)
                return JsonResponse({'message': 'message was sent successfully'})
        return JsonResponse({}, status=403)


~~class SchemaView(PermissionRequiredMixin, View):
    permission_required = 'change_permission'

    @method_decorator(xframe_options_sameorigin)
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



## ... source file abbreviated to get to View examples ...



    context_object_name = "recent_logs"
    model = QueryLog
    paginate_by = 20


class CreateQueryView(PermissionRequiredMixin, ExplorerContextMixin, CreateView):

    permission_required = 'change_permission'

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user
        return super(CreateQueryView, self).form_valid(form)

    form_class = QueryForm
    template_name = 'explorer/query.html'


class DeleteQueryView(PermissionRequiredMixin, ExplorerContextMixin, DeleteView):

    permission_required = 'change_permission'
    model = Query
    success_url = reverse_lazy("explorer_index")


~~class PlayQueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'change_permission'

    def get(self, request):
        if url_get_query_id(request):
            query = get_object_or_404(Query, pk=url_get_query_id(request))
            return self.render_with_sql(request, query, run_query=False)

        if url_get_log_id(request):
            log = get_object_or_404(QueryLog, pk=url_get_log_id(request))
            query = Query(sql=log.sql, title="Playground", connection=log.connection)
            return self.render_with_sql(request, query)

        return self.render()

    def post(self, request):
        sql = request.POST.get('sql')
        show = url_get_show(request)
        query = Query(sql=sql, title="Playground", connection=request.POST.get('connection'))
        passes_blacklist, failing_words = query.passes_blacklist()
        error = MSG_FAILED_BLACKLIST % ', '.join(failing_words) if not passes_blacklist else None
        run_query = not bool(error) if show else False
        return self.render_with_sql(request, query, run_query=run_query, error=error)

    def render(self):
        return self.render_template('explorer/play.html', {'title': 'Playground', 'form': QueryForm()})

    def render_with_sql(self, request, query, run_query=True, error=None):
        rows = url_get_rows(request)
        fullscreen = url_get_fullscreen(request)
        template = 'fullscreen' if fullscreen else 'play'
        form = QueryForm(request.POST if len(request.POST) else None, instance=query)
        return self.render_template('explorer/%s.html' % template, query_viewmodel(request.user,
                                                                                   query,
                                                                                   title="Playground",
                                                                                   run_query=run_query,
                                                                                   error=error,
                                                                                   rows=rows,
                                                                                   form=form))


~~class QueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id):
        query, form = QueryView.get_instance_and_form(request, query_id)
        query.save()  # updates the modified date
        show = url_get_show(request)
        rows = url_get_rows(request)
        vm = query_viewmodel(request.user, query, form=form, run_query=show, rows=rows)
        fullscreen = url_get_fullscreen(request)
        template = 'fullscreen' if fullscreen else 'query'
        return self.render_template('explorer/%s.html' % template, vm)

    def post(self, request, query_id):
        if not app_settings.EXPLORER_PERMISSION_CHANGE(request.user):
            return HttpResponseRedirect(
                reverse_lazy('query_detail', kwargs={'query_id': query_id})
            )
        show = url_get_show(request)
        query, form = QueryView.get_instance_and_form(request, query_id)
        success = form.is_valid() and form.save()
        vm = query_viewmodel(request.user,
                             query,
                             form=form,


## ... source file continues with no further View examples...

```

