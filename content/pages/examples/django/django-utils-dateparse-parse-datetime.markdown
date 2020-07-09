title: django.utils.dateparse parse_datetime Example Code
category: page
slug: django-utils-dateparse-parse-datetime-examples
sortorder: 500011432
toc: False
sidebartitle: django.utils.dateparse parse_datetime
meta: Python example code for the parse_datetime callable from the django.utils.dateparse module of the Django project.


parse_datetime is a callable within the django.utils.dateparse module of the Django project.


## Example 1 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / fields.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./fields.py)

```python
# fields.py
from collections import namedtuple
from datetime import datetime, time

from django import forms
~~from django.utils.dateparse import parse_datetime
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from .conf import settings
from .constants import EMPTY_VALUES
from .utils import handle_timezone
from .widgets import (
    BaseCSVWidget,
    CSVWidget,
    DateRangeWidget,
    LookupChoiceWidget,
    RangeWidget
)


class RangeField(forms.MultiValueField):
    widget = RangeWidget

    def __init__(self, fields=None, *args, **kwargs):
        if fields is None:
            fields = (
                forms.DecimalField(),
                forms.DecimalField())
        super().__init__(fields, *args, **kwargs)


## ... source file abbreviated to get to parse_datetime examples ...


        kwargs['widget'] = widget
        kwargs['help_text'] = field.help_text
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if len(data_list) == 2:
            value, lookup_expr = data_list
            if value not in EMPTY_VALUES:
                if lookup_expr not in EMPTY_VALUES:
                    return Lookup(value=value, lookup_expr=lookup_expr)
                else:
                    raise forms.ValidationError(
                        self.error_messages['lookup_required'],
                        code='lookup_required')
        return None


class IsoDateTimeField(forms.DateTimeField):
    ISO_8601 = 'iso-8601'
    input_formats = [ISO_8601]

    def strptime(self, value, format):
        value = force_str(value)

        if format == self.ISO_8601:
~~            parsed = parse_datetime(value)
            if parsed is None:  # Continue with other formats if doesn't match
                raise ValueError
            return handle_timezone(parsed)
        return super().strptime(value, format)


class BaseCSVField(forms.Field):
    base_widget_class = BaseCSVWidget

    def __init__(self, *args, **kwargs):
        widget = kwargs.get('widget') or self.widget
        kwargs['widget'] = self._get_widget_class(widget)

        super().__init__(*args, **kwargs)

    def _get_widget_class(self, widget):
        if isinstance(widget, BaseCSVWidget) or (
                isinstance(widget, type) and
                issubclass(widget, BaseCSVWidget)):
            return widget

        assert isinstance(widget, type), \
            "'%s.widget' must be a widget class, not %s." \
            % (self.__class__.__name__, repr(widget))


## ... source file continues with no further parse_datetime examples...

```

