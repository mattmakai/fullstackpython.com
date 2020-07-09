title: django.urls get_script_prefix Example Code
category: page
slug: django-urls-get-script-prefix-examples
sortorder: 500011405
toc: False
sidebartitle: django.urls get_script_prefix
meta: Python example code for the get_script_prefix callable from the django.urls module of the Django project.


get_script_prefix is a callable within the django.urls module of the Django project.


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

[**django-rest-framework / rest_framework / relations.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./relations.py)

```python
# relations.py
import sys
from collections import OrderedDict
from urllib import parse

from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.db.models import Manager
from django.db.models.query import QuerySet
~~from django.urls import NoReverseMatch, Resolver404, get_script_prefix, resolve
from django.utils.encoding import smart_str, uri_to_iri
from django.utils.translation import gettext_lazy as _

from rest_framework.fields import (
    Field, empty, get_attribute, is_simple_callable, iter_options
)
from rest_framework.reverse import reverse
from rest_framework.settings import api_settings
from rest_framework.utils import html


def method_overridden(method_name, klass, instance):
    method = getattr(klass, method_name)
    default_method = getattr(method, '__func__', method)  # Python 3 compat
    return default_method is not getattr(instance, method_name).__func__


class ObjectValueError(ValueError):


class ObjectTypeError(TypeError):


class Hyperlink(str):


## ... source file abbreviated to get to get_script_prefix examples ...


            return queryset.get(**lookup_kwargs)
        except ValueError:
            exc = ObjectValueError(str(sys.exc_info()[1]))
            raise exc.with_traceback(sys.exc_info()[2])
        except TypeError:
            exc = ObjectTypeError(str(sys.exc_info()[1]))
            raise exc.with_traceback(sys.exc_info()[2])

    def get_url(self, obj, view_name, request, format):
        if hasattr(obj, 'pk') and obj.pk in (None, ''):
            return None

        lookup_value = getattr(obj, self.lookup_field)
        kwargs = {self.lookup_url_kwarg: lookup_value}
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

    def to_internal_value(self, data):
        request = self.context.get('request', None)
        try:
            http_prefix = data.startswith(('http:', 'https:'))
        except AttributeError:
            self.fail('incorrect_type', data_type=type(data).__name__)

        if http_prefix:
            data = parse.urlparse(data).path
~~            prefix = get_script_prefix()
            if data.startswith(prefix):
                data = '/' + data[len(prefix):]

        data = uri_to_iri(parse.unquote(data))

        try:
            match = resolve(data)
        except Resolver404:
            self.fail('no_match')

        try:
            expected_viewname = request.versioning_scheme.get_versioned_viewname(
                self.view_name, request
            )
        except AttributeError:
            expected_viewname = self.view_name

        if match.view_name != expected_viewname:
            self.fail('incorrect_match')

        try:
            return self.get_object(match.view_name, match.args, match.kwargs)
        except (ObjectDoesNotExist, ObjectValueError, ObjectTypeError):
            self.fail('does_not_exist')


## ... source file continues with no further get_script_prefix examples...

```

