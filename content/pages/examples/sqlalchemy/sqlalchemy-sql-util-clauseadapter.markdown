title: sqlalchemy.sql.util ClauseAdapter Example Code
category: page
slug: sqlalchemy-sql-util-clauseadapter-examples
sortorder: 500031133
toc: False
sidebartitle: sqlalchemy.sql.util ClauseAdapter
meta: Example code for understanding how to use the ClauseAdapter class from the sqlalchemy.sql.util module of the SQLAlchemy project.


`ClauseAdapter` is a class within the `sqlalchemy.sql.util` module of the SQLAlchemy project.



## Example 1 from sqlalchemy-utils
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

[**sqlalchemy-utils / sqlalchemy_utils / relationships / __init__.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/relationships/__init__.py)

```python
# __init__.py
import sqlalchemy as sa
~~from sqlalchemy.sql.util import ClauseAdapter

from .chained_join import chained_join  # noqa


def path_to_relationships(path, cls):
    relationships = []
    for path_name in path.split('.'):
        rel = getattr(cls, path_name)
        relationships.append(rel)
        cls = rel.mapper.class_
    return relationships


def adapt_expr(expr, *selectables):
    for selectable in selectables:
~~        expr = ClauseAdapter(selectable).traverse(expr)
    return expr


def inverse_join(selectable, left_alias, right_alias, relationship):
    if relationship.property.secondary is not None:
        secondary_alias = sa.alias(relationship.property.secondary)
        return selectable.join(
            secondary_alias,
            adapt_expr(
                relationship.property.secondaryjoin,
                sa.inspect(left_alias).selectable,
                secondary_alias
            )
        ).join(
            right_alias,
            adapt_expr(
                relationship.property.primaryjoin,
                sa.inspect(right_alias).selectable,
                secondary_alias
            )
        )
    else:
        join = sa.orm.join(right_alias, left_alias, relationship)
        onclause = join.onclause


## ... source file continues with no further ClauseAdapter examples...

```

