title: sqlalchemy.sql.expression FunctionElement Example Code
category: page
slug: sqlalchemy-sql-expression-functionelement-examples
sortorder: 500031125
toc: False
sidebartitle: sqlalchemy.sql.expression FunctionElement
meta: Example code for understanding how to use the FunctionElement class from the sqlalchemy.sql.expression module of the SQLAlchemy project.


`FunctionElement` is a class within the `sqlalchemy.sql.expression` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-expression-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-expression-columnclause-examples.html">ColumnClause</a>,
<a href="/sqlalchemy-sql-expression-columnelement-examples.html">ColumnElement</a>,
<a href="/sqlalchemy-sql-expression-executable-examples.html">Executable</a>,
and <a href="/sqlalchemy-sql-expression-unaryexpression-examples.html">UnaryExpression</a>
are several other callables with code examples from the same `sqlalchemy.sql.expression` package.

## Example 1 from GeoAlchemy2
[GeoAlchemy2](https://github.com/geoalchemy/geoalchemy2)
([project documentation](https://geoalchemy-2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/GeoAlchemy2/))
extends [SQLAlchemy](/sqlalchemy.html) with new data types for working
with geospatial databases, particularly [PostGIS](http://postgis.net/),
which is a spatial database extender for [PostgreSQL](/postgresql.html).
The project is provided as open source under the
[MIT license](https://github.com/geoalchemy/geoalchemy2/blob/master/COPYING.rst).

[**GeoAlchemy2 / geoalchemy2 / elements.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./elements.py)

```python
# elements.py
import binascii
import struct

try:
    from sqlalchemy.sql import functions
    from sqlalchemy.sql.functions import FunctionElement
except ImportError:  # SQLA < 0.9  # pragma: no cover
    from sqlalchemy.sql import expression as functions
~~    from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy.types import to_instance
from sqlalchemy.ext.compiler import compiles

from .compat import PY3, str as str_
from .exc import ArgumentError


if PY3:
    BinasciiError = binascii.Error
else:
    BinasciiError = TypeError


class HasFunction(object):
    pass


class _SpatialElement(HasFunction):

    def __init__(self, data, srid=-1, extended=False):
        self.srid = srid
        self.data = data
        self.extended = extended



## ... source file abbreviated to get to FunctionElement examples ...



    geom_from_extended_version = 'raster'

    def __init__(self, data):
        try:
            bin_data = binascii.unhexlify(data[:114])
        except BinasciiError:
            bin_data = data
            data = str(binascii.hexlify(data).decode(encoding='utf-8'))
        byte_order = bin_data[0]
        srid = bin_data[53:57]
        if not PY3:
            byte_order = bytearray(byte_order)[0]
        srid = struct.unpack('<I' if byte_order else '>I', srid)[0]
        _SpatialElement.__init__(self, data, srid, True)

    @property
    def desc(self):
        return self.data

    @staticmethod
    def _data_from_desc(desc):
        return desc


~~class CompositeElement(FunctionElement):

    def __init__(self, base, field, type_):
        self.name = field
        self.type = to_instance(type_)

        super(CompositeElement, self).__init__(base)


@compiles(CompositeElement)
def _compile_pgelem(expr, compiler, **kw):
    return '(%s).%s' % (compiler.process(expr.clauses, **kw), expr.name)



## ... source file continues with no further FunctionElement examples...

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
from sqlalchemy.ext.compiler import compiles
~~from sqlalchemy.sql.expression import ColumnElement, FunctionElement
from sqlalchemy.sql.functions import GenericFunction

from .functions.orm import quote


~~class array_get(FunctionElement):
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


class row_to_json(GenericFunction):
    name = 'row_to_json'


## ... source file continues with no further FunctionElement examples...

```

