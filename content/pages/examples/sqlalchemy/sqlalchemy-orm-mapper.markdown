title: sqlalchemy.orm mapper Example Code
category: page
slug: sqlalchemy-orm-mapper-examples
sortorder: 500031068
toc: False
sidebartitle: sqlalchemy.orm mapper
meta: Python example code that shows how to use the mapper callable from the sqlalchemy.orm module of the SQLAlchemy project.


`mapper` is a callable within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-load-examples.html">Load</a>,
<a href="/sqlalchemy-orm-query-examples.html">Query</a>,
<a href="/sqlalchemy-orm-relationshipproperty-examples.html">RelationshipProperty</a>,
<a href="/sqlalchemy-orm-session-examples.html">Session</a>,
<a href="/sqlalchemy-orm-synonymproperty-examples.html">SynonymProperty</a>,
<a href="/sqlalchemy-orm-aliased-examples.html">aliased</a>,
<a href="/sqlalchemy-orm-attributes-examples.html">attributes</a>,
<a href="/sqlalchemy-orm-backref-examples.html">backref</a>,
<a href="/sqlalchemy-orm-class-mapper-examples.html">class_mapper</a>,
<a href="/sqlalchemy-orm-column-property-examples.html">column_property</a>,
<a href="/sqlalchemy-orm-composite-examples.html">composite</a>,
<a href="/sqlalchemy-orm-interfaces-examples.html">interfaces</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">mapper</a>,
<a href="/sqlalchemy-orm-mapperlib-examples.html">mapperlib</a>,
<a href="/sqlalchemy-orm-object-mapper-examples.html">object_mapper</a>,
<a href="/sqlalchemy-orm-object-session-examples.html">object_session</a>,
<a href="/sqlalchemy-orm-query-examples.html">query</a>,
<a href="/sqlalchemy-orm-relationship-examples.html">relationship</a>,
<a href="/sqlalchemy-orm-session-examples.html">session</a>,
<a href="/sqlalchemy-orm-sessionmaker-examples.html">sessionmaker</a>,
and <a href="/sqlalchemy-orm-strategies-examples.html">strategies</a>
are several other callables with code examples from the same `sqlalchemy.orm` package.

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
~~from sqlalchemy.orm import mapperlib
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm.exc import UnmappedInstanceError
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
                mapper = sa.inspect(cls)
~~                polymorphic_on = mapper.polymorphic_on.name
                if polymorphic_on in data:
~~                    if data[polymorphic_on] == mapper.polymorphic_identity:
                        return cls
            raise ValueError(
                "Multiple declarative classes found for table '{0}'. Given "
                "data row does not match any polymorphic identity of the "
                "found classes.".format(
                    table.name
                )
            )
    elif found_classes:
        return found_classes.pop()
    return None


def get_type(expr):
    if hasattr(expr, 'type'):
        return expr.type
    elif isinstance(expr, InstrumentedAttribute):
        expr = expr.property

    if isinstance(expr, ColumnProperty):
        return expr.columns[0].type
    elif isinstance(expr, RelationshipProperty):
        return expr.mapper.class_
    raise TypeError("Couldn't inspect type.")


def cast_if(expression, type_):
    try:
        expr_type = get_type(expression)
    except TypeError:
        expr_type = expression
        check_type = type_().python_type
    else:
        check_type = type_

    return (
        sa.cast(expression, type_)
        if not isinstance(expr_type, check_type)
        else expression
    )


def get_column_key(model, column):
    mapper = sa.inspect(model)
    try:
~~        return mapper.get_property_by_column(column).key
    except sa.orm.exc.UnmappedColumnError:
~~        for key, c in mapper.columns.items():
            if c.name == column.name and c.table is column.table:
                return key
    raise sa.orm.exc.UnmappedColumnError(
        'No column %s is configured on mapper %s...' %
        (column, mapper)
    )


def get_mapper(mixed):
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
    if isinstance(mixed, AliasedInsp):
        return mixed.mapper
    if isinstance(mixed, sa.orm.attributes.InstrumentedAttribute):
        mixed = mixed.class_
    if isinstance(mixed, sa.Table):
        mappers = [
            mapper for mapper in mapperlib._mapper_registry
~~            if mixed in mapper.tables
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
        except UnmappedInstanceError:
            conn = obj


## ... source file abbreviated to get to mapper examples ...


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
    elif isinstance(mixed, sa.orm.attributes.InstrumentedAttribute):
        return mixed.parent.tables
    elif isinstance(mixed, sa.orm.query._ColumnEntity):
        mixed = mixed.expr

    mapper = get_mapper(mixed)

    polymorphic_mappers = get_polymorphic_mappers(mapper)
    if polymorphic_mappers:
        tables = sum((m.tables for m in polymorphic_mappers), [])
    else:
~~        tables = mapper.tables
    return tables


def get_columns(mixed):
    if isinstance(mixed, sa.sql.selectable.Selectable):
        return mixed.c
    if isinstance(mixed, sa.orm.util.AliasedClass):
        return sa.inspect(mixed).mapper.columns
    if isinstance(mixed, sa.orm.Mapper):
        return mixed.columns
    if isinstance(mixed, InstrumentedAttribute):
        return mixed.property.columns
    if isinstance(mixed, ColumnProperty):
        return mixed.columns
    if isinstance(mixed, sa.Column):
        return [mixed]
    if not isclass(mixed):
        mixed = mixed.__class__
    return sa.inspect(mixed).columns


def table_name(obj):
    class_ = getattr(obj, 'class_', obj)



## ... source file abbreviated to get to mapper examples ...


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
        if attr == key:
            prop = (
                descriptor.property
                if hasattr(descriptor, 'property')
                else None
            )
            if isinstance(prop, ColumnProperty):
                if isinstance(entity, sa.orm.util.AliasedClass):
~~                    for c in mapper.selectable.c:
                        if c.key == attr:
                            return c
                else:
                    return getattr(prop.parent.class_, attr)
            else:

                if isinstance(entity, sa.orm.util.AliasedClass):
                    return getattr(entity, attr)
                try:
                    return getattr(mapper.class_, attr)
                except AttributeError:
                    pass


def get_all_descriptors(expr):
    if isinstance(expr, sa.sql.selectable.Selectable):
        return expr.c
    insp = sa.inspect(expr)
    try:
        polymorphic_mappers = get_polymorphic_mappers(insp)
    except sa.exc.NoInspectionAvailable:
        return get_mapper(expr).all_orm_descriptors
    else:
        attrs = dict(get_mapper(expr).all_orm_descriptors)


## ... source file continues with no further mapper examples...

```

