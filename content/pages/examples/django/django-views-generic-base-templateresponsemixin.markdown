title: django.views.generic.base TemplateResponseMixin Example Code
category: page
slug: django-views-generic-base-templateresponsemixin-examples
sortorder: 500011530
toc: False
sidebartitle: django.views.generic.base TemplateResponseMixin
meta: Python example code for the TemplateResponseMixin class from the django.views.generic.base module of the Django project.


TemplateResponseMixin is a class within the django.views.generic.base module of the Django project.


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


## ... source file abbreviated to get to TemplateResponseMixin examples ...


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


## ... source file abbreviated to get to TemplateResponseMixin examples ...


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


## ... source file continues with no further TemplateResponseMixin examples...

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

[**django-wiki / src/wiki / views / mixins.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/views/mixins.py)

```python
# mixins.py
import logging

~~from django.views.generic.base import TemplateResponseMixin
from wiki.conf import settings
from wiki.core.plugins import registry

log = logging.getLogger(__name__)


~~class ArticleMixin(TemplateResponseMixin):


    def dispatch(self, request, article, *args, **kwargs):
        self.urlpath = kwargs.pop("urlpath", None)
        self.article = article
        self.children_slice = []
        if settings.SHOW_MAX_CHILDREN > 0:
            try:
                for child in self.article.get_children(
                    max_num=settings.SHOW_MAX_CHILDREN + 1,
                    articles__article__current_revision__deleted=False,
                    user_can_read=request.user,
                ):
                    self.children_slice.append(child)
            except AttributeError as e:
                log.error(
                    "Attribute error most likely caused by wrong MPTT version. Use 0.5.3+.\n\n"
                    + str(e)
                )
                raise
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["urlpath"] = self.urlpath


## ... source file continues with no further TemplateResponseMixin examples...

```

