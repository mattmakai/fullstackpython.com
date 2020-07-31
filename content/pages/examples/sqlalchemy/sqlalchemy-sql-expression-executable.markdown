title: sqlalchemy.sql.expression Executable Example Code
category: page
slug: sqlalchemy-sql-expression-executable-examples
sortorder: 500031124
toc: False
sidebartitle: sqlalchemy.sql.expression Executable
meta: Example code for understanding how to use the Executable class from the sqlalchemy.sql.expression module of the SQLAlchemy project.


`Executable` is a class within the `sqlalchemy.sql.expression` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-expression-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-expression-columnclause-examples.html">ColumnClause</a>,
<a href="/sqlalchemy-sql-expression-columnelement-examples.html">ColumnElement</a>,
<a href="/sqlalchemy-sql-expression-functionelement-examples.html">FunctionElement</a>,
and <a href="/sqlalchemy-sql-expression-unaryexpression-examples.html">UnaryExpression</a>
are several other callables with code examples from the same `sqlalchemy.sql.expression` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / ddl / mssql.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/ddl/mssql.py)

```python
# mssql.py
from sqlalchemy import types as sqltypes
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import Column
from sqlalchemy.schema import CreateIndex
from sqlalchemy.sql.expression import ClauseElement
~~from sqlalchemy.sql.expression import Executable

from .base import AddColumn
from .base import alter_column
from .base import alter_table
from .base import ColumnDefault
from .base import ColumnName
from .base import ColumnNullable
from .base import ColumnType
from .base import format_column_name
from .base import format_server_default
from .base import format_table_name
from .base import format_type
from .base import RenameTable
from .impl import DefaultImpl
from .. import util


class MSSQLImpl(DefaultImpl):
    __dialect__ = "mssql"
    transactional_ddl = True
    batch_separator = "GO"

    type_synonyms = DefaultImpl.type_synonyms + ({"VARCHAR", "NVARCHAR"},)



## ... source file abbreviated to get to Executable examples ...


            super(MSSQLImpl, self).bulk_insert(table, rows, **kw)

    def drop_column(self, table_name, column, schema=None, **kw):
        drop_default = kw.pop("mssql_drop_default", False)
        if drop_default:
            self._exec(
                _ExecDropConstraint(
                    table_name, column, "sys.default_constraints", schema
                )
            )
        drop_check = kw.pop("mssql_drop_check", False)
        if drop_check:
            self._exec(
                _ExecDropConstraint(
                    table_name, column, "sys.check_constraints", schema
                )
            )
        drop_fks = kw.pop("mssql_drop_foreign_key", False)
        if drop_fks:
            self._exec(_ExecDropFKConstraint(table_name, column, schema))
        super(MSSQLImpl, self).drop_column(
            table_name, column, schema=schema, **kw
        )


~~class _ExecDropConstraint(Executable, ClauseElement):
    def __init__(self, tname, colname, type_, schema):
        self.tname = tname
        self.colname = colname
        self.type_ = type_
        self.schema = schema


~~class _ExecDropFKConstraint(Executable, ClauseElement):
    def __init__(self, tname, colname, schema):
        self.tname = tname
        self.colname = colname
        self.schema = schema


@compiles(_ExecDropConstraint, "mssql")
def _exec_drop_col_constraint(element, compiler, **kw):
    schema, tname, colname, type_ = (
        element.schema,
        element.tname,
        element.colname,
        element.type_,
    )
    return """declare @const_name varchar(256)
select @const_name = [name] from %(type)s
where parent_object_id = object_id('%(schema_dot)s%(tname)s')
and col_name(parent_object_id, parent_column_id) = '%(colname)s'
exec('alter table %(tname_quoted)s drop constraint ' + @const_name)""" % {
        "type": type_,
        "tname": tname,
        "colname": colname,
        "tname_quoted": format_table_name(compiler, tname, schema),
        "schema_dot": schema + "." if schema else "",


## ... source file continues with no further Executable examples...

```

