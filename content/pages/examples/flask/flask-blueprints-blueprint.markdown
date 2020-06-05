title: flask.blueprints Blueprint code examples
category: page
slug: flask-blueprints-blueprint-examples
sortorder: 500021000
toc: False
sidebartitle: flask.blueprints Blueprint
meta: Python example code for the Blueprint class from the flask.blueprints module of the Flask project.


Blueprint is a class within the flask.blueprints module of the Flask project.


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
    """
        Will dynamically import a class from a string path
        :param class_path: string with class path


## ... source file abbreviated to get to Blueprint examples ...


        """
        return self.get_app.config["APP_ICON"]

    @property
    def languages(self):
        return self.get_app.config["LANGUAGES"]

    @property
    def version(self):
        """
            Get the current F.A.B. version

            :return: String with the current F.A.B. version
        """
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
        """
            Registers indexview, utilview (back function), babel views and Security views.
        """
        self.indexview = self._check_and_init(self.indexview)
        self.add_view_no_menu(self.indexview)
        self.add_view_no_menu(UtilView())
        self.bm.register_views()
        self.sm.register_views()
        self.openapi_manager.register_views()
        self.menuapi_manager.register_views()

    def _add_addon_views(self):
        """
            Registers declared addon's


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
# -*- coding: utf-8 -*-
"""
    flaskbb.auth.views
    ------------------

    This view provides user authentication, registration and a view for
    resetting the password of a user if he has lost his password

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
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
        """Dynamically load the rate limiting config from the database."""
        # [count] [per|/] [n (optional)] [second|minute|hour|day|month|year]
        return "{count}/{timeout}minutes".format(
            count=flaskbb_config["AUTH_REQUESTS"],
            timeout=flaskbb_config["AUTH_TIMEOUT"]
        )

    def login_rate_limit_message():
        """Display the amount of time left until the user can access the requested
        resource again."""
        current_limit = getattr(g, 'view_rate_limit', None)
        if current_limit is not None:
            window_stats = limiter.limiter.get_window_stats(*current_limit)
            reset_time = datetime.utcfromtimestamp(window_stats[0])
            timeout = reset_time - datetime.utcnow()
        return "{timeout}".format(timeout=format_timedelta(timeout))

    @auth.before_request
    def check_rate_limiting():
        """Check the the rate limits for each request for this blueprint."""
        if not flaskbb_config["AUTH_RATELIMIT_ENABLED"]:
            return None


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


