title: sqlalchemy.exc NoInspectionAvailable Example Code
category: page
slug: sqlalchemy-exc-noinspectionavailable-examples
sortorder: 500031039
toc: False
sidebartitle: sqlalchemy.exc NoInspectionAvailable
meta: Example code for understanding how to use the NoInspectionAvailable class from the sqlalchemy.exc module of the SQLAlchemy project.


`NoInspectionAvailable` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-databaseerror-examples.html">DatabaseError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-invalidrequesterror-examples.html">InvalidRequestError</a>,
<a href="/sqlalchemy-exc-nosuchtableerror-examples.html">NoSuchTableError</a>,
<a href="/sqlalchemy-exc-operationalerror-examples.html">OperationalError</a>,
<a href="/sqlalchemy-exc-programmingerror-examples.html">ProgrammingError</a>,
and <a href="/sqlalchemy-exc-unsupportedcompilationerror-examples.html">UnsupportedCompilationError</a>
are several other callables with code examples from the same `sqlalchemy.exc` package.

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
~~from sqlalchemy.exc import NoInspectionAvailable
from sqlalchemy.orm import object_session
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


## ... source file abbreviated to get to NoInspectionAvailable examples ...


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

    session = object_session(obj)

    chain = QueryChain([])
    classes = obj.__class__._decl_class_registry

    for table, keys in group_foreign_keys(foreign_keys):
        keys = list(keys)
        for class_ in classes.values():
            try:
                mapper = sa.inspect(class_)
~~            except NoInspectionAvailable:
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
    criteria = []
    visited_constraints = []
    for key in keys:
        if key.constraint in visited_constraints:
            continue
        visited_constraints.append(key.constraint)

        subcriteria = []
        for index, column in enumerate(key.constraint.columns):
            foreign_column = (


## ... source file continues with no further NoInspectionAvailable examples...

```

