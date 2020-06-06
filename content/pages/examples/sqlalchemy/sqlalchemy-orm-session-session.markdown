title: sqlalchemy.orm.session Session code examples
category: page
slug: sqlalchemy-orm-session-session-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.orm.session Session
meta: Python example code for the Session class from the sqlalchemy.orm.session module of the SQLAlchemy project.


Session is a class within the sqlalchemy.orm.session module of the SQLAlchemy project.


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
~~from sqlalchemy.orm.session import Session as SessionBase

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


def _set_default_query_class(d, cls):


## ... source file abbreviated to get to Session examples ...


        return self.end_time - self.start_time

    def __repr__(self):
        return (
            f"<query statement={self.statement!r} parameters={self.parameters!r}"
            f" duration={self.duration:.03f}>"
        )


def _calling_context(app_path):
    frm = sys._getframe(1)
    while frm.f_back is not None:
        name = frm.f_globals.get("__name__")
        if name and (name == app_path or name.startswith(f"{app_path}.")):
            funcname = frm.f_code.co_name
            return f"{frm.f_code.co_filename}:{frm.f_lineno} ({funcname})"
        frm = frm.f_back
    return "<unknown>"


~~class SignallingSession(SessionBase):
    """The signalling session is the default session that Flask-SQLAlchemy
    uses.  It extends the default session system with bind selection and
    modification tracking.

    If you want to use a different session you can override the
    :meth:`SQLAlchemy.create_session` function.

    .. versionadded:: 2.0

    .. versionadded:: 2.1
        The `binds` option was added, which allows a session to be joined
        to an external transaction.
    """

    def __init__(self, db, autocommit=False, autoflush=True, **options):
        #: The application that this session belongs to.
        self.app = app = db.get_app()
        track_modifications = app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
        bind = options.pop("bind", None) or db.engine
        binds = options.pop("binds", db.get_binds(app))

        if track_modifications:
~~            _SessionSignalEvents.register(self)

~~        SessionBase.__init__(
            self,
            autocommit=autocommit,
            autoflush=autoflush,
            bind=bind,
            binds=binds,
            **options,
        )

    def get_bind(self, mapper=None, clause=None):
        """Return the engine or connection for a given model or
        table, using the ``__bind_key__`` if it is set.
        """
        # mapper is None if someone tries to just get a connection
        if mapper is not None:
            try:
                # SA >= 1.3
                persist_selectable = mapper.persist_selectable
            except AttributeError:
                # SA < 1.3
                persist_selectable = mapper.mapped_table

            info = getattr(persist_selectable, "info", {})
            bind_key = info.get("bind_key")
            if bind_key is not None:
                state = get_state(self.app)
                return state.db.get_engine(self.app, bind=bind_key)
~~        return SessionBase.get_bind(self, mapper, clause)


~~class _SessionSignalEvents:
    @classmethod
    def register(cls, session):
        if not hasattr(session, "_model_changes"):
            session._model_changes = {}

        event.listen(session, "before_flush", cls.record_ops)
        event.listen(session, "before_commit", cls.record_ops)
        event.listen(session, "before_commit", cls.before_commit)
        event.listen(session, "after_commit", cls.after_commit)
        event.listen(session, "after_rollback", cls.after_rollback)

    @classmethod
    def unregister(cls, session):
        if hasattr(session, "_model_changes"):
            del session._model_changes

        event.remove(session, "before_flush", cls.record_ops)
        event.remove(session, "before_commit", cls.record_ops)
        event.remove(session, "before_commit", cls.before_commit)
        event.remove(session, "after_commit", cls.after_commit)
        event.remove(session, "after_rollback", cls.after_rollback)

    @staticmethod
    def record_ops(session, flush_context=None, instances=None):


