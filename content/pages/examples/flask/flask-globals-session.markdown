title: flask.globals session Python code examples
category: page
slug: flask-globals-session-examples
sortorder: 500021001
toc: False
sidebartitle: flask.globals session
meta: Python example code for the session function from the flask.globals module of the Flask project.


session is a function within the flask.globals module of the Flask project.


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

[**Flask AppBuilder / flask_appbuilder / security / registerviews.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/security/registerviews.py)

```python
# registerviews.py
__author__ = "Daniel Gaspar"

import logging

~~from flask import flash, redirect, request, session, url_for
from flask_babel import lazy_gettext
from flask_openid import OpenIDResponse, SessionWrapper
from openid.consumer.consumer import CANCEL, Consumer, SUCCESS

from .forms import LoginForm_oid, RegisterUserDBForm, RegisterUserOIDForm
from .. import const as c
from .._compat import as_unicode
from ..validators import Unique
from ..views import expose, PublicFormView

log = logging.getLogger(__name__)


def get_first_last_name(fullname):
    names = fullname.split()
    if len(names) > 1:
        return names[0], " ".join(names[1:])
    elif names:
        return names[0], ""


class BaseRegisterUser(PublicFormView):
    """
        Make your own user registration view and inherit from this class if you


## ... source file abbreviated to get to session examples ...


class RegisterUserOIDView(BaseRegisterUser):
    """
        View for Registering a new user, auth OID mode
    """

    route_base = "/register"

    form = RegisterUserOIDForm
    default_view = "form_oid_post"

    @expose("/formoidone", methods=["GET", "POST"])
    def form_oid_post(self, flag=True):
        if flag:
            self.oid_login_handler(self.form_oid_post, self.appbuilder.sm.oid)
        form = LoginForm_oid()
        if form.validate_on_submit():
            session["remember_me"] = form.remember_me.data
            return self.appbuilder.sm.oid.try_login(
                form.openid.data, ask_for=["email", "fullname"]
            )
~~        resp = session.pop("oid_resp", None)
        if resp:
            self._init_vars()
            form = self.form.refresh()
            self.form_get(form)
            form.username.data = resp.email
            first_name, last_name = get_first_last_name(resp.fullname)
            form.first_name.data = first_name
            form.last_name.data = last_name
            form.email.data = resp.email
            widgets = self._get_edit_widget(form=form)
            # self.update_redirect()
            return self.render_template(
                self.form_template,
                title=self.form_title,
                widgets=widgets,
                form_action="form",
                appbuilder=self.appbuilder,
            )
        else:
            flash(as_unicode(self.error_message), "warning")
            return redirect(self.get_redirect())

    def oid_login_handler(self, f, oid):
        """


## ... source file continues with no further session examples...


```


## Example 2 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / utils / helpers.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/utils/helpers.py)

```python
# helpers.py
"""
import ast
import itertools
import logging
import operator
import os
import re
import time
import warnings
from datetime import datetime, timedelta
from email import message_from_string
from functools import wraps

import pkg_resources
import requests
import unidecode
from babel.core import get_locale_identifier
from babel.dates import format_date as babel_format_date
from babel.dates import format_datetime as babel_format_datetime
from babel.dates import format_timedelta as babel_format_timedelta
~~from flask import flash, g, redirect, request, session, url_for
from flask_allows import Permission
from flask_babelplus import lazy_gettext as _
from flask_login import current_user
from flask_themes2 import get_themes_list, render_theme_template
from jinja2 import Markup
from PIL import ImageFile
from pytz import UTC
from werkzeug.local import LocalProxy
from werkzeug.utils import ImportStringError, import_string

from flaskbb._compat import (iteritems, range_method, string_types, text_type,
                             to_bytes, to_unicode)
from flaskbb.extensions import babel, redis_store
from flaskbb.utils.settings import flaskbb_config

try:  # compat
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

logger = logging.getLogger(__name__)

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')



## ... source file abbreviated to get to session examples ...


            result.append(word)
    return text_type(delim.join(result))


def redirect_or_next(endpoint, **kwargs):
    """Redirects the user back to the page they were viewing or to a specified
    endpoint. Wraps Flasks :func:`Flask.redirect` function.

    :param endpoint: The fallback endpoint.
    """
    return redirect(request.args.get("next") or endpoint, **kwargs)


def render_template(template, **context):  # pragma: no cover
    """A helper function that uses the `render_theme_template` function
    without needing to edit all the views
    """
    if current_user.is_authenticated and current_user.theme:
        theme = current_user.theme
    else:
~~        theme = session.get("theme", flaskbb_config["DEFAULT_THEME"])
    return render_theme_template(theme, template, **context)


# TODO(anr): clean this up
def do_topic_action(topics, user, action, reverse):  # noqa: C901
    """Executes a specific action for topics. Returns a list with the modified
    topic objects.

    :param topics: A iterable with ``Topic`` objects.
    :param user: The user object which wants to perform the action.
    :param action: One of the following actions: locked, important and delete.
    :param reverse: If the action should be done in a reversed way.
                    For example, to unlock a topic, ``reverse`` should be
                    set to ``True``.
    """
    if not topics:
        return False

    from flaskbb.utils.requirements import (
        IsAtleastModeratorInForum,
        CanDeleteTopic,
        Has,
    )



## ... source file continues with no further session examples...


```


