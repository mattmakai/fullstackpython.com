title: flask.signals Namespace Example Code
category: page
slug: flask-signals-namespace-examples
sortorder: 500021029
toc: False
sidebartitle: flask.signals Namespace
meta: Example code for understanding how to use the Namespace class from the flask.signals module of the Flask project.


[Namespace](https://github.com/pallets/flask/blob/master/src/flask/signals.py)
is a class used within the `flask.signals` module, but it is
actually imported from the
[Blinker project](https://github.com/jek/blinker). Blinker
is a fast dispatching system for event subscriptions, also known as
"signals". [Flask](/flask.html) uses this library instead of
implementing its own event subscription signaling model.
[Namespace is defined within Blinker](https://github.com/jek/blinker/blob/master/blinker/base.py)
as a mapping of signal names to signals, and it serves the
same purpose in the Flask project.

<a href="/flask-signals-got-request-exception-examples.html">got_request_exception</a>
is another callable from the `flask.signals` package with code examples.

## Example 1 from flask-login
[Flask-Login](https://github.com/maxcountryman/flask-login)
([project documentation](https://flask-login.readthedocs.io/en/latest/)
and [PyPI package](https://pypi.org/project/Flask-Login/))
is a [Flask](/flask.html) extension that provides user session
management, which handles common tasks such as logging in
and out of a [web application](/web-development.html) and
managing associated user session data. Flask-Login is
open sourced under the
[MIT license](https://github.com/maxcountryman/flask-login/blob/master/LICENSE).

[**flask-login / flask_login / signals.py**](https://github.com/maxcountryman/flask-login/blob/master/flask_login/./signals.py)

```python
# signals.py


~~from flask.signals import Namespace


~~_signals = Namespace()


user_logged_in = _signals.signal('logged-in')

user_logged_out = _signals.signal('logged-out')

user_loaded_from_cookie = _signals.signal('loaded-from-cookie')

user_loaded_from_header = _signals.signal('loaded-from-header')

user_loaded_from_request = _signals.signal('loaded-from-request')

user_login_confirmed = _signals.signal('login-confirmed')

user_unauthorized = _signals.signal('unauthorized')

user_needs_refresh = _signals.signal('needs-refresh')

user_accessed = _signals.signal('accessed')

session_protected = _signals.signal('session-protected')



## ... source file continues with no further Namespace examples...

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
~~from flask.signals import Namespace
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

~~_signals = Namespace()
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


def _set_default_query_class(d, cls):
    if "query_class" not in d:
        d["query_class"] = cls


def _wrap_with_default_query_class(fn, cls):
    @functools.wraps(fn)
    def newfn(*args, **kwargs):


## ... source file continues with no further Namespace examples...

```


## Example 3 from Flask-User
[Flask-User](https://github.com/lingthio/Flask-User)
([PyPI information](https://pypi.org/project/Flask-User/)
and
[project documentation](https://flask-user.readthedocs.io/en/latest/))
is a [Flask](/flask.html) extension that makes it easier to add
custom user account management and authentication to the projects
you are building. The extension supports persistent data storage
through both [relational databases](/databases.html) and
[MongoDB](/mongodb.html). The project is provided as open source under
the [MIT license](https://github.com/lingthio/Flask-User/blob/master/LICENSE.txt).

[**Flask-User / flask_user / signals.py**](https://github.com/lingthio/Flask-User/blob/master/flask_user/./signals.py)

```python
# signals.py



~~from flask.signals import Namespace

~~_signals = Namespace()                              # Place Flask-User signals in our own namespace


user_changed_password = _signals.signal('user.user_changed_password')

user_changed_username = _signals.signal('user.user_changed_username')

user_confirmed_email = _signals.signal('user.user_confirmed_email')

user_forgot_password = _signals.signal('user.forgot_password')

user_logged_in = _signals.signal('user.user_logged_in')

user_logged_out = _signals.signal('user.user_logged_out')

user_registered = _signals.signal('user.user_registered')

user_reset_password = _signals.signal('user.user_reset_password')

user_sent_invitation = _signals.signal('user.user_sent_invitation')




## ... source file continues with no further Namespace examples...

```

