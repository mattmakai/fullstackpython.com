title: sqlalchemy.inspection inspect Example Code
category: page
slug: sqlalchemy-inspection-inspect-examples
sortorder: 500031051
toc: False
sidebartitle: sqlalchemy.inspection inspect
meta: Python example code that shows how to use the inspect callable from the sqlalchemy.inspection module of the SQLAlchemy project.


`inspect` is a callable within the `sqlalchemy.inspection` module of the SQLAlchemy project.



## Example 1 from graphene-sqlalchemy
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

[**graphene-sqlalchemy / graphene_sqlalchemy / tests / test_converter.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/tests/test_converter.py)

```python
# test_converter.py
import enum

import pytest
from sqlalchemy import Column, func, select, types
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base
~~from sqlalchemy.inspection import inspect
from sqlalchemy.orm import column_property, composite
from sqlalchemy_utils import ChoiceType, JSONType, ScalarListType

import graphene
from graphene.relay import Node
from graphene.types.datetime import DateTime
from graphene.types.json import JSONString

from ..converter import (convert_sqlalchemy_column,
                         convert_sqlalchemy_composite,
                         convert_sqlalchemy_relationship)
from ..fields import (UnsortedSQLAlchemyConnectionField,
                      default_connection_field_factory)
from ..registry import Registry, get_global_registry
from ..types import SQLAlchemyObjectType
from .models import Article, CompositeFullName, Pet, Reporter


def mock_resolver():
    pass


def get_field(sqlalchemy_type, **column_kwargs):
    class Model(declarative_base()):
        __tablename__ = 'model'
        id_ = Column(types.Integer, primary_key=True)
        column = Column(sqlalchemy_type, doc="Custom Help Text", **column_kwargs)

~~    column_prop = inspect(Model).column_attrs['column']
    return convert_sqlalchemy_column(column_prop, get_global_registry(), mock_resolver)


def get_field_from_column(column_):
    class Model(declarative_base()):
        __tablename__ = 'model'
        id_ = Column(types.Integer, primary_key=True)
        column = column_

~~    column_prop = inspect(Model).column_attrs['column']
    return convert_sqlalchemy_column(column_prop, get_global_registry(), mock_resolver)


def test_should_unknown_sqlalchemy_field_raise_exception():
    re_err = "Don't know how to convert the SQLAlchemy field"
    with pytest.raises(Exception, match=re_err):
        get_field(getattr(types, 'LargeBinary', types.Binary)())


def test_should_date_convert_string():
    assert get_field(types.Date()).type == graphene.String


def test_should_datetime_convert_datetime():
    assert get_field(types.DateTime()).type == DateTime


def test_should_time_convert_string():
    assert get_field(types.Time()).type == graphene.String


def test_should_string_convert_string():
    assert get_field(types.String()).type == graphene.String



## ... source file continues with no further inspect examples...

```


## Example 2 from sandman2
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

~~from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy  # pylint: disable=import-error,no-name-in-module
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

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


## ... source file abbreviated to get to inspect examples ...


        for column in cls.__table__.columns:  # pylint: disable=no-member
            if column.nullable:
                columns.append(column.name)
        return columns

    @classmethod
    def primary_key(cls):
        return list(
            cls.__table__.primary_key.columns)[  # pylint: disable=no-member
                0].key

    def to_dict(self):
        result_dict = {}
        for column in self.__table__.columns.keys():  # pylint: disable=no-member
            value = result_dict[column] = getattr(self, column, None)
            if isinstance(value, Decimal):
                result_dict[column] = float(result_dict[column])
            elif isinstance(value, datetime.datetime):
                result_dict[column] = value.isoformat()
            elif isinstance(value, datetime.time):
                result_dict[column] = value.strftime("%H:%M:%S")
        return result_dict

    def links(self):
        link_dict = {'self': self.resource_uri()}
~~        for relationship in inspect(  # pylint: disable=maybe-no-member
                self.__class__).relationships:
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


## ... source file continues with no further inspect examples...

```

