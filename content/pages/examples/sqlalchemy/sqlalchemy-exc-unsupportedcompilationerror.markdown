title: sqlalchemy.exc UnsupportedCompilationError Example Code
category: page
slug: sqlalchemy-exc-unsupportedcompilationerror-examples
sortorder: 500031043
toc: False
sidebartitle: sqlalchemy.exc UnsupportedCompilationError
meta: Example code for understanding how to use the UnsupportedCompilationError class from the sqlalchemy.exc module of the SQLAlchemy project.


`UnsupportedCompilationError` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-databaseerror-examples.html">DatabaseError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-invalidrequesterror-examples.html">InvalidRequestError</a>,
<a href="/sqlalchemy-exc-noinspectionavailable-examples.html">NoInspectionAvailable</a>,
<a href="/sqlalchemy-exc-nosuchtableerror-examples.html">NoSuchTableError</a>,
<a href="/sqlalchemy-exc-operationalerror-examples.html">OperationalError</a>,
and <a href="/sqlalchemy-exc-programmingerror-examples.html">ProgrammingError</a>
are several other callables with code examples from the same `sqlalchemy.exc` package.

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

[**SQLAthanor / sqlathanor / utilities.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./utilities.py)

```python
# utilities.py

import csv
import linecache
import warnings
import yaml
from collections import OrderedDict

from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.exc import InvalidRequestError as SA_InvalidRequestError
~~from sqlalchemy.exc import UnsupportedCompilationError as SA_UnsupportedCompilationError

from validator_collection import validators, checkers
from validator_collection.errors import NotAnIterableError

from sqlathanor._compat import json, is_py2, is_py36, is_py35, dict as dict_
from sqlathanor.errors import InvalidFormatError, UnsupportedSerializationError, \
    UnsupportedDeserializationError, MaximumNestingExceededError, \
    MaximumNestingExceededWarning, DeserializationError, CSVStructureError

UTILITY_COLUMNS = [
    'metadata',
    'primary_key_value',
    '_decl_class_registry',
    '_sa_instance_state',
    '_sa_class_manager'
]

def bool_to_tuple(input):

    if input is True:
        input = (True, True)
    elif not input:
        input = (False, False)
    elif not isinstance(input, tuple) or len(input) > 2:


## ... source file continues with no further UnsupportedCompilationError examples...

```

