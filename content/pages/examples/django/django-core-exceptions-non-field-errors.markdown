title: django.core.exceptions NON_FIELD_ERRORS Example Code
category: page
slug: django-core-exceptions-non-field-errors-examples
sortorder: 500011103
toc: False
sidebartitle: django.core.exceptions NON_FIELD_ERRORS
meta: Python example code for the NON_FIELD_ERRORS constant from the django.core.exceptions module of the Django project.


NON_FIELD_ERRORS is a constant within the django.core.exceptions module of the Django project.


## Example 1 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / results.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./results.py)

```python
# results.py
from collections import OrderedDict
from tablib import Dataset

~~from django.core.exceptions import NON_FIELD_ERRORS


class Error:
    def __init__(self, error, traceback=None, row=None):
        self.error = error
        self.traceback = traceback
        self.row = row


class RowResult:
    IMPORT_TYPE_UPDATE = 'update'
    IMPORT_TYPE_NEW = 'new'
    IMPORT_TYPE_DELETE = 'delete'
    IMPORT_TYPE_SKIP = 'skip'
    IMPORT_TYPE_ERROR = 'error'
    IMPORT_TYPE_INVALID = 'invalid'

    valid_import_types = frozenset([
        IMPORT_TYPE_NEW,
        IMPORT_TYPE_UPDATE,
        IMPORT_TYPE_DELETE,
        IMPORT_TYPE_SKIP,
    ])



## ... source file abbreviated to get to NON_FIELD_ERRORS examples ...


        self.diff = None
        self.import_type = None
        self.raw_values = {}


class InvalidRow:

    def __init__(self, number, validation_error, values):
        self.number = number
        self.error = validation_error
        self.values = values
        try:
            self.error_dict = validation_error.message_dict
        except AttributeError:
            self.error_dict = {NON_FIELD_ERRORS: validation_error.messages}

    @property
    def field_specific_errors(self):
        return {
            key: value for key, value in self.error_dict.items()
            if key != NON_FIELD_ERRORS
        }

    @property
    def non_field_specific_errors(self):
~~        return self.error_dict.get(NON_FIELD_ERRORS, [])

    @property
    def error_count(self):
        count = 0
        for error_list in self.error_dict.values():
            count += len(error_list)
        return count


class Result:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.base_errors = []
        self.diff_headers = []
        self.rows = []  # RowResults
        self.invalid_rows = []  # InvalidRow
        self.failed_dataset = Dataset()
        self.totals = OrderedDict([(RowResult.IMPORT_TYPE_NEW, 0),
                                   (RowResult.IMPORT_TYPE_UPDATE, 0),
                                   (RowResult.IMPORT_TYPE_DELETE, 0),
                                   (RowResult.IMPORT_TYPE_SKIP, 0),
                                   (RowResult.IMPORT_TYPE_ERROR, 0),
                                   (RowResult.IMPORT_TYPE_INVALID, 0)])
        self.total_rows = 0


## ... source file continues with no further NON_FIELD_ERRORS examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / messages.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/messages.py)

```python
# messages.py
from django.contrib import messages
~~from django.core.exceptions import NON_FIELD_ERRORS
from django.template.loader import render_to_string
from django.utils.html import format_html, format_html_join


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




## ... source file continues with no further NON_FIELD_ERRORS examples...

```

