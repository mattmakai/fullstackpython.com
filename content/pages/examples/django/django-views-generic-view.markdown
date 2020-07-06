title: django.views.generic View Example Code
category: page
slug: django-views-generic-view-examples
sortorder: 500011528
toc: False
sidebartitle: django.views.generic View
meta: Python example code for the View class from the django.views.generic module of the Django project.


View is a class within the django.views.generic module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / views / upload.py**](https://github.com/jrief/django-angular/blob/master/djng/views/upload.py)

```python
# upload.py
from django.core.exceptions import SuspiciousMultipartForm
from django.core import signing
~~from django.views.generic import View
from django.http import JsonResponse

from djng import app_settings
from djng.forms.fields import FileField, ImageField


~~class FileUploadView(View):
    storage = app_settings.upload_storage
    thumbnail_size = app_settings.THUMBNAIL_OPTIONS
    signer = signing.Signer()

    def post(self, request, *args, **kwargs):
        if request.POST.get('filetype') == 'file':
            field = FileField
        elif request.POST.get('filetype') == 'image':
            field = ImageField
        else:
            raise SuspiciousMultipartForm("Missing attribute 'filetype' in form data.")
        data = {}
        for name, file_obj in request.FILES.items():
            data[name] = field.preview(file_obj)
        return JsonResponse(data)



## ... source file continues with no further View examples...

```


## Example 2 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / views.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./views.py)

```python
# views.py
from django.core.exceptions import ImproperlyConfigured
~~from django.views.generic import View
from django.views.generic.list import (
    MultipleObjectMixin,
    MultipleObjectTemplateResponseMixin
)

from .constants import ALL_FIELDS
from .filterset import filterset_factory
from .utils import MigrationNotice, RenameAttributesBase


class FilterMixinRenames(RenameAttributesBase):
    renamed_attributes = (
        ('filter_fields', 'filterset_fields', MigrationNotice),
    )


class FilterMixin(metaclass=FilterMixinRenames):
    filterset_class = None
    filterset_fields = ALL_FIELDS
    strict = True

    def get_filterset_class(self):
        if self.filterset_class:
            return self.filterset_class


## ... source file abbreviated to get to View examples ...


        kwargs = self.get_filterset_kwargs(filterset_class)
        return filterset_class(**kwargs)

    def get_filterset_kwargs(self, filterset_class):
        kwargs = {
            'data': self.request.GET or None,
            'request': self.request,
        }
        try:
            kwargs.update({
                'queryset': self.get_queryset(),
            })
        except ImproperlyConfigured:
            if filterset_class._meta.model is None:
                msg = ("'%s' does not define a 'model' and the view '%s' does "
                       "not return a valid queryset from 'get_queryset'.  You "
                       "must fix one of them.")
                args = (filterset_class.__name__, self.__class__.__name__)
                raise ImproperlyConfigured(msg % args)
        return kwargs

    def get_strict(self):
        return self.strict


~~class BaseFilterView(FilterMixin, MultipleObjectMixin, View):

    def get(self, request, *args, **kwargs):
        filterset_class = self.get_filterset_class()
        self.filterset = self.get_filterset(filterset_class)

        if not self.filterset.is_bound or self.filterset.is_valid() or not self.get_strict():
            self.object_list = self.filterset.qs
        else:
            self.object_list = self.filterset.queryset.none()

        context = self.get_context_data(filter=self.filterset,
                                        object_list=self.object_list)
        return self.render_to_response(context)


class FilterView(MultipleObjectTemplateResponseMixin, BaseFilterView):
    template_name_suffix = '_filter'


def object_filter(request, model=None, queryset=None, template_name=None,
                  extra_context=None, context_processors=None,
                  filter_class=None):
    class ECFilterView(FilterView):
        def get_context_data(self, **kwargs):


## ... source file continues with no further View examples...

```


## Example 3 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / views / generic.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/views/generic.py)

```python
# generic.py
~~from django.views.generic import View

from ..settings import oauth2_settings
from .mixins import (
    ClientProtectedResourceMixin, OAuthLibMixin, ProtectedResourceMixin,
    ReadWriteScopedResourceMixin, ScopedResourceMixin
)


class InitializationMixin(OAuthLibMixin):


    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS


~~class ProtectedResourceView(ProtectedResourceMixin, InitializationMixin, View):
    pass


class ScopedProtectedResourceView(ScopedResourceMixin, ProtectedResourceView):
    pass


class ReadWriteScopedResourceView(ReadWriteScopedResourceMixin, ProtectedResourceView):
    pass


~~class ClientProtectedResourceView(ClientProtectedResourceMixin, InitializationMixin, View):


    pass


class ClientProtectedScopedResourceView(ScopedResourceMixin, ClientProtectedResourceView):


    pass



## ... source file continues with no further View examples...

```


## Example 4 from django-rest-framework
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

[**django-rest-framework / rest_framework / compat.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./compat.py)

```python
# compat.py
from django.conf import settings
~~from django.views.generic import View


def unicode_http_header(value):
    if isinstance(value, bytes):
        return value.decode('iso-8859-1')
    return value


def distinct(queryset, base):
    if settings.DATABASES[queryset.db]["ENGINE"] == "django.db.backends.oracle":
        return base.filter(pk__in=set(queryset.values_list('pk', flat=True)))
    return queryset.distinct()


try:
    from django.contrib.postgres import fields as postgres_fields
except ImportError:
    postgres_fields = None


try:
    import coreapi
except ImportError:
    coreapi = None

try:
    import uritemplate
except ImportError:
    uritemplate = None


try:
    import coreschema
except ImportError:
    coreschema = None


try:
    import yaml
except ImportError:
    yaml = None


try:
    import requests
except ImportError:
    requests = None


~~if 'patch' not in View.http_method_names:
~~    View.http_method_names = View.http_method_names + ['patch']


try:
    import markdown

    HEADERID_EXT_PATH = 'markdown.extensions.toc'
    LEVEL_PARAM = 'baselevel'

    def apply_markdown(text):
        extensions = [HEADERID_EXT_PATH]
        extension_configs = {
            HEADERID_EXT_PATH: {
                LEVEL_PARAM: '2'
            }
        }
        md = markdown.Markdown(
            extensions=extensions, extension_configs=extension_configs
        )
        md_filter_add_syntax_highlight(md)
        return md.convert(text)
except ImportError:
    apply_markdown = None
    markdown = None



## ... source file continues with no further View examples...

```


## Example 5 from django-wiki
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

[**django-wiki / src/wiki / views / accounts.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/views/accounts.py)

```python
# accounts.py
from django.conf import settings as django_settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import UpdateView
~~from django.views.generic import View
from wiki import forms
from wiki.conf import settings

User = get_user_model()


class Signup(CreateView):
    model = User
    form_class = forms.UserCreationForm
    template_name = "wiki/accounts/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous and not request.user.is_superuser:
            return redirect("wiki:root")
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.SIGNUP_URL)
        if not request.user.is_superuser and not settings.ACCOUNT_SIGNUP_ALLOWED:
            c = {"error_msg": _("Account signup is only allowed for administrators.")}
            return render(request, "wiki/error.html", context=c)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["honeypot_class"] = context["form"].honeypot_class
        context["honeypot_jsfunction"] = context["form"].honeypot_jsfunction
        return context

    def get_success_url(self, *args):
        messages.success(
            self.request, _("You are now signed up... and now you can sign in!")
        )
        return reverse("wiki:login")


~~class Logout(View):
    def dispatch(self, request, *args, **kwargs):
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.LOGOUT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        messages.info(request, _("You are no longer logged in. Bye bye!"))
        return redirect("wiki:root")


class Login(FormView):

    form_class = AuthenticationForm
    template_name = "wiki/accounts/login.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect("wiki:root")
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):


## ... source file continues with no further View examples...

```

