title: django.utils.http url_has_allowed_host_and_scheme Example Code
category: page
slug: django-utils-http-url-has-allowed-host-and-scheme-examples
sortorder: 500011474
toc: False
sidebartitle: django.utils.http url_has_allowed_host_and_scheme
meta: Python example code for the url_has_allowed_host_and_scheme callable from the django.utils.http module of the Django project.


url_has_allowed_host_and_scheme is a callable within the django.utils.http module of the Django project.


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
from django.shortcuts import resolve_url
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


## ... source file abbreviated to get to url_has_allowed_host_and_scheme examples ...


            backend_path = '.'.join([backend.__module__,
                                     backend.__class__.__name__])
            user.backend = backend_path
        django_login(request, user)

    def logout(self, request):
        django_logout(request)

    def confirm_email(self, request, email_address):
        email_address.verified = True
        email_address.set_as_primary(conditional=True)
        email_address.save()

    def set_password(self, user, password):
        user.set_password(password)
        user.save()

    def get_user_search_fields(self):
        user = get_user_model()()
        return filter(lambda a: a and hasattr(user, a),
                      [app_settings.USER_MODEL_USERNAME_FIELD,
                       'first_name', 'last_name', 'email'])

    def is_safe_url(self, url):
        try:
~~            from django.utils.http import url_has_allowed_host_and_scheme
        except ImportError:
            from django.utils.http import \
                is_safe_url as url_has_allowed_host_and_scheme

~~        return url_has_allowed_host_and_scheme(url, allowed_hosts=None)

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = reverse(
            "account_confirm_email",
            args=[emailconfirmation.key])
        ret = build_absolute_uri(
            request,
            url)
        return ret

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        activate_url = self.get_email_confirmation_url(
            request,
            emailconfirmation)
        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": emailconfirmation.key,
        }
        if signup:
            email_template = 'account/email/email_confirmation_signup'
        else:


## ... source file continues with no further url_has_allowed_host_and_scheme examples...

```

