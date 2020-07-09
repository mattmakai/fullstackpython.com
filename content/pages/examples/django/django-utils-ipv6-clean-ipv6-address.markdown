title: django.utils.ipv6 clean_ipv6_address Example Code
category: page
slug: django-utils-ipv6-clean-ipv6-address-examples
sortorder: 500011478
toc: False
sidebartitle: django.utils.ipv6 clean_ipv6_address
meta: Python example code for the clean_ipv6_address callable from the django.utils.ipv6 module of the Django project.


clean_ipv6_address is a callable within the django.utils.ipv6 module of the Django project.


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
from django.utils.duration import duration_string
from django.utils.encoding import is_protected_type, smart_str
from django.utils.formats import localize_input, sanitize_separators
~~from django.utils.ipv6 import clean_ipv6_address
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


def is_simple_callable(obj):
    if inspect.isbuiltin(obj):


## ... source file abbreviated to get to clean_ipv6_address examples ...


            return str(value)
        else:
            return getattr(value, self.uuid_format)


class IPAddressField(CharField):

    default_error_messages = {
        'invalid': _('Enter a valid IPv4 or IPv6 address.'),
    }

    def __init__(self, protocol='both', **kwargs):
        self.protocol = protocol.lower()
        self.unpack_ipv4 = (self.protocol == 'both')
        super().__init__(**kwargs)
        validators, error_message = ip_address_validators(protocol, self.unpack_ipv4)
        self.validators.extend(validators)

    def to_internal_value(self, data):
        if not isinstance(data, str):
            self.fail('invalid', value=data)

        if ':' in data:
            try:
                if self.protocol in ('both', 'ipv6'):
~~                    return clean_ipv6_address(data, self.unpack_ipv4)
            except DjangoValidationError:
                self.fail('invalid', value=data)

        return super().to_internal_value(data)



class IntegerField(Field):
    default_error_messages = {
        'invalid': _('A valid integer is required.'),
        'max_value': _('Ensure this value is less than or equal to {max_value}.'),
        'min_value': _('Ensure this value is greater than or equal to {min_value}.'),
        'max_string_length': _('String value too large.')
    }
    MAX_STRING_LENGTH = 1000  # Guard against malicious string inputs.
    re_decimal = re.compile(r'\.0*\s*$')  # allow e.g. '1.0' as an int, but not '1.2'

    def __init__(self, **kwargs):
        self.max_value = kwargs.pop('max_value', None)
        self.min_value = kwargs.pop('min_value', None)
        super().__init__(**kwargs)
        if self.max_value is not None:
            message = lazy_format(self.error_messages['max_value'], max_value=self.max_value)
            self.validators.append(


## ... source file continues with no further clean_ipv6_address examples...

```

