title: django.contrib.staticfiles finders Example Code
category: page
slug: django-contrib-staticfiles-finders-examples
sortorder: 500011065
toc: False
sidebartitle: django.contrib.staticfiles finders
meta: Python example code for the finders callable from the django.contrib.staticfiles module of the Django project.


finders is a callable within the django.contrib.staticfiles module of the Django project.


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
~~        return finders.find(self.path)

    def url(self):
        return storage.staticfiles_storage.url(self.path)


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


## ... source file abbreviated to get to finders examples ...


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
                "num_found": self.num_found,
                "num_used": self.num_used,
                "staticfiles": used_paths,
                "staticfiles_apps": self.get_staticfiles_apps(),
                "staticfiles_dirs": self.get_staticfiles_dirs(),
                "staticfiles_finders": self.get_staticfiles_finders(),
            }
        )

    def get_staticfiles_finders(self):
        finders_mapping = OrderedDict()
~~        for finder in finders.get_finders():
            for path, finder_storage in finder.list([]):
                if getattr(finder_storage, "prefix", None):
                    prefixed_path = join(finder_storage.prefix, path)
                else:
                    prefixed_path = path
                finder_cls = finder.__class__
                finder_path = ".".join([finder_cls.__module__, finder_cls.__name__])
                real_path = finder_storage.path(path)
                payload = (prefixed_path, real_path)
                finders_mapping.setdefault(finder_path, []).append(payload)
                self.num_found += 1
        return finders_mapping

    def get_staticfiles_dirs(self):
        dirs = []
~~        for finder in finders.get_finders():
~~            if isinstance(finder, finders.FileSystemFinder):
                dirs.extend(finder.locations)
        return [(prefix, normpath(dir)) for prefix, dir in dirs]

    def get_staticfiles_apps(self):
        apps = []
~~        for finder in finders.get_finders():
~~            if isinstance(finder, finders.AppDirectoriesFinder):
                for app in finder.apps:
                    if app not in apps:
                        apps.append(app)
        return apps



## ... source file continues with no further finders examples...

```


## Example 2 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / collector.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./collector.py)

```python
# collector.py
import os

from collections import OrderedDict

import django
~~from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage

from pipeline.finders import PipelineFinder


class Collector(object):
    request = None

    def __init__(self, storage=None):
        if storage is None:
            storage = staticfiles_storage
        self.storage = storage

    def _get_modified_time(self, storage, prefixed_path):
        if django.VERSION[:2] >= (1, 10):
            return storage.get_modified_time(prefixed_path)
        return storage.modified_time(prefixed_path)

    def clear(self, path=""):
        dirs, files = self.storage.listdir(path)
        for f in files:
            fpath = os.path.join(path, f)
            self.storage.delete(fpath)
        for d in dirs:
            self.clear(os.path.join(path, d))

    def collect(self, request=None, files=[]):
        if self.request and self.request is request:
            return
        self.request = request
        found_files = OrderedDict()
~~        for finder in finders.get_finders():
            if isinstance(finder, PipelineFinder):
                continue
            for path, storage in finder.list(['CVS', '.*', '*-']):
                if getattr(storage, 'prefix', None):
                    prefixed_path = os.path.join(storage.prefix, path)
                else:
                    prefixed_path = path

                if (prefixed_path not in found_files and
                    (not files or prefixed_path in files)):
                    found_files[prefixed_path] = (storage, path)
                    self.copy_file(path, prefixed_path, storage)

                if files and len(files) == len(found_files):
                    break

        return found_files.keys()

    def copy_file(self, path, prefixed_path, source_storage):
        if not self.delete_file(path, prefixed_path, source_storage):
            return
        with source_storage.open(path) as source_file:
            self.storage.save(prefixed_path, source_file)



## ... source file continues with no further finders examples...

```

