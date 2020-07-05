title: sqlalchemy.types UserDefinedType Example Code
category: page
slug: sqlalchemy-types-userdefinedtype-examples
sortorder: 500031119
toc: False
sidebartitle: sqlalchemy.types UserDefinedType
meta: Python example code for the UserDefinedType class from the sqlalchemy.types module of the SQLAlchemy project.


UserDefinedType is a class within the sqlalchemy.types module of the SQLAlchemy project.


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

