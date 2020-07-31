title: sqlalchemy.schema DDLElement Example Code
category: page
slug: sqlalchemy-schema-ddlelement-examples
sortorder: 500031102
toc: False
sidebartitle: sqlalchemy.schema DDLElement
meta: Example code for understanding how to use the DDLElement class from the sqlalchemy.schema module of the SQLAlchemy project.


`DDLElement` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-createtable-examples.html">CreateTable</a>,
<a href="/sqlalchemy-schema-foreignkey-examples.html">ForeignKey</a>,
<a href="/sqlalchemy-schema-foreignkeyconstraint-examples.html">ForeignKeyConstraint</a>,
<a href="/sqlalchemy-schema-index-examples.html">Index</a>,
<a href="/sqlalchemy-schema-primarykeyconstraint-examples.html">PrimaryKeyConstraint</a>,
and <a href="/sqlalchemy-schema-table-examples.html">Table</a>
are several other callables with code examples from the same `sqlalchemy.schema` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / ddl / base.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/ddl/base.py)

```python
# base.py
import functools

from sqlalchemy import exc
from sqlalchemy import Integer
from sqlalchemy import types as sqltypes
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import Column
~~from sqlalchemy.schema import DDLElement
from sqlalchemy.sql.elements import quoted_name

from ..util import sqla_compat
from ..util.sqla_compat import _columns_for_constraint  # noqa
from ..util.sqla_compat import _find_columns  # noqa
from ..util.sqla_compat import _fk_spec  # noqa
from ..util.sqla_compat import _is_type_bound  # noqa
from ..util.sqla_compat import _table_for_constraint  # noqa


~~class AlterTable(DDLElement):


    def __init__(self, table_name, schema=None):
        self.table_name = table_name
        self.schema = schema


class RenameTable(AlterTable):
    def __init__(self, old_table_name, new_table_name, schema=None):
        super(RenameTable, self).__init__(old_table_name, schema=schema)
        self.new_table_name = new_table_name


class AlterColumn(AlterTable):
    def __init__(
        self,
        name,
        column_name,
        schema=None,
        existing_type=None,
        existing_nullable=None,
        existing_server_default=None,
        existing_comment=None,
    ):


## ... source file continues with no further DDLElement examples...

```


