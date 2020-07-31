title: sqlalchemy.sql table Example Code
category: page
slug: sqlalchemy-sql-table-examples
sortorder: 500031117
toc: False
sidebartitle: sqlalchemy.sql table
meta: Python example code that shows how to use the table callable from the sqlalchemy.sql module of the SQLAlchemy project.


`table` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
<a href="/sqlalchemy-sql-extract-examples.html">extract</a>,
<a href="/sqlalchemy-sql-functions-examples.html">functions</a>,
<a href="/sqlalchemy-sql-operators-examples.html">operators</a>,
<a href="/sqlalchemy-sql-schema-examples.html">schema</a>,
<a href="/sqlalchemy-sql-select-examples.html">select</a>,
and <a href="/sqlalchemy-sql-sqltypes-examples.html">sqltypes</a>
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


## ... source file abbreviated to get to table examples ...


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

~~            account = table('account',
                column('name', String)
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
        unique=False,
        **kw
    ):
        r"""Issue a "create index" instruction using the current
        migration context.

        e.g.::

            from alembic import op
            op.create_index('ik_test', 't1', ['foo', 'bar'])

        Functional indexes can be produced by using the
        :func:`sqlalchemy.sql.expression.text` construct::

            from alembic import op
            from sqlalchemy import text
            op.create_index('ik_test', 't1', [text('lower(foo)')])

        .. versionadded:: 0.6.7 support for making use of the
           :func:`-sqlalchemy.sql.expression.text` construct in
           conjunction with
           :meth:`.Operations.create_index` in
           order to produce functional expressions within CREATE INDEX.

        :param index_name: name of the index.
~~        :param table_name: name of the owning table.
        :param columns: a list consisting of string column names and/or
         :func:`-sqlalchemy.sql.expression.text` constructs.
        :param schema: Optional schema name to operate within.  To control
         quoting of the schema outside of the default behavior, use
         the SQLAlchemy construct
         :class:`-sqlalchemy.sql.elements.quoted_name`.

         .. versionadded:: 0.7.0 'schema' can now accept a
            :class:`-sqlalchemy.sql.elements.quoted_name` construct.

        :param unique: If True, create a unique index.

        :param quote:
            Force quoting of this column's name on or off, corresponding
            to ``True`` or ``False``. When left at its default
            of ``None``, the column identifier will be quoted according to
            whether the name is case sensitive (identifiers with at least one
            upper case character are treated as case sensitive), or if it's a
            reserved word. This flag is only needed to force quoting of a
            reserved word which is not known by the SQLAlchemy dialect.

        :param \**kw: Additional keyword arguments not mentioned above are
            dialect specific, and passed in the form
            ``<dialectname>_<argname>``.


## ... source file abbreviated to get to table examples ...


        schema_obj = schemaobj.SchemaObjects(migration_context)

        return schema_obj.index(
            self.index_name,
            self.table_name,
            ["x"],
            schema=self.schema,
            **self.kw
        )

    @classmethod
    @util._with_legacy_names(
        [("name", "index_name"), ("tablename", "table_name")]
    )
    def drop_index(
        cls, operations, index_name, table_name=None, schema=None, **kw
    ):
        r"""Issue a "drop index" instruction using the current
        migration context.

        e.g.::

            drop_index("accounts")

        :param index_name: name of the index.
~~        :param table_name: name of the owning table.  Some
         backends such as Microsoft SQL Server require this.
        :param schema: Optional schema name to operate within.  To control
         quoting of the schema outside of the default behavior, use
         the SQLAlchemy construct
         :class:`-sqlalchemy.sql.elements.quoted_name`.

         .. versionadded:: 0.7.0 'schema' can now accept a
            :class:`-sqlalchemy.sql.elements.quoted_name` construct.

        :param \**kw: Additional keyword arguments not mentioned above are
            dialect specific, and passed in the form
            ``<dialectname>_<argname>``.
            See the documentation regarding an individual dialect at
            :ref:`dialect_toplevel` for detail on documented arguments.

            .. versionadded:: 0.9.5 Support for dialect-specific keyword
               arguments for DROP INDEX

        .. versionchanged:: 0.8.0 The following positional argument names
           have been changed:

           * name -> index_name

        current batch migration context.


