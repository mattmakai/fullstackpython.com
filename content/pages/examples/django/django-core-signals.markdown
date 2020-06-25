title: django.core signals code examples
category: page
slug: django-core-signals-examples
sortorder: 500011084
toc: False
sidebartitle: django.core signals
meta: Python example code for the signals function from the django.core module of the Django project.


signals is a function within the django.core module of the Django project.


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

~~from django.core import signals
try:
    from django.db import close_old_connections
except ImportError:
    from django.db import close_connection
    close_old_connections = None
try:
    from django.core.servers.basehttp import (
            AdminMediaHandler as StaticFilesHandler)
except ImportError:
    from django.contrib.staticfiles.handlers import StaticFilesHandler

from webtest import TestApp
try:
    from webtest.utils import NoDefault
except ImportError:
    NoDefault = ''

from django_webtest.response import DjangoWebtestResponse
from django_webtest.compat import to_string, to_wsgi_safe_string


_notgiven = object()




## ... source file abbreviated to get to signals examples ...


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
~~            signals.request_started.disconnect(close_old_connections)
~~            signals.request_finished.disconnect(close_old_connections)
        else:  # Django < 1.6
~~            signals.request_finished.disconnect(close_connection)

        try:
            req.environ.setdefault('REMOTE_ADDR', '127.0.0.1')

            req.environ['REMOTE_ADDR'] = to_string(req.environ['REMOTE_ADDR'])
            req.environ['PATH_INFO'] = to_string(req.environ['PATH_INFO'])

            data = {}
            on_template_render = partial(store_rendered_templates, data)
            template_rendered.connect(on_template_render)

            response = super(DjangoTestApp, self).do_request(req, status,
                                                             expect_errors)

            def flattend(detail):
                if len(data[detail]) == 1:
                    return data[detail][0]
                return data[detail]

            response.context = None
            response.template = None
            response.templates = data.get('templates', None)

            if data.get('context'):
                response.context = flattend('context')

            if data.get('template'):
                response.template = flattend('template')
            elif data.get('templates'):
                response.template = flattend('templates')

            response.__class__ = self.response_class
            return response
        finally:
            if close_old_connections:  # Django 1.6+
~~                signals.request_started.connect(close_old_connections)
~~                signals.request_finished.connect(close_old_connections)
            else:  # Django < 1.6
~~                signals.request_finished.connect(close_connection)

    def get(self, url, *args, **kwargs):
        extra_environ = kwargs.get('extra_environ')
        user = kwargs.pop('user', _notgiven)
        auto_follow = kwargs.pop('auto_follow', False)

        kwargs['extra_environ'] = self._update_environ(extra_environ, user)
        response = super(DjangoTestApp, self).get(url, *args, **kwargs)

        def is_redirect(r):
            return r.status_int >= 300 and r.status_int < 400
        while auto_follow and is_redirect(response):
            response = response.follow(**kwargs)

        return response

    def post(self, url, *args, **kwargs):
        extra_environ = kwargs.get('extra_environ')
        user = kwargs.pop('user', _notgiven)
        kwargs['extra_environ'] = self._update_environ(extra_environ, user)
        return super(DjangoTestApp, self).post(url, *args, **kwargs)

    def put(self, url, *args, **kwargs):
        extra_environ = kwargs.get('extra_environ')


## ... source file continues with no further signals examples...

```

