title: sqlalchemy.types DateTime Example Code
category: page
slug: sqlalchemy-types-datetime-examples
sortorder: 500031137
toc: False
sidebartitle: sqlalchemy.types DateTime
meta: Example code for understanding how to use the DateTime class from the sqlalchemy.types module of the SQLAlchemy project.


`DateTime` is a class within the `sqlalchemy.types` module of the SQLAlchemy project.

<a href="/sqlalchemy-types-boolean-examples.html">BOOLEAN</a>,
<a href="/sqlalchemy-types-boolean-examples.html">Boolean</a>,
<a href="/sqlalchemy-types-date-examples.html">DATE</a>,
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

## Example 1 from SQLAthanor
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



## ... source file continues with no further DateTime examples...

```

