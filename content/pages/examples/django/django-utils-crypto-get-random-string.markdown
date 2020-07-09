title: django.utils.crypto get_random_string Example Code
category: page
slug: django-utils-crypto-get-random-string-examples
sortorder: 500011430
toc: False
sidebartitle: django.utils.crypto get_random_string
meta: Python example code for the get_random_string callable from the django.utils.crypto module of the Django project.


get_random_string is a callable within the django.utils.crypto module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / models.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/models.py)

```python
# models.py
from __future__ import absolute_import

from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.db import models
~~from django.utils.crypto import get_random_string
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

import allauth.app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import get_next_redirect_url, setup_user_email
from allauth.utils import get_user_model

from ..utils import get_request_param
from . import app_settings, providers
from .adapter import get_adapter
from .fields import JSONField


class SocialAppManager(models.Manager):
    def get_current(self, provider, request=None):
        cache = {}
        if request:
            cache = getattr(request, '_socialapp_cache', {})
            request._socialapp_cache = cache
        app = cache.get(provider)
        if not app:
            site = get_current_site(request)
            app = self.get(


## ... source file abbreviated to get to get_random_string examples ...


                    self.token = t
                except SocialToken.DoesNotExist:
                    self.token.account = a
                    self.token.save()
        except SocialAccount.DoesNotExist:
            pass

    def get_redirect_url(self, request):
        url = self.state.get('next')
        return url

    @classmethod
    def state_from_request(cls, request):
        state = {}
        next_url = get_next_redirect_url(request)
        if next_url:
            state['next'] = next_url
        state['process'] = get_request_param(request, 'process', 'login')
        state['scope'] = get_request_param(request, 'scope', '')
        state['auth_params'] = get_request_param(request, 'auth_params', '')
        return state

    @classmethod
    def stash_state(cls, request):
        state = cls.state_from_request(request)
~~        verifier = get_random_string()
        request.session['socialaccount_state'] = (state, verifier)
        return verifier

    @classmethod
    def unstash_state(cls, request):
        if 'socialaccount_state' not in request.session:
            raise PermissionDenied()
        state, verifier = request.session.pop('socialaccount_state')
        return state

    @classmethod
    def verify_and_unstash_state(cls, request, verifier):
        if 'socialaccount_state' not in request.session:
            raise PermissionDenied()
        state, verifier2 = request.session.pop('socialaccount_state')
        if verifier != verifier2:
            raise PermissionDenied()
        return state



## ... source file continues with no further get_random_string examples...

```

