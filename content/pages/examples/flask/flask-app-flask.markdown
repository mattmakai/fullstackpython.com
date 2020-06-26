title: flask.app Flask code examples
category: page
slug: flask-app-flask-examples
sortorder: 500021001
toc: False
sidebartitle: flask.app Flask
meta: Python example code for the Flask class from the flask.app module of the Flask project.


Flask is a class within the flask.app module of the Flask project.


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


## Example 2 from FlaskBB
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


## Example 3 from flask-base
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


## Example 4 from flask-bookshelf
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


## Example 5 from flaskex
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


## Example 6 from flask-phone-input
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


## Example 7 from flaskSaaS
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


## Example 8 from Flasky
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


## Example 9 from sandman2
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


## Example 10 from tedivms-flask
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

