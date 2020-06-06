title: sqlalchemy.schema ForeignKey code examples
category: page
slug: sqlalchemy-schema-foreignkey-examples
sortorder: 500031005
toc: False
sidebartitle: sqlalchemy.schema ForeignKey
meta: Python example code for the ForeignKey class from the sqlalchemy.schema module of the SQLAlchemy project.


ForeignKey is a class within the sqlalchemy.schema module of the SQLAlchemy project.


## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / util / sqla_compat.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/util/sqla_compat.py)

```python
# sqla_compat.py
import re

from sqlalchemy import __version__
from sqlalchemy import inspect
from sqlalchemy import schema
from sqlalchemy import sql
from sqlalchemy import types as sqltypes
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.schema import Column
~~from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.sql.elements import quoted_name
from sqlalchemy.sql.expression import _BindParamClause
from sqlalchemy.sql.expression import _TextClause as TextClause
from sqlalchemy.sql.visitors import traverse

from . import compat


def _safe_int(value):
    try:
        return int(value)
    except:
        return value


_vers = tuple(
    [_safe_int(x) for x in re.findall(r"(\d+|[abc]\d)", __version__)]
)
sqla_110 = _vers >= (1, 1, 0)
sqla_1115 = _vers >= (1, 1, 15)
sqla_120 = _vers >= (1, 2, 0)
sqla_1216 = _vers >= (1, 2, 16)
sqla_13 = _vers >= (1, 3)
sqla_14 = _vers >= (1, 4)


## ... source file abbreviated to get to ForeignKey examples ...


            connectable, tablename, schemaname
        )


def _exec_on_inspector(inspector, statement, **params):
    if sqla_14:
        with inspector._operation_context() as conn:
            return conn.execute(statement, params)
    else:
        return inspector.bind.execute(statement, params)


def _server_default_is_computed(column):
    if not has_computed:
        return False
    else:
        return isinstance(column.computed, Computed)


def _table_for_constraint(constraint):
~~    if isinstance(constraint, ForeignKeyConstraint):
        return constraint.parent
    else:
        return constraint.table


def _columns_for_constraint(constraint):
~~    if isinstance(constraint, ForeignKeyConstraint):
        return [fk.parent for fk in constraint.elements]
    elif isinstance(constraint, CheckConstraint):
        return _find_columns(constraint.sqltext)
    else:
        return list(constraint.columns)


def _fk_spec(constraint):
    source_columns = [
        constraint.columns[key].name for key in constraint.column_keys
    ]

    source_table = constraint.parent.name
    source_schema = constraint.parent.schema
    target_schema = constraint.elements[0].column.table.schema
    target_table = constraint.elements[0].column.table.name
    target_columns = [element.column.name for element in constraint.elements]
    ondelete = constraint.ondelete
    onupdate = constraint.onupdate
    deferrable = constraint.deferrable
    initially = constraint.initially
    return (
        source_schema,
        source_table,


## ... source file continues with no further ForeignKey examples...


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

[**sqlalchemy-utils / sqlalchemy_utils / functions / foreign_keys.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/foreign_keys.py)

```python
# foreign_keys.py
from collections import defaultdict
from itertools import groupby

import sqlalchemy as sa
from sqlalchemy.exc import NoInspectionAvailable
from sqlalchemy.orm import object_session
~~from sqlalchemy.schema import ForeignKeyConstraint, MetaData, Table

from ..query_chain import QueryChain
from .database import has_index
from .orm import get_column_key, get_mapper, get_tables


def get_foreign_key_values(fk, obj):
    return dict(
        (
            fk.constraint.columns.values()[index].key,
            getattr(obj, element.column.key)
        )
        for
        index, element
        in
        enumerate(fk.constraint.elements)
    )


def group_foreign_keys(foreign_keys):
    """
    Return a groupby iterator that groups given foreign keys by table.

    :param foreign_keys: a sequence of foreign keys


## ... source file abbreviated to get to ForeignKey examples ...


    .. seealso:: :func:`get_referencing_foreign_keys`

    .. versionadded: 0.26.1
    """
    foreign_keys = sorted(
        foreign_keys, key=lambda key: key.constraint.table.name
    )
    return groupby(foreign_keys, lambda key: key.constraint.table)


def get_referencing_foreign_keys(mixed):
    """
    Returns referencing foreign keys for given Table object or declarative
    class.

    :param mixed:
        SA Table object or SA declarative class

    ::

~~        get_referencing_foreign_keys(User)  # set([ForeignKey('user.id')])

        get_referencing_foreign_keys(User.__table__)


    This function also understands inheritance. This means it returns
    all foreign keys that reference any table in the class inheritance tree.

    Let's say you have three classes which use joined table inheritance,
    namely TextItem, Article and BlogPost with Article and BlogPost inheriting
    TextItem.

    ::

        # This will check all foreign keys that reference either article table
        # or textitem table.
        get_referencing_foreign_keys(Article)

    .. seealso:: :func:`get_tables`
    """
    if isinstance(mixed, sa.Table):
        tables = [mixed]
    else:
        tables = get_tables(mixed)

    referencing_foreign_keys = set()

    for table in mixed.metadata.tables.values():
        if table not in tables:
            for constraint in table.constraints:
~~                if isinstance(constraint, sa.sql.schema.ForeignKeyConstraint):
                    for fk in constraint.elements:
                        if any(fk.references(t) for t in tables):
                            referencing_foreign_keys.add(fk)
    return referencing_foreign_keys


def merge_references(from_, to, foreign_keys=None):
    """
    Merge the references of an entity into another entity.

    Consider the following models::

        class User(self.Base):
            __tablename__ = 'user'
            id = sa.Column(sa.Integer, primary_key=True)
            name = sa.Column(sa.String(255))

            def __repr__(self):
                return 'User(name=%r)' % self.name

        class BlogPost(self.Base):
            __tablename__ = 'blog_post'
            id = sa.Column(sa.Integer, primary_key=True)
            title = sa.Column(sa.String(255))
~~            author_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))

            author = sa.orm.relationship(User)


    Now lets add some data::

        john = self.User(name='John')
        jack = self.User(name='Jack')
        post = self.BlogPost(title='Some title', author=john)
        post2 = self.BlogPost(title='Other title', author=jack)
        self.session.add_all([
            john,
            jack,
            post,
            post2
        ])
        self.session.commit()


    If we wanted to merge all John's references to Jack it would be as easy as
    ::

        merge_references(john, jack)
        self.session.commit()


## ... source file abbreviated to get to ForeignKey examples ...


    """
    reflected_metadata = MetaData()

    if metadata.bind is None and engine is None:
        raise Exception(
            'Either pass a metadata object with bind or '
            'pass engine as a second parameter'
        )

    constraints = defaultdict(list)

    for table_name in metadata.tables.keys():
        table = Table(
            table_name,
            reflected_metadata,
            autoload=True,
            autoload_with=metadata.bind or engine
        )

        for constraint in table.constraints:
~~            if not isinstance(constraint, ForeignKeyConstraint):
                continue

            if not has_index(constraint):
                constraints[table.name].append(constraint)

    return dict(constraints)


def get_fk_constraint_for_columns(table, *columns):
    for constraint in table.constraints:
        if list(constraint.columns.values()) == list(columns):
            return constraint


## ... source file continues with no further ForeignKey examples...


```

