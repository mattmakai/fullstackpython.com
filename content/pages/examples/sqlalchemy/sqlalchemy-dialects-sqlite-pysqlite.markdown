title: sqlalchemy.dialects.sqlite pysqlite Example Code
category: page
slug: sqlalchemy-dialects-sqlite-pysqlite-examples
sortorder: 500031020
toc: False
sidebartitle: sqlalchemy.dialects.sqlite pysqlite
meta: Python example code that shows how to use the pysqlite callable from the sqlalchemy.dialects.sqlite module of the SQLAlchemy project.


`pysqlite` is a callable within the `sqlalchemy.dialects.sqlite` module of the SQLAlchemy project.



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

[**databases / databases / backends / sqlite.py**](https://github.com/encode/databases/blob/master/databases/backends/sqlite.py)

```python
# sqlite.py
import logging
import typing
import uuid

import aiosqlite
~~from sqlalchemy.dialects.sqlite import pysqlite
from sqlalchemy.engine.interfaces import Dialect, ExecutionContext
from sqlalchemy.engine.result import ResultMetaData, RowProxy
from sqlalchemy.sql import ClauseElement
from sqlalchemy.types import TypeEngine

from databases.core import LOG_EXTRA, DatabaseURL
from databases.interfaces import ConnectionBackend, DatabaseBackend, TransactionBackend

logger = logging.getLogger("databases")


class SQLiteBackend(DatabaseBackend):
    def __init__(
        self, database_url: typing.Union[DatabaseURL, str], **options: typing.Any
    ) -> None:
        self._database_url = DatabaseURL(database_url)
        self._options = options
~~        self._dialect = pysqlite.dialect(paramstyle="qmark")
        self._dialect.supports_native_decimal = False
        self._pool = SQLitePool(self._database_url, **self._options)

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        pass

    def connection(self) -> "SQLiteConnection":
        return SQLiteConnection(self._pool, self._dialect)


class SQLitePool:
    def __init__(self, url: DatabaseURL, **options: typing.Any) -> None:
        self._url = url
        self._options = options

    async def acquire(self) -> aiosqlite.Connection:
        connection = aiosqlite.connect(
            database=self._url.database, isolation_level=None, **self._options
        )
        await connection.__aenter__()
        return connection


## ... source file continues with no further pysqlite examples...

```

