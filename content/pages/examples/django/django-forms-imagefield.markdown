title: django.forms ImageField Example Code
category: page
slug: django-forms-imagefield-examples
sortorder: 500011269
toc: False
sidebartitle: django.forms ImageField
meta: Python example code for the ImageField class from the django.forms module of the Django project.


ImageField is a class within the django.forms module of the Django project.


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

[**django-rest-framework / rest_framework / fields.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./fields.py)

```python
# fields.py
import copy
import datetime
import decimal
import functools
import inspect
import re
import uuid
import warnings
from collections import OrderedDict
from collections.abc import Mapping

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import (
    EmailValidator, MaxLengthValidator, MaxValueValidator, MinLengthValidator,
    MinValueValidator, ProhibitNullCharactersValidator, RegexValidator,
    URLValidator, ip_address_validators
)
from django.forms import FilePathField as DjangoFilePathField
~~from django.forms import ImageField as DjangoImageField
from django.utils import timezone
from django.utils.dateparse import (
    parse_date, parse_datetime, parse_duration, parse_time
)
from django.utils.duration import duration_string
from django.utils.encoding import is_protected_type, smart_str
from django.utils.formats import localize_input, sanitize_separators
from django.utils.ipv6 import clean_ipv6_address
from django.utils.timezone import utc
from django.utils.translation import gettext_lazy as _
from pytz.exceptions import InvalidTimeError

from rest_framework import (
    ISO_8601, RemovedInDRF313Warning, RemovedInDRF314Warning
)
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.settings import api_settings
from rest_framework.utils import html, humanize_datetime, json, representation
from rest_framework.utils.formatting import lazy_format
from rest_framework.validators import ProhibitSurrogateCharactersValidator


class empty:
    pass


## ... source file abbreviated to get to ImageField examples ...


        if not self.allow_empty_file and not file_size:
            self.fail('empty')
        if self.max_length and len(file_name) > self.max_length:
            self.fail('max_length', max_length=self.max_length, length=len(file_name))

        return data

    def to_representation(self, value):
        if not value:
            return None

        use_url = getattr(self, 'use_url', api_settings.UPLOADED_FILES_USE_URL)
        if use_url:
            try:
                url = value.url
            except AttributeError:
                return None
            request = self.context.get('request', None)
            if request is not None:
                return request.build_absolute_uri(url)
            return url

        return value.name


~~class ImageField(FileField):
    default_error_messages = {
        'invalid_image': _(
            'Upload a valid image. The file you uploaded was either not an image or a corrupted image.'
        ),
    }

    def __init__(self, *args, **kwargs):
        self._DjangoImageField = kwargs.pop('_DjangoImageField', DjangoImageField)
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        file_object = super().to_internal_value(data)
        django_field = self._DjangoImageField()
        django_field.error_messages = self.error_messages
        return django_field.clean(file_object)



class _UnvalidatedField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allow_blank = True
        self.allow_null = True



## ... source file continues with no further ImageField examples...

```

