title: sqlalchemy.engine Engine Example Code
category: page
slug: sqlalchemy-engine-engine-examples
sortorder: 500031019
toc: False
sidebartitle: sqlalchemy.engine Engine
meta: Python example code for the Engine class from the sqlalchemy.engine module of the SQLAlchemy project.


Engine is a class within the sqlalchemy.engine module of the SQLAlchemy project.


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
~~from sqlalchemy.engine import Engine, Connection
from sqlalchemy.sql import schema

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


## ... source file abbreviated to get to Engine examples ...


        return super()._execute_context(
            dialect, constructor, statement, parameters, *args
        )

    def _execute_baked_query(self, bq, multiparams, params):
        elem = bq.query
        if self._has_events or self.engine._has_events:
            for fn in self.dispatch.before_execute:
                _, multiparams, params = fn(self, elem, multiparams, params)

        distilled_params = _distill_params(multiparams, params)

        ret = self._execute_context(
            self.dialect,
            self.dialect.execution_ctx_cls._init_baked_query,
            bq.compiled_sql,
            distilled_params,
            bq,
            distilled_params,
        )
        if self._has_events or self.engine._has_events:
            self.dispatch.after_execute(self, elem, multiparams, params, ret)
        return ret


~~class _SAEngine(Engine):
    _connection_cls = _SAConnection

    def __init__(self, dialect, **kwargs):
        super().__init__(None, dialect, None, **kwargs)


class _AcquireContext:
    __slots__ = ["_acquire", "_conn"]

    def __init__(self, acquire):
        self._acquire = acquire
        self._conn = None

    async def __aenter__(self):
        self._conn = await self._acquire()
        return self._conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        conn, self._conn = self._conn, None
        await conn.release()

    def __await__(self):
        return self._acquire().__await__()



## ... source file continues with no further Engine examples...

```

