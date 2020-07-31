title: sqlalchemy.ext.declarative DeclarativeMeta Example Code
category: page
slug: sqlalchemy-ext-declarative-declarativemeta-examples
sortorder: 500031048
toc: False
sidebartitle: sqlalchemy.ext.declarative DeclarativeMeta
meta: Example code for understanding how to use the DeclarativeMeta class from the sqlalchemy.ext.declarative module of the SQLAlchemy project.


`DeclarativeMeta` is a class within the `sqlalchemy.ext.declarative` module of the SQLAlchemy project.

<a href="/sqlalchemy-ext-declarative-declarative-base-examples.html">declarative_base</a>
is another callable from the `sqlalchemy.ext.declarative` package with code examples.

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
~~from sqlalchemy.ext.declarative import DeclarativeMeta
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

    return _make_table



## ... source file abbreviated to get to DeclarativeMeta examples ...


        self._engine_options = engine_options or {}
        _include_sqlalchemy(self, query_class)

        if app is not None:
            self.init_app(app)

    @property
    def metadata(self):

        return self.Model.metadata

    def create_scoped_session(self, options=None):

        if options is None:
            options = {}

        scopefunc = options.pop("scopefunc", _app_ctx_stack.__ident_func__)
        options.setdefault("query_cls", self.Query)
        return orm.scoped_session(self.create_session(options), scopefunc=scopefunc)

    def create_session(self, options):

        return orm.sessionmaker(class_=SignallingSession, db=self, **options)

    def make_declarative_base(self, model, metadata=None):
~~        if not isinstance(model, DeclarativeMeta):
            model = declarative_base(
                cls=model, name="Model", metadata=metadata, metaclass=DefaultMeta
            )

        if metadata is not None and model.metadata is not metadata:
            model.metadata = metadata

        if not getattr(model, "query_class", None):
            model.query_class = self.Query

        model.query = _QueryProperty(self)
        return model

    def init_app(self, app):

        if not (
            app.config.get("SQLALCHEMY_DATABASE_URI")
            or app.config.get("SQLALCHEMY_BINDS")
        ):
            raise RuntimeError(
                "Either SQLALCHEMY_DATABASE_URI or SQLALCHEMY_BINDS needs to be set."
            )

        app.config.setdefault("SQLALCHEMY_DATABASE_URI", None)


## ... source file continues with no further DeclarativeMeta examples...

```


## Example 2 from marshmallow-sqlalchemy
[marshmallow-sqlalchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy)
([project documentation](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/))
is a code library that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) with the
[Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
data serialization tool.

The marshmallow-sqlalchemy project is provided as open source under the
[MIT license](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/LICENSE).

[**marshmallow-sqlalchemy / src/marshmallow_sqlalchemy / schema / sqlalchemy_schema.py**](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/src/marshmallow_sqlalchemy/schema/sqlalchemy_schema.py)

```python
# sqlalchemy_schema.py
from marshmallow.fields import Field
from marshmallow.schema import Schema, SchemaMeta, SchemaOpts
import sqlalchemy as sa
~~from sqlalchemy.ext.declarative import DeclarativeMeta

from ..convert import ModelConverter
from ..exceptions import IncorrectSchemaTypeError
from .load_instance_mixin import LoadInstanceMixin


class SQLAlchemyAutoField(Field):
    def __init__(self, *, column_name=None, model=None, table=None, field_kwargs):
        super().__init__()

        if model and table:
            raise ValueError("Cannot pass both `model` and `table` options.")

        self.column_name = column_name
        self.model = model
        self.table = table
        self.field_kwargs = field_kwargs

    def create_field(self, schema_opts, column_name, converter):
        model = self.model or schema_opts.model
        if model:
            return converter.field_for(model, column_name, **self.field_kwargs)
        else:
            table = self.table if self.table is not None else schema_opts.table


## ... source file continues with no further DeclarativeMeta examples...

```

