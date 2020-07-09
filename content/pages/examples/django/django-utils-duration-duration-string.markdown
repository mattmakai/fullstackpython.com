title: django.utils.duration duration_string Example Code
category: page
slug: django-utils-duration-duration-string-examples
sortorder: 500011439
toc: False
sidebartitle: django.utils.duration duration_string
meta: Python example code for the duration_string callable from the django.utils.duration module of the Django project.


duration_string is a callable within the django.utils.duration module of the Django project.


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
from django.forms import ImageField as DjangoImageField
from django.utils import timezone
from django.utils.dateparse import (
    parse_date, parse_datetime, parse_duration, parse_time
)
~~from django.utils.duration import duration_string
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


class BuiltinSignatureError(Exception):
    pass



## ... source file abbreviated to get to duration_string examples ...


        'min_value': _('Ensure this value is greater than or equal to {min_value}.'),
    }

    def __init__(self, **kwargs):
        self.max_value = kwargs.pop('max_value', None)
        self.min_value = kwargs.pop('min_value', None)
        super().__init__(**kwargs)
        if self.max_value is not None:
            message = lazy_format(self.error_messages['max_value'], max_value=self.max_value)
            self.validators.append(
                MaxValueValidator(self.max_value, message=message))
        if self.min_value is not None:
            message = lazy_format(self.error_messages['min_value'], min_value=self.min_value)
            self.validators.append(
                MinValueValidator(self.min_value, message=message))

    def to_internal_value(self, value):
        if isinstance(value, datetime.timedelta):
            return value
        parsed = parse_duration(str(value))
        if parsed is not None:
            return parsed
        self.fail('invalid', format='[DD] [HH:[MM:]]ss[.uuuuuu]')

    def to_representation(self, value):
~~        return duration_string(value)



class ChoiceField(Field):
    default_error_messages = {
        'invalid_choice': _('"{input}" is not a valid choice.')
    }
    html_cutoff = None
    html_cutoff_text = _('More than {count} items...')

    def __init__(self, choices, **kwargs):
        self.choices = choices
        self.html_cutoff = kwargs.pop('html_cutoff', self.html_cutoff)
        self.html_cutoff_text = kwargs.pop('html_cutoff_text', self.html_cutoff_text)

        self.allow_blank = kwargs.pop('allow_blank', False)

        super().__init__(**kwargs)

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        try:


## ... source file continues with no further duration_string examples...

```

