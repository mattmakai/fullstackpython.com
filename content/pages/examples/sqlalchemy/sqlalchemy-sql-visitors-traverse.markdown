title: sqlalchemy.sql.visitors traverse Example Code
category: page
slug: sqlalchemy-sql-visitors-traverse-examples
sortorder: 500031134
toc: False
sidebartitle: sqlalchemy.sql.visitors traverse
meta: Python example code that shows how to use the traverse callable from the sqlalchemy.sql.visitors module of the SQLAlchemy project.


`traverse` is a callable within the `sqlalchemy.sql.visitors` module of the SQLAlchemy project.



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
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.sql.elements import quoted_name
from sqlalchemy.sql.expression import _BindParamClause
from sqlalchemy.sql.expression import _TextClause as TextClause
~~from sqlalchemy.sql.visitors import traverse

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
try:
    from sqlalchemy import Computed  # noqa

    has_computed = True


## ... source file abbreviated to get to traverse examples ...


        target_schema,
        target_table,
        target_columns,
        onupdate,
        ondelete,
        deferrable,
        initially,
    )


def _fk_is_self_referential(constraint):
    spec = constraint.elements[0]._get_colspec()
    tokens = spec.split(".")
    tokens.pop(-1)  # colname
    tablekey = ".".join(tokens)
    return tablekey == constraint.parent.key


def _is_type_bound(constraint):
    return constraint._type_bound


def _find_columns(clause):

    cols = set()
~~    traverse(clause, {}, {"column": cols.add})
    return cols


def _remove_column_from_collection(collection, column):

    to_remove = collection[column.key]
    collection.remove(to_remove)


def _textual_index_column(table, text_):
    if isinstance(text_, compat.string_types):
        c = Column(text_, sqltypes.NULLTYPE)
        table.append_column(c)
        return c
    elif isinstance(text_, TextClause):
        return _textual_index_element(table, text_)
    else:
        raise ValueError("String or text() construct expected")


class _textual_index_element(sql.ColumnElement):

    __visit_name__ = "_textual_idx_element"



## ... source file continues with no further traverse examples...

```

