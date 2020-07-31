title: sqlalchemy.sql functions Example Code
category: page
slug: sqlalchemy-sql-functions-examples
sortorder: 500031112
toc: False
sidebartitle: sqlalchemy.sql functions
meta: Python example code that shows how to use the functions callable from the sqlalchemy.sql module of the SQLAlchemy project.


`functions` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
<a href="/sqlalchemy-sql-extract-examples.html">extract</a>,
<a href="/sqlalchemy-sql-operators-examples.html">operators</a>,
<a href="/sqlalchemy-sql-schema-examples.html">schema</a>,
<a href="/sqlalchemy-sql-select-examples.html">select</a>,
<a href="/sqlalchemy-sql-sqltypes-examples.html">sqltypes</a>,
and <a href="/sqlalchemy-sql-table-examples.html">table</a>
are several other callables with code examples from the same `sqlalchemy.sql` package.

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
~~from sqlalchemy.sql import functions
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.ext.compiler import compiles

from . import types
from . import elements


class TableRowElement(ColumnElement):
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
~~            if isinstance(element, functions.Function):
                continue
            elif isinstance(element, elements.HasFunction):
                if element.extended:
                    func_name = element.geom_from_extended_version
                    func_args = [element.data]
                else:
                    func_name = element.geom_from
                    func_args = [element.data, element.srid]
                args[idx] = getattr(functions.func, func_name)(*func_args)
            else:
                try:
                    insp = inspect(element)
                    if hasattr(insp, "selectable"):
                        args[idx] = TableRowElement(insp.selectable)
                except Exception:
                    continue

~~        functions.GenericFunction.__init__(self, *args, **kwargs)

    __doc__ = (
        'Return the geometry as a GeoJSON "geometry" object, or the row as a '
        'GeoJSON feature" object (PostGIS 3 only). (Cf GeoJSON specifications RFC '
        '7946). 2D and 3D Geometries are both supported. GeoJSON only support SFS '
        '1.1 geometry types (no curve support for example). '
        'See https://postgis.net/docs/ST_AsGeoJSON.html')


@compiles(TableRowElement)
def _compile_table_row_thing(element, compiler, **kw):

    compiled = compiler.process(list(element.selectable.columns)[0], **kw)

    schema = getattr(element.selectable, "schema", "")
    name = element.selectable.name
    pattern = r"(.?%s.?\.)?(.?%s.?)\." % (schema, name)
    m = re.match(pattern, compiled)
    if m:
        return m.group(2)

    return compiled.split(".")[0]


class GenericFunction(functions.GenericFunction):

    _register = False

    def __init__(self, *args, **kwargs):
        expr = kwargs.pop('expr', None)
        args = list(args)
        if expr is not None:
            args = [expr] + args
        for idx, elem in enumerate(args):
            if isinstance(elem, elements.HasFunction):
                if elem.extended:
                    func_name = elem.geom_from_extended_version
                    func_args = [elem.data]
                else:
                    func_name = elem.geom_from
                    func_args = [elem.data, elem.srid]
                args[idx] = getattr(functions.func, func_name)(*func_args)
~~        functions.GenericFunction.__init__(self, *args, **kwargs)




_FUNCTIONS = [

    ('ST_Collect', types.Geometry,
     'Return a specified ST_Geometry value from a collection of other geometries.'),

    ('ST_BdPolyFromText', types.Geometry,
     'Construct a Polygon given an arbitrary collection of closed linestrings'
     'as a MultiLineString Well-Known text representation.'),

    ('ST_BdMPolyFromText', types.Geometry,
     'Construct a MultiPolygon given an arbitrary collection of closed '
     'linestrings as a MultiLineString text representation Well-Known text '
     'representation.'),

    ('ST_Box2dFromGeoHash', types.Geometry,
     'Return a BOX2D from a GeoHash string.'),

    ('ST_GeogFromText', types.Geography,
     'Return a specified geography value from Well-Known Text representation '
     'or extended (WKT).'),


## ... source file continues with no further functions examples...

```