## Example 4 from flask_jsondash
[Flask JSONDash](https://github.com/christabor/flask_jsondash) is a
configurable web application built in Flask that creates charts and
dashboards from arbitrary API endpoints. Everything for the web app
is configured in JSON. The code is provided as open source under the
[MIT license](https://github.com/christabor/flask_jsondash/blob/master/LICENSE).

[**flask_jsondash / flask_jsondash / charts_builder.py**](https://github.com/christabor/flask_jsondash/blob/master/flask_jsondash/./charts_builder.py)

```python
# charts_builder.py
# -*- coding: utf-8 -*-

"""
flask_jsondash.charts_builder
-----------------------------

The chart blueprint that houses all functionality.

:copyright: (c) 2016 by Chris Tabor.
:license: MIT, see LICENSE for more details.
"""

import json
import os
import uuid
from datetime import datetime as dt

import jinja2
~~from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, send_from_directory, url_for)

from flask_jsondash import static, templates

from flask_jsondash import db
from flask_jsondash import settings
from flask_jsondash.utils import setting
from flask_jsondash.utils import adapter
from flask_jsondash import utils
from flask_jsondash.schema import (
    validate_raw_json, InvalidSchemaError,
)

TEMPLATE_DIR = os.path.dirname(templates.__file__)
STATIC_DIR = os.path.dirname(static.__file__)

# Internally required libs that are also shared in `settings.py`
# for charts. These follow the same format as what is loaded in
# `get_active_assets` so that shared libraries are loaded in the same manner
# for simplicty and prevention of duplicate loading.
# Note these are just LABELS, not files.
REQUIRED_STATIC_FAMILES = ['D3']

~~charts = Blueprint(
    'jsondash',
    __name__,
    template_folder=TEMPLATE_DIR,
    static_url_path=STATIC_DIR,
    static_folder=STATIC_DIR,
)


def auth(**kwargs):
    """Check if general auth functions have been specified.

    Checks for either a global auth (if authtype is None), or
    an action specific auth (specified by authtype).
    """
    if 'JSONDASH' not in current_app.config:
        return True
    if 'auth' not in current_app.config['JSONDASH']:
        return True
    authtype = kwargs.pop('authtype')
    auth_conf = current_app.config.get('JSONDASH').get('auth')
    # If the user didn't supply an auth function, assume true.
    if authtype not in auth_conf:
        return True
    # Only perform the user-supplied check


## ... source file continues with no further Blueprint examples...


```


## Example 5 from flask-restx
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
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

~~from flask import url_for, Blueprint, render_template


~~class Apidoc(Blueprint):
    """
    Allow to know if the blueprint has already been registered
    until https://github.com/mitsuhiko/flask/pull/1301 is merged
    """

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


## ... source file continues with no further Blueprint examples...


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
    """Generate a CSRF token. The token is cached for a request, so multiple
    calls to this function will generate the same token.

    During testing, it might be useful to access the signed token in
    ``g.csrf_token`` and the raw token in ``session['csrf_token']``.

    :param secret_key: Used to securely sign the token. Default is
        ``WTF_CSRF_SECRET_KEY`` or ``SECRET_KEY``.
    :param token_key: Key where token is stored in session for comparison.
        Default is ``WTF_CSRF_FIELD_NAME`` or ``'csrf_token'``.
    """


## ... source file abbreviated to get to Blueprint examples ...



            good_referrer = 'https://{0}/'.format(request.host)

            if not same_origin(request.referrer, good_referrer):
                self._error_response('The referrer does not match the host.')

        g.csrf_valid = True  # mark this request as CSRF valid

    def exempt(self, view):
        """Mark a view or blueprint to be excluded from CSRF protection.

        ::

            @app.route('/some-view', methods=['POST'])
            @csrf.exempt
            def some_view():
                ...

        ::

~~            bp = Blueprint(...)
            csrf.exempt(bp)

        """

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
        """Register a function that will generate the response for CSRF errors.

        .. deprecated:: 0.14
            Use the standard Flask error system with
            ``@app.errorhandler(CSRFError)`` instead. This will be removed in
            version 1.0.

        The function will be passed one argument, ``reason``. By default it
        will raise a :class:`-flask_wtf.csrf.CSRFError`. ::


## ... source file continues with no further Blueprint examples...


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

[**flaskSaaS / app / views / user.py**](https://github.com/alectrocute/flaskSaaS/blob/master/app/views/user.py)

```python
# user.py
~~from flask import (Blueprint, render_template, redirect, request, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required, current_user
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import user as user_forms
from app.toolbox import email
# Setup Stripe integration
import stripe
import json
from json import dumps

stripe_keys = {
	'secret_key': "sk_test_GvpPOs0XFxeP0fQiWMmk6HYe",
	'publishable_key': "pk_test_UU62FhsIB6457uPiUX6mJS5x"
}

stripe.api_key = stripe_keys['secret_key']

# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
~~userbp = Blueprint('userbp', __name__, url_prefix='/user')


@userbp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = user_forms.SignUp()
    if form.validate_on_submit():
        # Create a user who hasn't validated his email address
        user = models.User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data,
            email=form.email.data,
            confirmation=False,
            password=form.password.data,
        )
        # Insert the user in the database
        db.session.add(user)
        db.session.commit()
        # Subject of the confirmation email
        subject = 'Please confirm your email address.'
        # Generate a random token
        token = ts.dumps(user.email, salt='email-confirm-key')
        # Build a confirm link with token
        confirmUrl = url_for('userbp.confirm', token=token, _external=True)


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
    """Converts newlines into <p> and <br />s."""
    normalized_value = re.sub(r'\r\n|\r|\n', '\n', value) # normalize newlines
    html_value = normalized_value.replace('\n', '\n<br />\n')
    if eval_ctx.autoescape:
        return Markup(html_value)


## ... source file continues with no further Blueprint examples...


```

