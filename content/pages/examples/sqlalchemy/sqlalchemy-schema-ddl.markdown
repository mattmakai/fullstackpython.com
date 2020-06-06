title: sqlalchemy.schema DDL code examples
category: page
slug: sqlalchemy-schema-ddl-examples
sortorder: 500031003
toc: False
sidebartitle: sqlalchemy.schema DDL
meta: Python example code for the DDL class from the sqlalchemy.schema module of the SQLAlchemy project.


DDL is a class within the sqlalchemy.schema module of the SQLAlchemy project.


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

    """Represent an ALTER TABLE statement.

    Only the string name and optional schema name of the table
    is required, not a full Table object.

    """

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


## ... source file continues with no further DDL examples...


```


## Example 2 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
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


## ... source file continues with no further DDL examples...


```

