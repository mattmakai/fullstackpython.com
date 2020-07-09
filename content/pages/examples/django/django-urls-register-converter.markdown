title: django.urls register_converter Example Code
category: page
slug: django-urls-register-converter-examples
sortorder: 500011409
toc: False
sidebartitle: django.urls register_converter
meta: Python example code for the register_converter callable from the django.urls module of the Django project.


register_converter is a callable within the django.urls module of the Django project.


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



## ... source file abbreviated to get to register_converter examples ...


                assert path is not None
                assert suffix_route is not None
                route = str(urlpattern.pattern).rstrip('$').rstrip('/') + suffix_route
                new_pattern = path(route, view, kwargs, name)
            else:
                new_pattern = url(regex, view, kwargs, name)

            ret.append(new_pattern)

    return ret


def format_suffix_patterns(urlpatterns, suffix_required=False, allowed=None):
    suffix_kwarg = api_settings.FORMAT_SUFFIX_KWARG
    if allowed:
        if len(allowed) == 1:
            allowed_pattern = allowed[0]
        else:
            allowed_pattern = '(%s)' % '|'.join(allowed)
        suffix_pattern = r'\.(?P<%s>%s)/?$' % (suffix_kwarg, allowed_pattern)
    else:
        suffix_pattern = r'\.(?P<%s>[a-z0-9]+)/?$' % suffix_kwarg

    if path and register_converter:
        converter_name, suffix_converter = _get_format_path_converter(suffix_kwarg, allowed)
~~        register_converter(suffix_converter, converter_name)

        suffix_route = '<%s:%s>' % (converter_name, suffix_kwarg)
    else:
        suffix_route = None

    return apply_suffix_patterns(urlpatterns, suffix_pattern, suffix_required, suffix_route)



## ... source file continues with no further register_converter examples...

```

