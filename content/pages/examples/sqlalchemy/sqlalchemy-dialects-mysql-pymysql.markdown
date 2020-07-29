title: sqlalchemy.dialects.mysql pymysql Example Code
category: page
slug: sqlalchemy-dialects-mysql-pymysql-examples
sortorder: 500031006
toc: False
sidebartitle: sqlalchemy.dialects.mysql pymysql
meta: Python example code that shows how to use the pymysql callable from the sqlalchemy.dialects.mysql module of the SQLAlchemy project.


`pymysql` is a callable within the `sqlalchemy.dialects.mysql` module of the SQLAlchemy project.



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

[**databases / databases / backends / mysql.py**](https://github.com/encode/databases/blob/master/databases/backends/mysql.py)

```python
# mysql.py
import getpass
import logging
import typing
import uuid

import aiomysql
~~from sqlalchemy.dialects.mysql import pymysql
from sqlalchemy.engine.interfaces import Dialect, ExecutionContext
from sqlalchemy.engine.result import ResultMetaData, RowProxy
from sqlalchemy.sql import ClauseElement
from sqlalchemy.types import TypeEngine

from databases.core import LOG_EXTRA, DatabaseURL
from databases.interfaces import ConnectionBackend, DatabaseBackend, TransactionBackend

logger = logging.getLogger("databases")


class MySQLBackend(DatabaseBackend):
    def __init__(
        self, database_url: typing.Union[DatabaseURL, str], **options: typing.Any
    ) -> None:
        self._database_url = DatabaseURL(database_url)
        self._options = options
~~        self._dialect = pymysql.dialect(paramstyle="pyformat")
        self._dialect.supports_native_decimal = True
        self._pool = None

    def _get_connection_kwargs(self) -> dict:
        url_options = self._database_url.options

        kwargs = {}
        min_size = url_options.get("min_size")
        max_size = url_options.get("max_size")
        ssl = url_options.get("ssl")

        if min_size is not None:
            kwargs["minsize"] = int(min_size)
        if max_size is not None:
            kwargs["maxsize"] = int(max_size)
        if ssl is not None:
            kwargs["ssl"] = {"true": True, "false": False}[ssl.lower()]

        for key, value in self._options.items():
            if key == "min_size":
                key = "minsize"
            elif key == "max_size":
                key = "maxsize"
            kwargs[key] = value


## ... source file continues with no further pymysql examples...

```

