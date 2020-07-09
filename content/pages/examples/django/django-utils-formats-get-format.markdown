title: django.utils.formats get_format Example Code
category: page
slug: django-utils-formats-get-format-examples
sortorder: 500011451
toc: False
sidebartitle: django.utils.formats get_format
meta: Python example code for the get_format callable from the django.utils.formats module of the Django project.


get_format is a callable within the django.utils.formats module of the Django project.


## Example 1 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / templatetags / jet_tags.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/templatetags/jet_tags.py)

```python
# jet_tags.py
from __future__ import unicode_literals
import json
import os
from django import template
try:
    from django.core.urlresolvers import reverse
except ImportError: # Django 1.11
    from django.urls import reverse

from django.forms import CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
~~from django.utils.formats import get_format
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_text
from jet import settings, VERSION
from jet.models import Bookmark
from jet.utils import get_model_instance_label, get_model_queryset, get_possible_language_codes, \
    get_admin_site, get_menu_items

try:
    from urllib.parse import parse_qsl
except ImportError:
    from urlparse import parse_qsl


register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag


@assignment_tag
def jet_get_date_format():
~~    return get_format('DATE_INPUT_FORMATS')[0]


@assignment_tag
def jet_get_time_format():
~~    return get_format('TIME_INPUT_FORMATS')[0]


@assignment_tag
def jet_get_datetime_format():
~~    return get_format('DATETIME_INPUT_FORMATS')[0]


@assignment_tag(takes_context=True)
def jet_get_menu(context):
    return get_menu_items(context)


@assignment_tag
def jet_get_bookmarks(user):
    if user is None:
        return None
    return Bookmark.objects.filter(user=user.pk)


@register.filter
def jet_is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter
def jet_select2_lookups(field):
    if hasattr(field, 'field') and \
            (isinstance(field.field, ModelChoiceField) or isinstance(field.field, ModelMultipleChoiceField)):
        qs = field.field.queryset


## ... source file continues with no further get_format examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / widgets.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/widgets.py)

```python
# widgets.py
import itertools
import json
from functools import total_ordering

from django import forms
from django.conf import settings
from django.forms import widgets
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.urls import reverse
~~from django.utils.formats import get_format
from django.utils.functional import cached_property
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from taggit.forms import TagWidget
from taggit.models import Tag

from wagtail.admin.datetimepicker import to_datetimepicker_format
from wagtail.admin.staticfiles import versioned_static
from wagtail.core import hooks
from wagtail.core.models import Page
from wagtail.utils.widgets import WidgetWithScript

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_TIME_FORMAT = '%H:%M'


class AdminAutoHeightTextInput(widgets.Textarea):
    template_name = 'wagtailadmin/widgets/auto_height_text_input.html'

    def __init__(self, attrs=None):
        default_attrs = {'rows': '1'}
        if attrs:
            default_attrs.update(attrs)

        super().__init__(default_attrs)


class AdminDateInput(widgets.DateInput):
    template_name = 'wagtailadmin/widgets/date_input.html'

    def __init__(self, attrs=None, format=None):
        default_attrs = {'autocomplete': 'off'}
        fmt = format
        if attrs:
            default_attrs.update(attrs)
        if fmt is None:
            fmt = getattr(settings, 'WAGTAIL_DATE_FORMAT', DEFAULT_DATE_FORMAT)
        self.js_format = to_datetimepicker_format(fmt)
        super().__init__(attrs=default_attrs, format=fmt)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        config = {
~~            'dayOfWeekStart': get_format('FIRST_DAY_OF_WEEK'),
            'format': self.js_format,
        }
        context['widget']['config_json'] = json.dumps(config)

        return context

    @property
    def media(self):
        return forms.Media(js=[
            versioned_static('wagtailadmin/js/date-time-chooser.js'),
        ])


class AdminTimeInput(widgets.TimeInput):
    template_name = 'wagtailadmin/widgets/time_input.html'

    def __init__(self, attrs=None, format=None):
        default_attrs = {'autocomplete': 'off'}
        if attrs:
            default_attrs.update(attrs)
        fmt = format
        if fmt is None:
            fmt = getattr(settings, 'WAGTAIL_TIME_FORMAT', DEFAULT_TIME_FORMAT)
        self.js_format = to_datetimepicker_format(fmt)


## ... source file abbreviated to get to get_format examples ...


            versioned_static('wagtailadmin/js/date-time-chooser.js'),
        ])


class AdminDateTimeInput(widgets.DateTimeInput):
    template_name = 'wagtailadmin/widgets/datetime_input.html'

    def __init__(self, attrs=None, format=None, time_format=None):
        default_attrs = {'autocomplete': 'off'}
        fmt = format
        if attrs:
            default_attrs.update(attrs)
        if fmt is None:
            fmt = getattr(settings, 'WAGTAIL_DATETIME_FORMAT', DEFAULT_DATETIME_FORMAT)
        time_fmt = time_format
        if time_fmt is None:
            time_fmt = getattr(settings, 'WAGTAIL_TIME_FORMAT', DEFAULT_TIME_FORMAT)
        self.js_format = to_datetimepicker_format(fmt)
        self.js_time_format = to_datetimepicker_format(time_fmt)
        super().__init__(attrs=default_attrs, format=fmt)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        config = {
~~            'dayOfWeekStart': get_format('FIRST_DAY_OF_WEEK'),
            'format': self.js_format,
            'formatTime': self.js_time_format
        }
        context['widget']['config_json'] = json.dumps(config)

        return context

    @property
    def media(self):
        return forms.Media(js=[
            versioned_static('wagtailadmin/js/date-time-chooser.js'),
        ])


class AdminTagWidget(TagWidget):
    template_name = 'wagtailadmin/widgets/tag_widget.html'

    def __init__(self, *args, **kwargs):
        self.tag_model = kwargs.pop('tag_model', Tag)
        self.free_tagging = kwargs.pop('free_tagging', None)
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)


## ... source file continues with no further get_format examples...

```

