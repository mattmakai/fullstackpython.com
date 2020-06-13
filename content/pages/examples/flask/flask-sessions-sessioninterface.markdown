title: flask.sessions SessionInterface code examples
category: page
slug: flask-sessions-sessioninterface-examples
sortorder: 500021014
toc: False
sidebartitle: flask.sessions SessionInterface
meta: Python example code for the SessionInterface class from the flask.sessions module of the Flask project.


SessionInterface is a class within the flask.sessions module of the Flask project.


## Example 1 from tedivms-flask
[tedivm's flask starter app](https://github.com/tedivm/tedivms-flask) is a
base of [Flask](/flask.html) code and related projects such as
[Celery](/celery.html) which provides a template to start your own
Flask web app. The project comes baked with an admin panel,
[API authentication and authorization](/application-programming-interfaces.html),
[SQLAlchemy](/sqlalchemy.html) and many other common libraries that are
often used with Flask.

The project's code is provided as open source under the
[BSD 2-Clause "Simplified" license](https://github.com/tedivm/tedivms-flask/blob/master/LICENSE.txt).

[**tedivms-flask / app / __init__.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/./__init__.py)

```python
# __init__.py
import boto3
from celery import Celery
from datetime import datetime
import os
import requests
import yaml

from flask import Flask, session, render_template
from flask_mail import Mail
from flask_migrate import Migrate, MigrateCommand
~~from flask.sessions import SessionInterface
from flask_sqlalchemy import SQLAlchemy
from flask_user import user_logged_out
from flask_wtf.csrf import CSRFProtect

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from beaker.middleware import SessionMiddleware

# Instantiate Flask extensions
db = SQLAlchemy()
csrf_protect = CSRFProtect()
mail = Mail()
migrate = Migrate()


def get_config():
    # Instantiate Flask
    app = Flask(__name__)

    # Load App Config settings
    # Load common settings from 'app/settings.py' file
    app.config.from_object('app.settings')
    # Load local settings from environmental variable
    if 'APPLICATION_SETTINGS' in os.environ:


## ... source file abbreviated to get to SessionInterface examples ...



    if 'CACHE_TYPE' not in app.config or not app.config['CACHE_TYPE']:
        app.config['CACHE_TYPE'] = 'file'

    if app.config['CACHE_TYPE'] == 'file':
        if 'CACHE_ROOT' not in app.config or not app.config['CACHE_ROOT']:
            app.config['CACHE_ROOT'] = '/tmp/%s' % __name__

    session_opts['session.type'] = app.config['CACHE_TYPE']

    if 'CACHE_ROOT' in app.config and app.config['CACHE_ROOT']:
        session_opts['session.data_dir'] = app.config['CACHE_ROOT'] + '/session'

    if 'CACHE_URL' in app.config and app.config['CACHE_URL']:
        session_opts['session.url'] = app.config['CACHE_URL']

    session_opts['session.auto'] = app.config.get('SESSION_AUTO', True)
    session_opts['session.cookie_expires'] = app.config.get('SESSION_COOKIE_EXPIRES', 86400)
    session_opts['session.secret'] = app.secret_key

~~    class BeakerSessionInterface(SessionInterface):
        def open_session(self, app, request):
            session = request.environ['beaker.session']
            return session

        def save_session(self, app, session, response):
            session.save()

    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
~~    app.session_interface = BeakerSessionInterface()

    @user_logged_out.connect_via(app)
    def clear_session(sender, user, **extra):
        session.clear()


def init_celery_service(app):
    celery.conf.update(app.config)


def init_error_handlers(app):

    def show_error(status, message='An unknown error has occured.'):
        return render_template('pages/errors.html', error_code=status, message=message), status

    @app.errorhandler(401)
    def error_unauthorized(e):
        return show_error(401, 'Unauthorized')

    @app.errorhandler(403)
    def error_forbidden(e):
        return show_error(403, 'Forbidden')

    @app.errorhandler(404)


## ... source file continues with no further SessionInterface examples...


```

