title: flask.sessions BadSignature code examples
category: page
slug: flask-sessions-badsignature-examples
sortorder: 500021013
toc: False
sidebartitle: flask.sessions BadSignature
meta: Python example code for the BadSignature class from the flask.sessions module of the Flask project.


BadSignature is a class within the flask.sessions module of the Flask project.


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
# -*- coding: utf -*-
"""
    flaskbb.tokens.serializer
    -------------------------

    :copyright: (c) 2018 the FlaskBB Team.
    :license: BSD, see LICENSE for more details
"""

from datetime import timedelta

~~from itsdangerous import (BadData, BadSignature, SignatureExpired,
                          TimedJSONWebSignatureSerializer)

from ..core import tokens


_DEFAULT_EXPIRY = timedelta(hours=1)


class FlaskBBTokenSerializer(tokens.TokenSerializer):
    """
    Default token serializer for FlaskBB. Generates JWTs
    that are time sensitive. By default they will expire after
    1 hour.

    It creates tokens from flaskbb.core.tokens.Token instances
    and creates instances of that class when loading tokens.

    When loading a token, if an error occurs related to the
    token itself, a flaskbb.core.tokens.TokenError will be
    raised. Exceptions not caused by parsing the token
    are simply propagated.

    :str secret_key: The secret key used to sign the tokens
    :timedelta expiry: Expiration of tokens


## ... source file abbreviated to get to BadSignature examples ...


                'op': token.operation,
            }
        )

    def loads(self, raw_token):
        """
        Transforms a JWT into a flaskbb.core.tokens.Token.

        If a token is invalid due to it being malformed,
        tampered with or expired, a flaskbb.core.tokens.TokenError
        is raised. Errors not related to token parsing are
        simply propagated.

        :str raw_token: JWT to be parsed
        :returns flaskbb.core.tokens.Token: Parsed token
        """
        try:
            parsed = self._serializer.loads(raw_token)
        except SignatureExpired:
            raise tokens.TokenError.expired()
~~        except BadSignature:  # pragma: no branch
            raise tokens.TokenError.invalid()
        # ideally we never end up here as BadSignature should
        # catch everything else, however since this is the root
        # exception for itsdangerous we'll catch it down and
        # and re-raise our own
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


        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def generate_email_change_token(self, new_email, expiration=3600):
        """Generate an email change token to email an existing user."""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def generate_password_reset_token(self, expiration=3600):
        """
        Generate a password reset change token to email to an existing user.
        """
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def confirm_account(self, token):
        """Verify that the provided token is for this user's id."""
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
        """Verify the new email for this user."""
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
        """Verify the new password for this user."""
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
        """Generate a number of fake users for testing."""
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


## ... source file continues with no further BadSignature examples...


```

