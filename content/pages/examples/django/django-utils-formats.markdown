title: django.utils formats Example Code
category: page
slug: django-utils-formats-examples
sortorder: 500011418
toc: False
sidebartitle: django.utils formats
meta: Python example code for the formats callable from the django.utils module of the Django project.


formats is a callable within the django.utils module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog_tests / tests.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/tests.py)

```python
# tests.py
import datetime
import django
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User, AnonymousUser
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.http import HttpResponse
from django.test import TestCase, RequestFactory
~~from django.utils import dateformat, formats, timezone
from dateutil.tz import gettz

from auditlog.middleware import AuditlogMiddleware
from auditlog.models import LogEntry
from auditlog.registry import auditlog
from auditlog_tests.models import SimpleModel, AltPrimaryKeyModel, UUIDPrimaryKeyModel, \
    ProxyModel, SimpleIncludeModel, SimpleExcludeModel, SimpleMappingModel, RelatedModel, \
    ManyRelatedModel, AdditionalDataIncludedModel, DateTimeFieldModel, ChoicesFieldModel, \
    CharfieldTextfieldModel, PostgresArrayFieldModel, NoDeleteHistoryModel
from auditlog import compat


class SimpleModelTest(TestCase):
    def setUp(self):
        self.obj = SimpleModel.objects.create(text='I am not difficult.')

    def test_create(self):
        obj = self.obj

        self.assertTrue(obj.history.count() == 1, msg="There is one log entry")

        try:
            history = obj.history.get()
        except obj.history.DoesNotExist:


## ... source file abbreviated to get to formats examples ...



        self.assertTrue(dtm.history.count() == 2, msg="There are two log entries")

    def test_changes_display_dict_datetime(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()
        localized_timestamp = timestamp.astimezone(gettz(settings.TIME_ZONE))
        self.assertTrue(dtm.history.latest().changes_display_dict["timestamp"][1] == \
                        dateformat.format(localized_timestamp, settings.DATETIME_FORMAT),
                        msg=("The datetime should be formatted according to Django's settings for"
                             " DATETIME_FORMAT"))
        timestamp = timezone.now()
        dtm.timestamp = timestamp
        dtm.save()
        localized_timestamp = timestamp.astimezone(gettz(settings.TIME_ZONE))
        self.assertTrue(dtm.history.latest().changes_display_dict["timestamp"][1] == \
                        dateformat.format(localized_timestamp, settings.DATETIME_FORMAT),
                        msg=("The datetime should be formatted according to Django's settings for"
                             " DATETIME_FORMAT"))

        with self.settings(USE_L10N=True, LANGUAGE_CODE='en-GB'):
            self.assertTrue(dtm.history.latest().changes_display_dict["timestamp"][1] == \
~~                        formats.localize(localized_timestamp),
                        msg=("The datetime should be formatted according to Django's settings for"
                             " USE_L10N is True with a different LANGUAGE_CODE."))


    def test_changes_display_dict_date(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["date"][1] == \
                        dateformat.format(date, settings.DATE_FORMAT),
                        msg=("The date should be formatted according to Django's settings for"
                             " DATE_FORMAT unless USE_L10N is True."))
        date = datetime.date(2017, 1, 11)
        dtm.date = date
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["date"][1] == \
                        dateformat.format(date, settings.DATE_FORMAT),
                        msg=("The date should be formatted according to Django's settings for"
                             " DATE_FORMAT unless USE_L10N is True."))

        with self.settings(USE_L10N=True, LANGUAGE_CODE='en-GB'):
            self.assertTrue(dtm.history.latest().changes_display_dict["date"][1] == \
~~                        formats.localize(date),
                        msg=("The date should be formatted according to Django's settings for"
                             " USE_L10N is True with a different LANGUAGE_CODE."))

    def test_changes_display_dict_time(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["time"][1] == \
                        dateformat.format(time, settings.TIME_FORMAT),
                        msg=("The time should be formatted according to Django's settings for"
                             " TIME_FORMAT unless USE_L10N is True."))
        time = datetime.time(6, 0)
        dtm.time = time
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["time"][1] == \
                        dateformat.format(time, settings.TIME_FORMAT),
                        msg=("The time should be formatted according to Django's settings for"
                             " TIME_FORMAT unless USE_L10N is True."))

        with self.settings(USE_L10N=True, LANGUAGE_CODE='en-GB'):
            self.assertTrue(dtm.history.latest().changes_display_dict["time"][1] == \
~~                        formats.localize(time),
                        msg=("The time should be formatted according to Django's settings for"
                             " USE_L10N is True with a different LANGUAGE_CODE."))

    def test_update_naive_dt(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()

        dtm.naive_dt = timezone.make_naive(timezone.now(), timezone=timezone.utc)
        dtm.save()


class UnregisterTest(TestCase):
    def setUp(self):
        auditlog.unregister(SimpleModel)
        self.obj = SimpleModel.objects.create(text='No history')

    def tearDown(self):
        auditlog.register(SimpleModel)

    def test_unregister_create(self):
        obj = self.obj


## ... source file continues with no further formats examples...

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


## ... source file abbreviated to get to formats examples ...


    if not hasattr(forms.Widget, 'format_value'):
        def format_value(self, value):
            return self._format_value(value)


class Input(Widget):
    template_name = 'floppyforms/input.html'
    input_type = None
    datalist = None

    def __init__(self, *args, **kwargs):
        datalist = kwargs.pop('datalist', None)
        if datalist is not None:
            self.datalist = datalist
        template_name = kwargs.pop('template_name', None)
        if template_name is not None:
            self.template_name = template_name
        super(Input, self).__init__(*args, **kwargs)
        self.context_instance = None

    def get_context_data(self):
        return {}

    def format_value(self, value):
        if self.is_localized:
~~            value = formats.localize_input(value)
        return force_str(value)

    def get_context(self, name, value, attrs=None):
        context = {
            'widget': self,
            'type': self.input_type,
            'name': name,
            'hidden': self.is_hidden,
            'required': self.is_required,
            'True': True,
        }

        if self.is_hidden:
            context['hidden'] = True

        if value is None:
            value = ''

        if value != '':
            context['value'] = self.format_value(value)

        context.update(self.get_context_data())
        context['attrs'] = self.build_attrs(attrs)



## ... source file abbreviated to get to formats examples ...


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
            value = datetime_safe.new_date(value)
            return value.strftime(self.format)
        return value

    if django.VERSION < (1, 6):
        def _has_changed(self, initial, data):
            try:
~~                input_format = formats.get_format('DATE_INPUT_FORMATS')[0]
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
~~            self.format = formats.get_format('DATETIME_INPUT_FORMATS')[0]
            self.manual_format = False

    def format_value(self, value):
        if hasattr(value, 'strftime'):
            value = datetime_safe.new_datetime(value)
            return value.strftime(self.format)
        return value

    if django.VERSION < (1, 6):
        def _has_changed(self, initial, data):
            try:
~~                input_format = formats.get_format('DATETIME_INPUT_FORMATS')[0]
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
            self.manual_format = True
        else:
~~            self.format = formats.get_format('TIME_INPUT_FORMATS')[0]
            self.manual_format = False

    def format_value(self, value):
        if hasattr(value, 'strftime'):
            return value.strftime(self.format)
        return value

    if django.VERSION < (1, 6):
        def _has_changed(self, initial, data):
            try:
~~                input_format = formats.get_format('TIME_INPUT_FORMATS')[0]
                initial = datetime.datetime.strptime(initial, input_format).time()
            except (TypeError, ValueError):
                pass
            return super(TimeInput, self)._has_changed(
                self._format_value(initial), data
            )


class SearchInput(Input):
    template_name = 'floppyforms/search.html'
    input_type = 'search'


class EmailInput(TextInput):
    template_name = 'floppyforms/email.html'
    input_type = 'email'


class URLInput(TextInput):
    template_name = 'floppyforms/url.html'
    input_type = 'url'


class ColorInput(Input):


## ... source file abbreviated to get to formats examples ...


class RadioSelect(Select):
    template_name = 'floppyforms/radio.html'


class CheckboxSelectMultiple(SelectMultiple):
    template_name = 'floppyforms/checkbox_select.html'


class MultiWidget(forms.MultiWidget):
    @property
    def is_hidden(self):
        return all(w.is_hidden for w in self.widgets)

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = dict(self.attrs, **kwargs)
        attrs.update(base_attrs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    if django.VERSION < (1, 11):
        def format_value(self, value):
            if value == '' or value is None:
                return None
            if self.is_localized:
~~                return formats.localize_input(value)
            return force_str(value)

        def get_context(self, name, value, attrs):
            context = {}
            context['widget'] = {
                'name': name,
                'is_hidden': self.is_hidden,
                'required': self.is_required,
                'value': self.format_value(value),
                'attrs': self.build_attrs(self.attrs, attrs),
                'template_name': self.template_name,
            }
            if self.is_localized:
                for widget in self.widgets:
                    widget.is_localized = self.is_localized
            if not isinstance(value, list):
                value = self.decompress(value)

            final_attrs = context['widget']['attrs']
            input_type = final_attrs.pop('type', None)
            id_ = final_attrs.get('id')
            subwidgets = []
            for i, widget in enumerate(self.widgets):
                if input_type is not None:


## ... source file abbreviated to get to formats examples ...


        if value is None:
            value = ''

        context.update(self.get_context_data())
        attrs.update(self.attrs)

        for key, value in attrs.items():
            if value is True:
                attrs[key] = False
        context['year_id'] = self.year_field % attrs['id']
        context['month_id'] = self.month_field % attrs['id']
        context['day_id'] = self.day_field % attrs['id']
        del attrs['id']

        context['attrs'] = attrs
        return context

    def render(self, name, value, attrs=None, extra_context={}, renderer=None):
        try:
            year_val, month_val, day_val = value.year, value.month, value.day
        except AttributeError:
            year_val = month_val = day_val = None
            if isinstance(value, str):
                if settings.USE_L10N:
                    try:
~~                        input_format = formats.get_format(
                            'DATE_INPUT_FORMATS'
                        )[0]
                        v = datetime.datetime.strptime(value, input_format)
                        year_val, month_val, day_val = v.year, v.month, v.day
                    except ValueError:
                        pass
                else:
                    match = RE_DATE.match(value)
                    if match:
                        year_val, month_val, day_val = map(int, match.groups())

        context = self.get_context(name, value, attrs=attrs,
                                   extra_context=extra_context)

        context['year_choices'] = [(i, i) for i in self.years]
        context['year_val'] = year_val

        context['month_choices'] = list(MONTHS.items())
        context['month_val'] = month_val

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
~~                input_format = formats.get_format('DATE_INPUT_FORMATS')[0]
                try:
                    date_value = datetime.date(int(y), int(m), int(d))
                except ValueError:
                    return '%s-%s-%s' % (y, m, d)
                else:
                    date_value = datetime_safe.new_date(date_value)
                    return date_value.strftime(input_format)
            else:
                return '%s-%s-%s' % (y, m, d)
        return data.get(name, None)



## ... source file continues with no further formats examples...

```

