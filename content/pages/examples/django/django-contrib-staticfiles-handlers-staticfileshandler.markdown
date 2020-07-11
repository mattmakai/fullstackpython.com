title: django.contrib.staticfiles.handlers StaticFilesHandler Example Code
category: page
slug: django-contrib-staticfiles-handlers-staticfileshandler-examples
sortorder: 500011071
toc: False
sidebartitle: django.contrib.staticfiles.handlers StaticFilesHandler
meta: Python example code for the StaticFilesHandler class from the django.contrib.staticfiles.handlers module of the Django project.


StaticFilesHandler is a class within the django.contrib.staticfiles.handlers module of the Django project.


## Example 1 from django-webtest
[django-webtest](https://github.com/django-webtest/django-webtest)
([PyPI package information](https://pypi.org/project/django-webtest/))
is a [Django](/django.html) extension that makes it easier to use
[WebTest](http://docs.pylonsproject.org/projects/webtest/) with
your projects.

The project is open sourced under the
[MIT license](https://github.com/django-webtest/django-webtest/blob/master/LICENSE.txt).

[**django-webtest / django_webtest / __init__.py**](https://github.com/django-webtest/django-webtest/blob/master/django_webtest/./__init__.py)

```python
# __init__.py
import copy

from django.conf import settings
from django.test.signals import template_rendered
from django.core.handlers.wsgi import WSGIHandler
from django.test import TestCase, TransactionTestCase
from django.test.client import store_rendered_templates

from functools import partial

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module

from django.core import signals
try:
    from django.db import close_old_connections
except ImportError:
    from django.db import close_connection
    close_old_connections = None
try:
    from django.core.servers.basehttp import (
            AdminMediaHandler as StaticFilesHandler)
except ImportError:
~~    from django.contrib.staticfiles.handlers import StaticFilesHandler

from webtest import TestApp
try:
    from webtest.utils import NoDefault
except ImportError:
    NoDefault = ''

from django_webtest.response import DjangoWebtestResponse
from django_webtest.compat import to_string, to_wsgi_safe_string


_notgiven = object()


class DjangoTestApp(TestApp):
    response_class = DjangoWebtestResponse

    def __init__(self, *args, **kwargs):
        extra_environ = (kwargs.get('extra_environ') or {}).copy()
        extra_environ.setdefault('HTTP_HOST', 'testserver')
        kwargs['extra_environ'] = extra_environ
        super(DjangoTestApp, self).__init__(self.get_wsgi_handler(), *args, **kwargs)

    def get_wsgi_handler(self):
~~        return StaticFilesHandler(WSGIHandler())

    def set_user(self, user):
        if user is None and 'WEBTEST_USER' in self.extra_environ:
            del self.extra_environ['WEBTEST_USER']
        if user is not None:
            self.extra_environ = self._update_environ(self.extra_environ, user)

    def _update_environ(self, environ, user=_notgiven):
        environ = environ or {}

        if user is not _notgiven:
            if user is None:
                environ['WEBTEST_USER'] = ''
            else:
                username = _get_username(user)
                environ['WEBTEST_USER'] = to_wsgi_safe_string(username)

        return environ

    def do_request(self, req, status, expect_errors):
        if close_old_connections is not None:  # Django 1.6+
            signals.request_started.disconnect(close_old_connections)
            signals.request_finished.disconnect(close_old_connections)
        else:  # Django < 1.6


## ... source file continues with no further StaticFilesHandler examples...

```

