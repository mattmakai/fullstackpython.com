title: flask.sessions BadSignature Example Code
category: page
slug: flask-sessions-badsignature-examples
sortorder: 500021026
toc: False
sidebartitle: flask.sessions BadSignature
meta: Example code for understanding how to use the BadSignature class from the flask.sessions module of the Flask project.


[BadSignature](https://github.com/pallets/flask/blob/master/src/flask/sessions.py)
is a class often imported into [Flask](/flask.html) applications from
the `flask.sessions` module. `BadSignature` is actually defined in the
[itsdangerous](https://github.com/pallets/itsdangerous) project and
imported into Flask sessions for applications to use.

<a href="/flask-sessions-sessioninterface-examples.html">SessionInterface</a>
and
<a href="/flask-sessions-sessionmixin-examples.html">SessionMixin</a>
are a couple of other callables within the `flask.sessions` package that also have code examples.

## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / tokens / serializer.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/tokens/serializer.py)

```python
# serializer.py

from datetime import timedelta

~~from itsdangerous import (BadData, BadSignature, SignatureExpired,
                          TimedJSONWebSignatureSerializer)

from ..core import tokens


_DEFAULT_EXPIRY = timedelta(hours=1)


class FlaskBBTokenSerializer(tokens.TokenSerializer):

    def __init__(self, secret_key, expiry=_DEFAULT_EXPIRY):
        self._serializer = TimedJSONWebSignatureSerializer(
            secret_key, int(expiry.total_seconds())
        )

    def dumps(self, token):
        return self._serializer.dumps(
            {
                'id': token.user_id,
                'op': token.operation,
            }
        )

    def loads(self, raw_token):
        try:
            parsed = self._serializer.loads(raw_token)
        except SignatureExpired:
            raise tokens.TokenError.expired()
~~        except BadSignature:  # pragma: no branch
            raise tokens.TokenError.invalid()
        except BadData:  # pragma: no cover
            raise tokens.TokenError.bad()
        else:
            return tokens.Token(user_id=parsed['id'], operation=parsed['op'])



## ... source file continues with no further BadSignature examples...

```


## Example 2 from flask-base
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

[**flask-base / app / models / user.py**](https://github.com/hack4impact/flask-base/blob/master/app/models/user.py)

```python
# user.py
from flask import current_app
from flask_login import AnonymousUserMixin, UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
~~from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db, login_manager


class Permission:
    GENERAL = 0x01
    ADMINISTER = 0xff


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    index = db.Column(db.String(64))
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.GENERAL, 'main', True),
            'Administrator': (


## ... source file abbreviated to get to BadSignature examples ...



    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=604800):

        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def generate_password_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def confirm_account(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
~~        except (BadSignature, SignatureExpired):
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
~~        except (BadSignature, SignatureExpired):
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        db.session.commit()
        return True

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
~~        except (BadSignature, SignatureExpired):
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        db.session.commit()
        return True

    @staticmethod
    def generate_fake(count=100, **kwargs):
        from sqlalchemy.exc import IntegrityError
        from random import seed, choice
        from faker import Faker

        fake = Faker()
        roles = Role.query.all()

        seed()
        for i in range(count):
            u = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password='password',


## ... source file continues with no further BadSignature examples...

```


## Example 3 from flask-bones
[flask-bones](https://github.com/cburmeister/flask-bones)
([demo](http://flask-bones.herokuapp.com/))
is large scale [Flask](/flask.html) example application built
with [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
([example Blueprint code](/flask-blueprints-blueprint-examples.html)).
This project is provided as open source under the
[MIT license](https://github.com/cburmeister/flask-bones/blob/master/LICENSE).

[**flask-bones / app / auth / views.py**](https://github.com/cburmeister/flask-bones/blob/master/app/auth/views.py)

```python
# views.py
from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask_babel import gettext
from flask_login import login_user, login_required, logout_user
~~from itsdangerous import URLSafeSerializer, BadSignature
from app.extensions import lm
from app.jobs import send_registration_email
from app.user.models import User
from app.user.forms import RegisterUserForm
from .forms import LoginForm
from ..auth import auth


@lm.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash(
            gettext(
                'You were logged in as {username}'.format(
                    username=form.user.username
                ),
            ),


## ... source file abbreviated to get to BadSignature examples ...


            remote_addr=request.remote_addr,
        )

        s = URLSafeSerializer(current_app.secret_key)
        token = s.dumps(user.id)

        send_registration_email.queue(user.id, token)

        flash(
            gettext(
                'Sent verification email to {email}'.format(
                    email=user.email
                )
            ),
            'success'
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@auth.route('/verify/<token>', methods=['GET'])
def verify(token):
    s = URLSafeSerializer(current_app.secret_key)
    try:
        id = s.loads(token)
~~    except BadSignature:
        abort(404)

    user = User.query.filter_by(id=id).first_or_404()
    if user.active:
        abort(404)
    else:
        user.active = True
        user.update()

        flash(
            gettext(
                'Registered user {username}. Please login to continue.'.format(
                    username=user.username
                ),
            ),
            'success'
        )
        return redirect(url_for('auth.login'))



## ... source file continues with no further BadSignature examples...

```


## Example 4 from Flask-Security-Too
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

from flask import _request_ctx_stack, current_app, flash, g, request, session, url_for
from flask.json import JSONEncoder
from flask_login import login_user as _login_user
from flask_login import logout_user as _logout_user
from flask_login import current_user
from flask_login import COOKIE_NAME as REMEMBER_COOKIE_NAME
from flask_principal import AnonymousIdentity, Identity, identity_changed, Need
from flask_wtf import csrf
from wtforms import validators, ValidationError
~~from itsdangerous import BadSignature, SignatureExpired
from werkzeug.local import LocalProxy
from werkzeug.datastructures import MultiDict

from .quart_compat import best
from .signals import user_authenticated

_security = LocalProxy(lambda: current_app.extensions["security"])

_datastore = LocalProxy(lambda: _security.datastore)

_pwd_context = LocalProxy(lambda: _security.pwd_context)

_hashing_context = LocalProxy(lambda: _security.hashing_context)

localize_callback = LocalProxy(lambda: _security.i18n_domain.gettext)

FsPermNeed = partial(Need, "fsperm")
FsPermNeed.__doc__ = """A need with the method preset to `"fsperm"`."""


def _(translate):
    return translate




## ... source file abbreviated to get to BadSignature examples ...


    if config_value("EMAIL_PLAINTEXT"):
        body = _security.render_template("%s/%s.txt" % ctx, **context)
    if config_value("EMAIL_HTML"):
        html = _security.render_template("%s/%s.html" % ctx, **context)

    sender = _security.email_sender
    if isinstance(sender, LocalProxy):
        sender = sender._get_current_object()

    _security._mail_util.send_mail(
        template, subject, recipient, str(sender), body, html, context.get("user", None)
    )


def get_token_status(token, serializer, max_age=None, return_data=False):
    serializer = getattr(_security, serializer + "_serializer")
    max_age = get_max_age(max_age)
    user, data = None, None
    expired, invalid = False, False

    try:
        data = serializer.loads(token, max_age=max_age)
    except SignatureExpired:
        d, data = serializer.loads_unsafe(token)
        expired = True
~~    except (BadSignature, TypeError, ValueError):
        invalid = True

    if data:
        user = _datastore.find_user(fs_uniquifier=data[0])

    expired = expired and (user is not None)

    if return_data:
        return expired, invalid, user, data
    else:
        return expired, invalid, user


def check_and_get_token_status(token, serializer, within=None):
    serializer = getattr(_security, serializer + "_serializer")
    max_age = within.total_seconds()
    data = None
    expired, invalid = False, False

    try:
        data = serializer.loads(token, max_age=max_age)
    except SignatureExpired:
        d, data = serializer.loads_unsafe(token)
        expired = True
~~    except (BadSignature, TypeError, ValueError):
        invalid = True

    return expired, invalid, data


def get_identity_attributes(app=None) -> List:
    app = app or current_app
    iattrs = app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"]
    if iattrs:
        return [[*f][0] for f in iattrs]
    return []


def get_identity_attribute(attr, app=None) -> Dict:
    app = app or current_app
    iattrs = app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"]
    if iattrs:
        details = [
            mapping[attr] for mapping in iattrs if list(mapping.keys())[0] == attr
        ]
        if details:
            return details[0]
    return {}



## ... source file continues with no further BadSignature examples...

```

