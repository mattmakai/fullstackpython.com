title: sqlalchemy.ext.declarative declarative_base Example Code
category: page
slug: sqlalchemy-ext-declarative-declarative-base-examples
sortorder: 500031049
toc: False
sidebartitle: sqlalchemy.ext.declarative declarative_base
meta: Python example code that shows how to use the declarative_base callable from the sqlalchemy.ext.declarative module of the SQLAlchemy project.


`declarative_base` is a callable within the `sqlalchemy.ext.declarative` module of the SQLAlchemy project.

<a href="/sqlalchemy-ext-declarative-declarativemeta-examples.html">DeclarativeMeta</a>
is another callable from the `sqlalchemy.ext.declarative` package with code examples.

## Example 1 from flask-sqlalchemy
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
from flask import request
from flask.signals import Namespace
from sqlalchemy import event
from sqlalchemy import inspect
from sqlalchemy import orm
from sqlalchemy.engine.url import make_url
~~from sqlalchemy.ext.declarative import declarative_base
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
        info = kwargs.pop("info", None) or {}
        info.setdefault("bind_key", None)
        kwargs["info"] = info
        return sqlalchemy.Table(*args, **kwargs)

    return _make_table


## ... source file abbreviated to get to declarative_base examples ...


        _include_sqlalchemy(self, query_class)

        if app is not None:
            self.init_app(app)

    @property
    def metadata(self):

        return self.Model.metadata

    def create_scoped_session(self, options=None):

        if options is None:
            options = {}

        scopefunc = options.pop("scopefunc", _app_ctx_stack.__ident_func__)
        options.setdefault("query_cls", self.Query)
        return orm.scoped_session(self.create_session(options), scopefunc=scopefunc)

    def create_session(self, options):

        return orm.sessionmaker(class_=SignallingSession, db=self, **options)

    def make_declarative_base(self, model, metadata=None):
        if not isinstance(model, DeclarativeMeta):
~~            model = declarative_base(
                cls=model, name="Model", metadata=metadata, metaclass=DefaultMeta
            )

        if metadata is not None and model.metadata is not metadata:
            model.metadata = metadata

        if not getattr(model, "query_class", None):
            model.query_class = self.Query

        model.query = _QueryProperty(self)
        return model

    def init_app(self, app):

        if not (
            app.config.get("SQLALCHEMY_DATABASE_URI")
            or app.config.get("SQLALCHEMY_BINDS")
        ):
            raise RuntimeError(
                "Either SQLALCHEMY_DATABASE_URI or SQLALCHEMY_BINDS needs to be set."
            )

        app.config.setdefault("SQLALCHEMY_DATABASE_URI", None)
        app.config.setdefault("SQLALCHEMY_BINDS", None)


## ... source file continues with no further declarative_base examples...

```


## Example 2 from graphene-sqlalchemy
[graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy)
([project documentation](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/)
and
[PyPI package information](https://pypi.org/project/graphene-sqlalchemy/))
is a [SQLAlchemy](/sqlalchemy.html) integration for
[Graphene](https://graphene-python.org/), which makes it easier to build
GraphQL-based [APIs](/application-programming-interfaces.html) into Python
[web applications](/web-development.html). The package allows you to
subclass SQLAlchemy classes and build queries around them with custom
code to match the backend queries with the GraphQL-based request queries.
The project is provided as open source under the
[MIT license](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/LICENSE.md).

[**graphene-sqlalchemy / graphene_sqlalchemy / tests / models.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/tests/models.py)

```python
# models.py
from __future__ import absolute_import

import enum

from sqlalchemy import (Column, Date, Enum, ForeignKey, Integer, String, Table,
                        func, select)
~~from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property, composite, mapper, relationship

PetKind = Enum("cat", "dog", name="pet_kind")


class HairKind(enum.Enum):
    LONG = 'long'
    SHORT = 'short'


~~Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("pet_id", Integer, ForeignKey("pets.id")),
    Column("reporter_id", Integer, ForeignKey("reporters.id")),
)


class Editor(Base):
    __tablename__ = "editors"
    editor_id = Column(Integer(), primary_key=True)
    name = Column(String(100))


class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer(), primary_key=True)
    name = Column(String(30))
    pet_kind = Column(PetKind, nullable=False)
    hair_kind = Column(Enum(HairKind, name="hair_kind"), nullable=False)
    reporter_id = Column(Integer(), ForeignKey("reporters.id"))




## ... source file continues with no further declarative_base examples...

```


## Example 3 from sqlalchemy-datatables
[sqlalchemy-datatables](https://github.com/Pegase745/sqlalchemy-datatables)
([PyPI package information](https://pypi.org/project/sqlalchemy-datatables/))
is a helper library that makes it easier to use [SQLAlchemy](/sqlalchemy.html)
with the jQuery [JavaScript](/javascript.html)
[DataTables](https://datatables.net/) plugin. This library is designed to
be [web framework](/web-frameworks.html) agnostic and provides code examples
for both [Flask](/flask.html) and [Pyramid](/pyramid.html).

The project is built and maintained by
[Michel Nemnom (Pegase745)](https://github.com/Pegase745) and is open
sourced under the
[MIT license](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/LICENSE).

[**sqlalchemy-datatables / tests / models.py**](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/./tests/models.py)

```python
# models.py
import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, func
~~from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import backref, relationship

