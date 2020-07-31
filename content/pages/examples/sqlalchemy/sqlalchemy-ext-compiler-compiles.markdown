title: sqlalchemy.ext.compiler compiles Example Code
category: page
slug: sqlalchemy-ext-compiler-compiles-examples
sortorder: 500031047
toc: False
sidebartitle: sqlalchemy.ext.compiler compiles
meta: Python example code that shows how to use the compiles callable from the sqlalchemy.ext.compiler module of the SQLAlchemy project.


`compiles` is a callable within the `sqlalchemy.ext.compiler` module of the SQLAlchemy project.



## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / util / sqla_compat.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/util/sqla_compat.py)

```python
# sqla_compat.py
import re

from sqlalchemy import __version__
from sqlalchemy import inspect
from sqlalchemy import schema
from sqlalchemy import sql
from sqlalchemy import types as sqltypes
~~from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.schema import Column
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.sql.elements import quoted_name
from sqlalchemy.sql.expression import _BindParamClause
from sqlalchemy.sql.expression import _TextClause as TextClause
from sqlalchemy.sql.visitors import traverse

from . import compat


def _safe_int(value):
    try:
        return int(value)
    except:
        return value


_vers = tuple(
    [_safe_int(x) for x in re.findall(r"(\d+|[abc]\d)", __version__)]
)
sqla_110 = _vers >= (1, 1, 0)
sqla_1115 = _vers >= (1, 1, 15)
sqla_120 = _vers >= (1, 2, 0)


## ... source file abbreviated to get to compiles examples ...


    if isinstance(text_, compat.string_types):
        c = Column(text_, sqltypes.NULLTYPE)
        table.append_column(c)
        return c
    elif isinstance(text_, TextClause):
        return _textual_index_element(table, text_)
    else:
        raise ValueError("String or text() construct expected")


class _textual_index_element(sql.ColumnElement):

    __visit_name__ = "_textual_idx_element"

    def __init__(self, table, text):
        self.table = table
        self.text = text
        self.key = text.text
        self.fake_column = schema.Column(self.text.text, sqltypes.NULLTYPE)
        table.append_column(self.fake_column)

    def get_children(self):
        return [self.fake_column]


~~@compiles(_textual_index_element)
def _render_textual_index_column(element, compiler, **kw):
    return compiler.process(element.text, **kw)


class _literal_bindparam(_BindParamClause):
    pass


~~@compiles(_literal_bindparam)
def _render_literal_bindparam(element, compiler, **kw):
    return compiler.render_literal_bindparam(element, **kw)


def _get_index_expressions(idx):
    return list(idx.expressions)


def _get_index_column_names(idx):
    return [getattr(exp, "name", None) for exp in _get_index_expressions(idx)]


def _column_kwargs(col):
    if sqla_13:
        return col.kwargs
    else:
        return {}


def _get_constraint_final_name(constraint, dialect):
    if constraint.name is None:
        return None
    elif sqla_14:
        return dialect.identifier_preparer.format_constraint(


## ... source file continues with no further compiles examples...

```


