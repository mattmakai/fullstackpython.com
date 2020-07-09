title: django.utils.safestring SafeData Example Code
category: page
slug: django-utils-safestring-safedata-examples
sortorder: 500011484
toc: False
sidebartitle: django.utils.safestring SafeData
meta: Python example code for the SafeData class from the django.utils.safestring module of the Django project.


SafeData is a class within the django.utils.safestring module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / angular_base.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/angular_base.py)

```python
# angular_base.py
from base64 import b64encode
from collections import UserList
import json
import warnings

from django.forms import forms
from django.http import QueryDict
from django.utils.html import format_html, format_html_join, escape, conditional_escape
from django.utils.encoding import force_text
from django.utils.module_loading import import_string
~~from django.utils.safestring import mark_safe, SafeText, SafeData
from django.core.exceptions import ValidationError, ImproperlyConfigured

from .fields import DefaultFieldMixin


~~class SafeTuple(SafeData, tuple):


class TupleErrorList(UserList, list):
    def __init__(self, initlist=None, error_class=None):
        super(TupleErrorList, self).__init__(initlist)

        if error_class is None:
            self.error_class = 'errorlist'
        else:
            self.error_class = 'errorlist {}'.format(error_class)

    def as_data(self):
        return ValidationError(self.data).error_list

    def get_json_data(self, escape_html=False):
        errors = []
        for error in self.as_data():
            message = list(error)[0]
            errors.append({
                'message': escape(message) if escape_html else message,
                'code': error.code or '',
            })
        return errors



## ... source file continues with no further SafeData examples...

```


## Example 2 from django-rest-framework
[Django REST Framework](https://github.com/encode/django-rest-framework)
([project homepage and documentation](https://www.django-rest-framework.org/),
[PyPI package information](https://pypi.org/project/djangorestframework/)
and [more resources on Full Stack Python](/django-rest-framework-drf.html)),
often abbreviated as "DRF", is a popular [Django](/django.html) extension
for building [web APIs](/application-programming-interfaces.html).
The project has fantastic documentation and a wonderful
[quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
that serve as examples of how to make it easier for newcomers
to get started.

The project is open sourced under the
[Encode OSS Ltd. license](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md).

[**django-rest-framework / rest_framework / templatetags / rest_framework.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/templatetags/rest_framework.py)

```python
# rest_framework.py
import re
from collections import OrderedDict

from django import template
from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.encoding import force_str, iri_to_uri
from django.utils.html import escape, format_html, smart_urlquote
~~from django.utils.safestring import SafeData, mark_safe

from rest_framework.compat import apply_markdown, pygments_highlight
from rest_framework.renderers import HTMLFormRenderer
from rest_framework.utils.urls import replace_query_param

register = template.Library()

class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')


@register.tag(name='code')
def highlight_code(parser, token):
    code = token.split_contents()[-1]
    nodelist = parser.parse(('endcode',))
    parser.delete_first_token()
    return CodeNode(code, nodelist)


class CodeNode(template.Node):
    style = 'emacs'

    def __init__(self, lang, code):
        self.lang = lang
        self.nodelist = code


## ... source file continues with no further SafeData examples...

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

[**django-tables2 / django_tables2 / columns / base.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/base.py)

```python
# base.py
from collections import OrderedDict
from itertools import islice

from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.utils.html import format_html
~~from django.utils.safestring import SafeData
from django.utils.text import capfirst

from ..utils import (
    Accessor,
    AttributeDict,
    OrderBy,
    OrderByTuple,
    call_with_appropriate,
    computed_values,
)


class Library:

    def __init__(self):
        self.columns = []

    def register(self, column):
        if not hasattr(column, "from_field"):
            raise ImproperlyConfigured(
                "{} is not a subclass of Column".format(column.__class__.__name__)
            )
        self.columns.append(column)
        return column


## ... source file abbreviated to get to SafeData examples ...


    def is_ordered(self):
        return self.name in (self._table.order_by or ())

    @property
    def orderable(self):
        if self.column.orderable is not None:
            return self.column.orderable
        return self._table.orderable

    @property
    def verbose_name(self):
        if self.column.verbose_name is not None:
            return self.column.verbose_name

        name = self.name.replace("_", " ")

        model = self._table.data.model
        if model:
            field = Accessor(self.accessor).get_field(model)
            if field:
                if hasattr(field, "field"):
                    name = field.field.verbose_name
                else:
                    name = getattr(field, "verbose_name", field.name)

~~            if isinstance(name, SafeData):
                return name

        return capfirst(name)

    @property
    def visible(self):
        return self.column.visible

    @property
    def localize(self):
        return self.column.localize


class BoundColumns:

    def __init__(self, table, base_columns):
        self._table = table
        self.columns = OrderedDict()
        for name, column in base_columns.items():
            self.columns[name] = bound_column = BoundColumn(table, column, name)
            bound_column.render = getattr(table, "render_" + name, column.render)
            bound_column.value = getattr(
                table, "value_" + name, getattr(table, "render_" + name, column.value)
            )


## ... source file continues with no further SafeData examples...

```

