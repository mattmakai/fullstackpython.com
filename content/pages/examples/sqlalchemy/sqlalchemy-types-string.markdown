title: sqlalchemy.types String Example Code
category: page
slug: sqlalchemy-types-string-examples
sortorder: 500031143
toc: False
sidebartitle: sqlalchemy.types String
meta: Example code for understanding how to use the String class from the sqlalchemy.types module of the SQLAlchemy project.


`String` is a class within the `sqlalchemy.types` module of the SQLAlchemy project.

<a href="/sqlalchemy-types-boolean-examples.html">BOOLEAN</a>,
<a href="/sqlalchemy-types-boolean-examples.html">Boolean</a>,
<a href="/sqlalchemy-types-date-examples.html">DATE</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DATETIME</a>,
<a href="/sqlalchemy-types-date-examples.html">Date</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DateTime</a>,
<a href="/sqlalchemy-types-enum-examples.html">Enum</a>,
<a href="/sqlalchemy-types-float-examples.html">FLOAT</a>,
<a href="/sqlalchemy-types-float-examples.html">Float</a>,
<a href="/sqlalchemy-types-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-types-integer-examples.html">Integer</a>,
<a href="/sqlalchemy-types-interval-examples.html">Interval</a>,
<a href="/sqlalchemy-types-nulltype-examples.html">NULLTYPE</a>,
<a href="/sqlalchemy-types-nulltype-examples.html">NullType</a>,
<a href="/sqlalchemy-types-text-examples.html">TEXT</a>,
<a href="/sqlalchemy-types-time-examples.html">TIME</a>,
<a href="/sqlalchemy-types-text-examples.html">Text</a>,
<a href="/sqlalchemy-types-time-examples.html">Time</a>,
<a href="/sqlalchemy-types-typeengine-examples.html">TypeEngine</a>,
<a href="/sqlalchemy-types-userdefinedtype-examples.html">UserDefinedType</a>,
and <a href="/sqlalchemy-types-to-instance-examples.html">to_instance</a>
are several other callables with code examples from the same `sqlalchemy.types` package.

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

[**PyHive / pyhive / tests / test_sqlalchemy_presto.py**](https://github.com/dropbox/PyHive/blob/master/pyhive/tests/test_sqlalchemy_presto.py)

```python
# test_sqlalchemy_presto.py
from __future__ import absolute_import
from __future__ import unicode_literals
from builtins import str
from pyhive.tests.sqlalchemy_test_case import SqlAlchemyTestCase
from pyhive.tests.sqlalchemy_test_case import with_engine_connection
from sqlalchemy import types
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import Column
from sqlalchemy.schema import MetaData
from sqlalchemy.schema import Table
~~from sqlalchemy.types import String

import contextlib
import unittest


class TestSqlAlchemyPresto(unittest.TestCase, SqlAlchemyTestCase):
    def create_engine(self):
        return create_engine('presto://localhost:8080/hive/default?source={}'.format(self.id()))

    def test_bad_format(self):
        self.assertRaises(
            ValueError,
            lambda: create_engine('presto://localhost:8080/hive/default/what'),
        )

    @with_engine_connection
    def test_reflect_select(self, engine, connection):
        one_row_complex = Table('one_row_complex', MetaData(bind=engine), autoload=True)
        self.assertEqual(len(one_row_complex.c), 15 - 1)
        self.assertIsInstance(one_row_complex.c.string, Column)
        rows = one_row_complex.select().execute().fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(list(rows[0]), [
            True,


## ... source file continues with no further String examples...

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

[**sqlacodegen / sqlacodegen / codegen.py**](https://github.com/agronholm/sqlacodegen/blob/master/sqlacodegen/./codegen.py)

```python
# codegen.py
from __future__ import unicode_literals, division, print_function, absolute_import

import inspect
import re
import sys
from collections import defaultdict
from importlib import import_module
from inspect import ArgSpec
from keyword import iskeyword

import sqlalchemy
import sqlalchemy.exc
from sqlalchemy import (
    Enum, ForeignKeyConstraint, PrimaryKeyConstraint, CheckConstraint, UniqueConstraint, Table,
    Column, Float)
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import NullType
~~from sqlalchemy.types import Boolean, String
from sqlalchemy.util import OrderedDict

try:
    from sqlalchemy import ARRAY
except ImportError:
    from sqlalchemy.dialects.postgresql import ARRAY

try:
    from sqlalchemy import Computed
except ImportError:
    Computed = None

try:
    import geoalchemy2  # noqa: F401
except ImportError:
    pass

_re_boolean_check_constraint = re.compile(r"(?:(?:.*?)\.)?(.*?) IN \(0, 1\)")
_re_column_name = re.compile(r'(?:(["`]?)(?:.*)\1\.)?(["`]?)(.*)\2')
_re_enum_check_constraint = re.compile(r"(?:(?:.*?)\.)?(.*?) IN \((.+)\)")
_re_enum_item = re.compile(r"'(.*?)(?<!\\)'")
_re_invalid_identifier = re.compile(r'[^a-zA-Z0-9_]' if sys.version_info[0] < 3 else r'(?u)\W')




## ... source file abbreviated to get to String examples ...



            if noindexes:
                table.indexes.clear()

            if noconstraints:
                table.constraints = {table.primary_key}
                table.foreign_keys.clear()
                for col in table.columns:
                    col.foreign_keys.clear()
            else:
                for constraint in table.constraints.copy():
                    if isinstance(constraint, CheckConstraint):
                        sqltext = self._get_compiled_expression(constraint.sqltext)

                        match = _re_boolean_check_constraint.match(sqltext)
                        if match:
                            colname = _re_column_name.match(match.group(1)).group(3)
                            table.constraints.remove(constraint)
                            table.c[colname].type = Boolean()
                            continue

                        match = _re_enum_check_constraint.match(sqltext)
                        if match:
                            colname = _re_column_name.match(match.group(1)).group(3)
                            items = match.group(2)
~~                            if isinstance(table.c[colname].type, String):
                                table.constraints.remove(constraint)
                                if not isinstance(table.c[colname].type, Enum):
                                    options = _re_enum_item.findall(items)
                                    table.c[colname].type = Enum(*options, native_enum=False)
                                continue

            if noclasses or not table.primary_key or table.name in association_tables:
                model = self.table_model(table)
            else:
                model = self.class_model(table, links[table.name], self.inflect_engine,
                                         not nojoined)
                classes[model.name] = model

            self.models.append(model)
            model.add_imports(self.collector)

        for model in classes.values():
            if model.parent_name != 'Base':
                classes[model.parent_name].children.append(model)
                self.models.remove(model)

        if not any(isinstance(model, self.class_model) for model in self.models):
            self.collector.add_literal_import('sqlalchemy', 'MetaData')
        else:


## ... source file continues with no further String examples...

```

