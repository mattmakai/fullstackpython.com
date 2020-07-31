title: sqlalchemy.pool StaticPool Example Code
category: page
slug: sqlalchemy-pool-staticpool-examples
sortorder: 500031097
toc: False
sidebartitle: sqlalchemy.pool StaticPool
meta: Example code for understanding how to use the StaticPool class from the sqlalchemy.pool module of the SQLAlchemy project.


`StaticPool` is a class within the `sqlalchemy.pool` module of the SQLAlchemy project.

<a href="/sqlalchemy-pool-nullpool-examples.html">NullPool</a>
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


## ... source file abbreviated to get to StaticPool examples ...


            if app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]:
                warnings.warn(
                    "'COMMIT_ON_TEARDOWN' is deprecated and will be"
                    " removed in version 3.1. Call"
                    " 'db.session.commit()'` directly instead.",
                    DeprecationWarning,
                )

                if response_or_exc is None:
                    self.session.commit()

            self.session.remove()
            return response_or_exc

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
~~                from sqlalchemy.pool import StaticPool

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
                from sqlalchemy.pool import NullPool

                options["poolclass"] = NullPool

            if not detected_in_memory and not os.path.isabs(sa_url.database):
                os.makedirs(app.instance_path, exist_ok=True)
                sa_url.database = os.path.join(app.instance_path, sa_url.database)

    @property
    def engine(self):
        return self.get_engine()


## ... source file continues with no further StaticPool examples...

```

