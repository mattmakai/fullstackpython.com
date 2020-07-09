title: django.urls URLPattern Example Code
category: page
slug: django-urls-urlpattern-examples
sortorder: 500011400
toc: False
sidebartitle: django.urls URLPattern
meta: Python example code for the URLPattern class from the django.urls module of the Django project.


URLPattern is a class within the django.urls module of the Django project.


## Example 1 from django-rest-framework
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

[**django-rest-framework / rest_framework / schemas / generators.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/schemas/generators.py)

```python
# generators.py
import re
from importlib import import_module

from django.conf import settings
from django.contrib.admindocs.views import simplify_regex
from django.core.exceptions import PermissionDenied
from django.http import Http404
~~from django.urls import URLPattern, URLResolver

from rest_framework import exceptions
from rest_framework.request import clone_request
from rest_framework.settings import api_settings
from rest_framework.utils.model_meta import _get_pk


def get_pk_name(model):
    meta = model._meta.concrete_model._meta
    return _get_pk(meta).name


def is_api_view(callback):
    from rest_framework.views import APIView
    cls = getattr(callback, 'cls', None)
    return (cls is not None) and issubclass(cls, APIView)


def endpoint_ordering(endpoint):
    path, method, callback = endpoint
    method_priority = {
        'GET': 0,
        'POST': 1,
        'PUT': 2,


## ... source file abbreviated to get to URLPattern examples ...


)


class EndpointEnumerator:
    def __init__(self, patterns=None, urlconf=None):
        if patterns is None:
            if urlconf is None:
                urlconf = settings.ROOT_URLCONF

            if isinstance(urlconf, str):
                urls = import_module(urlconf)
            else:
                urls = urlconf
            patterns = urls.urlpatterns

        self.patterns = patterns

    def get_api_endpoints(self, patterns=None, prefix=''):
        if patterns is None:
            patterns = self.patterns

        api_endpoints = []

        for pattern in patterns:
            path_regex = prefix + str(pattern.pattern)
~~            if isinstance(pattern, URLPattern):
                path = self.get_path_from_regex(path_regex)
                callback = pattern.callback
                if self.should_include_endpoint(path, callback):
                    for method in self.get_allowed_methods(callback):
                        endpoint = (path, method, callback)
                        api_endpoints.append(endpoint)

            elif isinstance(pattern, URLResolver):
                nested_endpoints = self.get_api_endpoints(
                    patterns=pattern.url_patterns,
                    prefix=path_regex
                )
                api_endpoints.extend(nested_endpoints)

        return sorted(api_endpoints, key=endpoint_ordering)

    def get_path_from_regex(self, path_regex):

        path = simplify_regex(path_regex)

        return re.sub(_PATH_PARAMETER_COMPONENT_RE, r'{\g<parameter>}', path)

    def should_include_endpoint(self, path, callback):
        if not is_api_view(callback):


## ... source file continues with no further URLPattern examples...

```

