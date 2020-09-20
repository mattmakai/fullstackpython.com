title: flask.globals session Example Code
category: page
slug: flask-globals-session-examples
sortorder: 500021017
toc: False
sidebartitle: flask.globals session
meta: Python example code that shows how to use the session callable from the flask.globals module of the Flask project.


[session](https://github.com/pallets/flask/blob/master/src/flask/globals.py)
is function in the [Flask](/flask.html) `flask.globals` module and is an
instance of
[LocalProxy](https://github.com/pallets/werkzeug/blob/master/src/werkzeug/local.py)
from the [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) library.
`session` stores data about the user session for the current request and it
can be used to access session data.

Note that `session` is usually imported directly from `flask` instead of
from `flask.globals`, even though it is defined within the `globals` module.
It's the same function that is imported, but it's less characters to type
when you leave off the `.globals` part.

<a href="/flask-globals-current-app-examples.html">current_app</a>,
<a href="/flask-globals-g-examples.html">g</a>,
and <a href="/flask-globals-request-examples.html">request</a>
are several other callables with code examples from the same `flask.globals` package.

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
from flask import Blueprint
from flask import current_app as app
~~from flask import redirect, render_template, request, session, url_for
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

auth = Blueprint("auth", __name__)


@auth.route("/confirm", methods=["POST", "GET"])


## ... source file abbreviated to get to session examples ...


        log("registrations", "[{date}] {ip} - {name} registered with {email}")
        db.session.close()

        if is_teams_mode():
            return redirect(url_for("teams.private"))

        return redirect(url_for("challenges.listing"))
    else:
        return render_template("register.html", errors=errors)


@auth.route("/login", methods=["POST", "GET"])
@ratelimit(method="POST", limit=10, interval=5)
def login():
    errors = get_errors()
    if request.method == "POST":
        name = request.form["name"]

        if validators.validate_email(name) is True:
            user = Users.query.filter_by(email=name).first()
        else:
            user = Users.query.filter_by(name=name).first()

        if user:
            if user and verify_password(request.form["password"], user.password):
~~                session.regenerate()

                login_user(user)
                log("logins", "[{date}] {ip} - {name} logged in")

                db.session.close()
                if request.args.get("next") and validators.is_safe_url(
                    request.args.get("next")
                ):
                    return redirect(request.args.get("next"))
                return redirect(url_for("challenges.listing"))

            else:
                log("logins", "[{date}] {ip} - submitted invalid password for {name}")
                errors.append("Your username or password is incorrect")
                db.session.close()
                return render_template("login.html", errors=errors)
        else:
            log("logins", "[{date}] {ip} - submitted invalid account information")
            errors.append("Your username or password is incorrect")
            db.session.close()
            return render_template("login.html", errors=errors)
    else:
        db.session.close()
        return render_template("login.html", errors=errors)


## ... source file continues with no further session examples...

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

    route_base = "/register"


## ... source file abbreviated to get to session examples ...


            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data,
        )


class RegisterUserOIDView(BaseRegisterUser):

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
        if request.args.get("openid_complete") != u"yes":
            return f(False)


## ... source file continues with no further session examples...

```


## Example 3 from FlaskBB
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


def slugify(text, delim=u"-"):
    text = unidecode.unidecode(text)
    result = []
    for word in _punct_re.split(text.lower()):
        if word:
            result.append(word)
    return text_type(delim.join(result))


def redirect_or_next(endpoint, **kwargs):
    return redirect(request.args.get("next") or endpoint, **kwargs)


def render_template(template, **context):  # pragma: no cover
    if current_user.is_authenticated and current_user.theme:
        theme = current_user.theme
    else:
~~        theme = session.get("theme", flaskbb_config["DEFAULT_THEME"])
    return render_theme_template(theme, template, **context)


def do_topic_action(topics, user, action, reverse):  # noqa: C901
    if not topics:
        return False

    from flaskbb.utils.requirements import (
        IsAtleastModeratorInForum,
        CanDeleteTopic,
        Has,
    )

    if not Permission(IsAtleastModeratorInForum(forum=topics[0].forum)):
        flash(
            _("You do not have the permissions to execute this action."),
            "danger",
        )
        return False

    modified_topics = 0
    if action not in {"delete", "hide", "unhide"}:
        for topic in topics:
            if getattr(topic, action) and not reverse:


## ... source file continues with no further session examples...

```


## Example 4 from flaskex
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

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only


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


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")



## ... source file continues with no further session examples...

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



## ... source file abbreviated to get to session examples ...




class HTTPDigestAuth(HTTPAuth):
    def __init__(self, scheme=None, realm=None, use_ha1_pw=False):
        super(HTTPDigestAuth, self).__init__(scheme or 'Digest', realm)
        self.use_ha1_pw = use_ha1_pw
        self.random = SystemRandom()
        try:
            self.random.random()
        except NotImplementedError:  # pragma: no cover
            self.random = Random()

        self.generate_nonce_callback = None
        self.verify_nonce_callback = None
        self.generate_opaque_callback = None
        self.verify_opaque_callback = None

        def _generate_random():
            return md5(str(self.random.random()).encode('utf-8')).hexdigest()

        def default_generate_nonce():
            session["auth_nonce"] = _generate_random()
            return session["auth_nonce"]

        def default_verify_nonce(nonce):
~~            session_nonce = session.get("auth_nonce")
            if nonce is None or session_nonce is None:
                return False
            return safe_str_cmp(nonce, session_nonce)

        def default_generate_opaque():
            session["auth_opaque"] = _generate_random()
            return session["auth_opaque"]

        def default_verify_opaque(opaque):
~~            session_opaque = session.get("auth_opaque")
            if opaque is None or session_opaque is None:  # pragma: no cover
                return False
            return safe_str_cmp(opaque, session_opaque)

        self.generate_nonce(default_generate_nonce)
        self.generate_opaque(default_generate_opaque)
        self.verify_nonce(default_verify_nonce)
        self.verify_opaque(default_verify_opaque)

    def generate_nonce(self, f):
        self.generate_nonce_callback = f
        return f

    def verify_nonce(self, f):
        self.verify_nonce_callback = f
        return f

    def generate_opaque(self, f):
        self.generate_opaque_callback = f
        return f

    def verify_opaque(self, f):
        self.verify_opaque_callback = f
        return f


## ... source file continues with no further session examples...

```


## Example 6 from flask-login
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


current_user = LocalProxy(lambda: _get_user())


def encode_cookie(payload, key=None):
    return u'{0}|{1}'.format(payload, _cookie_digest(payload, key=key))


def decode_cookie(cookie, key=None):
    try:
        payload, digest = cookie.rsplit(u'|', 1)
        if hasattr(digest, 'decode'):
            digest = digest.decode('ascii')  # pragma: no cover
    except ValueError:
        return

    if safe_str_cmp(_cookie_digest(payload, key=key), digest):
        return payload


## ... source file abbreviated to get to session examples ...


        return login_view
    else:
        if request.view_args is None:
            return url_for(login_view)
        else:
            return url_for(login_view, **request.view_args)


def login_url(login_view, next_url=None, next_field='next'):
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
~~    return session.get('_fresh', False)


def login_user(user, remember=False, duration=None, force=False, fresh=True):
    if not force and not user.is_active:
        return False

    user_id = getattr(user, current_app.login_manager.id_attribute)()
    session['_user_id'] = user_id
    session['_fresh'] = fresh
    session['_id'] = current_app.login_manager._session_identifier_generator()

    if remember:
        session['_remember'] = 'set'
        if duration is not None:
            try:
                session['_remember_seconds'] = (duration.microseconds +
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
    session['_fresh'] = True
    session['_id'] = current_app.login_manager._session_identifier_generator()
    user_login_confirmed.send(current_app._get_current_object())


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view


## ... source file continues with no further session examples...

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

    if value is None:
        value = current_app.config.get(config_name, default)

    if required and value is None:


## ... source file continues with no further session examples...

```


## Example 8 from flaskSaaS
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

import datetime as dt
import logging
from logging.handlers import RotatingFileHandler
import pytz

~~from flask import request, session
from structlog import wrap_logger
from structlog.processors import JSONRenderer

from app import app

app.logger.setLevel(app.config['LOG_LEVEL'])

app.logger.removeHandler(app.logger.handlers[0])

TZ = pytz.timezone(app.config['TIMEZONE'])


def add_fields(_, level, event_dict):
    now = dt.datetime.now()
    event_dict['timestamp'] = TZ.localize(now, True).astimezone(pytz.utc).isoformat()
    event_dict['level'] = level

    if session:
~~        event_dict['session_id'] = session.get('session_id')

    if request:
        try:
            event_dict['ip_address'] = request.headers['X-Forwarded-For'].split(',')[0].strip()
        except:
            event_dict['ip_address'] = 'unknown'

    return event_dict


if app.config.get('LOG_FILENAME'):
    file_handler = RotatingFileHandler(filename=app.config['LOG_FILENAME'],
                                       maxBytes=app.config['LOG_MAXBYTES'],
                                       backupCount=app.config['LOG_BACKUPS'],
                                       mode='a',
                                       encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

logger = wrap_logger(
    app.logger,
    processors=[
        add_fields,
        JSONRenderer(indent=None)


## ... source file continues with no further session examples...

```


## Example 9 from Flask-Security-Too
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

[**Flask-Security-Too / flask_security / twofactor.py**](https://github.com/Flask-Middleware/flask-security/blob/master/flask_security/./twofactor.py)

```python
# twofactor.py

~~from flask import current_app as app, redirect, request, session
from werkzeug.datastructures import MultiDict
from werkzeug.local import LocalProxy

from .utils import (
    SmsSenderFactory,
    base_render_json,
    config_value,
    do_flash,
    login_user,
    json_error_response,
    send_mail,
    url_for_security,
)
from .signals import (
    tf_code_confirmed,
    tf_disabled,
    tf_security_token_sent,
    tf_profile_changed,
)

_security = LocalProxy(lambda: app.extensions["security"])
_datastore = LocalProxy(lambda: _security.datastore)


def tf_clean_session():
    if config_value("TWO_FACTOR"):
        for k in [
            "tf_state",
            "tf_user_id",
            "tf_primary_method",
            "tf_remember_login",
            "tf_totp_secret",
        ]:
~~            session.pop(k, None)


def tf_send_security_token(user, method, totp_secret, phone_number):
    token_to_be_sent = _security._totp_factory.generate_totp_password(totp_secret)
    if method == "email" or method == "mail":
        send_mail(
            config_value("EMAIL_SUBJECT_TWO_FACTOR"),
            user.email,
            "two_factor_instructions",
            user=user,
            token=token_to_be_sent,
            username=user.calc_username(),
        )
    elif method == "sms":
        msg = "Use this code to log in: %s" % token_to_be_sent
        from_number = config_value("SMS_SERVICE_CONFIG")["PHONE_NUMBER"]
        to_number = phone_number
        sms_sender = SmsSenderFactory.createSender(config_value("SMS_SERVICE"))
        sms_sender.send_sms(from_number=from_number, to_number=to_number, msg=msg)

    elif method == "google_authenticator" or method == "authenticator":
        pass
    tf_security_token_sent.send(
        app._get_current_object(),


## ... source file continues with no further session examples...

```


## Example 10 from Flask-SocketIO
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

[**Flask-SocketIO / example / sessions.py**](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/./example/sessions.py)

```python
# sessions.py
~~from flask import Flask, render_template, session, request, jsonify
from flask_login import LoginManager, UserMixin, current_user, login_user, \
    logout_user
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
app.config['SESSION_TYPE'] = 'filesystem'
login = LoginManager(app)
Session(app)
socketio = SocketIO(app, manage_session=False)


class User(UserMixin, object):
    def __init__(self, id=None):
        self.id = id


@login.user_loader
def load_user(id):
    return User(id)


@app.route('/')
def index():
    return render_template('sessions.html')


@app.route('/session', methods=['GET', 'POST'])
def session_access():
    if request.method == 'GET':
        return jsonify({
~~            'session': session.get('value', ''),
            'user': current_user.id
                if current_user.is_authenticated else 'anonymous'
        })
    data = request.get_json()
    if 'session' in data:
        session['value'] = data['session']
    elif 'user' in data:
        if data['user']:
            login_user(User(data['user']))
        else:
            logout_user()
    return '', 204


@socketio.on('get-session')
def get_session():
    emit('refresh-session', {
~~        'session': session.get('value', ''),
        'user': current_user.id
            if current_user.is_authenticated else 'anonymous'
    })


@socketio.on('set-session')
def set_session(data):
    if 'session' in data:
        session['value'] = data['session']
    elif 'user' in data:
        if data['user'] is not None:
            login_user(User(data['user']))
        else:
            logout_user()


if __name__ == '__main__':
    socketio.run(app)



## ... source file continues with no further session examples...

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


## ... source file abbreviated to get to session examples ...


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
                    self.USER_EMAIL_SENDER_EMAIL = default_sender

        if not self.USER_EMAIL_SENDER_NAME:
            self.USER_EMAIL_SENDER_NAME = self.USER_APP_NAME

        if self.USER_USER_SESSION_EXPIRATION:
            app.permanent_session_lifetime = datetime.timedelta(seconds=self.USER_USER_SESSION_EXPIRATION)

            @app.before_request
            def advance_session_timeout():
~~                session.permanent = True    # Timeout after app.permanent_session_lifetime period
~~                session.modified = True     # Advance session timeout each time a user visits a page

        self.login_manager = LoginManager(app)
        self.login_manager.login_view = 'user.login'

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


## ... source file continues with no further session examples...

```


## Example 12 from indico
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
        record.request_id = request.id if has_request_context() else '0' * 16
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


## ... source file abbreviated to get to session examples ...


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
~~        return {'id': session.user.id,
~~                'email': session.user.email,
~~                'name': session.user.full_name}

    def before_request(self, *args, **kwargs):
        super(IndicoSentry, self).before_request()
        if not has_request_context():
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


## ... source file continues with no further session examples...

```


## Example 13 from tedivms-flask
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
    app = Flask(__name__)

    app.config.from_object('app.settings')
    if 'APPLICATION_SETTINGS' in os.environ:
        app.config.from_envvar(os.environ['APPLICATION_SETTINGS'])
    if 'AWS_SECRETS_MANAGER_CONFIG' in os.environ:


## ... source file abbreviated to get to session examples ...


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

    class BeakerSessionInterface(SessionInterface):
        def open_session(self, app, request):
            session = request.environ['beaker.session']
            return session

        def save_session(self, app, session, response):
~~            session.save()

    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.session_interface = BeakerSessionInterface()

    @user_logged_out.connect_via(app)
    def clear_session(sender, user, **extra):
~~        session.clear()


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
    def error_pagenotfound(e):
        return show_error(404, 'Page not found.')

    @app.errorhandler(500)


## ... source file continues with no further session examples...

```


## Example 14 from trape
[trape](https://github.com/jofpin/trape) is a research tool for tracking
people's activities that are logged digitally. The tool uses
[Flask](/flask.html) to create a web front end to view aggregated data
on an individual the application is set to track. The source code is
provided as open source under the MIT license, according to the
[README](https://github.com/jofpin/trape/blob/master/README.md).

[**trape / core / sockets.py**](https://github.com/jofpin/trape/blob/master/./core/sockets.py)

```python
# sockets.py
from socket import gethostname, gethostbyname 
from threading import Lock
~~from flask import Flask, render_template, session, request, json
from flask_socketio import SocketIO, emit, join_room, rooms, disconnect
import core.stats 
import core.user
from user_objects import attacks_hook_message
from core.utils import utils
from core.db import Database
import sys

trape = core.stats.trape
app = core.stats.app

db = Database()

async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

db.sentences_victim('clean_online', None, 2)

def background_thread():
    count = 0

@socketio.on("join", namespace="/trape")
def join(message):
    try:
        join_room(message['room'])
~~        session['receive_count'] = session.get('receive_count', 0) + 1
    except Exception as error:
        pass

@socketio.on("my_room_event", namespace="/trape")
def send_room_message(message):
    try:
~~        session['receive_count'] = session.get('receive_count', 0) + 1
        hookAction = attacks_hook_message(message['data']['type'])
        utils.Go(utils.Color['white'] + "[" + utils.Color['blueBold'] + "@" + utils.Color['white'] + "]" + " " + hookAction + utils.Color['blue'] + message['data']['message'] + utils.Color['white'] + ' in '  + utils.Color['green'] + message['room'] + utils.Color['white'])
        emit('my_response', {'data': message['data'], 'count': session['receive_count']},room = message['room'])
    except Exception as error:
        pass

@socketio.on("disconnect_request", namespace="/trape")
def disconnect_request(d):
    try:
~~        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response', {'data': 'Disconnected!', 'count': session['receive_count']})
        utils.Go(utils.Color['white'] + "[" + utils.Color['redBold'] + "-" + utils.Color['white'] + "]" + utils.Color['red'] + " " + "A victim has closed her connection with the following id:" + " " + utils.Color['green'] + d['vId'] + utils.Color['white'])
        db.sentences_victim('disconnect_victim', d['vId'], 2)
    except Exception as error:
        pass

@socketio.on("error", namespace="/trape")
def socket_def_error(d):
    pass

@socketio.on_error("/trape")
def error_handler(e):
    pass

@app.route("/" + trape.home_path)
def home():
    gMaps_free_api_key = 'AIzaSyBUPHAjZl3n8Eza66ka6B78iVyPteC5MgM'
    if (trape.gmaps != ''):
        gMaps_free_api_key = trape.gmaps

    shorten_api = 'AIzaSyCPzcppCT27KTHnxAIQvYhtvB_l8sKGYBs'

    html = trape.injectCSS_Paths(render_template("home.html", async_mode=socketio.async_mode).replace('[OWN_API_KEY_HERE]', gMaps_free_api_key).replace('[LIBS_SRC]', trape.JSFiles[1]['src']).replace('[TRAPE_SRC]', trape.JSFiles[4]['src']))
    return html


## ... source file continues with no further session examples...

```

