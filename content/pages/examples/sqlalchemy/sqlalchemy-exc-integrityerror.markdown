title: sqlalchemy.exc IntegrityError code examples
category: page
slug: sqlalchemy-exc-integrityerror-examples
sortorder: 500031001
toc: False
sidebartitle: sqlalchemy.exc IntegrityError
meta: Python example code for the IntegrityError class from the sqlalchemy.exc module of the SQLAlchemy project.


IntegrityError is a class within the sqlalchemy.exc module of the SQLAlchemy project.


## Example 1 from flask-base
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
from itsdangerous import BadSignature, SignatureExpired
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
                Permission.ADMINISTER,
                'admin',


## ... source file abbreviated to get to IntegrityError examples ...


        db.session.commit()
        return True

    def reset_password(self, token, new_password):
        """Verify the new password for this user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
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
~~        from sqlalchemy.exc import IntegrityError
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
                confirmed=True,
                role=choice(roles),
                **kwargs)
            db.session.add(u)
            try:
                db.session.commit()
~~            except IntegrityError:
                db.session.rollback()

    def __repr__(self):
        return '<User \'%s\'>' % self.full_name()


class AnonymousUser(AnonymousUserMixin):
    def can(self, _):
        return False

    def is_admin(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


## ... source file continues with no further IntegrityError examples...


```


## Example 2 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / asserts.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./asserts.py)

```python
# asserts.py
We can easily test the constraints by assert_* functions::


    from sqlalchemy_utils import (
        assert_nullable,
        assert_non_nullable,
        assert_max_length
    )

    assert_nullable(user, 'name')
    assert_non_nullable(user, 'email')
    assert_max_length(user, 'name', 200)

    # raises AssertionError because the max length of email is 255
    assert_max_length(user, 'email', 300)
"""
from decimal import Decimal

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
~~from sqlalchemy.exc import DataError, IntegrityError


def _update_field(obj, field, value):
    session = sa.orm.object_session(obj)
    column = sa.inspect(obj.__class__).columns[field]
    query = column.table.update().values(**{column.key: value})
    session.execute(query)
    session.flush()


def _expect_successful_update(obj, field, value, reraise_exc):
    try:
        _update_field(obj, field, value)
    except (reraise_exc) as e:
        session = sa.orm.object_session(obj)
        session.rollback()
        assert False, str(e)


def _expect_failing_update(obj, field, value, expected_exc):
    try:
        _update_field(obj, field, value)
    except expected_exc:
        pass


## ... source file abbreviated to get to IntegrityError examples ...


        session = sa.orm.object_session(obj)
        session.rollback()


def _repeated_value(type_):
    if isinstance(type_, ARRAY):
        if isinstance(type_.item_type, sa.Integer):
            return [0]
        elif isinstance(type_.item_type, sa.String):
            return [u'a']
        elif isinstance(type_.item_type, sa.Numeric):
            return [Decimal('0')]
        else:
            raise TypeError('Unknown array item type')
    else:
        return u'a'


def _expected_exception(type_):
    if isinstance(type_, ARRAY):
~~        return IntegrityError
    else:
        return DataError


def assert_nullable(obj, column):
    """
    Assert that given column is nullable. This is checked by running an SQL
    update that assigns given column as None.

    :param obj: SQLAlchemy declarative model object
    :param column: Name of the column
    """
    _expect_successful_update(obj, column, None, IntegrityError)


def assert_non_nullable(obj, column):
    """
    Assert that given column is not nullable. This is checked by running an SQL
    update that assigns given column as None.

    :param obj: SQLAlchemy declarative model object
    :param column: Name of the column
    """
    _expect_failing_update(obj, column, None, IntegrityError)


## ... source file abbreviated to get to IntegrityError examples ...


        _repeated_value(type_) * max_length,
        _expected_exception(type_)
    )
    _expect_failing_update(
        obj,
        column,
        _repeated_value(type_) * (max_length + 1),
        _expected_exception(type_)
    )


def assert_min_value(obj, column, min_value):
    """
    Assert that the given column must have a minimum value of `min_value`.

    :param obj: SQLAlchemy declarative model object
    :param column: Name of the column
    :param min_value: The minimum allowed value for given column
    """
    _expect_successful_update(obj, column, min_value, IntegrityError)
~~    _expect_failing_update(obj, column, min_value - 1, IntegrityError)


def assert_max_value(obj, column, min_value):
    """
    Assert that the given column must have a minimum value of `max_value`.

    :param obj: SQLAlchemy declarative model object
    :param column: Name of the column
    :param max_value: The maximum allowed value for given column
    """
    _expect_successful_update(obj, column, min_value, IntegrityError)
~~    _expect_failing_update(obj, column, min_value + 1, IntegrityError)


## ... source file continues with no further IntegrityError examples...


```

