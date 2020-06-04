title: flask.globals request Python code examples
category: page
slug: flask-globals-request-examples
sortorder: 500021000
toc: False
sidebartitle: flask.globals request
meta: Python example code for the request function from the flask.globals module of the Flask project.


request is a function within the flask.globals module of the Flask project.


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

[**Flask AppBuilder / flask_appbuilder / urltools.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/./urltools.py)

```python
# urltools.py
import re

~~from flask import request


class Stack(object):
    """
        Stack data structure will not insert
        equal sequential data
    """

    def __init__(self, list=None, size=5):
        self.size = size
        self.data = list or []

    def push(self, item):
        if self.data:
            if item != self.data[len(self.data) - 1]:
                self.data.append(item)
        else:
            self.data.append(item)
        if len(self.data) > self.size:
            self.data.pop(0)

    def pop(self):
        if len(self.data) == 0:
            return None


## ... source file abbreviated to get to request examples ...



def get_group_by_args():
    """
        Get page arguments for group by
    """
    group_by = request.args.get("group_by")
    if not group_by:
        group_by = ""
    return group_by


def get_page_args():
    """
        Get page arguments, returns a dictionary
        { <VIEW_NAME>: PAGE_NUMBER }

        Arguments are passed: page_<VIEW_NAME>=<PAGE_NUMBER>

    """
    pages = {}
~~    for arg in request.args:
        re_match = re.findall("page_(.*)", arg)
        if re_match:
~~            pages[re_match[0]] = int(request.args.get(arg))
    return pages


def get_page_size_args():
    """
        Get page size arguments, returns an int
        { <VIEW_NAME>: PAGE_NUMBER }

        Arguments are passed: psize_<VIEW_NAME>=<PAGE_SIZE>

    """
    page_sizes = {}
~~    for arg in request.args:
        re_match = re.findall("psize_(.*)", arg)
        if re_match:
~~            page_sizes[re_match[0]] = int(request.args.get(arg))
    return page_sizes


def get_order_args():
    """
        Get order arguments, return a dictionary
        { <VIEW_NAME>: (ORDER_COL, ORDER_DIRECTION) }

        Arguments are passed like: _oc_<VIEW_NAME>=<COL_NAME>&_od_<VIEW_NAME>='asc'|'desc'

    """
    orders = {}
~~    for arg in request.args:
        re_match = re.findall("_oc_(.*)", arg)
        if re_match:
~~            order_direction = request.args.get("_od_" + re_match[0])
            if order_direction in ("asc", "desc"):
~~                orders[re_match[0]] = (request.args.get(arg), order_direction)
    return orders


def get_filter_args(filters):
    filters.clear_filters()
~~    for arg in request.args:
        re_match = re.findall("_flt_(\d)_(.*)", arg)
        if re_match:
            filters.add_filter_index(
~~                re_match[0][1], int(re_match[0][0]), request.args.get(arg)
            )


## ... source file continues with no further request examples...


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
# -*- coding: utf-8 -*-
"""
    flaskbb.app
    -----------

    manages the app creation and configuration process

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
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
# extensions
from flaskbb.extensions import (alembic, allows, babel, cache, celery, csrf,
                                db, debugtoolbar, limiter, login_manager, mail,
                                redis_store, themes, whooshee)
from flaskbb.plugins import spec
from flaskbb.plugins.manager import FlaskBBPluginManager
from flaskbb.plugins.models import PluginRegistry
from flaskbb.plugins.utils import remove_zombie_plugins_from_db, template_hook
# models
from flaskbb.user.models import Guest, User
# various helpers
from flaskbb.utils.helpers import (app_config_from_env, crop_title,
                                   format_date, format_datetime,
                                   forum_is_unread, get_alembic_locations,
                                   get_flaskbb_config, is_online, mark_online,
                                   render_template, time_since, time_utcnow,
                                   topic_is_unread)
# permission checks (here they are used for the jinja filters)


## ... source file abbreviated to get to request examples ...



def configure_before_handlers(app):
    """Configures the before request handlers."""

    @app.before_request
    def update_lastseen():
        """Updates `lastseen` before every reguest if the user is
        authenticated."""
        if current_user.is_authenticated:
            current_user.lastseen = time_utcnow()
            db.session.add(current_user)
            db.session.commit()

    if app.config["REDIS_ENABLED"]:

        @app.before_request
        def mark_current_user_online():
            if current_user.is_authenticated:
                mark_online(current_user.username)
            else:
~~                mark_online(request.remote_addr, guest=True)

    app.pluggy.hook.flaskbb_request_processors(app=app)


def configure_errorhandlers(app):
    """Configures the error handlers."""

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/forbidden_page.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/page_not_found.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/server_error.html"), 500

    app.pluggy.hook.flaskbb_errorhandlers(app=app)


def configure_migrations(app):
    """Configure migrations."""


## ... source file continues with no further request examples...


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
    if not session.get('logged_in'):
~~        form = forms.LoginForm(request.form)
~~        if request.method == 'POST':
~~            username = request.form['username'].lower()
~~            password = request.form['password']
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
    if not session.get('logged_in'):
~~        form = forms.LoginForm(request.form)
~~        if request.method == 'POST':
~~            username = request.form['username'].lower()
~~            password = helpers.hash_password(request.form['password'])
~~            email = request.form['email']
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
    if session.get('logged_in'):
~~        if request.method == 'POST':
~~            password = request.form['password']
            if password != "":
                password = helpers.hash_password(password)
~~            email = request.form['email']
            helpers.change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")


## ... source file continues with no further request examples...


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


## ... source file abbreviated to get to request examples ...


    l_url = urlparse(login_url)
    c_url = urlparse(current_url)

    if (not l_url.scheme or l_url.scheme == c_url.scheme) and \
            (not l_url.netloc or l_url.netloc == c_url.netloc):
        return urlunparse(('', '', c_url.path, c_url.params, c_url.query, ''))
    return current_url


def expand_login_view(login_view):
    '''
    Returns the url for the login view, expanding the view name to a url if
    needed.

    :param login_view: The name of the login view or a URL for the login view.
    :type login_view: str
    '''
    if login_view.startswith(('https://', 'http://', '/')):
        return login_view
    else:
~~        if request.view_args is None:
            return url_for(login_view)
        else:
~~            return url_for(login_view, **request.view_args)


def login_url(login_view, next_url=None, next_field='next'):
    '''
    Creates a URL for redirecting to a login page. If only `login_view` is
    provided, this will just return the URL for it. If `next_url` is provided,
    however, this will append a ``next=URL`` parameter to the query string
    so that the login view can redirect back to that URL. Flask-Login's default
    unauthorized handler uses this function when redirecting to your login url.
    To force the host name used, set `FORCE_HOST_FOR_REDIRECTS` to a host. This
    prevents from redirecting to external sites if request headers Host or
    X-Forwarded-For are present.

    :param login_view: The name of the login view. (Alternately, the actual
                       URL to the login view.)
    :type login_view: str
    :param next_url: The URL to give the login view for redirection.
    :type next_url: str
    :param next_field: What field to store the next URL in. (It defaults to
                       ``next``.)
    :type next_field: str
    '''
    base = expand_login_view(login_view)



## ... source file abbreviated to get to request examples ...




def logout_user():
    '''
    Logs a user out. (You do not need to pass the actual user.) This will
    also clean up the remember me cookie if it exists.
    '''

    user = _get_user()

    if '_user_id' in session:
        session.pop('_user_id')

    if '_fresh' in session:
        session.pop('_fresh')

    if '_id' in session:
        session.pop('_id')

    cookie_name = current_app.config.get('REMEMBER_COOKIE_NAME', COOKIE_NAME)
~~    if cookie_name in request.cookies:
        session['_remember'] = 'clear'
        if '_remember_seconds' in session:
            session.pop('_remember_seconds')

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


## ... source file abbreviated to get to request examples ...


        if not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()

    ...which is essentially the code that this function adds to your views.

    It can be convenient to globally turn off authentication when unit testing.
    To enable this, if the application configuration variable `LOGIN_DISABLED`
    is set to `True`, this decorator will be ignored.

    .. Note ::

        Per `W3 guidelines for CORS preflight requests
        <http://www.w3.org/TR/cors/#cross-origin-request-with-preflight-0>`_,
        HTTP ``OPTIONS`` requests are exempt from login checks.

    :param func: The view function to decorate.
    :type func: function
    '''
    @wraps(func)
    def decorated_view(*args, **kwargs):
~~        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view


def fresh_login_required(func):
    '''
    If you decorate a view with this, it will ensure that the current user's
    login is fresh - i.e. their session was not restored from a 'remember me'
    cookie. Sensitive operations, like changing a password or e-mail, should
    be protected with this, to impede the efforts of cookie thieves.

    If the user is not authenticated, :meth:`LoginManager.unauthorized` is
    called as normal. If they are authenticated, but their session is not
    fresh, it will call :meth:`LoginManager.needs_refresh` instead. (In that
    case, you will need to provide a :attr:`LoginManager.refresh_view`.)

    Behaves identically to the :func:`login_required` decorator with respect
    to configuration variables.

    .. Note ::

        Per `W3 guidelines for CORS preflight requests
        <http://www.w3.org/TR/cors/#cross-origin-request-with-preflight-0>`_,
        HTTP ``OPTIONS`` requests are exempt from login checks.

    :param func: The view function to decorate.
    :type func: function
    '''
    @wraps(func)
    def decorated_view(*args, **kwargs):
~~        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not login_fresh():
            return current_app.login_manager.needs_refresh()
        return func(*args, **kwargs)
    return decorated_view


def set_login_view(login_view, blueprint=None):
    '''
    Sets the login view for the app or blueprint. If a blueprint is passed,
    the login view is set for this blueprint on ``blueprint_login_views``.

    :param login_view: The user object to log in.
    :type login_view: str
    :param blueprint: The blueprint which this login view should be set on.
        Defaults to ``None``.
    :type blueprint: object
    '''

    num_login_views = len(current_app.login_manager.blueprint_login_views)


## ... source file abbreviated to get to request examples ...



        current_app.login_manager.login_view = None
    else:
        current_app.login_manager.login_view = login_view


def _get_user():
    if has_request_context() and not hasattr(_request_ctx_stack.top, 'user'):
        current_app.login_manager._load_user()

    return getattr(_request_ctx_stack.top, 'user', None)


def _cookie_digest(payload, key=None):
    key = _secret_key(key)

    return hmac.new(key, payload.encode('utf-8'), sha512).hexdigest()


def _get_remote_addr():
~~    address = request.headers.get('X-Forwarded-For', request.remote_addr)
    if address is not None:
        # An 'X-Forwarded-For' header includes a comma separated list of the
        # addresses, the first address being the actual remote address.
        address = address.encode('utf-8').split(b',')[0].strip()
    return address


def _create_identifier():
~~    user_agent = request.headers.get('User-Agent')
    if user_agent is not None:
        user_agent = user_agent.encode('utf-8')
    base = '{0}|{1}'.format(_get_remote_addr(), user_agent)
    if str is bytes:
        base = text_type(base, 'utf-8', errors='replace')  # pragma: no cover
    h = sha512()
    h.update(base.encode('utf8'))
    return h.hexdigest()


def _user_context_processor():
    return dict(current_user=_get_user())


def _secret_key(key=None):
    if key is None:
        key = current_app.config['SECRET_KEY']

    if isinstance(key, text_type):  # pragma: no cover
        key = key.encode('latin1')  # ensure bytes

    return key


## ... source file continues with no further request examples...


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

[**flask-restx / flask_restx / marshalling.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./marshalling.py)

```python
# marshalling.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict
from functools import wraps
from six import iteritems

~~from flask import request, current_app, has_app_context

from .mask import Mask, apply as apply_mask
from .utils import unpack


def make(cls):
    if isinstance(cls, type):
        return cls()
    return cls


def marshal(data, fields, envelope=None, skip_none=False, mask=None, ordered=False):
    """Takes raw data (in the form of a dict, list, object) and a dict of
    fields to output and filters the data based on those fields.

    :param data: the actual object(s) from which the fields are taken from
    :param fields: a dict of whose keys will make up the final serialized
                   response output
    :param envelope: optional key that will be used to envelop the serialized
                     response
    :param bool skip_none: optional key will be used to eliminate fields
                           which value is None or the field's key not
                           exist in data
    :param bool ordered: Wether or not to preserve order


## ... source file abbreviated to get to request examples ...


    ):
        """
        :param fields: a dict of whose keys will make up the final
                       serialized response output
        :param envelope: optional key that will be used to envelop the serialized
                         response
        """
        self.fields = fields
        self.envelope = envelope
        self.skip_none = skip_none
        self.ordered = ordered
        self.mask = Mask(mask, skip=True)

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            mask = self.mask
            if has_app_context():
                mask_header = current_app.config["RESTX_MASK_HEADER"]
~~                mask = request.headers.get(mask_header) or mask
            if isinstance(resp, tuple):
                data, code, headers = unpack(resp)
                return (
                    marshal(
                        data,
                        self.fields,
                        self.envelope,
                        self.skip_none,
                        mask,
                        self.ordered,
                    ),
                    code,
                    headers,
                )
            else:
                return marshal(
                    resp, self.fields, self.envelope, self.skip_none, mask, self.ordered
                )

        return wrapper


class marshal_with_field(object):
    """


## ... source file continues with no further request examples...


```


## Example 6 from flask-sqlalchemy
[flask-sqlalchemy](https://github.com/pallets/flask-sqlalchemy)
([project documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
and
[PyPI information](https://pypi.org/project/Flask-SQLAlchemy/)) is a
[Flask](/flask.html) extension that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) when building Flask apps. flask-sqlalchemy
provides helper functions that reduce the amount of common boilerplate
code that you have to frequently write yourself if you did not use this
library when combining Flask with SQLAlchemy.

flask-sqlalchemy is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/pallets/flask-sqlalchemy/blob/master/LICENSE.rst).

[**flask-sqlalchemy / src/flask_sqlalchemy / __init__.py**](https://github.com/pallets/flask-sqlalchemy/blob/master/src/flask_sqlalchemy/./__init__.py)

```python
# __init__.py
import functools
import os
import sys
import warnings
from math import ceil
from operator import itemgetter
from threading import Lock
from time import perf_counter

import sqlalchemy
from flask import _app_ctx_stack
from flask import abort
from flask import current_app
~~from flask import request
from flask.signals import Namespace
from sqlalchemy import event
from sqlalchemy import inspect
from sqlalchemy import orm
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.orm.session import Session as SessionBase

from .model import DefaultMeta
from .model import Model

__version__ = "3.0.0.dev"

_signals = Namespace()
models_committed = _signals.signal("models-committed")
before_models_committed = _signals.signal("before-models-committed")


def _make_table(db):
    def _make_table(*args, **kwargs):
        if len(args) > 1 and isinstance(args[1], db.Column):
            args = (args[0], db.metadata) + args[1:]


## ... source file abbreviated to get to request examples ...



        If ``page`` or ``per_page`` are ``None``, they will be retrieved from
        the request query. If ``max_per_page`` is specified, ``per_page`` will
        be limited to that value. If there is no request or they aren't in the
        query, they default to 1 and 20 respectively. If ``count`` is ``False``,
        no query to help determine total page count will be run.

        When ``error_out`` is ``True`` (default), the following rules will
        cause a 404 response:

        * No items are found and ``page`` is not 1.
        * ``page`` is less than 1, or ``per_page`` is negative.
        * ``page`` or ``per_page`` are not ints.

        When ``error_out`` is ``False``, ``page`` and ``per_page`` default to
        1 and 20 respectively.

        Returns a :class:`Pagination` object.
        """

~~        if request:
            if page is None:
                try:
~~                    page = int(request.args.get("page", 1))
                except (TypeError, ValueError):
                    if error_out:
                        abort(404)

                    page = 1

            if per_page is None:
                try:
~~                    per_page = int(request.args.get("per_page", 20))
                except (TypeError, ValueError):
                    if error_out:
                        abort(404)

                    per_page = 20
        else:
            if page is None:
                page = 1

            if per_page is None:
                per_page = 20

        if max_per_page is not None:
            per_page = min(per_page, max_per_page)

        if page < 1:
            if error_out:
                abort(404)
            else:
                page = 1

        if per_page < 0:
            if error_out:
                abort(404)


## ... source file continues with no further request examples...


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
    """Generate a CSRF token. The token is cached for a request, so multiple
    calls to this function will generate the same token.

    During testing, it might be useful to access the signed token in
    ``g.csrf_token`` and the raw token in ``session['csrf_token']``.

    :param secret_key: Used to securely sign the token. Default is
        ``WTF_CSRF_SECRET_KEY`` or ``SECRET_KEY``.
    :param token_key: Key where token is stored in session for comparison.
        Default is ``WTF_CSRF_FIELD_NAME`` or ``'csrf_token'``.
    """


## ... source file abbreviated to get to request examples ...


            'WTF_CSRF_METHODS', ['POST', 'PUT', 'PATCH', 'DELETE']
        ))
        app.config.setdefault('WTF_CSRF_FIELD_NAME', 'csrf_token')
        app.config.setdefault(
            'WTF_CSRF_HEADERS', ['X-CSRFToken', 'X-CSRF-Token']
        )
        app.config.setdefault('WTF_CSRF_TIME_LIMIT', 3600)
        app.config.setdefault('WTF_CSRF_SSL_STRICT', True)

        app.jinja_env.globals['csrf_token'] = generate_csrf
        app.context_processor(lambda: {'csrf_token': generate_csrf})

        @app.before_request
        def csrf_protect():
            if not app.config['WTF_CSRF_ENABLED']:
                return

            if not app.config['WTF_CSRF_CHECK_DEFAULT']:
                return

~~            if request.method not in app.config['WTF_CSRF_METHODS']:
                return

~~            if not request.endpoint:
                return

~~            if request.blueprint in self._exempt_blueprints:
                return

~~            view = app.view_functions.get(request.endpoint)
            dest = '{0}.{1}'.format(view.__module__, view.__name__)

            if dest in self._exempt_views:
                return

            self.protect()

    def _get_csrf_token(self):
        # find the token in the form data
        field_name = current_app.config['WTF_CSRF_FIELD_NAME']
~~        base_token = request.form.get(field_name)

        if base_token:
            return base_token

        # if the form has a prefix, the name will be {prefix}-csrf_token
~~        for key in request.form:
            if key.endswith(field_name):
~~                csrf_token = request.form[key]

                if csrf_token:
                    return csrf_token

        # find the token in the headers
        for header_name in current_app.config['WTF_CSRF_HEADERS']:
~~            csrf_token = request.headers.get(header_name)

            if csrf_token:
                return csrf_token

        return None

    def protect(self):
~~        if request.method not in current_app.config['WTF_CSRF_METHODS']:
            return

        try:
            validate_csrf(self._get_csrf_token())
        except ValidationError as e:
            logger.info(e.args[0])
            self._error_response(e.args[0])

~~        if request.is_secure and current_app.config['WTF_CSRF_SSL_STRICT']:
~~            if not request.referrer:
                self._error_response('The referrer header is missing.')

~~            good_referrer = 'https://{0}/'.format(request.host)

~~            if not same_origin(request.referrer, good_referrer):
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

            bp = Blueprint(...)
            csrf.exempt(bp)

        """

        if isinstance(view, Blueprint):
            self._exempt_blueprints.add(view.name)
            return view


## ... source file continues with no further request examples...


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

[**flaskSaaS / app / admin.py**](https://github.com/alectrocute/flaskSaaS/blob/master/app/./admin.py)

```python
# admin.py
import os.path as op

~~from flask import request, Response
from werkzeug.exceptions import HTTPException
from flask_admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin

from app import app, db
from app.models import User


admin = Admin(app, name='Admin', template_mode='bootstrap3')

class ModelView(ModelView):

    def is_accessible(self):
~~        auth = request.authorization or request.environ.get('REMOTE_USER')  # workaround for Apache
        if not auth or (auth.username, auth.password) != app.config['ADMIN_CREDENTIALS']:
            raise HTTPException('', Response('You have to an administrator.', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            ))
        return True

# Users
admin.add_view(ModelView(User, db.session))

# Static files
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static'))


## ... source file continues with no further request examples...


```


## Example 9 from newspie
[NewsPie](https://github.com/skamieniarz/newspie) is a minimalistic news
aggregator created with [Flask](/flask.html) and the
[News API](https://newsapi.org/).

NewsPie is provided as open source under the
[MIT license](https://github.com/skamieniarz/newspie/blob/master/LICENSE).

[**newspie / news.py**](https://github.com/skamieniarz/newspie/blob/master/././news.py)

```python
# news.py
# -*- coding: utf-8 -*-
'''
NewsPie - a minimalistic news aggregator built with Flask and powered by
News API (https://newsapi.org/).

Created by @skamieniarz (https://github.com/skamieniarz) in 2019.
'''
import configparser
import json
import logging
import os

import requests
import requests_cache
from dateutil import parser
~~from flask import (Flask, make_response, redirect, render_template, request,
                   url_for)

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
API_KEY = os.environ.get('NEWS_API_KEY')
TOP_HEADLINES = CONFIG['ENDPOINTS']['TOP_HEADLINES']
EVERYTHING = CONFIG['ENDPOINTS']['EVERYTHING']
PAGE_SIZE = int(CONFIG['VARIOUS']['PAGE_SIZE'])

CATEGORIES = ('general', 'sports', 'business', 'entertainment', 'health',
              'science', 'technology')
with open('data/countries.json') as json_file:
    COUNTRIES = json.load(json_file)

logging.basicConfig(level=logging.DEBUG)
requests_cache.install_cache(cache_name='news_cache',
                             backend='sqlite',
                             expire_after=300)

APP = Flask(__name__)


@APP.route('/', methods=['GET', 'POST'])
def root():


## ... source file abbreviated to get to request examples ...




@APP.errorhandler(404)
def page_not_found(error):
    ''' Not existing pages redirect to the first page of general category. '''
    return redirect(url_for('category', category='general', page=1))


@APP.route('/category/<string:category>', methods=['GET', 'POST'])
def category(category):
    ''' Handles category route.

    Parameters:
        - name: category
          in: path
          description: Name of the news category
        - name: page
          in: query
          description: Number of the page
    '''
~~    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('category', category=category, page=1))
~~    if request.method == 'POST' and category in CATEGORIES:
        return do_post(page, category)
    if category in CATEGORIES:
        params = {'page': page, 'category': category, 'pageSize': PAGE_SIZE}
        country = get_cookie('country')
        if country is not None:
            params.update({'country': country})
        response = requests.get(TOP_HEADLINES,
                                params=params,
                                headers={'Authorization': API_KEY})
        if response.status_code == 200:
            pages = count_pages(response.json())
            if page > pages:
                page = pages
                return redirect(url_for('category', category=category, page=page))
            articles = parse_articles(response.json())
            return render(articles, page, pages, country, category)
        elif response.status_code == 401:
            return render_template(CONFIG['VARIOUS']['401_TEMPLATE'])
    return redirect(url_for('category', category='general', page=page))


@APP.route('/search/<string:query>', methods=['GET', 'POST'])
def search(query):
    ''' Handles category route.

    Parameters:
        - name: query
          in: path
          description: Query string to be searched
        - name: page
          in: query
          description: Number of the page
    '''
~~    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('search', query=query, page=1))
    params = {
        'qInTitle': query,
        'sortBy': 'relevancy',
        'page': page,
        'pageSize': PAGE_SIZE
    }
~~    if request.method == 'POST':
        return do_post(page, category='search', current_query=query)
    response = requests.get(EVERYTHING,
                            params=params,
                            headers={'Authorization': API_KEY})
    pages = count_pages(response.json())
    if page > pages:
        page = pages
        return redirect(url_for('search', query=query, page=page))
    articles = parse_articles(response.json())
    return render(articles,
                  page,
                  pages,
                  country=get_cookie('country'),
                  category='search')


def do_post(page, category='general', current_query=None):
    ''' Helper method that handles POST request basing on the input. '''
~~    new_query = request.form.get('search_query')
~~    country = request.form.get('country')
~~    next_page = request.form.get('next_page')
~~    previous_page = request.form.get('previous_page')
    if new_query is not None and new_query != '':
        return redirect(url_for('search', query=new_query, page=1))
    if country is not None and country != get_cookie('country'):
        response = make_response(
            redirect(url_for('category', category=category, page=1)))
        response.set_cookie('country', country)
        return response
    if next_page is not None:
        page = int(next_page) + 1
    elif previous_page is not None:
        page = int(previous_page) - 1
    if category == 'search':
        return redirect(url_for('search', query=current_query, page=page))
    return redirect(url_for('category', category=category, page=page))


def parse_articles(response):
    ''' Parses articles fetched from News API.

    Returns:
        A list of dicts containing publishing date, title, URL and source of
        articles.
    '''
    parsed_articles = []


## ... source file abbreviated to get to request examples ...


    ''' Renders the template with appropriate variables. Up to 12 pages
        allowed. '''
    pages = pages if pages <= 12 else 12
    return render_template(CONFIG['VARIOUS']['TEMPLATE'],
                           articles=articles,
                           categories=CATEGORIES,
                           category=category,
                           countries=COUNTRIES,
                           country=country,
                           page=page,
                           pages=pages)


def get_cookie(key):
    ''' Helper method that gets cookie's value.

    Returns:
        A string with a value of a cookie with provided key. If a key is
        missing, None is returned.
    '''
~~    cookie_value = request.cookies.get(key)
    return cookie_value


if __name__ == '__main__':
    APP.run()


## ... source file continues with no further request examples...


```


## Example 10 from sandman2
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

[**sandman2 / sandman2 / service.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./service.py)

```python
# service.py
"""Automatically generated REST API services from SQLAlchemy
ORM models or a database introspection."""

# Third-party imports
~~from flask import request, make_response
import flask
from flask.views import MethodView
from sqlalchemy import asc, desc

# Application imports
from sandman2.exception import NotFoundException, BadRequestException
from sandman2.model import db
from sandman2.decorators import etag, validate_fields


def add_link_headers(response, links):
    """Return *response* with the proper link headers set, based on the contents
    of *links*.

    :param response: :class:`flask.Response` response object for links to be
                     added
    :param dict links: Dictionary of links to be added
    :rtype :class:`flask.Response` :
    """
    link_string = '<{}>; rel=self'.format(links['self'])
    for link in links.values():
        link_string += ', <{}>; rel=related'.format(link)
    response.headers['Link'] = link_string
    return response


def jsonify(resource):
    """Return a Flask ``Response`` object containing a
    JSON representation of *resource*.

    :param resource: The resource to act as the basis of the response
    """

    response = flask.jsonify(resource.to_dict())
    response = add_link_headers(response, resource.links())
    return response


def is_valid_method(model, resource=None):
    """Return the error message to be sent to the client if the current
    request passes fails any user-defined validation."""
    validation_function_name = 'is_valid_{}'.format(
~~        request.method.lower())
    if hasattr(model, validation_function_name):
        return getattr(model, validation_function_name)(request, resource)

class Service(MethodView):

    """The *Service* class is a generic extension of Flask's *MethodView*,
    providing default RESTful functionality for a given ORM resource.

    Each service has an associated *__model__* attribute which represents the
    ORM resource it exposes. Services are JSON-only. HTML-based representation
    is available through the admin interface.
    """

    #: The sandman2.model.Model-derived class to expose
    __model__ = None

    #: The string used to describe the elements when a collection is
    #: returned.
    __json_collection_name__ = 'resources'

    def delete(self, resource_id):
        """Return an HTTP response object resulting from a HTTP DELETE call.

        :param resource_id: The value of the resource's primary key


## ... source file abbreviated to get to request examples ...


        db.session().commit()
        return self._no_content_response()

    @etag
    def get(self, resource_id=None):
        """Return an HTTP response object resulting from an HTTP GET call.

        If *resource_id* is provided, return just the single resource.
        Otherwise, return the full collection.

        :param resource_id: The value of the resource's primary key
        """
        if request.path.endswith('meta'):
            return self._meta()

        if resource_id is None:
            error_message = is_valid_method(self.__model__)
            if error_message:
                raise BadRequestException(error_message)

~~            if 'export' in request.args: 
                return self._export(self._all_resources())

            return flask.jsonify({
                self.__json_collection_name__: self._all_resources()
                })
        else:
            resource = self._resource(resource_id)
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
            return jsonify(resource)

    def patch(self, resource_id):
        """Return an HTTP response object resulting from an HTTP PATCH call.

        :returns: ``HTTP 200`` if the resource already exists
        :returns: ``HTTP 400`` if the request is malformed
        :returns: ``HTTP 404`` if the resource is not found
        :param resource_id: The value of the resource's primary key
        """
        resource = self._resource(resource_id)
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
~~        if not request.json:
            raise BadRequestException('No JSON data received')
~~        resource.update(request.json)
        db.session().merge(resource)
        db.session().commit()
        return jsonify(resource)

    @validate_fields
    def post(self):
        """Return the JSON representation of a new resource created through
        an HTTP POST call.

        :returns: ``HTTP 201`` if a resource is properly created
        :returns: ``HTTP 204`` if the resource already exists
        :returns: ``HTTP 400`` if the request is malformed or missing data
        """
        resource = self.__model__.query.filter_by(**request.json).first()
        if resource:
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
            return self._no_content_response()

~~        resource = self.__model__(**request.json)  # pylint: disable=not-callable
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().add(resource)
        db.session().commit()
        return self._created_response(resource)

    def put(self, resource_id):
        """Return the JSON representation of a new resource created or updated
        through an HTTP PUT call.

        If resource_id is not provided, it is assumed the primary key field is
        included and a totally new resource is created. Otherwise, the existing
        resource referred to by *resource_id* is updated with the provided JSON
        data. This method is idempotent.

        :returns: ``HTTP 201`` if a new resource is created
        :returns: ``HTTP 200`` if a resource is updated
        :returns: ``HTTP 400`` if the request is malformed or missing data
        """
        resource = self.__model__.query.get(resource_id)
        if resource:
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
~~            resource.update(request.json)
            db.session().merge(resource)
            db.session().commit()
            return jsonify(resource)

~~        resource = self.__model__(**request.json)  # pylint: disable=not-callable
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().add(resource)
        db.session().commit()
        return self._created_response(resource)

    def _meta(self):
        """Return a description of this resource as reported by the
        database."""
        return flask.jsonify(self.__model__.description())

    def _resource(self, resource_id):
        """Return the ``sandman2.model.Model`` instance with the given
        *resource_id*.

        :rtype: :class:`sandman2.model.Model`
        """
        resource = self.__model__.query.get(resource_id)
        if not resource:
            raise NotFoundException()
        return resource

    def _all_resources(self):
        """Return the complete collection of resources as a list of
        dictionaries.

        :rtype: :class:`sandman2.model.Model`
        """
        queryset = self.__model__.query
~~        args = {k: v for (k, v) in request.args.items() if k not in ('page', 'export')}
        limit = None
        if args:
            filters = []
            order = []
            for key, value in args.items():
                if value.startswith('%'):
                    filters.append(getattr(self.__model__, key).like(str(value), escape='/'))
                elif key == 'sort':
                    direction = desc if value.startswith('-') else asc
                    order.append(direction(getattr(self.__model__, value.lstrip('-'))))
                elif key == 'limit':
                    limit = int(value)
                elif hasattr(self.__model__, key):
                    filters.append(getattr(self.__model__, key) == value)
                else:
                    raise BadRequestException('Invalid field [{}]'.format(key))
            queryset = queryset.filter(*filters).order_by(*order)
~~        if 'page' in request.args:
~~            resources = queryset.paginate(page=int(request.args['page']), per_page=limit).items
        else:
            queryset = queryset.limit(limit)
            resources = queryset.all()
        return [r.to_dict() for r in resources]

    def _export(self, collection):
        """Return a CSV of the resources in *collection*.

        :param list collection: A list of resources represented by dicts
        """
        fieldnames = collection[0].keys()
        faux_csv = ','.join(fieldnames) + '\r\n'
        for resource in collection:
            faux_csv += ','.join((str(x) for x in resource.values())) + '\r\n'
        response = make_response(faux_csv)
        response.mimetype = 'text/csv'
        return response


    @staticmethod
    def _no_content_response():
        """Return an HTTP 204 "No Content" response.

        :returns: HTTP Response


## ... source file continues with no further request examples...


```


## Example 11 from tedivms-flask
[tedivm's flask starter app](https://github.com/tedivm/tedivms-flask) is a
base of [Flask](/flask.html) code and related projects such as
[Celery](/celery.html) which provides a template to start your own
Flask web app. The project comes baked with an admin panel,
[API authentication and authorization](/application-programming-interfaces.html),
[SQLAlchemy](/sqlalchemy.html) and many other common libraries that are
often used with Flask.

The project's code is provided as open source under the
[BSD 2-Clause "Simplified" license](https://github.com/tedivm/tedivms-flask/blob/master/LICENSE.txt).

[**tedivms-flask / app / utils / api.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/utils/api.py)

```python
# api.py
from app.models import user_models as users
from functools import wraps
~~from flask import request, abort, current_app


def is_authorized_api_user(roles=False):
    """Verify API Token and its owners permission to use it"""
~~    if 'API_ID' not in request.headers:
        return False
~~    if 'API_KEY' not in request.headers:
        return False
~~    api_key = users.ApiKey.query.filter(users.ApiKey.id==request.headers['API_ID']).first()
    if not api_key:
        return False
~~    if not current_app.user_manager.verify_password(request.headers['API_KEY'], api_key.hash):
        return False
    if not roles:
        return True
    if api_key.user.has_role('admin'):
        return True
    for role in roles:
        if api_key.user.has_role(role):
            return True
    return False


def roles_accepted_api(*role_names):
    def wrapper(view_function):
        @wraps(view_function)
        def decorated_view_function(*args, **kwargs):
            if not is_authorized_api_user(role_names):
                return abort(403)
            return view_function(*args, **kwargs)
        return decorated_view_function
    return wrapper


def api_credentials_required():
    def wrapper(view_function):


## ... source file continues with no further request examples...


```

