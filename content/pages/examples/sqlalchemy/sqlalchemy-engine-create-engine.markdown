title: sqlalchemy.engine create_engine Example Code
category: page
slug: sqlalchemy-engine-create-engine-examples
sortorder: 500031023
toc: False
sidebartitle: sqlalchemy.engine create_engine
meta: Python example code that shows how to use the create_engine callable from the sqlalchemy.engine module of the SQLAlchemy project.


`create_engine` is a callable within the `sqlalchemy.engine` module of the SQLAlchemy project.

<a href="/sqlalchemy-engine-connection-examples.html">Connection</a>,
<a href="/sqlalchemy-engine-engine-examples.html">Engine</a>,
<a href="/sqlalchemy-engine-default-examples.html">default</a>,
and <a href="/sqlalchemy-engine-url-examples.html">url</a>
are several other callables with code examples from the same `sqlalchemy.engine` package.

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
~~from sqlalchemy.engine import create_engine
from sqlalchemy.schema import Column
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
]




class TestSqlAlchemyHive(unittest.TestCase, SqlAlchemyTestCase):
~~    def create_engine(self):
~~        return create_engine('hive://localhost:10000/default')

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
        one_row_complex = Table('one_row_complex', MetaData(bind=engine), autoload=True)
        self.assertEqual(len(one_row_complex.c), 15)


## ... source file abbreviated to get to create_engine examples ...


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
        fake_table = Table('select', MetaData(bind=engine), Column('map', sqlalchemy.types.String))
        query = str(fake_table.select(fake_table.c.map == 'a'))
        self.assertIn('`select`', query)
        self.assertIn('`map`', query)
        self.assertNotIn('"select"', query)
        self.assertNotIn('"map"', query)

    def test_switch_database(self):
~~        engine = create_engine('hive://localhost:10000/pyhive_test_database')
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


## ... source file continues with no further create_engine examples...

```


## Example 2 from sqlacodegen
[sqlacodegen](https://github.com/agronholm/sqlacodegen)
([PyPI package information](https://pypi.org/project/sqlacodegen/))
is a tool for
reading from an existing [relational database](/databases.html) to
generate code to create [SQLAlchemy](/sqlalchemy.html) models based
on that database. The project is primarily written and maintained
by [Alex Grönholm (agronholm)](https://github.com/agronholm) and it
is open sourced under the
[MIT license](https://github.com/agronholm/sqlacodegen/blob/master/LICENSE).

[**sqlacodegen / sqlacodegen / main.py**](https://github.com/agronholm/sqlacodegen/blob/master/sqlacodegen/./main.py)

```python
# main.py
from __future__ import unicode_literals, division, print_function, absolute_import

import argparse
import io
import sys

import pkg_resources
~~from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

from sqlacodegen.codegen import CodeGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Generates SQLAlchemy model code from an existing database.')
    parser.add_argument('url', nargs='?', help='SQLAlchemy url to the database')
    parser.add_argument('--version', action='store_true', help="print the version number and exit")
    parser.add_argument('--schema', help='load tables from an alternate schema')
    parser.add_argument('--tables', help='tables to process (comma-separated, default: all)')
    parser.add_argument('--noviews', action='store_true', help="ignore views")
    parser.add_argument('--noindexes', action='store_true', help='ignore indexes')
    parser.add_argument('--noconstraints', action='store_true', help='ignore constraints')
    parser.add_argument('--nojoined', action='store_true',
                        help="don't autodetect joined table inheritance")
    parser.add_argument('--noinflect', action='store_true',
                        help="don't try to convert tables names to singular form")
    parser.add_argument('--noclasses', action='store_true',
                        help="don't generate classes, only tables")
    parser.add_argument('--nocomments', action='store_true', help="don't render column comments")
    parser.add_argument('--outfile', help='file to write output to (default: stdout)')
    args = parser.parse_args()

    if args.version:
        version = pkg_resources.get_distribution('sqlacodegen').parsed_version
        print(version.public)
        return
    if not args.url:
        print('You must supply a url\n', file=sys.stderr)
        parser.print_help()
        return

~~    engine = create_engine(args.url)
    metadata = MetaData(engine)
    tables = args.tables.split(',') if args.tables else None
    metadata.reflect(engine, args.schema, not args.noviews, tables)

    outfile = io.open(args.outfile, 'w', encoding='utf-8') if args.outfile else sys.stdout
    generator = CodeGenerator(metadata, args.noindexes, args.noconstraints, args.nojoined,
                              args.noinflect, args.noclasses, nocomments=args.nocomments)
    generator.render(outfile)



## ... source file continues with no further create_engine examples...

```


## Example 3 from sqlalchemy-clickhouse
[sqlalchemy-clickhouse](https://github.com/cloudflare/sqlalchemy-clickhouse)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
for communicating with the open source [ClickHouse](https://clickhouse.tech/)
database management system. ClickHouse is column-oriented and therefore
better for some use cases and worse for others compared to a traditional
[relational database](/databases.html).

The code for this project is open sourced under the
[MIT license](https://github.com/cloudflare/sqlalchemy-clickhouse/blob/master/LICENSE.txt)
while ClickHouse is provided as open source under the
[Apache License 2.0](https://github.com/ClickHouse/ClickHouse/blob/master/LICENSE).

[**sqlalchemy-clickhouse / example.py**](https://github.com/cloudflare/sqlalchemy-clickhouse/blob/master/././example.py)

```python
# example.py

import connector
cursor = connector.connect('default').cursor()
cursor.execute('SELECT * FROM test LIMIT 10')
print(cursor.fetchone())

from sqlalchemy.dialects import registry
registry.register("clickhouse", "base", "dialect")

from sqlalchemy import *
~~from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *

~~engine = create_engine('clickhouse://default:@localhost:8123/default')
logs = Table('test', MetaData(bind=engine), autoload=True)
print(select([func.count('*')], from_obj=logs).scalar())



## ... source file continues with no further create_engine examples...

```

