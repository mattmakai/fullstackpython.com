title: sqlalchemy.types Integer code examples
category: page
slug: sqlalchemy-types-integer-examples
sortorder: 500031103
toc: False
sidebartitle: sqlalchemy.types Integer
meta: Python example code for the Integer class from the sqlalchemy.types module of the SQLAlchemy project.


Integer is a class within the sqlalchemy.types module of the SQLAlchemy project.


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

