title: django.utils.http base36_to_int Example Code
category: page
slug: django-utils-http-base36-to-int-examples
sortorder: 500011469
toc: False
sidebartitle: django.utils.http base36_to_int
meta: Python example code for the base36_to_int callable from the django.utils.http module of the Django project.


base36_to_int is a callable within the django.utils.http module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / tests.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/./tests.py)

```python
# tests.py
from __future__ import unicode_literals

import json
import requests
from datetime import date, datetime

import django
from django.core.files.base import ContentFile
from django.db import models
from django.test import RequestFactory, TestCase
~~from django.utils.http import base36_to_int, int_to_base36
from django.views import csrf

from . import utils


try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch  # noqa


class MockedResponse(object):
    def __init__(self, status_code, content, headers=None):
        if headers is None:
            headers = {}

        self.status_code = status_code
        self.content = content.encode('utf8')
        self.headers = headers

    def json(self):
        return json.loads(self.text)

    def raise_for_status(self):


## ... source file abbreviated to get to base36_to_int examples ...


        instance = SomeBinaryModel(bb=b'some binary data')

        serialized = utils.serialize_instance(instance)
        deserialized = utils.deserialize_instance(SomeBinaryModel, serialized)

        self.assertEqual(serialized['bb'], 'c29tZSBiaW5hcnkgZGF0YQ==')
        self.assertEqual(serialized['bb_empty'], '')
        self.assertEqual(deserialized.bb, b'some binary data')
        self.assertEqual(deserialized.bb_empty, b'')

    def test_build_absolute_uri(self):
        self.assertEqual(
            utils.build_absolute_uri(None, '/foo'),
            'http://example.com/foo')
        self.assertEqual(
            utils.build_absolute_uri(None, '/foo', protocol='ftp'),
            'ftp://example.com/foo')
        self.assertEqual(
            utils.build_absolute_uri(None, 'http://foo.com/bar'),
            'http://foo.com/bar')

    def test_int_to_base36(self):
        n = 55798679658823689999
        b36 = 'brxk553wvxbf3'
        assert int_to_base36(n) == b36
~~        assert base36_to_int(b36) == n

    def test_templatetag_with_csrf_failure(self):
        request = self.factory.get('/tests/test_403_csrf.html')
        response = csrf.csrf_failure(
            request,
            template_name='tests/test_403_csrf.html'
        )
        self.assertEqual(response.status_code, 403)



## ... source file continues with no further base36_to_int examples...

```

