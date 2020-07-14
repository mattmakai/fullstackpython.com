title: django.contrib.staticfiles.finders BaseStorageFinder Example Code
category: page
slug: django-contrib-staticfiles-finders-basestoragefinder-examples
sortorder: 500011068
toc: False
sidebartitle: django.contrib.staticfiles.finders BaseStorageFinder
meta: Python example code for the BaseStorageFinder class from the django.contrib.staticfiles.finders module of the Django project.


BaseStorageFinder is a class within the django.contrib.staticfiles.finders module of the Django project.


## Example 1 from django-pipeline
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

[**django-pipeline / pipeline / finders.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./finders.py)

```python
# finders.py
from itertools import chain

from django.contrib.staticfiles.storage import staticfiles_storage
~~from django.contrib.staticfiles.finders import BaseFinder, BaseStorageFinder, find, \
    AppDirectoriesFinder as DjangoAppDirectoriesFinder, FileSystemFinder as DjangoFileSystemFinder
from django.utils._os import safe_join
from os.path import normpath

from pipeline.conf import settings


~~class PipelineFinder(BaseStorageFinder):
    storage = staticfiles_storage

    def find(self, path, all=False):
        if not settings.PIPELINE_ENABLED:
            return super(PipelineFinder, self).find(path, all)
        else:
            return []

    def list(self, ignore_patterns):
        return []


class ManifestFinder(BaseFinder):
    def find(self, path, all=False):
        matches = []
        for elem in chain(settings.STYLESHEETS.values(), settings.JAVASCRIPT.values()):
            if normpath(elem['output_filename']) == normpath(path):
                match = safe_join(settings.PIPELINE_ROOT, path)
                if not all:
                    return match
                matches.append(match)
        return matches

    def list(self, *args):


## ... source file continues with no further BaseStorageFinder examples...

```

