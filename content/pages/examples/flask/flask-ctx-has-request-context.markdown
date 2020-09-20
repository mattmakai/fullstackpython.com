title: flask.ctx has_request_context Example Code
category: page
slug: flask-ctx-has-request-context-examples
sortorder: 500021013
toc: False
sidebartitle: flask.ctx has_request_context
meta: Python example code that shows how to use the has_request_context callable from the flask.ctx module of the Flask project.


[has_request_context](https://github.com/pallets/flask/blob/master/src/flask/ctx.py)
is a function within the `flask.ctx` module that is useful for
determining if a
[request context](https://flask.palletsprojects.com/en/1.1.x/reqcontext/)
is available or not. There is a similar
[has_app_context](/flask-ctx-has-app-context-examples.html)
function as well that works for the
[application context](https://flask.palletsprojects.com/en/1.1.x/appcontext/).


<a href="/flask-ctx-after-this-request-examples.html">after_this_request</a>
and
<a href="/flask-ctx-has-app-context-examples.html">has_app_context</a>
are a couple of other callables within the `flask.ctx` package that also have code examples.

## Example 1 from Flask AppBuilder
[Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder)
([documentation](https://flask-appbuilder.readthedocs.io/en/latest/)
and
[example apps](https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples))
is a web application generator that uses Flask to automatically create
the code for database-driven applications based on parameters set
by the user. The generated applications include default security settings,
forms, and internationalization support.

Flask App Builder is provided under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/LICENSE).

[**Flask AppBuilder / flask_appbuilder / babel / manager.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/babel/manager.py)

```python
# manager.py
import os

~~from flask import has_request_context, request, session
from flask_babel import Babel

from .views import LocaleView
from ..basemanager import BaseManager


class BabelManager(BaseManager):

    babel = None
    locale_view = None

    def __init__(self, appbuilder):
        super(BabelManager, self).__init__(appbuilder)
        app = appbuilder.get_app
        app.config.setdefault("BABEL_DEFAULT_LOCALE", "en")
        if not app.config.get("LANGUAGES"):
            app.config["LANGUAGES"] = {"en": {"flag": "us", "name": "English"}}
        appbuilder_parent_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), os.pardir
        )
        appbuilder_translations_path = os.path.join(
            appbuilder_parent_dir, "translations"
        )
        if "BABEL_TRANSLATION_DIRECTORIES" in app.config:
            current_translation_directories = app.config.get(
                "BABEL_TRANSLATION_DIRECTORIES"
            )
            translations_path = (
                appbuilder_translations_path + ";" + current_translation_directories
            )
        else:
            translations_path = appbuilder_translations_path + ";translations"
        app.config["BABEL_TRANSLATION_DIRECTORIES"] = translations_path
        self.babel = Babel(app)
        self.babel.locale_selector_func = self.get_locale

    def register_views(self):
        self.locale_view = LocaleView()
        self.appbuilder.add_view_no_menu(self.locale_view)

    @property
    def babel_default_locale(self):
        return self.appbuilder.get_app.config["BABEL_DEFAULT_LOCALE"]

    @property
    def languages(self):
        return self.appbuilder.get_app.config["LANGUAGES"]

    def get_locale(self):
~~        if has_request_context():
            for arg, value in request.args.items():
                if arg == "_l_":
                    if value in self.languages:
                        return value
                    else:
                        return self.babel_default_locale
            locale = session.get("locale")
            if locale:
                return locale
            session["locale"] = self.babel_default_locale
            return session["locale"]



## ... source file continues with no further has_request_context examples...

```


## Example 2 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / forum / locals.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/forum/locals.py)

```python
# locals.py

~~from flask import _request_ctx_stack, has_request_context, request
from werkzeug.local import LocalProxy

from .models import Category, Forum, Post, Topic


@LocalProxy
def current_post():
    return _get_item(Post, 'post_id', 'post')


@LocalProxy
def current_topic():
    if current_post:
        return current_post.topic
    return _get_item(Topic, 'topic_id', 'topic')


@LocalProxy
def current_forum():
    if current_topic:
        return current_topic.forum
    return _get_item(Forum, 'forum_id', 'forum')


@LocalProxy
def current_category():
    if current_forum:
        return current_forum.category
    return _get_item(Category, 'category_id', 'category')


def _get_item(model, view_arg, name):
    if (
~~        has_request_context() and
        not getattr(_request_ctx_stack.top, name, None) and
        view_arg in request.view_args
    ):
        setattr(
            _request_ctx_stack.top,
            name,
            model.query.filter_by(id=request.view_args[view_arg]).first()
        )

    return getattr(_request_ctx_stack.top, name, None)



## ... source file continues with no further has_request_context examples...

```


## Example 3 from Flask-SocketIO
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
~~from flask import _request_ctx_stack, has_request_context, json as flask_json
from flask.sessions import SessionMixin
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


## ... source file abbreviated to get to has_request_context examples ...


        self.default_exception_handler = exception_handler
        return exception_handler

    def on_event(self, message, handler, namespace=None):
        self.on(message, namespace=namespace)(handler)

    def on_namespace(self, namespace_handler):
        if not isinstance(namespace_handler, Namespace):
            raise ValueError('Not a namespace instance.')
        namespace_handler._set_socketio(self)
        if self.server:
            self.server.register_namespace(namespace_handler)
        else:
            self.namespace_handlers.append(namespace_handler)

    def emit(self, event, *args, **kwargs):
        namespace = kwargs.pop('namespace', '/')
        room = kwargs.pop('room', None)
        include_self = kwargs.pop('include_self', True)
        skip_sid = kwargs.pop('skip_sid', None)
        if not include_self and not skip_sid:
            skip_sid = flask.request.sid
        callback = kwargs.pop('callback', None)
        if callback:
            sid = None
~~            if has_request_context():
                sid = getattr(flask.request, 'sid', None)
            original_callback = callback

            def _callback_wrapper(*args):
                return self._handle_event(original_callback, None, namespace,
                                          sid, *args)

            if sid:
                callback = _callback_wrapper
        self.server.emit(event, *args, namespace=namespace, room=room,
                         skip_sid=skip_sid, callback=callback, **kwargs)

    def send(self, data, json=False, namespace=None, room=None,
             callback=None, include_self=True, skip_sid=None, **kwargs):
        skip_sid = flask.request.sid if not include_self else skip_sid
        if json:
            self.emit('json', data, namespace=namespace, room=room,
                      skip_sid=skip_sid, callback=callback, **kwargs)
        else:
            self.emit('message', data, namespace=namespace, room=room,
                      skip_sid=skip_sid, callback=callback, **kwargs)

    def close_room(self, room, namespace=None):
        self.server.close_room(room, namespace)


## ... source file continues with no further has_request_context examples...

```


## Example 4 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / logger.py**](https://github.com/indico/indico/blob/master/indico/core/logger.py)

```python
# logger.py

from __future__ import unicode_literals

import logging
import logging.config
import logging.handlers
import os
import smtplib
import warnings
from email.mime.text import MIMEText
from email.utils import formatdate
from pprint import pformat

import yaml
~~from flask import current_app, has_request_context, request, session

from indico.core.config import config
from indico.util.i18n import set_best_lang
from indico.web.util import get_request_info


try:
    from raven import setup_logging
    from raven.contrib.celery import register_logger_signal, register_signal
    from raven.contrib.flask import Sentry
    from raven.handlers.logging import SentryHandler
except ImportError:
    Sentry = object  # so we can subclass
    has_sentry = False
else:
    has_sentry = True


class AddRequestIDFilter(object):
    def filter(self, record):
~~        record.request_id = request.id if has_request_context() else '0' * 16
        return True


class AddUserIDFilter(object):
    def filter(self, record):
~~        record.user_id = unicode(session.user.id) if has_request_context() and session and session.user else '-'
        return True


class RequestInfoFormatter(logging.Formatter):
    def format(self, record):
        rv = super(RequestInfoFormatter, self).format(record)
        info = get_request_info()
        if info:
            rv += '\n\n' + pformat(info)
        return rv


class FormattedSubjectSMTPHandler(logging.handlers.SMTPHandler):
    def getSubject(self, record):
        return self.subject % record.__dict__

    def emit(self, record):
        try:
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port, timeout=self._timeout)
            msg = MIMEText(self.format(record), 'plain', 'utf-8')
            msg['From'] = self.fromaddr


## ... source file abbreviated to get to has_request_context examples ...


            if formatter.pop('append_request_info', False):
                assert '()' not in formatter
                formatter['()'] = RequestInfoFormatter
        if config.DB_LOG:
            data['loggers']['indico._db'] = {'level': 'DEBUG', 'propagate': False, 'handlers': ['_db']}
            data['handlers']['_db'] = {'class': 'logging.handlers.SocketHandler', 'host': '127.0.0.1', 'port': 9020}
        if config.CUSTOMIZATION_DEBUG and config.CUSTOMIZATION_DIR:
            data['loggers'].setdefault('indico.customization', {})['level'] = 'DEBUG'
        logging.config.dictConfig(data)
        if config.SENTRY_DSN:
            if not has_sentry:
                raise Exception('`raven` must be installed to use sentry logging')
            init_sentry(app)

    @classmethod
    def get(cls, name=None):
        if name is None:
            name = 'indico'
        elif name != 'indico' and not name.startswith('indico.'):
            name = 'indico.' + name
        return logging.getLogger(name)


class IndicoSentry(Sentry):
    def get_user_info(self, request):
~~        if not has_request_context() or not session.user:
            return None
        return {'id': session.user.id,
                'email': session.user.email,
                'name': session.user.full_name}

    def before_request(self, *args, **kwargs):
        super(IndicoSentry, self).before_request()
~~        if not has_request_context():
            return
        self.client.extra_context({'Endpoint': str(request.url_rule.endpoint) if request.url_rule else None,
                                   'Request ID': request.id})
        self.client.tags_context({'locale': set_best_lang()})


def init_sentry(app):
    sentry = IndicoSentry(wrap_wsgi=False, register_signal=True, logging=False)
    sentry.init_app(app)
    handler = SentryHandler(sentry.client, level=getattr(logging, config.SENTRY_LOGGING_LEVEL))
    handler.addFilter(BlacklistFilter({'indico.flask', 'celery.redirected'}))
    setup_logging(handler)
    register_logger_signal(sentry.client)
    register_signal(sentry.client)


def sentry_log_exception():
    try:
        sentry = current_app.extensions['sentry']
    except KeyError:
        return
    sentry.captureException()




## ... source file continues with no further has_request_context examples...

```

