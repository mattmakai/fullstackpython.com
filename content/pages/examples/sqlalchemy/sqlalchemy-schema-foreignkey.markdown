title: sqlalchemy.schema ForeignKey Example Code
category: page
slug: sqlalchemy-schema-foreignkey-examples
sortorder: 500031103
toc: False
sidebartitle: sqlalchemy.schema ForeignKey
meta: Example code for understanding how to use the ForeignKey class from the sqlalchemy.schema module of the SQLAlchemy project.


`ForeignKey` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-createtable-examples.html">CreateTable</a>,
<a href="/sqlalchemy-schema-ddlelement-examples.html">DDLElement</a>,
<a href="/sqlalchemy-schema-foreignkeyconstraint-examples.html">ForeignKeyConstraint</a>,
<a href="/sqlalchemy-schema-index-examples.html">Index</a>,
<a href="/sqlalchemy-schema-primarykeyconstraint-examples.html">PrimaryKeyConstraint</a>,
and <a href="/sqlalchemy-schema-table-examples.html">Table</a>
are several other callables with code examples from the same `sqlalchemy.schema` package.

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
~~from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import NullType
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


## ... source file abbreviated to get to ForeignKey examples ...


                value = getattr(coltype, attr, missing)
                default = defaults.get(attr, missing)
                if value is missing or value == default:
                    use_kwargs = True
                elif use_kwargs:
                    args.append('{0}={1}'.format(attr, repr(value)))
                else:
                    args.append(repr(value))

        rendered = coltype.__class__.__name__
        if args:
            rendered += '({0})'.format(', '.join(args))

        return rendered

    def render_constraint(self, constraint):
        def render_fk_options(*opts):
            opts = [repr(opt) for opt in opts]
            for attr in 'ondelete', 'onupdate', 'deferrable', 'initially', 'match':
                value = getattr(constraint, attr, None)
                if value:
                    opts.append('{0}={1!r}'.format(attr, value))

            return ', '.join(opts)

~~        if isinstance(constraint, ForeignKey):
            remote_column = '{0}.{1}'.format(constraint.column.table.fullname,
                                             constraint.column.name)
            return 'ForeignKey({0})'.format(render_fk_options(remote_column))
        elif isinstance(constraint, ForeignKeyConstraint):
            local_columns = _get_column_names(constraint)
            remote_columns = ['{0}.{1}'.format(fk.column.table.fullname, fk.column.name)
                              for fk in constraint.elements]
            return 'ForeignKeyConstraint({0})'.format(
                render_fk_options(local_columns, remote_columns))
        elif isinstance(constraint, CheckConstraint):
            return 'CheckConstraint({0!r})'.format(
                self._get_compiled_expression(constraint.sqltext))
        elif isinstance(constraint, UniqueConstraint):
            columns = [repr(col.name) for col in constraint.columns]
            return 'UniqueConstraint({0})'.format(', '.join(columns))

    @staticmethod
    def render_index(index):
        extra_args = [repr(col.name) for col in index.columns]
        if index.unique:
            extra_args.append('unique=True')
        return 'Index({0!r}, {1})'.format(index.name, ', '.join(extra_args))

    def render_column(self, column, show_name):


## ... source file continues with no further ForeignKey examples...

```

