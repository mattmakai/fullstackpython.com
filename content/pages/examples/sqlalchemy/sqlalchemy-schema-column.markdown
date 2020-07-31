title: sqlalchemy.schema Column Example Code
category: page
slug: sqlalchemy-schema-column-examples
sortorder: 500031099
toc: False
sidebartitle: sqlalchemy.schema Column
meta: Example code for understanding how to use the Column class from the sqlalchemy.schema module of the SQLAlchemy project.


`Column` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-createtable-examples.html">CreateTable</a>,
<a href="/sqlalchemy-schema-ddlelement-examples.html">DDLElement</a>,
<a href="/sqlalchemy-schema-foreignkey-examples.html">ForeignKey</a>,
<a href="/sqlalchemy-schema-foreignkeyconstraint-examples.html">ForeignKeyConstraint</a>,
<a href="/sqlalchemy-schema-index-examples.html">Index</a>,
<a href="/sqlalchemy-schema-primarykeyconstraint-examples.html">PrimaryKeyConstraint</a>,
and <a href="/sqlalchemy-schema-table-examples.html">Table</a>
are several other callables with code examples from the same `sqlalchemy.schema` package.

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
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CheckConstraint
~~from sqlalchemy.schema import Column
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
sqla_1216 = _vers >= (1, 2, 16)
sqla_13 = _vers >= (1, 3)


## ... source file abbreviated to get to Column examples ...


    tokens = spec.split(".")
    tokens.pop(-1)  # colname
    tablekey = ".".join(tokens)
    return tablekey == constraint.parent.key


def _is_type_bound(constraint):
    return constraint._type_bound


def _find_columns(clause):

    cols = set()
    traverse(clause, {}, {"column": cols.add})
    return cols


def _remove_column_from_collection(collection, column):

    to_remove = collection[column.key]
    collection.remove(to_remove)


def _textual_index_column(table, text_):
    if isinstance(text_, compat.string_types):
~~        c = Column(text_, sqltypes.NULLTYPE)
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


@compiles(_textual_index_element)


## ... source file continues with no further Column examples...

```


## Example 2 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / loader.py**](https://github.com/python-gino/gino/blob/master/src/gino/./loader.py)

```python
# loader.py
import types
import warnings

from sqlalchemy import select
~~from sqlalchemy.schema import Column
from sqlalchemy.sql.elements import Label

from .declarative import Model


class Loader:

    @classmethod
    def get(cls, value):
        from .crud import Alias

        if isinstance(value, Loader):
            rv = value
        elif isinstance(value, type) and issubclass(value, Model):
            rv = ModelLoader(value)
        elif isinstance(value, Alias):
            rv = AliasLoader(value)
~~        elif isinstance(value, Column):
            rv = ColumnLoader(value)
        elif isinstance(value, Label):
            rv = ColumnLoader(value.name)
        elif isinstance(value, tuple):
            rv = TupleLoader(value)
        elif callable(value):
            rv = CallableLoader(value)
        else:
            rv = ValueLoader(value)
        return rv

    @property
    def query(self):
        rv = select(self.get_columns())
        from_clause = self.get_from()
        if from_clause is not None:
            rv = rv.select_from(from_clause)
        return rv.execution_options(loader=self)

    def do_load(self, row, context):
        raise NotImplementedError

    def get_columns(self):
        return []

    def get_from(self):
        return None

    def __getattr__(self, item):
        return getattr(self.query, item)


_none = object()


def _get_column(model, column_or_name) -> Column:
    if isinstance(column_or_name, str):
        return getattr(model, column_or_name)

~~    if isinstance(column_or_name, Column):
        if column_or_name in model:
            return column_or_name
        raise AttributeError(
            "Column {} does not belong to model {}".format(column_or_name, model)
        )

    raise TypeError(
        "Unknown column {} with type {}".format(column_or_name, type(column_or_name))
    )


class ModelLoader(Loader):

    def __init__(self, model, *columns, **extras):
        self.model = model
        self._distinct = None
        if columns:
            self.columns = [_get_column(model, name) for name in columns]
        else:
            self.columns = model
        self.extras = dict((key, self.get(value)) for key, value in extras.items())
        self.on_clause = None

    def _do_load(self, row):


## ... source file continues with no further Column examples...

