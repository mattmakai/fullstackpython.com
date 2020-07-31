title: sqlalchemy.sql schema Example Code
category: page
slug: sqlalchemy-sql-schema-examples
sortorder: 500031114
toc: False
sidebartitle: sqlalchemy.sql schema
meta: Python example code that shows how to use the schema callable from the sqlalchemy.sql module of the SQLAlchemy project.


`schema` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
<a href="/sqlalchemy-sql-extract-examples.html">extract</a>,
<a href="/sqlalchemy-sql-functions-examples.html">functions</a>,
<a href="/sqlalchemy-sql-operators-examples.html">operators</a>,
<a href="/sqlalchemy-sql-select-examples.html">select</a>,
<a href="/sqlalchemy-sql-sqltypes-examples.html">sqltypes</a>,
and <a href="/sqlalchemy-sql-table-examples.html">table</a>
are several other callables with code examples from the same `sqlalchemy.sql` package.

## Example 1 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / engine.py**](https://github.com/python-gino/gino/blob/master/src/gino/./engine.py)

```python
# engine.py
import asyncio
import collections
import functools
import sys
import time
from contextvars import ContextVar

from sqlalchemy.cutils import _distill_params
from sqlalchemy.engine import Engine, Connection
~~from sqlalchemy.sql import schema

from .aiocontextvars import patch_asyncio
from .exceptions import MultipleResultsFound, NoResultFound
from .transaction import GinoTransaction

patch_asyncio()


class _BaseDBAPIConnection:
    _reset_agent = None
    gino_conn = None

    def __init__(self, cursor_cls):
        self._cursor_cls = cursor_cls
        self._closed = False

    def commit(self):
        pass

    def cursor(self):
        return self._cursor_cls(self)

    @property
    def raw_connection(self):


## ... source file abbreviated to get to schema examples ...


        self._tx_ctx = args

    async def __aenter__(self):
        conn = await self._conn_ctx.__aenter__()
        try:
            args, kwargs = self._tx_ctx
            self._tx_ctx = conn.transaction(*args, **kwargs)
            return await self._tx_ctx.__aenter__()
        except Exception:
            await self._conn_ctx.__aexit__(*sys.exc_info())
            raise

    async def __aexit__(self, *exc_info):
        try:
            tx, self._tx_ctx = self._tx_ctx, None
            return await tx.__aexit__(*exc_info)
        except Exception:
            exc_info = sys.exc_info()
            raise
        finally:
            await self._conn_ctx.__aexit__(*exc_info)


class GinoConnection:

~~    schema_for_object = schema._schema_getter(None)

    def __init__(self, dialect, sa_conn, stack=None):
        self._dialect = dialect
        self._sa_conn = sa_conn
        self._stack = stack

    @property
    def _dbapi_conn(self):
        return self._sa_conn.connection

    @property
    def raw_connection(self):
        return self._dbapi_conn.raw_connection

    async def get_raw_connection(self, *, timeout=None):
        return await self._dbapi_conn.acquire(timeout=timeout)

    async def release(self, *, permanent=True):
        if permanent and self._stack is not None:
            dbapi_conn = self._stack.remove(lambda x: x.gino_conn is self)
            if dbapi_conn:
                await dbapi_conn.release(True)
            else:
                raise ValueError("This connection is already released.")


## ... source file continues with no further schema examples...

```

