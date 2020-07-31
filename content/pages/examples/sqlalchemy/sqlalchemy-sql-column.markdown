title: sqlalchemy.sql column Example Code
category: page
slug: sqlalchemy-sql-column-examples
sortorder: 500031109
toc: False
sidebartitle: sqlalchemy.sql column
meta: Python example code that shows how to use the column callable from the sqlalchemy.sql module of the SQLAlchemy project.


`column` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
<a href="/sqlalchemy-sql-extract-examples.html">extract</a>,
<a href="/sqlalchemy-sql-functions-examples.html">functions</a>,
<a href="/sqlalchemy-sql-operators-examples.html">operators</a>,
<a href="/sqlalchemy-sql-schema-examples.html">schema</a>,
<a href="/sqlalchemy-sql-select-examples.html">select</a>,
<a href="/sqlalchemy-sql-sqltypes-examples.html">sqltypes</a>,
and <a href="/sqlalchemy-sql-table-examples.html">table</a>
are several other callables with code examples from the same `sqlalchemy.sql` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / operations / ops.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/operations/ops.py)

```python
# ops.py
import re

from sqlalchemy.types import NULLTYPE

from . import schemaobj
from .base import BatchOperations
from .base import Operations
from .. import util
from ..util import sqla_compat


class MigrateOperation(object):

    @util.memoized_property
    def info(self):
        return {}

    _mutations = frozenset()


class AddConstraintOp(MigrateOperation):

    add_constraint_ops = util.Dispatcher()

    @property
    def constraint_type(self):
        raise NotImplementedError()

    @classmethod
    def register_add_constraint(cls, type_):
        def go(klass):
            cls.add_constraint_ops.dispatch_for(type_)(klass.from_constraint)
            return klass

        return go


## ... source file abbreviated to get to column examples ...


    @classmethod
    def bulk_insert(cls, operations, table, rows, multiinsert=True):

        op = cls(table, rows, multiinsert=multiinsert)
        operations.invoke(op)


@Operations.register_operation("execute")
class ExecuteSQLOp(MigrateOperation):

    def __init__(self, sqltext, execution_options=None):
        self.sqltext = sqltext
        self.execution_options = execution_options

    @classmethod
    def execute(cls, operations, sqltext, execution_options=None):
        r"""Execute the given SQL using the current migration context.

        The given SQL can be a plain string, e.g.::

            op.execute("INSERT INTO table (foo) VALUES ('some value')")

        Or it can be any kind of Core SQL Expression construct, such as
        below where we use an update construct::

~~            from sqlalchemy.sql import table, column
            from sqlalchemy import String
            from alembic import op

            account = table('account',
~~                column('name', String)
            )
            op.execute(
                account.update().\\
                    where(account.c.name==op.inline_literal('account 1')).\\
                    values({'name':op.inline_literal('account 2')})
                    )

        Above, we made use of the SQLAlchemy
        :func:`sqlalchemy.sql.expression.table` and
        :func:`sqlalchemy.sql.expression.column` constructs to make a brief,
        ad-hoc table construct just for our UPDATE statement.  A full
        :class:`-sqlalchemy.schema.Table` construct of course works perfectly
        fine as well, though note it's a recommended practice to at least
        ensure the definition of a table is self-contained within the migration
        script, rather than imported from a module that may break compatibility
        with older migrations.

        In a SQL script context, the statement is emitted directly to the
        output stream.   There is *no* return result, however, as this
        function is oriented towards generating a change script
        that can run in "offline" mode.     Additionally, parameterized
        statements are discouraged here, as they *will not work* in offline
        mode.  Above, we use :meth:`.inline_literal` where parameters are
        to be used.
        When producing MySQL-compatible migration files,
        it is recommended that the ``existing_type``,
        ``existing_server_default``, and ``existing_nullable``
        parameters be present, if not being altered.

        Type changes which are against the SQLAlchemy
        "schema" types :class:`-sqlalchemy.types.Boolean`
        and  :class:`-sqlalchemy.types.Enum` may also
        add or drop constraints which accompany those
        types on backends that don't support them natively.
        The ``existing_type`` argument is
        used in this case to identify and remove a previous
        constraint that was bound to the type object.

        :param table_name: string name of the target table.
        :param column_name: string name of the target column,
         as it exists before the operation begins.
        :param nullable: Optional; specify ``True`` or ``False``
         to alter the column's nullability.
        :param server_default: Optional; specify a string
         SQL expression, :func:`-sqlalchemy.sql.expression.text`,
         or :class:`-sqlalchemy.schema.DefaultClause` to indicate
         an alteration to the column's default value.
         Set to ``None`` to have the default removed.
        :param comment: optional string text of a new comment to add to the
~~         column.

         .. versionadded:: 1.0.6

        :param new_column_name: Optional; specify a string name here to
         indicate the new name within a column rename operation.
        :param type\_: Optional; a :class:`-sqlalchemy.types.TypeEngine`
         type object to specify a change to the column's type.
         For SQLAlchemy types that also indicate a constraint (i.e.
         :class:`-sqlalchemy.types.Boolean`, :class:`-sqlalchemy.types.Enum`),
         the constraint is also generated.
        :param autoincrement: set the ``AUTO_INCREMENT`` flag of the column;
         currently understood by the MySQL dialect.
        :param existing_type: Optional; a
         :class:`-sqlalchemy.types.TypeEngine`
         type object to specify the previous type.   This
         is required for all MySQL column alter operations that
         don't otherwise specify a new type, as well as for
         when nullability is being changed on a SQL Server
~~         column.  It is also used if the type is a so-called
         SQLlchemy "schema" type which may define a constraint (i.e.
         :class:`-sqlalchemy.types.Boolean`,
         :class:`-sqlalchemy.types.Enum`),
         so that the constraint can be dropped.
        :param existing_server_default: Optional; The existing
~~         default value of the column.   Required on MySQL if
         an existing default is not being changed; else MySQL
         removes the default.
        :param existing_nullable: Optional; the existing nullability
~~         of the column.  Required on MySQL if the existing nullability
         is not being changed; else MySQL sets this to NULL.
        :param existing_autoincrement: Optional; the existing autoincrement
~~         of the column.  Used for MySQL's system of altering a column
         that specifies ``AUTO_INCREMENT``.
        :param existing_comment: string text of the existing comment on the
         column to be maintained.  Required on MySQL if the existing comment
         on the column is not being changed.

         .. versionadded:: 1.0.6

        :param schema: Optional schema name to operate within.  To control
         quoting of the schema outside of the default behavior, use
         the SQLAlchemy construct
         :class:`-sqlalchemy.sql.elements.quoted_name`.

         .. versionadded:: 0.7.0 'schema' can now accept a
            :class:`-sqlalchemy.sql.elements.quoted_name` construct.

        :param postgresql_using: String argument which will indicate a
         SQL expression to render within the Postgresql-specific USING clause
         within ALTER COLUMN.    This string is taken directly as raw SQL which
         must explicitly include any necessary quoting or escaping of tokens
         within the expression.

         .. versionadded:: 0.8.8

        batch migration context.


## ... source file continues with no further column examples...

```

