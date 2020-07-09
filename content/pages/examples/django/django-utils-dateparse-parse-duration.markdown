title: django.utils.dateparse parse_duration Example Code
category: page
slug: django-utils-dateparse-parse-duration-examples
sortorder: 500011433
toc: False
sidebartitle: django.utils.dateparse parse_duration
meta: Python example code for the parse_duration callable from the django.utils.dateparse module of the Django project.


parse_duration is a callable within the django.utils.dateparse module of the Django project.


## Example 1 from django-import-export
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
from django.utils import datetime_safe, timezone
~~from django.utils.dateparse import parse_duration
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



## ... source file abbreviated to get to parse_duration examples ...


        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        for format in self.formats:
            try:
                return datetime.strptime(value, format).time()
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid time.")

    def render(self, value, obj=None):
        if not value:
            return ""
        return value.strftime(self.formats[0])


class DurationWidget(Widget):

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None

        try:
~~            return parse_duration(value)
        except (ValueError, TypeError):
            raise ValueError("Enter a valid duration.")

    def render(self, value, obj=None):
        if value is None:
            return ""
        return str(value)


class SimpleArrayWidget(Widget):

    def __init__(self, separator=None):
        if separator is None:
            separator = ','
        self.separator = separator
        super().__init__()

    def clean(self, value, row=None, *args, **kwargs):
        return value.split(self.separator) if value else []

    def render(self, value, obj=None):
        return self.separator.join(str(v) for v in value)




## ... source file continues with no further parse_duration examples...

```

