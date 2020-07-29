title: sqlalchemy.dialects.postgresql pypostgresql Example Code
category: page
slug: sqlalchemy-dialects-postgresql-pypostgresql-examples
sortorder: 500031015
toc: False
sidebartitle: sqlalchemy.dialects.postgresql pypostgresql
meta: Python example code that shows how to use the pypostgresql callable from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


`pypostgresql` is a callable within the `sqlalchemy.dialects.postgresql` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-postgresql-array-examples.html">ARRAY</a>,
<a href="/sqlalchemy-dialects-postgresql-bigint-examples.html">BIGINT</a>,
<a href="/sqlalchemy-dialects-postgresql-bit-examples.html">BIT</a>,
<a href="/sqlalchemy-dialects-postgresql-double-precision-examples.html">DOUBLE_PRECISION</a>,
<a href="/sqlalchemy-dialects-postgresql-excludeconstraint-examples.html">ExcludeConstraint</a>,
<a href="/sqlalchemy-dialects-postgresql-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">JSON</a>,
<a href="/sqlalchemy-dialects-postgresql-tsvector-examples.html">TSVECTOR</a>,
<a href="/sqlalchemy-dialects-postgresql-array-examples.html">array</a>,
and <a href="/sqlalchemy-dialects-postgresql-json-examples.html">json</a>
are several other callables with code examples from the same `sqlalchemy.dialects.postgresql` package.

## Example 1 from databases
[databases](https://github.com/encode/databases)
([project homepage](https://www.encode.io/databases/)
and
[PyPI page](https://pypi.org/project/databases/) provides
[asyncio](https://docs.python.org/3/library/asyncio.html) support
with an [SQLALchemy](/sqlalchemy.html) Core interface for common
[relational databases](/databases.html) such as [MySQL](/mysql.html),
[PostgreSQL](/postgresql.html) and [SQLite](/sqlite.html). This is
handy for integrating with asynchronous I/O
[web frameworks](/web-frameworks.html) like [Sanic](/sanic.html).
The project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/encode/databases/blob/master/LICENSE.md).

[**databases / databases / backends / postgres.py**](https://github.com/encode/databases/blob/master/databases/backends/postgres.py)

```python
# postgres.py
import logging
import typing
from collections.abc import Mapping

import asyncpg
~~from sqlalchemy.dialects.postgresql import pypostgresql
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.sql import ClauseElement
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import TypeEngine

from databases.core import LOG_EXTRA, DatabaseURL
from databases.interfaces import ConnectionBackend, DatabaseBackend, TransactionBackend

logger = logging.getLogger("databases")


_result_processors = {}  # type: dict


class PostgresBackend(DatabaseBackend):
    def __init__(
        self, database_url: typing.Union[DatabaseURL, str], **options: typing.Any
    ) -> None:
        self._database_url = DatabaseURL(database_url)
        self._options = options
        self._dialect = self._get_dialect()
        self._pool = None

    def _get_dialect(self) -> Dialect:
~~        dialect = pypostgresql.dialect(paramstyle="pyformat")

        dialect.implicit_returning = True
        dialect.supports_native_enum = True
        dialect.supports_smallserial = True  # 9.2+
        dialect._backslash_escapes = False
        dialect.supports_sane_multi_rowcount = True  # psycopg 2.0.9+
        dialect._has_native_hstore = True
        dialect.supports_native_decimal = True

        return dialect

    def _get_connection_kwargs(self) -> dict:
        url_options = self._database_url.options

        kwargs = {}
        min_size = url_options.get("min_size")
        max_size = url_options.get("max_size")
        ssl = url_options.get("ssl")

        if min_size is not None:
            kwargs["min_size"] = int(min_size)
        if max_size is not None:
            kwargs["max_size"] = int(max_size)
        if ssl is not None:


## ... source file continues with no further pypostgresql examples...

```

