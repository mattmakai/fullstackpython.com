title: django.urls URLResolver Example Code
category: page
slug: django-urls-urlresolver-examples
sortorder: 500011401
toc: False
sidebartitle: django.urls URLResolver
meta: Python example code for the URLResolver class from the django.urls module of the Django project.


URLResolver is a class within the django.urls module of the Django project.


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

[**django-rest-framework / rest_framework / urlpatterns.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./urlpatterns.py)

```python
# urlpatterns.py
from django.conf.urls import include, url
~~from django.urls import URLResolver, path, register_converter
from django.urls.resolvers import RoutePattern

from rest_framework.settings import api_settings


def _get_format_path_converter(suffix_kwarg, allowed):
    if allowed:
        if len(allowed) == 1:
            allowed_pattern = allowed[0]
        else:
            allowed_pattern = '(?:%s)' % '|'.join(allowed)
        suffix_pattern = r"\.%s/?" % allowed_pattern
    else:
        suffix_pattern = r"\.[a-z0-9]+/?"

    class FormatSuffixConverter:
        regex = suffix_pattern

        def to_python(self, value):
            return value.strip('./')

        def to_url(self, value):
            return '.' + value + '/'

    converter_name = 'drf_format_suffix'
    if allowed:
        converter_name += '_' + '_'.join(allowed)

    return converter_name, FormatSuffixConverter


def apply_suffix_patterns(urlpatterns, suffix_pattern, suffix_required, suffix_route=None):
    ret = []
    for urlpattern in urlpatterns:
~~        if isinstance(urlpattern, URLResolver):
            regex = urlpattern.pattern.regex.pattern
            namespace = urlpattern.namespace
            app_name = urlpattern.app_name
            kwargs = urlpattern.default_kwargs
            patterns = apply_suffix_patterns(urlpattern.url_patterns,
                                             suffix_pattern,
                                             suffix_required,
                                             suffix_route)

            if isinstance(urlpattern.pattern, RoutePattern):
                assert path is not None
                route = str(urlpattern.pattern)
                new_pattern = path(route, include((patterns, app_name), namespace), kwargs)
            else:
                new_pattern = url(regex, include((patterns, app_name), namespace), kwargs)

            ret.append(new_pattern)
        else:
            regex = urlpattern.pattern.regex.pattern.rstrip('$').rstrip('/') + suffix_pattern
            view = urlpattern.callback
            kwargs = urlpattern.default_args
            name = urlpattern.name
            if not suffix_required:
                ret.append(urlpattern)


## ... source file continues with no further URLResolver examples...

```

