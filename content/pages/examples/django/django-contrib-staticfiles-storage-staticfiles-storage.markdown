title: django.contrib.staticfiles.storage staticfiles_storage Example Code
category: page
slug: django-contrib-staticfiles-storage-staticfiles-storage-examples
sortorder: 500011076
toc: False
sidebartitle: django.contrib.staticfiles.storage staticfiles_storage
meta: Python example code for the staticfiles_storage callable from the django.contrib.staticfiles.storage module of the Django project.


staticfiles_storage is a callable within the django.contrib.staticfiles.storage module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / fields.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/fields.py)

```python
# fields.py
import re
import mimetypes

from django.conf import settings
~~from django.contrib.staticfiles.storage import staticfiles_storage
from django.core import signing
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.urls import reverse_lazy
from django.forms import fields, models as model_fields, widgets
from django.utils.html import format_html
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _, ungettext_lazy

from djng import app_settings
from .widgets import DropFileWidget, DropImageWidget


class DefaultFieldMixin(object):
    render_label = True

    def has_subwidgets(self):
        return False

    def get_potential_errors(self):
        return self.get_input_required_errors()



## ... source file abbreviated to get to staticfiles_storage examples ...



class FileField(FileFieldMixin, fields.FileField):
    storage = app_settings.upload_storage
    signer = signing.Signer()

    def __init__(self, *args, **kwargs):
        accept = kwargs.pop('accept', '*/*')
        fileupload_url = kwargs.pop('fileupload_url', reverse_lazy('fileupload'))
        area_label = kwargs.pop('area_label', _("Drop file here or click to upload"))
        attrs = {
            'accept': accept,
            'ngf-pattern': accept,
        }
        kwargs.update(widget=DropFileWidget(area_label, fileupload_url, attrs=attrs))
        super(FileField, self).__init__(*args, **kwargs)

    @classmethod
    def preview(cls, file_obj):
        available_name = cls.storage.get_available_name(file_obj.name)
        temp_name = cls.storage.save(available_name, file_obj)
        extension = mimetypes.guess_extension(file_obj.content_type)
        if extension:
            extension = extension[1:]
        else:
            extension = '_blank'
~~        icon_url = staticfiles_storage.url('djng/icons/{}.png'.format(extension))
        return {
            'url': 'url({})'.format(icon_url),
            'temp_name': cls.signer.sign(temp_name),
            'file_name': file_obj.name,
            'file_size': file_obj.size,
            'charset': file_obj.charset,
            'content_type': file_obj.content_type,
            'content_type_extra': file_obj.content_type_extra,
        }


class ImageField(FileFieldMixin, fields.ImageField):
    storage = app_settings.upload_storage
    signer = signing.Signer()

    def __init__(self, *args, **kwargs):
        if 'easy_thumbnails' not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured("'djng.forms.fields.ImageField' requires 'easy-thubnails' to be installed")
        accept = kwargs.pop('accept', 'image/*')
        fileupload_url = kwargs.pop('fileupload_url', reverse_lazy('fileupload'))
        area_label = kwargs.pop('area_label', _("Drop image here or click to upload"))
        attrs = {
            'accept': accept,
            'ngf-pattern': accept,


## ... source file continues with no further staticfiles_storage examples...

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

[**django-pipeline / pipeline / manifest.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./manifest.py)

```python
# manifest.py
import os

from django.conf.settings import settings as django_settings
from django.contrib.staticfiles.finders import get_finders
~~from django.contrib.staticfiles.storage import staticfiles_storage

from pipeline.conf import settings

from manifesto import Manifest

from pipeline.packager import Packager


class PipelineManifest(Manifest):
    def __init__(self):
        self.packager = Packager()
        self.packages = self.collect_packages()
        self.finders = get_finders()
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
~~                yield staticfiles_storage.url(path)
        else:
            for package in self.packages:
                for path in self.packager.compile(package.paths):
                    self.package_files.append(path)
~~                    yield staticfiles_storage.url(path)

        ignore_patterns = getattr(django_settings, "STATICFILES_IGNORE_PATTERNS", None)
        for finder in self.finders:
            for path, storage in finder.list(ignore_patterns):
                if getattr(storage, 'prefix', None):
                    prefixed_path = os.path.join(storage.prefix, path)
                else:
                    prefixed_path = path

                if prefixed_path not in self.package_files:

                    self.package_files.append(prefixed_path)
~~                    yield staticfiles_storage.url(prefixed_path)



## ... source file continues with no further staticfiles_storage examples...

```

