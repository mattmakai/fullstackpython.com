title: django.template.base Context Example Code
category: page
slug: django-template-base-context-examples
sortorder: 500011363
toc: False
sidebartitle: django.template.base Context
meta: Python example code for the Context class from the django.template.base module of the Django project.


Context is a class within the django.template.base module of the Django project.


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



## ... source file continues with no further Context examples...

```

