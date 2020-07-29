title: sqlalchemy.dialects.postgresql ExcludeConstraint Example Code
category: page
slug: sqlalchemy-dialects-postgresql-excludeconstraint-examples
sortorder: 500031011
toc: False
sidebartitle: sqlalchemy.dialects.postgresql ExcludeConstraint
meta: Example code for understanding how to use the ExcludeConstraint class from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


`ExcludeConstraint` is a class within the `sqlalchemy.dialects.postgresql` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-postgresql-array-examples.html">ARRAY</a>,
<a href="/sqlalchemy-dialects-postgresql-bigint-examples.html">BIGINT</a>,
<a href="/sqlalchemy-dialects-postgresql-bit-examples.html">BIT</a>,
<a href="/sqlalchemy-dialects-postgresql-double-precision-examples.html">DOUBLE_PRECISION</a>,
<a href="/sqlalchemy-dialects-postgresql-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">JSON</a>,
<a href="/sqlalchemy-dialects-postgresql-tsvector-examples.html">TSVECTOR</a>,
<a href="/sqlalchemy-dialects-postgresql-array-examples.html">array</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">json</a>,
and <a href="/sqlalchemy-dialects-postgresql-pypostgresql-examples.html">pypostgresql</a>
are several other callables with code examples from the same `sqlalchemy.dialects.postgresql` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / ddl / postgresql.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/ddl/postgresql.py)

```python
# postgresql.py
import logging
import re

from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import text
from sqlalchemy import types as sqltypes
from sqlalchemy.dialects.postgresql import BIGINT
~~from sqlalchemy.dialects.postgresql import ExcludeConstraint
from sqlalchemy.dialects.postgresql import INTEGER
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql.expression import UnaryExpression
from sqlalchemy.types import NULLTYPE

from .base import alter_column
from .base import alter_table
from .base import AlterColumn
from .base import ColumnComment
from .base import compiles
from .base import format_column_name
from .base import format_table_name
from .base import format_type
from .base import RenameTable
from .impl import DefaultImpl
from .. import util
from ..autogenerate import render
from ..operations import ops
from ..operations import schemaobj
from ..operations.base import BatchOperations
from ..operations.base import Operations
from ..util import compat
from ..util import sqla_compat



## ... source file abbreviated to get to ExcludeConstraint examples ...


        self.schema = schema
        self._orig_constraint = _orig_constraint
        self.kw = kw

    @classmethod
    def from_constraint(cls, constraint):
        constraint_table = sqla_compat._table_for_constraint(constraint)

        return cls(
            constraint.name,
            constraint_table.name,
            [(expr, op) for expr, name, op in constraint._render_exprs],
            where=constraint.where,
            schema=constraint_table.schema,
            _orig_constraint=constraint,
            deferrable=constraint.deferrable,
            initially=constraint.initially,
            using=constraint.using,
        )

    def to_constraint(self, migration_context=None):
        if self._orig_constraint is not None:
            return self._orig_constraint
        schema_obj = schemaobj.SchemaObjects(migration_context)
        t = schema_obj.table(self.table_name, schema=self.schema)
~~        excl = ExcludeConstraint(
            *self.elements,
            name=self.constraint_name,
            where=self.where,
            **self.kw
        )
        for expr, name, oper in excl._render_exprs:
            t.append_column(Column(name, NULLTYPE))
        t.append_constraint(excl)
        return excl

    @classmethod
    def create_exclude_constraint(
        cls, operations, constraint_name, table_name, *elements, **kw
    ):
        op = cls(constraint_name, table_name, elements, **kw)
        return operations.invoke(op)

    @classmethod
    def batch_create_exclude_constraint(
        cls, operations, constraint_name, *elements, **kw
    ):
        kw["schema"] = operations.impl.schema
        op = cls(constraint_name, operations.impl.table_name, elements, **kw)
        return operations.invoke(op)


@render.renderers.dispatch_for(CreateExcludeConstraintOp)
def _add_exclude_constraint(autogen_context, op):
    return _exclude_constraint(op.to_constraint(), autogen_context, alter=True)


~~@render._constraint_renderers.dispatch_for(ExcludeConstraint)
def _render_inline_exclude_constraint(constraint, autogen_context):
    rendered = render._user_defined_render(
        "exclude", constraint, autogen_context
    )
    if rendered is not False:
        return rendered

    return _exclude_constraint(constraint, autogen_context, False)


def _postgresql_autogenerate_prefix(autogen_context):

    imports = autogen_context.imports
    if imports is not None:
        imports.add("from sqlalchemy.dialects import postgresql")
    return "postgresql."


def _exclude_constraint(constraint, autogen_context, alter):
    opts = []

    has_batch = autogen_context._has_batch

    if constraint.deferrable:


## ... source file continues with no further ExcludeConstraint examples...

```

