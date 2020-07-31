title: sqlalchemy.orm object_session Example Code
category: page
slug: sqlalchemy-orm-object-session-examples
sortorder: 500031071
toc: False
sidebartitle: sqlalchemy.orm object_session
meta: Python example code that shows how to use the object_session callable from the sqlalchemy.orm module of the SQLAlchemy project.


`object_session` is a callable within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-load-examples.html">Load</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">Mapper</a>,
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

[**sqlalchemy-utils / sqlalchemy_utils / functions / foreign_keys.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/foreign_keys.py)

```python
# foreign_keys.py
from collections import defaultdict
from itertools import groupby

import sqlalchemy as sa
from sqlalchemy.exc import NoInspectionAvailable
~~from sqlalchemy.orm import object_session
from sqlalchemy.schema import ForeignKeyConstraint, MetaData, Table

from ..query_chain import QueryChain
from .database import has_index
from .orm import get_column_key, get_mapper, get_tables


def get_foreign_key_values(fk, obj):
    return dict(
        (
            fk.constraint.columns.values()[index].key,
            getattr(obj, element.column.key)
        )
        for
        index, element
        in
        enumerate(fk.constraint.elements)
    )


def group_foreign_keys(foreign_keys):
    foreign_keys = sorted(
        foreign_keys, key=lambda key: key.constraint.table.name
    )
    return groupby(foreign_keys, lambda key: key.constraint.table)


def get_referencing_foreign_keys(mixed):
    if isinstance(mixed, sa.Table):
        tables = [mixed]
    else:
        tables = get_tables(mixed)

    referencing_foreign_keys = set()

    for table in mixed.metadata.tables.values():
        if table not in tables:
            for constraint in table.constraints:
                if isinstance(constraint, sa.sql.schema.ForeignKeyConstraint):
                    for fk in constraint.elements:
                        if any(fk.references(t) for t in tables):
                            referencing_foreign_keys.add(fk)
    return referencing_foreign_keys


def merge_references(from_, to, foreign_keys=None):
    if from_.__tablename__ != to.__tablename__:
        raise TypeError('The tables of given arguments do not match.')

~~    session = object_session(from_)
    foreign_keys = get_referencing_foreign_keys(from_)

    for fk in foreign_keys:
        old_values = get_foreign_key_values(fk, from_)
        new_values = get_foreign_key_values(fk, to)
        criteria = (
            getattr(fk.constraint.table.c, key) == value
            for key, value in old_values.items()
        )
        try:
            mapper = get_mapper(fk.constraint.table)
        except ValueError:
            query = (
                fk.constraint.table
                .update()
                .where(sa.and_(*criteria))
                .values(new_values)
            )
            session.execute(query)
        else:
            (
                session.query(mapper.class_)
                .filter_by(**old_values)
                .update(
                    new_values,
                    'evaluate'
                )
            )


def dependent_objects(obj, foreign_keys=None):
    if foreign_keys is None:
        foreign_keys = get_referencing_foreign_keys(obj)

~~    session = object_session(obj)

    chain = QueryChain([])
    classes = obj.__class__._decl_class_registry

    for table, keys in group_foreign_keys(foreign_keys):
        keys = list(keys)
        for class_ in classes.values():
            try:
                mapper = sa.inspect(class_)
            except NoInspectionAvailable:
                continue
            parent_mapper = mapper.inherits
            if (
                table in mapper.tables and
                not (parent_mapper and table in parent_mapper.tables)
            ):
                query = session.query(class_).filter(
                    sa.or_(*_get_criteria(keys, class_, obj))
                )
                chain.queries.append(query)
    return chain


def _get_criteria(keys, class_, obj):


## ... source file continues with no further object_session examples...

```

