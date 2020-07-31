title: sqlalchemy.sql.sqltypes NullType Example Code
category: page
slug: sqlalchemy-sql-sqltypes-nulltype-examples
sortorder: 500031132
toc: False
sidebartitle: sqlalchemy.sql.sqltypes NullType
meta: Example code for understanding how to use the NullType class from the sqlalchemy.sql.sqltypes module of the SQLAlchemy project.


`NullType` is a class within the `sqlalchemy.sql.sqltypes` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-sqltypes-nulltype-examples.html">NullType</a>
is another callable from the `sqlalchemy.sql.sqltypes` package with code examples.

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
~~from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.types import Boolean, String
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



## ... source file abbreviated to get to NullType examples ...


        type_ = type(obj) if not isinstance(obj, type) else obj
        pkgname = type_.__module__

        if pkgname.startswith('sqlalchemy.dialects.'):
            dialect_pkgname = '.'.join(pkgname.split('.')[0:3])
            dialect_pkg = import_module(dialect_pkgname)

            if type_.__name__ in dialect_pkg.__all__:
                pkgname = dialect_pkgname
        else:
            pkgname = 'sqlalchemy' if type_.__name__ in sqlalchemy.__all__ else type_.__module__
        self.add_literal_import(pkgname, type_.__name__)

    def add_literal_import(self, pkgname, name):
        names = self.setdefault(pkgname, set())
        names.add(name)


class Model(object):
    def __init__(self, table):
        super(Model, self).__init__()
        self.table = table
        self.schema = table.schema

        for column in table.columns:
~~            if not isinstance(column.type, NullType):
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

                if isinstance(coltype, ARRAY):
                    new_coltype.item_type = self._get_adapted_type(new_coltype.item_type, bind)

                try:
                    if new_coltype.compile(bind.dialect) != compiled_type:
                        if not isinstance(new_coltype, Float) and \
                           not (isinstance(new_coltype, ARRAY) and
                                isinstance(new_coltype.item_type, Float)):
                            break
                except sqlalchemy.exc.CompileError:


## ... source file continues with no further NullType examples...

```

