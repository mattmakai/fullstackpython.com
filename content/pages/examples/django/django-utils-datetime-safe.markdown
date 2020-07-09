title: django.utils datetime_safe Example Code
category: page
slug: django-utils-datetime-safe-examples
sortorder: 500011417
toc: False
sidebartitle: django.utils datetime_safe
meta: Python example code for the datetime_safe callable from the django.utils module of the Django project.


datetime_safe is a callable within the django.utils module of the Django project.


## Example 1 from django-floppyforms
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

[**django-floppyforms / floppyforms / widgets.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/./widgets.py)

```python
# widgets.py
import datetime
import re
from itertools import chain

import django
from django import forms
from django.conf import settings
from django.forms.widgets import FILE_INPUT_CONTRADICTION
from django.template import loader
~~from django.utils import datetime_safe, formats
from django.utils.dates import MONTHS
from django.utils.encoding import force_str
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .compat import MULTIVALUE_DICT_TYPES, flatten_contexts


from django.forms.utils import to_current_timezone


RE_DATE = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')


__all__ = (
    'TextInput', 'PasswordInput', 'HiddenInput', 'ClearableFileInput',
    'FileInput', 'DateInput', 'DateTimeInput', 'TimeInput', 'Textarea',
    'CheckboxInput', 'Select', 'NullBooleanSelect', 'SelectMultiple',
    'RadioSelect', 'CheckboxSelectMultiple', 'SearchInput', 'RangeInput',
    'ColorInput', 'EmailInput', 'URLInput', 'PhoneNumberInput', 'NumberInput',
    'IPAddressInput', 'MultiWidget', 'Widget', 'SplitDateTimeWidget',
    'SplitHiddenDateTimeWidget', 'MultipleHiddenInput', 'SelectDateWidget',
    'SlugInput',


## ... source file abbreviated to get to datetime_safe examples ...


    template_name = 'floppyforms/textarea.html'
    rows = 10
    cols = 40

    def __init__(self, attrs=None):
        default_attrs = {'cols': self.cols, 'rows': self.rows}
        if attrs:
            default_attrs.update(attrs)
        super(Textarea, self).__init__(default_attrs)

    def format_value(self, value):
        return conditional_escape(force_str(value))


class DateInput(Input):
    template_name = 'floppyforms/date.html'
    input_type = 'date'
    supports_microseconds = False

    def __init__(self, attrs=None, format=None):
        super(DateInput, self).__init__(attrs)
        self.format = '%Y-%m-%d'

    def format_value(self, value):
        if hasattr(value, 'strftime'):
~~            value = datetime_safe.new_date(value)
            return value.strftime(self.format)
        return value

    if django.VERSION < (1, 6):
        def _has_changed(self, initial, data):
            try:
                input_format = formats.get_format('DATE_INPUT_FORMATS')[0]
                initial = datetime.datetime.strptime(initial, input_format).date()
            except (TypeError, ValueError):
                pass
            return super(DateInput, self)._has_changed(
                self._format_value(initial), data
            )


class DateTimeInput(Input):
    template_name = 'floppyforms/datetime.html'
    input_type = 'datetime'
    supports_microseconds = False

    def __init__(self, attrs=None, format=None):
        super(DateTimeInput, self).__init__(attrs)
        if format:
            self.format = format
            self.manual_format = True
        else:
            self.format = formats.get_format('DATETIME_INPUT_FORMATS')[0]
            self.manual_format = False

    def format_value(self, value):
        if hasattr(value, 'strftime'):
~~            value = datetime_safe.new_datetime(value)
            return value.strftime(self.format)
        return value

    if django.VERSION < (1, 6):
        def _has_changed(self, initial, data):
            try:
                input_format = formats.get_format('DATETIME_INPUT_FORMATS')[0]
                initial = datetime.datetime.strptime(initial, input_format)
            except (TypeError, ValueError):
                pass
            return super(DateTimeInput, self)._has_changed(
                self._format_value(initial), data
            )


class TimeInput(Input):
    template_name = 'floppyforms/time.html'
    input_type = 'time'
    supports_microseconds = False

    def __init__(self, attrs=None, format=None):
        super(TimeInput, self).__init__(attrs)
        if format:
            self.format = format


## ... source file abbreviated to get to datetime_safe examples ...


        context['day_choices'] = [(i, i) for i in range(1, 32)]
        context['day_val'] = day_val


        if self.required is False:
            context['year_choices'].insert(0, self.none_value)
            context['month_choices'].insert(0, self.none_value)
            context['day_choices'].insert(0, self.none_value)

        return loader.render_to_string(self.template_name, context)

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        d = data.get(self.day_field % name)
        if y == m == d == "0":
            return None
        if y and m and d:
            if settings.USE_L10N:
                input_format = formats.get_format('DATE_INPUT_FORMATS')[0]
                try:
                    date_value = datetime.date(int(y), int(m), int(d))
                except ValueError:
                    return '%s-%s-%s' % (y, m, d)
                else:
~~                    date_value = datetime_safe.new_date(date_value)
                    return date_value.strftime(input_format)
            else:
                return '%s-%s-%s' % (y, m, d)
        return data.get(name, None)



## ... source file continues with no further datetime_safe examples...

```


