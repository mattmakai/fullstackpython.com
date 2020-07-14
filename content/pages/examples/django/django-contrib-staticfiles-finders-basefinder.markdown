title: django.contrib.staticfiles.finders BaseFinder Example Code
category: page
slug: django-contrib-staticfiles-finders-basefinder-examples
sortorder: 500011067
toc: False
sidebartitle: django.contrib.staticfiles.finders BaseFinder
meta: Python example code for the BaseFinder class from the django.contrib.staticfiles.finders module of the Django project.


BaseFinder is a class within the django.contrib.staticfiles.finders module of the Django project.


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


class PipelineFinder(BaseStorageFinder):
    storage = staticfiles_storage

    def find(self, path, all=False):
        if not settings.PIPELINE_ENABLED:
            return super(PipelineFinder, self).find(path, all)
        else:
            return []

    def list(self, ignore_patterns):
        return []


~~class ManifestFinder(BaseFinder):
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
        return []


~~class CachedFileFinder(BaseFinder):
    def find(self, path, all=False):
        try:
            start, _, extn = path.rsplit('.', 2)
        except ValueError:
            return []
        path = '.'.join((start, extn))
        return find(path, all=all) or []

    def list(self, *args):
        return []


class PatternFilterMixin(object):
    ignore_patterns = []

    def get_ignored_patterns(self):
        return list(set(self.ignore_patterns))

    def list(self, ignore_patterns):
        if ignore_patterns:
            ignore_patterns = ignore_patterns + self.get_ignored_patterns()
        return super(PatternFilterMixin, self).list(ignore_patterns)




## ... source file continues with no further BaseFinder examples...

```

