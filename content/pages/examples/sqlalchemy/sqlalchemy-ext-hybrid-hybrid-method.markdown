title: sqlalchemy.ext.hybrid hybrid_method Example Code
category: page
slug: sqlalchemy-ext-hybrid-hybrid-method-examples
sortorder: 500031050
toc: False
sidebartitle: sqlalchemy.ext.hybrid hybrid_method
meta: Python example code that shows how to use the hybrid_method callable from the sqlalchemy.ext.hybrid module of the SQLAlchemy project.


`hybrid_method` is a callable within the `sqlalchemy.ext.hybrid` module of the SQLAlchemy project.

<a href="/sqlalchemy-ext-hybrid-hybrid-property-examples.html">HYBRID_PROPERTY</a>,
<a href="/sqlalchemy-ext-hybrid-hybrid-method-examples.html">hybrid_method</a>,
and <a href="/sqlalchemy-ext-hybrid-hybrid-property-examples.html">hybrid_property</a>
are several other callables with code examples from the same `sqlalchemy.ext.hybrid` package.

## Example 1 from SQLAlchemy Mixins
[SQLAlchemy Mixins](https://github.com/absent1706/sqlalchemy-mixins)
([PyPI package information](https://pypi.org/project/sqlalchemy-mixins/))
is a collection of
[mixins](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
useful for extending [SQLAlchemy](/sqlalchemy.html) and simplifying
your [database](/databases.html)-interacting code for some common
use cases. SQLAlchemy Mixins is open sourced under the
[MIT license](https://github.com/absent1706/sqlalchemy-mixins/blob/master/LICENSE.txt).

[**SQLAlchemy Mixins / sqlalchemy_mixins / tests / test_smartquery.py**](https://github.com/absent1706/sqlalchemy-mixins/blob/master/sqlalchemy_mixins/tests/test_smartquery.py)

```python
# test_smartquery.py
import unittest
import datetime

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
~~from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm import Session
from sqlalchemy_mixins import SmartQueryMixin, smart_query
from sqlalchemy_mixins.eagerload import JOINED, SUBQUERY

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=False)

sess = Session(engine)


class BaseModel(Base, SmartQueryMixin):
    __abstract__ = True
    pass


class User(BaseModel):
    __tablename__ = 'user'
    __repr_attrs__ = ['name']
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)

    posts = sa.orm.relationship('Post')
    comments = sa.orm.relationship('Comment')


class Post(BaseModel):
    __tablename__ = 'post'
    id = sa.Column(sa.Integer, primary_key=True)
    body = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    archived = sa.Column(sa.Boolean, default=False)

    user = sa.orm.relationship('User')
    comments = sa.orm.relationship('Comment')

    @hybrid_property
    def public(self):
        return not self.archived

    @public.expression
    def public(cls):
        return -cls.archived

~~    @hybrid_method
    def is_commented_by_user(cls, user, mapper=None):
        mapper = mapper or cls
        return mapper.comments.any(Comment.user_id == user.id)

~~    @hybrid_method
    def is_public(cls, value, mapper=None):
        mapper = mapper or cls
        return mapper.public == value


class Comment(BaseModel):
    __tablename__ = 'comment'
    __repr_attrs__ = ['body']
    id = sa.Column(sa.Integer, primary_key=True)
    body = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    post_id = sa.Column(sa.Integer, sa.ForeignKey('post.id'))
    rating = sa.Column(sa.Integer)
    created_at = sa.Column(sa.DateTime)

    user = sa.orm.relationship('User')
    post = sa.orm.relationship('Post')


class BaseTest(unittest.TestCase):
    def setUp(self):
        sess.rollback()

        BaseModel.set_session(None)


## ... source file continues with no further hybrid_method examples...

```

