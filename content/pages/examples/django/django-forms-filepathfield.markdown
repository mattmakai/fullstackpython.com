title: django.forms FilePathField Example Code
category: page
slug: django-forms-filepathfield-examples
sortorder: 500011266
toc: False
sidebartitle: django.forms FilePathField
meta: Python example code for the FilePathField class from the django.forms module of the Django project.


FilePathField is a class within the django.forms module of the Django project.


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
~~from django.forms import FilePathField as DjangoFilePathField
from django.forms import ImageField as DjangoImageField
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


## ... source file abbreviated to get to FilePathField examples ...


    def get_value(self, dictionary):
        if self.field_name not in dictionary:
            if getattr(self.root, 'partial', False):
                return empty
        if html.is_html_input(dictionary):
            return dictionary.getlist(self.field_name)
        return dictionary.get(self.field_name, empty)

    def to_internal_value(self, data):
        if isinstance(data, str) or not hasattr(data, '__iter__'):
            self.fail('not_a_list', input_type=type(data).__name__)
        if not self.allow_empty and len(data) == 0:
            self.fail('empty')

        return {
            super(MultipleChoiceField, self).to_internal_value(item)
            for item in data
        }

    def to_representation(self, value):
        return {
            self.choice_strings_to_values.get(str(item), item) for item in value
        }


~~class FilePathField(ChoiceField):
    default_error_messages = {
        'invalid_choice': _('"{input}" is not a valid path choice.')
    }

    def __init__(self, path, match=None, recursive=False, allow_files=True,
                 allow_folders=False, required=None, **kwargs):
        field = DjangoFilePathField(
            path, match=match, recursive=recursive, allow_files=allow_files,
            allow_folders=allow_folders, required=required
        )
        kwargs['choices'] = field.choices
        super().__init__(**kwargs)



class FileField(Field):
    default_error_messages = {
        'required': _('No file was submitted.'),
        'invalid': _('The submitted data was not a file. Check the encoding type on the form.'),
        'no_name': _('No filename could be determined.'),
        'empty': _('The submitted file is empty.'),
        'max_length': _('Ensure this filename has at most {max_length} characters (it has {length}).'),
    }



## ... source file continues with no further FilePathField examples...

```

