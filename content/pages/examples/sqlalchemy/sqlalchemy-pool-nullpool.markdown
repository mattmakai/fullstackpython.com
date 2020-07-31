title: sqlalchemy.pool NullPool Example Code
category: page
slug: sqlalchemy-pool-nullpool-examples
sortorder: 500031096
toc: False
sidebartitle: sqlalchemy.pool NullPool
meta: Example code for understanding how to use the NullPool class from the sqlalchemy.pool module of the SQLAlchemy project.


`NullPool` is a class within the `sqlalchemy.pool` module of the SQLAlchemy project.

<a href="/sqlalchemy-pool-staticpool-examples.html">StaticPool</a>
is another callable from the `sqlalchemy.pool` package with code examples.

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
from sqlalchemy.engine.url import make_url
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


## ... source file abbreviated to get to NullPool examples ...


    def apply_driver_hacks(self, app, sa_url, options):
        if sa_url.drivername.startswith("mysql"):
            sa_url.query.setdefault("charset", "utf8")
            if sa_url.drivername != "mysql+gaerdbms":
                options.setdefault("pool_size", 10)
                options.setdefault("pool_recycle", 7200)
        elif sa_url.drivername == "sqlite":
            pool_size = options.get("pool_size")
            detected_in_memory = False
            if sa_url.database in (None, "", ":memory:"):
                detected_in_memory = True
                from sqlalchemy.pool import StaticPool

                options["poolclass"] = StaticPool
                if "connect_args" not in options:
                    options["connect_args"] = {}
                options["connect_args"]["check_same_thread"] = False

                if pool_size == 0:
                    raise RuntimeError(
                        "SQLite in memory database with an "
                        "empty queue not possible due to data "
                        "loss."
                    )
            elif not pool_size:
~~                from sqlalchemy.pool import NullPool

                options["poolclass"] = NullPool

            if not detected_in_memory and not os.path.isabs(sa_url.database):
                os.makedirs(app.instance_path, exist_ok=True)
                sa_url.database = os.path.join(app.instance_path, sa_url.database)

    @property
    def engine(self):
        return self.get_engine()

    def make_connector(self, app=None, bind=None):
        return _EngineConnector(self, self.get_app(app), bind)

    def get_engine(self, app=None, bind=None):

        app = self.get_app(app)
        state = get_state(app)

        with self._engine_lock:
            connector = state.connectors.get(bind)

            if connector is None:
                connector = self.make_connector(app, bind)


## ... source file continues with no further NullPool examples...

```


## Example 2 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management that is
powered by [SQLAlchemy](/sqlalchemy.html) on the backend. The code
for this project is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / cli / setup.py**](https://github.com/indico/indico/blob/master/indico/cli/setup.py)

```python
# setup.py

from __future__ import unicode_literals

import os
import re
import shutil
import socket
import sys
from operator import attrgetter
from smtplib import SMTP

import click
from click import wrap_text
from flask.helpers import get_root_path
from pkg_resources import iter_entry_points
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import PathCompleter, WordCompleter
from prompt_toolkit.layout.lexers import SimpleLexer
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token
from pytz import all_timezones, common_timezones
from redis import RedisError, StrictRedis
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
~~from sqlalchemy.pool import NullPool
from terminaltables import AsciiTable
from werkzeug.urls import url_parse

from indico.core.db.sqlalchemy.util.models import import_all_models
from indico.util.console import cformat
from indico.util.string import validate_email


click.disable_unicode_literals_warning = True


def _echo(msg=''):
    click.echo(msg, err=True)


def _warn(msg):
    msg = wrap_text(msg)
    click.echo(click.style(msg, fg='yellow'), err=True)


def _error(msg):
    msg = wrap_text(msg)
    click.echo(click.style(msg, fg='red', bold=True), err=True)



## ... source file continues with no further NullPool examples...

```

