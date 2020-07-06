title: django.views.decorators.debug sensitive_post_parameters Example Code
category: page
slug: django-views-decorators-debug-sensitive-post-parameters-examples
sortorder: 500011517
toc: False
sidebartitle: django.views.decorators.debug sensitive_post_parameters
meta: Python example code for the sensitive_post_parameters callable from the django.views.decorators.debug module of the Django project.


sensitive_post_parameters is a callable within the django.views.decorators.debug module of the Django project.


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
~~from django.views.decorators.debug import sensitive_post_parameters
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


sensitive_post_parameters_m = method_decorator(
~~    sensitive_post_parameters(
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
        if request.user.is_authenticated and \


## ... source file continues with no further sensitive_post_parameters examples...

```