~~Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    birthday = Column(Date)
    address = relationship('Address', uselist=False, backref=backref('user'))

    def __unicode__(self):
        return '%s' % self.name

    def __repr__(self):
        return '<%s#%s>' % (self.__class__.__name__, self.id)

    @hybrid_property
    def dummy(self):
        return self.name[0:3]

    @dummy.expression
    def dummy(cls):


## ... source file continues with no further declarative_base examples...

```


## Example 4 from SQLAlchemy Mixins
[SQLAlchemy Mixins](https://github.com/absent1706/sqlalchemy-mixins)
([PyPI package information](https://pypi.org/project/sqlalchemy-mixins/))
is a collection of
[mixins](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
useful for extending [SQLAlchemy](/sqlalchemy.html) and simplifying
your [database](/databases.html)-interacting code for some common
use cases. SQLAlchemy Mixins is open sourced under the
[MIT license](https://github.com/absent1706/sqlalchemy-mixins/blob/master/LICENSE.txt).

[**SQLAlchemy Mixins / sqlalchemy_mixins / inspection.py**](https://github.com/absent1706/sqlalchemy-mixins/blob/master/sqlalchemy_mixins/./inspection.py)

```python
# inspection.py
from sqlalchemy import inspect
~~from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm import RelationshipProperty

from .utils import classproperty


~~Base = declarative_base()


class InspectionMixin(Base):
    __abstract__ = True

    @classproperty
    def columns(cls):
        return inspect(cls).columns.keys()

    @classproperty
    def primary_keys_full(cls):
        mapper = cls.__mapper__
        return [
            mapper.get_property_by_column(column)
            for column in mapper.primary_key
        ]

    @classproperty
    def primary_keys(cls):
        return [pk.key for pk in cls.primary_keys_full]

    @classproperty
    def relations(cls):
        return [c.key for c in cls.__mapper__.iterate_properties


## ... source file continues with no further declarative_base examples...

```


## Example 5 from SQLAthanor
[SQLAthanor](https://github.com/insightindustry/sqlathanor)
([PyPI package information](https://pypi.org/project/sqlathanor/)
and
[project documentation](https://sqlathanor.readthedocs.io/en/latest/index.html))
is a [SQLAlchemy](/sqlalchemy.html) extension that provides serialization and
deserialization support for JSON, CSV, YAML and Python dictionaries.
This project is similar to [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
with one major difference: SQLAthanor works through SQLAlchemy models
while Marshmallow is less coupled to SQLAlchemy because it requires
separate representations of the serialization objects. Both libraries
have their uses depending on whether the project plans to use SQLAlchemy
for object representations or would prefer to avoid that couping.
SQLAthanor is open sourced under the
[MIT license](https://github.com/insightindustry/sqlathanor/blob/master/LICENSE).

[**SQLAthanor / sqlathanor / declarative / declarative_base.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/declarative/declarative_base.py)

```python
# declarative_base.py


~~from sqlalchemy.ext.declarative import declarative_base as SA_declarative_base
from validator_collection import checkers

from sqlathanor.declarative.base_model import BaseModel


~~def declarative_base(cls = BaseModel, **kwargs):
    if isinstance(cls, tuple):
        class_list = [x for x in cls]
        class_list.insert(0, BaseModel)
        cls = (x for x in class_list)
    elif checkers.is_iterable(cls):
        class_list = [BaseModel]
        class_list.extend(cls)
        cls = (x for x in class_list)

    return SA_declarative_base(cls = cls, **kwargs)


def as_declarative(**kw):
    def decorate(cls):
        kw['cls'] = cls
        kw['name'] = cls.__name__
~~        return declarative_base(**kw)

    return decorate



## ... source file continues with no further declarative_base examples...

```


## Example 6 from sandman2
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

[**sandman2 / sandman2 / model.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./model.py)

```python
# model.py

import datetime
from decimal import Decimal

from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy  # pylint: disable=import-error,no-name-in-module
from sqlalchemy.ext.automap import automap_base
~~from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class Model(object):


    __url__ = None

    __version__ = '1'

    __methods__ = {
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'HEAD',
        'OPTIONS'
        }

    @classmethod
    def required(cls):
        columns = []
        for column in cls.__table__.columns:  # pylint: disable=no-member


## ... source file abbreviated to get to declarative_base examples ...


            if 'collection' not in relationship.key:
                instance = getattr(self, relationship.key)
                if instance:
                    link_dict[str(relationship.key)] = instance.resource_uri()
        return link_dict

    def resource_uri(self):
        return self.__url__ + '/' + str(getattr(self, self.primary_key()))

    def update(self, attributes):
        for attribute in attributes:
            setattr(self, attribute, attributes[attribute])
        return self

    @classmethod
    def description(cls):

        description = {}
        for column in cls.__table__.columns:  # pylint: disable=no-member
            column_description = str(column.type)
            if not column.nullable:
                column_description += ' (required)'
            description[column.name] = column_description
        return description

~~DeclarativeModel = declarative_base(cls=(db.Model, Model))
AutomapModel = automap_base(DeclarativeModel)



## ... source file continues with no further declarative_base examples...

```

