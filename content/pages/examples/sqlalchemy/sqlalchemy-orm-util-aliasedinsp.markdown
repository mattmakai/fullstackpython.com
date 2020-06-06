title: sqlalchemy.orm.util AliasedInsp code examples
category: page
slug: sqlalchemy-orm-util-aliasedinsp-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.orm.util AliasedInsp
meta: Python example code for the AliasedInsp class from the sqlalchemy.orm.util module of the SQLAlchemy project.


AliasedInsp is a class within the sqlalchemy.orm.util module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
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
from sqlalchemy.orm.session import object_session
~~from sqlalchemy.orm.util import AliasedInsp

from ..utils import is_sequence


def get_class_by_table(base, table, data=None):
    """
    Return declarative class associated with given table. If no class is found
    this function returns `None`. If multiple classes were found (polymorphic
    cases) additional `data` parameter can be given to hint which class
    to return.

    ::

        class User(Base):
            __tablename__ = 'entity'
            id = sa.Column(sa.Integer, primary_key=True)
            name = sa.Column(sa.String)


        get_class_by_table(Base, User.__table__)  # User class


    This function also supports models using single table inheritance.
    Additional data paratemer should be provided in these case.


## ... source file abbreviated to get to AliasedInsp examples ...




    Raises:
        ValueError: if multiple mappers were found for given argument

    .. versionadded: 0.26.1
    """
    if isinstance(mixed, sa.orm.query._MapperEntity):
        mixed = mixed.expr
    elif isinstance(mixed, sa.Column):
        mixed = mixed.table
    elif isinstance(mixed, sa.orm.query._ColumnEntity):
        mixed = mixed.expr

    if isinstance(mixed, sa.orm.Mapper):
        return mixed
    if isinstance(mixed, sa.orm.util.AliasedClass):
        return sa.inspect(mixed).mapper
    if isinstance(mixed, sa.sql.selectable.Alias):
        mixed = mixed.element
~~    if isinstance(mixed, AliasedInsp):
        return mixed.mapper
    if isinstance(mixed, sa.orm.attributes.InstrumentedAttribute):
        mixed = mixed.class_
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


## ... source file abbreviated to get to AliasedInsp examples ...


    ] + [
        get_query_entity(entity) for entity in query._join_entities
    ]


def is_labeled_query(expr):
    return (
        isinstance(expr, sa.sql.elements.Label) and
        isinstance(
            list(expr.base_columns)[0],
            (sa.sql.selectable.Select, sa.sql.selectable.ScalarSelect)
        )
    )


def get_query_entity(expr):
    if isinstance(expr, sa.orm.attributes.InstrumentedAttribute):
        return expr.parent.class_
    elif isinstance(expr, sa.Column):
        return expr.table
~~    elif isinstance(expr, AliasedInsp):
        return expr.entity
    return expr


def get_query_entity_by_alias(query, alias):
    entities = get_query_entities(query)

    if not alias:
        return entities[0]

    for entity in entities:
        if isinstance(entity, sa.orm.util.AliasedClass):
            name = sa.inspect(entity).name
        else:
            name = get_mapper(entity).tables[0].name

        if name == alias:
            return entity


def get_polymorphic_mappers(mixed):
~~    if isinstance(mixed, AliasedInsp):
        return mixed.with_polymorphic_mappers
    else:
        return mixed.polymorphic_map.values()


def get_query_descriptor(query, entity, attr):
    if attr in query_labels(query):
        return attr
    else:
        entity = get_query_entity_by_alias(query, entity)
        if entity:
            descriptor = get_descriptor(entity, attr)
            if (
                hasattr(descriptor, 'property') and
                isinstance(descriptor.property, sa.orm.RelationshipProperty)
            ):
                return
            return descriptor


def get_descriptor(entity, attr):
    mapper = sa.inspect(entity)

    for key, descriptor in get_all_descriptors(mapper).items():


## ... source file continues with no further AliasedInsp examples...


```

