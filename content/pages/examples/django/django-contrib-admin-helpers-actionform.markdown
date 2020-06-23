title: django.contrib.admin.helpers ActionForm code examples
category: page
slug: django-contrib-admin-helpers-actionform-examples
sortorder: 500011020
toc: False
sidebartitle: django.contrib.admin.helpers ActionForm
meta: Python example code for the ActionForm class from the django.contrib.admin.helpers module of the Django project.


ActionForm is a class within the django.contrib.admin.helpers module of the Django project.


## Example 1 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / forms.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./forms.py)

```python
# forms.py
import os.path

from django import forms
~~from django.contrib.admin.helpers import ActionForm
from django.utils.translation import gettext_lazy as _


class ImportForm(forms.Form):
    import_file = forms.FileField(
        label=_('File to import')
        )
    input_format = forms.ChoiceField(
        label=_('Format'),
        choices=(),
        )

    def __init__(self, import_formats, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        for i, f in enumerate(import_formats):
            choices.append((str(i), f().get_title(),))
        if len(import_formats) > 1:
            choices.insert(0, ('', '---'))

        self.fields['input_format'].choices = choices


class ConfirmImportForm(forms.Form):


## ... source file abbreviated to get to ActionForm examples ...




class ExportForm(forms.Form):
    file_format = forms.ChoiceField(
        label=_('Format'),
        choices=(),
        )

    def __init__(self, formats, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        for i, f in enumerate(formats):
            choices.append((str(i), f().get_title(),))
        if len(formats) > 1:
            choices.insert(0, ('', '---'))

        self.fields['file_format'].choices = choices


def export_action_form_factory(formats):
~~    class _ExportActionForm(ActionForm):
        file_format = forms.ChoiceField(
            label=_('Format'), choices=formats, required=False)
    _ExportActionForm.__name__ = str('ExportActionForm')

    return _ExportActionForm



## ... source file continues with no further ActionForm examples...

```

