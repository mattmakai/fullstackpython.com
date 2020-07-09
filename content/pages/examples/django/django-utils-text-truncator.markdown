title: django.utils.text Truncator Example Code
category: page
slug: django-utils-text-truncator-examples
sortorder: 500011488
toc: False
sidebartitle: django.utils.text Truncator
meta: Python example code for the Truncator class from the django.utils.text module of the Django project.


Truncator is a class within the django.utils.text module of the Django project.


## Example 1 from django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).

[**django-extensions / django_extensions / admin / widgets.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/admin/widgets.py)

```python
# widgets.py
import six
from six.moves import urllib
from django import forms
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe
~~from django.utils.text import Truncator


class ForeignKeySearchInput(ForeignKeyRawIdWidget):

    widget_template = None
    search_path = None

    def _media(self):
        js_files = [
            static('django_extensions/js/jquery.bgiframe.js'),
            static('django_extensions/js/jquery.ajaxQueue.js'),
            static('django_extensions/js/jquery.autocomplete.js'),
        ]

        return forms.Media(
            css={'all': (static('django_extensions/css/jquery.autocomplete.css'), )},
            js=js_files,
        )
    media = property(_media)

    def label_for_value(self, value):
        key = self.rel.get_related_field().name
        obj = self.rel.model._default_manager.get(**{key: value})

~~        return Truncator(obj).words(14, truncate='...')

    def __init__(self, rel, search_fields, attrs=None):
        self.search_fields = search_fields
        super().__init__(rel, site, attrs)

    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        opts = self.rel.model._meta
        app_label = opts.app_label
        model_name = opts.object_name.lower()
        related_url = reverse('admin:%s_%s_changelist' % (app_label, model_name))
        if not self.search_path:
            self.search_path = urllib.parse.urljoin(related_url, 'foreignkey_autocomplete/')
        params = self.url_parameters()
        if params:
            url = '?' + '&amp;'.join(['%s=%s' % (k, v) for k, v in params.items()])
        else:
            url = ''

        if 'class' not in attrs:
            attrs['class'] = 'vForeignKeyRawIdAdminField'
        output = [forms.TextInput.render(self, name, value, attrs)]



## ... source file continues with no further Truncator examples...

```


## Example 2 from django-filer
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
from django.utils.functional import keep_lazy
~~from django.utils.text import Truncator, format_lazy


def string_concat(*strings):
    return format_lazy('{}' * len(strings), *strings)


def truncate_words(s, num, end_text='...'):
    truncate = end_text and ' %s' % end_text or ''
~~    return Truncator(s).words(num, truncate=truncate)


truncate_words = keep_lazy(truncate_words, six.text_type)


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


## ... source file continues with no further Truncator examples...

```

