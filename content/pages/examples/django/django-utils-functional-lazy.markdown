title: django.utils.functional lazy Example Code
category: page
slug: django-utils-functional-lazy-examples
sortorder: 500011458
toc: False
sidebartitle: django.utils.functional lazy
meta: Python example code for the lazy callable from the django.utils.functional module of the Django project.


lazy is a callable within the django.utils.functional module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / context_processors.py**](https://github.com/divio/django-cms/blob/develop/cms/./context_processors.py)

```python
# context_processors.py
try:
    from functools import lru_cache
except ImportError:
    from django.utils.lru_cache import lru_cache

~~from django.utils.functional import lazy

from cms.utils.conf import get_cms_setting
from cms.utils.page import get_page_template_from_request


def cms_settings(request):
    from menus.menu_pool import MenuRenderer

    @lru_cache(maxsize=None)
    def _get_menu_renderer():
        from menus.menu_pool import menu_pool
        return menu_pool.get_renderer(request)

~~    _get_menu_renderer = lazy(_get_menu_renderer, MenuRenderer)

    return {
        'cms_menu_renderer': _get_menu_renderer(),
        'CMS_MEDIA_URL': get_cms_setting('MEDIA_URL'),
        'CMS_TEMPLATE': lambda: get_page_template_from_request(request),
    }



## ... source file continues with no further lazy examples...

```


## Example 2 from django-rest-framework
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

[**django-rest-framework / rest_framework / reverse.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./reverse.py)

```python
# reverse.py
from django.urls import NoReverseMatch
from django.urls import reverse as django_reverse
~~from django.utils.functional import lazy

from rest_framework.settings import api_settings
from rest_framework.utils.urls import replace_query_param


def preserve_builtin_query_params(url, request=None):
    if request is None:
        return url

    overrides = [
        api_settings.URL_FORMAT_OVERRIDE,
    ]

    for param in overrides:
        if param and (param in request.GET):
            value = request.GET[param]
            url = replace_query_param(url, param, value)

    return url


def reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    scheme = getattr(request, 'versioning_scheme', None)
    if scheme is not None:
        try:
            url = scheme.reverse(viewname, args, kwargs, request, format, **extra)
        except NoReverseMatch:
            url = _reverse(viewname, args, kwargs, request, format, **extra)
    else:
        url = _reverse(viewname, args, kwargs, request, format, **extra)

    return preserve_builtin_query_params(url, request)


def _reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    if format is not None:
        kwargs = kwargs or {}
        kwargs['format'] = format
    url = django_reverse(viewname, args=args, kwargs=kwargs, **extra)
    if request:
        return request.build_absolute_uri(url)
    return url


~~reverse_lazy = lazy(reverse, str)



## ... source file continues with no further lazy examples...

```


## Example 3 from django-wiki
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

[**django-wiki / src/wiki / models / __init__.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/models/__init__.py)

```python
# __init__.py
from django import shortcuts
from django import urls
from django.urls import base
~~from django.utils.functional import lazy

from .article import *  # noqa
from .pluginbase import *  # noqa
from .urlpath import *  # noqa

original_django_reverse = urls.reverse


def reverse(*args, **kwargs):
    if isinstance(args[0], str) and args[0].startswith("wiki:"):
        url_kwargs = kwargs.get("kwargs", {})
        path = url_kwargs.get("path", False)
        if path is not False:
            url_kwargs.pop("article_id", None)
            url_kwargs["path"] = path
            kwargs["kwargs"] = url_kwargs

        url = original_django_reverse(*args, **kwargs)
        if hasattr(reverse, "_transform_url"):
            url = reverse._transform_url(url)
    else:
        url = original_django_reverse(*args, **kwargs)

    return url


~~reverse_lazy = lazy(reverse, str)


base.reverse = reverse
base.reverse_lazy = reverse_lazy
urls.reverse = reverse
urls.reverse_lazy = reverse_lazy
shortcuts.reverse = reverse



## ... source file continues with no further lazy examples...

```

