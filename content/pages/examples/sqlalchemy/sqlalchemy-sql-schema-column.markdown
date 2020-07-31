title: sqlalchemy.sql.schema Column Example Code
category: page
slug: sqlalchemy-sql-schema-column-examples
sortorder: 500031130
toc: False
sidebartitle: sqlalchemy.sql.schema Column
meta: Example code for understanding how to use the Column class from the sqlalchemy.sql.schema module of the SQLAlchemy project.


`Column` is a class within the `sqlalchemy.sql.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-schema-schemaitem-examples.html">SchemaItem</a>
is another callable from the `sqlalchemy.sql.schema` package with code examples.

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
from sqlalchemy.dialects.postgresql import pypostgresql
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.sql import ClauseElement
~~from sqlalchemy.sql.schema import Column
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
        dialect = pypostgresql.dialect(paramstyle="pyformat")

        dialect.implicit_returning = True


## ... source file abbreviated to get to Column examples ...


        "_column_map_full",
    )

    def __init__(
        self,
        row: asyncpg.Record,
        result_columns: tuple,
        dialect: Dialect,
        column_maps: typing.Tuple[
            typing.Mapping[typing.Any, typing.Tuple[int, TypeEngine]],
            typing.Mapping[int, typing.Tuple[int, TypeEngine]],
            typing.Mapping[str, typing.Tuple[int, TypeEngine]],
        ],
    ) -> None:
        self._row = row
        self._result_columns = result_columns
        self._dialect = dialect
        self._column_map, self._column_map_int, self._column_map_full = column_maps

    def values(self) -> typing.ValuesView:
        return self._row.values()

    def __getitem__(self, key: typing.Any) -> typing.Any:
        if len(self._column_map) == 0:  # raw query
            return self._row[key]
~~        elif isinstance(key, Column):
            idx, datatype = self._column_map_full[str(key)]
        elif isinstance(key, int):
            idx, datatype = self._column_map_int[key]
        else:
            idx, datatype = self._column_map[key]
        raw = self._row[idx]
        try:
            processor = _result_processors[datatype]
        except KeyError:
            processor = datatype.result_processor(self._dialect, None)
            _result_processors[datatype] = processor

        if processor is not None:
            return processor(raw)
        return raw

    def __iter__(self) -> typing.Iterator:
        return iter(self._row.keys())

    def __len__(self) -> int:
        return len(self._row)


class PostgresConnection(ConnectionBackend):


## ... source file continues with no further Column examples...

```

