title: sqlalchemy.dialects.postgresql.base PGCompiler Example Code
category: page
slug: sqlalchemy-dialects-postgresql-base-pgcompiler-examples
sortorder: 500031016
toc: False
sidebartitle: sqlalchemy.dialects.postgresql.base PGCompiler
meta: Example code for understanding how to use the PGCompiler class from the sqlalchemy.dialects.postgresql.base module of the SQLAlchemy project.


`PGCompiler` is a class within the `sqlalchemy.dialects.postgresql.base` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-postgresql-base-pgidentifierpreparer-examples.html">PGIdentifierPreparer</a>
and
<a href="/sqlalchemy-dialects-postgresql-base-pgtypecompiler-examples.html">PGTypeCompiler</a>
are a couple of other callables within the `sqlalchemy.dialects.postgresql.base` package that also have code examples.

## Example 1 from sqlalchemy-clickhouse
[sqlalchemy-clickhouse](https://github.com/cloudflare/sqlalchemy-clickhouse)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
for communicating with the open source [ClickHouse](https://clickhouse.tech/)
database management system. ClickHouse is column-oriented and therefore
better for some use cases and worse for others compared to a traditional
[relational database](/databases.html).

The code for this project is open sourced under the
[MIT license](https://github.com/cloudflare/sqlalchemy-clickhouse/blob/master/LICENSE.txt)
while ClickHouse is provided as open source under the
[Apache License 2.0](https://github.com/ClickHouse/ClickHouse/blob/master/LICENSE).

[**sqlalchemy-clickhouse / base.py**](https://github.com/cloudflare/sqlalchemy-clickhouse/blob/master/././base.py)

```python
# base.py

import re

import sqlalchemy.types as sqltypes
from sqlalchemy import exc as sa_exc
from sqlalchemy import util as sa_util
from sqlalchemy.engine import default, reflection
from sqlalchemy.sql import compiler, expression
from sqlalchemy.sql.elements import quoted_name
~~from sqlalchemy.dialects.postgresql.base import PGCompiler, PGIdentifierPreparer
from sqlalchemy.types import (
    CHAR, DATE, DATETIME, INTEGER, SMALLINT, BIGINT, DECIMAL, TIME,
    TIMESTAMP, VARCHAR, BINARY, BOOLEAN, FLOAT, REAL)

VERSION = (0, 1, 0, None)

colspecs = {}

class ARRAY(sqltypes.TypeEngine):
    __visit_name__ = 'ARRAY'

ischema_names = {
    'Int64': INTEGER,
    'Int32': INTEGER,
    'Int16': INTEGER,
    'Int8': INTEGER,
    'UInt64': INTEGER,
    'UInt32': INTEGER,
    'UInt16': INTEGER,
    'UInt8': INTEGER,
    'Date': DATE,
    'DateTime': DATETIME,
    'Float64': FLOAT,
    'Float32': FLOAT,
    'String': VARCHAR,
    'FixedString': VARCHAR,
    'Enum': VARCHAR,
    'Enum8': VARCHAR,
    'Enum16': VARCHAR,
    'Array': ARRAY,
}

class ClickHouseIdentifierPreparer(PGIdentifierPreparer):
    def quote_identifier(self, value):
        return self._escape_identifier(value)
    def quote(self, ident, force=None):
        if self._requires_quotes(ident):
            return '"{}"'.format(ident)
        return ident

~~class ClickHouseCompiler(PGCompiler):
    def visit_count_func(self, fn, **kw):
        return 'count{0}'.format(self.process(fn.clause_expr, **kw))

    def visit_random_func(self, fn, **kw):
        return 'rand()'

    def visit_now_func(self, fn, **kw):
        return 'now()'

    def visit_current_date_func(self, fn, **kw):
        return 'today()'

    def visit_true(self, element, **kw):
        return '1'

    def visit_false(self, element, **kw):
        return '0'

    def visit_cast(self, cast, **kwargs):
        if self.dialect.supports_cast:
            return super(ClickHouseCompiler, self).visit_cast(cast, **kwargs)
        else:
            return self.process(cast.clause, **kwargs)



## ... source file continues with no further PGCompiler examples...

```

