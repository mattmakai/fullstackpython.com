title: flask.sessions SessionMixin Example Code
category: page
slug: flask-sessions-sessionmixin-examples
sortorder: 500021028
toc: False
sidebartitle: flask.sessions SessionMixin
meta: Example code for understanding how to use the SessionMixin class from the flask.sessions module of the Flask project.


[SessionMixin](https://github.com/pallets/flask/blob/master/src/flask/sessions.py)
is a class used with [Flask](/flask.html) projects that is defined in
the `flask.sessions` module. `SessionMixin` expands a standard
[Python dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
with [session](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)
attributes.

<a href="/flask-sessions-badsignature-examples.html">BadSignature</a>
and
<a href="/flask-sessions-sessioninterface-examples.html">SessionInterface</a>
are a couple of other callables within the `flask.sessions` package that also have code examples.

## Example 1 from Flask-SocketIO
[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
([PyPI package information](https://pypi.org/project/Flask-SocketIO/),
[official tutorial](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
and
[project documentation](https://flask-socketio.readthedocs.io/en/latest/))
is a code library by [Miguel Grinberg](https://blog.miguelgrinberg.com/index)
that provides Socket.IO integration for [Flask](/flask.html) applications.
This extension makes it easier to add bi-directional communications on the
web via the [WebSockets](/websockets.html) protocol.

The Flask-SocketIO project is open source under the
[MIT license](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/LICENSE).

[**Flask-SocketIO / flask_socketio / __init__.py**](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/./flask_socketio/__init__.py)

```python
# __init__.py
from functools import wraps
import os
import sys

gevent_socketio_found = True
try:
    from socketio import socketio_manage
except ImportError:
    gevent_socketio_found = False
if gevent_socketio_found:
    print('The gevent-socketio package is incompatible with this version of '
          'the Flask-SocketIO extension. Please uninstall it, and then '
          'install the latest version of python-socketio in its place.')
    sys.exit(1)

import flask
from flask import _request_ctx_stack, has_request_context, json as flask_json
~~from flask.sessions import SessionMixin
import socketio
from socketio.exceptions import ConnectionRefusedError
from werkzeug.debug import DebuggedApplication
from werkzeug.serving import run_with_reloader

from .namespace import Namespace
from .test_client import SocketIOTestClient

__version__ = '4.3.2dev'


class _SocketIOMiddleware(socketio.WSGIApp):
    def __init__(self, socketio_app, flask_app, socketio_path='socket.io'):
        self.flask_app = flask_app
        super(_SocketIOMiddleware, self).__init__(socketio_app,
                                                  flask_app.wsgi_app,
                                                  socketio_path=socketio_path)

    def __call__(self, environ, start_response):
        environ = environ.copy()
        environ['flask.app'] = self.flask_app
        return super(_SocketIOMiddleware, self).__call__(environ,
                                                         start_response)


~~class _ManagedSession(dict, SessionMixin):
    pass


class SocketIO(object):

    def __init__(self, app=None, **kwargs):
        self.server = None
        self.server_options = {}
        self.wsgi_server = None
        self.handlers = []
        self.namespace_handlers = []
        self.exception_handlers = {}
        self.default_exception_handler = None
        self.manage_session = True
        if app is not None or 'message_queue' in kwargs:
            self.init_app(app, **kwargs)
        else:
            self.server_options.update(kwargs)

    def init_app(self, app, **kwargs):
        if app is not None:
            if not hasattr(app, 'extensions'):
                app.extensions = {}  # pragma: no cover
            app.extensions['socketio'] = self


## ... source file continues with no further SessionMixin examples...

```

