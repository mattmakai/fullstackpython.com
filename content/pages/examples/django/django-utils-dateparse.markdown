title: django.utils dateparse Example Code
category: page
slug: django-utils-dateparse-examples
sortorder: 500011416
toc: False
sidebartitle: django.utils dateparse
meta: Python example code for the dateparse callable from the django.utils module of the Django project.


dateparse is a callable within the django.utils module of the Django project.


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
~~from django.utils import dateparse
from django.utils.encoding import force_bytes, force_str


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


## ... source file abbreviated to get to dateparse examples ...


            elif isinstance(field, FileField):
                if v and not isinstance(v, str):
                    v = v.name
            try:
                json.dumps(v, cls=DjangoJSONEncoder)
            except TypeError:
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
~~                    v = dateparse.parse_datetime(v)
                elif isinstance(f, TimeField):
~~                    v = dateparse.parse_time(v)
                elif isinstance(f, DateField):
~~                    v = dateparse.parse_date(v)
                elif isinstance(f, BinaryField):
                    v = force_bytes(
                        base64.b64decode(
                            force_bytes(v)))
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


## ... source file continues with no further dateparse examples...

```

