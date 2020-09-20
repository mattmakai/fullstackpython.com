title: flask.blueprints Blueprint Example Code
category: page
slug: flask-blueprints-blueprint-examples
sortorder: 500021004
toc: False
sidebartitle: flask.blueprints Blueprint
meta: Example code for understanding how to use the Blueprint class from the flask.blueprints module of the Flask project.


A Blueprint in [Flask](/flask.html) is
[a "mold" or template for creating parts of web applications](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly).
This
[Blueprint](https://github.com/pallets/flask/blob/master/src/flask/blueprints.py)
class within the `flask.blueprints` module implements that functionality
for Flask [web apps](/web-development.html).



## Example 1 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [Flask](/flask.html). The application can be used
as-is to run CTF events, or modified for custom rules for related
scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / CTFd / auth.py**](https://github.com/CTFd/CTFd/blob/master/./CTFd/auth.py)

```python
# auth.py
import base64

import requests
~~from flask import Blueprint
from flask import current_app as app
from flask import redirect, render_template, request, session, url_for
from itsdangerous.exc import BadSignature, BadTimeSignature, SignatureExpired

from CTFd.cache import clear_team_session, clear_user_session
from CTFd.models import Teams, UserFieldEntries, UserFields, Users, db
from CTFd.utils import config, email, get_app_config, get_config
from CTFd.utils import user as current_user
from CTFd.utils import validators
from CTFd.utils.config import is_teams_mode
from CTFd.utils.config.integrations import mlc_registration
from CTFd.utils.config.visibility import registration_visible
from CTFd.utils.crypto import verify_password
from CTFd.utils.decorators import ratelimit
from CTFd.utils.decorators.visibility import check_registration_visibility
from CTFd.utils.helpers import error_for, get_errors, markup
from CTFd.utils.logging import log
from CTFd.utils.modes import TEAMS_MODE
from CTFd.utils.security.auth import login_user, logout_user
from CTFd.utils.security.signing import unserialize
from CTFd.utils.validators import ValidationError

~~auth = Blueprint("auth", __name__)


@auth.route("/confirm", methods=["POST", "GET"])
@auth.route("/confirm/<data>", methods=["POST", "GET"])
@ratelimit(method="POST", limit=10, interval=60)
def confirm(data=None):
    if not get_config("verify_emails"):
        return redirect(url_for("challenges.listing"))

    if data and request.method == "GET":
        try:
            user_email = unserialize(data, max_age=1800)
        except (BadTimeSignature, SignatureExpired):
            return render_template(
                "confirm.html", errors=["Your confirmation link has expired"]
            )
        except (BadSignature, TypeError, base64.binascii.Error):
            return render_template(
                "confirm.html", errors=["Your confirmation token is invalid"]
            )

        user = Users.query.filter_by(email=user_email).first_or_404()
        if user.verified:
            return redirect(url_for("views.settings"))


## ... source file continues with no further Blueprint examples...

```


## Example 2 from Flask AppBuilder
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

[**Flask AppBuilder / flask_appbuilder / base.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/./base.py)

```python
# base.py
from functools import reduce
import logging
from typing import Dict

~~from flask import Blueprint, current_app, url_for

from . import __version__
from .api.manager import OpenApiManager
from .babel.manager import BabelManager
from .const import (
    LOGMSG_ERR_FAB_ADD_PERMISSION_MENU,
    LOGMSG_ERR_FAB_ADD_PERMISSION_VIEW,
    LOGMSG_ERR_FAB_ADDON_IMPORT,
    LOGMSG_ERR_FAB_ADDON_PROCESS,
    LOGMSG_INF_FAB_ADD_VIEW,
    LOGMSG_INF_FAB_ADDON_ADDED,
    LOGMSG_WAR_FAB_VIEW_EXISTS,
)
from .filters import TemplateFilters
from .menu import Menu, MenuApiManager
from .views import IndexView, UtilView

log = logging.getLogger(__name__)


def dynamic_class_import(class_path):
    try:
        tmp = class_path.split(".")
        module_path = ".".join(tmp[0:-1])


## ... source file abbreviated to get to Blueprint examples ...



    @property
    def app_name(self):
        return self.get_app.config["APP_NAME"]

    @property
    def app_theme(self):
        return self.get_app.config["APP_THEME"]

    @property
    def app_icon(self):
        return self.get_app.config["APP_ICON"]

    @property
    def languages(self):
        return self.get_app.config["LANGUAGES"]

    @property
    def version(self):
        return __version__

    def _add_global_filters(self):
        self.template_filters = TemplateFilters(self.get_app, self.sm)

    def _add_global_static(self):
~~        bp = Blueprint(
            "appbuilder",
            __name__,
            url_prefix="/static",
            template_folder="templates",
            static_folder=self.static_folder,
            static_url_path=self.static_url_path,
        )
        self.get_app.register_blueprint(bp)

    def _add_admin_views(self):
        self.indexview = self._check_and_init(self.indexview)
        self.add_view_no_menu(self.indexview)
        self.add_view_no_menu(UtilView())
        self.bm.register_views()
        self.sm.register_views()
        self.openapi_manager.register_views()
        self.menuapi_manager.register_views()

    def _add_addon_views(self):
        for addon in self._addon_managers:
            addon_class = dynamic_class_import(addon)
            if addon_class:
                addon_class = addon_class(self)
                try:


## ... source file continues with no further Blueprint examples...

```


## Example 3 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / auth / views.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/auth/views.py)

```python
# views.py
import logging
from datetime import datetime

~~from flask import Blueprint, current_app, flash, g, redirect, request, url_for
from flask.views import MethodView
from flask_babelplus import gettext as _
from flask_login import (
    confirm_login,
    current_user,
    login_fresh,
    login_required,
    login_user,
    logout_user,
)

from flaskbb.auth.forms import (
    AccountActivationForm,
    ForgotPasswordForm,
    LoginForm,
    LoginRecaptchaForm,
    ReauthForm,
    RegisterForm,
    RequestActivationForm,
    ResetPasswordForm,
)
from flaskbb.extensions import db, limiter
from flaskbb.utils.helpers import (
    anonymous_required,


## ... source file abbreviated to get to Blueprint examples ...


            else:
                try:
                    db.session.commit()
                except Exception:  # noqa
                    logger.exception("Database error while activating account")
                    db.session.rollback()
                    flash(
                        _(
                            "Could not activate account due to an unrecoverable error"  # noqa
                        ), "danger"
                    )

                    return redirect(url_for('auth.request_activation_token'))

                flash(
                    _("Your account has been activated and you can now login."),
                    "success"
                )
                return redirect(url_for("forum.index"))

        return render_template("auth/account_activation.html", form=form)


@impl(tryfirst=True)
def flaskbb_load_blueprints(app):
~~    auth = Blueprint("auth", __name__)

    def login_rate_limit():
        return "{count}/{timeout}minutes".format(
            count=flaskbb_config["AUTH_REQUESTS"],
            timeout=flaskbb_config["AUTH_TIMEOUT"]
        )

    def login_rate_limit_message():
        current_limit = getattr(g, 'view_rate_limit', None)
        if current_limit is not None:
            window_stats = limiter.limiter.get_window_stats(*current_limit)
            reset_time = datetime.utcfromtimestamp(window_stats[0])
            timeout = reset_time - datetime.utcnow()
        return "{timeout}".format(timeout=format_timedelta(timeout))

    @auth.before_request
    def check_rate_limiting():
        if not flaskbb_config["AUTH_RATELIMIT_ENABLED"]:
            return None
        return limiter.check()

    @auth.errorhandler(429)
    def login_rate_limit_error(error):
        return render_template(


## ... source file continues with no further Blueprint examples...

```


## Example 4 from flask-base
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

[**flask-base / app / main / views.py**](https://github.com/hack4impact/flask-base/blob/master/app/main/views.py)

```python
# views.py
~~from flask import Blueprint, render_template

from app.models import EditableHTML

~~main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)



## ... source file continues with no further Blueprint examples...

```


## Example 5 from flask-bones
[flask-bones](https://github.com/cburmeister/flask-bones)
([demo](http://flask-bones.herokuapp.com/))
is large scale [Flask](/flask.html) example application built
with [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
([example Blueprint code](/flask-blueprints-blueprint-examples.html)).
This project is provided as open source under the
[MIT license](https://github.com/cburmeister/flask-bones/blob/master/LICENSE).

[**flask-bones / app / auth / __init__.py**](https://github.com/cburmeister/flask-bones/blob/master/app/auth/__init__.py)

```python
# __init__.py
~~from flask import Blueprint

~~auth = Blueprint('auth', __name__, template_folder='templates')

from . import views



## ... source file continues with no further Blueprint examples...

```


## Example 6 from flask-bookshelf
[flask-bookshelf](https://github.com/damyanbogoev/flask-bookshelf) is the
example [Flask](/flask.html) application that developers create when
going through
[this Flask series of blog posts](https://damyanon.net/tags/flask-series/).

[**flask-bookshelf / bookshelf / admin / controllers.py**](https://github.com/damyanbogoev/flask-bookshelf/blob/master/bookshelf/admin/controllers.py)

```python
# controllers.py
from sqlalchemy import exc
~~from flask import Blueprint, render_template, flash
from flask import current_app, redirect, request, url_for
from flask_security.decorators import roles_required
from bookshelf.admin.forms.author_forms import CreateAuthorForm
from bookshelf.cache import cache
from bookshelf.data.models import Author, db


~~admin = Blueprint("admin", __name__, template_folder="templates")


@admin.route("/")
@roles_required("admin")
def index():
    return render_template("admin_index.htm")


@admin.route("/author/create", methods=["GET", "POST"])
@roles_required("admin")
def create_author():
    form = CreateAuthorForm(request.form)
    if request.method == "POST" and form.validate():
        names = form.names.data
        current_app.logger.info("Adding a new author %s.", (names))
        author = Author(names)

        try:
            db.session.add(author)
            db.session.commit()
            cache.clear()
            flash("Author successfully created.")
        except exc.SQLAlchemyError as e:
            flash("Author was not created.")


## ... source file continues with no further Blueprint examples...

```


## Example 7 from Flask-Bootstrap
[flask-bootstrap](https://github.com/mbr/flask-bootstrap)
([PyPI package information](https://pypi.org/project/Flask-Bootstrap/))
makes it easier to use the [Bootstrap CSS framework](/bootstrap-css.html)
in your [Flask](/flask.html) applications with less boilerplate
code. The project was primarily created by
[Marc Brinkmann @mbr](https://github.com/mbr) and the source code is
open sourced under the
[Apache 2.0 license](https://github.com/mbr/flask-bootstrap/blob/master/LICENSE).

[**Flask-Bootstrap / flask_bootstrap / __init__.py**](https://github.com/mbr/flask-bootstrap/blob/master/flask_bootstrap/./__init__.py)

```python
# __init__.py

import re

~~from flask import Blueprint, current_app, url_for

try:
    from wtforms.fields import HiddenField
except ImportError:

    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:

    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


from .forms import render_form

__version__ = '3.3.7.1.dev1'
BOOTSTRAP_VERSION = re.sub(r'^(\d+\.\d+\.\d+).*', r'\1', __version__)
JQUERY_VERSION = '1.12.4'
HTML5SHIV_VERSION = '3.7.3'
RESPONDJS_VERSION = '1.4.2'


class CDN(object):



## ... source file abbreviated to get to Blueprint examples ...


        filename = '%s.min.%s' % tuple(filename.rsplit('.', 1))

    cdns = current_app.extensions['bootstrap']['cdns']
    resource_url = cdns[cdn].get_resource_url(filename)

    if resource_url.startswith('//') and config['BOOTSTRAP_CDN_FORCE_SSL']:
        resource_url = 'https:%s' % resource_url

    return resource_url


class Bootstrap(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
        app.config.setdefault('BOOTSTRAP_CDN_FORCE_SSL', False)

        app.config.setdefault('BOOTSTRAP_QUERYSTRING_REVVING', True)
        app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', False)

        app.config.setdefault('BOOTSTRAP_LOCAL_SUBDOMAIN', None)

~~        blueprint = Blueprint(
            'bootstrap',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/bootstrap',
            subdomain=app.config['BOOTSTRAP_LOCAL_SUBDOMAIN'])

        blueprint.add_app_template_filter(render_form)

        app.register_blueprint(blueprint)

        app.jinja_env.globals['bootstrap_is_hidden_field'] =\
            is_hidden_field_filter
        app.jinja_env.globals['bootstrap_find_resource'] =\
            bootstrap_find_resource
        app.jinja_env.add_extension('jinja2.ext.do')

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        local = StaticCDN('bootstrap.static', rev=True)
        static = StaticCDN()

        def lwrap(cdn, primary=static):


## ... source file continues with no further Blueprint examples...

```


## Example 8 from flask-debugtoolbar
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


~~module = Blueprint('debugtoolbar', __name__)


def replace_insensitive(string, target, replacement):
    no_case = string.lower()
    index = no_case.rfind(target.lower())
    if index >= 0:
        return string[:index] + replacement + string[index + len(target):]
    else:  # no results so return the original string
        return string


def _printable(value):
    try:
        return decode_text(repr(value))
    except Exception as e:
        return '<repr(%s) raised %s: %s>' % (
               object.__repr__(value), type(e).__name__, e)


class DebugToolbarExtension(object):
    _static_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'static'))

    _redirect_codes = [301, 302, 303, 304]


## ... source file continues with no further Blueprint examples...

```


## Example 9 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / apidoc.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./apidoc.py)

```python
# apidoc.py
from __future__ import unicode_literals

~~from flask import url_for, Blueprint, render_template


~~class Apidoc(Blueprint):

    def __init__(self, *args, **kwargs):
        self.registered = False
        super(Apidoc, self).__init__(*args, **kwargs)

    def register(self, *args, **kwargs):
        super(Apidoc, self).register(*args, **kwargs)
        self.registered = True


apidoc = Apidoc(
    "restx_doc",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/swaggerui",
)


@apidoc.add_app_template_global
def swagger_static(filename):
    return url_for("restx_doc.static", filename=filename)




## ... source file continues with no further Blueprint examples...

```


## Example 10 from Flask-WTF
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

    if field_name not in g:


## ... source file abbreviated to get to Blueprint examples ...


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

        g.csrf_valid = True  # mark this request as CSRF valid

    def exempt(self, view):

~~        if isinstance(view, Blueprint):
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
        ), stacklevel=2)

        @wraps(view)
        def handler(reason):


## ... source file continues with no further Blueprint examples...

```


## Example 11 from Flask-User
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


## ... source file abbreviated to get to Blueprint examples ...



        @self.login_manager.user_loader
        def load_user_by_user_token(user_token):
            user = self.db_manager.UserClass.get_user_by_token(user_token)
            return user

        self.babel = app.extensions.get('babel', None)
        from .translation_utils import init_translations
        init_translations(self.babel)

        if not hasattr(app.jinja_env, 'install_gettext_callables'):
            app.jinja_env.add_extension('jinja2.ext.i18n')
            app.jinja_env.install_null_translations()

        def flask_user_context_processor():
            def call_or_get(function_or_property):
                return function_or_property() if callable(function_or_property) else function_or_property

            return dict(
                user_manager=current_app.user_manager,
                call_or_get=call_or_get,
            )

        app.context_processor(flask_user_context_processor)

~~        blueprint = Blueprint('flask_user', __name__, template_folder='templates')
        app.register_blueprint(blueprint)

        self.AddEmailFormClass = forms.AddEmailForm
        self.ChangePasswordFormClass = forms.ChangePasswordForm
        self.ChangeUsernameFormClass = forms.ChangeUsernameForm
        self.EditUserProfileFormClass = forms.EditUserProfileForm
        self.ForgotPasswordFormClass = forms.ForgotPasswordForm
        self.InviteUserFormClass = forms.InviteUserForm
        self.LoginFormClass = forms.LoginForm
        self.RegisterFormClass = forms.RegisterForm
        self.ResendEmailConfirmationFormClass = forms.ResendEmailConfirmationForm
        self.ResetPasswordFormClass = forms.ResetPasswordForm

        self.db_manager = DBManager(app, db, UserClass, UserEmailClass, UserInvitationClass, RoleClass)

        self.password_manager = PasswordManager(app)

        if self.USER_ENABLE_EMAIL:
            from .email_adapters.smtp_email_adapter import SMTPEmailAdapter
            self.email_adapter = SMTPEmailAdapter(app)

        if self.USER_ENABLE_EMAIL:
            self.email_manager = EmailManager(app)



## ... source file continues with no further Blueprint examples...

```


## Example 12 from Flask-VueJs-Template
[Flask-VueJs-Template](https://github.com/gtalarico/flask-vuejs-template)
([demo site](https://flask-vuejs-template.herokuapp.com/))
is a minimal [Flask](/flask.html) boilerplate starter project that
combines Flask, [Vue.js](https://www.fullstackpython.com/vuejs.html),
and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).
The project provides some sensible defaults that are easy to continue
building on, and the source code is open source under the
[MIT license](https://github.com/gtalarico/flask-vuejs-template/blob/master/LICENSE.md).

[**Flask-VueJs-Template / app / client.py**](https://github.com/gtalarico/flask-vuejs-template/blob/master/app/./client.py)

```python
# client.py

import os
~~from flask import Blueprint, render_template

~~client_bp = Blueprint('client_app', __name__,
                      url_prefix='',
                      static_url_path='',
                      static_folder='./dist/static/',
                      template_folder='./dist/',
                      )



## ... source file continues with no further Blueprint examples...

```


## Example 13 from Datadog Flask Example App
The [Datadog Flask example app](https://github.com/DataDog/trace-examples/tree/master/python/flask)
contains many examples of the [Flask](/flask.html) core functions
available to a developer using the [web framework](/web-frameworks.html).

[**Datadog Flask Example App / python/flask/app / blueprint.py**](https://github.com/DataDog/trace-examples/blob/master/python/flask/app/./blueprint.py)

```python
# blueprint.py
from ddtrace import Pin
~~from flask import abort, Blueprint, render_template_string

from .limiter import limiter


~~bp = Blueprint('bp', __name__, url_prefix='/bp/')

Pin.override(bp, service='flask-bp', app='flask', app_type='web')


@bp.before_request
def bp_before_request():
    print('Hook: bp_before_request')


@bp.before_app_request
def bp_before_app_request():
    print('Hook: bp_before_app_request')


@bp.before_app_first_request
def bp_before_app_first_request():
    print('Hook: bp_before_app_first_request')


@bp.after_request
def bp_after_request(response):
    print('Hook: bp_after_request')
    return response



## ... source file continues with no further Blueprint examples...

```


## Example 14 from tedivms-flask
[tedivm's flask starter app](https://github.com/tedivm/tedivms-flask) is a
base of [Flask](/flask.html) code and related projects such as
[Celery](/celery.html) which provides a template to start your own
Flask web app. The project comes baked with an admin panel,
[API authentication and authorization](/application-programming-interfaces.html),
[SQLAlchemy](/sqlalchemy.html) and many other common libraries that are
often used with Flask.

The project's code is provided as open source under the
[BSD 2-Clause "Simplified" license](https://github.com/tedivm/tedivms-flask/blob/master/LICENSE.txt).

[**tedivms-flask / app / extensions / jinja.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/extensions/jinja.py)

```python
# jinja.py
~~from flask import Blueprint
from wtforms.fields import HiddenField
from jinja2 import evalcontextfilter, Markup
import re

~~jinja_extensions_blueprint = Blueprint('jinja_extensions_blueprint', __name__, template_folder='templates')


@jinja_extensions_blueprint.app_template_filter()
def filesize_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.0f%s' % (num, ['', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'][magnitude])


@jinja_extensions_blueprint.app_template_global
def is_hidden_field_filter(field):
    return isinstance(field, HiddenField)


@jinja_extensions_blueprint.app_template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    normalized_value = re.sub(r'\r\n|\r|\n', '\n', value) # normalize newlines
    html_value = normalized_value.replace('\n', '\n<br />\n')
    if eval_ctx.autoescape:
        return Markup(html_value)
    return html_value


## ... source file continues with no further Blueprint examples...

```

