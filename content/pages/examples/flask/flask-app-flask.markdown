title: flask.app Flask Example Code
category: page
slug: flask-app-flask-examples
sortorder: 500021001
toc: False
sidebartitle: flask.app Flask
meta: Example code for understanding how to use the Flask class from the flask.app module of the Flask project.


[Flask](https://github.com/pallets/flask/blob/master/src/flask/app.py) is
a class within the `flask.app` module of the [Flask](/flask.html) framework
that implements the [WSGI application specification](/wsgi-servers.html).
This class acts as a central registry for a significant amount of a Flask
application's functionality, including URL rounting,
[template configurations](/template-engines.html), and handling view functions.

<a href="/flask-app-badrequest-examples.html">BadRequest</a>,
<a href="/flask-app-headers-examples.html">Headers</a>,
and <a href="/flask-app-immutabledict-examples.html">ImmutableDict</a>
are several other callables with code examples from the same `flask.app` package.

You should read up on these subjects along with these `Flask` examples:

* [web development](/web-development.html) and [web design](/web-design.html)
* [Flask](/flask.html) and [web framework](/web-frameworks.html) concepts


## Example 1 from Braintree Flask app
[Braintree's Flask example payments app](https://github.com/braintree/braintree_flask_example)
demonstrates how to incorporate this payment provider's
[API](/application-programming-interfaces.html) into your
[Flask](/flask.html) [web application](/web-development.html).
The code is open sourced under the
[MIT license](https://github.com/braintree/braintree_flask_example/blob/master/LICENSE).

[**Braintree Flask app / app.py**](https://github.com/braintree/braintree_flask_example/blob/master/././app.py)

```python
# app.py
~~from flask import Flask, redirect, url_for, render_template, request, flash

import os
from os.path import join, dirname
from dotenv import load_dotenv
import braintree
from gateway import generate_client_token, transact, find_transaction

load_dotenv()

~~app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

PORT = int(os.environ.get('PORT', 4567))

TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('new_checkout'))

@app.route('/checkouts/new', methods=['GET'])
def new_checkout():
    client_token = generate_client_token()
    return render_template('checkouts/new.html', client_token=client_token)

@app.route('/checkouts/<transaction_id>', methods=['GET'])


## ... source file continues with no further Flask examples...

```


## Example 2 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [Flask](/flask.html). The application can be used
as-is to run CTF events, or modified for custom rules for related
scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / manage.py**](https://github.com/CTFd/CTFd/blob/master/././manage.py)

```python
# manage.py
~~from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from CTFd import create_app
from CTFd.utils import get_config as get_config_util, set_config as set_config_util
from CTFd.models import *

app = create_app()

manager = Manager(app)
manager.add_command("db", MigrateCommand)


def jsenums():
    from CTFd.constants import JS_ENUMS
    import json
    import os

    path = os.path.join(app.root_path, "themes/core/assets/js/constants.js")

    with open(path, "w+") as f:
        for k, v in JS_ENUMS.items():
            f.write("const {} = Object.freeze({});".format(k, json.dumps(v)))



## ... source file continues with no further Flask examples...

```


## Example 3 from Flask AppBuilder
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

[**Flask AppBuilder / flask_appbuilder / tests / _test_oauth_registration_role.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/tests/_test_oauth_registration_role.py)

```python
# _test_oauth_registration_role.py
import logging
import unittest

~~from flask import Flask
from flask_appbuilder import AppBuilder, SQLA


logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger(__name__)


class OAuthRegistrationRoleTestCase(unittest.TestCase):
    def setUp(self):
~~        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.db = SQLA(self.app)

    def tearDown(self):
        self.appbuilder = None
        self.app = None
        self.db = None

    def test_self_registration_not_enabled(self):
        self.app.config["AUTH_USER_REGISTRATION"] = False
        self.appbuilder = AppBuilder(self.app, self.db.session)

        result = self.appbuilder.sm.auth_user_oauth(userinfo={"username": "testuser"})

        self.assertIsNone(result)
        self.assertEqual(len(self.appbuilder.sm.get_all_users()), 0)

    def test_register_and_attach_static_role(self):
        self.app.config["AUTH_USER_REGISTRATION"] = True
        self.app.config["AUTH_USER_REGISTRATION_ROLE"] = "Public"
        self.appbuilder = AppBuilder(self.app, self.db.session)

        user = self.appbuilder.sm.auth_user_oauth(userinfo={"username": "testuser"})



## ... source file continues with no further Flask examples...

```


## Example 4 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / app.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/./app.py)

```python
# app.py
import logging
import logging.config
import os
import sys
import time
import warnings
from datetime import datetime

~~from flask import Flask, request
from flask_login import current_user
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError, ProgrammingError

from flaskbb._compat import iteritems, string_types
from flaskbb.extensions import (alembic, allows, babel, cache, celery, csrf,
                                db, debugtoolbar, limiter, login_manager, mail,
                                redis_store, themes, whooshee)
from flaskbb.plugins import spec
from flaskbb.plugins.manager import FlaskBBPluginManager
from flaskbb.plugins.models import PluginRegistry
from flaskbb.plugins.utils import remove_zombie_plugins_from_db, template_hook
from flaskbb.user.models import Guest, User
from flaskbb.utils.helpers import (app_config_from_env, crop_title,
                                   format_date, format_datetime,
                                   forum_is_unread, get_alembic_locations,
                                   get_flaskbb_config, is_online, mark_online,
                                   render_template, time_since, time_utcnow,
                                   topic_is_unread)
from flaskbb.utils.requirements import (CanBanUser, CanEditUser, IsAdmin,
                                        IsAtleastModerator, can_delete_topic,
                                        can_edit_post, can_moderate,
                                        can_post_reply, can_post_topic,
                                        has_permission,
                                        permission_with_identity)
from flaskbb.utils.search import (ForumWhoosheer, PostWhoosheer,
                                  TopicWhoosheer, UserWhoosheer)
from flaskbb.utils.settings import flaskbb_config
from flaskbb.utils.translations import FlaskBBDomain

from . import markup  # noqa
from .auth import views as auth_views  # noqa
from .deprecation import FlaskBBDeprecation
from .display.navigation import NavigationContentType
from .forum import views as forum_views  # noqa
from .management import views as management_views  # noqa
from .user import views as user_views  # noqa

logger = logging.getLogger(__name__)


def create_app(config=None, instance_path=None):

~~    app = Flask(
        "flaskbb", instance_path=instance_path, instance_relative_config=True
    )

    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    configure_app(app, config)
    configure_celery_app(app, celery)
    configure_extensions(app)
    load_plugins(app)
    configure_blueprints(app)
    configure_template_filters(app)
    configure_context_processors(app)
    configure_before_handlers(app)
    configure_errorhandlers(app)
    configure_migrations(app)
    configure_translations(app)
    app.pluggy.hook.flaskbb_additional_setup(app=app, pluggy=app.pluggy)

    return app


def configure_app(app, config):
    app.config.from_object("flaskbb.configs.default.DefaultConfig")


## ... source file continues with no further Flask examples...

```


## Example 5 from flask-base
[flask-base](https://github.com/hack4impact/flask-base)
([project documentation](http://hack4impact.github.io/flask-base/))
provides boilerplate code for new [Flask](/flask.html) web apps.
The purpose of the boilerplate is to stitch together disparate
libraries that are commonly used in Flask projects, such as
[Redis](/redis.html) for fast caching and transient data storage,
[SendGrid](https://www.twilio.com/sendgrid) for transactional email,
[SQLAlchemy](/sqlalchemy.html) for persistent data storage through a
[relational database](/databases.html) backend,
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) for form
handling and many others.

flask-base is provided as open source under the
[MIT license](https://github.com/hack4impact/flask-base/blob/master/LICENSE.md).

[**flask-base / app / __init__.py**](https://github.com/hack4impact/flask-base/blob/master/app/./__init__.py)

```python
# __init__.py
import os

~~from flask import Flask
from flask_assets import Environment
from flask_compress import Compress
from flask_login import LoginManager
from flask_mail import Mail
from flask_rq import RQ
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from app.assets import app_css, app_js, vendor_css, vendor_js
from config import config as Config

basedir = os.path.abspath(os.path.dirname(__file__))

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
compress = Compress()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'


def create_app(config):
~~    app = Flask(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app.config.from_object(Config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    Config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)
    RQ(app)

    from .utils import register_template_utils
    register_template_utils(app)

    assets_env = Environment(app)
    dirs = ['assets/styles', 'assets/scripts']
    for path in dirs:
        assets_env.append_path(os.path.join(basedir, path))


## ... source file continues with no further Flask examples...

```


## Example 6 from flask-bones
[flask-bones](https://github.com/cburmeister/flask-bones)
([demo](http://flask-bones.herokuapp.com/))
is large scale [Flask](/flask.html) example application built
with [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
([example Blueprint code](/flask-blueprints-blueprint-examples.html)).
This project is provided as open source under the
[MIT license](https://github.com/cburmeister/flask-bones/blob/master/LICENSE).

[**flask-bones / app / __init__.py**](https://github.com/cburmeister/flask-bones/blob/master/app/./__init__.py)

```python
# __init__.py
import time

~~from flask import Flask, g, render_template, request
import arrow
import requests

from app import config
from app.assets import assets
from app.auth import auth
from app.commands import create_db, drop_db, populate_db, recreate_db
from app.database import db
from app.extensions import lm, travis, mail, migrate, bcrypt, babel, rq, limiter
from app.user import user
from app.utils import url_for_other_page


def create_app(config=config.base_config):
~~    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_jinja_env(app)
    register_commands(app)

    def get_locale():
        return request.accept_languages.best_match(config.SUPPORTED_LOCALES)

    if babel.locale_selector_func is None:
        babel.locale_selector_func = get_locale

    @app.before_request
    def before_request():
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
        g.pjax = 'X-PJAX' in request.headers

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')



## ... source file continues with no further Flask examples...

```


## Example 7 from flask-bookshelf
[flask-bookshelf](https://github.com/damyanbogoev/flask-bookshelf) is the
example [Flask](/flask.html) application that developers create when
going through
[this Flask series of blog posts](https://damyanon.net/tags/flask-series/).

[**flask-bookshelf / bookshelf / __init__.py**](https://github.com/damyanbogoev/flask-bookshelf/blob/master/bookshelf/./__init__.py)

```python
# __init__.py
~~from flask import abort, Flask, g, render_template, request, current_app
from flask_babel import Babel
from flask_security import current_user
from bookshelf.utils import get_instance_folder_path
from bookshelf.main.controllers import main
from bookshelf.admin.controllers import admin
from bookshelf.cache import cache
from bookshelf.config import configure_app
from bookshelf.data.models import db

~~app = Flask(
    __name__,
    instance_path=get_instance_folder_path(),
    instance_relative_config=True,
    template_folder="templates",
)

babel = Babel(app)
configure_app(app)
cache.init_app(app)
db.init_app(app)
app.jinja_env.add_extension("jinja2.ext.loopcontrols")


@app.url_defaults
def set_language_code(endpoint, values):
    if "lang_code" in values or not g.get("lang_code", None):
        return
    if app.url_map.is_endpoint_expecting(endpoint, "lang_code"):
        values["lang_code"] = g.lang_code


@app.url_value_preprocessor
def get_lang_code(endpoint, values):
    if values is not None:


## ... source file continues with no further Flask examples...

```


## Example 8 from flaskex
[Flaskex](https://github.com/anfederico/Flaskex) is a working example
[Flask](/flask.html) web application intended as a base to build your
own applications upon. The application comes with pre-built sign up, log in
and related screens, as well as a database backend. Flaskex is provided
as open source under the
[MIT license](https://github.com/anfederico/Flaskex/blob/master/LICENSE.txt).

[**flaskex / app.py**](https://github.com/anfederico/Flaskex/blob/master/././app.py)

```python
# app.py

from scripts import tabledef
from scripts import forms
from scripts import helpers
~~from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os

~~app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only


@app.route('/', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if form.validate():
                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('login.html', form=form)
    user = helpers.get_user()
    return render_template('home.html', user=user)


@app.route("/logout")
def logout():


## ... source file continues with no further Flask examples...

```


## Example 9 from Flask-HTTPAuth
[Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth)
([documentation](https://flask-httpauth.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/Flask-HTTPAuth/))
is a [Flask](/flask.html) framework extension that creates
Basic and Digest HTTP authentication for routes. This project
is primarily built and maintained by
[Miguel Grinberg](https://blog.miguelgrinberg.com/). It is provided
as open source under the
[MIT license](https://github.com/miguelgrinberg/Flask-HTTPAuth/blob/master/LICENSE).

[**Flask-HTTPAuth / tests / test_basic_get_password.py**](https://github.com/miguelgrinberg/Flask-HTTPAuth/blob/master/./tests/test_basic_get_password.py)

```python
# test_basic_get_password.py
import unittest
import base64
~~from flask import Flask
from flask_httpauth import HTTPBasicAuth


class HTTPAuthTestCase(unittest.TestCase):
    def setUp(self):
~~        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'my secret'

        basic_auth = HTTPBasicAuth()

        @basic_auth.get_password
        def get_basic_password(username):
            if username == 'john':
                return 'hello'
            elif username == 'susan':
                return 'bye'
            else:
                return None

        @app.route('/')
        def index():
            return 'index'

        @app.route('/basic')
        @basic_auth.login_required
        def basic_auth_route():
            return 'basic_auth:' + basic_auth.username()

        self.app = app
        self.basic_auth = basic_auth


## ... source file continues with no further Flask examples...

```


## Example 10 from flask-phone-input
[flask-phone-input](https://github.com/miguelgrinberg/flask-phone-input)
is an example application that ties together the
[intTellInput.js](https://github.com/jackocnr/intl-tel-input)
JavaScript plugin with the
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) form-handling
library. flask-phone-input is provided as open source under the
[MIT license](https://github.com/miguelgrinberg/flask-phone-input/blob/1a1c227c044474ce0fe133493d7f8b0fb8312409/LICENSE).

[**flask-phone-input / app.py**](https://github.com/miguelgrinberg/flask-phone-input/blob/master/././app.py)

```python
# app.py
~~from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import phonenumbers
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

~~app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
Bootstrap(app)


class PhoneForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhoneForm()
    if form.validate_on_submit():
        session['phone'] = form.phone.data
        return redirect(url_for('show_phone'))
    return render_template('index.html', form=form)


## ... source file continues with no further Flask examples...

```


## Example 11 from flaskSaaS
[flaskSaas](https://github.com/alectrocute/flaskSaaS) is a boilerplate
starter project to build a software-as-a-service (SaaS) web application
in [Flask](/flask.html), with [Stripe](/stripe.html) for billing. The
boilerplate relies on many common Flask extensions such as
[Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/),
[Flask-Login](https://flask-login.readthedocs.io/en/latest/),
[Flask-Admin](https://flask-admin.readthedocs.io/en/latest/), and
many others. The project is provided as open source under the
[MIT license](https://github.com/alectrocute/flaskSaaS/blob/master/LICENSE).

[**flaskSaaS / app / __init__.py**](https://github.com/alectrocute/flaskSaaS/blob/master/app/./__init__.py)

```python
# __init__.py
~~from flask import Flask

~~app = Flask(__name__)

app.config.from_object('app.config')

from app.logger_setup import logger

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask.ext.mail import Mail
mail = Mail(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
toolbar = DebugToolbarExtension(app)

from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from app.views import main, user, error
app.register_blueprint(user.userbp)

from flask.ext.login import LoginManager
from app.models import User


## ... source file continues with no further Flask examples...

```


## Example 12 from Flask-SocketIO
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

[**Flask-SocketIO / test_socketio.py**](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/././test_socketio.py)

```python
# test_socketio.py
import json
import unittest
import coverage

cov = coverage.coverage(branch=True)
cov.start()

~~from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace, disconnect

~~app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
disconnected = None


@socketio.on('connect')
def on_connect():
    if request.args.get('fail'):
        return False
    send('connected')
    send(json.dumps(request.args.to_dict(flat=False)))
    send(json.dumps({h: request.headers[h] for h in request.headers.keys()
                     if h not in ['Host', 'Content-Type', 'Content-Length']}))


@socketio.on('disconnect')
def on_disconnect():
    global disconnected
    disconnected = '/'


@socketio.on('connect', namespace='/test')
def on_connect_test():
    send('connected-test')


## ... source file abbreviated to get to Flask examples ...


        client.emit('exit', {}, namespace='/ns')
        self.assertFalse(client.is_connected('/ns'))
        with self.assertRaises(RuntimeError):
            client.emit('hello', {}, namespace='/ns')

    def test_emit_class_based(self):
        client = socketio.test_client(app, namespace='/ns')
        client.get_received('/ns')
        client.emit('my_custom_event', {'a': 'b'}, namespace='/ns')
        received = client.get_received('/ns')
        self.assertEqual(len(received), 1)
        self.assertEqual(len(received[0]['args']), 1)
        self.assertEqual(received[0]['name'], 'my custom response')
        self.assertEqual(received[0]['args'][0]['a'], 'b')

    def test_request_event_data_class_based(self):
        client = socketio.test_client(app, namespace='/ns')
        client.get_received('/ns')
        global request_event_data
        request_event_data = None
        client.emit('other_custom_event', 'foo', namespace='/ns')
        expected_data = {'message': 'other_custom_event', 'args': ('foo',)}
        self.assertEqual(request_event_data, expected_data)

    def test_delayed_init(self):
~~        app = Flask(__name__)
        socketio = SocketIO(allow_upgrades=False, json=flask_json)

        @socketio.on('connect')
        def on_connect():
            send({'connected': 'foo'}, json=True)

        socketio.init_app(app, cookie='foo')
        self.assertFalse(socketio.server.eio.allow_upgrades)
        self.assertEqual(socketio.server.eio.cookie, 'foo')

        client = socketio.test_client(app)
        received = client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0]['args'], {'connected': 'foo'})


if __name__ == '__main__':
    unittest.main()



## ... source file continues with no further Flask examples...

```


## Example 13 from Flask-User
[Flask-User](https://github.com/lingthio/Flask-User)
([PyPI information](https://pypi.org/project/Flask-User/)
and
[project documentation](https://flask-user.readthedocs.io/en/latest/))
is a [Flask](/flask.html) extension that makes it easier to add
custom user account management and authentication to the projects
you are building. The extension supports persistent data storage
through both [relational databases](/databases.html) and
[MongoDB](/mongodb.html). The project is provided as open source under
the [MIT license](https://github.com/lingthio/Flask-User/blob/master/LICENSE.txt).

[**Flask-User / flask_user / user_manager.py**](https://github.com/lingthio/Flask-User/blob/master/flask_user/./user_manager.py)

```python
# user_manager.py


import datetime

~~from flask import abort, Blueprint, current_app, Flask, session
from flask_login import LoginManager
from wtforms import ValidationError

from . import ConfigError
from . import forms
from .db_manager import DBManager
from .email_manager import EmailManager
from .password_manager import PasswordManager
from .token_manager import TokenManager
from .translation_utils import lazy_gettext as _  # map _() to lazy_gettext()
from .user_manager__settings import UserManager__Settings
from .user_manager__utils import UserManager__Utils
from .user_manager__views import UserManager__Views


class UserManager(UserManager__Settings, UserManager__Utils, UserManager__Views):

    def __init__(self, app, db, UserClass, **kwargs):

        self.app = app
        if app:
            self.init_app(app, db, UserClass, **kwargs)

    def init_app(
        self, app, db, UserClass,
        UserInvitationClass=None,
        UserEmailClass=None,
        RoleClass=None,    # Only used for testing
        ):

~~        if not isinstance(app, Flask):
            raise TypeError("flask_user.UserManager.init_app(): Parameter 'app' is an instance of class '%s' "
                            "instead of a subclass of class 'flask.Flask'."
                            % app.__class__.__name__)

        app.user_manager = self

        self.db = db

        for attrib_name in dir(self):
            if attrib_name[0:5] == 'USER_':
                default_value = getattr(UserManager, attrib_name)
                setattr(self, attrib_name, app.config.get(attrib_name, default_value))

        if not self.USER_EMAIL_SENDER_EMAIL:
            default_sender = app.config.get('DEFAULT_MAIL_SENDER', None)
            default_sender = app.config.get('MAIL_DEFAULT_SENDER', default_sender)
            if default_sender:
                if default_sender[-1:] == '>':
                    start = default_sender.rfind('<')
                    if start >= 1:
                        self.USER_EMAIL_SENDER_EMAIL = default_sender[start + 1:-1]
                        if not self.USER_EMAIL_SENDER_NAME:
                            self.USER_EMAIL_SENDER_NAME = default_sender[0:start].strip(' "')
                else:


## ... source file continues with no further Flask examples...

```


## Example 14 from Flask-VueJs-Template
[Flask-VueJs-Template](https://github.com/gtalarico/flask-vuejs-template)
([demo site](https://flask-vuejs-template.herokuapp.com/))
is a minimal [Flask](/flask.html) boilerplate starter project that
combines Flask, [Vue.js](https://www.fullstackpython.com/vuejs.html),
and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).
The project provides some sensible defaults that are easy to continue
building on, and the source code is open source under the
[MIT license](https://github.com/gtalarico/flask-vuejs-template/blob/master/LICENSE.md).

[**Flask-VueJs-Template / app / __init__.py**](https://github.com/gtalarico/flask-vuejs-template/blob/master/app/./__init__.py)

```python
# __init__.py
import os
~~from flask import Flask, current_app, send_file

from .api import api_bp
from .client import client_bp

~~app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)





## ... source file continues with no further Flask examples...

```


## Example 15 from Flasky
[Flasky](https://github.com/miguelgrinberg/flasky) is a wonderful
example application by
[Miguel Grinberg](https://github.com/miguelgrinberg) that he builds
while teaching developers how to use [Flask](/flask.html) in
[his books and videos](https://courses.miguelgrinberg.com/). Flasky
is [open sourced under the MIT license](https://github.com/miguelgrinberg/flasky/blob/master/LICENSE).

[**Flasky / app / __init__.py**](https://github.com/miguelgrinberg/flasky/blob/master/./app/__init__.py)

```python
# __init__.py
~~from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
~~    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app


## ... source file continues with no further Flask examples...

```


## Example 16 from Datadog Flask Example App
The [Datadog Flask example app](https://github.com/DataDog/trace-examples/tree/master/python/flask)
contains many examples of the [Flask](/flask.html) core functions
available to a developer using the [web framework](/web-frameworks.html).

[**Datadog Flask Example App / python/flask/app / app.py**](https://github.com/DataDog/trace-examples/blob/master/python/flask/app/./app.py)

```python
# app.py
from ddtrace import patch_all; patch_all(flask=True, requests=True)  # noqa

from ddtrace import tracer

~~from flask import Flask, Response
from flask import after_this_request
from flask import abort, jsonify, render_template, url_for
from flask.views import View
from werkzeug.routing import Rule

from flask_caching import Cache
from flask_cors import CORS

import requests

from .blueprint import bp
from .exceptions import AppException
from .limiter import limiter
from .signals import connect_signals

~~app = Flask(__name__)

app.register_blueprint(bp)

connect_signals(app)

CORS(app)
Cache(app, config=dict(CACHE_TYPE='simple'))
limiter.init_app(app)


@app.context_processor
def inject_url_map():
    return dict(url_map=app.url_map)


@app.before_first_request
def before_first_request():
    print('Hook: before_first_request')


@app.before_request
def before_request():
    print('Hook: before_request')



## ... source file continues with no further Flask examples...

```


## Example 17 from keras-flask-deploy-webapp
The
[keras-flask-deploy-webapp](https://github.com/mtobeiyf/keras-flask-deploy-webapp)
project combines the [Flask](/flask.html) [web framework](/web-frameworks.html)
with the [Keras deep learning library](https://keras.io/) to provide
an example image classifier that is easy to [deploy](/deployment.html).
The application can be quckly run in a [Docker](/docker.html) container
on your local development environment. The project is licensed under the
[GNU General Public License v3.0](https://github.com/mtobeiyf/keras-flask-deploy-webapp/blob/master/LICENSE).

[**keras-flask-deploy-webapp / app.py**](https://github.com/mtobeiyf/keras-flask-deploy-webapp/blob/master/././app.py)

```python
# app.py
import os
import sys

~~from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np
from util import base64_to_pil


~~app = Flask(__name__)



from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
model = MobileNetV2(weights='imagenet')

print('Model loaded. Check http://127.0.0.1:5000/')


MODEL_PATH = 'models/your_model.h5'



def model_predict(img, model):
    img = img.resize((224, 224))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    return preds



## ... source file continues with no further Flask examples...

```


## Example 18 from sandman2
[sandman2](https://github.com/jeffknupp/sandman2)
([project documentation](https://sandman2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/sandman2/))
is a code library for automatically generating
[RESTful APIs](/application-programming-interfaces.html) from
existing database schemas. This approach is handy for solving
straightforward situations where you want to put an abstraction
layer between one or more applications and your
[relational database](/databases.html) to prevent or reduce
direct database access.

The sandman2 project is provided under the
[Apache License 2.0](https://github.com/jeffknupp/sandman2/blob/master/LICENSE).

[**sandman2 / sandman2 / app.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./app.py)

```python
# app.py

~~from flask import Flask, current_app, jsonify
from sqlalchemy.sql import sqltypes

from sandman2.exception import (
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    NotAcceptableException,
    NotImplementedException,
    ConflictException,
    ServerErrorException,
    ServiceUnavailableException,
    )
from sandman2.service import Service
from sandman2.model import db, Model, AutomapModel
from sandman2.admin import CustomAdminView
from flask_admin import Admin
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

def get_app(
        database_uri,
        exclude_tables=None,
        user_models=None,
        reflect_all=True,
        read_only=False,
        schema=None):
~~    app = Flask('sandman2')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SANDMAN2_READ_ONLY'] = read_only
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.classes = []
    db.init_app(app)
    admin = Admin(app, base_template='layout.html', template_mode='bootstrap3')
    _register_error_handlers(app)
    if user_models:
        with app.app_context():
            _register_user_models(user_models, admin, schema=schema)
    elif reflect_all:
        with app.app_context():
            _reflect_all(exclude_tables, admin, read_only, schema=schema)

    @app.route('/')
    def index():
        routes = {}
        for cls in app.classes:
            routes[cls.__model__.__name__] = '{}{{/{}}}'.format(
                cls.__model__.__url__,
                cls.__model__.primary_key())
        return jsonify(routes)
    return app



## ... source file continues with no further Flask examples...

```


## Example 19 from Science Flask
[Science Flask](https://github.com/danielhomola/science_flask)
is a [Flask](/flask.html)-powered web application for online
scientific research tools. The project was built as a template
for any scientist or groups of scientists to use when working
together without having to really understand how the application
is built. The application includes an academic registration
process (only valid academic email addresses can be used), an
admin panel, logging, and analysis forms.

[@danielhomola](https://github.com/danielhomola) is the
primary creator of Science Flask and the project is open
source under the
[GNU General Public License](https://github.com/danielhomola/science_flask/blob/master/LICENSE).

[**Science Flask / frontend / __init__.py**](https://github.com/danielhomola/science_flask/blob/master/./frontend/__init__.py)

```python
# __init__.py
import os
~~from flask import Flask, url_for, redirect, request, abort
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore, signals, \
                           current_user
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers
from flask_wtf.csrf import CSRFProtect
from celery import Celery


appdir = os.path.abspath(os.path.dirname(__file__))
ROOTDIR = os.path.abspath(os.path.join(appdir, os.pardir))
user_data_folder = os.path.join(ROOTDIR, 'userData')

~~app = Flask(__name__, instance_path=user_data_folder)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

mail = Mail(app)

csrf = CSRFProtect(app)

def create_celery_app():
    celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    celery.app = app
    return celery


## ... source file continues with no further Flask examples...

```


## Example 20 from tedivms-flask
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

~~from flask import Flask, session, render_template
from flask_mail import Mail
from flask_migrate import Migrate, MigrateCommand
from flask.sessions import SessionInterface
from flask_sqlalchemy import SQLAlchemy
from flask_user import user_logged_out
from flask_wtf.csrf import CSRFProtect

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from beaker.middleware import SessionMiddleware

db = SQLAlchemy()
csrf_protect = CSRFProtect()
mail = Mail()
migrate = Migrate()


def get_config():
~~    app = Flask(__name__)

    app.config.from_object('app.settings')
    if 'APPLICATION_SETTINGS' in os.environ:
        app.config.from_envvar(os.environ['APPLICATION_SETTINGS'])
    if 'AWS_SECRETS_MANAGER_CONFIG' in os.environ:
        secret_config = get_secrets(os.environ['AWS_SECRETS_MANAGER_CONFIG'])
        app.config.update(secret_config)
    elif 'AWS_SECRETS_MANAGER_CONFIG' in app.config:
        secret_config = get_secrets(app.config['AWS_SECRETS_MANAGER_CONFIG'])
        app.config.update(secret_config)
    for setting in app.config:
        if setting in os.environ:
            if os.environ[setting].lower() == 'true':
                app.config[setting] = True
            elif os.environ[setting].lower() == 'false':
                app.config[setting] = False
            else:
                app.config[setting] = os.environ[setting]
    if app.config.get('USER_LDAP', False):
        app.config['USER_ENABLE_USERNAME'] = True
    return app.config


def get_secrets(secret_name, region=False):


## ... source file abbreviated to get to Flask examples ...



    return yaml.safe_load(secret)


def get_secret_region():
    if 'AWS_SECRETS_REGION' in os.environ:
        return os.environ['AWS_SECRETS_REGION']

    boto3_session = boto3.session.Session()
    if boto3_session.region_name:
        return boto3_session.region_name

    r = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document', timeout=0.2)
    r.raise_for_status()
    data = r.json()
    return data['region']


base_config = get_config()

celery = Celery(__name__, broker=base_config['CELERY_BROKER'])
cache = None # Initiate below, but define here for scope reasons.


def create_app(extra_config_settings={}):
~~    app = Flask(__name__)

    base_config = get_config()
    app.config.update(base_config)
    app.config.update(extra_config_settings)


    db.init_app(app)

    migrate.init_app(app, db)

    mail.init_app(app)

    csrf_protect.init_app(app)

    cache = init_cache_manager(app)

    init_session_manager(app)

    init_celery_service(app)

    init_error_handlers(app)

    from app.extensions.jinja import jinja_extensions_blueprint
    app.register_blueprint(jinja_extensions_blueprint)


## ... source file continues with no further Flask examples...

```


## Example 21 from trape
[trape](https://github.com/jofpin/trape) is a research tool for tracking
people's activities that are logged digitally. The tool uses
[Flask](/flask.html) to create a web front end to view aggregated data
on an individual the application is set to track. The source code is
provided as open source under the MIT license, according to the
[README](https://github.com/jofpin/trape/blob/master/README.md).

[**trape / core / user.py**](https://github.com/jofpin/trape/blob/master/./core/user.py)

```python
# user.py
import time
from core.dependence import urllib2
~~from flask import Flask, render_template, session, request, json, Response
from core.user_objects import *
import core.stats
from core.utils import utils
from core.db import Database
import os
import sys
import platform
from multiprocessing import Process

trape = core.stats.trape
app = core.stats.app

db = Database()

class victim_server(object):
    @app.route("/" + trape.victim_path)
    def homeVictim():
        opener = urllib2.build_opener()
        headers = victim_headers(request.user_agent)
        opener.addheaders = headers
        if (trape.type_lure == 'local'):
            html = assignScripts(victim_inject_code(render_template("/" + trape.url_to_clone), 'payload', '/', trape.gmaps, trape.ipinfo))
        else:
            html = assignScripts(victim_inject_code(opener.open(trape.url_to_clone).read(), 'payload', trape.url_to_clone, trape.gmaps, trape.ipinfo))


## ... source file continues with no further Flask examples...

```

