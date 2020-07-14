title: django.template.base VariableDoesNotExist Example Code
category: page
slug: django-template-base-variabledoesnotexist-examples
sortorder: 500011373
toc: False
sidebartitle: django.template.base VariableDoesNotExist
meta: Python example code for the VariableDoesNotExist class from the django.template.base module of the Django project.


VariableDoesNotExist is a class within the django.template.base module of the Django project.


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

[**django-pipeline / pipeline / templatetags / pipeline.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/templatetags/pipeline.py)

```python
# pipeline.py
import logging
import subprocess

from django.contrib.staticfiles.storage import staticfiles_storage

from django import template
~~from django.template.base import Context, VariableDoesNotExist
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from ..collector import default_collector
from ..conf import settings
from ..exceptions import CompilerError
from ..packager import Packager, PackageNotFound
from ..utils import guess_type

logger = logging.getLogger(__name__)

register = template.Library()


class PipelineMixin(object):
    request = None
    _request_var = None

    @property
    def request_var(self):
        if not self._request_var:
            self._request_var = template.Variable('request')
        return self._request_var

    def package_for(self, package_name, package_type):
        package = {
            'js': getattr(settings, 'JAVASCRIPT', {}).get(package_name, {}),
            'css': getattr(settings, 'STYLESHEETS', {}).get(package_name, {}),
        }[package_type]

        if package:
            package = {package_name: package}

        packager = {
            'js': Packager(css_packages={}, js_packages=package),
            'css': Packager(css_packages=package, js_packages={}),
        }[package_type]

        return packager.package_for(package_type, package_name)

    def render(self, context):
        try:
            self.request = self.request_var.resolve(context)
~~        except VariableDoesNotExist:
            pass

    def render_compressed(self, package, package_name, package_type):
        if settings.PIPELINE_ENABLED:
            return self.render_compressed_output(package, package_name,
                                                 package_type)
        else:
            return self.render_compressed_sources(package, package_name,
                                                  package_type)

    def render_compressed_output(self, package, package_name, package_type):
        method = getattr(self, f'render_{package_type}')

        return method(package, package.output_filename)

    def render_compressed_sources(self, package, package_name, package_type):
        if settings.PIPELINE_COLLECTOR_ENABLED:
            default_collector.collect(self.request)

        packager = Packager()
        method = getattr(self, f'render_individual_{package_type}')

        try:
            paths = packager.compile(package.paths)


## ... source file continues with no further VariableDoesNotExist examples...

```

