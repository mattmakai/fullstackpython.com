title: sqlalchemy.sql operators Example Code
category: page
slug: sqlalchemy-sql-operators-examples
sortorder: 500031092
toc: False
sidebartitle: sqlalchemy.sql operators
meta: Python example code for the operators callable from the sqlalchemy.sql module of the SQLAlchemy project.


operators is a callable within the sqlalchemy.sql module of the SQLAlchemy project.


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
from sqlalchemy.types import UserDefinedType
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
~~from sqlalchemy.sql import operators
try:
    from sqlalchemy.sql.functions import _FunctionGenerator
except ImportError:  # SQLA < 0.9  # pragma: no cover
    from sqlalchemy.sql.expression import _FunctionGenerator


~~INTERSECTS = operators.custom_op('&&')
~~OVERLAPS_OR_TO_LEFT = operators.custom_op('&<')
~~OVERLAPS_OR_TO_RIGHT = operators.custom_op('&>')
~~OVERLAPS_OR_BELOW = operators.custom_op('&<|')
~~TO_LEFT = operators.custom_op('<<')
~~BELOW = operators.custom_op('<<|')
~~TO_RIGHT = operators.custom_op('>>')
~~CONTAINED = operators.custom_op('@')
~~OVERLAPS_OR_ABOVE = operators.custom_op('|&>')
~~ABOVE = operators.custom_op('|>>')
~~CONTAINS = operators.custom_op('-')
~~SAME = operators.custom_op('-=')
~~DISTANCE_CENTROID = operators.custom_op('<->')
~~DISTANCE_BOX = operators.custom_op('<#>')


class BaseComparator(UserDefinedType.Comparator):

    key = None

    def __getattr__(self, name):


        if not name.lower().startswith('st_'):
            raise AttributeError


        func_ = _FunctionGenerator(expr=self.expr)
        return getattr(func_, name)

    def intersects(self, other):
        return self.operate(INTERSECTS, other, result_type=sqltypes.Boolean)

    def overlaps_or_to_left(self, other):
        return self.operate(OVERLAPS_OR_TO_LEFT, other,
                            result_type=sqltypes.Boolean)

    def overlaps_or_to_right(self, other):


## ... source file continues with no further operators examples...

```

