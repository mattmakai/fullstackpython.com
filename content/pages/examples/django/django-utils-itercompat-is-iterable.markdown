title: django.utils.itercompat is_iterable Example Code
category: page
slug: django-utils-itercompat-is-iterable-examples
sortorder: 500011479
toc: False
sidebartitle: django.utils.itercompat is_iterable
meta: Python example code for the is_iterable callable from the django.utils.itercompat module of the Django project.


is_iterable is a callable within the django.utils.itercompat module of the Django project.


## Example 1 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / filters.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./filters.py)

```python
# filters.py
from collections import OrderedDict
from datetime import timedelta

from django import forms
from django.db.models import Q
from django.db.models.constants import LOOKUP_SEP
from django.forms.utils import pretty_name
~~from django.utils.itercompat import is_iterable
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .conf import settings
from .constants import EMPTY_VALUES
from .fields import (
    BaseCSVField,
    BaseRangeField,
    ChoiceField,
    DateRangeField,
    DateTimeRangeField,
    IsoDateTimeField,
    IsoDateTimeRangeField,
    LookupChoiceField,
    ModelChoiceField,
    ModelMultipleChoiceField,
    MultipleChoiceField,
    RangeField,
    TimeRangeField
)
from .utils import get_model_field, label_for_filter

__all__ = [
    'AllValuesFilter',


## ... source file abbreviated to get to is_iterable examples ...



        kwargs.setdefault('label', _('Ordering'))
        kwargs.setdefault('help_text', '')
        kwargs.setdefault('null_label', None)
        super().__init__(*args, **kwargs)

    def get_ordering_value(self, param):
        descending = param.startswith('-')
        param = param[1:] if descending else param
        field_name = self.param_map.get(param, param)

        return "-%s" % field_name if descending else field_name

    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        ordering = [self.get_ordering_value(param) for param in value]
        return qs.order_by(*ordering)

    @classmethod
    def normalize_fields(cls, fields):
        if isinstance(fields, dict):
            return OrderedDict(fields)

~~        assert is_iterable(fields), \
            "'fields' must be an iterable (e.g., a list, tuple, or mapping)."

        assert all(isinstance(field, str) or
~~                   is_iterable(field) and len(field) == 2  # may need to be wrapped in parens
                   for field in fields), \
            "'fields' must contain strings or (field name, param name) pairs."

        return OrderedDict([
            (f, f) if isinstance(f, str) else f for f in fields
        ])

    def build_choices(self, fields, labels):
        ascending = [
            (param, labels.get(field, _(pretty_name(param))))
            for field, param in fields.items()
        ]
        descending = [
            ('-%s' % param, labels.get('-%s' % param, self.descending_fmt % label))
            for param, label in ascending
        ]

        return [val for pair in zip(ascending, descending) for val in pair]


class FilterMethod:
    def __init__(self, filter_instance):
        self.f = filter_instance



## ... source file continues with no further is_iterable examples...

```

