title: sqlalchemy.sql.functions GenericFunction Example Code
category: page
slug: sqlalchemy-sql-functions-genericfunction-examples
sortorder: 500031128
toc: False
sidebartitle: sqlalchemy.sql.functions GenericFunction
meta: Example code for understanding how to use the GenericFunction class from the sqlalchemy.sql.functions module of the SQLAlchemy project.


`GenericFunction` is a class within the `sqlalchemy.sql.functions` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-functions-functionelement-examples.html">FunctionElement</a>
is another callable from the `sqlalchemy.sql.functions` package with code examples.

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

[**sqlalchemy-utils / sqlalchemy_utils / expressions.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./expressions.py)

```python
# expressions.py
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import ColumnElement, FunctionElement
~~from sqlalchemy.sql.functions import GenericFunction

from .functions.orm import quote


class array_get(FunctionElement):
    name = 'array_get'


@compiles(array_get)
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


~~class row_to_json(GenericFunction):
    name = 'row_to_json'
    type = postgresql.JSON


@compiles(row_to_json, 'postgresql')
def compile_row_to_json(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


~~class json_array_length(GenericFunction):
    name = 'json_array_length'
    type = sa.Integer


@compiles(json_array_length, 'postgresql')
def compile_json_array_length(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


class Asterisk(ColumnElement):
    def __init__(self, selectable):
        self.selectable = selectable


@compiles(Asterisk)
def compile_asterisk(element, compiler, **kw):
    return '%s.*' % quote(compiler.dialect, element.selectable.name)



## ... source file continues with no further GenericFunction examples...

```

