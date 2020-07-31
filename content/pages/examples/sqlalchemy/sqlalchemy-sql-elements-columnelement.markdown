title: sqlalchemy.sql.elements ColumnElement Example Code
category: page
slug: sqlalchemy-sql-elements-columnelement-examples
sortorder: 500031119
toc: False
sidebartitle: sqlalchemy.sql.elements ColumnElement
meta: Example code for understanding how to use the ColumnElement class from the sqlalchemy.sql.elements module of the SQLAlchemy project.


`ColumnElement` is a class within the `sqlalchemy.sql.elements` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-elements-label-examples.html">Label</a>
is another callable from the `sqlalchemy.sql.elements` package with code examples.

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

[**GeoAlchemy2 / geoalchemy2 / functions.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./functions.py)

```python
# functions.py
import re

from sqlalchemy import inspect
from sqlalchemy.sql import functions
~~from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.ext.compiler import compiles

from . import types
from . import elements


~~class TableRowElement(ColumnElement):
    def __init__(self, selectable):
        self.selectable = selectable

    @property
    def _from_objects(self):
        return [self.selectable]


class ST_AsGeoJSON(functions.GenericFunction):

    name = "ST_AsGeoJSON"

    def __init__(self, *args, **kwargs):
        expr = kwargs.pop('expr', None)
        args = list(args)
        if expr is not None:
            args = [expr] + args
        for idx, element in enumerate(args):
            if isinstance(element, functions.Function):
                continue
            elif isinstance(element, elements.HasFunction):
                if element.extended:
                    func_name = element.geom_from_extended_version
                    func_args = [element.data]


## ... source file continues with no further ColumnElement examples...

```

