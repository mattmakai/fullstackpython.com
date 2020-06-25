title: django.core cache code examples
category: page
slug: django-core-cache-examples
sortorder: 500011078
toc: False
sidebartitle: django.core cache
meta: Python example code for the cache function from the django.core module of the Django project.


cache is a function within the django.core module of the Django project.


## Example 1 from django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).

[**django-debug-toolbar / debug_toolbar / panels / cache.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/panels/cache.py)

```python
# cache.py
import inspect
import sys
import time
from collections import OrderedDict

from django.conf import settings
~~from django.core import cache
from django.core.cache import CacheHandler, caches as original_caches
from django.core.cache.backends.base import BaseCache
from django.dispatch import Signal
from django.middleware import cache as middleware_cache
from django.utils.translation import gettext_lazy as _, ngettext as __

from debug_toolbar import settings as dt_settings
from debug_toolbar.panels import Panel
from debug_toolbar.utils import (
    get_stack,
    get_template_info,
    render_stacktrace,
    tidy_stacktrace,
)

cache_called = Signal()


def send_signal(method):
    def wrapped(self, *args, **kwargs):
        t = time.time()
        value = method(self, *args, **kwargs)
        t = time.time() - t



## ... source file abbreviated to get to cache examples ...


    @property
    def nav_subtitle(self):
        cache_calls = len(self.calls)
        return __(
            "%(cache_calls)d call in %(time).2fms",
            "%(cache_calls)d calls in %(time).2fms",
            cache_calls,
        ) % {"cache_calls": cache_calls, "time": self.total_time}

    @property
    def title(self):
        count = len(getattr(settings, "CACHES", ["default"]))
        return __(
            "Cache calls from %(count)d backend",
            "Cache calls from %(count)d backends",
            count,
        ) % {"count": count}

    def enable_instrumentation(self):
        if isinstance(middleware_cache.caches, CacheHandlerPatch):
~~            cache.caches = middleware_cache.caches
        else:
~~            cache.caches = CacheHandlerPatch()

    def disable_instrumentation(self):
~~        cache.caches = original_caches
        middleware_cache.caches = original_caches

    def generate_stats(self, request, response):
        self.record_stats(
            {
                "total_calls": len(self.calls),
                "calls": self.calls,
                "total_time": self.total_time,
                "hits": self.hits,
                "misses": self.misses,
                "counts": self.counts,
            }
        )

    def generate_server_timing(self, request, response):
        stats = self.get_stats()
        value = stats.get("total_time", 0)
        title = "Cache {} Calls".format(stats.get("total_calls", 0))
        self.record_server_timing("total_time", title, value)



## ... source file continues with no further cache examples...

```