## Example 3 from flaskex
[Flaskex](https://github.com/anfederico/Flaskex) is a working example
[Flask](/flask.html) web application intended as a base to build your
own applications upon. The application comes with pre-built sign up, log in
and related screens, as well as a database backend. Flaskex is provided
as open source under the
[MIT license](https://github.com/anfederico/Flaskex/blob/master/LICENSE.txt).

[**flaskex / app.py**](https://github.com/anfederico/Flaskex/blob/master/././app.py)

```python
# app.py
# -*- coding: utf-8 -*-

from scripts import tabledef
from scripts import forms
from scripts import helpers
~~from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)

# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def login():
~~    if not session.get('logged_in'):
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
    session['logged_in'] = False
    return redirect(url_for('login'))


# -------- Signup ---------------------------------------------------------- #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
~~    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = helpers.hash_password(request.form['password'])
            email = request.form['email']
            if form.validate():
                if not helpers.username_taken(username):
                    helpers.add_user(username, password, email)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Signup successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'User/Pass required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login'))


# -------- Settings ---------------------------------------------------------- #
@app.route('/settings', methods=['GET', 'POST'])
def settings():
~~    if session.get('logged_in'):
        if request.method == 'POST':
            password = request.form['password']
            if password != "":
                password = helpers.hash_password(password)
            email = request.form['email']
            helpers.change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")


## ... source file continues with no further session examples...


```


## Example 4 from flask-login
[Flask-Login](https://github.com/maxcountryman/flask-login)
([project documentation](https://flask-login.readthedocs.io/en/latest/)
and [PyPI package](https://pypi.org/project/Flask-Login/))
is a [Flask](/flask.html) extension that provides user session
management, which handles common tasks such as logging in
and out of a [web application](/web-development.html) and
managing associated user session data. Flask-Login is
open sourced under the
[MIT license](https://github.com/maxcountryman/flask-login/blob/master/LICENSE).

[**flask-login / flask_login / utils.py**](https://github.com/maxcountryman/flask-login/blob/master/flask_login/./utils.py)

```python
# utils.py
# -*- coding: utf-8 -*-
'''
    flask_login.utils
    -----------------
    General utilities.
'''


import hmac
from hashlib import sha512
from functools import wraps
from werkzeug.local import LocalProxy
from werkzeug.security import safe_str_cmp
from werkzeug.urls import url_decode, url_encode

~~from flask import (_request_ctx_stack, current_app, request, session, url_for,
                   has_request_context)

from ._compat import text_type, urlparse, urlunparse
from .config import COOKIE_NAME, EXEMPT_METHODS
from .signals import user_logged_in, user_logged_out, user_login_confirmed


#: A proxy for the current user. If no user is logged in, this will be an
#: anonymous user
current_user = LocalProxy(lambda: _get_user())


def encode_cookie(payload, key=None):
    '''
    This will encode a ``unicode`` value into a cookie, and sign that cookie
    with the app's secret key.

    :param payload: The value to encode, as `unicode`.
    :type payload: unicode

    :param key: The key to use when creating the cookie digest. If not
                specified, the SECRET_KEY value from app config will be used.
    :type key: str
    '''


## ... source file abbreviated to get to session examples ...


    '''
    base = expand_login_view(login_view)

    if next_url is None:
        return base

    parsed_result = urlparse(base)
    md = url_decode(parsed_result.query)
    md[next_field] = make_next_param(base, next_url)
    netloc = current_app.config.get('FORCE_HOST_FOR_REDIRECTS') or \
        parsed_result.netloc
    parsed_result = parsed_result._replace(netloc=netloc,
                                           query=url_encode(md, sort=True))
    return urlunparse(parsed_result)


def login_fresh():
    '''
    This returns ``True`` if the current login is fresh.
    '''
~~    return session.get('_fresh', False)


def login_user(user, remember=False, duration=None, force=False, fresh=True):
    '''
    Logs a user in. You should pass the actual user object to this. If the
    user's `is_active` property is ``False``, they will not be logged in
    unless `force` is ``True``.

    This will return ``True`` if the log in attempt succeeds, and ``False`` if
    it fails (i.e. because the user is inactive).

    :param user: The user object to log in.
    :type user: object
    :param remember: Whether to remember the user after their session expires.
        Defaults to ``False``.
    :type remember: bool
    :param duration: The amount of time before the remember cookie expires. If
        ``None`` the value set in the settings is used. Defaults to ``None``.
    :type duration: :class:`datetime.timedelta`
    :param force: If the user is inactive, setting this to ``True`` will log
        them in regardless. Defaults to ``False``.
    :type force: bool
    :param fresh: setting this to ``False`` will log in the user with a session
        marked as not "fresh". Defaults to ``True``.


## ... source file abbreviated to get to session examples ...


                                                (duration.seconds +
                                                 duration.days * 24 * 3600) *
                                                10**6) / 10.0**6
            except AttributeError:
                raise Exception('duration must be a datetime.timedelta, '
                                'instead got: {0}'.format(duration))

    current_app.login_manager._update_request_context_with_user(user)
    user_logged_in.send(current_app._get_current_object(), user=_get_user())
    return True


def logout_user():
    '''
    Logs a user out. (You do not need to pass the actual user.) This will
    also clean up the remember me cookie if it exists.
    '''

    user = _get_user()

~~    if '_user_id' in session:
~~        session.pop('_user_id')

~~    if '_fresh' in session:
~~        session.pop('_fresh')

~~    if '_id' in session:
~~        session.pop('_id')

    cookie_name = current_app.config.get('REMEMBER_COOKIE_NAME', COOKIE_NAME)
    if cookie_name in request.cookies:
        session['_remember'] = 'clear'
~~        if '_remember_seconds' in session:
~~            session.pop('_remember_seconds')

    user_logged_out.send(current_app._get_current_object(), user=user)

    current_app.login_manager._update_request_context_with_user()
    return True


def confirm_login():
    '''
    This sets the current session as fresh. Sessions become stale when they
    are reloaded from a cookie.
    '''
    session['_fresh'] = True
    session['_id'] = current_app.login_manager._session_identifier_generator()
    user_login_confirmed.send(current_app._get_current_object())


def login_required(func):
    '''
    If you decorate a view with this, it will ensure that the current user is
    logged in and authenticated before calling the actual view. (If they are
    not, it calls the :attr:`LoginManager.unauthorized` callback.) For
    example::



## ... source file continues with no further session examples...


```


## Example 5 from Flask-WTF
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

    secret_key = _get_config(
        secret_key, 'WTF_CSRF_SECRET_KEY', current_app.secret_key,
        message='A secret key is required to use CSRF.'
    )
    field_name = _get_config(
        token_key, 'WTF_CSRF_FIELD_NAME', 'csrf_token',
        message='A field name is required to use CSRF.'
    )

    if field_name not in g:
        s = URLSafeTimedSerializer(secret_key, salt='wtf-csrf-token')

~~        if field_name not in session:
            session[field_name] = hashlib.sha1(os.urandom(64)).hexdigest()

        try:
            token = s.dumps(session[field_name])
        except TypeError:
            session[field_name] = hashlib.sha1(os.urandom(64)).hexdigest()
            token = s.dumps(session[field_name])

        setattr(g, field_name, token)

    return g.get(field_name)


def validate_csrf(data, secret_key=None, time_limit=None, token_key=None):
    """Check if the given data is a valid CSRF token. This compares the given
    signed token to the one stored in the session.

    :param data: The signed CSRF token to be checked.
    :param secret_key: Used to securely sign the token. Default is
        ``WTF_CSRF_SECRET_KEY`` or ``SECRET_KEY``.
    :param time_limit: Number of seconds that the token is valid. Default is
        ``WTF_CSRF_TIME_LIMIT`` or 3600 seconds (60 minutes).
    :param token_key: Key where token is stored in session for comparison.
        Default is ``WTF_CSRF_FIELD_NAME`` or ``'csrf_token'``.


## ... source file abbreviated to get to session examples ...


    .. versionchanged:: 0.14
        Raises ``ValidationError`` with a specific error message rather than
        returning ``True`` or ``False``.
    """

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

~~    if field_name not in session:
        raise ValidationError('The CSRF session token is missing.')

    s = URLSafeTimedSerializer(secret_key, salt='wtf-csrf-token')

    try:
        token = s.loads(data, max_age=time_limit)
    except SignatureExpired:
        raise ValidationError('The CSRF token has expired.')
    except BadData:
        raise ValidationError('The CSRF token is invalid.')

    if not safe_str_cmp(session[field_name], token):
        raise ValidationError('The CSRF tokens do not match.')


def _get_config(
    value, config_name, default=None,
    required=True, message='CSRF is not configured.'
):
    """Find config value based on provided value, Flask config, and default
    value.

    :param value: already provided config value
    :param config_name: Flask ``config`` key


## ... source file continues with no further session examples...


```


## Example 6 from flaskSaaS
[flaskSaas](https://github.com/alectrocute/flaskSaaS) is a boilerplate
starter project to build a software-as-a-service (SaaS) web application
in [Flask](/flask.html), with [Stripe](/stripe.html) for billing. The
boilerplate relies on many common Flask extensions such as
[Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/),
[Flask-Login](https://flask-login.readthedocs.io/en/latest/),
[Flask-Admin](https://flask-admin.readthedocs.io/en/latest/), and
many others. The project is provided as open source under the
[MIT license](https://github.com/alectrocute/flaskSaaS/blob/master/LICENSE).

[**flaskSaaS / app / logger_setup.py**](https://github.com/alectrocute/flaskSaaS/blob/master/app/./logger_setup.py)

```python
# logger_setup.py
:Example:
        >>> from website import logger
        >>> logger.info('event', foo='bar')
**Levels**:
        - logger.debug('For debugging purposes')
        - logger.info('An event occured, for example a database update')
        - logger.warning('Rare situation')
        - logger.error('Something went wrong')
        - logger.critical('Very very bad')
You can build a log incrementally as so:
        >>> log = logger.new(date='now')
        >>> log = log.bind(weather='rainy')
        >>> log.info('user logged in', user='John')
'''

import datetime as dt
import logging
from logging.handlers import RotatingFileHandler
import pytz

~~from flask import request, session
from structlog import wrap_logger
from structlog.processors import JSONRenderer

from app import app

# Set the logging level
app.logger.setLevel(app.config['LOG_LEVEL'])

# Remove the stdout handler
app.logger.removeHandler(app.logger.handlers[0])

TZ = pytz.timezone(app.config['TIMEZONE'])


def add_fields(_, level, event_dict):
    ''' Add custom fields to each record. '''
    now = dt.datetime.now()
    event_dict['timestamp'] = TZ.localize(now, True).astimezone(pytz.utc).isoformat()
    event_dict['level'] = level

~~    if session:
~~        event_dict['session_id'] = session.get('session_id')

    if request:
        try:
            event_dict['ip_address'] = request.headers['X-Forwarded-For'].split(',')[0].strip()
        except:
            event_dict['ip_address'] = 'unknown'

    return event_dict


# Add a handler to write log messages to a file
if app.config.get('LOG_FILENAME'):
    file_handler = RotatingFileHandler(filename=app.config['LOG_FILENAME'],
                                       maxBytes=app.config['LOG_MAXBYTES'],
                                       backupCount=app.config['LOG_BACKUPS'],
                                       mode='a',
                                       encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

# Wrap the application logger with structlog to format the output
logger = wrap_logger(
    app.logger,
    processors=[


## ... source file continues with no further session examples...


```

