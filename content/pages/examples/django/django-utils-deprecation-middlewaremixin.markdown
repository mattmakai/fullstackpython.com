title: django.utils.deprecation MiddlewareMixin Example Code
category: page
slug: django-utils-deprecation-middlewaremixin-examples
sortorder: 500011437
toc: False
sidebartitle: django.utils.deprecation MiddlewareMixin
meta: Python example code for the MiddlewareMixin class from the django.utils.deprecation module of the Django project.


MiddlewareMixin is a class within the django.utils.deprecation module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / middleware.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/middleware.py)

```python
# middleware.py
from __future__ import unicode_literals

import threading
import time

from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.functional import curry
from django.apps import apps
from auditlog.models import LogEntry
from auditlog.compat import is_authenticated

try:
~~    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


threadlocal = threading.local()


~~class AuditlogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        threadlocal.auditlog = {
            'signal_duid': (self.__class__, time.time()),
            'remote_addr': request.META.get('REMOTE_ADDR'),
        }

        if request.META.get('HTTP_X_FORWARDED_FOR'):
            threadlocal.auditlog['remote_addr'] = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]

        if hasattr(request, 'user') and is_authenticated(request.user):
            set_actor = curry(self.set_actor, user=request.user, signal_duid=threadlocal.auditlog['signal_duid'])
            pre_save.connect(set_actor, sender=LogEntry, dispatch_uid=threadlocal.auditlog['signal_duid'], weak=False)

    def process_response(self, request, response):
        if hasattr(threadlocal, 'auditlog'):
            pre_save.disconnect(sender=LogEntry, dispatch_uid=threadlocal.auditlog['signal_duid'])

        return response

    def process_exception(self, request, exception):
        if hasattr(threadlocal, 'auditlog'):
            pre_save.disconnect(sender=LogEntry, dispatch_uid=threadlocal.auditlog['signal_duid'])



## ... source file continues with no further MiddlewareMixin examples...

```


## Example 2 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / middleware.py**](https://github.com/jrief/django-angular/blob/master/djng/./middleware.py)

```python
# middleware.py
from django import http
from django.urls import reverse
from django.utils.http import unquote
try:
~~    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


~~class AngularUrlMiddleware(MiddlewareMixin):
    ANGULAR_REVERSE = '/angular/reverse/'

    def process_request(self, request):
        if request.path == self.ANGULAR_REVERSE:
            url_name = request.GET.get('djng_url_name')
            url_args = request.GET.getlist('djng_url_args', [])
            url_kwargs = {}

            url_args = filter(lambda x: x, url_args)

            for param in request.GET:
                if param.startswith('djng_url_kwarg_'):
                    if request.GET[param]:
                        url_kwargs[param[15:]] = request.GET[param]  # [15:] to remove 'djng_url_kwarg' prefix

            url = unquote(reverse(url_name, args=url_args, kwargs=url_kwargs))
            assert not url.startswith(self.ANGULAR_REVERSE), "Prevent recursive requests"

            request.path = request.path_info = url
            request.environ['PATH_INFO'] = url
            query = request.GET.copy()
            for key in request.GET:
                if key.startswith('djng_url'):
                    query.pop(key, None)


## ... source file continues with no further MiddlewareMixin examples...

```


