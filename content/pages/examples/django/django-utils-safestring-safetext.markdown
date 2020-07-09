title: django.utils.safestring SafeText Example Code
category: page
slug: django-utils-safestring-safetext-examples
sortorder: 500011485
toc: False
sidebartitle: django.utils.safestring SafeText
meta: Python example code for the SafeText class from the django.utils.safestring module of the Django project.


SafeText is a class within the django.utils.safestring module of the Django project.


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


class SafeTuple(SafeData, tuple):


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

    def as_json(self, escape_html=False):
        return json.dumps(self.get_json_data(escape_html))

    def extend(self, iterable):
        for item in iterable:
            if not isinstance(item, str):
                self.append(item)
        return None

    def as_ul(self):
        if not self:
~~            return SafeText()
        first = self[0]
        if isinstance(first, tuple):
            error_lists = {'$pristine': [], '$dirty': []}
            for e in self:
                if e[5] == '$message':
                    li_format = '<li ng-show="{0}.{1} && {0}.{3}" class="{2}" ng-bind="{0}.{3}"></li>'
                else:
                    li_format = '<li ng-show="{0}.{1}" class="{2}">{3}</li>'
                err_tuple = (e[0], e[3], e[4], force_text(e[5]))
                error_lists[e[2]].append(format_html(li_format, *err_tuple))
            dirty_errors, pristine_errors = '', ''
            if len(error_lists['$dirty']) > 0:
                dirty_errors = format_html(
                    '<ul ng-show="{0}.$dirty && !{0}.$untouched" class="{1}" ng-cloak>{2}</ul>',  # duck typing: !...$untouched
                    first[0], first[1], mark_safe(''.join(error_lists['$dirty']))
                )
            if len(error_lists['$pristine']) > 0:
                pristine_errors = format_html(
                    '<ul ng-show="{0}.$pristine" class="{1}" ng-cloak>{2}</ul>',
                    first[0], first[1], mark_safe(''.join(error_lists['$pristine']))
                )
            return format_html('{}{}', dirty_errors, pristine_errors)
        return format_html('<ul class="errorlist">{0}</ul>',
            format_html_join('', '<li>{0}</li>', ((force_text(e),) for e in self)))


## ... source file continues with no further SafeText examples...

```

