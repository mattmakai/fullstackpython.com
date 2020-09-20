title: flask.globals g Example Code
category: page
slug: flask-globals-g-examples
sortorder: 500021015
toc: False
sidebartitle: flask.globals g
meta: Python example code that shows how to use the g callable from the flask.globals module of the Flask project.


[g](https://flask.palletsprojects.com/en/1.1.x/api/#flask.g) is
an object for storing data during the
[application context](https://flask.palletsprojects.com/en/1.1.x/appcontext/)
of a running [Flask](/flask.html) web app.

`g` can also be imported directly from the `flask` module instead
of `flask.globals`, so you will often see that shortcut in example code.

<a href="/flask-globals-current-app-examples.html">current_app</a>,
<a href="/flask-globals-request-examples.html">request</a>,
and <a href="/flask-globals-session-examples.html">session</a>
are several other callables with code examples from the same `flask.globals` package.

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

[**Flask AppBuilder / flask_appbuilder / security / manager.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/security/manager.py)

```python
# manager.py
import base64
import datetime
import json
import logging
import re
from typing import Dict, List, Set

~~from flask import g, session, url_for
from flask_babel import lazy_gettext as _
from flask_jwt_extended import current_user as current_user_jwt
from flask_jwt_extended import JWTManager
from flask_login import current_user, LoginManager
from flask_openid import OpenID
from werkzeug.security import check_password_hash, generate_password_hash

from .api import SecurityApi
from .registerviews import (
    RegisterUserDBView,
    RegisterUserOAuthView,
    RegisterUserOIDView,
)
from .views import (
    AuthDBView,
    AuthLDAPView,
    AuthOAuthView,
    AuthOIDView,
    AuthRemoteUserView,
    PermissionModelView,
    PermissionViewModelView,
    RegisterUserModelView,
    ResetMyPasswordView,
    ResetPasswordView,


## ... source file abbreviated to get to g examples ...


        return self.appbuilder.get_app.config["AUTH_LDAP_TLS_CACERTDIR"]

    @property
    def auth_ldap_tls_cacertfile(self):
        return self.appbuilder.get_app.config["AUTH_LDAP_TLS_CACERTFILE"]

    @property
    def auth_ldap_tls_certfile(self):
        return self.appbuilder.get_app.config["AUTH_LDAP_TLS_CERTFILE"]

    @property
    def auth_ldap_tls_keyfile(self):
        return self.appbuilder.get_app.config["AUTH_LDAP_TLS_KEYFILE"]

    @property
    def openid_providers(self):
        return self.appbuilder.get_app.config["OPENID_PROVIDERS"]

    @property
    def oauth_providers(self):
        return self.appbuilder.get_app.config["OAUTH_PROVIDERS"]

    @property
    def current_user(self):
        if current_user.is_authenticated:
~~            return g.user
        elif current_user_jwt:
            return current_user_jwt

    def oauth_user_info_getter(self, f):

        def wraps(provider, response=None):
            ret = f(self, provider, response=response)
            if not type(ret) == dict:
                log.error(
                    "OAuth user info decorated function "
                    "did not returned a dict, but: {0}".format(type(ret))
                )
                return {}
            return ret

        self.oauth_user_info = wraps
        return wraps

    def get_oauth_token_key_name(self, provider):
        for _provider in self.oauth_providers:
            if _provider["name"] == provider:
                return _provider.get("token_key", "oauth_token")

    def get_oauth_token_secret_name(self, provider):


## ... source file abbreviated to get to g examples ...


                        role, permission_name, view_menu_name
                    ):
                        result.add(view_menu_name)
            else:
                db_role_ids.append(role.id)
        pvms_names = [
            pvm.view_menu.name
            for pvm in self.find_roles_permission_view_menus(
                permission_name, db_role_ids
            )
        ]
        result.update(pvms_names)
        return result

    def has_access(self, permission_name, view_name):
        if current_user.is_authenticated:
            return self._has_view_access(g.user, permission_name, view_name)
        elif current_user_jwt:
            return self._has_view_access(current_user_jwt, permission_name, view_name)
        else:
            return self.is_item_public(permission_name, view_name)

    def get_user_menu_access(self, menu_names: List[str] = None) -> Set[str]:
        if current_user.is_authenticated:
            return self._get_user_permission_view_menus(
~~                g.user, "menu_access", view_menus_name=menu_names
            )
        elif current_user_jwt:
            return self._get_user_permission_view_menus(
                current_user_jwt, "menu_access", view_menus_name=menu_names
            )
        else:
            return self._get_user_permission_view_menus(
                None, "menu_access", view_menus_name=menu_names
            )

    def add_permissions_view(self, base_permissions, view_menu):
        view_menu_db = self.add_view_menu(view_menu)
        perm_views = self.find_permissions_view_menu(view_menu_db)

        if not perm_views:
            for permission in base_permissions:
                pv = self.add_permission_view_menu(permission, view_menu)
                if self.auth_role_admin not in self.builtin_roles:
                    role_admin = self.find_role(self.auth_role_admin)
                    self.add_permission_role(role_admin, pv)
        else:
            role_admin = self.find_role(self.auth_role_admin)
            for permission in base_permissions:
                if not self.exist_permission_on_views(perm_views, permission):


## ... source file abbreviated to get to g examples ...


        raise NotImplementedError

    def add_permission_view_menu(self, permission_name, view_menu_name):
        raise NotImplementedError

    def del_permission_view_menu(self, permission_name, view_menu_name, cascade=True):
        raise NotImplementedError

    def exist_permission_on_views(self, lst, item):
        raise NotImplementedError

    def exist_permission_on_view(self, lst, permission, view_menu):
        raise NotImplementedError

    def add_permission_role(self, role, perm_view):
        raise NotImplementedError

    def del_permission_role(self, role, perm_view):
        raise NotImplementedError

    def load_user(self, pk):
        return self.get_user_by_id(int(pk))

    def load_user_jwt(self, pk):
        user = self.load_user(pk)
~~        g.user = user
        return user

    @staticmethod
    def before_request():
~~        g.user = current_user



## ... source file continues with no further g examples...

```


## Example 2 from flask-bones
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
    app = Flask(__name__)
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
~~        g.request_start_time = time.time()
~~        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
~~        g.pjax = 'X-PJAX' in request.headers

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    return app


def register_commands(app):
    for command in [create_db, drop_db, populate_db, recreate_db]:
        app.cli.command()(command)


def register_extensions(app):
    travis.init_app(app)
    db.init_app(app)
    lm.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    assets.init_app(app)
    babel.init_app(app)
    rq.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)


## ... source file continues with no further g examples...

```


## Example 3 from flask-bookshelf
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

app = Flask(
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
~~    if "lang_code" in values or not g.get("lang_code", None):
        return
    if app.url_map.is_endpoint_expecting(endpoint, "lang_code"):
~~        values["lang_code"] = g.lang_code


@app.url_value_preprocessor
def get_lang_code(endpoint, values):
    if values is not None:
~~        g.lang_code = values.pop("lang_code", None)


@app.before_request
def ensure_lang_support():
~~    lang_code = g.get("lang_code", None)
    if lang_code and lang_code not in app.config["SUPPORTED_LANGUAGES"].keys():
        abort(404)


@babel.localeselector
def get_locale():
~~    return g.get("lang_code", app.config["BABEL_DEFAULT_LOCALE"])


@babel.timezoneselector
def get_timezone():
~~    user = g.get("user", None)
    if user is not None:
        return user.timezone
    return "UTC"


@app.errorhandler(404)
def page_not_found(error):
    current_app.logger.error("Page not found: %s", (request.path, error))
    return render_template("404.htm"), 404


@app.errorhandler(500)
def internal_server_error(error):
    current_app.logger.error("Server Error: %s", (error))
    return render_template("500.htm"), 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    current_app.logger.error("Unhandled Exception: %s", (error))
    return render_template("500.htm"), 500


@app.context_processor
def inject_data():
~~    return dict(user=current_user, lang_code=g.get("lang_code", None))


@app.route("/")
@app.route("/<lang_code>/")
@cache.cached(300)
def home(lang_code=None):
    return render_template("index.htm")


app.register_blueprint(main, url_prefix="/main")
app.register_blueprint(main, url_prefix="/<lang_code>/main")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(admin, url_prefix="/<lang_code>/admin")



## ... source file continues with no further g examples...

```


## Example 4 from flask-debugtoolbar
[Flask Debug-toolbar](https://github.com/flask-debugtoolbar/flask-debugtoolbar)
([documentation](https://flask-debugtoolbar.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/Flask-DebugToolbar/))
is a [Flask](/flask.html) conversion of the popular
[Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
project. This extension creates a sidebar with useful debugging
information when you are running a Flask application in development
mode. The project is provided as open source under
[this license](https://github.com/flask-debugtoolbar/flask-debugtoolbar/blob/master/LICENSE).

[**flask-debugtoolbar / flask_debugtoolbar / __init__.py**](https://github.com/flask-debugtoolbar/flask-debugtoolbar/blob/master/flask_debugtoolbar/./__init__.py)

```python
# __init__.py
import os
import warnings

~~from flask import Blueprint, current_app, request, g, send_from_directory, url_for
from flask.globals import _request_ctx_stack
from jinja2 import Environment, PackageLoader
from werkzeug.urls import url_quote_plus

from flask_debugtoolbar.compat import iteritems
from flask_debugtoolbar.toolbar import DebugToolbar
from flask_debugtoolbar.utils import decode_text, gzip_compress, gzip_decompress

try:
    from importlib.metadata import version

    __version__ = version("Flask-DebugToolbar")
except ImportError:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("Flask-DebugToolbar").version


module = Blueprint('debugtoolbar', __name__)


def replace_insensitive(string, target, replacement):
    no_case = string.lower()
    index = no_case.rfind(target.lower())


## ... source file abbreviated to get to g examples ...


        rule = req.url_rule

        if getattr(rule, 'provide_automatic_options', False) \
           and req.method == 'OPTIONS':
            return app.make_default_options_response()

        view_func = app.view_functions[rule.endpoint]
        view_func = self.process_view(app, view_func, req.view_args)

        return view_func(**req.view_args)

    def _show_toolbar(self):
        if request.blueprint == 'debugtoolbar':
            return False

        hosts = current_app.config['DEBUG_TB_HOSTS']
        if hosts and request.remote_addr not in hosts:
            return False

        return True

    def send_static_file(self, filename):
        return send_from_directory(self._static_dir, filename)

    def process_request(self):
~~        g.debug_toolbar = self

        if not self._show_toolbar():
            return

        real_request = request._get_current_object()

        self.debug_toolbars[real_request] = (
            DebugToolbar(real_request, self.jinja_env))

        for panel in self.debug_toolbars[real_request].panels:
            panel.process_request(real_request)

    def process_view(self, app, view_func, view_kwargs):
        real_request = request._get_current_object()
        try:
            toolbar = self.debug_toolbars[real_request]
        except KeyError:
            return view_func

        for panel in toolbar.panels:
            new_view = panel.process_view(real_request, view_func, view_kwargs)
            if new_view:
                view_func = new_view



## ... source file continues with no further g examples...

```


## Example 5 from Flask-HTTPAuth
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

[**Flask-HTTPAuth / flask_httpauth.py**](https://github.com/miguelgrinberg/Flask-HTTPAuth/blob/master/././flask_httpauth.py)

```python
# flask_httpauth.py

from base64 import b64decode
from functools import wraps
from hashlib import md5
from random import Random, SystemRandom
~~from flask import request, make_response, session, g
from werkzeug.datastructures import Authorization
from werkzeug.security import safe_str_cmp

__version__ = '4.1.1dev'


class HTTPAuth(object):
    def __init__(self, scheme=None, realm=None, header=None):
        self.scheme = scheme
        self.realm = realm or "Authentication Required"
        self.header = header
        self.get_password_callback = None
        self.get_user_roles_callback = None
        self.auth_error_callback = None

        def default_get_password(username):
            return None

        def default_auth_error(status):
            return "Unauthorized Access", status

        self.get_password(default_get_password)
        self.error_handler(default_auth_error)



## ... source file abbreviated to get to g examples ...


                (role is not None or optional is not None):  # pragma: no cover
            raise ValueError(
                'role and optional are the only supported arguments')

        def login_required_internal(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                auth = self.get_auth()

                if request.method != 'OPTIONS':  # pragma: no cover
                    password = self.get_auth_password(auth)

                    status = None
                    user = self.authenticate(auth, password)
                    if user in (False, None):
                        status = 401
                    elif not self.authorize(role, user, auth):
                        status = 403
                    if not optional and status:
                        request.data
                        try:
                            return self.auth_error_callback(status)
                        except TypeError:
                            return self.auth_error_callback()

~~                    g.flask_httpauth_user = user if user is not True \
                        else auth.username if auth else None
                return f(*args, **kwargs)
            return decorated

        if f:
            return login_required_internal(f)
        return login_required_internal

    def username(self):
        if not request.authorization:
            return ""
        return request.authorization.username

    def current_user(self):
        if hasattr(g, 'flask_httpauth_user'):
~~            return g.flask_httpauth_user


class HTTPBasicAuth(HTTPAuth):
    def __init__(self, scheme=None, realm=None):
        super(HTTPBasicAuth, self).__init__(scheme or 'Basic', realm)

        self.hash_password_callback = None
        self.verify_password_callback = None

    def hash_password(self, f):
        self.hash_password_callback = f
        return f

    def verify_password(self, f):
        self.verify_password_callback = f
        return f

    def get_auth(self):
        header = self.header or 'Authorization'
        if header not in request.headers:
            return None
        value = request.headers[header].encode('utf-8')
        try:
            scheme, credentials = value.split(b' ', 1)


## ... source file abbreviated to get to g examples ...


            def decorated(*args, **kwargs):
                selected_auth = None
                if 'Authorization' in request.headers:
                    try:
                        scheme, creds = request.headers[
                            'Authorization'].split(None, 1)
                    except ValueError:
                        pass
                    else:
                        for auth in self.additional_auth:
                            if auth.scheme == scheme:
                                selected_auth = auth
                                break
                if selected_auth is None:
                    selected_auth = self.main_auth
                return selected_auth.login_required(role=role)(f)(
                    *args, **kwargs)
            return decorated

        if f:
            return login_required_internal(f)
        return login_required_internal

    def current_user(self):
        if hasattr(g, 'flask_httpauth_user'):  # pragma: no cover
~~            return g.flask_httpauth_user



## ... source file continues with no further g examples...

```


## Example 6 from Flask-WTF
[Flask-WTF](https://github.com/lepture/flask-wtf)
([project documentation](https://flask-wtf.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/Flask-WTF/))
provides a bridge between [Flask](/flask.html) and the the
[WTForms](https://wtforms.readthedocs.io/en/2.3.x/) form-handling library.
It makes it easier to use WTForms by reducing boilerplate code and
shorter examples for common form operations as well as common security
practices such as [CSRF](/cross-site-request-forgery-csrf.html).

[**Flask-WTF / flask_wtf / csrf.py**](https://github.com/lepture/flask-wtf/blob/master/flask_wtf/./csrf.py)

```python
# csrf.py
import hashlib
import logging
import os
import warnings
from urllib.parse import urlparse
from functools import wraps

~~from flask import Blueprint, current_app, g, request, session
from itsdangerous import BadData, SignatureExpired, URLSafeTimedSerializer
from werkzeug.exceptions import BadRequest
from werkzeug.security import safe_str_cmp
from wtforms import ValidationError
from wtforms.csrf.core import CSRF

from ._compat import FlaskWTFDeprecationWarning

__all__ = ('generate_csrf', 'validate_csrf', 'CSRFProtect')
logger = logging.getLogger(__name__)


def generate_csrf(secret_key=None, token_key=None):

    secret_key = _get_config(
        secret_key, 'WTF_CSRF_SECRET_KEY', current_app.secret_key,
        message='A secret key is required to use CSRF.'
    )
    field_name = _get_config(
        token_key, 'WTF_CSRF_FIELD_NAME', 'csrf_token',
        message='A field name is required to use CSRF.'
    )

~~    if field_name not in g:
        s = URLSafeTimedSerializer(secret_key, salt='wtf-csrf-token')

        if field_name not in session:
            session[field_name] = hashlib.sha1(os.urandom(64)).hexdigest()

        try:
            token = s.dumps(session[field_name])
        except TypeError:
            session[field_name] = hashlib.sha1(os.urandom(64)).hexdigest()
            token = s.dumps(session[field_name])

        setattr(g, field_name, token)

~~    return g.get(field_name)


def validate_csrf(data, secret_key=None, time_limit=None, token_key=None):

    secret_key = _get_config(
        secret_key, 'WTF_CSRF_SECRET_KEY', current_app.secret_key,
        message='A secret key is required to use CSRF.'
    )
    field_name = _get_config(
        token_key, 'WTF_CSRF_FIELD_NAME', 'csrf_token',
        message='A field name is required to use CSRF.'
    )
    time_limit = _get_config(
        time_limit, 'WTF_CSRF_TIME_LIMIT', 3600, required=False
    )

    if not data:
        raise ValidationError('The CSRF token is missing.')

    if field_name not in session:
        raise ValidationError('The CSRF session token is missing.')

    s = URLSafeTimedSerializer(secret_key, salt='wtf-csrf-token')



## ... source file abbreviated to get to g examples ...


    value, config_name, default=None,
    required=True, message='CSRF is not configured.'
):

    if value is None:
        value = current_app.config.get(config_name, default)

    if required and value is None:
        raise RuntimeError(message)

    return value


class _FlaskFormCSRF(CSRF):
    def setup_form(self, form):
        self.meta = form.meta
        return super().setup_form(form)

    def generate_csrf_token(self, csrf_token_field):
        return generate_csrf(
            secret_key=self.meta.csrf_secret,
            token_key=self.meta.csrf_field_name
        )

    def validate_csrf_token(self, form, field):
~~        if g.get('csrf_valid', False):
            return

        try:
            validate_csrf(
                field.data,
                self.meta.csrf_secret,
                self.meta.csrf_time_limit,
                self.meta.csrf_field_name
            )
        except ValidationError as e:
            logger.info(e.args[0])
            raise


class CSRFProtect:

    def __init__(self, app=None):
        self._exempt_views = set()
        self._exempt_blueprints = set()

        if app:
            self.init_app(app)

    def init_app(self, app):


## ... source file abbreviated to get to g examples ...



            if csrf_token:
                return csrf_token

        return None

    def protect(self):
        if request.method not in current_app.config['WTF_CSRF_METHODS']:
            return

        try:
            validate_csrf(self._get_csrf_token())
        except ValidationError as e:
            logger.info(e.args[0])
            self._error_response(e.args[0])

        if request.is_secure and current_app.config['WTF_CSRF_SSL_STRICT']:
            if not request.referrer:
                self._error_response('The referrer header is missing.')

            good_referrer = f'https://{request.host}/'

            if not same_origin(request.referrer, good_referrer):
                self._error_response('The referrer does not match the host.')

~~        g.csrf_valid = True  # mark this request as CSRF valid

    def exempt(self, view):

        if isinstance(view, Blueprint):
            self._exempt_blueprints.add(view.name)
            return view

        if isinstance(view, str):
            view_location = view
        else:
            view_location = '.'.join((view.__module__, view.__name__))

        self._exempt_views.add(view_location)
        return view

    def _error_response(self, reason):
        raise CSRFError(reason)

    def error_handler(self, view):

        warnings.warn(FlaskWTFDeprecationWarning(
            '"@csrf.error_handler" is deprecated. Use the standard Flask '
            'error system with "@app.errorhandler(CSRFError)" instead. This '
            'will be removed in 1.0.'


## ... source file continues with no further g examples...

```


## Example 7 from Flask-Security-Too
[Flask-Security-Too](https://github.com/Flask-Middleware/flask-security/)
([PyPi page](https://pypi.org/project/Flask-Security-Too/) and
[project documentation](https://flask-security-too.readthedocs.io/en/stable/))
is a maintained fork of the original
[Flask-Security](https://github.com/mattupstate/flask-security) project that
makes it easier to add common security features to [Flask](/flask.html)
web applications. A few of the critical goals of the Flask-Security-Too
project are ensuring JavaScript client-based single-page applications (SPAs)
can work securely with Flask-based backends and that guidance by the
[OWASP](https://owasp.org/) organization is followed by default.

The Flask-Security-Too project is provided as open source under the
[MIT license](https://github.com/Flask-Middleware/flask-security/blob/master/LICENSE).

[**Flask-Security-Too / flask_security / utils.py**](https://github.com/Flask-Middleware/flask-security/blob/master/flask_security/./utils.py)

```python
# utils.py
import abc
import base64
import datetime
from functools import partial
import hashlib
import hmac
import time
from typing import Dict, List
import warnings
from datetime import timedelta
from urllib.parse import parse_qsl, parse_qs, urlsplit, urlunsplit, urlencode
import urllib.request
import urllib.error

~~from flask import _request_ctx_stack, current_app, flash, g, request, session, url_for
from flask.json import JSONEncoder
from flask_login import login_user as _login_user
from flask_login import logout_user as _logout_user
from flask_login import current_user
from flask_login import COOKIE_NAME as REMEMBER_COOKIE_NAME
from flask_principal import AnonymousIdentity, Identity, identity_changed, Need
from flask_wtf import csrf
from wtforms import validators, ValidationError
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.local import LocalProxy
from werkzeug.datastructures import MultiDict

from .quart_compat import best
from .signals import user_authenticated

_security = LocalProxy(lambda: current_app.extensions["security"])

_datastore = LocalProxy(lambda: _security.datastore)

_pwd_context = LocalProxy(lambda: _security.pwd_context)

_hashing_context = LocalProxy(lambda: _security.hashing_context)

localize_callback = LocalProxy(lambda: _security.i18n_domain.gettext)


## ... source file abbreviated to get to g examples ...


        user.login_count = user.login_count + 1 if user.login_count else 1

        _datastore.put(user)

    session["fs_cc"] = "set"  # CSRF cookie
    session["fs_paa"] = time.time()  # Primary authentication at - timestamp

    identity_changed.send(
        current_app._get_current_object(), identity=Identity(user.fs_uniquifier)
    )

    user_authenticated.send(
        current_app._get_current_object(), user=user, authn_via=authn_via
    )
    return True


def logout_user():

    for key in ("identity.name", "identity.auth_type", "fs_paa", "fs_gexp"):
        session.pop(key, None)

    csrf_field_name = find_csrf_field_name()
    if csrf_field_name:
        session.pop(csrf_field_name, None)
~~        g.pop(csrf_field_name, None)
    session["fs_cc"] = "clear"
    identity_changed.send(
        current_app._get_current_object(), identity=AnonymousIdentity()
    )
    _logout_user()


def check_and_update_authn_fresh(within, grace, method=None):

    if method == "basic":
        return True

    if within.total_seconds() < 0:
        return True

    if "fs_paa" not in session:
        return False

    now = datetime.datetime.utcnow()
    new_exp = now + grace
    grace_ts = int(new_exp.timestamp())

    fs_gexp = session.get("fs_gexp", None)
    if fs_gexp:


## ... source file continues with no further g examples...

```


## Example 8 from Flask-User
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

[**Flask-User / flask_user / decorators.py**](https://github.com/lingthio/Flask-User/blob/master/flask_user/./decorators.py)

```python
# decorators.py


from functools import wraps
~~from flask import current_app, g
from flask_login import current_user

def _is_logged_in_with_confirmed_email(user_manager):
    if user_manager.call_or_get(current_user.is_authenticated):
        unconfirmed_email_allowed = \
            getattr(g, '_flask_user_allow_unconfirmed_email', False)
        
        if unconfirmed_email_allowed or user_manager.db_manager.user_has_confirmed_email(current_user):
            return True

    return False


def login_required(view_function):
    @wraps(view_function)    # Tells debuggers that is is a function wrapper
    def decorator(*args, **kwargs):
        user_manager = current_app.user_manager
        
        allowed = _is_logged_in_with_confirmed_email(user_manager)
        if not allowed:
            return user_manager.unauthenticated_view()

        return view_function(*args, **kwargs)



## ... source file abbreviated to get to g examples ...


def roles_required(*role_names):
    def wrapper(view_function):

        @wraps(view_function)    # Tells debuggers that is is a function wrapper
        def decorator(*args, **kwargs):
            user_manager = current_app.user_manager

            allowed = _is_logged_in_with_confirmed_email(user_manager)
            if not allowed:
                return user_manager.unauthenticated_view()

            if not current_user.has_roles(*role_names):
                return user_manager.unauthorized_view()

            return view_function(*args, **kwargs)

        return decorator

    return wrapper



def allow_unconfirmed_email(view_function):
    @wraps(view_function)    # Tells debuggers that is is a function wrapper
    def decorator(*args, **kwargs):
~~        g._flask_user_allow_unconfirmed_email = True

        try:
            user_manager = current_app.user_manager

            allowed = _is_logged_in_with_confirmed_email(user_manager)
            if not allowed:
                return user_manager.unauthenticated_view()

            return view_function(*args, **kwargs)

        finally:
~~            g._flask_user_allow_unconfirmed_email = False

    return decorator



## ... source file continues with no further g examples...

```


## Example 9 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / config.py**](https://github.com/indico/indico/blob/master/indico/core/config.py)

```python
# config.py

from __future__ import absolute_import, unicode_literals

import ast
import codecs
import os
import re
import socket
import warnings
from datetime import timedelta

import pytz
from celery.schedules import crontab
~~from flask import current_app, g
from flask.helpers import get_root_path
from werkzeug.datastructures import ImmutableDict
from werkzeug.urls import url_parse

from indico.util.caching import make_hashable
from indico.util.fs import resolve_link
from indico.util.packaging import package_is_editable
from indico.util.string import crc32, snakify


DEFAULTS = {
    'ATTACHMENT_STORAGE': 'default',
    'AUTH_PROVIDERS': {},
    'BASE_URL': None,
    'CACHE_BACKEND': 'files',
    'CACHE_DIR': '/opt/indico/cache',
    'CATEGORY_CLEANUP': {},
    'CELERY_BROKER': None,
    'CELERY_CONFIG': {},
    'CELERY_RESULT_BACKEND': None,
    'COMMUNITY_HUB_URL': 'https://hub.getindico.io',
    'CUSTOMIZATION_DEBUG': False,
    'CUSTOMIZATION_DIR': None,
    'CUSTOM_COUNTRIES': {},


## ... source file abbreviated to get to g examples ...


class IndicoConfig(object):

    __slots__ = ('_config', '_exc')

    def __init__(self, config=None, exc=AttributeError):
        object.__setattr__(self, '_config', config)
        object.__setattr__(self, '_exc', exc)

    @property
    def data(self):
        try:
            return self._config or current_app.config['INDICO']
        except KeyError:
            raise RuntimeError('config not loaded')

    @property
    def hash(self):
        return crc32(repr(make_hashable(sorted(self.data.items()))))

    @property
    def CONFERENCE_CSS_TEMPLATES_BASE_URL(self):
        return self.BASE_URL + '/css/confTemplates'

    @property
    def IMAGES_BASE_URL(self):
~~        return 'static/images' if g.get('static_site') else url_parse('{}/images'.format(self.BASE_URL)).path

    @property
    def LATEX_ENABLED(self):
        return bool(self.XELATEX_PATH)

    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise self._exc('no such setting: ' + name)

    def __setattr__(self, key, value):
        raise AttributeError('cannot change config at runtime')

    def __delattr__(self, key):
        raise AttributeError('cannot change config at runtime')


config = IndicoConfig()



## ... source file continues with no further g examples...

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

[**tedivms-flask / app / extensions / ldap.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/extensions/ldap.py)

```python
# ldap.py

~~from flask import current_app, g
from flask_login import current_user
from flask_user import UserManager
from flask_user.forms import LoginForm
from flask_user.translation_utils import lazy_gettext as _    # map _() to lazy_gettext()

import datetime
from ldap3 import Server, Connection, ALL
from app import db
from app.models import user_models


def authenticate(user, password):
    s = Server(current_app.config['LDAP_HOST'], get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

    user_dn = get_dn_from_user(user)
    c = Connection(current_app.config['LDAP_HOST'], user=user_dn, password=password)

    if not c.bind():
        print('Unable to bind user %s' % (user_dn))
        return False

    return True




## ... source file abbreviated to get to g examples ...


    email_attribute = current_app.config.get('LDAP_EMAIL_ATTRIBUTE', False)
    if not email_attribute:
        return False
    conn = get_bound_connection()
    user_search = get_dn_from_user(user)
    user_object = '(objectclass=%s)' % (current_app.config['LDAP_USER_OBJECT_CLASS'],)
    conn.search(user_search, user_object, attributes=[email_attribute])
    if len(conn.entries) < 1:
        return False
    return getattr(conn.entries[0], email_attribute, False)[0]


def user_in_group(user, group):
    conn = get_bound_connection()
    group_search = get_dn_from_group(group)
    group_object = '(objectclass=%s)' % (current_app.config['LDAP_GROUP_OBJECT_CLASS'],)
    conn.search(group_search, group_object, attributes=['memberUid'])
    if len(conn.entries) < 1:
        return False
    members = conn.entries[0].memberUid
    return user in members


def get_bound_connection():
~~    if 'ldap_connection' in g:
~~        return g.ldap_connection
    server = Server(current_app.config['LDAP_HOST'], get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema
~~    g.ldap_connection = Connection(server, current_app.config['LDAP_BIND_DN'], current_app.config['LDAP_BIND_PASSWORD'], auto_bind=True)
~~    return g.ldap_connection


def get_dn_from_user(user):
    return "%s=%s,%s" % (current_app.config['LDAP_USERNAME_ATTRIBUTE'], user, current_app.config['LDAP_USER_BASE'] )


def get_dn_from_group(group):
    return '%s=%s,%s' % (current_app.config['LDAP_GROUP_ATTRIBUTE'], group, current_app.config['LDAP_GROUP_BASE'])


class TedivmLoginForm(LoginForm):

    def validate_user(self):
        user_manager =  current_app.user_manager
        if current_app.config.get('USER_LDAP', False):
            if not authenticate(self.username.data, self.password.data):
                return False
            user = user_manager.db_manager.find_user_by_username(self.username.data)
            if not user:
                email = get_user_email(self.username.data)
                if not email:
                    email = None

                user = user_models.User(username=self.username.data,
def get_user_email(user):


## ... source file continues with no further g examples...

```

