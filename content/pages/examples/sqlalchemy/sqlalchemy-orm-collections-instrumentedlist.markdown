title: sqlalchemy.orm.collections InstrumentedList Example Code
category: page
slug: sqlalchemy-orm-collections-instrumentedlist-examples
sortorder: 500031079
toc: False
sidebartitle: sqlalchemy.orm.collections InstrumentedList
meta: Example code for understanding how to use the InstrumentedList class from the sqlalchemy.orm.collections module of the SQLAlchemy project.


`InstrumentedList` is a class within the `sqlalchemy.orm.collections` module of the SQLAlchemy project.



## Example 1 from sqlalchemy-utils
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

[**sqlalchemy-utils / sqlalchemy_utils / types / __init__.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/__init__.py)

```python
# __init__.py
from functools import wraps

~~from sqlalchemy.orm.collections import InstrumentedList as _InstrumentedList

from .arrow import ArrowType  # noqa
from .choice import Choice, ChoiceType  # noqa
from .color import ColorType  # noqa
from .country import CountryType  # noqa
from .currency import CurrencyType  # noqa
from .email import EmailType  # noqa
from .encrypted.encrypted_type import EncryptedType  # noqa
from .enriched_datetime.enriched_date_type import EnrichedDateType  # noqa
from .ip_address import IPAddressType  # noqa
from .json import JSONType  # noqa
from .locale import LocaleType  # noqa
from .ltree import LtreeType  # noqa
from .password import Password, PasswordType  # noqa
from .pg_composite import (  # noqa
    CompositeArray,
    CompositeType,
    register_composites,
    remove_composite_listeners
)
from .phone_number import (  # noqa
    PhoneNumber,
    PhoneNumberParseException,
    PhoneNumberType
)
from .range import (  # noqa
    DateRangeType,
    DateTimeRangeType,
    Int8RangeType,
    IntRangeType,
    NumericRangeType
)
from .scalar_list import ScalarListException, ScalarListType  # noqa
from .timezone import TimezoneType  # noqa
from .ts_vector import TSVectorType  # noqa
from .url import URLType  # noqa
from .uuid import UUIDType  # noqa
from .weekdays import WeekDaysType  # noqa

from .enriched_datetime.enriched_datetime_type import EnrichedDateTimeType  # noqa isort:skip


~~class InstrumentedList(_InstrumentedList):

    def any(self, attr):
        return any(getattr(item, attr) for item in self)

    def all(self, attr):
        return all(getattr(item, attr) for item in self)


def instrumented_list(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
~~        return InstrumentedList([item for item in f(*args, **kwargs)])
    return wrapper



## ... source file continues with no further InstrumentedList examples...

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

[**SQLAthanor / sqlathanor / utilities.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./utilities.py)

```python
# utilities.py

import csv
import linecache
import warnings
import yaml
from collections import OrderedDict

~~from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.exc import InvalidRequestError as SA_InvalidRequestError
from sqlalchemy.exc import UnsupportedCompilationError as SA_UnsupportedCompilationError

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


## ... source file continues with no further InstrumentedList examples...

```

