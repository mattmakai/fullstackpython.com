title: sqlalchemy.ext.mutable Mutable code examples
category: page
slug: sqlalchemy-ext-mutable-mutable-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.ext.mutable Mutable
meta: Python example code for the Mutable class from the sqlalchemy.ext.mutable module of the SQLAlchemy project.


Mutable is a class within the sqlalchemy.ext.mutable module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / types / password.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/password.py)

```python
# password.py
import weakref

import six
from sqlalchemy import types
from sqlalchemy.dialects import oracle, postgresql, sqlite
~~from sqlalchemy.ext.mutable import Mutable

from ..exceptions import ImproperlyConfigured
from .scalar_coercible import ScalarCoercible

passlib = None
try:
    import passlib
    from passlib.context import LazyCryptContext
except ImportError:
    pass


~~class Password(Mutable, object):

    @classmethod
    def coerce(cls, key, value):
        if isinstance(value, Password):
            return value

        if isinstance(value, (six.string_types, six.binary_type)):
            return cls(value, secret=True)

        super(Password, cls).coerce(key, value)

    def __init__(self, value, context=None, secret=False):
        # Store the hash (if it is one).
        self.hash = value if not secret else None

        # Store the secret if we have one.
        self.secret = value if secret else None

        # The hash should be bytes.
        if isinstance(self.hash, six.text_type):
            self.hash = self.hash.encode('utf8')

        # Save weakref of the password context (if we have one)
        self.context = weakref.proxy(context) if context is not None else None


## ... source file continues with no further Mutable examples...


```

