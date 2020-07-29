title: sqlalchemy.engine.url make_url Example Code
category: page
slug: sqlalchemy-engine-url-make-url-examples
sortorder: 500031032
toc: False
sidebartitle: sqlalchemy.engine.url make_url
meta: Python example code that shows how to use the make_url callable from the sqlalchemy.engine.url module of the SQLAlchemy project.


`make_url` is a callable within the `sqlalchemy.engine.url` module of the SQLAlchemy project.



## Example 1 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [SQLAlchemy](/sqlalchemy.html) and [Flask](/flask.html).
The application can be used as-is to run CTF events, or the code can be
modified for custom rules on hacking scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / tests / helpers.py**](https://github.com/CTFd/CTFd/blob/master/./tests/helpers.py)

```python
# helpers.py
import datetime
import gc
import random
import string
import uuid
from collections import namedtuple
from unittest.mock import Mock, patch

import requests
from flask.testing import FlaskClient
~~from sqlalchemy.engine.url import make_url
from sqlalchemy_utils import drop_database
from werkzeug.datastructures import Headers

from CTFd import create_app
from CTFd.cache import cache, clear_standings
from CTFd.config import TestingConfig
from CTFd.models import (
    Awards,
    ChallengeFiles,
    Challenges,
    Fails,
    Files,
    Flags,
    Hints,
    Notifications,
    PageFiles,
    Pages,
    Solves,
    Tags,
    Teams,
    Tokens,
    Tracking,
    Unlocks,
    Users,


## ... source file abbreviated to get to make_url examples ...


                if isinstance(headers, dict):
                    headers = Headers(headers)
                headers.extend(api_key_headers)
                kwargs["headers"] = headers
        return super(CTFdTestClient, self).open(*args, **kwargs)


def create_ctfd(
    ctf_name="CTFd",
    ctf_description="CTF description",
    name="admin",
    email="admin@ctfd.io",
    password="password",
    user_mode="users",
    setup=True,
    enable_plugins=False,
    application_root="/",
    config=TestingConfig,
):
    if enable_plugins:
        config.SAFE_MODE = False
    else:
        config.SAFE_MODE = True

    config.APPLICATION_ROOT = application_root
~~    url = make_url(config.SQLALCHEMY_DATABASE_URI)
    if url.database:
        url.database = str(uuid.uuid4())
    config.SQLALCHEMY_DATABASE_URI = str(url)

    app = create_app(config)
    app.test_client_class = CTFdTestClient

    if setup:
        app = setup_ctfd(
            app,
            ctf_name=ctf_name,
            ctf_description=ctf_description,
            name=name,
            email=email,
            password=password,
            user_mode=user_mode,
        )
    return app


def setup_ctfd(
    app,
    ctf_name="CTFd",
    ctf_description="CTF description",


## ... source file continues with no further make_url examples...

```


## Example 2 from flask-sqlalchemy
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


class _EngineConnector:
    def __init__(self, sa, app, bind=None):
        self._sa = sa
        self._app = app
        self._engine = None
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

        options.update(self._app.config["SQLALCHEMY_ENGINE_OPTIONS"])
        options.update(self._sa._engine_options)
        return options



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

    __slots__ = ("_query",)

    def __init__(self, query):
        self._query = query

    @property
    def query(self):
        return self._query

    def model(self, model):
        if model is not None:
            model = weakref.ref(model)


## ... source file abbreviated to get to make_url examples ...


                if not hasattr(self, key) and key not in self.no_delegate:
                    setattr(self, key, getattr(mod, key))
        if ext:
            if query_ext:
                Executable.gino = property(self.query_executor)
            if schema_ext:
                SchemaItem.gino = property(self.schema_visitor)
                patch_schema(self)

    @property
    def Model(self):
        return self._model

    @property
    def bind(self):
        if self._bind is None:
            return _PlaceHolder(UninitializedError("Gino engine is not initialized."))
        return self._bind

    @bind.setter
    def bind(self, bind):
        self._bind = bind

    async def set_bind(self, bind, loop=None, **kwargs):
        if isinstance(bind, str):
~~            bind = make_url(bind)
        if isinstance(bind, URL):
            from . import create_engine

            bind = await create_engine(bind, loop=loop, bakery=self._bakery, **kwargs)
        self.bind = bind
        return bind

    def pop_bind(self):
        from .bakery import Bakery

        self._bakery = Bakery()
        bind, self.bind = self.bind, None
        return bind

    def with_bind(self, bind, loop=None, **kwargs):
        return _BindContext(self, bind, loop, kwargs)

    def __await__(self):
        async def init():
            await self.set_bind(self.bind)
            return self

        return init().__await__()



## ... source file continues with no further make_url examples...

```

