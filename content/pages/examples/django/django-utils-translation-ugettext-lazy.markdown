title: django.utils.translation ugettext_lazy Example Code
category: page
slug: django-utils-translation-ugettext-lazy-examples
sortorder: 500011510
toc: False
sidebartitle: django.utils.translation ugettext_lazy
meta: Python example code for the ugettext_lazy callable from the django.utils.translation module of the Django project.


ugettext_lazy is a callable within the django.utils.translation module of the Django project.


## Example 1 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / imageadmin.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/imageadmin.py)

```python
# imageadmin.py
from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext as _
~~from django.utils.translation import ugettext_lazy

from ..settings import FILER_IMAGE_MODEL
from ..thumbnail_processors import normalize_subject_location
from ..utils.compatibility import string_concat
from ..utils.loader import load_model
from .fileadmin import FileAdmin


Image = load_model(FILER_IMAGE_MODEL)


class ImageAdminForm(forms.ModelForm):
    subject_location = forms.CharField(
        max_length=64, required=False,
        label=_('Subject location'),
        help_text=_('Location of the main subject of the scene. '
                    'Format: "x,y".'))

    def sidebar_image_ratio(self):
        if self.instance:
            return '%.6F' % self.instance.sidebar_image_ratio()
        else:
            return ''

    def _set_previous_subject_location(self, cleaned_data):
        subject_location = self.instance.subject_location
        cleaned_data['subject_location'] = subject_location
        self.data = self.data.copy()
        self.data['subject_location'] = subject_location

    def clean_subject_location(self):
        cleaned_data = super(ImageAdminForm, self).clean()
        subject_location = cleaned_data['subject_location']
        if not subject_location:
            return subject_location

        coordinates = normalize_subject_location(subject_location)

        if not coordinates:
~~            err_msg = ugettext_lazy('Invalid subject location format. ')
            err_code = 'invalid_subject_format'

        elif (
            coordinates[0] > self.instance.width
            or coordinates[1] > self.instance.height
        ):
~~            err_msg = ugettext_lazy(
                'Subject location is outside of the image. ')
            err_code = 'subject_out_of_bounds'
        else:
            return subject_location

        self._set_previous_subject_location(cleaned_data)
        raise forms.ValidationError(
            string_concat(
                err_msg,
~~                ugettext_lazy('Your input: "{subject_location}". '.format(
                    subject_location=subject_location)),
                'Previous value is restored.'),
            code=err_code)

    class Meta(object):
        model = Image
        exclude = ()

    class Media(object):
        css = {
        }
        js = (

        )


class ImageAdmin(FileAdmin):
    change_form_template = 'admin/filer/image/change_form.html'
    form = ImageAdminForm


if FILER_IMAGE_MODEL == 'filer.Image':
    extra_main_fields = ('author', 'default_alt_text', 'default_caption',)
else:


## ... source file continues with no further ugettext_lazy examples...

```

