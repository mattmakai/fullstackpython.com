title: sqlalchemy.schema Column code examples
category: page
slug: sqlalchemy-schema-column-examples
sortorder: 500031073
toc: False
sidebartitle: sqlalchemy.schema Column
meta: Python example code for the Column class from the sqlalchemy.schema module of the SQLAlchemy project.


Column is a class within the sqlalchemy.schema module of the SQLAlchemy project.


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
~~from sqlalchemy.schema import Column
from sqlalchemy.schema import ForeignKeyConstraint
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


## ... source file abbreviated to get to Column examples ...


    tokens = spec.split(".")
    tokens.pop(-1)  # colname
    tablekey = ".".join(tokens)
    return tablekey == constraint.parent.key


def _is_type_bound(constraint):
    return constraint._type_bound


def _find_columns(clause):

    cols = set()
    traverse(clause, {}, {"column": cols.add})
    return cols


def _remove_column_from_collection(collection, column):

    to_remove = collection[column.key]
    collection.remove(to_remove)


def _textual_index_column(table, text_):
    if isinstance(text_, compat.string_types):
~~        c = Column(text_, sqltypes.NULLTYPE)
        table.append_column(c)
        return c
    elif isinstance(text_, TextClause):
        return _textual_index_element(table, text_)
    else:
        raise ValueError("String or text() construct expected")


class _textual_index_element(sql.ColumnElement):

    __visit_name__ = "_textual_idx_element"

    def __init__(self, table, text):
        self.table = table
        self.text = text
        self.key = text.text
        self.fake_column = schema.Column(self.text.text, sqltypes.NULLTYPE)
        table.append_column(self.fake_column)

    def get_children(self):
        return [self.fake_column]


@compiles(_textual_index_element)


## ... source file continues with no further Column examples...

```


## Example 2 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / loader.py**](https://github.com/python-gino/gino/blob/master/src/gino/./loader.py)

```python
# loader.py
import types
import warnings

from sqlalchemy import select
~~from sqlalchemy.schema import Column
from sqlalchemy.sql.elements import Label

from .declarative import Model


class Loader:

    @classmethod
    def get(cls, value):
        from .crud import Alias

        if isinstance(value, Loader):
            rv = value
        elif isinstance(value, type) and issubclass(value, Model):
            rv = ModelLoader(value)
        elif isinstance(value, Alias):
            rv = AliasLoader(value)
~~        elif isinstance(value, Column):
            rv = ColumnLoader(value)
        elif isinstance(value, Label):
            rv = ColumnLoader(value.name)
        elif isinstance(value, tuple):
            rv = TupleLoader(value)
        elif callable(value):
            rv = CallableLoader(value)
        else:
            rv = ValueLoader(value)
        return rv

    @property
    def query(self):
        rv = select(self.get_columns())
        from_clause = self.get_from()
        if from_clause is not None:
            rv = rv.select_from(from_clause)
        return rv.execution_options(loader=self)

    def do_load(self, row, context):
        raise NotImplementedError

    def get_columns(self):
        return []

    def get_from(self):
        return None

    def __getattr__(self, item):
        return getattr(self.query, item)


_none = object()


def _get_column(model, column_or_name) -> Column:
    if isinstance(column_or_name, str):
        return getattr(model, column_or_name)

~~    if isinstance(column_or_name, Column):
        if column_or_name in model:
            return column_or_name
        raise AttributeError(
            "Column {} does not belong to model {}".format(column_or_name, model)
        )

    raise TypeError(
        "Unknown column {} with type {}".format(column_or_name, type(column_or_name))
    )


class ModelLoader(Loader):

    def __init__(self, model, *columns, **extras):
        self.model = model
        self._distinct = None
        if columns:
            self.columns = [_get_column(model, name) for name in columns]
        else:
            self.columns = model
        self.extras = dict((key, self.get(value)) for key, value in extras.items())
        self.on_clause = None

    def _do_load(self, row):


## ... source file continues with no further Column examples...

```

