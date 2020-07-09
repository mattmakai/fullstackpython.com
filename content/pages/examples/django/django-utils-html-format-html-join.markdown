title: django.utils.html format_html_join Example Code
category: page
slug: django-utils-html-format-html-join-examples
sortorder: 500011465
toc: False
sidebartitle: django.utils.html format_html_join
meta: Python example code for the format_html_join callable from the django.utils.html module of the Django project.


format_html_join is a callable within the django.utils.html module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / sekizai_processors.py**](https://github.com/jrief/django-angular/blob/master/djng/./sekizai_processors.py)

```python
# sekizai_processors.py

import warnings

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
~~from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

if 'sekizai' not in settings.INSTALLED_APPS:
    msg = "Install django-sekizai when using these postprocessors"
    raise ImproperlyConfigured(msg)


def module_list(context, data, namespace):
    warnings.warn("This postprocessor is deprecated. Read on how to resolve AngularJS dependencies using `{% with_data \"ng-requires\" ... %}`")
    modules = set(m.strip(' "\'') for m in data.split())
~~    text = format_html_join(', ', '"{0}"', ((m,) for m in modules))
    return text


def module_config(context, data, namespace):
    warnings.warn("This postprocessor is deprecated. Read on how to resolve AngularJS dependencies using `{% with_data \"ng-config\" ... %}`")
    configs = [(mark_safe(c),) for c in data.split('\n') if c]
~~    text = format_html_join('', '.config({0})', configs)
    return text



## ... source file continues with no further format_html_join examples...

```


## Example 2 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / templatetags / filer_admin_tags.py**](https://github.com/divio/django-filer/blob/develop/filer/templatetags/filer_admin_tags.py)

```python
# filer_admin_tags.py
from __future__ import absolute_import, unicode_literals

from django.template import Library
~~from django.utils.html import format_html_join

from ..admin.tools import admin_url_params, admin_url_params_encoded


register = Library()

assignment_tag = getattr(register, 'assignment_tag', register.simple_tag)


def filer_actions(context):
    context['action_index'] = context.get('action_index', -1) + 1
    return context


filer_actions = register.inclusion_tag(
    "admin/filer/actions.html", takes_context=True)(filer_actions)


@register.simple_tag(takes_context=True)
def filer_admin_context_url_params(context, first_separator='?'):
    return admin_url_params_encoded(
        context['request'], first_separator=first_separator)


@register.simple_tag(takes_context=True)
def filer_admin_context_hidden_formfields(context):
    request = context.get('request')
~~    return format_html_join(
        '\n',
        '<input type="hidden" name="{0}" value="{1}">',
        admin_url_params(request).items(),
    )


@assignment_tag(takes_context=True)
def filer_has_permission(context, item, action):
    permission_method_name = 'has_{action}_permission'.format(action=action)
    permission_method = getattr(item, permission_method_name, None)
    request = context.get('request')

    if not permission_method or not request:
        return False
    return permission_method(request)



## ... source file continues with no further format_html_join examples...

```


## Example 3 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / utils.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/./utils.py)

```python
# utils.py
import inspect
import warnings
from collections import OrderedDict
from functools import total_ordering
from itertools import chain

from django.core.exceptions import FieldDoesNotExist
from django.db import models
~~from django.utils.html import format_html_join


class Sequence(list):

    def expand(self, columns):
        ellipses = self.count("...")
        if ellipses > 1:
            raise ValueError("'...' must be used at most once in a sequence.")
        elif ellipses == 0:
            self.append("...")

        columns = list(columns)  # take a copy and exhaust the generator
        head = []
        tail = []
        target = head  # start by adding things to the head
        for name in self:
            if name == "...":
                target = tail
                continue
            target.append(name)
            if name in columns:
                columns.pop(columns.index(name))
        self[:] = chain(head, columns, tail)



## ... source file abbreviated to get to format_html_join examples ...


            if hasattr(field, "remote_field"):
                rel = getattr(field, "remote_field", None)
                model = getattr(rel, "model", model)

        return field

    def penultimate(self, context, quiet=True):
        path, _, remainder = self.rpartition(self.SEPARATOR)
        return A(path).resolve(context, quiet=quiet), remainder


A = Accessor  # alias


class AttributeDict(OrderedDict):

    blacklist = ("th", "td", "_ordering", "thead", "tbody", "tfoot")

    def _iteritems(self):
        for key, v in self.items():
            value = v() if callable(v) else v
            if key not in self.blacklist and value is not None:
                yield (key, value)

    def as_html(self):
~~        return format_html_join(" ", '{}="{}"', self._iteritems())


def segment(sequence, aliases):
    if not (sequence or aliases):
        return
    for alias, parts in aliases.items():
        variants = {
            alias: OrderByTuple(parts),
            OrderBy(alias).opposite: OrderByTuple(parts).opposite,
        }
        for valias, vparts in variants.items():
            if list(sequence[: len(vparts)]) == list(vparts):
                tail_aliases = dict(aliases)
                del tail_aliases[alias]
                tail_sequence = sequence[len(vparts) :]
                if tail_sequence:
                    for tail in segment(tail_sequence, tail_aliases):
                        yield tuple(chain([valias], tail))
                    else:
                        continue
                else:
                    yield tuple([valias])




## ... source file continues with no further format_html_join examples...

```


## Example 4 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / messages.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/messages.py)

```python
# messages.py
from django.contrib import messages
from django.core.exceptions import NON_FIELD_ERRORS
from django.template.loader import render_to_string
~~from django.utils.html import format_html, format_html_join


def render(message, buttons, detail=''):
    return render_to_string('wagtailadmin/shared/messages.html', {
        'message': message,
        'buttons': buttons,
        'detail': detail,
    })


def debug(request, message, buttons=None, extra_tags=''):
    return messages.debug(request, render(message, buttons), extra_tags=extra_tags)


def info(request, message, buttons=None, extra_tags=''):
    return messages.info(request, render(message, buttons), extra_tags=extra_tags)


def success(request, message, buttons=None, extra_tags=''):
    return messages.success(request, render(message, buttons), extra_tags=extra_tags)


def warning(request, message, buttons=None, extra_tags=''):
    return messages.warning(request, render(message, buttons), extra_tags=extra_tags)


def error(request, message, buttons=None, extra_tags=''):
    return messages.error(request, render(message, buttons), extra_tags=extra_tags)


def validation_error(request, message, form, buttons=None):
    if not form.non_field_errors():
        detail = ''
    else:
        all_errors = []
        for field_name, errors in form.errors.items():
            if field_name == NON_FIELD_ERRORS:
                prefix = ''
            else:
                try:
                    field_label = form[field_name].label
                except KeyError:
                    field_label = field_name
                prefix = "%s: " % field_label

            for error in errors:
                all_errors.append(prefix + error)

~~        errors_html = format_html_join('\n', '<li>{}</li>', ((e,) for e in all_errors))
        detail = format_html("""<ul class="errorlist">{}</ul>""", errors_html)

    return messages.error(request, render(message, buttons, detail=detail))


def button(url, text, new_window=False):
    if url is None:
        raise ValueError("Button URLs must not be None")
    return url, text, new_window



## ... source file continues with no further format_html_join examples...

```

