title: django.utils.cache patch_response_headers Example Code
category: page
slug: django-utils-cache-patch-response-headers-examples
sortorder: 500011427
toc: False
sidebartitle: django.utils.cache patch_response_headers
meta: Python example code for the patch_response_headers callable from the django.utils.cache module of the Django project.


patch_response_headers is a callable within the django.utils.cache module of the Django project.


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



## ... source file abbreviated to get to patch_response_headers examples ...



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
~~            patch_response_headers(response, cache_timeout=ttl)
            patch_vary_headers(response, sorted(vary_cache_on_set))

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


## ... source file continues with no further patch_response_headers examples...

```

