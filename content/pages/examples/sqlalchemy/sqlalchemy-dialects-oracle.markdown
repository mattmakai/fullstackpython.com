title: sqlalchemy.dialects oracle Example Code
category: page
slug: sqlalchemy-dialects-oracle-examples
sortorder: 500031003
toc: False
sidebartitle: sqlalchemy.dialects oracle
meta: Python example code that shows how to use the oracle callable from the sqlalchemy.dialects module of the SQLAlchemy project.


`oracle` is a callable within the `sqlalchemy.dialects` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-mssql-examples.html">mssql</a>,
<a href="/sqlalchemy-dialects-mysql-examples.html">mysql</a>,
<a href="/sqlalchemy-dialects-postgresql-examples.html">postgresql</a>,
and <a href="/sqlalchemy-dialects-sqlite-examples.html">sqlite</a>
are several other callables with code examples from the same `sqlalchemy.dialects` package.

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

[**sqlalchemy-utils / sqlalchemy_utils / types / password.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/password.py)

```python
# password.py
import weakref

import six
from sqlalchemy import types
~~from sqlalchemy.dialects import oracle, postgresql, sqlite
from sqlalchemy.ext.mutable import Mutable

from ..exceptions import ImproperlyConfigured
from .scalar_coercible import ScalarCoercible

passlib = None
try:
    import passlib
    from passlib.context import LazyCryptContext
except ImportError:
    pass


class Password(Mutable, object):

    @classmethod
    def coerce(cls, key, value):
        if isinstance(value, Password):
            return value

        if isinstance(value, (six.string_types, six.binary_type)):
            return cls(value, secret=True)

        super(Password, cls).coerce(key, value)


## ... source file abbreviated to get to oracle examples ...


        if self._max_length is None:
            self._max_length = self.calculate_max_length()

        return self._max_length

    def calculate_max_length(self):
        max_lengths = [1024]
        for name in self.context.schemes():
            scheme = getattr(__import__('passlib.hash').hash, name)
            length = 4 + len(scheme.name)
            length += len(str(getattr(scheme, 'max_rounds', '')))
            length += (getattr(scheme, 'max_salt_size', 0) or 0)
            length += getattr(
                scheme,
                'encoded_checksum_size',
                scheme.checksum_size
            )
            max_lengths.append(length)

        return max(max_lengths)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            impl = postgresql.BYTEA(self.length)
        elif dialect.name == 'oracle':
~~            impl = oracle.RAW(self.length)
        elif dialect.name == 'sqlite':
            impl = sqlite.BLOB(self.length)
        else:
            impl = types.VARBINARY(self.length)
        return dialect.type_descriptor(impl)

    def process_bind_param(self, value, dialect):
        if isinstance(value, Password):
            if value.secret is not None:
                return self._hash(value.secret).encode('utf8')

            return value.hash

        if isinstance(value, six.string_types):
            return self._hash(value).encode('utf8')

    def process_result_value(self, value, dialect):
        if value is not None:
            return Password(value, self.context)

    def _hash(self, value):
        return getattr(self.context, self.hashing_method)(value)

    def _coerce(self, value):


## ... source file continues with no further oracle examples...

```

