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


## ... source file continues with no further BadSignature examples...

```

