title: django.utils.functional keep_lazy Example Code
category: page
slug: django-utils-functional-keep-lazy-examples
sortorder: 500011457
toc: False
sidebartitle: django.utils.functional keep_lazy
meta: Python example code for the keep_lazy callable from the django.utils.functional module of the Django project.


keep_lazy is a callable within the django.utils.functional module of the Django project.


## Example 1 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / utils / compatibility.py**](https://github.com/divio/django-filer/blob/develop/filer/utils/compatibility.py)

```python
# compatibility.py
from __future__ import absolute_import, unicode_literals

import sys

from django.utils import six
~~from django.utils.functional import keep_lazy
from django.utils.text import Truncator, format_lazy


def string_concat(*strings):
    return format_lazy('{}' * len(strings), *strings)


def truncate_words(s, num, end_text='...'):
    truncate = end_text and ' %s' % end_text or ''
    return Truncator(s).words(num, truncate=truncate)


~~truncate_words = keep_lazy(truncate_words, six.text_type)


if not six.PY3:
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()


def upath(path):
    if six.PY2 and not isinstance(path, six.text_type):
        return path.decode(fs_encoding)
    return path


def get_delete_permission(opts):
    from django.contrib.auth import get_permission_codename  # noqa
    return '%s.%s' % (opts.app_label, get_permission_codename('delete', opts))


try:
    from PIL import Image as PILImage  # noqa
    from PIL import ImageDraw as PILImageDraw  # noqa
    from PIL import ExifTags as PILExifTags  # noqa
except ImportError:
    try:
        import Image as PILImage  # noqa


## ... source file continues with no further keep_lazy examples...

```

