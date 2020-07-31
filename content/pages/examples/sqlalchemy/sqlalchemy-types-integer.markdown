title: sqlalchemy.types Integer Example Code
category: page
slug: sqlalchemy-types-integer-examples
sortorder: 500031140
toc: False
sidebartitle: sqlalchemy.types Integer
meta: Example code for understanding how to use the Integer class from the sqlalchemy.types module of the SQLAlchemy project.


`Integer` is a class within the `sqlalchemy.types` module of the SQLAlchemy project.

<a href="/sqlalchemy-types-boolean-examples.html">BOOLEAN</a>,
<a href="/sqlalchemy-types-boolean-examples.html">Boolean</a>,
<a href="/sqlalchemy-types-date-examples.html">DATE</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DATETIME</a>,
<a href="/sqlalchemy-types-date-examples.html">Date</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DateTime</a>,
<a href="/sqlalchemy-types-enum-examples.html">Enum</a>,
<a href="/sqlalchemy-types-float-examples.html">FLOAT</a>,
<a href="/sqlalchemy-types-float-examples.html">Float</a>,
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
<a href="/sqlalchemy-types-userdefinedtype-examples.html">UserDefinedType</a>,
and <a href="/sqlalchemy-types-to-instance-examples.html">to_instance</a>
are several other callables with code examples from the same `sqlalchemy.types` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / operations / schemaobj.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/operations/schemaobj.py)

```python
# schemaobj.py
from sqlalchemy import schema as sa_schema
~~from sqlalchemy.types import Integer
from sqlalchemy.types import NULLTYPE

from .. import util
from ..util.compat import string_types


class SchemaObjects(object):
    def __init__(self, migration_context=None):
        self.migration_context = migration_context

    def primary_key_constraint(self, name, table_name, cols, schema=None):
        m = self.metadata()
        columns = [sa_schema.Column(n, NULLTYPE) for n in cols]
        t = sa_schema.Table(table_name, m, *columns, schema=schema)
        p = sa_schema.PrimaryKeyConstraint(*[t.c[n] for n in cols], name=name)
        t.append_constraint(p)
        return p

    def foreign_key_constraint(
        self,
        name,
        source,
        referent,
        local_cols,


## ... source file continues with no further Integer examples...

```


## Example 2 from GeoAlchemy2
[GeoAlchemy2](https://github.com/geoalchemy/geoalchemy2)
([project documentation](https://geoalchemy-2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/GeoAlchemy2/))
extends [SQLAlchemy](/sqlalchemy.html) with new data types for working
with geospatial databases, particularly [PostGIS](http://postgis.net/),
which is a spatial database extender for [PostgreSQL](/postgresql.html).
The project is provided as open source under the
[MIT license](https://github.com/geoalchemy/geoalchemy2/blob/master/COPYING.rst).

[**GeoAlchemy2 / geoalchemy2 / types.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./types.py)

```python
# types.py
import warnings

~~from sqlalchemy.types import UserDefinedType, Integer
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql.base import ischema_names

try:
    from .shape import to_shape
    SHAPELY = True
except ImportError:
    SHAPELY = False


from .comparator import BaseComparator, Comparator
from .elements import WKBElement, WKTElement, RasterElement, CompositeElement
from .exc import ArgumentError


class _GISType(UserDefinedType):

    name = None

    from_text = None

    as_binary = None



## ... source file abbreviated to get to Integer examples ...



    def __init__(self, *args, **kwargs):
        kwargs['geometry_type'] = None
        kwargs['srid'] = -1
        super(Raster, self).__init__(*args, **kwargs)
        self.extended = None


class CompositeType(UserDefinedType):

    typemap = {}

    class comparator_factory(UserDefinedType.Comparator):
        def __getattr__(self, key):
            try:
                type_ = self.type.typemap[key]
            except KeyError:
                raise KeyError("Type '%s' doesn't have an attribute: '%s'"
                               % (self.type, key))

            return CompositeElement(self.expr, key, type_)


class GeometryDump(CompositeType):

~~    typemap = {'path': postgresql.ARRAY(Integer), 'geom': Geometry}


ischema_names['geometry'] = Geometry
ischema_names['geography'] = Geography
ischema_names['raster'] = Raster



## ... source file continues with no further Integer examples...

```


## Example 3 from SQLAthanor
[SQLAthanor](https://github.com/insightindustry/sqlathanor)
([PyPI package information](https://pypi.org/project/sqlathanor/)
and
[project documentation](https://sqlathanor.readthedocs.io/en/latest/index.html))
is a [SQLAlchemy](/sqlalchemy.html) extension that provides serialization and
deserialization support for JSON, CSV, YAML and Python dictionaries.
This project is similar to [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
with one major difference: SQLAthanor works through SQLAlchemy models
while Marshmallow is less coupled to SQLAlchemy because it requires
separate representations of the serialization objects. Both libraries
have their uses depending on whether the project plans to use SQLAlchemy
for object representations or would prefer to avoid that couping.
SQLAthanor is open sourced under the
[MIT license](https://github.com/insightindustry/sqlathanor/blob/master/LICENSE).

[**SQLAthanor / sqlathanor / default_deserializers.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./default_deserializers.py)

```python
# default_deserializers.py


import datetime
import io

from validator_collection import validators, checkers

from sqlathanor._compat import json
from sqlathanor.utilities import format_to_tuple, get_class_type_key, \
    raise_UnsupportedSerializationError, raise_UnsupportedDeserializationError
from sqlathanor.errors import UnsupportedValueTypeError

~~from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval

DEFAULT_PYTHON_SQL_TYPE_MAPPING = {
    'bool': Boolean,
    'str': Text,
    'int': Integer,
    'float': Float,
    'datetime': DateTime,
    'date': Date,
    'time': Time,
    'timedelta': Interval
}

def get_default_deserializer(class_attribute = None,
                             format = None):
    format_to_tuple(format)
    format = format.lower()

    class_type_key = get_class_type_key(class_attribute, None)

    deserializer_dict = DEFAULT_DESERIALIZERS.get(class_type_key, None)

    if deserializer_dict is None:
        return None



## ... source file continues with no further Integer examples...

```

