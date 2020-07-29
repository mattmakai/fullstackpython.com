title: sqlalchemy.dialects.postgresql JSON Example Code
category: page
slug: sqlalchemy-dialects-postgresql-json-examples
sortorder: 500031013
toc: False
sidebartitle: sqlalchemy.dialects.postgresql JSON
meta: Python example code that shows how to use the JSON constant from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


`JSON` is a constant within the `sqlalchemy.dialects.postgresql` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-postgresql-array-examples.html">ARRAY</a>,
<a href="/sqlalchemy-dialects-postgresql-bigint-examples.html">BIGINT</a>,
<a href="/sqlalchemy-dialects-postgresql-bit-examples.html">BIT</a>,
<a href="/sqlalchemy-dialects-postgresql-double-precision-examples.html">DOUBLE_PRECISION</a>,
<a href="/sqlalchemy-dialects-postgresql-excludeconstraint-examples.html">ExcludeConstraint</a>,
<a href="/sqlalchemy-dialects-postgresql-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-dialects-postgresql-tsvector-examples.html">TSVECTOR</a>,
<a href="/sqlalchemy-dialects-postgresql-array-examples.html">array</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">json</a>,
and <a href="/sqlalchemy-dialects-postgresql-pypostgresql-examples.html">pypostgresql</a>
are several other callables with code examples from the same `sqlalchemy.dialects.postgresql` package.

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

[**sqlalchemy-utils / sqlalchemy_utils / types / json.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/json.py)

```python
# json.py
from __future__ import absolute_import

import six
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql.base import ischema_names

from ..exceptions import ImproperlyConfigured

json = None
try:
    import anyjson as json
except ImportError:
    import json as json

try:
~~    from sqlalchemy.dialects.postgresql import JSON
    has_postgres_json = True
except ImportError:
    class PostgresJSONType(sa.types.UserDefinedType):
        def get_col_spec(self):
            return 'json'

    ischema_names['json'] = PostgresJSONType
    has_postgres_json = False


class JSONType(sa.types.TypeDecorator):
    impl = sa.UnicodeText

    def __init__(self, *args, **kwargs):
        if json is None:
            raise ImproperlyConfigured(
                'JSONType needs anyjson package installed.'
            )
        super(JSONType, self).__init__(*args, **kwargs)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            if has_postgres_json:
                return dialect.type_descriptor(JSON())


## ... source file continues with no further JSON examples...

```

