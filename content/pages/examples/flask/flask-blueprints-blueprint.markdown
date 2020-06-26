title: flask.blueprints Blueprint code examples
category: page
slug: flask-blueprints-blueprint-examples
sortorder: 500021002
toc: False
sidebartitle: flask.blueprints Blueprint
meta: Python example code for the Blueprint class from the flask.blueprints module of the Flask project.


A Blueprint in [Flask](/flask.html) is
[a "mold" or template for creating parts of web applications](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly).


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


## Example 2 from FlaskBB
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


## Example 4 from flask-bookshelf
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


## Example 5 from flask-debugtoolbar
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
from flask_debugtoolbar.utils import decode_text

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


## Example 6 from flask-restx
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


## Example 7 from Flask-WTF
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
from functools import wraps

~~from flask import Blueprint, current_app, g, request, session
from itsdangerous import BadData, SignatureExpired, URLSafeTimedSerializer
from werkzeug.exceptions import BadRequest
from werkzeug.security import safe_str_cmp
from wtforms import ValidationError
from wtforms.csrf.core import CSRF

from ._compat import FlaskWTFDeprecationWarning, string_types, urlparse

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

            good_referrer = 'https://{0}/'.format(request.host)

            if not same_origin(request.referrer, good_referrer):
                self._error_response('The referrer does not match the host.')

        g.csrf_valid = True  # mark this request as CSRF valid

    def exempt(self, view):

~~        if isinstance(view, Blueprint):
            self._exempt_blueprints.add(view.name)
            return view

        if isinstance(view, string_types):
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


## Example 8 from tedivms-flask
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

