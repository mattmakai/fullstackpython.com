title: django.contrib.staticfiles.finders get_finders Example Code
category: page
slug: django-contrib-staticfiles-finders-get-finders-examples
sortorder: 500011070
toc: False
sidebartitle: django.contrib.staticfiles.finders get_finders
meta: Python example code for the get_finders callable from the django.contrib.staticfiles.finders module of the Django project.


get_finders is a callable within the django.contrib.staticfiles.finders module of the Django project.


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

[**django-pipeline / pipeline / manifest.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./manifest.py)

```python
# manifest.py
import os

from django.conf.settings import settings as django_settings
~~from django.contrib.staticfiles.finders import get_finders
from django.contrib.staticfiles.storage import staticfiles_storage

from pipeline.conf import settings

from manifesto import Manifest

from pipeline.packager import Packager


class PipelineManifest(Manifest):
    def __init__(self):
        self.packager = Packager()
        self.packages = self.collect_packages()
~~        self.finders = get_finders()
        self.package_files = []

    def collect_packages(self):
        packages = []
        for package_name in self.packager.packages['css']:
            package = self.packager.package_for('css', package_name)
            if package.manifest:
                packages.append(package)
        for package_name in self.packager.packages['js']:
            package = self.packager.package_for('js', package_name)
            if package.manifest:
                packages.append(package)
        return packages

    def cache(self):

        if settings.PIPELINE_ENABLED:
            for package in self.packages:
                path = package.output_filename
                self.package_files.append(path)
                yield staticfiles_storage.url(path)
        else:
            for package in self.packages:
                for path in self.packager.compile(package.paths):


## ... source file continues with no further get_finders examples...

```

