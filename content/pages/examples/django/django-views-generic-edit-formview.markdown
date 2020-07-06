title: django.views.generic.edit FormView Example Code
category: page
slug: django-views-generic-edit-formview-examples
sortorder: 500011538
toc: False
sidebartitle: django.views.generic.edit FormView
meta: Python example code for the FormView class from the django.views.generic.edit module of the Django project.


FormView is a class within the django.views.generic.edit module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / views.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/views.py)

```python
# views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
~~from django.views.generic.edit import FormView

from ..account import app_settings as account_settings
from ..account.adapter import get_adapter as get_account_adapter
from ..account.views import (
    AjaxCapableProcessFormViewMixin,
    CloseableSignupMixin,
    RedirectAuthenticatedUserMixin,
)
from ..utils import get_form_class
from . import app_settings, helpers
from .adapter import get_adapter
from .forms import DisconnectForm, SignupForm
from .models import SocialAccount, SocialLogin


class SignupView(RedirectAuthenticatedUserMixin, CloseableSignupMixin,
~~                 AjaxCapableProcessFormViewMixin, FormView):
    form_class = SignupForm
    template_name = (
        'socialaccount/signup.' + account_settings.TEMPLATE_EXTENSION)

    def get_form_class(self):
        return get_form_class(app_settings.FORMS,
                              'signup',
                              self.form_class)

    def dispatch(self, request, *args, **kwargs):
        self.sociallogin = None
        data = request.session.get('socialaccount_sociallogin')
        if data:
            self.sociallogin = SocialLogin.deserialize(data)
        if not self.sociallogin:
            return HttpResponseRedirect(reverse('account_login'))
        return super(SignupView, self).dispatch(request, *args, **kwargs)

    def is_open(self):
        return get_adapter(self.request).is_open_for_signup(
            self.request,
            self.sociallogin)

    def get_form_kwargs(self):


## ... source file abbreviated to get to FormView examples ...



    def get_authenticated_redirect_url(self):
        return reverse(connections)


signup = SignupView.as_view()


class LoginCancelledView(TemplateView):
    template_name = (
        "socialaccount/login_cancelled." + account_settings.TEMPLATE_EXTENSION)


login_cancelled = LoginCancelledView.as_view()


class LoginErrorView(TemplateView):
    template_name = (
        "socialaccount/authentication_error." +
        account_settings.TEMPLATE_EXTENSION)


login_error = LoginErrorView.as_view()


~~class ConnectionsView(AjaxCapableProcessFormViewMixin, FormView):
    template_name = (
        "socialaccount/connections." +
        account_settings.TEMPLATE_EXTENSION)
    form_class = DisconnectForm
    success_url = reverse_lazy("socialaccount_connections")

    def get_form_class(self):
        return get_form_class(app_settings.FORMS,
                              'disconnect',
                              self.form_class)

    def get_form_kwargs(self):
        kwargs = super(ConnectionsView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        get_account_adapter().add_message(self.request,
                                          messages.INFO,
                                          'socialaccount/messages/'
                                          'account_disconnected.txt')
        form.save()
        return super(ConnectionsView, self).form_valid(form)



## ... source file continues with no further FormView examples...

```


## Example 2 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / mixins.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./mixins.py)

```python
# mixins.py
from django.http import HttpResponse
from django.utils.timezone import now
~~from django.views.generic.edit import FormView

from .formats import base_formats
from .forms import ExportForm
from .resources import modelresource_factory
from .signals import post_export


class ExportViewMixin:
    formats = base_formats.DEFAULT_FORMATS
    form_class = ExportForm
    resource_class = None

    def get_export_formats(self):
        return [f for f in self.formats if f().can_export()]

    def get_resource_class(self):
        if not self.resource_class:
            return modelresource_factory(self.model)
        return self.resource_class

    def get_export_resource_class(self):
        return self.get_resource_class()

    def get_resource_kwargs(self, request, *args, **kwargs):


## ... source file abbreviated to get to FormView examples ...



    def get_export_data(self, file_format, queryset, *args, **kwargs):
        resource_class = self.get_export_resource_class()
        data = resource_class(**self.get_export_resource_kwargs(self.request))\
            .export(queryset, *args, **kwargs)
        export_data = file_format.export_data(data)
        return export_data

    def get_export_filename(self, file_format):
        date_str = now().strftime('%Y-%m-%d')
        filename = "%s-%s.%s" % (self.model.__name__,
                                 date_str,
                                 file_format.get_extension())
        return filename

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['formats'] = self.get_export_formats()
        return kwargs


~~class ExportViewFormMixin(ExportViewMixin, FormView):
    def form_valid(self, form):
        formats = self.get_export_formats()
        file_format = formats[
            int(form.cleaned_data['file_format'])
        ]()
        if hasattr(self, 'get_filterset'):
            queryset = self.get_filterset(self.get_filterset_class()).qs
        else:
            queryset = self.get_queryset()
        export_data = self.get_export_data(file_format, queryset)
        content_type = file_format.get_content_type()
        try:
            response = HttpResponse(export_data, content_type=content_type)
        except TypeError:
            response = HttpResponse(export_data, mimetype=content_type)
        response['Content-Disposition'] = 'attachment; filename="%s"' % (
            self.get_export_filename(file_format),
        )

        post_export.send(sender=None, model=self.model)
        return response



## ... source file continues with no further FormView examples...

```


## Example 3 from django-mongonaut
[django-mongonaut](https://github.com/jazzband/django-mongonaut)
([project documentation](https://django-mongonaut.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-mongonaut/))
provides an introspective interface for working with
[MongoDB](/mongodb.html) via mongoengine. The project has its own new code
to map MongoDB to the [Django](/django.html) Admin interface.

django-mongonaut's highlighted features include automatic introspection of
mongoengine documents, the ability to constrain who sees what and what
they can do and full control for adding, editing and deleting documents.

The django-mongonaut project is open sourced under the
[MIT License](https://github.com/jazzband/django-mongonaut/blob/master/LICENSE.txt)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-mongonaut / mongonaut / views.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/./views.py)

```python
# views.py
import math

from django.contrib import messages
from django.urls import reverse
from django.forms import Form
from django.http import HttpResponseForbidden
from django.http import Http404
from django.utils.functional import cached_property
from django.views.generic.edit import DeletionMixin
from django.views.generic import ListView
from django.views.generic import TemplateView
~~from django.views.generic.edit import FormView
from mongoengine.fields import EmbeddedDocumentField, ListField

from mongonaut.forms import MongoModelForm
from mongonaut.mixins import MongonautFormViewMixin
from mongonaut.mixins import MongonautViewMixin
from mongonaut.utils import is_valid_object_id


class IndexView(MongonautViewMixin, ListView):

    template_name = "mongonaut/index.html"
    queryset = []
    permission = 'has_view_permission'

    def get_queryset(self):
        return self.get_mongoadmins()


~~class DocumentListView(MongonautViewMixin, FormView):
    form_class = Form
    success_url = '/'
    template_name = "mongonaut/document_list.html"
    permission = 'has_view_permission'

    documents_per_page = 25


    def get_qset(self, queryset, q):
        if self.mongoadmin.search_fields and q:
            params = {}
            for field in self.mongoadmin.search_fields:
                if field == 'id':
                    if is_valid_object_id(q):
                        return queryset.filter(pk=q)
                    continue
                search_key = "{field}__icontains".format(field=field)
                params[search_key] = q

            queryset = queryset.filter(**params)
        return queryset

    @cached_property
    def get_queryset(self):


## ... source file continues with no further FormView examples...

```

