title: django.utils.timezone make_aware Example Code
category: page
slug: django-utils-timezone-make-aware-examples
sortorder: 500011495
toc: False
sidebartitle: django.utils.timezone make_aware
meta: Python example code for the make_aware callable from the django.utils.timezone module of the Django project.


make_aware is a callable within the django.utils.timezone module of the Django project.


## Example 1 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / models / imagemodels.py**](https://github.com/divio/django-filer/blob/develop/filer/models/imagemodels.py)

```python
# imagemodels.py
from __future__ import absolute_import

import logging
from datetime import datetime

from django.conf import settings
from django.db import models
~~from django.utils.timezone import get_current_timezone, make_aware, now
from django.utils.translation import ugettext_lazy as _

from .abstract import BaseImage


logger = logging.getLogger("filer")


class Image(BaseImage):
    date_taken = models.DateTimeField(_('date taken'), null=True, blank=True,
                                      editable=False)
    author = models.CharField(_('author'), max_length=255, null=True, blank=True)
    must_always_publish_author_credit = models.BooleanField(_('must always publish author credit'), default=False)
    must_always_publish_copyright = models.BooleanField(_('must always publish copyright'), default=False)

    class Meta(BaseImage.Meta):
        swappable = 'FILER_IMAGE_MODEL'
        default_manager_name = 'objects'

    def save(self, *args, **kwargs):
        if self.date_taken is None:
            try:
                exif_date = self.exif.get('DateTimeOriginal', None)
                if exif_date is not None:
                    d, t = exif_date.split(" ")
                    year, month, day = d.split(':')
                    hour, minute, second = t.split(':')
                    if getattr(settings, "USE_TZ", False):
                        tz = get_current_timezone()
~~                        self.date_taken = make_aware(datetime(
                            int(year), int(month), int(day),
                            int(hour), int(minute), int(second)), tz)
                    else:
                        self.date_taken = datetime(
                            int(year), int(month), int(day),
                            int(hour), int(minute), int(second))
            except Exception:
                pass
        if self.date_taken is None:
            self.date_taken = now()
        super(Image, self).save(*args, **kwargs)



## ... source file continues with no further make_aware examples...

```


## Example 2 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / oauth2_validators.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./oauth2_validators.py)

```python
# oauth2_validators.py
import base64
import binascii
import http.client
import logging
from collections import OrderedDict
from datetime import datetime, timedelta
from urllib.parse import unquote_plus

import requests
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
~~from django.utils.timezone import make_aware
from django.utils.translation import gettext_lazy as _
from oauthlib.oauth2 import RequestValidator

from .exceptions import FatalClientError
from .models import (
    AbstractApplication, get_access_token_model,
    get_application_model, get_grant_model, get_refresh_token_model
)
from .scopes import get_scopes_backend
from .settings import oauth2_settings


log = logging.getLogger("oauth2_provider")

GRANT_TYPE_MAPPING = {
    "authorization_code": (AbstractApplication.GRANT_AUTHORIZATION_CODE, ),
    "password": (AbstractApplication.GRANT_PASSWORD, ),
    "client_credentials": (AbstractApplication.GRANT_CLIENT_CREDENTIALS, ),
    "refresh_token": (
        AbstractApplication.GRANT_AUTHORIZATION_CODE,
        AbstractApplication.GRANT_PASSWORD,
        AbstractApplication.GRANT_CLIENT_CREDENTIALS,
    )
}


## ... source file abbreviated to get to make_aware examples ...


            content = response.json()
        except ValueError:
            log.exception("Introspection: Failed to parse response as json")
            return None

        if "active" in content and content["active"] is True:
            if "username" in content:
                user, _created = UserModel.objects.get_or_create(
                    **{UserModel.USERNAME_FIELD: content["username"]}
                )
            else:
                user = None

            max_caching_time = datetime.now() + timedelta(
                seconds=oauth2_settings.RESOURCE_SERVER_TOKEN_CACHING_SECONDS
            )

            if "exp" in content:
                expires = datetime.utcfromtimestamp(content["exp"])
                if expires > max_caching_time:
                    expires = max_caching_time
            else:
                expires = max_caching_time

            scope = content.get("scope", "")
~~            expires = make_aware(expires)

            access_token, _created = AccessToken.objects.update_or_create(
                token=token,
                defaults={
                    "user": user,
                    "application": None,
                    "scope": scope,
                    "expires": expires,
                })

            return access_token

    def validate_bearer_token(self, token, scopes, request):
        if not token:
            return False

        introspection_url = oauth2_settings.RESOURCE_SERVER_INTROSPECTION_URL
        introspection_token = oauth2_settings.RESOURCE_SERVER_AUTH_TOKEN
        introspection_credentials = oauth2_settings.RESOURCE_SERVER_INTROSPECTION_CREDENTIALS

        try:
            access_token = AccessToken.objects.select_related("application", "user").get(token=token)
        except AccessToken.DoesNotExist:
            access_token = None


## ... source file continues with no further make_aware examples...

```


