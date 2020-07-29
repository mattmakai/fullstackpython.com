title: sqlalchemy.engine Engine Example Code
category: page
slug: sqlalchemy-engine-engine-examples
sortorder: 500031022
toc: False
sidebartitle: sqlalchemy.engine Engine
meta: Example code for understanding how to use the Engine class from the sqlalchemy.engine module of the SQLAlchemy project.


`Engine` is a class within the `sqlalchemy.engine` module of the SQLAlchemy project.

<a href="/sqlalchemy-engine-connection-examples.html">Connection</a>,
<a href="/sqlalchemy-engine-create-engine-examples.html">create_engine</a>,
<a href="/sqlalchemy-engine-default-examples.html">default</a>,
and <a href="/sqlalchemy-engine-url-examples.html">url</a>
are several other callables with code examples from the same `sqlalchemy.engine` package.

## Example 1 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [SQLAlchemy](/sqlalchemy.html) and [Flask](/flask.html).
The application can be used as-is to run CTF events, or the code can be
modified for custom rules on hacking scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / CTFd / __init__.py**](https://github.com/CTFd/CTFd/blob/master/./CTFd/__init__.py)

```python
# __init__.py
import datetime
import os
import sys
import weakref
from distutils.version import StrictVersion

import jinja2
from flask import Flask, Request
from flask_migrate import upgrade
from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.utils import cached_property

from CTFd import utils
from CTFd.plugins import init_plugins
from CTFd.utils.crypto import sha256
from CTFd.utils.initialization import (
    init_events,
    init_logs,
    init_request_processors,
    init_template_filters,
    init_template_globals,
)
from CTFd.utils.migrations import create_database, migrations, stamp_latest_revision
from CTFd.utils.sessions import CachingSessionInterface
from CTFd.utils.updates import update_check

__version__ = "3.0.0b2"


class CTFdRequest(Request):
    @cached_property
    def path(self):
        return self.script_root + super(CTFdRequest, self).path


## ... source file abbreviated to get to Engine examples ...


            }
        )
        app.jinja_loader = jinja2.ChoiceLoader([app.theme_loader, app.plugin_loader])

        from CTFd.models import (  # noqa: F401
            db,
            Teams,
            Solves,
            Challenges,
            Fails,
            Flags,
            Tags,
            Files,
            Tracking,
        )

        url = create_database()

        app.config["SQLALCHEMY_DATABASE_URI"] = str(url)

        db.init_app(app)

        migrations.init_app(app, db)

        if url.drivername.startswith("sqlite"):
~~            from sqlalchemy.engine import Engine
            from sqlalchemy import event

~~            @event.listens_for(Engine, "connect")
            def set_sqlite_pragma(dbapi_connection, connection_record):
                cursor = dbapi_connection.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()

            db.create_all()
            stamp_latest_revision()
        else:
            upgrade()

        from CTFd.models import ma

        ma.init_app(app)

        app.db = db
        app.VERSION = __version__

        from CTFd.cache import cache

        cache.init_app(app)
        app.cache = cache

        reverse_proxy = app.config.get("REVERSE_PROXY")
        if reverse_proxy:


## ... source file continues with no further Engine examples...

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