## Example 3 from django-cors-headers
[django-cors-headers](https://github.com/ottoyiu/django-cors-headers)
is an
[open source](https://github.com/ottoyiu/django-cors-headers/blob/master/LICENSE)
library for enabling
[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
handling in your [Django](/django.html) web applications and appropriately
dealing with HTTP headers for CORS requests.

[**django-cors-headers / src/corsheaders / middleware.py**](https://github.com/ottoyiu/django-cors-headers/blob/master/src/corsheaders/./middleware.py)

```python
# middleware.py
import re
from urllib.parse import urlparse

from django import http
from django.utils.cache import patch_vary_headers
~~from django.utils.deprecation import MiddlewareMixin

from corsheaders.conf import conf
from corsheaders.signals import check_request_enabled

ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"


~~class CorsPostCsrfMiddleware(MiddlewareMixin):
    def _https_referer_replace_reverse(self, request):
        if conf.CORS_REPLACE_HTTPS_REFERER and "ORIGINAL_HTTP_REFERER" in request.META:
            http_referer = request.META["ORIGINAL_HTTP_REFERER"]
            request.META["HTTP_REFERER"] = http_referer
            del request.META["ORIGINAL_HTTP_REFERER"]

    def process_request(self, request):
        self._https_referer_replace_reverse(request)
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        self._https_referer_replace_reverse(request)
        return None


~~class CorsMiddleware(MiddlewareMixin):
    def _https_referer_replace(self, request):
        origin = request.META.get("HTTP_ORIGIN")

        if (
            request.is_secure()
            and origin
            and "ORIGINAL_HTTP_REFERER" not in request.META
        ):

            url = urlparse(origin)
            if not conf.CORS_ORIGIN_ALLOW_ALL and not self.origin_found_in_white_lists(
                origin, url
            ):
                return

            try:
                http_referer = request.META["HTTP_REFERER"]
                http_host = "https://%s/" % request.META["HTTP_HOST"]
                request.META = request.META.copy()
                request.META["ORIGINAL_HTTP_REFERER"] = http_referer
                request.META["HTTP_REFERER"] = http_host
            except KeyError:
                pass



## ... source file continues with no further MiddlewareMixin examples...

```


## Example 4 from django-downloadview
[django-downloadview](https://github.com/benoitbryon/django-downloadview)
([project documentation](https://django-downloadview.readthedocs.io/en/1.9/)
and
[PyPI package information](https://pypi.org/project/django-downloadview/))
is a [Django](/django.html) extension for serving downloads through your
web application. While typically you would use a web server to handle
[static content](/static-content.html), sometimes you need to control
file access, such as requiring a user to register before downloading a
PDF. In that situations, django-downloadview is a handy library to avoid
boilerplate code for common scenarios.

[**django-downloadview / django_downloadview / middlewares.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/./middlewares.py)

```python
# middlewares.py
import collections
import copy
import os

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from django_downloadview.response import DownloadResponse
from django_downloadview.utils import import_member

try:
~~    from django.utils.deprecation import MiddlewareMixin
except ImportError:

~~    class MiddlewareMixin(object):
        def __init__(self, get_response=None):
~~            super(MiddlewareMixin, self).__init__()


AUTO_CONFIGURE = object()


def is_download_response(response):
    return isinstance(response, DownloadResponse)


~~class BaseDownloadMiddleware(MiddlewareMixin):

    def is_download_response(self, response):
        return is_download_response(response)

    def process_response(self, request, response):
        if self.is_download_response(response):
            return self.process_download_response(request, response)
        return response

    def process_download_response(self, request, response):
        raise NotImplementedError()


class RealDownloadMiddleware(BaseDownloadMiddleware):

    def is_download_response(self, response):
        if super(RealDownloadMiddleware, self).is_download_response(response):
            try:
                return response.file.url or response.file.name
            except AttributeError:
                return False
            else:
                return True
        return False


## ... source file continues with no further MiddlewareMixin examples...

```


## Example 5 from django-easy-timezones
[django-easy-timezones](https://github.com/Miserlou/django-easy-timezones)
([project website](https://www.gun.io/blog/django-easy-timezones))
is a Django
[middleware](https://docs.djangoproject.com/en/2.2/topics/http/middleware/)
[code library](https://pypi.org/project/django-easy-timezones/)
to simplify handling time data in your applications using
users' geolocation data.

[**django-easy-timezones / easy_timezones / middleware.py**](https://github.com/Miserlou/django-easy-timezones/blob/master/easy_timezones/./middleware.py)

```python
# middleware.py
    if not GEOIPV6_DATABASE:
        raise ImproperlyConfigured("GEOIPV6_DATABASE setting has not been properly defined.")

    if not os.path.exists(GEOIPV6_DATABASE):
        raise ImproperlyConfigured("GEOIPV6_DATABASE setting is defined, but file does not exist.")

    return (GEOIP_DATABASE, GEOIPV6_DATABASE)

load_db_settings()

def load_db():

    GEOIP_DATABASE, GEOIPV6_DATABASE = load_db_settings()

    global db
    db = pygeoip.GeoIP(GEOIP_DATABASE, pygeoip.MEMORY_CACHE)

    global db_v6
    db_v6 = pygeoip.GeoIP(GEOIPV6_DATABASE, pygeoip.MEMORY_CACHE)

    global db_loaded
    db_loaded = True


if django.VERSION >= (1, 10):
~~    from django.utils.deprecation import MiddlewareMixin
    middleware_base_class = MiddlewareMixin
else:
    middleware_base_class = object


class EasyTimezoneMiddleware(middleware_base_class):
    def process_request(self, request):

        if not request:
            return

        if not db_loaded:
            load_db()

        tz = request.session.get('django_timezone')

        if not tz:
            tz = timezone.get_default_timezone()

            client_ip = get_ip_address_from_request(request)
            ip_addrs = client_ip.split(',')
            for ip in ip_addrs:
                if is_valid_ip(ip) and not is_local_ip(ip):
                    if ':' in ip:


## ... source file continues with no further MiddlewareMixin examples...

```


## Example 6 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / middleware.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./middleware.py)

```python
# middleware.py
from django.contrib.auth import authenticate
from django.utils.cache import patch_vary_headers
~~from django.utils.deprecation import MiddlewareMixin


~~class OAuth2TokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.META.get("HTTP_AUTHORIZATION", "").startswith("Bearer"):
            if not hasattr(request, "user") or request.user.is_anonymous:
                user = authenticate(request=request)
                if user:
                    request.user = request._cached_user = user

    def process_response(self, request, response):
        patch_vary_headers(response, ("Authorization",))
        return response



## ... source file continues with no further MiddlewareMixin examples...

```


## Example 7 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / middleware.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./middleware.py)

```python
# middleware.py
from django.core.exceptions import MiddlewareNotUsed
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.html import strip_spaces_between_tags as minify_html

from pipeline.conf import settings

~~from django.utils.deprecation import MiddlewareMixin


~~class MinifyHTMLMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(MinifyHTMLMiddleware, self).__init__(*args, **kwargs)
        if not settings.PIPELINE_ENABLED:
            raise MiddlewareNotUsed

    def process_response(self, request, response):
        if response.has_header('Content-Type') and 'text/html' in response['Content-Type']:
            try:
                response.content = minify_html(response.content.decode('utf-8').strip())
                response['Content-Length'] = str(len(response.content))
            except DjangoUnicodeDecodeError:
                pass
        return response



## ... source file continues with no further MiddlewareMixin examples...

```


## Example 8 from django-webtest
[django-webtest](https://github.com/django-webtest/django-webtest)
([PyPI package information](https://pypi.org/project/django-webtest/))
is a [Django](/django.html) extension that makes it easier to use
[WebTest](http://docs.pylonsproject.org/projects/webtest/) with
your projects.

The project is open sourced under the
[MIT license](https://github.com/django-webtest/django-webtest/blob/master/LICENSE.txt).

[**django-webtest / django_webtest / middleware.py**](https://github.com/django-webtest/django-webtest/blob/master/django_webtest/./middleware.py)

```python
# middleware.py
import django
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.core.exceptions import ImproperlyConfigured
from django.contrib import auth
if django.VERSION >= (1, 10):
~~    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object

from django_webtest.compat import is_authenticated


class WebtestUserMiddleware(RemoteUserMiddleware):

    header = "WEBTEST_USER"

    def process_request(self, request):
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The django-webtest auth middleware requires the "
                "'django.contrib.auth.middleware.AuthenticationMiddleware' "
                "to be installed. Add it to your MIDDLEWARE setting "
                "or disable django-webtest auth support by setting "
                "'setup_auth' property of your WebTest subclass to False."
            )
        try:
            username = request.META[self.header]
        except KeyError:
            return
        if is_authenticated(request.user):
            if hasattr(request.user, "get_username"):
                authenticated_username = request.user.get_username()
            else:
                authenticated_username = request.user.username
            clean_username = self.clean_username(username, request)
            if authenticated_username == clean_username:
                return
        user = auth.authenticate(django_webtest_user=username)
        if user:
            request.user = user
            auth.login(request, user)


~~class DisableCSRFCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._dont_enforce_csrf_checks = True



## ... source file continues with no further MiddlewareMixin examples...

```


## Example 9 from graphite-web
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

[**graphite-web / webapp / graphite / middleware.py**](https://github.com/graphite-project/graphite-web/blob/master/webapp/graphite/middleware.py)

```python
# middleware.py
from graphite.logger import log
try:
~~    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    MiddlewareMixin = object


~~class LogExceptionsMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        log.exception('Exception encountered in <{0} {1}>'.format(request.method, request.build_absolute_uri()))
        return None



## ... source file continues with no further MiddlewareMixin examples...

```


## Example 10 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / middleware.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./middleware.py)

```python
# middleware.py
import django.middleware.locale
import django.shortcuts
from django.utils import translation
~~from django.utils.deprecation import MiddlewareMixin


~~class RequestLocaleMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'GET':
            language = request.GET.get('lang')
            if language:
                translation.activate(language)
                request.session[translation.LANGUAGE_SESSION_KEY] = translation.get_language()
                query = request.GET.copy()
                del query['lang']
                path = '?'.join([request.path, query.urlencode()])
                return django.shortcuts.redirect(path)



## ... source file continues with no further MiddlewareMixin examples...

```


## Example 11 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / middleware.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/middleware.py)

```python
# middleware.py
import warnings

~~from django.utils.deprecation import MiddlewareMixin
from wagtail.core.models import Site
from wagtail.utils.deprecation import RemovedInWagtail211Warning


warnings.warn(
    'wagtail.core.middleware.SiteMiddleware and the use of request.site is deprecated. '
    'Please update your code to use Site.find_for_request(request) in place of request.site, '
    'and remove wagtail.core.middleware.SiteMiddleware from MIDDLEWARES',
    RemovedInWagtail211Warning
)


~~class SiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            request.site = Site.find_for_request(request)
        except Site.DoesNotExist:
            request.site = None



## ... source file continues with no further MiddlewareMixin examples...

```

