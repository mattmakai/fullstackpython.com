title: django.utils.encoding force_bytes Example Code
category: page
slug: django-utils-encoding-force-bytes-examples
sortorder: 500011442
toc: False
sidebartitle: django.utils.encoding force_bytes
meta: Python example code for the force_bytes callable from the django.utils.encoding module of the Django project.


force_bytes is a callable within the django.utils.encoding module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / utils.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/./utils.py)

```python
# utils.py
import base64
import importlib
import json
import random
import re
import string
import unicodedata
from collections import OrderedDict
from urllib.parse import urlsplit

import django
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.exceptions import FieldDoesNotExist, ImproperlyConfigured
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import ValidationError, validate_email
from django.db.models import FileField
from django.db.models.fields import (
    BinaryField,
    DateField,
    DateTimeField,
    EmailField,
    TimeField,
)
from django.utils import dateparse
~~from django.utils.encoding import force_bytes, force_str


MAX_USERNAME_SUFFIX_LENGTH = 7
USERNAME_SUFFIX_CHARS = (
    [string.digits] * 4 +
    [string.ascii_letters] * (MAX_USERNAME_SUFFIX_LENGTH - 4))


def _generate_unique_username_base(txts, regex=None):
    from .account.adapter import get_adapter
    adapter = get_adapter()
    username = None
    regex = regex or r'[^\w\s@+.-]'
    for txt in txts:
        if not txt:
            continue
        username = unicodedata.normalize('NFKD', force_str(txt))
        username = username.encode('ascii', 'ignore').decode('ascii')
        username = force_str(re.sub(regex, '', username).lower())
        username = username.split('@')[0]
        username = username.strip()
        username = re.sub(r'\s+', '_', username)
        try:
            username = adapter.clean_username(username, shallow=True)


## ... source file abbreviated to get to force_bytes examples ...


                v = field.get_prep_value(v)
                k = SERIALIZED_DB_FIELD_PREFIX + k
        except FieldDoesNotExist:
            pass
        data[k] = v
    return json.loads(json.dumps(data, cls=DjangoJSONEncoder))


def deserialize_instance(model, data):
    ret = model()
    for k, v in data.items():
        is_db_value = False
        if k.startswith(SERIALIZED_DB_FIELD_PREFIX):
            k = k[len(SERIALIZED_DB_FIELD_PREFIX):]
            is_db_value = True
        if v is not None:
            try:
                f = model._meta.get_field(k)
                if isinstance(f, DateTimeField):
                    v = dateparse.parse_datetime(v)
                elif isinstance(f, TimeField):
                    v = dateparse.parse_time(v)
                elif isinstance(f, DateField):
                    v = dateparse.parse_date(v)
                elif isinstance(f, BinaryField):
~~                    v = force_bytes(
                        base64.b64decode(
~~                            force_bytes(v)))
                elif is_db_value:
                    try:
                        if django.VERSION < (3, 0):
                            v = f.from_db_value(v, None, None, None)
                        else:
                            v = f.from_db_value(v, None, None)
                    except Exception:
                        raise ImproperlyConfigured(
                            "Unable to auto serialize field '{}', custom"
                            " serialization override required".format(k)
                        )
            except FieldDoesNotExist:
                pass
        setattr(ret, k, v)
    return ret


def set_form_field_order(form, field_order):
    if field_order is None:
        return
    fields = OrderedDict()
    for key in field_order:
        try:
            fields[key] = form.fields.pop(key)


## ... source file continues with no further force_bytes examples...

```


## Example 2 from django-downloadview
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

[**django-downloadview / django_downloadview / io.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/./io.py)

