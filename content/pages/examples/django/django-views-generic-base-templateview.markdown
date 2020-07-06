title: django.views.generic.base TemplateView Example Code
category: page
slug: django-views-generic-base-templateview-examples
sortorder: 500011531
toc: False
sidebartitle: django.views.generic.base TemplateView
meta: Python example code for the TemplateView class from the django.views.generic.base module of the Django project.


TemplateView is a class within the django.views.generic.base module of the Django project.


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
~~from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

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
                 AjaxCapableProcessFormViewMixin, FormView):
    form_class = SignupForm
    template_name = (
        'socialaccount/signup.' + account_settings.TEMPLATE_EXTENSION)

    def get_form_class(self):
        return get_form_class(app_settings.FORMS,


## ... source file abbreviated to get to TemplateView examples ...



    def get_form_kwargs(self):
        ret = super(SignupView, self).get_form_kwargs()
        ret['sociallogin'] = self.sociallogin
        return ret

    def form_valid(self, form):
        self.request.session.pop('socialaccount_sociallogin', None)
        form.save(self.request)
        return helpers.complete_social_signup(self.request,
                                              self.sociallogin)

    def get_context_data(self, **kwargs):
        ret = super(SignupView, self).get_context_data(**kwargs)
        ret.update(dict(site=get_current_site(self.request),
                        account=self.sociallogin.account))
        return ret

    def get_authenticated_redirect_url(self):
        return reverse(connections)


signup = SignupView.as_view()


~~class LoginCancelledView(TemplateView):
    template_name = (
        "socialaccount/login_cancelled." + account_settings.TEMPLATE_EXTENSION)


login_cancelled = LoginCancelledView.as_view()


~~class LoginErrorView(TemplateView):
    template_name = (
        "socialaccount/authentication_error." +
        account_settings.TEMPLATE_EXTENSION)


login_error = LoginErrorView.as_view()


class ConnectionsView(AjaxCapableProcessFormViewMixin, FormView):
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


## ... source file continues with no further TemplateView examples...

```


## Example 2 from django-wiki
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

[**django-wiki / src/wiki / views / deleted_list.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/views/deleted_list.py)

```python
# deleted_list.py
from django.shortcuts import redirect
~~from django.views.generic.base import TemplateView
from wiki import models


~~class DeletedListView(TemplateView):

    template_name = "wiki/deleted_list.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect("wiki:root")

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        article_list = models.Article.objects.all()
        deleted_articles = []
        for article in article_list:
            if article.current_revision.deleted:
                deleted_articles.append(article)
        kwargs["deleted_articles"] = deleted_articles
        return super().get_context_data(**kwargs)



## ... source file continues with no further TemplateView examples...

```