## Example 2 from Amazon Redshift SQLAlchemy Dialect
[Amazon Redshift SQLAlchemy Dialect](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
that can communicate with the [AWS Redshift](https://aws.amazon.com/redshift/)
data store. The SQL is essentially [PostgreSQL](/postgresql.html)
and requires [psycopg2](https://www.psycopg.org/) to properly
operate. This project and its code are open sourced under the
[MIT license](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/LICENSE).

[**Amazon Redshift SQLAlchemy Dialect / sqlalchemy_redshift / ddl.py**](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/sqlalchemy_redshift/./ddl.py)

```python
# ddl.py
import sqlalchemy as sa
from sqlalchemy.ext import compiler as sa_compiler
~~from sqlalchemy.schema import DDLElement

from .compat import string_types


def _check_if_key_exists(key):
    return isinstance(key, sa.Column) or key


def get_table_attributes(preparer,
                         diststyle=None,
                         distkey=None,
                         sortkey=None,
                         interleaved_sortkey=None):
    text = ""

    has_distkey = _check_if_key_exists(distkey)
    if diststyle:
        diststyle = diststyle.upper()
        if diststyle not in ('EVEN', 'KEY', 'ALL'):
            raise sa.exc.ArgumentError(
                u"diststyle {0} is invalid".format(diststyle)
            )
        if diststyle != 'KEY' and has_distkey:
            raise sa.exc.ArgumentError(


## ... source file abbreviated to get to DDLElement examples ...


    text = """\
        CREATE MATERIALIZED VIEW {name}
        {backup}
        {table_attributes}
        AS {selectable}\
    Drop the materialized view from the database.
    SEE:
    docs.aws.amazon.com/redshift/latest/dg/materialized-view-drop-sql-command

    This undoes the create command, as expected:

    >>> import sqlalchemy as sa
    >>> from sqlalchemy_redshift.dialect import DropMaterializedView
    >>> engine = sa.create_engine('redshift+psycopg2://example')
    >>> drop = DropMaterializedView(
    ...     'materialized_view_of_users',
    ...     if_exists=True
    ... )
    >>> print(drop.compile(engine))
    <BLANKLINE>
    DROP MATERIALIZED VIEW IF EXISTS materialized_view_of_users
    <BLANKLINE>
    <BLANKLINE>

    This can be included in any execute() statement.
~~        Build the DropMaterializedView DDLElement.

        Parameters
        ----------
        name: str
            name of the materialized view to drop
        if_exists: bool, optional
            if True, the IF EXISTS clause is added. This will make the query
            successful even if the view does not exist, i.e. it lets you drop
            a non-existant view. Defaults to False.
        cascade: bool, optional
            if True, the CASCADE clause is added. This will drop all
            views/objects in the DB that depend on this materialized view.
            Defaults to False.
    Formats and returns the drop statement for materialized views.

            distkey = distkey.name
        text += " DISTKEY ({0})".format(preparer.quote(distkey))

    has_sortkey = _check_if_key_exists(sortkey)
    has_interleaved = _check_if_key_exists(interleaved_sortkey)
    if has_sortkey and has_interleaved:
        raise sa.exc.ArgumentError(
            "Parameters sortkey and interleaved_sortkey are "
            "mutually exclusive; you may not specify both."
        )

    if has_sortkey or has_interleaved:
        keys = sortkey if has_sortkey else interleaved_sortkey
        if isinstance(keys, (string_types, sa.Column)):
            keys = [keys]
        keys = [key.name if isinstance(key, sa.Column) else key
                for key in keys]
        if has_interleaved:
            text += " INTERLEAVED"
        sortkey_string = ", ".join(preparer.quote(key)
                                   for key in keys)
        text += " SORTKEY ({0})".format(sortkey_string)
    return text


~~class CreateMaterializedView(DDLElement):
    def __init__(self, name, selectable, backup=True, diststyle=None,
                 distkey=None, sortkey=None, interleaved_sortkey=None):
        self.name = name
        self.selectable = selectable
        self.backup = backup
        self.diststyle = diststyle
        self.distkey = distkey
        self.sortkey = sortkey
        self.interleaved_sortkey = interleaved_sortkey


@sa_compiler.compiles(CreateMaterializedView)
def compile_create_materialized_view(element, compiler, **kw):



## ... source file continues with no further DDLElement examples...

```


## Example 3 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlalchemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / view.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./view.py)

```python
# view.py
import sqlalchemy as sa
from sqlalchemy.ext import compiler
~~from sqlalchemy.schema import DDLElement, PrimaryKeyConstraint


~~class CreateView(DDLElement):
    def __init__(self, name, selectable, materialized=False):
        self.name = name
        self.selectable = selectable
        self.materialized = materialized


@compiler.compiles(CreateView)
def compile_create_materialized_view(element, compiler, **kw):
    return 'CREATE {}VIEW {} AS {}'.format(
        'MATERIALIZED ' if element.materialized else '',
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


~~class DropView(DDLElement):
    def __init__(self, name, materialized=False, cascade=True):
        self.name = name
        self.materialized = materialized
        self.cascade = cascade


@compiler.compiles(DropView)
def compile_drop_materialized_view(element, compiler, **kw):
    return 'DROP {}VIEW IF EXISTS {} {}'.format(
        'MATERIALIZED ' if element.materialized else '',
        element.name,
        'CASCADE' if element.cascade else ''
    )


def create_table_from_selectable(
    name,
    selectable,
    indexes=None,
    metadata=None,
    aliases=None
):
    if indexes is None:
        indexes = []


## ... source file continues with no further DDLElement examples...

```