## Example 2 from Amazon Redshift SQLAlchemy Dialect
[Amazon Redshift SQLAlchemy Dialect](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
that can communicate with the [AWS Redshift](https://aws.amazon.com/redshift/)
data store. The SQL is essentially [PostgreSQL](/postgresql.html)
and requires [psycopg2](https://www.psycopg.org/) to properly
operate. This project and its code are open sourced under the
[MIT license](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/LICENSE).

[**Amazon Redshift SQLAlchemy Dialect / sqlalchemy_redshift / dialect.py**](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/sqlalchemy_redshift/./dialect.py)

```python
# dialect.py
import re
from collections import defaultdict, namedtuple

from packaging.version import Version
import pkg_resources
import sqlalchemy as sa
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql.base import (
    PGCompiler, PGDDLCompiler, PGIdentifierPreparer, PGTypeCompiler
)
from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from sqlalchemy.engine import reflection
~~from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import (
    BinaryExpression, BooleanClauseList, Delete
)
from sqlalchemy.types import (
    VARCHAR, NullType, SMALLINT, INTEGER, BIGINT,
    DECIMAL, REAL, BOOLEAN, CHAR, DATE, TIMESTAMP)
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

from .commands import (
    CopyCommand, UnloadFromSelect, Format, Compression, Encoding,
    CreateLibraryCommand, AlterTableAppendCommand, RefreshMaterializedView
)
from .ddl import (
    CreateMaterializedView, DropMaterializedView, get_table_attributes
)

sa_version = Version(sa.__version__)

try:
    import alembic
except ImportError:
    pass
else:
    from alembic.ddl import postgresql

    from alembic.ddl.base import RenameTable
~~    compiles(RenameTable, 'redshift')(postgresql.visit_rename_table)

    if Version(alembic.__version__) >= Version('1.0.6'):
        from alembic.ddl.base import ColumnComment
~~        compiles(ColumnComment, 'redshift')(postgresql.visit_column_comment)

    class RedshiftImpl(postgresql.PostgresqlImpl):
        __dialect__ = 'redshift'

__all__ = (
    'SMALLINT',
    'INTEGER',
    'BIGINT',
    'DECIMAL',
    'REAL',
    'BOOLEAN',
    'CHAR',
    'DATE',
    'TIMESTAMP',
    'VARCHAR',
    'DOUBLE_PRECISION',
    'TIMESTAMPTZ',

    'CopyCommand', 'UnloadFromSelect', 'RedshiftDialect', 'Compression',
    'Encoding', 'Format', 'CreateLibraryCommand', 'AlterTableAppendCommand',
    'RefreshMaterializedView',

    'CreateMaterializedView', 'DropMaterializedView'
)


## ... source file continues with no further compiles examples...

```


## Example 3 from GeoAlchemy2
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
from sqlalchemy.sql.elements import ColumnElement
~~from sqlalchemy.ext.compiler import compiles

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


## ... source file abbreviated to get to compiles examples ...


        attributes['type'] = type_

        type_str = '{0}.{1}'.format(type_.__module__, type_.__name__)
        docs.append('Return type: :class:`{0}`.'.format(type_str))

    if len(docs) != 0:
        attributes['__doc__'] = '\n\n'.join(docs)

    globals()[name] = type(name, (GenericFunction,), attributes)




_SQLITE_FUNCTIONS = {
    "ST_GeomFromEWKT": "GeomFromEWKT",
    "ST_GeomFromEWKB": "GeomFromEWKB",
    "ST_AsBinary": "AsBinary",
    "ST_AsEWKB": "AsEWKB",
    "ST_AsGeoJSON": "AsGeoJSON",
}


def _compiles_default(cls):
    def _compile_default(element, compiler, **kw):
        return "{}({})".format(cls, compiler.process(element.clauses, **kw))
~~    compiles(globals()[cls])(_compile_default)


def _compiles_sqlite(cls, fn):
    def _compile_sqlite(element, compiler, **kw):
        return "{}({})".format(fn, compiler.process(element.clauses, **kw))
~~    compiles(globals()[cls], "sqlite")(_compile_sqlite)


for cls, fn in _SQLITE_FUNCTIONS.items():
    _compiles_default(cls)
    _compiles_sqlite(cls, fn)

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

        functions.GenericFunction.__init__(self, *args, **kwargs)

    __doc__ = (
        'Return the geometry as a GeoJSON "geometry" object, or the row as a '
        'GeoJSON feature" object (PostGIS 3 only). (Cf GeoJSON specifications RFC '
        '7946). 2D and 3D Geometries are both supported. GeoJSON only support SFS '
        '1.1 geometry types (no curve support for example). '
        'See https://postgis.net/docs/ST_AsGeoJSON.html')


~~@compiles(TableRowElement)
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


## ... source file continues with no further compiles examples...

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
from sqlalchemy.dialects import postgresql
~~from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import ColumnElement, FunctionElement
from sqlalchemy.sql.functions import GenericFunction

from .functions.orm import quote


class array_get(FunctionElement):
    name = 'array_get'


~~@compiles(array_get)
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
    type = postgresql.JSON


~~@compiles(row_to_json, 'postgresql')
def compile_row_to_json(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


class json_array_length(GenericFunction):
    name = 'json_array_length'
    type = sa.Integer


~~@compiles(json_array_length, 'postgresql')
def compile_json_array_length(element, compiler, **kw):
    return "%s(%s)" % (element.name, compiler.process(element.clauses))


class Asterisk(ColumnElement):
    def __init__(self, selectable):
        self.selectable = selectable


~~@compiles(Asterisk)
def compile_asterisk(element, compiler, **kw):
    return '%s.*' % quote(compiler.dialect, element.selectable.name)



## ... source file continues with no further compiles examples...

```

