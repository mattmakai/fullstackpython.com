title: django.views.generic FormView Example Code
category: page
slug: django-views-generic-formview-examples
sortorder: 500011523
toc: False
sidebartitle: django.views.generic FormView
meta: Python example code for the FormView class from the django.views.generic module of the Django project.


FormView is a class within the django.views.generic module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / views / crud.py**](https://github.com/jrief/django-angular/blob/master/djng/views/crud.py)

```python
# crud.py
import json

from django.core.exceptions import ValidationError
from django.core import serializers
from django.forms.models import modelform_factory
~~from django.views.generic import FormView

from djng.views.mixins import JSONBaseMixin, JSONResponseException


class NgMissingParameterError(ValueError):
    pass


~~class NgCRUDView(JSONBaseMixin, FormView):
    model = None
    fields = None
    form_class = None
    slug_field = 'slug'
    serializer_name = 'python'
    serialize_natural_keys = False

    allowed_methods = ['GET', 'POST', 'DELETE']
    exclude_methods = []

    def get_allowed_methods(self):
        return [method for method in self.allowed_methods if method not in self.exclude_methods]

    def dispatch(self, request, *args, **kwargs):
        allowed_methods = self.get_allowed_methods()
        try:
            if request.method == 'GET' and 'GET' in allowed_methods:
                if 'pk' in request.GET or self.slug_field in request.GET:
                    return self.ng_get(request, *args, **kwargs)
                return self.ng_query(request, *args, **kwargs)
            elif request.method == 'POST' and 'POST' in allowed_methods:
                return self.ng_save(request, *args, **kwargs)
            elif request.method == 'DELETE' and 'DELETE' in allowed_methods:
                return self.ng_delete(request, *args, **kwargs)


## ... source file continues with no further FormView examples...

```


## Example 2 from django-haystack
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

[**django-haystack / haystack / generic_views.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./generic_views.py)

```python
# generic_views.py
from django.conf import settings
from django.core.paginator import Paginator
~~from django.views.generic import FormView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from .forms import FacetedSearchForm, ModelSearchForm
from .query import SearchQuerySet

RESULTS_PER_PAGE = getattr(settings, "HAYSTACK_SEARCH_RESULTS_PER_PAGE", 20)


class SearchMixin(MultipleObjectMixin, FormMixin):

    template_name = "search/search.html"
    load_all = True
    form_class = ModelSearchForm
    context_object_name = None
    paginate_by = RESULTS_PER_PAGE
    paginate_orphans = 0
    paginator_class = Paginator
    page_kwarg = "page"
    form_name = "form"
    search_field = "q"
    object_list = None

    def get_queryset(self):


## ... source file abbreviated to get to FormView examples ...


        return self.render_to_response(context)


class FacetedSearchMixin(SearchMixin):

    form_class = FacetedSearchForm
    facet_fields = None

    def get_form_kwargs(self):
        kwargs = super(FacetedSearchMixin, self).get_form_kwargs()
        kwargs.update({"selected_facets": self.request.GET.getlist("selected_facets")})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(FacetedSearchMixin, self).get_context_data(**kwargs)
        context.update({"facets": self.queryset.facet_counts()})
        return context

    def get_queryset(self):
        qs = super(FacetedSearchMixin, self).get_queryset()
        for field in self.facet_fields:
            qs = qs.facet(field)
        return qs


~~class SearchView(SearchMixin, FormView):

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FacetedSearchView(FacetedSearchMixin, SearchView):

    pass



## ... source file continues with no further FormView examples...

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

[**django-oauth-toolkit / oauth2_provider / views / base.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/views/base.py)

```python
# base.py
import json
import logging
import urllib.parse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
~~from django.views.generic import FormView, View

from ..exceptions import OAuthToolkitError
from ..forms import AllowForm
from ..http import OAuth2ResponseRedirect
from ..models import get_access_token_model, get_application_model
from ..scopes import get_scopes_backend
from ..settings import oauth2_settings
from ..signals import app_authorized
from .mixins import OAuthLibMixin


log = logging.getLogger("oauth2_provider")


class BaseAuthorizationView(LoginRequiredMixin, OAuthLibMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.oauth2_data = {}
        return super().dispatch(request, *args, **kwargs)

    def error_response(self, error, application, **kwargs):
        redirect, error_response = super().error_response(error, **kwargs)

        if redirect:
            return self.redirect(error_response["url"], application)

        status = error_response["error"].status_code
        return self.render_to_response(error_response, status=status)

    def redirect(self, redirect_to, application):
        if application is None:
            allowed_schemes = oauth2_settings.ALLOWED_REDIRECT_URI_SCHEMES
        else:
            allowed_schemes = application.get_allowed_schemes()
        return OAuth2ResponseRedirect(redirect_to, allowed_schemes)


RFC3339 = "%Y-%m-%dT%H:%M:%SZ"


~~class AuthorizationView(BaseAuthorizationView, FormView):
    template_name = "oauth2_provider/authorize.html"
    form_class = AllowForm

    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    skip_authorization_completely = False

    def get_initial(self):
        scopes = self.oauth2_data.get("scope", self.oauth2_data.get("scopes", []))
        initial_data = {
            "redirect_uri": self.oauth2_data.get("redirect_uri", None),
            "scope": " ".join(scopes),
            "client_id": self.oauth2_data.get("client_id", None),
            "state": self.oauth2_data.get("state", None),
            "response_type": self.oauth2_data.get("response_type", None),
            "code_challenge": self.oauth2_data.get("code_challenge", None),
            "code_challenge_method": self.oauth2_data.get("code_challenge_method", None),
        }
        return initial_data

    def form_valid(self, form):
        client_id = form.cleaned_data["client_id"]


## ... source file continues with no further FormView examples...

```


## Example 4 from django-wiki
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
~~from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import View
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


class Logout(View):
    def dispatch(self, request, *args, **kwargs):
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.LOGOUT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        messages.info(request, _("You are no longer logged in. Bye bye!"))
        return redirect("wiki:root")


~~class Login(FormView):

    form_class = AuthenticationForm
    template_name = "wiki/accounts/login.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect("wiki:root")
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        self.request.session.set_test_cookie()
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        self.referer = request.session.get("login_referer", "")
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.referer = request.META.get("HTTP_REFERER", "")
        request.session["login_referer"] = self.referer


## ... source file continues with no further FormView examples...

```

