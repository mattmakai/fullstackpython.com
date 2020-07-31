title: sqlalchemy.schema CreateIndex Example Code
category: page
slug: sqlalchemy-schema-createindex-examples
sortorder: 500031100
toc: False
sidebartitle: sqlalchemy.schema CreateIndex
meta: Example code for understanding how to use the CreateIndex class from the sqlalchemy.schema module of the SQLAlchemy project.


`CreateIndex` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
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



## ... source file continues with no further CreateIndex examples...

```

