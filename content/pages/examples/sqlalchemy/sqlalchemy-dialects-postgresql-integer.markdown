title: sqlalchemy.dialects.postgresql INTEGER Example Code
category: page
slug: sqlalchemy-dialects-postgresql-integer-examples
sortorder: 500031012
toc: False
sidebartitle: sqlalchemy.dialects.postgresql INTEGER
meta: Python example code that shows how to use the INTEGER constant from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


`INTEGER` is a constant within the `sqlalchemy.dialects.postgresql` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-postgresql-array-examples.html">ARRAY</a>,
<a href="/sqlalchemy-dialects-postgresql-bigint-examples.html">BIGINT</a>,
<a href="/sqlalchemy-dialects-postgresql-bit-examples.html">BIT</a>,
<a href="/sqlalchemy-dialects-postgresql-double-precision-examples.html">DOUBLE_PRECISION</a>,
<a href="/sqlalchemy-dialects-postgresql-excludeconstraint-examples.html">ExcludeConstraint</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">JSON</a>,
<a href="/sqlalchemy-dialects-postgresql-tsvector-examples.html">TSVECTOR</a>,
<a href="/sqlalchemy-dialects-postgresql-array-examples.html">array</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">json</a>,
and <a href="/sqlalchemy-dialects-postgresql-pypostgresql-examples.html">pypostgresql</a>
are several other callables with code examples from the same `sqlalchemy.dialects.postgresql` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / ddl / postgresql.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/ddl/postgresql.py)

```python
# postgresql.py
import logging
import re

from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import text
from sqlalchemy import types as sqltypes
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.dialects.postgresql import ExcludeConstraint
~~from sqlalchemy.dialects.postgresql import INTEGER
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql.expression import UnaryExpression
from sqlalchemy.types import NULLTYPE

from .base import alter_column
from .base import alter_table
from .base import AlterColumn
from .base import ColumnComment
from .base import compiles
from .base import format_column_name
from .base import format_table_name
from .base import format_type
from .base import RenameTable
from .impl import DefaultImpl
from .. import util
from ..autogenerate import render
from ..operations import ops
from ..operations import schemaobj
from ..operations.base import BatchOperations
from ..operations.base import Operations
from ..util import compat
from ..util import sqla_compat




## ... source file abbreviated to get to INTEGER examples ...


                    schema=schema,
                    using=using,
                    existing_type=existing_type,
                    existing_server_default=existing_server_default,
                    existing_nullable=existing_nullable,
                )
            )

        super(PostgresqlImpl, self).alter_column(
            table_name,
            column_name,
            nullable=nullable,
            server_default=server_default,
            name=name,
            schema=schema,
            autoincrement=autoincrement,
            existing_type=existing_type,
            existing_server_default=existing_server_default,
            existing_nullable=existing_nullable,
            existing_autoincrement=existing_autoincrement,
            **kw
        )

    def autogen_column_reflect(self, inspector, table, column_info):
        if column_info.get("default") and isinstance(
~~            column_info["type"], (INTEGER, BIGINT)
        ):
            seq_match = re.match(
                r"nextval\('(.+?)'::regclass\)", column_info["default"]
            )
            if seq_match:
                info = sqla_compat._exec_on_inspector(
                    inspector,
                    text(
                        "select c.relname, a.attname "
                        "from pg_class as c join "
                        "pg_depend d on d.objid=c.oid and "
                        "d.classid='pg_class'::regclass and "
                        "d.refclassid='pg_class'::regclass "
                        "join pg_class t on t.oid=d.refobjid "
                        "join pg_attribute a on a.attrelid=t.oid and "
                        "a.attnum=d.refobjsubid "
                        "where c.relkind='S' and c.relname=:seqname"
                    ),
                    seqname=seq_match.group(1),
                ).first()
                if info:
                    seqname, colname = info
                    if colname == column_info["name"]:
                        log.info(


## ... source file continues with no further INTEGER examples...

```

