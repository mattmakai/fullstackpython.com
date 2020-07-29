title: sqlalchemy.engine.result RowProxy Example Code
category: page
slug: sqlalchemy-engine-result-rowproxy-examples
sortorder: 500031029
toc: False
sidebartitle: sqlalchemy.engine.result RowProxy
meta: Example code for understanding how to use the RowProxy class from the sqlalchemy.engine.result module of the SQLAlchemy project.


`RowProxy` is a class within the `sqlalchemy.engine.result` module of the SQLAlchemy project.

<a href="/sqlalchemy-engine-result-resultmetadata-examples.html">ResultMetaData</a>
is another callable from the `sqlalchemy.engine.result` package with code examples.

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
from sqlalchemy.dialects.sqlite import pysqlite
from sqlalchemy.engine.interfaces import Dialect, ExecutionContext
~~from sqlalchemy.engine.result import ResultMetaData, RowProxy
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
        self._dialect = pysqlite.dialect(paramstyle="qmark")
        self._dialect.supports_native_decimal = False
        self._pool = SQLitePool(self._database_url, **self._options)

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        pass


## ... source file abbreviated to get to RowProxy examples ...




class SQLiteConnection(ConnectionBackend):
    def __init__(self, pool: SQLitePool, dialect: Dialect):
        self._pool = pool
        self._dialect = dialect
        self._connection = None

    async def acquire(self) -> None:
        assert self._connection is None, "Connection is already acquired"
        self._connection = await self._pool.acquire()

    async def release(self) -> None:
        assert self._connection is not None, "Connection is not acquired"
        await self._pool.release(self._connection)
        self._connection = None

    async def fetch_all(self, query: ClauseElement) -> typing.List[typing.Mapping]:
        assert self._connection is not None, "Connection is not acquired"
        query, args, context = self._compile(query)

        async with self._connection.execute(query, args) as cursor:
            rows = await cursor.fetchall()
            metadata = ResultMetaData(context, cursor.description)
            return [
~~                RowProxy(metadata, row, metadata._processors, metadata._keymap)
                for row in rows
            ]

    async def fetch_one(self, query: ClauseElement) -> typing.Optional[typing.Mapping]:
        assert self._connection is not None, "Connection is not acquired"
        query, args, context = self._compile(query)

        async with self._connection.execute(query, args) as cursor:
            row = await cursor.fetchone()
            if row is None:
                return None
            metadata = ResultMetaData(context, cursor.description)
~~            return RowProxy(metadata, row, metadata._processors, metadata._keymap)

    async def execute(self, query: ClauseElement) -> typing.Any:
        assert self._connection is not None, "Connection is not acquired"
        query, args, context = self._compile(query)
        cursor = await self._connection.cursor()
        try:
            await cursor.execute(query, args)
            if cursor.lastrowid == 0:
                return cursor.rowcount
            return cursor.lastrowid
        finally:
            await cursor.close()

    async def execute_many(self, queries: typing.List[ClauseElement]) -> None:
        assert self._connection is not None, "Connection is not acquired"
        for single_query in queries:
            await self.execute(single_query)

    async def iterate(
        self, query: ClauseElement
    ) -> typing.AsyncGenerator[typing.Any, None]:
        assert self._connection is not None, "Connection is not acquired"
        query, args, context = self._compile(query)
        cursor = await self._connection.cursor()
        async with self._connection.execute(query, args) as cursor:
            metadata = ResultMetaData(context, cursor.description)
            async for row in cursor:
~~                yield RowProxy(metadata, row, metadata._processors, metadata._keymap)

    def transaction(self) -> TransactionBackend:
        return SQLiteTransaction(self)

    def _compile(
        self, query: ClauseElement
    ) -> typing.Tuple[str, list, CompilationContext]:
        compiled = query.compile(dialect=self._dialect)
        args = []
        for key, raw_val in compiled.construct_params().items():
            if key in compiled._bind_processors:
                val = compiled._bind_processors[key](raw_val)
            else:
                val = raw_val
            args.append(val)

        execution_context = self._dialect.execution_ctx_cls()
        execution_context.dialect = self._dialect
        execution_context.result_column_struct = (
            compiled._result_columns,
            compiled._ordered_columns,
            compiled._textual_ordered_columns,
        )



## ... source file continues with no further RowProxy examples...

```

