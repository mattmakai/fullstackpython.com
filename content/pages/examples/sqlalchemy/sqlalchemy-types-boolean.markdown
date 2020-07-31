title: sqlalchemy.types Boolean Example Code
category: page
slug: sqlalchemy-types-boolean-examples
sortorder: 500031135
toc: False
sidebartitle: sqlalchemy.types Boolean
meta: Example code for understanding how to use the Boolean class from the sqlalchemy.types module of the SQLAlchemy project.


`Boolean` is a class within the `sqlalchemy.types` module of the SQLAlchemy project.

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
<a href="/sqlalchemy-types-string-examples.html">String</a>,
<a href="/sqlalchemy-types-text-examples.html">TEXT</a>,
<a href="/sqlalchemy-types-time-examples.html">TIME</a>,
<a href="/sqlalchemy-types-text-examples.html">Text</a>,
<a href="/sqlalchemy-types-time-examples.html">Time</a>,
<a href="/sqlalchemy-types-typeengine-examples.html">TypeEngine</a>,
<a href="/sqlalchemy-types-userdefinedtype-examples.html">UserDefinedType</a>,
and <a href="/sqlalchemy-types-to-instance-examples.html">to_instance</a>
are several other callables with code examples from the same `sqlalchemy.types` package.

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




## ... source file abbreviated to get to Boolean examples ...



        self.models = []
        self.collector = ImportCollector()
        classes = {}
        for table in metadata.sorted_tables:
            if table.name in self.ignored_tables:
                continue

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
~~                            table.c[colname].type = Boolean()
                            continue

                        match = _re_enum_check_constraint.match(sqltext)
                        if match:
                            colname = _re_column_name.match(match.group(1)).group(3)
                            items = match.group(2)
                            if isinstance(table.c[colname].type, String):
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


## ... source file continues with no further Boolean examples...

```


## Example 2 from SQLAthanor
[SQLAthanor](https://github.com/insightindustry/sqlathanor)
([PyPI package information](https://pypi.org/project/sqlathanor/)
and
[project documentation](https://sqlathanor.readthedocs.io/en/latest/index.html))
is a [SQLAlchemy](/sqlalchemy.html) extension that provides serialization and
deserialization support for JSON, CSV, YAML and Python dictionaries.
This project is similar to [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
with one major difference: SQLAthanor works through SQLAlchemy models
while Marshmallow is less coupled to SQLAlchemy because it requires
separate representations of the serialization objects. Both libraries
have their uses depending on whether the project plans to use SQLAlchemy
for object representations or would prefer to avoid that couping.
SQLAthanor is open sourced under the
[MIT license](https://github.com/insightindustry/sqlathanor/blob/master/LICENSE).

[**SQLAthanor / sqlathanor / default_deserializers.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./default_deserializers.py)

```python
# default_deserializers.py


import datetime
import io

from validator_collection import validators, checkers

from sqlathanor._compat import json
from sqlathanor.utilities import format_to_tuple, get_class_type_key, \
    raise_UnsupportedSerializationError, raise_UnsupportedDeserializationError
from sqlathanor.errors import UnsupportedValueTypeError

~~from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval

DEFAULT_PYTHON_SQL_TYPE_MAPPING = {
    'bool': Boolean,
    'str': Text,
    'int': Integer,
    'float': Float,
    'datetime': DateTime,
    'date': Date,
    'time': Time,
    'timedelta': Interval
}

def get_default_deserializer(class_attribute = None,
                             format = None):
    format_to_tuple(format)
    format = format.lower()

    class_type_key = get_class_type_key(class_attribute, None)

    deserializer_dict = DEFAULT_DESERIALIZERS.get(class_type_key, None)

    if deserializer_dict is None:
        return None



## ... source file continues with no further Boolean examples...

```

