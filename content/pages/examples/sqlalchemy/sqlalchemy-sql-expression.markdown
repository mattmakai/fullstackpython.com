title: sqlalchemy.sql expression Example Code
category: page
slug: sqlalchemy-sql-expression-examples
sortorder: 500031110
toc: False
sidebartitle: sqlalchemy.sql expression
meta: Python example code that shows how to use the expression callable from the sqlalchemy.sql module of the SQLAlchemy project.


`expression` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-extract-examples.html">extract</a>,
<a href="/sqlalchemy-sql-functions-examples.html">functions</a>,
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

[**GeoAlchemy2 / geoalchemy2 / __init__.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./__init__.py)

```python
# __init__.py
from .types import (  # NOQA
    Geometry,
    Geography,
    Raster
    )

from .elements import (  # NOQA
    WKTElement,
    WKBElement,
    RasterElement
    )

from .exc import ArgumentError

from . import functions  # NOQA
from . import types  # NOQA

from sqlalchemy import Table, event
~~from sqlalchemy.sql import select, func, expression


def _setup_ddl_event_listeners():
    @event.listens_for(Table, "before_create")
    def before_create(target, connection, **kw):
        dispatch("before-create", target, connection)

    @event.listens_for(Table, "after_create")
    def after_create(target, connection, **kw):
        dispatch("after-create", target, connection)

    @event.listens_for(Table, "before_drop")
    def before_drop(target, connection, **kw):
        dispatch("before-drop", target, connection)

    @event.listens_for(Table, "after_drop")
    def after_drop(target, connection, **kw):
        dispatch("after-drop", target, connection)

    def dispatch(event, table, bind):
        if event in ('before-create', 'before-drop'):
            gis_cols = [c for c in table.c if
                        isinstance(c.type, Geometry) and
                        c.type.management is True]

            regular_cols = [x for x in table.c if x not in gis_cols]

            table.info["_saved_columns"] = table.c

~~            column_collection = expression.ColumnCollection()
            for col in regular_cols:
                column_collection.add(col)
            table.columns = column_collection

            if event == 'before-drop':
                for c in gis_cols:
                    if bind.dialect.name == 'sqlite':
                        drop_func = 'DiscardGeometryColumn'
                    elif bind.dialect.name == 'postgresql':
                        drop_func = 'DropGeometryColumn'
                    else:
                        raise ArgumentError('dialect {} is not supported'.format(bind.dialect.name))
                    args = [table.schema] if table.schema else []
                    args.extend([table.name, c.name])

                    stmt = select([getattr(func, drop_func)(*args)])
                    stmt = stmt.execution_options(autocommit=True)
                    bind.execute(stmt)

        elif event == 'after-create':
            table.columns = table.info.pop('_saved_columns')

            for c in table.c:
                if isinstance(c.type, Geometry) and c.type.management is True:


## ... source file continues with no further expression examples...

```

