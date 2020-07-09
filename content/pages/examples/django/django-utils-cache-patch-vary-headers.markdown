title: django.utils.cache patch_vary_headers Example Code
category: page
slug: django-utils-cache-patch-vary-headers-examples
sortorder: 500011428
toc: False
sidebartitle: django.utils.cache patch_vary_headers
meta: Python example code for the patch_vary_headers callable from the django.utils.cache module of the Django project.


patch_vary_headers is a callable within the django.utils.cache module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / cache / page.py**](https://github.com/divio/django-cms/blob/develop/cms/cache/page.py)

```python
# page.py

import hashlib

from datetime import timedelta

from django.conf import settings
~~from django.utils.cache import add_never_cache_headers, patch_response_headers, patch_vary_headers
from django.utils.encoding import iri_to_uri
from django.utils.timezone import now

from cms.cache import _get_cache_version, _set_cache_version, _get_cache_key
from cms.constants import EXPIRE_NOW, MAX_EXPIRATION_TTL
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils.conf import get_cms_setting
from cms.utils.helpers import get_timezone_name


def _page_cache_key(request):
    cache_key = "%s:%d:%s" % (
        get_cms_setting("CACHE_PREFIX"),
        settings.SITE_ID,
        hashlib.sha1(iri_to_uri(request.get_full_path()).encode('utf-8')).hexdigest()
    )
    if settings.USE_TZ:
        cache_key += '.%s' % get_timezone_name()
    return cache_key


def set_page_cache(response):
    from django.core.cache import cache



## ... source file abbreviated to get to patch_vary_headers examples ...


    timestamp = now()

    placeholders = toolbar.content_renderer.get_rendered_placeholders()
    placeholder_ttl_list = []
    vary_cache_on_set = set()
    for ph in placeholders:
        ttl = ph.get_cache_expiration(request, timestamp)
        vary_cache_on = ph.get_vary_cache_on(request)

        placeholder_ttl_list.append(ttl)
        if ttl and vary_cache_on:
            vary_cache_on_set |= set(vary_cache_on)

    if EXPIRE_NOW not in placeholder_ttl_list:
        if placeholder_ttl_list:
            min_placeholder_ttl = min(x for x in placeholder_ttl_list)
        else:
            min_placeholder_ttl = MAX_EXPIRATION_TTL
        ttl = min(
            get_cms_setting('CACHE_DURATIONS')['content'],
            min_placeholder_ttl
        )

        if ttl > 0:
            patch_response_headers(response, cache_timeout=ttl)
~~            patch_vary_headers(response, sorted(vary_cache_on_set))

            version = _get_cache_version()
            expires_datetime = timestamp + timedelta(seconds=ttl)
            cache.set(
                _page_cache_key(request),
                (
                    response.content,
                    response._headers,
                    expires_datetime,
                ),
                ttl,
                version=version
            )
            _set_cache_version(version)
    return response


def get_page_cache(request):
    from django.core.cache import cache
    return cache.get(_page_cache_key(request), version=_get_cache_version())


def get_xframe_cache(page):
    from django.core.cache import cache


## ... source file continues with no further patch_vary_headers examples...

```


## Example 2 from django-cors-headers
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
~~from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin

from corsheaders.conf import conf
from corsheaders.signals import check_request_enabled

ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"


class CorsPostCsrfMiddleware(MiddlewareMixin):
    def _https_referer_replace_reverse(self, request):
        if conf.CORS_REPLACE_HTTPS_REFERER and "ORIGINAL_HTTP_REFERER" in request.META:
            http_referer = request.META["ORIGINAL_HTTP_REFERER"]
            request.META["HTTP_REFERER"] = http_referer
            del request.META["ORIGINAL_HTTP_REFERER"]

    def process_request(self, request):
        self._https_referer_replace_reverse(request)
        return None



## ... source file abbreviated to get to patch_vary_headers examples ...


        if request._cors_enabled:
            if conf.CORS_REPLACE_HTTPS_REFERER:
                self._https_referer_replace(request)

            if (
                request.method == "OPTIONS"
                and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META
            ):
                response = http.HttpResponse()
                response["Content-Length"] = "0"
                return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request._cors_enabled and conf.CORS_REPLACE_HTTPS_REFERER:
            self._https_referer_replace(request)
        return None

    def process_response(self, request, response):
        enabled = getattr(request, "_cors_enabled", None)
        if enabled is None:
            enabled = self.is_enabled(request)

        if not enabled:
            return response

~~        patch_vary_headers(response, ["Origin"])

        origin = request.META.get("HTTP_ORIGIN")
        if not origin:
            return response

        url = urlparse(origin)

        if conf.CORS_ALLOW_CREDENTIALS:
            response[ACCESS_CONTROL_ALLOW_CREDENTIALS] = "true"

        if (
            not conf.CORS_ORIGIN_ALLOW_ALL
            and not self.origin_found_in_white_lists(origin, url)
            and not self.check_signal(request)
        ):
            return response

        if conf.CORS_ORIGIN_ALLOW_ALL and not conf.CORS_ALLOW_CREDENTIALS:
            response[ACCESS_CONTROL_ALLOW_ORIGIN] = "*"
        else:
            response[ACCESS_CONTROL_ALLOW_ORIGIN] = origin

        if len(conf.CORS_EXPOSE_HEADERS):
            response[ACCESS_CONTROL_EXPOSE_HEADERS] = ", ".join(


## ... source file continues with no further patch_vary_headers examples...

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

[**django-oauth-toolkit / oauth2_provider / middleware.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./middleware.py)

```python
# middleware.py
from django.contrib.auth import authenticate
~~from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin


class OAuth2TokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.META.get("HTTP_AUTHORIZATION", "").startswith("Bearer"):
            if not hasattr(request, "user") or request.user.is_anonymous:
                user = authenticate(request=request)
                if user:
                    request.user = request._cached_user = user

    def process_response(self, request, response):
~~        patch_vary_headers(response, ("Authorization",))
        return response



## ... source file continues with no further patch_vary_headers examples...

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

[**django-rest-framework / rest_framework / views.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./views.py)

```python
# views.py
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db import connection, models, transaction
from django.http import Http404
from django.http.response import HttpResponseBase
~~from django.utils.cache import cc_delim_re, patch_vary_headers
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import DefaultSchema
from rest_framework.settings import api_settings
from rest_framework.utils import formatting


def get_view_name(view):
    name = getattr(view, 'name', None)
    if name is not None:
        return name

    name = view.__class__.__name__
    name = formatting.remove_trailing_string(name, 'View')
    name = formatting.remove_trailing_string(name, 'ViewSet')
    name = formatting.camelcase_to_spaces(name)

    suffix = getattr(view, 'suffix', None)
    if suffix:


## ... source file abbreviated to get to patch_vary_headers examples ...


        version, scheme = self.determine_version(request, *args, **kwargs)
        request.version, request.versioning_scheme = version, scheme

        self.perform_authentication(request)
        self.check_permissions(request)
        self.check_throttles(request)

    def finalize_response(self, request, response, *args, **kwargs):
        assert isinstance(response, HttpResponseBase), (
            'Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` '
            'to be returned from the view, but received a `%s`'
            % type(response)
        )

        if isinstance(response, Response):
            if not getattr(request, 'accepted_renderer', None):
                neg = self.perform_content_negotiation(request, force=True)
                request.accepted_renderer, request.accepted_media_type = neg

            response.accepted_renderer = request.accepted_renderer
            response.accepted_media_type = request.accepted_media_type
            response.renderer_context = self.get_renderer_context()

        vary_headers = self.headers.pop('Vary', None)
        if vary_headers is not None:
~~            patch_vary_headers(response, cc_delim_re.split(vary_headers))

        for key, value in self.headers.items():
            response[key] = value

        return response

    def handle_exception(self, exc):
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            auth_header = self.get_authenticate_header(self.request)

            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN

        exception_handler = self.get_exception_handler()

        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)

        if response is None:
            self.raise_uncaught_exception(exc)



## ... source file continues with no further patch_vary_headers examples...

```