## ... source file abbreviated to get to table examples ...



        .. versionchanged:: 0.8.0 The following positional argument names
           have been changed:

           * name -> index_name


    def __init__(
        self, table_name, columns, schema=None, _orig_table=None, **kw
    ):
        self.table_name = table_name
        self.columns = columns
        self.schema = schema
        self.kw = kw
        self._orig_table = _orig_table

    def reverse(self):
        return DropTableOp.from_table(self.to_table())

    def to_diff_tuple(self):
        return ("add_table", self.to_table())

    @classmethod
    def from_table(cls, table):
        return cls(
~~            table.name,
            list(table.c) + list(table.constraints),
~~            schema=table.schema,
            _orig_table=table,
            **table.kwargs
        )

    def to_table(self, migration_context=None):
        if self._orig_table is not None:
            return self._orig_table
        schema_obj = schemaobj.SchemaObjects(migration_context)

        return schema_obj.table(
            self.table_name, *self.columns, schema=self.schema, **self.kw
        )

    @classmethod
    @util._with_legacy_names([("name", "table_name")])
    def create_table(cls, operations, table_name, *columns, **kw):
        r"""Issue a "create table" instruction using the current migration
        context.

        This directive receives an argument list similar to that of the
        traditional :class:`sqlalchemy.schema.Table` construct, but without the
        metadata::


## ... source file abbreviated to get to table examples ...


        current migration context.

        Generally, only that aspect of the column which
        is being changed, i.e. name, type, nullability,
        default, needs to be specified.  Multiple changes
        can also be specified at once and the backend should
        "do the right thing", emitting each change either
        separately or together as the backend allows.

        MySQL has special requirements here, since MySQL
        cannot ALTER a column without a full specification.
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

~~        :param table_name: string name of the target table.
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
         column.

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


## ... source file abbreviated to get to table examples ...



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

        Parameters are the same as that of :meth:`.Operations.alter_column`,
        as well as the following option(s):

        :param insert_before: String name of an existing column which this
~~         column should be placed before, when creating the new table.

         .. versionadded:: 1.4.0

        :param insert_before: String name of an existing column which this
~~         column should be placed after, when creating the new table.  If
         both :paramref:`.BatchOperations.alter_column.insert_before`
         and :paramref:`.BatchOperations.alter_column.insert_after` are
         omitted, the column is inserted after the last existing column
~~         in the table.

         .. versionadded:: 1.4.0

        .. seealso::

            :meth:`.Operations.alter_column`



    def __init__(self, table_name, column, schema=None, **kw):
        super(AddColumnOp, self).__init__(table_name, schema=schema)
        self.column = column
        self.kw = kw

    def reverse(self):
        return DropColumnOp.from_column_and_tablename(
            self.schema, self.table_name, self.column
        )

    def to_diff_tuple(self):
        return ("add_column", self.schema, self.table_name, self.column)

    def to_column(self):
        return self.column

            from sqlalchemy import INTEGER, VARCHAR, NVARCHAR, Column


## ... source file abbreviated to get to table examples ...


           have been changed:

           * name -> table_name


    def __init__(
        self, table_name, schema=None, table_kw=None, _orig_table=None
    ):
        self.table_name = table_name
        self.schema = schema
        self.table_kw = table_kw or {}
        self._orig_table = _orig_table

    def to_diff_tuple(self):
        return ("remove_table", self.to_table())

    def reverse(self):
        if self._orig_table is None:
            raise ValueError(
                "operation is not reversible; " "original table is not present"
            )
        return CreateTableOp.from_table(self._orig_table)

    @classmethod
    def from_table(cls, table):
~~        return cls(table.name, schema=table.schema, _orig_table=table)

    def to_table(self, migration_context=None):
        if self._orig_table is not None:
            return self._orig_table
        schema_obj = schemaobj.SchemaObjects(migration_context)
        return schema_obj.table(
            self.table_name, schema=self.schema, **self.table_kw
        )

    @classmethod
    @util._with_legacy_names([("name", "table_name")])
    def drop_table(cls, operations, table_name, schema=None, **kw):
        r"""Issue a "drop table" instruction using the current
        migration context.


        e.g.::

            drop_table("accounts")

        :param table_name: Name of the table
        :param schema: Optional schema name to operate within.  To control
         quoting of the schema outside of the default behavior, use
         the SQLAlchemy construct


## ... source file continues with no further table examples...

```

