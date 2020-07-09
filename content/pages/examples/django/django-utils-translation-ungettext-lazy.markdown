title: django.utils.translation ungettext_lazy Example Code
category: page
slug: django-utils-translation-ungettext-lazy-examples
sortorder: 500011512
toc: False
sidebartitle: django.utils.translation ungettext_lazy
meta: Python example code for the ungettext_lazy callable from the django.utils.translation module of the Django project.


ungettext_lazy is a callable within the django.utils.translation module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / fields.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/fields.py)

```python
# fields.py
import re
import mimetypes

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core import signing
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.urls import reverse_lazy
from django.forms import fields, models as model_fields, widgets
from django.utils.html import format_html
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
~~from django.utils.translation import ugettext_lazy as _, ungettext_lazy

from djng import app_settings
from .widgets import DropFileWidget, DropImageWidget


class DefaultFieldMixin(object):
    render_label = True

    def has_subwidgets(self):
        return False

    def get_potential_errors(self):
        return self.get_input_required_errors()

    def get_input_required_errors(self):
        errors = []
        if self.required:
            self.widget.attrs['ng-required'] = 'true'
            for key, msg in self.error_messages.items():
                if key == 'required':
                    errors.append(('$error.required', msg))
        return errors

    def get_min_max_length_errors(self):
        errors = []
        if getattr(self, 'min_length', None):
            self.widget.attrs['ng-minlength'] = self.min_length
        if getattr(self, 'max_length', None):
            self.widget.attrs['ng-maxlength'] = self.max_length
        for item in self.validators:
            if getattr(item, 'code', None) == 'min_length':
~~                message = ungettext_lazy(
                    'Ensure this value has at least %(limit_value)d character',
                    'Ensure this value has at least %(limit_value)d characters',
                    'limit_value')
                errors.append(('$error.minlength', message % {'limit_value': self.min_length}))
            if getattr(item, 'code', None) == 'max_length':
~~                message = ungettext_lazy(
                    'Ensure this value has at most %(limit_value)d character',
                    'Ensure this value has at most %(limit_value)d characters',
                    'limit_value')
                errors.append(('$error.maxlength', message % {'limit_value': self.max_length}))
        return errors

    def get_min_max_value_errors(self):
        errors = []
        if isinstance(getattr(self, 'min_value', None), int):
            self.widget.attrs['min'] = self.min_value
        if isinstance(getattr(self, 'max_value', None), int):
            self.widget.attrs['max'] = self.max_value
        errkeys = []
        for key, msg in self.error_messages.items():
            if key == 'min_value':
                errors.append(('$error.min', msg))
                errkeys.append(key)
            if key == 'max_value':
                errors.append(('$error.max', msg))
                errkeys.append(key)
        for item in self.validators:
            if getattr(item, 'code', None) == 'min_value' and 'min_value' not in errkeys:
                errors.append(('$error.min', item.message % {'limit_value': self.min_value}))
                errkeys.append('min_value')


## ... source file continues with no further ungettext_lazy examples...

```

