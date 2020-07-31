title: sqlalchemy.sql.expression UnaryExpression Example Code
category: page
slug: sqlalchemy-sql-expression-unaryexpression-examples
sortorder: 500031126
toc: False
sidebartitle: sqlalchemy.sql.expression UnaryExpression
meta: Example code for understanding how to use the UnaryExpression class from the sqlalchemy.sql.expression module of the SQLAlchemy project.


`UnaryExpression` is a class within the `sqlalchemy.sql.expression` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-expression-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-expression-columnclause-examples.html">ColumnClause</a>,
<a href="/sqlalchemy-sql-expression-columnelement-examples.html">ColumnElement</a>,
<a href="/sqlalchemy-sql-expression-executable-examples.html">Executable</a>,
and <a href="/sqlalchemy-sql-expression-functionelement-examples.html">FunctionElement</a>
are several other callables with code examples from the same `sqlalchemy.sql.expression` package.

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
from sqlalchemy.dialects.postgresql import ExcludeConstraint
from sqlalchemy.dialects.postgresql import INTEGER
from sqlalchemy.sql.expression import ColumnClause
~~from sqlalchemy.sql.expression import UnaryExpression
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


log = logging.getLogger(__name__)



## ... source file abbreviated to get to UnaryExpression examples ...



    def correct_for_autogen_constraints(
        self,
        conn_unique_constraints,
        conn_indexes,
        metadata_unique_constraints,
        metadata_indexes,
    ):

        conn_indexes_by_name = dict((c.name, c) for c in conn_indexes)

        doubled_constraints = set(
            index
            for index in conn_indexes
            if index.info.get("duplicates_constraint")
        )

        for ix in doubled_constraints:
            conn_indexes.remove(ix)

        for idx in list(metadata_indexes):
            if idx.name in conn_indexes_by_name:
                continue
            exprs = idx.expressions
            for expr in exprs:
~~                while isinstance(expr, UnaryExpression):
                    expr = expr.element
                if not isinstance(expr, Column):
                    util.warn(
                        "autogenerate skipping functional index %s; "
                        "not supported by SQLAlchemy reflection" % idx.name
                    )
                    metadata_indexes.discard(idx)

    def render_type(self, type_, autogen_context):
        mod = type(type_).__module__
        if not mod.startswith("sqlalchemy.dialects.postgresql"):
            return False

        if hasattr(self, "_render_%s_type" % type_.__visit_name__):
            meth = getattr(self, "_render_%s_type" % type_.__visit_name__)
            return meth(type_, autogen_context)

        return False

    def _render_HSTORE_type(self, type_, autogen_context):
        return render._render_type_w_subtype(
            type_, autogen_context, "text_type", r"(.+?\(.*text_type=)"
        )



## ... source file continues with no further UnaryExpression examples...

```

