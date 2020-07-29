title: sqlalchemy.engine Connection Example Code
category: page
slug: sqlalchemy-engine-connection-examples
sortorder: 500031021
toc: False
sidebartitle: sqlalchemy.engine Connection
meta: Example code for understanding how to use the Connection class from the sqlalchemy.engine module of the SQLAlchemy project.


`Connection` is a class within the `sqlalchemy.engine` module of the SQLAlchemy project.

<a href="/sqlalchemy-engine-engine-examples.html">Engine</a>,
<a href="/sqlalchemy-engine-create-engine-examples.html">create_engine</a>,
<a href="/sqlalchemy-engine-default-examples.html">default</a>,
and <a href="/sqlalchemy-engine-url-examples.html">url</a>
are several other callables with code examples from the same `sqlalchemy.engine` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / runtime / migration.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/runtime/migration.py)

```python
# migration.py
from contextlib import contextmanager
import logging
import sys

from sqlalchemy import Column
from sqlalchemy import literal_column
from sqlalchemy import MetaData
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import Table
~~from sqlalchemy.engine import Connection
from sqlalchemy.engine import url as sqla_url
from sqlalchemy.engine.strategies import MockEngineStrategy

from .. import ddl
from .. import util
from ..util import sqla_compat
from ..util.compat import callable
from ..util.compat import EncodedIO

log = logging.getLogger(__name__)


class _ProxyTransaction(object):
    def __init__(self, migration_context):
        self.migration_context = migration_context

    @property
    def _proxied_transaction(self):
        return self.migration_context._transaction

    def rollback(self):
        self._proxied_transaction.rollback()

    def commit(self):


## ... source file abbreviated to get to Connection examples ...


            log.info("Generating static SQL")
        log.info(
            "Will assume %s DDL.",
            "transactional"
            if self.impl.transactional_ddl
            else "non-transactional",
        )

    @classmethod
    def configure(
        cls,
        connection=None,
        url=None,
        dialect_name=None,
        dialect=None,
        environment_context=None,
        dialect_opts=None,
        opts=None,
    ):
        if opts is None:
            opts = {}
        if dialect_opts is None:
            dialect_opts = {}

        if connection:
~~            if not isinstance(connection, Connection):
                util.warn(
                    "'connection' argument to configure() is expected "
                    "to be a sqlalchemy.engine.Connection instance, "
                    "got %r" % connection,
                    stacklevel=3,
                )

            dialect = connection.dialect
        elif url:
            url = sqla_url.make_url(url)
            dialect = url.get_dialect()(**dialect_opts)
        elif dialect_name:
            url = sqla_url.make_url("%s://" % dialect_name)
            dialect = url.get_dialect()(**dialect_opts)
        elif not dialect:
            raise Exception("Connection, url, or dialect_name is required.")

        return MigrationContext(dialect, connection, opts, environment_context)

    @contextmanager
    def autocommit_block(self):
        _in_connection_transaction = self._in_connection_transaction()

        if self.impl.transactional_ddl:


## ... source file continues with no further Connection examples...

```


## Example 2 from GINO
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


## ... source file abbreviated to get to Connection examples ...



class _ReusingDBAPIConnection(_BaseDBAPIConnection):
    def __init__(self, cursor_cls, root):
        super().__init__(cursor_cls)
        self._root = root

    @property
    def raw_connection(self):
        return self._root.raw_connection

    async def _acquire(self, timeout):
        return await self._root.acquire(timeout=timeout)

    async def _release(self):
        pass


class _bypass_no_param:
    def keys(self):
        return []


_bypass_no_param = _bypass_no_param()


~~class _SAConnection(Connection):
    def _execute_context(self, dialect, constructor, statement, parameters, *args):
        if parameters == [_bypass_no_param]:
            constructor = getattr(
                self.dialect.execution_ctx_cls,
                constructor.__name__ + "_prepared",
                constructor,
            )
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


## ... source file abbreviated to get to Connection examples ...



    async def one(self, clause, *multiparams, **params):
        async with self.acquire(reuse=True) as conn:
            return await conn.one(clause, *multiparams, **params)

    async def scalar(self, clause, *multiparams, **params):
        async with self.acquire(reuse=True) as conn:
            return await conn.scalar(clause, *multiparams, **params)

    async def status(self, clause, *multiparams, **params):
        async with self.acquire(reuse=True) as conn:
            return await conn.status(clause, *multiparams, **params)

    def compile(self, clause, *multiparams, **params):
        return self._dialect.compile(clause, *multiparams, **params)

    def transaction(self, *args, timeout=None, reuse=True, reusable=True, **kwargs):
        return _TransactionContext(
            self.acquire(timeout=timeout, reuse=reuse, reusable=reusable),
            (args, kwargs),
        )

    def iterate(self, clause, *multiparams, **params):
        connection = self.current_connection
        if connection is None:
~~            raise ValueError("No Connection in context, please provide one")
        return connection.iterate(clause, *multiparams, **params)

    def update_execution_options(self, **opt):
        self._sa_engine.update_execution_options(**opt)

    async def _run_visitor(self, *args, **kwargs):
        async with self.acquire(reuse=True) as conn:
            await getattr(conn, "_run_visitor")(*args, **kwargs)

    def repr(self, color=False):
        return self._pool.repr(color)

    def __repr__(self):
        return self.repr()



## ... source file continues with no further Connection examples...

```

