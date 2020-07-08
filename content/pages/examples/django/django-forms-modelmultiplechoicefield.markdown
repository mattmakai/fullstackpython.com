title: django.forms ModelMultipleChoiceField Example Code
category: page
slug: django-forms-modelmultiplechoicefield-examples
sortorder: 500011274
toc: False
sidebartitle: django.forms ModelMultipleChoiceField
meta: Python example code for the ModelMultipleChoiceField class from the django.forms module of the Django project.


ModelMultipleChoiceField is a class within the django.forms module of the Django project.


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




## ... source file abbreviated to get to ModelMultipleChoiceField examples ...


def jet_is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter
def jet_select2_lookups(field):
    if hasattr(field, 'field') and \
            (isinstance(field.field, ModelChoiceField) or isinstance(field.field, ModelMultipleChoiceField)):
        qs = field.field.queryset
        model = qs.model

        if getattr(model, 'autocomplete_search_fields', None) and getattr(field.field, 'autocomplete', True):
            choices = []
            app_label = model._meta.app_label
            model_name = model._meta.object_name

            attrs = {
                'class': 'ajax',
                'data-app-label': app_label,
                'data-model': model_name,
                'data-ajax--url': reverse('jet:model_lookup')
            }

            initial_value = field.value()

~~            if hasattr(field, 'field') and isinstance(field.field, ModelMultipleChoiceField):
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
                    field.field.widget.widget = Select(attrs)
                else:


## ... source file continues with no further ModelMultipleChoiceField examples...

```

