title: sqlalchemy.schema CreateIndex code examples
category: page
slug: sqlalchemy-schema-createindex-examples
sortorder: 500031002
toc: False
sidebartitle: sqlalchemy.schema CreateIndex
meta: Python example code for the CreateIndex class from the sqlalchemy.schema module of the SQLAlchemy project.


CreateIndex is a class within the sqlalchemy.schema module of the SQLAlchemy project.


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
~~from sqlalchemy.schema import CreateIndex
from sqlalchemy.sql.expression import ClauseElement
from sqlalchemy.sql.expression import Executable

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



## ... source file abbreviated to get to CreateIndex examples ...


                super(MSSQLImpl, self).alter_column(
                    table_name,
                    column_name,
                    schema=schema,
                    server_default=server_default,
                )

        if name is not None:
            super(MSSQLImpl, self).alter_column(
                table_name, column_name, schema=schema, name=name
            )

    def create_index(self, index):
        # this likely defaults to None if not present, so get()
        # should normally not return the default value.  being
        # defensive in any case
        mssql_include = index.kwargs.get("mssql_include", None) or ()
        for col in mssql_include:
            if col not in index.table.c:
                index.table.append_column(Column(col, sqltypes.NullType))
~~        self._exec(CreateIndex(index))

    def bulk_insert(self, table, rows, **kw):
        if self.as_sql:
            self._exec(
                "SET IDENTITY_INSERT %s ON"
                % self.dialect.identifier_preparer.format_table(table)
            )
            super(MSSQLImpl, self).bulk_insert(table, rows, **kw)
            self._exec(
                "SET IDENTITY_INSERT %s OFF"
                % self.dialect.identifier_preparer.format_table(table)
            )
        else:
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


## ... source file continues with no further CreateIndex examples...


```

