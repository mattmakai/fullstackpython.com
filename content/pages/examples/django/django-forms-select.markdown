title: django.forms Select Example Code
category: page
slug: django-forms-select-examples
sortorder: 500011276
toc: False
sidebartitle: django.forms Select
meta: Python example code for the Select class from the django.forms module of the Django project.


Select is a class within the django.forms module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / gears / widgets.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/gears/widgets.py)

```python
# widgets.py
~~from django.forms import FileInput, CheckboxSelectMultiple, Select


class CustomFileInput(FileInput):
    template_name = 'gears/widgets/file_input.html'
    accept = ''
    show_file_name = True


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name = 'gears/widgets/checkbox_multiple_select.html'
    hide_label = False
    hide_apply_btn = False

    class Media:
        js = ('gears/js/checkbox_multiple_select.js',)

    def __init__(self, *args, **kwargs):
        self.hide_label = kwargs.pop('hide_label', False)
        self.hide_apply_btn = kwargs.pop('hide_apply_btn', False)
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'hide_label': self.hide_label,
            'hide_apply_btn': self.hide_apply_btn,
        })
        return context


~~class DropdownSelectSubmit(Select):
    template_name = 'gears/widgets/dropdown_select_submit.html'
    empty_label = 'Not selected'
    label_class = ''
    empty_label_class = 'text-warning'
    nonempty_label_class = 'text-success'

    class Media:
        js = ('gears/js/dropdown_select_submit.js',)

    def __init__(self, *args, **kwargs):
        self.empty_label = kwargs.pop('empty_label', 'Not selected')
        self.label_class = kwargs.pop('label_class', '')
        self.empty_label_class = kwargs.pop('empty_label_class', 'text-warning')
        self.nonempty_label_class = kwargs.pop(
            'nonempty_label_class', 'text-success')
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        widget = context['widget']
        widget['label_class'] = self.label_class
        widget['empty_label_class'] = self.empty_label_class
        widget['nonempty_label_class'] = self.nonempty_label_class
        widget['label'] = self.empty_label


## ... source file continues with no further Select examples...

```


## Example 2 from django-jet
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

~~from django.forms import CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.utils.formats import get_format
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
    return get_format('DATE_INPUT_FORMATS')[0]




## ... source file abbreviated to get to Select examples ...


            initial_value = field.value()

            if hasattr(field, 'field') and isinstance(field.field, ModelMultipleChoiceField):
                if initial_value:
                    initial_objects = model.objects.filter(pk__in=initial_value)
                    choices.extend(
                        [(initial_object.pk, get_model_instance_label(initial_object))
                            for initial_object in initial_objects]
                    )

                if isinstance(field.field.widget, RelatedFieldWidgetWrapper):
                    field.field.widget.widget = SelectMultiple(attrs)
                else:
                    field.field.widget = SelectMultiple(attrs)
                field.field.choices = choices
            elif hasattr(field, 'field') and isinstance(field.field, ModelChoiceField):
                if initial_value:
                    try:
                        initial_object = model.objects.get(pk=initial_value)
                        attrs['data-object-id'] = initial_value
                        choices.append((initial_object.pk, get_model_instance_label(initial_object)))
                    except model.DoesNotExist:
                        pass

                if isinstance(field.field.widget, RelatedFieldWidgetWrapper):
~~                    field.field.widget.widget = Select(attrs)
                else:
~~                    field.field.widget = Select(attrs)
                field.field.choices = choices

    return field


@assignment_tag(takes_context=True)
def jet_get_current_theme(context):
    if 'request' in context and 'JET_THEME' in context['request'].COOKIES:
        theme = context['request'].COOKIES['JET_THEME']
        if isinstance(settings.JET_THEMES, list) and len(settings.JET_THEMES) > 0:
            for conf_theme in settings.JET_THEMES:
                if isinstance(conf_theme, dict) and conf_theme.get('theme') == theme:
                    return theme
    return settings.JET_DEFAULT_THEME


@assignment_tag
def jet_get_themes():
    return settings.JET_THEMES


@assignment_tag
def jet_get_current_version():
    return VERSION


## ... source file continues with no further Select examples...

```