```


## Example 3 from PyHive
[PyHive](https://github.com/dropbox/PyHive)
([PyPI package information](https://pypi.org/project/PyHive/))
is a set of [DB-API](https://www.python.org/dev/peps/pep-0249/)
and
[SQLAlchemy](/sqlalchemy.html)
interfaces that make it easier to use [Presto](https://prestodb.io/)
and [Apache Hive](http://hive.apache.org/) with Python.
[Dropbox's engineering team](https://www.dropbox.com/jobs/teams/engineering)
created this code library, open sourced it and put it out under
the [Apache 2.0 license](https://github.com/dropbox/PyHive/blob/master/LICENSE).

[**PyHive / pyhive / tests / test_sqlalchemy_hive.py**](https://github.com/dropbox/PyHive/blob/master/pyhive/tests/test_sqlalchemy_hive.py)

```python
# test_sqlalchemy_hive.py
from __future__ import absolute_import
from __future__ import unicode_literals
from builtins import str
from pyhive.sqlalchemy_hive import HiveDate
from pyhive.sqlalchemy_hive import HiveDecimal
from pyhive.sqlalchemy_hive import HiveTimestamp
from pyhive.tests.sqlalchemy_test_case import SqlAlchemyTestCase
from pyhive.tests.sqlalchemy_test_case import with_engine_connection
from sqlalchemy import types
from sqlalchemy.engine import create_engine
~~from sqlalchemy.schema import Column
from sqlalchemy.schema import MetaData
from sqlalchemy.schema import Table
import contextlib
import datetime
import decimal
import sqlalchemy.types
import unittest

_ONE_ROW_COMPLEX_CONTENTS = [
    True,
    127,
    32767,
    2147483647,
    9223372036854775807,
    0.5,
    0.25,
    'a string',
    datetime.datetime(1970, 1, 1),
    b'123',
    '[1,2]',
    '{1:2,3:4}',
    '{"a":1,"b":2}',
    '{0:1}',
    decimal.Decimal('0.1'),


## ... source file abbreviated to get to Column examples ...


        self.assertEqual(list(row), _ONE_ROW_COMPLEX_CONTENTS)

        self.assertIsInstance(one_row_complex.c.boolean.type, types.Boolean)
        self.assertIsInstance(one_row_complex.c.tinyint.type, types.Integer)
        self.assertIsInstance(one_row_complex.c.smallint.type, types.Integer)
        self.assertIsInstance(one_row_complex.c.int.type, types.Integer)
        self.assertIsInstance(one_row_complex.c.bigint.type, types.BigInteger)
        self.assertIsInstance(one_row_complex.c.float.type, types.Float)
        self.assertIsInstance(one_row_complex.c.double.type, types.Float)
        self.assertIsInstance(one_row_complex.c.string.type, types.String)
        self.assertIsInstance(one_row_complex.c.timestamp.type, HiveTimestamp)
        self.assertIsInstance(one_row_complex.c.binary.type, types.String)
        self.assertIsInstance(one_row_complex.c.array.type, types.String)
        self.assertIsInstance(one_row_complex.c.map.type, types.String)
        self.assertIsInstance(one_row_complex.c.struct.type, types.String)
        self.assertIsInstance(one_row_complex.c.union.type, types.String)
        self.assertIsInstance(one_row_complex.c.decimal.type, HiveDecimal)

    @with_engine_connection
    def test_type_map(self, engine, connection):
        row = connection.execute('SELECT * FROM one_row_complex').fetchone()
        self.assertListEqual(list(row), _ONE_ROW_COMPLEX_CONTENTS)

    @with_engine_connection
    def test_reserved_words(self, engine, connection):
~~        fake_table = Table('select', MetaData(bind=engine), Column('map', sqlalchemy.types.String))
        query = str(fake_table.select(fake_table.c.map == 'a'))
        self.assertIn('`select`', query)
        self.assertIn('`map`', query)
        self.assertNotIn('"select"', query)
        self.assertNotIn('"map"', query)

    def test_switch_database(self):
        engine = create_engine('hive://localhost:10000/pyhive_test_database')
        try:
            with contextlib.closing(engine.connect()) as connection:
                self.assertIn(
                    ('dummy_table',),
                    connection.execute('SHOW TABLES').fetchall()
                )
                connection.execute('USE default')
                self.assertIn(
                    ('one_row',),
                    connection.execute('SHOW TABLES').fetchall()
                )
        finally:
            engine.dispose()

    @with_engine_connection
    def test_lots_of_types(self, engine, connection):


## ... source file continues with no further Column examples...

```

