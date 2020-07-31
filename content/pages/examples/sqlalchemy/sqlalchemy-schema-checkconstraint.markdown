title: sqlalchemy.schema CheckConstraint Example Code
category: page
slug: sqlalchemy-schema-checkconstraint-examples
sortorder: 500031098
toc: False
sidebartitle: sqlalchemy.schema CheckConstraint
meta: Example code for understanding how to use the CheckConstraint class from the sqlalchemy.schema module of the SQLAlchemy project.


`CheckConstraint` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-createtable-examples.html">CreateTable</a>,
<a href="/sqlalchemy-schema-ddlelement-examples.html">DDLElement</a>,
<a href="/sqlalchemy-schema-foreignkey-examples.html">ForeignKey</a>,
<a href="/sqlalchemy-schema-foreignkeyconstraint-examples.html">ForeignKeyConstraint</a>,
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
~~from sqlalchemy.schema import CheckConstraint
from sqlalchemy.schema import Column
from sqlalchemy.schema import ForeignKeyConstraint
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


## ... source file abbreviated to get to CheckConstraint examples ...


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
    if isinstance(constraint, ForeignKeyConstraint):
        return constraint.parent
    else:
        return constraint.table


def _columns_for_constraint(constraint):
    if isinstance(constraint, ForeignKeyConstraint):
        return [fk.parent for fk in constraint.elements]
~~    elif isinstance(constraint, CheckConstraint):
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
        source_columns,
        target_schema,


## ... source file continues with no further CheckConstraint examples...

```

