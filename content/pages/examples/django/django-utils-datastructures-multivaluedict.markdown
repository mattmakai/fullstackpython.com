title: django.utils.datastructures MultiValueDict Example Code
category: page
slug: django-utils-datastructures-multivaluedict-examples
sortorder: 500011431
toc: False
sidebartitle: django.utils.datastructures MultiValueDict
meta: Python example code for the MultiValueDict class from the django.utils.datastructures module of the Django project.


MultiValueDict is a class within the django.utils.datastructures module of the Django project.


## Example 1 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / widgets.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./widgets.py)

```python
# widgets.py
from collections.abc import Iterable
from copy import deepcopy
from itertools import chain
from re import search, sub

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.utils import flatatt
~~from django.utils.datastructures import MultiValueDict
from django.utils.encoding import force_str
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


class LinkWidget(forms.Widget):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs)

        self.choices = choices

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        self.data = data
        return value

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        if not hasattr(self, 'data'):
            self.data = {}
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, extra_attrs=attrs)
        output = ['<ul%s>' % flatatt(final_attrs)]


## ... source file abbreviated to get to MultiValueDict examples ...


        if len(value) <= 1:
            value = value[0] if value else ''
            return super().render(name, value, attrs, renderer=renderer)

        value = [force_str(self.surrogate.format_value(v)) for v in value]
        value = ','.join(list(value))

        return self.surrogate.render(name, value, attrs, renderer=renderer)


class CSVWidget(BaseCSVWidget, forms.TextInput):
    def __init__(self, *args, attrs=None, **kwargs):
        super().__init__(*args, attrs, **kwargs)

        if attrs is not None:
            self.surrogate.attrs.update(attrs)


class QueryArrayWidget(BaseCSVWidget, forms.TextInput):

    def value_from_datadict(self, data, files, name):
~~        if not isinstance(data, MultiValueDict):
            for key, value in data.items():
                if isinstance(value, str):
                    data[key] = [x.strip() for x in value.rstrip(',').split(',') if x]
~~            data = MultiValueDict(data)

        values_list = data.getlist(name, data.getlist('%s[]' % name)) or []

        if len(values_list) > 0:
            ret = [x for x in values_list if x]
        else:
            ret = []

        return list(set(ret))

    def render(self, name, value, attrs=None, renderer=None):
        if not self._isiterable(value):
            value = [value]



## ... source file continues with no further MultiValueDict examples...

```


## Example 2 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / compat.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/./compat.py)

```python
# compat.py
from contextlib import contextmanager

import django
from django.template import Context
~~from django.utils.datastructures import MultiValueDict

MULTIVALUE_DICT_TYPES = (MultiValueDict,)


REQUIRED_CONTEXT_ATTRIBTUES = (
    '_form_config',
    '_form_render',
)


class DictContext(dict):
    pass


if django.VERSION < (1, 8):
    def get_template(context, template_name):
        from django.template.loader import get_template
        return get_template(template_name)

    def get_context(context):
        if not isinstance(context, Context):
            context = Context(context)
        return context



## ... source file continues with no further MultiValueDict examples...

```


## Example 3 from django-rest-framework
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

[**django-rest-framework / rest_framework / request.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./request.py)

```python
# request.py
import io
import sys
from contextlib import contextmanager

from django.conf import settings
from django.http import HttpRequest, QueryDict
from django.http.multipartparser import parse_header
from django.http.request import RawPostDataException
~~from django.utils.datastructures import MultiValueDict

from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework.settings import api_settings


def is_form_media_type(media_type):
    base_media_type, params = parse_header(media_type.encode(HTTP_HEADER_ENCODING))
    return (base_media_type == 'application/x-www-form-urlencoded' or
            base_media_type == 'multipart/form-data')


class override_method:

    def __init__(self, view, request, method):
        self.view = view
        self.request = request
        self.method = method
        self.action = getattr(view, 'action', None)

    def __enter__(self):
        self.view.request = clone_request(self.request, self.method)
        action_map = getattr(self.view, 'action_map', {})
        self.view.action = action_map.get(self.method.lower())
        return self.view.request


## ... source file abbreviated to get to MultiValueDict examples ...


            self._stream = io.BytesIO(self.body)

    def _supports_form_parsing(self):
        form_media = (
            'application/x-www-form-urlencoded',
            'multipart/form-data'
        )
        return any([parser.media_type in form_media for parser in self.parsers])

    def _parse(self):
        media_type = self.content_type
        try:
            stream = self.stream
        except RawPostDataException:
            if not hasattr(self._request, '_post'):
                raise
            if self._supports_form_parsing():
                return (self._request.POST, self._request.FILES)
            stream = None

        if stream is None or media_type is None:
            if media_type and is_form_media_type(media_type):
                empty_data = QueryDict('', encoding=self._request._encoding)
            else:
                empty_data = {}
~~            empty_files = MultiValueDict()
            return (empty_data, empty_files)

        parser = self.negotiator.select_parser(self, self.parsers)

        if not parser:
            raise exceptions.UnsupportedMediaType(media_type)

        try:
            parsed = parser.parse(stream, media_type, self.parser_context)
        except Exception:
            self._data = QueryDict('', encoding=self._request._encoding)
~~            self._files = MultiValueDict()
            self._full_data = self._data
            raise

        try:
            return (parsed.data, parsed.files)
        except AttributeError:
~~            empty_files = MultiValueDict()
            return (parsed, empty_files)

    def _authenticate(self):
        for authenticator in self.authenticators:
            try:
                user_auth_tuple = authenticator.authenticate(self)
            except exceptions.APIException:
                self._not_authenticated()
                raise

            if user_auth_tuple is not None:
                self._authenticator = authenticator
                self.user, self.auth = user_auth_tuple
                return

        self._not_authenticated()

    def _not_authenticated(self):
        self._authenticator = None

        if api_settings.UNAUTHENTICATED_USER:
            self.user = api_settings.UNAUTHENTICATED_USER()
        else:
            self.user = None


## ... source file continues with no further MultiValueDict examples...

```

