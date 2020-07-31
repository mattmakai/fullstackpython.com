title: sqlalchemy.orm.session object_session Example Code
category: page
slug: sqlalchemy-orm-session-object-session-examples
sortorder: 500031092
toc: False
sidebartitle: sqlalchemy.orm.session object_session
meta: Python example code that shows how to use the object_session callable from the sqlalchemy.orm.session module of the SQLAlchemy project.


`object_session` is a callable within the `sqlalchemy.orm.session` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-session-session-examples.html">Session</a>
is another callable from the `sqlalchemy.orm.session` package with code examples.

## Example 1 from sqlalchemy-utils
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
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm.properties import ColumnProperty, RelationshipProperty
from sqlalchemy.orm.query import _ColumnEntity
~~from sqlalchemy.orm.session import object_session
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
                mapper = sa.inspect(cls)
                polymorphic_on = mapper.polymorphic_on.name
                if polymorphic_on in data:


## ... source file abbreviated to get to object_session examples ...


    if isinstance(mixed, sa.Table):
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
~~            conn = object_session(obj).bind
        except UnmappedInstanceError:
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


## ... source file continues with no further object_session examples...

```

