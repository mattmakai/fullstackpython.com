title: sqlalchemy.sql.naming conv code examples
category: page
slug: sqlalchemy-sql-naming-conv-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.sql.naming conv
meta: Python example code for the conv function from the sqlalchemy.sql.naming module of the SQLAlchemy project.


conv is a function within the sqlalchemy.sql.naming module of the SQLAlchemy project.


## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / operations / base.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/operations/base.py)

```python
# base.py
from contextlib import contextmanager
import textwrap

from . import batch
from . import schemaobj
from .. import util
from ..util import sqla_compat
from ..util.compat import exec_
from ..util.compat import inspect_formatargspec
from ..util.compat import inspect_getargspec

__all__ = ("Operations", "BatchOperations")

try:
~~    from sqlalchemy.sql.naming import conv
except:
    conv = None


class Operations(util.ModuleClsProxy):

    """Define high level migration operations.

    Each operation corresponds to some schema migration operation,
    executed against a particular :class:`.MigrationContext`
    which in turn represents connectivity to a database,
    or a file output stream.

    While :class:`.Operations` is normally configured as
    part of the :meth:`.EnvironmentContext.run_migrations`
    method called from an ``env.py`` script, a standalone
    :class:`.Operations` instance can be
    made for use cases external to regular Alembic
    migrations by passing in a :class:`.MigrationContext`::

        from alembic.migration import MigrationContext
        from alembic.operations import Operations

        conn = myengine.connect()


## ... source file abbreviated to get to conv examples ...


        contains the naming convention
        ``{"ck": "ck_bool_%(table_name)s_%(constraint_name)s"}``, then the
        output of the following:

            op.add_column('t', 'x', Boolean(name='x'))

        will be::

            CONSTRAINT ck_bool_t_x CHECK (x in (1, 0)))

        The function is rendered in the output of autogenerate when
        a particular constraint name is already converted, for SQLAlchemy
        version **0.9.4 and greater only**.   Even though ``naming_convention``
        was introduced in 0.9.2, the string disambiguation service is new
        as of 0.9.4.

        .. versionadded:: 0.6.4

        """
        if conv:
~~            return conv(name)
        else:
            raise NotImplementedError(
                "op.f() feature requires SQLAlchemy 0.9.4 or greater."
            )

    def inline_literal(self, value, type_=None):
        r"""Produce an 'inline literal' expression, suitable for
        using in an INSERT, UPDATE, or DELETE statement.

        When using Alembic in "offline" mode, CRUD operations
        aren't compatible with SQLAlchemy's default behavior surrounding
        literal values,
        which is that they are converted into bound values and passed
        separately into the ``execute()`` method of the DBAPI cursor.
        An offline SQL
        script needs to have these rendered inline.  While it should
        always be noted that inline literal values are an **enormous**
        security hole in an application that handles untrusted input,
        a schema migration is not run in this context, so
        literals are safe to render inline, with the caveat that
        advanced types like dates may not be supported directly
        by SQLAlchemy.

        See :meth:`.execute` for an example usage of


## ... source file continues with no further conv examples...


```

