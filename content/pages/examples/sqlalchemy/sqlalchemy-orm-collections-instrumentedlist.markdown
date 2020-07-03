title: sqlalchemy.orm.collections InstrumentedList code examples
category: page
slug: sqlalchemy-orm-collections-instrumentedlist-examples
sortorder: 500031059
toc: False
sidebartitle: sqlalchemy.orm.collections InstrumentedList
meta: Python example code for the InstrumentedList class from the sqlalchemy.orm.collections module of the SQLAlchemy project.


InstrumentedList is a class within the sqlalchemy.orm.collections module of the SQLAlchemy project.


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

