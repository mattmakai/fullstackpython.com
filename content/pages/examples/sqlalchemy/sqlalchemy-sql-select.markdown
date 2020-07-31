title: sqlalchemy.sql select Example Code
category: page
slug: sqlalchemy-sql-select-examples
sortorder: 500031115
toc: False
sidebartitle: sqlalchemy.sql select
meta: Python example code that shows how to use the select callable from the sqlalchemy.sql module of the SQLAlchemy project.


`select` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
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

            column_collection = expression.ColumnCollection()
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

~~                    stmt = select([getattr(func, drop_func)(*args)])
                    stmt = stmt.execution_options(autocommit=True)
                    bind.execute(stmt)

        elif event == 'after-create':
            table.columns = table.info.pop('_saved_columns')

            for c in table.c:
                if isinstance(c.type, Geometry) and c.type.management is True:
                    args = [table.schema] if table.schema else []
                    args.extend([
                        table.name,
                        c.name,
                        c.type.srid,
                        c.type.geometry_type,
                        c.type.dimension
                    ])
                    if c.type.use_typmod is not None:
                        args.append(c.type.use_typmod)

~~                    stmt = select([func.AddGeometryColumn(*args)])
                    stmt = stmt.execution_options(autocommit=True)
                    bind.execute(stmt)

                if isinstance(c.type, (Geometry, Geography)) and \
                        c.type.spatial_index is True:
                    if bind.dialect.name == 'sqlite':
~~                        stmt = select([func.CreateSpatialIndex(table.name, c.name)])
                        stmt = stmt.execution_options(autocommit=True)
                        bind.execute(stmt)
                    elif bind.dialect.name == 'postgresql':
                        if table.schema:
                            bind.execute('CREATE INDEX "idx_%s_%s" ON "%s"."%s" '
                                         'USING GIST ("%s")' %
                                         (table.name, c.name, table.schema,
                                          table.name, c.name))
                        else:
                            bind.execute('CREATE INDEX "idx_%s_%s" ON "%s" '
                                         'USING GIST ("%s")' %
                                         (table.name, c.name, table.name, c.name))
                    else:
                        raise ArgumentError('dialect {} is not supported'.format(bind.dialect.name))

                if isinstance(c.type, Raster) and c.type.spatial_index is True:
                    if table.schema:
                        bind.execute('CREATE INDEX "idx_%s_%s" ON "%s"."%s" '
                                     'USING GIST (ST_ConvexHull("%s"))' %
                                     (table.name, c.name, table.schema,
                                      table.name, c.name))
                    else:
                        bind.execute('CREATE INDEX "idx_%s_%s" ON "%s" '
                                     'USING GIST (ST_ConvexHull("%s"))' %


## ... source file continues with no further select examples...

```