## Example 3 from graphite-web
[Graphite](https://github.com/graphite-project/graphite-web)
([project website](http://graphiteapp.org/),
[documentation](https://graphite.readthedocs.io/en/latest/) and
[PyPI package information](https://pypi.org/project/graphite-web/))
is a metrics collection and visualization tool, built with both
Python and JavaScript. Metrics are collected by a Node.js application
and displayed using a [Django](/django.html) web application,
called "Graphite-Web", which is one of three core projects under
the Graphite umbrella (the other two are
[Carbon](https://github.com/graphite-project/carbon) and
[Whisper](https://github.com/graphite-project/whisper)).

Graphite is provided as open sourced under the
[Apache License 2.0](https://github.com/graphite-project/whisper/blob/master/LICENSE).

[**graphite-web / webapp / graphite / util.py**](https://github.com/graphite-project/graphite-web/blob/master/webapp/graphite/util.py)

```python
# util.py

import imp
import io
import json as _json
import socket
import time
import sys
import calendar
import pytz
import six
import traceback

from datetime import datetime
from functools import wraps
from os.path import splitext, basename

from django.conf import settings
~~from django.utils.timezone import make_aware

from graphite.compat import HttpResponse
from graphite.logger import log

if sys.version_info >= (3, 0):
  PY3 = True
  import pickle
  from io import BytesIO
else:
  PY3 = False
  import cPickle as pickle
  from cStringIO import StringIO as BytesIO

try:
  import msgpack  # NOQA
except ImportError:
  import graphite.umsgpack as msgpack  # NOQA


def epoch(dt):
  if not dt.tzinfo:
    tb = traceback.extract_stack(None, 2)
    log.warning('epoch() called with non-timezone-aware datetime in %s at %s:%d' % (tb[0][2], tb[0][0], tb[0][1]))
    return calendar.timegm(make_aware(dt, pytz.timezone(settings.TIME_ZONE)).astimezone(pytz.utc).timetuple())
  return calendar.timegm(dt.astimezone(pytz.utc).timetuple())


def epoch_to_dt(timestamp):
~~    return make_aware(datetime.utcfromtimestamp(timestamp), pytz.utc)


def timebounds(requestContext):
  startTime = int(epoch(requestContext['startTime']))
  endTime = int(epoch(requestContext['endTime']))
  now = int(epoch(requestContext['now']))

  return (startTime, endTime, now)


def is_local_interface(host):
  is_ipv6 = False
  if ':' not in host:
    pass
  elif host.count(':') == 1:
    host = host.split(':', 1)[0]
  else:
    is_ipv6 = True

    if host.find('[', 0, 2) != -1:
      last_bracket_position  = host.rfind(']')
      last_colon_position = host.rfind(':')
      if last_colon_position > last_bracket_position:
        host = host.rsplit(':', 1)[0]


## ... source file continues with no further make_aware examples...

```

