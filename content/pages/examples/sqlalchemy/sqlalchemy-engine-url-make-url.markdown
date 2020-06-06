title: sqlalchemy.engine.url make_url code examples
category: page
slug: sqlalchemy-engine-url-make-url-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.engine.url make_url
meta: Python example code for the make_url function from the sqlalchemy.engine.url module of the SQLAlchemy project.


make_url is a function within the sqlalchemy.engine.url module of the SQLAlchemy project.


## Example 1 from flask-sqlalchemy
[flask-sqlalchemy](https://github.com/pallets/flask-sqlalchemy)
([project documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
and
[PyPI information](https://pypi.org/project/Flask-SQLAlchemy/)) is a
[Flask](/flask.html) extension that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) when building Flask apps. flask-sqlalchemy
provides helper functions that reduce the amount of common boilerplate
code that you have to frequently write yourself if you did not use this
library when combining Flask with SQLAlchemy.

flask-sqlalchemy is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/pallets/flask-sqlalchemy/blob/master/LICENSE.rst).

[**flask-sqlalchemy / src/flask_sqlalchemy / __init__.py**](https://github.com/pallets/flask-sqlalchemy/blob/master/src/flask_sqlalchemy/./__init__.py)

```python
# __init__.py
import functools
import os
import sys
import warnings
from math import ceil
from operator import itemgetter
from threading import Lock
from time import perf_counter

import sqlalchemy
from flask import _app_ctx_stack
from flask import abort
from flask import current_app
from flask import request
from flask.signals import Namespace
from sqlalchemy import event
from sqlalchemy import inspect
from sqlalchemy import orm
~~from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.orm.session import Session as SessionBase

from .model import DefaultMeta
from .model import Model

__version__ = "3.0.0.dev"

_signals = Namespace()
models_committed = _signals.signal("models-committed")
before_models_committed = _signals.signal("before-models-committed")


def _make_table(db):
    def _make_table(*args, **kwargs):
        if len(args) > 1 and isinstance(args[1], db.Column):
            args = (args[0], db.metadata) + args[1:]
        info = kwargs.pop("info", None) or {}
        info.setdefault("bind_key", None)
        kwargs["info"] = info
        return sqlalchemy.Table(*args, **kwargs)



## ... source file abbreviated to get to make_url examples ...


        self._connected_for = None
        self._bind = bind
        self._lock = Lock()

    def get_uri(self):
        if self._bind is None:
            return self._app.config["SQLALCHEMY_DATABASE_URI"]
        binds = self._app.config.get("SQLALCHEMY_BINDS") or ()
        assert (
            self._bind in binds
        ), f"Bind {self._bind!r} is not configured in 'SQLALCHEMY_BINDS'."
        return binds[self._bind]

    def get_engine(self):
        with self._lock:
            uri = self.get_uri()
            echo = self._app.config["SQLALCHEMY_ECHO"]
            if (uri, echo) == self._connected_for:
                return self._engine

~~            sa_url = make_url(uri)
            options = self.get_options(sa_url, echo)
            self._engine = rv = self._sa.create_engine(sa_url, options)

            if _record_queries(self._app):
                _EngineDebuggingSignalEvents(
                    self._engine, self._app.import_name
                ).register()

            self._connected_for = (uri, echo)

            return rv

    def get_options(self, sa_url, echo):
        options = {}

        self._sa.apply_driver_hacks(self._app, sa_url, options)

        if echo:
            options["echo"] = echo

        # Give the config options set by a developer explicitly priority
        # over decisions FSA makes.
        options.update(self._app.config["SQLALCHEMY_ENGINE_OPTIONS"])
        # Give options set in SQLAlchemy.__init__() ultimate priority


## ... source file continues with no further make_url examples...


```


## Example 2 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / functions / database.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/database.py)

```python
# database.py
try:
    from collections.abc import Mapping, Sequence
except ImportError:  # For python 2.7 support
    from collections import Mapping, Sequence
import itertools
import os
from copy import copy

import sqlalchemy as sa
~~from sqlalchemy.engine.url import make_url
from sqlalchemy.exc import OperationalError, ProgrammingError

from ..utils import starts_with
from .orm import quote


def escape_like(string, escape_char='*'):
    """
    Escape the string paremeter used in SQL LIKE expressions.

    ::

        from sqlalchemy_utils import escape_like


        query = session.query(User).filter(
            User.name.ilike(escape_like('John'))
        )


    :param string: a string to escape
    :param escape_char: escape character
    """
    return (


## ... source file abbreviated to get to make_url examples ...


        database_exists(engine.url)  #=> True

    """

    def get_scalar_result(engine, sql):
        result_proxy = engine.execute(sql)
        result = result_proxy.scalar()
        result_proxy.close()
        engine.dispose()
        return result

    def sqlite_file_exists(database):
        if not os.path.isfile(database) or os.path.getsize(database) < 100:
            return False

        with open(database, 'rb') as f:
            header = f.read(100)

        return header[:16] == b'SQLite format 3\x00'

~~    url = copy(make_url(url))
    database = url.database
    if url.drivername.startswith('postgres'):
        url.database = 'postgres'
    else:
        url.database = None

    engine = sa.create_engine(url)

    if engine.dialect.name == 'postgresql':
        text = "SELECT 1 FROM pg_database WHERE datname='%s'" % database
        return bool(get_scalar_result(engine, text))

    elif engine.dialect.name == 'mysql':
        text = ("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA "
                "WHERE SCHEMA_NAME = '%s'" % database)
        return bool(get_scalar_result(engine, text))

    elif engine.dialect.name == 'sqlite':
        if database:
            return database == ':memory:' or sqlite_file_exists(database)
        else:
            # The default SQLAlchemy database is in memory,
            # and :memory is not required, thus we should support that use-case
            return True


## ... source file abbreviated to get to make_url examples ...



    :param url: A SQLAlchemy engine URL.
    :param encoding: The encoding to create the database as.
    :param template:
        The name of the template from which to create the new database. At the
        moment only supported by PostgreSQL driver.

    To create a database, you can pass a simple URL that would have
    been passed to ``create_engine``. ::

        create_database('postgresql://postgres@localhost/name')

    You may also pass the url from an existing engine. ::

        create_database(engine.url)

    Has full support for mysql, postgres, and sqlite. In theory,
    other database engines should be supported.
    """

~~    url = copy(make_url(url))

    database = url.database

    if url.drivername.startswith('postgres'):
        url.database = 'postgres'
    elif url.drivername.startswith('mssql'):
        url.database = 'master'
    elif not url.drivername.startswith('sqlite'):
        url.database = None

    if url.drivername == 'mssql+pyodbc':
        engine = sa.create_engine(url, connect_args={'autocommit': True})
    elif url.drivername == 'postgresql+pg8000':
        engine = sa.create_engine(url, isolation_level='AUTOCOMMIT')
    else:
        engine = sa.create_engine(url)
    result_proxy = None

    if engine.dialect.name == 'postgresql':
        if not template:
            template = 'template1'

        text = "CREATE DATABASE {0} ENCODING '{1}' TEMPLATE {2}".format(
            quote(engine, database),


## ... source file abbreviated to get to make_url examples ...


        result_proxy = engine.execute(text)

    if result_proxy is not None:
        result_proxy.close()
    engine.dispose()


def drop_database(url):
    """Issue the appropriate DROP DATABASE statement.

    :param url: A SQLAlchemy engine URL.

    Works similar to the :ref:`create_database` method in that both url text
    and a constructed url are accepted. ::

        drop_database('postgresql://postgres@localhost/name')
        drop_database(engine.url)

    """

~~    url = copy(make_url(url))

    database = url.database

    if url.drivername.startswith('postgres'):
        url.database = 'postgres'
    elif url.drivername.startswith('mssql'):
        url.database = 'master'
    elif not url.drivername.startswith('sqlite'):
        url.database = None

    if url.drivername == 'mssql+pyodbc':
        engine = sa.create_engine(url, connect_args={'autocommit': True})
    elif url.drivername == 'postgresql+pg8000':
        engine = sa.create_engine(url, isolation_level='AUTOCOMMIT')
    else:
        engine = sa.create_engine(url)
    conn_resource = None

    if engine.dialect.name == 'sqlite' and database != ':memory:':
        if database:
            os.remove(database)

    elif (
                engine.dialect.name == 'postgresql' and


## ... source file continues with no further make_url examples...


```


## Example 3 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / api.py**](https://github.com/python-gino/gino/blob/master/src/gino/./api.py)

```python
# api.py
import weakref

import sqlalchemy as sa
~~from sqlalchemy.engine.url import make_url, URL
from sqlalchemy.sql.base import Executable
from sqlalchemy.sql.schema import SchemaItem

from . import json_support
from .crud import CRUDModel
from .declarative import declarative_base, declared_attr
from .exceptions import UninitializedError
from .schema import GinoSchemaVisitor, patch_schema


class GinoExecutor:
    """
    The default ``gino`` extension on
    :class:`-sqlalchemy.sql.expression.Executable` constructs for implicit
    execution.

    Instances of this class are created when visiting the ``gino`` property of
    :class:`-sqlalchemy.sql.expression.Executable` instances (also referred as
    queries or clause elements), for example::

        await User.query.gino.first()

    This allows GINO to add the asynchronous query APIs (:meth:`all`,
    :meth:`first`, :meth:`one`, :meth:`one_or_none`, :meth:`scalar`,


## ... source file abbreviated to get to make_url examples ...


            return _PlaceHolder(UninitializedError("Gino engine is not initialized."))
        return self._bind

    # noinspection PyMethodOverriding,PyAttributeOutsideInit
    @bind.setter
    def bind(self, bind):
        self._bind = bind

    async def set_bind(self, bind, loop=None, **kwargs):
        """
        Bind self to the given :class:`-.engine.GinoEngine` and return it.

        If the given ``bind`` is a string or
        :class:`-sqlalchemy.engine.url.URL`, all arguments will be sent to
        :func:`-gino.create_engine` to create a new engine, and return it.

        :return: :class:`-.engine.GinoEngine`

        """
        if isinstance(bind, str):
~~            bind = make_url(bind)
        if isinstance(bind, URL):
            from . import create_engine

            bind = await create_engine(bind, loop=loop, bakery=self._bakery, **kwargs)
        self.bind = bind
        return bind

    def pop_bind(self):
        """
        Unbind self, and return the bound engine.

        This is usually used in a chained call to close the engine::

            await db.pop_bind().close()

        :return: :class:`-.engine.GinoEngine` or ``None`` if self is not bound.

        """
        from .bakery import Bakery

        self._bakery = Bakery()
        bind, self.bind = self.bind, None
        return bind



## ... source file continues with no further make_url examples...


```

