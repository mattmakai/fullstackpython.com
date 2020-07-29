title: sqlalchemy.dialects postgresql Example Code
category: page
slug: sqlalchemy-dialects-postgresql-examples
sortorder: 500031004
toc: False
sidebartitle: sqlalchemy.dialects postgresql
meta: Python example code that shows how to use the postgresql callable from the sqlalchemy.dialects module of the SQLAlchemy project.


`postgresql` is a callable within the `sqlalchemy.dialects` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-mssql-examples.html">mssql</a>,
<a href="/sqlalchemy-dialects-mysql-examples.html">mysql</a>,
<a href="/sqlalchemy-dialects-oracle-examples.html">oracle</a>,
and <a href="/sqlalchemy-dialects-sqlite-examples.html">sqlite</a>
are several other callables with code examples from the same `sqlalchemy.dialects` package.

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

[**GeoAlchemy2 / geoalchemy2 / types.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./types.py)

```python
# types.py
import warnings

from sqlalchemy.types import UserDefinedType, Integer
from sqlalchemy.sql import func
~~from sqlalchemy.dialects import postgresql
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

    comparator_factory = Comparator



## ... source file abbreviated to get to postgresql examples ...



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



## ... source file continues with no further postgresql examples...

```


## Example 2 from marshmallow-sqlalchemy
[marshmallow-sqlalchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy)
([project documentation](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/))
is a code library that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) with the
[Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
data serialization tool.

The marshmallow-sqlalchemy project is provided as open source under the
[MIT license](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/LICENSE).

[**marshmallow-sqlalchemy / src/marshmallow_sqlalchemy / convert.py**](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/src/marshmallow_sqlalchemy/./convert.py)

```python
# convert.py
import inspect
import functools
import warnings

import uuid
import marshmallow as ma
from marshmallow import validate, fields
~~from sqlalchemy.dialects import postgresql, mysql, mssql
from sqlalchemy.orm import SynonymProperty
import sqlalchemy as sa

from .exceptions import ModelConversionError
from .fields import Related, RelatedList


def _is_field(value):
    return isinstance(value, type) and issubclass(value, fields.Field)


def _has_default(column):
    return (
        column.default is not None
        or column.server_default is not None
        or _is_auto_increment(column)
    )


def _is_auto_increment(column):
    return column.table is not None and column is column.table._autoincrement_column


def _postgres_array_factory(converter, data_type):
    return functools.partial(
        fields.List, converter._get_field_class_for_data_type(data_type.item_type)
    )


class ModelConverter:

    SQLA_TYPE_MAPPING = {
        sa.Enum: fields.Field,
        sa.JSON: fields.Raw,
~~        postgresql.BIT: fields.Integer,
~~        postgresql.OID: fields.Integer,
~~        postgresql.UUID: fields.UUID,
~~        postgresql.MACADDR: fields.String,
~~        postgresql.INET: fields.String,
~~        postgresql.CIDR: fields.String,
~~        postgresql.JSON: fields.Raw,
~~        postgresql.JSONB: fields.Raw,
~~        postgresql.HSTORE: fields.Raw,
~~        postgresql.ARRAY: _postgres_array_factory,
~~        postgresql.MONEY: fields.Decimal,
~~        postgresql.DATE: fields.Date,
~~        postgresql.TIME: fields.Time,
        mysql.BIT: fields.Integer,
        mysql.YEAR: fields.Integer,
        mysql.SET: fields.List,
        mysql.ENUM: fields.Field,
        mysql.INTEGER: fields.Integer,
        mysql.DATETIME: fields.DateTime,
        mssql.BIT: fields.Integer,
    }
    DIRECTION_MAPPING = {"MANYTOONE": False, "MANYTOMANY": True, "ONETOMANY": True}

    def __init__(self, schema_cls=None):
        self.schema_cls = schema_cls

    @property
    def type_mapping(self):
        if self.schema_cls:
            return self.schema_cls.TYPE_MAPPING
        else:
            return ma.Schema.TYPE_MAPPING

    def fields_for_model(
        self,
        model,
        *,


## ... source file continues with no further postgresql examples...

```


## Example 3 from sqlalchemy-datatables
[sqlalchemy-datatables](https://github.com/Pegase745/sqlalchemy-datatables)
([PyPI package information](https://pypi.org/project/sqlalchemy-datatables/))
is a helper library that makes it easier to use [SQLAlchemy](/sqlalchemy.html)
with the jQuery [JavaScript](/javascript.html)
[DataTables](https://datatables.net/) plugin. This library is designed to
be [web framework](/web-frameworks.html) agnostic and provides code examples
for both [Flask](/flask.html) and [Pyramid](/pyramid.html).

The project is built and maintained by
[Michel Nemnom (Pegase745)](https://github.com/Pegase745) and is open
sourced under the
[MIT license](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/LICENSE).

[**sqlalchemy-datatables / datatables / datatables.py**](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/./datatables/datatables.py)

```python
# datatables.py
from __future__ import absolute_import

import math

from sqlalchemy import Text, func, or_
~~from sqlalchemy.dialects import mysql, postgresql, sqlite

from datatables.clean_regex import clean_regex
from datatables.search_methods import SEARCH_METHODS


class DataTables:

    def __init__(self, request, query, columns, allow_regex_searches=False):
        self.params = dict(request)
        if 'sEcho' in self.params:
            raise ValueError(
                'Legacy datatables not supported, upgrade to >=1.10')
        self.query = query
        self.columns = columns
        self.results = None
        self.allow_regex_searches = allow_regex_searches

        self.cardinality_filtered = 0

        self.cardinality = 0

        self.yadcf_params = []
        self.filter_expressions = []
        self.error = None


## ... source file abbreviated to get to postgresql examples ...


            column_nr = int(self.params.get('order[{:d}][column]'.format(i)))
            column = self.columns[column_nr]
            direction = self.params.get('order[{:d}][dir]'.format(i))
            sort_expr = column.sqla_expr
            if direction == 'asc':
                sort_expr = sort_expr.asc()
            elif direction == 'desc':
                sort_expr = sort_expr.desc()
            else:
                raise ValueError(
                    'Invalid order direction: {}'.format(direction))
            if column.nulls_order:
                if column.nulls_order == 'nullsfirst':
                    sort_expr = sort_expr.nullsfirst()
                elif column.nulls_order == 'nullslast':
                    sort_expr = sort_expr.nullslast()
                else:
                    raise ValueError(
                        'Invalid order direction: {}'.format(direction))

            sort_expressions.append(sort_expr)
            i += 1
        self.sort_expressions = sort_expressions

    def _get_regex_operator(self):
~~        if isinstance(self.query.session.bind.dialect, postgresql.dialect):
            return '-'
        elif isinstance(self.query.session.bind.dialect, mysql.dialect):
            return 'REGEXP'
        elif isinstance(self.query.session.bind.dialect, sqlite.dialect):
            return 'REGEXP'
        else:
            raise NotImplementedError(
                'Regex searches are not implemented for this dialect')



## ... source file continues with no further postgresql examples...

```


## Example 4 from sqlalchemy-utils
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
~~from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import ColumnElement, FunctionElement
from sqlalchemy.sql.functions import GenericFunction

from .functions.orm import quote


class array_get(FunctionElement):
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
~~    type = postgresql.JSON


@compiles(row_to_json, 'postgresql')
def compile_row_to_json(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


class json_array_length(GenericFunction):
    name = 'json_array_length'
    type = sa.Integer


@compiles(json_array_length, 'postgresql')
def compile_json_array_length(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


class Asterisk(ColumnElement):
    def __init__(self, selectable):
        self.selectable = selectable


@compiles(Asterisk)
def compile_asterisk(element, compiler, **kw):


## ... source file continues with no further postgresql examples...

```

