title: django.template.defaultfilters filesizeformat Example Code
category: page
slug: django-template-defaultfilters-filesizeformat-examples
sortorder: 500011384
toc: False
sidebartitle: django.template.defaultfilters filesizeformat
meta: Python example code that shows how to use the filesizeformat callable from the django.template.defaultfilters module of the Django project.


`filesizeformat` is a callable within the `django.template.defaultfilters` module of the Django project.

<a href="/django-template-defaultfilters-escape-examples.html">escape</a>,
<a href="/django-template-defaultfilters-safe-examples.html">safe</a>,
<a href="/django-template-defaultfilters-slugify-examples.html">slugify</a>,
<a href="/django-template-defaultfilters-striptags-examples.html">striptags</a>,
<a href="/django-template-defaultfilters-title-examples.html">title</a>,
and <a href="/django-template-defaultfilters-truncatechars-examples.html">truncatechars</a>
are several other callables with code examples from the same `django.template.defaultfilters` package.

## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / fields.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/fields.py)

```python
# fields.py
import os

import willow

from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms.fields import ImageField
~~from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _


ALLOWED_EXTENSIONS = ['gif', 'jpg', 'jpeg', 'png', 'webp']
SUPPORTED_FORMATS_TEXT = _("GIF, JPEG, PNG, WEBP")


class WagtailImageField(ImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.max_upload_size = getattr(settings, 'WAGTAILIMAGES_MAX_UPLOAD_SIZE', 10 * 1024 * 1024)
        self.max_image_pixels = getattr(settings, 'WAGTAILIMAGES_MAX_IMAGE_PIXELS', 128 * 1000000)
~~        max_upload_size_text = filesizeformat(self.max_upload_size)

        if self.max_upload_size is not None:
            self.help_text = _(
                "Supported formats: %(supported_formats)s. Maximum filesize: %(max_upload_size)s."
            ) % {
                'supported_formats': SUPPORTED_FORMATS_TEXT,
                'max_upload_size': max_upload_size_text,
            }
        else:
            self.help_text = _(
                "Supported formats: %(supported_formats)s."
            ) % {
                'supported_formats': SUPPORTED_FORMATS_TEXT,
            }

        self.error_messages['invalid_image_extension'] = _(
            "Not a supported image format. Supported formats: %s."
        ) % SUPPORTED_FORMATS_TEXT

        self.error_messages['invalid_image_known_format'] = _(
            "Not a valid %s image."
        )

        self.error_messages['file_too_large'] = _(


## ... source file abbreviated to get to filesizeformat examples ...


    def check_image_file_format(self, f):
        extension = os.path.splitext(f.name)[1].lower()[1:]

        if extension not in ALLOWED_EXTENSIONS:
            raise ValidationError(self.error_messages['invalid_image_extension'], code='invalid_image_extension')

        image_format = extension.upper()
        if image_format == 'JPG':
            image_format = 'JPEG'

        internal_image_format = f.image.format.upper()
        if internal_image_format == 'MPO':
            internal_image_format = 'JPEG'

        if internal_image_format != image_format:
            raise ValidationError(self.error_messages['invalid_image_known_format'] % (
                image_format,
            ), code='invalid_image_known_format')

    def check_image_file_size(self, f):
        if self.max_upload_size is None:
            return

        if f.size > self.max_upload_size:
            raise ValidationError(self.error_messages['file_too_large'] % (
~~                filesizeformat(f.size),
            ), code='file_too_large')

    def check_image_pixel_size(self, f):
        if self.max_image_pixels is None:
            return

        image = willow.Image.open(f)
        width, height = image.get_size()
        frames = image.get_frame_count()
        num_pixels = width * height * frames

        if num_pixels > self.max_image_pixels:
            raise ValidationError(self.error_messages['file_too_many_pixels'] % (
                num_pixels
            ), code='file_too_many_pixels')

    def to_python(self, data):
        f = super().to_python(data)

        if f is not None:
            self.check_image_file_size(f)
            self.check_image_file_format(f)
            self.check_image_pixel_size(f)



## ... source file continues with no further filesizeformat examples...

```

