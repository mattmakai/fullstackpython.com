title: django.utils.timezone get_current_timezone Example Code
category: page
slug: django-utils-timezone-get-current-timezone-examples
sortorder: 500011494
toc: False
sidebartitle: django.utils.timezone get_current_timezone
meta: Python example code for the get_current_timezone callable from the django.utils.timezone module of the Django project.


get_current_timezone is a callable within the django.utils.timezone module of the Django project.


## Example 1 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / models / imagemodels.py**](https://github.com/divio/django-filer/blob/develop/filer/models/imagemodels.py)

```python
# imagemodels.py
from __future__ import absolute_import

import logging
from datetime import datetime

from django.conf import settings
from django.db import models
~~from django.utils.timezone import get_current_timezone, make_aware, now
from django.utils.translation import ugettext_lazy as _

from .abstract import BaseImage


logger = logging.getLogger("filer")


class Image(BaseImage):
    date_taken = models.DateTimeField(_('date taken'), null=True, blank=True,
                                      editable=False)
    author = models.CharField(_('author'), max_length=255, null=True, blank=True)
    must_always_publish_author_credit = models.BooleanField(_('must always publish author credit'), default=False)
    must_always_publish_copyright = models.BooleanField(_('must always publish copyright'), default=False)

    class Meta(BaseImage.Meta):
        swappable = 'FILER_IMAGE_MODEL'
        default_manager_name = 'objects'

    def save(self, *args, **kwargs):
        if self.date_taken is None:
            try:
                exif_date = self.exif.get('DateTimeOriginal', None)
                if exif_date is not None:
                    d, t = exif_date.split(" ")
                    year, month, day = d.split(':')
                    hour, minute, second = t.split(':')
                    if getattr(settings, "USE_TZ", False):
~~                        tz = get_current_timezone()
                        self.date_taken = make_aware(datetime(
                            int(year), int(month), int(day),
                            int(hour), int(minute), int(second)), tz)
                    else:
                        self.date_taken = datetime(
                            int(year), int(month), int(day),
                            int(hour), int(minute), int(second))
            except Exception:
                pass
        if self.date_taken is None:
            self.date_taken = now()
        super(Image, self).save(*args, **kwargs)



## ... source file continues with no further get_current_timezone examples...

```

