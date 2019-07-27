title: django.db.models CharField Example Code
category: page
slug: django-db-models-charfield-examples
sortorder: 50101
toc: False
sidebartitle: django.db.models CharField
meta: Python code examples for the CharField class used in the Django ORM, found within the django.db.models module of the Django project. 


[CharField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a commonly-defined field used as an attribute to reference a
text-based [database](/databases.html) column when defining 
[Model](/django-db-models-model-examples.html) classes with
the [Django ORM](/django-orm.html).

The [Django](/django.html) project has wonderful documentation for
[CharField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.CharField)
and all of the other column fields.

Note that `CharField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a code library for [Django](/django.html) that allows users to send 
HTTP requests from the Django admin user interface. The code for
the project is open source under the 
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / models.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/models.py)

```python
# -*- coding: utf-8 -*-

~~from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from requests import Request as HTTPRequest, Session
from requests.cookies import create_cookie, RequestsCookieJar
from urllib.parse import parse_qs, urlparse, urlencode
from requests_toolbelt.utils import dump

from model_utils.models import TimeStampedModel

from smithy.helpers import render_with_context, parse_dump_result


class NameValueModel(TimeStampedModel):
~~    name = models.CharField(max_length = 200)
    value = models.TextField(blank = True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Request(TimeStampedModel):
    """
    A base model shared by RequestBlueprint and
    RequestRecord. Used solely to reduce
    """
    METHODS = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('OPTIONS', 'OPTIONS'),
        ('HEAD', 'HEAD'),
    )
    BODY_TYPES = (
        ('', 'Other'),
        ('application/x-www-form-urlencoded', 'x-www-form-urlencoded'),
        ('application/json', 'JSON'),
        ('text/plain', 'Text'),
        ('application/javascript', 'JavaScript'),
        ('application/xml', 'XML (application/xml)'),
        ('text/xml', 'XML (text/xml)'),
        ('text/html', 'HTML'),
    )
~~    method = models.CharField(
~~        max_length = 7, choices = METHODS,
~~        blank = False, null = False)
~~    name = models.CharField(max_length = 500, blank = False)
~~    url = models.CharField(max_length = 2083)
    body = models.TextField(blank = True)
~~    content_type = models.CharField(
~~        default = BODY_TYPES[0][0],
~~        blank = True, null = True,
~~        max_length = 100, choices = BODY_TYPES)

    def __str__(self):
        if self.name:
            return self.name
        return "{} {}".format(
            self.method,
            self.url,
        )


## source file continues from here without further CharField examples
```
