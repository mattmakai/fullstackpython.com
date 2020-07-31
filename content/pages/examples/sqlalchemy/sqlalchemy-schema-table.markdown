title: sqlalchemy.schema Table Example Code
category: page
slug: sqlalchemy-schema-table-examples
sortorder: 500031107
toc: False
sidebartitle: sqlalchemy.schema Table
meta: Example code for understanding how to use the Table class from the sqlalchemy.schema module of the SQLAlchemy project.


Table is a class within the sqlalchemy.schema module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-createtable-examples.html">CreateTable</a>,
<a href="/sqlalchemy-schema-ddlelement-examples.html">DDLElement</a>,
<a href="/sqlalchemy-schema-foreignkey-examples.html">ForeignKey</a>,
<a href="/sqlalchemy-schema-foreignkeyconstraint-examples.html">ForeignKeyConstraint</a>,
<a href="/sqlalchemy-schema-index-examples.html">Index</a>,
and <a href="/sqlalchemy-schema-primarykeyconstraint-examples.html">PrimaryKeyConstraint</a>
are several other callables with code examples from the same `sqlalchemy.schema` package.

## Example 1 from PyHive
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
from sqlalchemy.schema import Column
from sqlalchemy.schema import MetaData
~~from sqlalchemy.schema import Table
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
]



## ... source file abbreviated to get to Table examples ...


class TestSqlAlchemyHive(unittest.TestCase, SqlAlchemyTestCase):
    def create_engine(self):
        return create_engine('hive://localhost:10000/default')

    @with_engine_connection
    def test_dotted_column_names(self, engine, connection):
        row = connection.execute('SELECT * FROM one_row').fetchone()
        assert row.keys() == ['number_of_rows']
        assert 'number_of_rows' in row
        assert row.number_of_rows == 1
        assert row['number_of_rows'] == 1
        assert getattr(row, 'one_row.number_of_rows') == 1
        assert row['one_row.number_of_rows'] == 1

    @with_engine_connection
    def test_dotted_column_names_raw(self, engine, connection):
        row = connection.execution_options(hive_raw_colnames=True) \
            .execute('SELECT * FROM one_row').fetchone()
        assert row.keys() == ['one_row.number_of_rows']
        assert 'number_of_rows' not in row
        assert getattr(row, 'one_row.number_of_rows') == 1
        assert row['one_row.number_of_rows'] == 1

    @with_engine_connection
    def test_reflect_select(self, engine, connection):
~~        one_row_complex = Table('one_row_complex', MetaData(bind=engine), autoload=True)
        self.assertEqual(len(one_row_complex.c), 15)
        self.assertIsInstance(one_row_complex.c.string, Column)
        row = one_row_complex.select().execute().fetchone()
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
        types = [
            'INT', 'CHAR', 'VARCHAR', 'NCHAR', 'TEXT', 'Text', 'FLOAT',
            'NUMERIC', 'DECIMAL', 'TIMESTAMP', 'DATETIME', 'CLOB', 'BLOB',
            'BOOLEAN', 'SMALLINT', 'DATE', 'TIME',
            'String', 'Integer', 'SmallInteger',
            'Numeric', 'Float', 'DateTime', 'Date', 'Time', 'LargeBinary',
            'Boolean', 'Unicode', 'UnicodeText',
        ]
        cols = []
        for i, t in enumerate(types):
            cols.append(Column(str(i), getattr(sqlalchemy.types, t)))
        cols.append(Column('hive_date', HiveDate))
        cols.append(Column('hive_decimal', HiveDecimal))
        cols.append(Column('hive_timestamp', HiveTimestamp))
~~        table = Table('test_table', MetaData(bind=engine), *cols, schema='pyhive_test_database')
        table.drop(checkfirst=True)
        table.create()
        connection.execute('SET mapred.job.tracker=local')
        connection.execute('USE pyhive_test_database')
        big_number = 10 ** 10 - 1
        connection.execute("""
        INSERT OVERWRITE TABLE test_table
        SELECT
            1, "a", "a", "a", "a", "a", 0.1,
            0.1, 0.1, 0, 0, "a", "a",
            false, 1, 0, 0,
            "a", 1, 1,
            0.1, 0.1, 0, 0, 0, "a",
            false, "a", "a",
            0, %d, 123 + 2000
        FROM default.one_row



## ... source file continues with no further Table examples...

```


## Example 2 from sqlalchemy-utils
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

[**sqlalchemy-utils / sqlalchemy_utils / functions / foreign_keys.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/foreign_keys.py)

```python
# foreign_keys.py
from collections import defaultdict
from itertools import groupby

import sqlalchemy as sa
from sqlalchemy.exc import NoInspectionAvailable
from sqlalchemy.orm import object_session
~~from sqlalchemy.schema import ForeignKeyConstraint, MetaData, Table

from ..query_chain import QueryChain
from .database import has_index
from .orm import get_column_key, get_mapper, get_tables


def get_foreign_key_values(fk, obj):
    return dict(
        (
            fk.constraint.columns.values()[index].key,
            getattr(obj, element.column.key)
        )
        for
        index, element
        in
        enumerate(fk.constraint.elements)
    )


def group_foreign_keys(foreign_keys):
    foreign_keys = sorted(
        foreign_keys, key=lambda key: key.constraint.table.name
    )
    return groupby(foreign_keys, lambda key: key.constraint.table)


## ... source file abbreviated to get to Table examples ...


                getattr(class_, get_column_key(class_, column)) ==
                getattr(
                    obj,
                    sa.inspect(type(obj))
                    .get_property_by_column(
                        foreign_column
                    ).key
                )
            )
        criteria.append(sa.and_(*subcriteria))
    return criteria


def non_indexed_foreign_keys(metadata, engine=None):
    reflected_metadata = MetaData()

    if metadata.bind is None and engine is None:
        raise Exception(
            'Either pass a metadata object with bind or '
            'pass engine as a second parameter'
        )

    constraints = defaultdict(list)

    for table_name in metadata.tables.keys():
~~        table = Table(
            table_name,
            reflected_metadata,
            autoload=True,
            autoload_with=metadata.bind or engine
        )

        for constraint in table.constraints:
            if not isinstance(constraint, ForeignKeyConstraint):
                continue

            if not has_index(constraint):
                constraints[table.name].append(constraint)

    return dict(constraints)


def get_fk_constraint_for_columns(table, *columns):
    for constraint in table.constraints:
        if list(constraint.columns.values()) == list(columns):
            return constraint



## ... source file continues with no further Table examples...

```

