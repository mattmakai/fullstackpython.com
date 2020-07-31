title: sqlalchemy.types UserDefinedType Example Code
category: page
slug: sqlalchemy-types-userdefinedtype-examples
sortorder: 500031147
toc: False
sidebartitle: sqlalchemy.types UserDefinedType
meta: Example code for understanding how to use the UserDefinedType class from the sqlalchemy.types module of the SQLAlchemy project.


`UserDefinedType` is a class within the `sqlalchemy.types` module of the SQLAlchemy project.

<a href="/sqlalchemy-types-boolean-examples.html">BOOLEAN</a>,
<a href="/sqlalchemy-types-boolean-examples.html">Boolean</a>,
<a href="/sqlalchemy-types-date-examples.html">DATE</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DATETIME</a>,
<a href="/sqlalchemy-types-date-examples.html">Date</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DateTime</a>,
<a href="/sqlalchemy-types-enum-examples.html">Enum</a>,
<a href="/sqlalchemy-types-float-examples.html">FLOAT</a>,
<a href="/sqlalchemy-types-float-examples.html">Float</a>,
<a href="/sqlalchemy-types-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-types-integer-examples.html">Integer</a>,
<a href="/sqlalchemy-types-interval-examples.html">Interval</a>,
<a href="/sqlalchemy-types-nulltype-examples.html">NULLTYPE</a>,
<a href="/sqlalchemy-types-nulltype-examples.html">NullType</a>,
<a href="/sqlalchemy-types-string-examples.html">String</a>,
<a href="/sqlalchemy-types-text-examples.html">TEXT</a>,
<a href="/sqlalchemy-types-time-examples.html">TIME</a>,
<a href="/sqlalchemy-types-text-examples.html">Text</a>,
<a href="/sqlalchemy-types-time-examples.html">Time</a>,
<a href="/sqlalchemy-types-typeengine-examples.html">TypeEngine</a>,
and <a href="/sqlalchemy-types-to-instance-examples.html">to_instance</a>
are several other callables with code examples from the same `sqlalchemy.types` package.

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

[**GeoAlchemy2 / geoalchemy2 / comparator.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./comparator.py)

```python
# comparator.py

from sqlalchemy import types as sqltypes
~~from sqlalchemy.types import UserDefinedType
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.sql import operators
try:
    from sqlalchemy.sql.functions import _FunctionGenerator
except ImportError:  # SQLA < 0.9  # pragma: no cover
    from sqlalchemy.sql.expression import _FunctionGenerator


INTERSECTS = operators.custom_op('&&')
OVERLAPS_OR_TO_LEFT = operators.custom_op('&<')
OVERLAPS_OR_TO_RIGHT = operators.custom_op('&>')
OVERLAPS_OR_BELOW = operators.custom_op('&<|')
TO_LEFT = operators.custom_op('<<')
BELOW = operators.custom_op('<<|')
TO_RIGHT = operators.custom_op('>>')
CONTAINED = operators.custom_op('@')
OVERLAPS_OR_ABOVE = operators.custom_op('|&>')
ABOVE = operators.custom_op('|>>')
CONTAINS = operators.custom_op('-')
SAME = operators.custom_op('-=')
DISTANCE_CENTROID = operators.custom_op('<->')
DISTANCE_BOX = operators.custom_op('<#>')




## ... source file continues with no further UserDefinedType examples...

```

