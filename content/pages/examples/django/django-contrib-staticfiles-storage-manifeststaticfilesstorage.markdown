title: django.contrib.staticfiles.storage ManifestStaticFilesStorage Example Code
category: page
slug: django-contrib-staticfiles-storage-manifeststaticfilesstorage-examples
sortorder: 500011074
toc: False
sidebartitle: django.contrib.staticfiles.storage ManifestStaticFilesStorage
meta: Python example code for the ManifestStaticFilesStorage class from the django.contrib.staticfiles.storage module of the Django project.


ManifestStaticFilesStorage is a class within the django.contrib.staticfiles.storage module of the Django project.


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

[**django-pipeline / pipeline / storage.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./storage.py)

```python
# storage.py
import gzip

from io import BytesIO

~~from django.contrib.staticfiles.storage import CachedStaticFilesStorage, ManifestStaticFilesStorage, StaticFilesStorage
from django.contrib.staticfiles.utils import matches_patterns

from django.core.files.base import File


class PipelineMixin(object):
    packing = True

    def post_process(self, paths, dry_run=False, **options):
        if dry_run:
            return

        from pipeline.packager import Packager
        packager = Packager(storage=self)
        for package_name in packager.packages['css']:
            package = packager.package_for('css', package_name)
            output_file = package.output_filename
            if self.packing:
                packager.pack_stylesheets(package)
            paths[output_file] = (self, output_file)
            yield output_file, output_file, True
        for package_name in packager.packages['js']:
            package = packager.package_for('js', package_name)
            output_file = package.output_filename


## ... source file abbreviated to get to ManifestStaticFilesStorage examples ...


                gzipped_file = self._compress(original_file)
                gzipped_path = self.save(gzipped_path, gzipped_file)
                yield gzipped_path, gzipped_path, True


class NonPackagingMixin(object):
    packing = False


class PipelineStorage(PipelineMixin, StaticFilesStorage):
    pass


class NonPackagingPipelineStorage(NonPackagingMixin, PipelineStorage):
    pass


class PipelineCachedStorage(PipelineMixin, CachedStaticFilesStorage):
    pass


class NonPackagingPipelineCachedStorage(NonPackagingMixin, PipelineCachedStorage):
    pass


~~class PipelineManifestStorage(PipelineMixin, ManifestStaticFilesStorage):
    pass


~~class NonPackagingPipelineManifestStorage(NonPackagingMixin, ManifestStaticFilesStorage):
    pass



## ... source file continues with no further ManifestStaticFilesStorage examples...

```

