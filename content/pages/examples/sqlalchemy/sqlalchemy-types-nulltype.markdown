title: sqlalchemy.types NULLTYPE code examples
category: page
slug: sqlalchemy-types-nulltype-examples
sortorder: 500031001
toc: False
sidebartitle: sqlalchemy.types NULLTYPE
meta: Python example code for the NULLTYPE class from the sqlalchemy.types module of the SQLAlchemy project.


NULLTYPE is a class within the sqlalchemy.types module of the SQLAlchemy project.


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
from sqlalchemy.sql.expression import UnaryExpression
~~from sqlalchemy.types import NULLTYPE

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




## ... source file abbreviated to get to NULLTYPE examples ...


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
        excl = ExcludeConstraint(
            *self.elements,
            name=self.constraint_name,
            where=self.where,
            **self.kw
        )
        for expr, name, oper in excl._render_exprs:
~~            t.append_column(Column(name, NULLTYPE))
        t.append_constraint(excl)
        return excl

    @classmethod
    def create_exclude_constraint(
        cls, operations, constraint_name, table_name, *elements, **kw
    ):
        """Issue an alter to create an EXCLUDE constraint using the
        current migration context.

        .. note::  This method is Postgresql specific, and additionally
           requires at least SQLAlchemy 1.0.

        e.g.::

            from alembic import op

            op.create_exclude_constraint(
                "user_excl",
                "user",

                ("period", '&&'),
                ("group", '='),
                where=("group != 'some group'")


## ... source file continues with no further NULLTYPE examples...


```

