title: django.shortcuts resolve_url Example Code
category: page
slug: django-shortcuts-resolve-url-examples
sortorder: 500011349
toc: False
sidebartitle: django.shortcuts resolve_url
meta: Python example code for the resolve_url callable from the django.shortcuts module of the Django project.


resolve_url is a callable within the django.shortcuts module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / adapter.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/adapter.py)

```python
# adapter.py
from __future__ import unicode_literals

import hashlib
import json
import time
import warnings

from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_backends,
    login as django_login,
    logout as django_logout,
)
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
~~from django.shortcuts import resolve_url
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from ..utils import (
    build_absolute_uri,
    email_address_exists,
    generate_unique_username,
    get_user_model,
    import_attribute,
)
from . import app_settings


class DefaultAccountAdapter(object):

    error_messages = {
        'username_blacklisted':
        _('Username can not be used. Please use other username.'),
        'username_taken':
        AbstractUser._meta.get_field('username').error_messages['unique'],


## ... source file abbreviated to get to resolve_url examples ...


                                         from_email,
                                         [email])
            if 'html' in bodies:
                msg.attach_alternative(bodies['html'], 'text/html')
        else:
            msg = EmailMessage(subject,
                               bodies['html'],
                               from_email,
                               [email])
            msg.content_subtype = 'html'  # Main content is now text/html
        return msg

    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        msg.send()

    def get_login_redirect_url(self, request):
        assert request.user.is_authenticated
        url = getattr(settings, "LOGIN_REDIRECT_URLNAME", None)
        if url:
            warnings.warn("LOGIN_REDIRECT_URLNAME is deprecated, simply"
                          " use LOGIN_REDIRECT_URL with a URL name",
                          DeprecationWarning)
        else:
            url = settings.LOGIN_REDIRECT_URL
~~        return resolve_url(url)

    def get_logout_redirect_url(self, request):
~~        return resolve_url(app_settings.LOGOUT_REDIRECT_URL)

    def get_email_confirmation_redirect_url(self, request):
        if request.user.is_authenticated:
            if app_settings.EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL:
                return  \
                    app_settings.EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL
            else:
                return self.get_login_redirect_url(request)
        else:
            return app_settings.EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL

    def is_open_for_signup(self, request):
        return True

    def new_user(self, request):
        user = get_user_model()()
        return user

    def populate_username(self, request, user):
        from .utils import user_username, user_email, user_field
        first_name = user_field(user, 'first_name')
        last_name = user_field(user, 'last_name')
        email = user_email(user)
        username = user_username(user)


## ... source file continues with no further resolve_url examples...

```

