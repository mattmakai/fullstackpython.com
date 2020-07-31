title: sqlalchemy.orm.exc UnmappedInstanceError Example Code
category: page
slug: sqlalchemy-orm-exc-unmappedinstanceerror-examples
sortorder: 500031082
toc: False
sidebartitle: sqlalchemy.orm.exc UnmappedInstanceError
meta: Example code for understanding how to use the UnmappedInstanceError class from the sqlalchemy.orm.exc module of the SQLAlchemy project.


`UnmappedInstanceError` is a class within the `sqlalchemy.orm.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-exc-noresultfound-examples.html">NoResultFound</a>
and
<a href="/sqlalchemy-orm-exc-unmappedclasserror-examples.html">UnmappedClassError</a>
are a couple of other callables within the `sqlalchemy.orm.exc` package that also have code examples.

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

[**graphene-sqlalchemy / graphene_sqlalchemy / utils.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./utils.py)

```python
# utils.py
import re
import warnings

from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import class_mapper, object_mapper
~~from sqlalchemy.orm.exc import UnmappedClassError, UnmappedInstanceError


def get_session(context):
    return context.get("session")


def get_query(model, context):
    query = getattr(model, "query", None)
    if not query:
        session = get_session(context)
        if not session:
            raise Exception(
                "A query in the model Base or a session in the schema is required for querying.\n"
                "Read more http://docs.graphene-python.org/projects/sqlalchemy/en/latest/tips/#querying"
            )
        query = session.query(model)
    return query


def is_mapped_class(cls):
    try:
        class_mapper(cls)
    except (ArgumentError, UnmappedClassError):
        return False
    else:
        return True


def is_mapped_instance(cls):
    try:
        object_mapper(cls)
~~    except (ArgumentError, UnmappedInstanceError):
        return False
    else:
        return True


def to_type_name(name):
    return "".join(part[:1].upper() + part[1:] for part in name.split("_"))


_re_enum_value_name_1 = re.compile("(.)([A-Z][a-z]+)")
_re_enum_value_name_2 = re.compile("([a-z0-9])([A-Z])")


def to_enum_value_name(name):
    return _re_enum_value_name_2.sub(
        r"\1_\2", _re_enum_value_name_1.sub(r"\1_\2", name)
    ).upper()


class EnumValue(str):

    def __new__(cls, s, value):
        return super(EnumValue, cls).__new__(cls, s)



## ... source file continues with no further UnmappedInstanceError examples...

```


## Example 2 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlalchemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / functions / orm.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/orm.py)

```python
# orm.py
from collections import OrderedDict
from functools import partial
from inspect import isclass
from operator import attrgetter

import six
import sqlalchemy as sa
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import mapperlib
from sqlalchemy.orm.attributes import InstrumentedAttribute
~~from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm.properties import ColumnProperty, RelationshipProperty
from sqlalchemy.orm.query import _ColumnEntity
from sqlalchemy.orm.session import object_session
from sqlalchemy.orm.util import AliasedInsp

from ..utils import is_sequence


def get_class_by_table(base, table, data=None):
    found_classes = set(
        c for c in base._decl_class_registry.values()
        if hasattr(c, '__table__') and c.__table__ is table
    )
    if len(found_classes) > 1:
        if not data:
            raise ValueError(
                "Multiple declarative classes found for table '{0}'. "
                "Please provide data parameter for this function to be able "
                "to determine polymorphic scenarios.".format(
                    table.name
                )
            )
        else:
            for cls in found_classes:


## ... source file abbreviated to get to UnmappedInstanceError examples ...


        mappers = [
            mapper for mapper in mapperlib._mapper_registry
            if mixed in mapper.tables
        ]
        if len(mappers) > 1:
            raise ValueError(
                "Multiple mappers found for table '%s'." % mixed.name
            )
        elif not mappers:
            raise ValueError(
                "Could not get mapper for table '%s'." % mixed.name
            )
        else:
            return mappers[0]
    if not isclass(mixed):
        mixed = type(mixed)
    return sa.inspect(mixed)


def get_bind(obj):
    if hasattr(obj, 'bind'):
        conn = obj.bind
    else:
        try:
            conn = object_session(obj).bind
~~        except UnmappedInstanceError:
            conn = obj

    if not hasattr(conn, 'execute'):
        raise TypeError(
            'This method accepts only Session, Engine, Connection and '
            'declarative model objects.'
        )
    return conn


def get_primary_keys(mixed):
    return OrderedDict(
        (
            (key, column) for key, column in get_columns(mixed).items()
            if column.primary_key
        )
    )


def get_tables(mixed):
    if isinstance(mixed, sa.Table):
        return [mixed]
    elif isinstance(mixed, sa.Column):
        return [mixed.table]


## ... source file continues with no further UnmappedInstanceError examples...

```

