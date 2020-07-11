title: django.contrib.staticfiles.storage HashedFilesMixin Example Code
category: page
slug: django-contrib-staticfiles-storage-hashedfilesmixin-examples
sortorder: 500011073
toc: False
sidebartitle: django.contrib.staticfiles.storage HashedFilesMixin
meta: Python example code for the HashedFilesMixin class from the django.contrib.staticfiles.storage module of the Django project.


HashedFilesMixin is a class within the django.contrib.staticfiles.storage module of the Django project.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / staticfiles.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/staticfiles.py)

```python
# staticfiles.py
import hashlib

from django.conf import settings
~~from django.contrib.staticfiles.storage import HashedFilesMixin
from django.core.files.storage import get_storage_class
from django.templatetags.static import static

from wagtail import __version__


try:
    use_version_strings = settings.WAGTAILADMIN_STATIC_FILE_VERSION_STRINGS
except AttributeError:

    if settings.DEBUG:
        use_version_strings = True
    else:
        storage = get_storage_class(settings.STATICFILES_STORAGE)
        use_version_strings = not issubclass(storage, HashedFilesMixin)


if use_version_strings:
    VERSION_HASH = hashlib.sha1(
        (__version__ + settings.SECRET_KEY).encode('utf-8')
    ).hexdigest()[:8]
else:
    VERSION_HASH = None



## ... source file continues with no further HashedFilesMixin examples...

```

