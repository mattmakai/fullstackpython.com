title: django.utils.html conditional_escape Example Code
category: page
slug: django-utils-html-conditional-escape-examples
sortorder: 500011461
toc: False
sidebartitle: django.utils.html conditional_escape
meta: Python example code for the conditional_escape callable from the django.utils.html module of the Django project.


conditional_escape is a callable within the django.utils.html module of the Django project.


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
from django.utils import datetime_safe, formats
from django.utils.dates import MONTHS
from django.utils.encoding import force_str
~~from django.utils.html import conditional_escape
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
)




## ... source file abbreviated to get to conditional_escape examples ...


            data, files, self.clear_checkbox_name(name)
        ):
            if upload:
                return FILE_INPUT_CONTRADICTION
            return False
        return upload

    def format_value(self, value):
        if not value:
            return None
        return value


class Textarea(Input):
    template_name = 'floppyforms/textarea.html'
    rows = 10
    cols = 40

    def __init__(self, attrs=None):
        default_attrs = {'cols': self.cols, 'rows': self.rows}
        if attrs:
            default_attrs.update(attrs)
        super(Textarea, self).__init__(default_attrs)

    def format_value(self, value):
~~        return conditional_escape(force_str(value))


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
                input_format = formats.get_format('DATE_INPUT_FORMATS')[0]
                initial = datetime.datetime.strptime(initial, input_format).date()
            except (TypeError, ValueError):
                pass


## ... source file continues with no further conditional_escape examples...

```


## Example 2 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / columns / manytomanycolumn.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/manytomanycolumn.py)

```python
# manytomanycolumn.py
from django.db import models
from django.utils.encoding import force_str
~~from django.utils.html import conditional_escape, mark_safe

from .base import Column, LinkTransform, library


@library.register
class ManyToManyColumn(Column):

    def __init__(
        self, transform=None, filter=None, separator=", ", linkify_item=None, *args, **kwargs
    ):
        kwargs.setdefault("orderable", False)
        super().__init__(*args, **kwargs)

        if transform is not None:
            self.transform = transform
        if filter is not None:
            self.filter = filter
        self.separator = separator

        link_kwargs = None
        if callable(linkify_item):
            link_kwargs = dict(url=linkify_item)
        elif isinstance(linkify_item, (dict, tuple)):
            link_kwargs = dict(reverse_args=linkify_item)
        elif linkify_item is True:
            link_kwargs = dict()

        if link_kwargs is not None:
            self.linkify_item = LinkTransform(attrs=self.attrs.get("a", {}), **link_kwargs)

    def transform(self, obj):
        return force_str(obj)

    def filter(self, qs):
        return qs.all()

    def render(self, value):
        if not value.exists():
            return self.default

        items = []
        for item in self.filter(value):
~~            content = conditional_escape(self.transform(item))
            if hasattr(self, "linkify_item"):
                content = self.linkify_item(content=content, record=item)

            items.append(content)

        return mark_safe(conditional_escape(self.separator).join(items))

    @classmethod
    def from_field(cls, field, **kwargs):
        if isinstance(field, models.ManyToManyField):
            return cls(**kwargs)



## ... source file continues with no further conditional_escape examples...

```

