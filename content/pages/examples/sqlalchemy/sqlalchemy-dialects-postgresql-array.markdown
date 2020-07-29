title: sqlalchemy.dialects.postgresql ARRAY Example Code
category: page
slug: sqlalchemy-dialects-postgresql-array-examples
sortorder: 500031007
toc: False
sidebartitle: sqlalchemy.dialects.postgresql ARRAY
meta: Python example code that shows how to use the ARRAY constant from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


`ARRAY` is a constant within the `sqlalchemy.dialects.postgresql` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-postgresql-bigint-examples.html">BIGINT</a>,
<a href="/sqlalchemy-dialects-postgresql-bit-examples.html">BIT</a>,
<a href="/sqlalchemy-dialects-postgresql-double-precision-examples.html">DOUBLE_PRECISION</a>,
<a href="/sqlalchemy-dialects-postgresql-excludeconstraint-examples.html">ExcludeConstraint</a>,
<a href="/sqlalchemy-dialects-postgresql-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">JSON</a>,
<a href="/sqlalchemy-dialects-postgresql-tsvector-examples.html">TSVECTOR</a>,
<a href="/sqlalchemy-dialects-postgresql-array-examples.html">array</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">json</a>,
and <a href="/sqlalchemy-dialects-postgresql-pypostgresql-examples.html">pypostgresql</a>
are several other callables with code examples from the same `sqlalchemy.dialects.postgresql` package.

## Example 1 from sqlacodegen
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
from sqlalchemy.types import Boolean, String
from sqlalchemy.util import OrderedDict

try:
    from sqlalchemy import ARRAY
except ImportError:
~~    from sqlalchemy.dialects.postgresql import ARRAY

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


class _DummyInflectEngine(object):
    @staticmethod
    def singular_noun(noun):
        return noun




## ... source file abbreviated to get to ARRAY examples ...


        names.add(name)


class Model(object):
    def __init__(self, table):
        super(Model, self).__init__()
        self.table = table
        self.schema = table.schema

        for column in table.columns:
            if not isinstance(column.type, NullType):
                column.type = self._get_adapted_type(column.type, column.table.bind)

    def _get_adapted_type(self, coltype, bind):
        compiled_type = coltype.compile(bind.dialect)
        for supercls in coltype.__class__.__mro__:
            if not supercls.__name__.startswith('_') and hasattr(supercls, '__visit_name__'):
                kw = {}
                if supercls is Enum:
                    kw['name'] = coltype.name

                new_coltype = coltype.adapt(supercls)
                for key, value in kw.items():
                    setattr(new_coltype, key, value)

~~                if isinstance(coltype, ARRAY):
                    new_coltype.item_type = self._get_adapted_type(new_coltype.item_type, bind)

                try:
                    if new_coltype.compile(bind.dialect) != compiled_type:
                        if not isinstance(new_coltype, Float) and \
                           not (isinstance(new_coltype, ARRAY) and
                                isinstance(new_coltype.item_type, Float)):
                            break
                except sqlalchemy.exc.CompileError:
                    break

                coltype = new_coltype
                if supercls.__name__ != supercls.__name__.upper():
                    break

        return coltype

    def add_imports(self, collector):
        if self.table.columns:
            collector.add_import(Column)

        for column in self.table.columns:
            collector.add_import(column.type)
            if column.server_default:
                if isinstance(column.server_default, Computed):
                    collector.add_literal_import('sqlalchemy', 'Computed')
                else:
                    collector.add_literal_import('sqlalchemy', 'text')

~~            if isinstance(column.type, ARRAY):
                collector.add_import(column.type.item_type.__class__)

        for constraint in sorted(self.table.constraints, key=_get_constraint_sort_key):
            if isinstance(constraint, ForeignKeyConstraint):
                if len(constraint.columns) > 1:
                    collector.add_literal_import('sqlalchemy', 'ForeignKeyConstraint')
                else:
                    collector.add_literal_import('sqlalchemy', 'ForeignKey')
            elif isinstance(constraint, UniqueConstraint):
                if len(constraint.columns) > 1:
                    collector.add_literal_import('sqlalchemy', 'UniqueConstraint')
            elif not isinstance(constraint, PrimaryKeyConstraint):
                collector.add_import(constraint)

        for index in self.table.indexes:
            if len(index.columns) > 1:
                collector.add_import(index)

    @staticmethod
    def _convert_to_valid_identifier(name):
        assert name, 'Identifier cannot be empty'
        if name[0].isdigit() or iskeyword(name):
            name = '_' + name
        elif name == 'metadata':


## ... source file continues with no further ARRAY examples...

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

[**sqlalchemy-utils / sqlalchemy_utils / asserts.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./asserts.py)

```python
# asserts.py
from decimal import Decimal

import sqlalchemy as sa
~~from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.exc import DataError, IntegrityError


def _update_field(obj, field, value):
    session = sa.orm.object_session(obj)
    column = sa.inspect(obj.__class__).columns[field]
    query = column.table.update().values(**{column.key: value})
    session.execute(query)
    session.flush()


def _expect_successful_update(obj, field, value, reraise_exc):
    try:
        _update_field(obj, field, value)
    except (reraise_exc) as e:
        session = sa.orm.object_session(obj)
        session.rollback()
        assert False, str(e)


def _expect_failing_update(obj, field, value, expected_exc):
    try:
        _update_field(obj, field, value)
    except expected_exc:
        pass
    else:
        raise AssertionError('Expected update to raise %s' % expected_exc)
    finally:
        session = sa.orm.object_session(obj)
        session.rollback()


def _repeated_value(type_):
~~    if isinstance(type_, ARRAY):
        if isinstance(type_.item_type, sa.Integer):
            return [0]
        elif isinstance(type_.item_type, sa.String):
            return [u'a']
        elif isinstance(type_.item_type, sa.Numeric):
            return [Decimal('0')]
        else:
            raise TypeError('Unknown array item type')
    else:
        return u'a'


def _expected_exception(type_):
~~    if isinstance(type_, ARRAY):
        return IntegrityError
    else:
        return DataError


def assert_nullable(obj, column):
    _expect_successful_update(obj, column, None, IntegrityError)


def assert_non_nullable(obj, column):
    _expect_failing_update(obj, column, None, IntegrityError)


def assert_max_length(obj, column, max_length):
    type_ = sa.inspect(obj.__class__).columns[column].type
    _expect_successful_update(
        obj,
        column,
        _repeated_value(type_) * max_length,
        _expected_exception(type_)
    )
    _expect_failing_update(
        obj,
        column,


## ... source file continues with no further ARRAY examples...

```

