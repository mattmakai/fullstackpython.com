title: flask.signals Namespace Python code examples
category: page
slug: flask-signals-namespace-examples
sortorder: 500021000
toc: False
sidebartitle: flask.signals Namespace
meta: Python example code for the Namespace class from the flask.signals module of the Flask project.


Namespace is a class within the flask.signals module of the Flask project.


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

[**flask-sqlalchemy / flask_sqlalchemy / __init__.py**](https://github.com/pallets/flask-sqlalchemy/blob/master/flask_sqlalchemy/./__init__.py)

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import functools
import os
import sys
import time
import warnings
from math import ceil
from operator import itemgetter
from threading import Lock

import sqlalchemy
from flask import _app_ctx_stack, abort, current_app, request
~~from flask.signals import Namespace
from sqlalchemy import event, inspect, orm
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.orm.session import Session as SessionBase

from flask_sqlalchemy.model import Model
from ._compat import itervalues, string_types, xrange
from .model import DefaultMeta
from . import utils

__version__ = "3.0.0.dev"

# the best timer function for the platform
if sys.platform == 'win32':
    if sys.version_info >= (3, 3):
        _timer = time.perf_counter
    else:
        _timer = time.clock
else:
    _timer = time.time

~~_signals = Namespace()
models_committed = _signals.signal('models-committed')


## ... source file abbreviated to get to Namespace examples ...


before_models_committed = _signals.signal('before-models-committed')


def _make_table(db):
    def _make_table(*args, **kwargs):
        if len(args) > 1 and isinstance(args[1], db.Column):
            args = (args[0], db.metadata) + args[1:]
        info = kwargs.pop('info', None) or {}
        info.setdefault('bind_key', None)
        kwargs['info'] = info
        return sqlalchemy.Table(*args, **kwargs)
    return _make_table


def _set_default_query_class(d, cls):
    if 'query_class' not in d:
        d['query_class'] = cls


def _wrap_with_default_query_class(fn, cls):
    @functools.wraps(fn)
    def newfn(*args, **kwargs):
        _set_default_query_class(kwargs, cls)


## ... source file continues with no further Namespace examples...


```

