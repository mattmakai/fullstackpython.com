title: sqlalchemy.schema ForeignKeyConstraint Example Code
category: page
slug: sqlalchemy-schema-foreignkeyconstraint-examples
sortorder: 500031104
toc: False
sidebartitle: sqlalchemy.schema ForeignKeyConstraint
meta: Example code for understanding how to use the ForeignKeyConstraint class from the sqlalchemy.schema module of the SQLAlchemy project.


`ForeignKeyConstraint` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-createtable-examples.html">CreateTable</a>,
<a href="/sqlalchemy-schema-ddlelement-examples.html">DDLElement</a>,
<a href="/sqlalchemy-schema-foreignkey-examples.html">ForeignKey</a>,
<a href="/sqlalchemy-schema-index-examples.html">Index</a>,
<a href="/sqlalchemy-schema-primarykeyconstraint-examples.html">PrimaryKeyConstraint</a>,
and <a href="/sqlalchemy-schema-table-examples.html">Table</a>
are several other callables with code examples from the same `sqlalchemy.schema` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / util / sqla_compat.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/util/sqla_compat.py)

```python
# sqla_compat.py
import re

from sqlalchemy import __version__
from sqlalchemy import inspect
from sqlalchemy import schema
from sqlalchemy import sql
from sqlalchemy import types as sqltypes
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.schema import Column
~~from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.sql.elements import quoted_name
from sqlalchemy.sql.expression import _BindParamClause
from sqlalchemy.sql.expression import _TextClause as TextClause
from sqlalchemy.sql.visitors import traverse

from . import compat


def _safe_int(value):
    try:
        return int(value)
    except:
        return value


_vers = tuple(
    [_safe_int(x) for x in re.findall(r"(\d+|[abc]\d)", __version__)]
)
sqla_110 = _vers >= (1, 1, 0)
sqla_1115 = _vers >= (1, 1, 15)
sqla_120 = _vers >= (1, 2, 0)
sqla_1216 = _vers >= (1, 2, 16)
sqla_13 = _vers >= (1, 3)
sqla_14 = _vers >= (1, 4)


## ... source file abbreviated to get to ForeignKeyConstraint examples ...


def _connectable_has_table(connectable, tablename, schemaname):
    if sqla_14:
        return inspect(connectable).has_table(tablename, schemaname)
    else:
        return connectable.dialect.has_table(
            connectable, tablename, schemaname
        )


def _exec_on_inspector(inspector, statement, **params):
    if sqla_14:
        with inspector._operation_context() as conn:
            return conn.execute(statement, params)
    else:
        return inspector.bind.execute(statement, params)


def _server_default_is_computed(column):
    if not has_computed:
        return False
    else:
        return isinstance(column.computed, Computed)


def _table_for_constraint(constraint):
~~    if isinstance(constraint, ForeignKeyConstraint):
        return constraint.parent
    else:
        return constraint.table


def _columns_for_constraint(constraint):
~~    if isinstance(constraint, ForeignKeyConstraint):
        return [fk.parent for fk in constraint.elements]
    elif isinstance(constraint, CheckConstraint):
        return _find_columns(constraint.sqltext)
    else:
        return list(constraint.columns)


def _fk_spec(constraint):
    source_columns = [
        constraint.columns[key].name for key in constraint.column_keys
    ]

    source_table = constraint.parent.name
    source_schema = constraint.parent.schema
    target_schema = constraint.elements[0].column.table.schema
    target_table = constraint.elements[0].column.table.name
    target_columns = [element.column.name for element in constraint.elements]
    ondelete = constraint.ondelete
    onupdate = constraint.onupdate
    deferrable = constraint.deferrable
    initially = constraint.initially
    return (
        source_schema,
        source_table,


## ... source file continues with no further ForeignKeyConstraint examples...

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

[**sqlalchemy-utils / sqlalchemy_utils / functions / foreign_keys.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/foreign_keys.py)

```python
# foreign_keys.py
from collections import defaultdict
from itertools import groupby

import sqlalchemy as sa
from sqlalchemy.exc import NoInspectionAvailable
from sqlalchemy.orm import object_session
~~from sqlalchemy.schema import ForeignKeyConstraint, MetaData, Table

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


## ... source file abbreviated to get to ForeignKeyConstraint examples ...


            )
        criteria.append(sa.and_(*subcriteria))
    return criteria


def non_indexed_foreign_keys(metadata, engine=None):
    reflected_metadata = MetaData()

    if metadata.bind is None and engine is None:
        raise Exception(
            'Either pass a metadata object with bind or '
            'pass engine as a second parameter'
        )

    constraints = defaultdict(list)

    for table_name in metadata.tables.keys():
        table = Table(
            table_name,
            reflected_metadata,
            autoload=True,
            autoload_with=metadata.bind or engine
        )

        for constraint in table.constraints:
~~            if not isinstance(constraint, ForeignKeyConstraint):
                continue

            if not has_index(constraint):
                constraints[table.name].append(constraint)

    return dict(constraints)


def get_fk_constraint_for_columns(table, *columns):
    for constraint in table.constraints:
        if list(constraint.columns.values()) == list(columns):
            return constraint



## ... source file continues with no further ForeignKeyConstraint examples...

```

