title: sqlalchemy.orm.attributes QueryableAttribute Example Code
category: page
slug: sqlalchemy-orm-attributes-queryableattribute-examples
sortorder: 500031077
toc: False
sidebartitle: sqlalchemy.orm.attributes QueryableAttribute
meta: Example code for understanding how to use the QueryableAttribute class from the sqlalchemy.orm.attributes module of the SQLAlchemy project.


`QueryableAttribute` is a class within the `sqlalchemy.orm.attributes` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-attributes-instrumentedattribute-examples.html">InstrumentedAttribute</a>
and
<a href="/sqlalchemy-orm-attributes-flag-modified-examples.html">flag_modified</a>
are a couple of other callables within the `sqlalchemy.orm.attributes` package that also have code examples.

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

[**SQLAthanor / sqlathanor / attributes.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./attributes.py)

```python
# attributes.py


~~from sqlalchemy.orm.attributes import QueryableAttribute as SA_QueryableAttribute
from sqlalchemy import util

from validator_collection import validators, checkers

from sqlathanor._serialization_support import SerializationMixin
from sqlathanor.utilities import bool_to_tuple, callable_to_dict


BLANK_ON_SERIALIZE = {
    'csv': None,
    'json': None,
    'yaml': None,
    'dict': None
}


class AttributeConfiguration(SerializationMixin):

    def __init__(self,
                 *args,
                 **kwargs):
        object.__setattr__(self, '_dict_proxy', {})
        self._current = -1
        self._name = None


## ... source file continues with no further QueryableAttribute examples...

```

