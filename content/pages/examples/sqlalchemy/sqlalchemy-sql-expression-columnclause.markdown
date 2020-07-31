title: sqlalchemy.sql.expression ColumnClause Example Code
category: page
slug: sqlalchemy-sql-expression-columnclause-examples
sortorder: 500031122
toc: False
sidebartitle: sqlalchemy.sql.expression ColumnClause
meta: Example code for understanding how to use the ColumnClause class from the sqlalchemy.sql.expression module of the SQLAlchemy project.


`ColumnClause` is a class within the `sqlalchemy.sql.expression` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-expression-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-expression-columnelement-examples.html">ColumnElement</a>,
<a href="/sqlalchemy-sql-expression-executable-examples.html">Executable</a>,
<a href="/sqlalchemy-sql-expression-functionelement-examples.html">FunctionElement</a>,
and <a href="/sqlalchemy-sql-expression-unaryexpression-examples.html">UnaryExpression</a>
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
~~from sqlalchemy.sql.expression import ColumnClause
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


log = logging.getLogger(__name__)


## ... source file abbreviated to get to ColumnClause examples ...


        return "%(prefix)screate_exclude_constraint(%(args)s)" % {
            "prefix": render._alembic_autogenerate_prefix(autogen_context),
            "args": ", ".join(args),
        }
    else:
        args = [
            "(%s, %r)"
            % (_render_potential_column(sqltext, autogen_context), opstring)
            for sqltext, name, opstring in constraint._render_exprs
        ]
        if constraint.where is not None:
            args.append(
                "where=%s"
                % render._render_potential_expr(
                    constraint.where, autogen_context
                )
            )
        args.extend(["%s=%r" % (k, v) for k, v in opts])
        return "%(prefix)sExcludeConstraint(%(args)s)" % {
            "prefix": _postgresql_autogenerate_prefix(autogen_context),
            "args": ", ".join(args),
        }


def _render_potential_column(value, autogen_context):
~~    if isinstance(value, ColumnClause):
        template = "%(prefix)scolumn(%(name)r)"

        return template % {
            "prefix": render._sqlalchemy_autogenerate_prefix(autogen_context),
            "name": value.name,
        }

    else:
        return render._render_potential_expr(
            value, autogen_context, wrap_in_text=False
        )



## ... source file continues with no further ColumnClause examples...

```

