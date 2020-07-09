title: django.utils.termcolors colorize Example Code
category: page
slug: django-utils-termcolors-colorize-examples
sortorder: 500011487
toc: False
sidebartitle: django.utils.termcolors colorize
meta: Python example code for the colorize callable from the django.utils.termcolors module of the Django project.


colorize is a callable within the django.utils.termcolors module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / utils / check.py**](https://github.com/divio/django-cms/blob/develop/cms/utils/check.py)

```python
# check.py
from contextlib import contextmanager
import inspect
from itertools import chain

from django.conf import settings
from django.utils.decorators import method_decorator
~~from django.utils.termcolors import colorize
from sekizai.helpers import validate_template

from cms import constants
from cms.models import AliasPluginModel
from cms.utils.conf import get_cms_setting
from cms.utils.compat.dj import is_installed


SUCCESS = 1
WARNING = 2
ERROR = 3
SKIPPED = 4

CHECKERS = []


class FileOutputWrapper(object):
    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr
        self.section_wrapper = FileSectionWrapper
        self.errors = 0
        self.successes = 0
        self.warnings = 0
        self.skips = 0

~~    def colorize(self, msg, opts=(), **kwargs):
~~        return colorize(msg, opts=opts, **kwargs)

    def write_line(self, message=''):
        self.write(u'%s\n' % message)

    def write(self, message):
        self.stdout.write(message)

    def write_stderr_line(self, message=''):
        self.write_stderr(u'%s\n' % message)

    def write_stderr(self, message):
        self.stderr.write(message)

    def success(self, message):
        self.successes += 1
        self.write_line(u'%s %s' % (message, self.colorize('[OK]', fg='green', opts=['bold'])))

    def error(self, message):
        self.errors += 1
        self.write_stderr_line(u'%s %s' % (message, self.colorize('[ERROR]', fg='red', opts=['bold'])))

    def warn(self, message):
        self.warnings += 1
        self.write_stderr_line(u'%s %s' % (message, self.colorize('[WARNING]', fg='yellow', opts=['bold'])))


## ... source file continues with no further colorize examples...

```

