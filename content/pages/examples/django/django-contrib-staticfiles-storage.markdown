title: django.contrib.staticfiles storage Example Code
category: page
slug: django-contrib-staticfiles-storage-examples
sortorder: 500011066
toc: False
sidebartitle: django.contrib.staticfiles storage
meta: Python example code for the storage callable from the django.contrib.staticfiles module of the Django project.


storage is a callable within the django.contrib.staticfiles module of the Django project.


## Example 1 from django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).

[**django-debug-toolbar / debug_toolbar / panels / staticfiles.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/panels/staticfiles.py)

```python
# staticfiles.py
from collections import OrderedDict
from os.path import join, normpath

from django.conf import settings
~~from django.contrib.staticfiles import finders, storage
from django.core.files.storage import get_storage_class
from django.utils.functional import LazyObject
from django.utils.translation import gettext_lazy as _, ngettext as __

from debug_toolbar import panels
from debug_toolbar.utils import ThreadCollector

try:
    import threading
except ImportError:
    threading = None


class StaticFile:

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def real_path(self):
        return finders.find(self.path)

    def url(self):
~~        return storage.staticfiles_storage.url(self.path)


class FileCollector(ThreadCollector):
    def collect(self, path, thread=None):
        if path.endswith("/"):
            return
        super().collect(StaticFile(path), thread)


collector = FileCollector()


class DebugConfiguredStorage(LazyObject):

    def _setup(self):

        configured_storage_cls = get_storage_class(settings.STATICFILES_STORAGE)

        class DebugStaticFilesStorage(configured_storage_cls):
            def __init__(self, collector, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.collector = collector

            def url(self, path):
                self.collector.collect(path)
                return super().url(path)

        self._wrapped = DebugStaticFilesStorage(collector)


~~_original_storage = storage.staticfiles_storage


class StaticFilesPanel(panels.Panel):

    name = "Static files"
    template = "debug_toolbar/panels/staticfiles.html"

    @property
    def title(self):
        return _("Static files (%(num_found)s found, %(num_used)s used)") % {
            "num_found": self.num_found,
            "num_used": self.num_used,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_found = 0
        self._paths = {}

    def enable_instrumentation(self):
~~        storage.staticfiles_storage = DebugConfiguredStorage()

    def disable_instrumentation(self):
~~        storage.staticfiles_storage = _original_storage

    @property
    def num_used(self):
        return len(self._paths[threading.currentThread()])

    nav_title = _("Static files")

    @property
    def nav_subtitle(self):
        num_used = self.num_used
        return __("%(num_used)s file used", "%(num_used)s files used", num_used) % {
            "num_used": num_used
        }

    def process_request(self, request):
        collector.clear_collection()
        return super().process_request(request)

    def generate_stats(self, request, response):
        used_paths = collector.get_collection()
        self._paths[threading.currentThread()] = used_paths

        self.record_stats(
            {


## ... source file continues with no further storage examples...

```