## Example 2 from django-haystack
[django-haystack](https://github.com/django-haystack/django-haystack)
([project website](http://haystacksearch.org/) and
[PyPI page](https://pypi.org/project/django-haystack/))
is a search abstraction layer that separates the Python search code
in a [Django](/django.html) web application from the search engine
implementation that it runs on, such as
[Apache Solr](http://lucene.apache.org/solr/),
[Elasticsearch](https://www.elastic.co/)
or [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html).

The django-haystack project is open source under the
[BSD license](https://github.com/django-haystack/django-haystack/blob/master/LICENSE).

[**django-haystack / haystack / fields.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./fields.py)

```python
# fields.py
import re
from inspect import ismethod

from django.template import loader
~~from django.utils import datetime_safe

from haystack.exceptions import SearchFieldError
from haystack.utils import get_model_ct_tuple


class NOT_PROVIDED:
    pass


DATE_REGEX = re.compile(
    r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(?:|T00:00:00Z?)$"
)
DATETIME_REGEX = re.compile(
    r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(T|\s+)(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}).*?$"
)




class SearchField(object):

    field_type = None

    def __init__(


## ... source file abbreviated to get to datetime_safe examples ...



        return bool(value)


class DateField(SearchField):
    field_type = "date"

    def __init__(self, **kwargs):
        if kwargs.get("facet_class") is None:
            kwargs["facet_class"] = FacetDateField

        super(DateField, self).__init__(**kwargs)

    def prepare(self, obj):
        return self.convert(super(DateField, self).prepare(obj))

    def convert(self, value):
        if value is None:
            return None

        if isinstance(value, str):
            match = DATE_REGEX.search(value)

            if match:
                data = match.groupdict()
~~                return datetime_safe.date(
                    int(data["year"]), int(data["month"]), int(data["day"])
                )
            else:
                raise SearchFieldError(
                    "Date provided to '%s' field doesn't appear to be a valid date string: '%s'"
                    % (self.instance_name, value)
                )

        return value


class DateTimeField(SearchField):
    field_type = "datetime"

    def __init__(self, **kwargs):
        if kwargs.get("facet_class") is None:
            kwargs["facet_class"] = FacetDateTimeField

        super(DateTimeField, self).__init__(**kwargs)

    def prepare(self, obj):
        return self.convert(super(DateTimeField, self).prepare(obj))

    def convert(self, value):
        if value is None:
            return None

        if isinstance(value, str):
            match = DATETIME_REGEX.search(value)

            if match:
                data = match.groupdict()
~~                return datetime_safe.datetime(
                    int(data["year"]),
                    int(data["month"]),
                    int(data["day"]),
                    int(data["hour"]),
                    int(data["minute"]),
                    int(data["second"]),
                )
            else:
                raise SearchFieldError(
                    "Datetime provided to '%s' field doesn't appear to be a valid datetime string: '%s'"
                    % (self.instance_name, value)
                )

        return value


class MultiValueField(SearchField):
    field_type = "string"

    def __init__(self, **kwargs):
        if kwargs.get("facet_class") is None:
            kwargs["facet_class"] = FacetMultiValueField

        if kwargs.get("use_template") is True:


## ... source file continues with no further datetime_safe examples...

```


## Example 3 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / widgets.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./widgets.py)

```python
# widgets.py
import json
from datetime import date, datetime
from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
~~from django.utils import datetime_safe, timezone
from django.utils.dateparse import parse_duration
from django.utils.encoding import force_str, smart_str


class Widget:
    def clean(self, value, row=None, *args, **kwargs):
        return value

    def render(self, value, obj=None):
        return force_str(value)


class NumberWidget(Widget):

    def is_empty(self, value):
        if isinstance(value, str):
            value = value.strip()
        return value is None or value == ""

    def render(self, value, obj=None):
        return value


class FloatWidget(NumberWidget):


## ... source file abbreviated to get to datetime_safe examples ...


                formats = ("%Y-%m-%d",)
            else:
                formats = settings.DATE_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, date):
            return value
        for format in self.formats:
            try:
                return datetime.strptime(value, format).date()
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid date.")

    def render(self, value, obj=None):
        if not value:
            return ""
        try:
            return value.strftime(self.formats[0])
        except:
~~            return datetime_safe.new_date(value).strftime(self.formats[0])


class DateTimeWidget(Widget):

    def __init__(self, format=None):
        if format is None:
            if not settings.DATETIME_INPUT_FORMATS:
                formats = ("%Y-%m-%d %H:%M:%S",)
            else:
                formats = settings.DATETIME_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, datetime):
            return value
        for format in self.formats:
            try:
                dt = datetime.strptime(value, format)
                if settings.USE_TZ:
                    dt = timezone.make_aware(dt,


## ... source file continues with no further datetime_safe examples...

```

