title: sqlalchemy.schema Table code examples
category: page
slug: sqlalchemy-schema-table-examples
sortorder: 500031008
toc: False
sidebartitle: sqlalchemy.schema Table
meta: Python example code for the Table class from the sqlalchemy.schema module of the SQLAlchemy project.


Table is a class within the sqlalchemy.schema module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
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


## ... source file abbreviated to get to Table examples ...


            # do something
            pass


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
~~        SA Table object or SA declarative class

    ::

        get_referencing_foreign_keys(User)  # set([ForeignKey('user.id')])

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


## ... source file abbreviated to get to Table examples ...


def non_indexed_foreign_keys(metadata, engine=None):
    """
    Finds all non indexed foreign keys from all tables of given MetaData.

    Very useful for optimizing postgresql database and finding out which
    foreign keys need indexes.

    :param metadata: MetaData object to inspect tables from
    """
    reflected_metadata = MetaData()

    if metadata.bind is None and engine is None:
        raise Exception(
            'Either pass a metadata object with bind or '
            'pass engine as a second parameter'
        )

    constraints = defaultdict(list)

    for table_name in metadata.tables.keys():
~~        table = Table(
            table_name,
            reflected_metadata,
            autoload=True,
            autoload_with=metadata.bind or engine
        )

        for constraint in table.constraints:
            if not isinstance(constraint, ForeignKeyConstraint):
                continue

            if not has_index(constraint):
                constraints[table.name].append(constraint)

    return dict(constraints)


def get_fk_constraint_for_columns(table, *columns):
    for constraint in table.constraints:
        if list(constraint.columns.values()) == list(columns):
            return constraint


## ... source file continues with no further Table examples...


```

