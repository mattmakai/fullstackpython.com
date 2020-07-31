title: sqlalchemy.exc InvalidRequestError Example Code
category: page
slug: sqlalchemy-exc-invalidrequesterror-examples
sortorder: 500031038
toc: False
sidebartitle: sqlalchemy.exc InvalidRequestError
meta: Example code for understanding how to use the InvalidRequestError class from the sqlalchemy.exc module of the SQLAlchemy project.


`InvalidRequestError` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-databaseerror-examples.html">DatabaseError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-noinspectionavailable-examples.html">NoInspectionAvailable</a>,
<a href="/sqlalchemy-exc-nosuchtableerror-examples.html">NoSuchTableError</a>,
<a href="/sqlalchemy-exc-operationalerror-examples.html">OperationalError</a>,
<a href="/sqlalchemy-exc-programmingerror-examples.html">ProgrammingError</a>,
and <a href="/sqlalchemy-exc-unsupportedcompilationerror-examples.html">UnsupportedCompilationError</a>
are several other callables with code examples from the same `sqlalchemy.exc` package.

## Example 1 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / declarative.py**](https://github.com/python-gino/gino/blob/master/src/gino/./declarative.py)

```python
# declarative.py
import collections

import sqlalchemy as sa
~~from sqlalchemy.exc import InvalidRequestError

from . import json_support
from .exceptions import GinoException


class ColumnAttribute:

    def __init__(self, prop_name, column):
        self.prop_name = prop_name
        self.column = column

    def __get__(self, instance, owner):
        if instance is None:
            return self.column
        else:
            return instance.__values__.get(self.prop_name)

    def __set__(self, instance, value):
        instance.__values__[self.prop_name] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete value.")




## ... source file abbreviated to get to InvalidRequestError examples ...


                    updates[k] = sub_cls.__attr_factory__(k, v)
                elif isinstance(v, (sa.Index, sa.Constraint)):
                    inspected_args.append(v)
                elif isinstance(v, json_support.JSONProperty):
                    updates[k] = v
        if table_name is None:
            return
        sub_cls._column_name_map = column_name_map

        table_args = updates.get(
            "__table_args__", getattr(sub_cls, "__table_args__", None)
        )
        args, table_kw = (), {}
        if isinstance(table_args, dict):
            table_kw = table_args
        elif isinstance(table_args, tuple) and table_args:
            if isinstance(table_args[-1], dict):
                args, table_kw = table_args[0:-1], table_args[-1]
            else:
                args = table_args

        args = (*columns, *inspected_args, *args)
        for item in args:
            try:
                _table = getattr(item, "table", None)
~~            except InvalidRequestError:
                _table = None
            if _table is not None:
                raise ValueError(
                    "{} is already attached to another table. Please do not "
                    "use the same item twice. A common mistake is defining "
                    "constraints and indices in a super class - we are working"
                    " on making it possible."
                )
        rv = sa.Table(table_name, sub_cls.__metadata__, *args, **table_kw)
        for k, v in updates.items():
            setattr(sub_cls, k, v)

        json_prop_names = set()
        for each_cls in sub_cls.__mro__[::-1]:
            for k, v in each_cls.__dict__.items():
                if isinstance(v, json_support.JSONProperty):
                    if not v.name:
                        v.name = k
                    json_prop_names.add(v.prop_name)
                    json_col = getattr(
                        sub_cls.__dict__.get(v.prop_name), "column", None
                    )
                    if not isinstance(json_col, sa.Column) or not isinstance(
                        json_col.type, sa.JSON


## ... source file continues with no further InvalidRequestError examples...

```


## Example 2 from SQLAlchemy filters
[SQLAlchemy filters](https://github.com/juliotrigo/sqlalchemy-filters)
         provides filtering, sorting and pagination for [SQLAlchemy](/sqlalchemy.html)
         query objects, which is particularly useful when building
         [web APIs](/application-programming-interfaces.html). SQLAlchemy filters
         is open sourced under the
         [Apache License version 2.0](https://github.com/juliotrigo/sqlalchemy-filters/blob/master/LICENSE).

[**SQLAlchemy filters / sqlalchemy_filters / models.py**](https://github.com/juliotrigo/sqlalchemy-filters/blob/master/sqlalchemy_filters/./models.py)

```python
# models.py
~~from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.mapper import Mapper
from sqlalchemy.util import symbol
import types

from .exceptions import BadQuery, FieldNotFound, BadSpec


class Field(object):

    def __init__(self, model, field_name):
        self.model = model
        self.field_name = field_name

    def get_sqlalchemy_field(self):
        if self.field_name not in self._get_valid_field_names():
            raise FieldNotFound(
                'Model {} has no column `{}`.'.format(
                    self.model, self.field_name
                )
            )
        sqlalchemy_field = getattr(self.model, self.field_name)

        if isinstance(sqlalchemy_field, types.MethodType):


## ... source file abbreviated to get to InvalidRequestError examples ...



def get_model_class_by_name(registry, name):
    for cls in registry.values():
        if getattr(cls, '__name__', None) == name:
            return cls


def get_default_model(query):
    query_models = get_query_models(query).values()
    if len(query_models) == 1:
        default_model, = iter(query_models)
    else:
        default_model = None
    return default_model


def auto_join(query, *model_names):
    query_models = get_query_models(query).values()
    model_registry = list(query_models)[-1]._decl_class_registry

    for name in model_names:
        model = get_model_class_by_name(model_registry, name)
        if model not in get_query_models(query).values():
            try:
                query = query.join(model)
~~            except InvalidRequestError:
                pass  # can't be autojoined
    return query



## ... source file continues with no further InvalidRequestError examples...

```


## Example 3 from SQLAthanor
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

[**SQLAthanor / sqlathanor / utilities.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./utilities.py)

```python
# utilities.py

import csv
import linecache
import warnings
import yaml
from collections import OrderedDict

from sqlalchemy.orm.collections import InstrumentedList
~~from sqlalchemy.exc import InvalidRequestError as SA_InvalidRequestError
from sqlalchemy.exc import UnsupportedCompilationError as SA_UnsupportedCompilationError

from validator_collection import validators, checkers
from validator_collection.errors import NotAnIterableError

from sqlathanor._compat import json, is_py2, is_py36, is_py35, dict as dict_
from sqlathanor.errors import InvalidFormatError, UnsupportedSerializationError, \
    UnsupportedDeserializationError, MaximumNestingExceededError, \
    MaximumNestingExceededWarning, DeserializationError, CSVStructureError

UTILITY_COLUMNS = [
    'metadata',
    'primary_key_value',
    '_decl_class_registry',
    '_sa_instance_state',
    '_sa_class_manager'
]

def bool_to_tuple(input):

    if input is True:
        input = (True, True)
    elif not input:
        input = (False, False)


## ... source file continues with no further InvalidRequestError examples...

```