## ... source file abbreviated to get to Session examples ...


        class User(db.Model):
            username = db.Column(db.String(80), unique=True)
            pw_hash = db.Column(db.String(80))

    You can still use :mod:`sqlalchemy` and :mod:`sqlalchemy.orm` directly, but
    note that Flask-SQLAlchemy customizations are available only through an
    instance of this :class:`SQLAlchemy` class.  Query classes default to
    :class:`BaseQuery` for `db.Query`, `db.Model.query_class`, and the default
    query_class for `db.relationship` and `db.backref`.  If you use these
    interfaces through :mod:`sqlalchemy` and :mod:`sqlalchemy.orm` directly,
    the default query class will be that of :mod:`sqlalchemy`.

    .. admonition:: Check types carefully

       Don't perform type or `isinstance` checks against `db.Table`, which
       emulates `Table` behavior but is not a class. `db.Table` exposes the
       `Table` interface, but is a function which allows omission of metadata.

    The ``session_options`` parameter, if provided, is a dict of parameters
    to be passed to the session constructor. See
~~    :class:`-sqlalchemy.orm.session.Session` for the standard options.

    The ``engine_options`` parameter, if provided, is a dict of parameters
    to be passed to create engine.  See :func:`-sqlalchemy.create_engine`
    for the standard options.  The values given here will be merged with and
    override anything set in the ``'SQLALCHEMY_ENGINE_OPTIONS'`` config
    variable or othewise set by this library.

    .. versionchanged:: 3.0
        Removed the ``use_native_unicode`` parameter and config.

    .. versionchanged:: 3.0
        ``COMMIT_ON_TEARDOWN`` is deprecated and will be removed in
        version 3.1. Call ``db.session.commit()`` directly instead.

    .. versionchanged:: 2.4
        Added the ``engine_options`` parameter.

    .. versionchanged:: 2.1
        Added the ``metadata`` parameter. This allows for setting custom
        naming conventions among other, non-trivial things.

    .. versionchanged:: 2.1
        Added the ``query_class`` parameter, to allow customisation
        of the query class, in place of the default of


## ... source file abbreviated to get to Session examples ...


        created and removed with the request/response cycle, and should be fine
        in most cases.

        :param options: dict of keyword arguments passed to session class  in
            ``create_session``
        """

        if options is None:
            options = {}

        scopefunc = options.pop("scopefunc", _app_ctx_stack.__ident_func__)
        options.setdefault("query_cls", self.Query)
        return orm.scoped_session(self.create_session(options), scopefunc=scopefunc)

    def create_session(self, options):
        """Create the session factory used by :meth:`create_scoped_session`.

        The factory **must** return an object that SQLAlchemy recognizes as a session,
        or registering session events may raise an exception.

~~        Valid factories include a :class:`-sqlalchemy.orm.session.Session`
        class or a :class:`-sqlalchemy.orm.session.sessionmaker`.

        The default implementation creates a ``sessionmaker`` for
~~        :class:`SignallingSession`.

        :param options: dict of keyword arguments passed to session class
        """

~~        return orm.sessionmaker(class_=SignallingSession, db=self, **options)

    def make_declarative_base(self, model, metadata=None):
        """Creates the declarative base that all models will inherit from.

        :param model: base model class (or a tuple of base classes) to pass
            to :func:`-sqlalchemy.ext.declarative.declarative_base`. Or a class
            returned from ``declarative_base``, in which case a new base class
            is not created.
        :param metadata: :class:`-sqlalchemy.MetaData` instance to use, or
            none to use SQLAlchemy's default.

        .. versionchanged 2.3.0::
            ``model`` can be an existing declarative base in order to support
            complex customization such as changing the metaclass.
        """
        if not isinstance(model, DeclarativeMeta):
            model = declarative_base(
                cls=model, name="Model", metadata=metadata, metaclass=DefaultMeta
            )

        # if user passed in a declarative base and a metaclass for some reason,
        # make sure the base uses the metaclass
        if metadata is not None and model.metadata is not metadata:
            model.metadata = metadata


## ... source file continues with no further Session examples...


```