```python
# io.py
import io

~~from django.utils.encoding import force_bytes, force_text


class TextIteratorIO(io.TextIOBase):

    def __init__(self, iterator):
        self._iter = iterator

        self._left = ""

    def readable(self):
        return True

    def _read1(self, n=None):
        while not self._left:
            try:
                self._left = next(self._iter)
            except StopIteration:
                break
            else:
                self._left = force_text(self._left)
        ret = self._left[:n]
        self._left = self._left[len(ret) :]
        return ret



## ... source file abbreviated to get to force_bytes examples ...


                    break
            else:
                chunks.append(self._left[: i + 1])
                self._left = self._left[i + 1 :]
                break
        return "".join(chunks)


class BytesIteratorIO(io.BytesIO):

    def __init__(self, iterator):
        self._iter = iterator

        self._left = b""

    def readable(self):
        return True

    def _read1(self, n=None):
        while not self._left:
            try:
                self._left = next(self._iter)
            except StopIteration:
                break
            else:
~~                self._left = force_bytes(self._left)
        ret = self._left[:n]
        self._left = self._left[len(ret) :]
        return ret

    def read(self, n=None):
        chunks = []
        if n is None or n < 0:
            while True:
                m = self._read1()
                if not m:
                    break
                chunks.append(m)
        else:
            while n > 0:
                m = self._read1(n)
                if not m:
                    break
                n -= len(m)
                chunks.append(m)
        return b"".join(chunks)

    def readline(self):
        chunks = []
        while True:


## ... source file continues with no further force_bytes examples...

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

[**django-rest-framework / rest_framework / test.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./test.py)

```python
# test.py
import io
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.handlers.wsgi import WSGIHandler
from django.test import override_settings, testcases
from django.test.client import Client as DjangoClient
from django.test.client import ClientHandler
from django.test.client import RequestFactory as DjangoRequestFactory
~~from django.utils.encoding import force_bytes
from django.utils.http import urlencode

from rest_framework.compat import coreapi, requests
from rest_framework.settings import api_settings


def force_authenticate(request, user=None, token=None):
    request._force_auth_user = user
    request._force_auth_token = token


if requests is not None:
    class HeaderDict(requests.packages.urllib3._collections.HTTPHeaderDict):
        def get_all(self, key, default):
            return self.getheaders(key)

    class MockOriginalResponse:
        def __init__(self, headers):
            self.msg = HeaderDict(headers)
            self.closed = False

        def isclosed(self):
            return self.closed



## ... source file abbreviated to get to force_bytes examples ...


    def CoreAPIClient(*args, **kwargs):
        raise ImproperlyConfigured('coreapi must be installed in order to use CoreAPIClient.')


class APIRequestFactory(DjangoRequestFactory):
    renderer_classes_list = api_settings.TEST_REQUEST_RENDERER_CLASSES
    default_format = api_settings.TEST_REQUEST_DEFAULT_FORMAT

    def __init__(self, enforce_csrf_checks=False, **defaults):
        self.enforce_csrf_checks = enforce_csrf_checks
        self.renderer_classes = {}
        for cls in self.renderer_classes_list:
            self.renderer_classes[cls.format] = cls
        super().__init__(**defaults)

    def _encode_data(self, data, format=None, content_type=None):

        if data is None:
            return ('', content_type)

        assert format is None or content_type is None, (
            'You may not set both `format` and `content_type`.'
        )

        if content_type:
~~            ret = force_bytes(data, settings.DEFAULT_CHARSET)

        else:
            format = format or self.default_format

            assert format in self.renderer_classes, (
                "Invalid format '{}'. Available formats are {}. "
                "Set TEST_REQUEST_RENDERER_CLASSES to enable "
                "extra request formats.".format(
                    format,
                    ', '.join(["'" + fmt + "'" for fmt in self.renderer_classes])
                )
            )

            renderer = self.renderer_classes[format]()
            ret = renderer.render(data)

            content_type = "{}; charset={}".format(
                renderer.media_type, renderer.charset
            )

            if isinstance(ret, str):
                ret = ret.encode(renderer.charset)

        return ret, content_type

    def get(self, path, data=None, **extra):
        r = {
            'QUERY_STRING': urlencode(data or {}, doseq=True),
        }
        if not data and '?' in path:
~~            query_string = force_bytes(path.split('?')[1])
            query_string = query_string.decode('iso-8859-1')
            r['QUERY_STRING'] = query_string
        r.update(extra)
        return self.generic('GET', path, **r)

    def post(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('POST', path, data, content_type, **extra)

    def put(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('PUT', path, data, content_type, **extra)

    def patch(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('PATCH', path, data, content_type, **extra)

    def delete(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('DELETE', path, data, content_type, **extra)

    def options(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('OPTIONS', path, data, content_type, **extra)


## ... source file continues with no further force_bytes examples...

```

