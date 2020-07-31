title: sqlalchemy.sql.naming conv Example Code
category: page
slug: sqlalchemy-sql-naming-conv-examples
sortorder: 500031129
toc: False
sidebartitle: sqlalchemy.sql.naming conv
meta: Python example code that shows how to use the conv callable from the sqlalchemy.sql.naming module of the SQLAlchemy project.


`conv` is a callable within the `sqlalchemy.sql.naming` module of the SQLAlchemy project.



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


    _to_impl = util.Dispatcher()

    def __init__(self, migration_context, impl=None):
        self.migration_context = migration_context
        if impl is None:
            self.impl = migration_context.impl
        else:
            self.impl = impl

        self.schema_obj = schemaobj.SchemaObjects(migration_context)

    @classmethod
    def register_operation(cls, name, sourcename=None):

        def register(op_cls):
            if sourcename is None:
                fn = getattr(op_cls, name)


## ... source file abbreviated to get to conv examples ...


            recreate,
            copy_from,
            table_args,
            table_kwargs,
            reflect_args,
            reflect_kwargs,
            naming_convention,
            partial_reordering,
        )
        batch_op = BatchOperations(self.migration_context, impl=impl)
        yield batch_op
        impl.flush()

    def get_context(self):

        return self.migration_context

    def invoke(self, operation):
        fn = self._to_impl.dispatch(
            operation, self.migration_context.impl.__dialect__
        )
        return fn(self, operation)

    def f(self, name):
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

