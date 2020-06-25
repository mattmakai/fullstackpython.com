title: sqlalchemy.ext.compiler compiles code examples
category: page
slug: sqlalchemy-ext-compiler-compiles-examples
sortorder: 500031031
toc: False
sidebartitle: sqlalchemy.ext.compiler compiles
meta: Python example code for the compiles function from the sqlalchemy.ext.compiler module of the SQLAlchemy project.


compiles is a function within the sqlalchemy.ext.compiler module of the SQLAlchemy project.


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
~~from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.schema import Column
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


## ... source file abbreviated to get to compiles examples ...


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

    def __init__(self, table, text):
        self.table = table
        self.text = text
        self.key = text.text
        self.fake_column = schema.Column(self.text.text, sqltypes.NULLTYPE)
        table.append_column(self.fake_column)

    def get_children(self):
        return [self.fake_column]


~~@compiles(_textual_index_element)
def _render_textual_index_column(element, compiler, **kw):
    return compiler.process(element.text, **kw)


class _literal_bindparam(_BindParamClause):
    pass


~~@compiles(_literal_bindparam)
def _render_literal_bindparam(element, compiler, **kw):
    return compiler.render_literal_bindparam(element, **kw)


def _get_index_expressions(idx):
    return list(idx.expressions)


def _get_index_column_names(idx):
    return [getattr(exp, "name", None) for exp in _get_index_expressions(idx)]


def _column_kwargs(col):
    if sqla_13:
        return col.kwargs
    else:
        return {}


def _get_constraint_final_name(constraint, dialect):
    if constraint.name is None:
        return None
    elif sqla_14:
        return dialect.identifier_preparer.format_constraint(


## ... source file continues with no further compiles examples...

```


## Example 2 from sqlalchemy-utils
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

[**sqlalchemy-utils / sqlalchemy_utils / expressions.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./expressions.py)

```python
# expressions.py
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
~~from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import ColumnElement, FunctionElement
from sqlalchemy.sql.functions import GenericFunction

from .functions.orm import quote


class array_get(FunctionElement):
    name = 'array_get'


~~@compiles(array_get)
def compile_array_get(element, compiler, **kw):
    args = list(element.clauses)
    if len(args) != 2:
        raise Exception(
            "Function 'array_get' expects two arguments (%d given)." %
            len(args)
        )

    if not hasattr(args[1], 'value') or not isinstance(args[1].value, int):
        raise Exception(
            "Second argument should be an integer."
        )
    return '(%s)[%s]' % (
        compiler.process(args[0]),
        sa.text(str(args[1].value + 1))
    )


class row_to_json(GenericFunction):
    name = 'row_to_json'
    type = postgresql.JSON


~~@compiles(row_to_json, 'postgresql')
def compile_row_to_json(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


class json_array_length(GenericFunction):
    name = 'json_array_length'
    type = sa.Integer


~~@compiles(json_array_length, 'postgresql')
def compile_json_array_length(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


class Asterisk(ColumnElement):
    def __init__(self, selectable):
        self.selectable = selectable


~~@compiles(Asterisk)
def compile_asterisk(element, compiler, **kw):
    return '%s.*' % quote(compiler.dialect, element.selectable.name)



## ... source file continues with no further compiles examples...

```

