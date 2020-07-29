title: sqlalchemy.dialects.postgresql.psycopg2 PGDialect_psycopg2 Example Code
category: page
slug: sqlalchemy-dialects-postgresql-psycopg2-pgdialect-psycopg2-examples
sortorder: 500031019
toc: False
sidebartitle: sqlalchemy.dialects.postgresql.psycopg2 PGDialect_psycopg2
meta: Example code for understanding how to use the PGDialect_psycopg2 class from the sqlalchemy.dialects.postgresql.psycopg2 module of the SQLAlchemy project.


`PGDialect_psycopg2` is a class within the `sqlalchemy.dialects.postgresql.psycopg2` module of the SQLAlchemy project.



## Example 1 from Amazon Redshift SQLAlchemy Dialect
[Amazon Redshift SQLAlchemy Dialect](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
that can communicate with the [AWS Redshift](https://aws.amazon.com/redshift/)
data store. The SQL is essentially [PostgreSQL](/postgresql.html)
and requires [psycopg2](https://www.psycopg.org/) to properly
operate. This project and its code are open sourced under the
[MIT license](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/LICENSE).

[**Amazon Redshift SQLAlchemy Dialect / sqlalchemy_redshift / dialect.py**](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/sqlalchemy_redshift/./dialect.py)

```python
# dialect.py
import re
from collections import defaultdict, namedtuple

from packaging.version import Version
import pkg_resources
import sqlalchemy as sa
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql.base import (
    PGCompiler, PGDDLCompiler, PGIdentifierPreparer, PGTypeCompiler
)
~~from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from sqlalchemy.engine import reflection
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import (
    BinaryExpression, BooleanClauseList, Delete
)
from sqlalchemy.types import (
    VARCHAR, NullType, SMALLINT, INTEGER, BIGINT,
    DECIMAL, REAL, BOOLEAN, CHAR, DATE, TIMESTAMP)
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

from .commands import (
    CopyCommand, UnloadFromSelect, Format, Compression, Encoding,
    CreateLibraryCommand, AlterTableAppendCommand, RefreshMaterializedView
)
from .ddl import (
    CreateMaterializedView, DropMaterializedView, get_table_attributes
)

sa_version = Version(sa.__version__)

try:
    import alembic
except ImportError:
    pass


## ... source file continues with no further PGDialect_psycopg2 examples...

```


## Example 2 from databases
[databases](https://github.com/encode/databases)
([project homepage](https://www.encode.io/databases/)
and
[PyPI page](https://pypi.org/project/databases/) provides
[asyncio](https://docs.python.org/3/library/asyncio.html) support
with an [SQLALchemy](/sqlalchemy.html) Core interface for common
[relational databases](/databases.html) such as [MySQL](/mysql.html),
[PostgreSQL](/postgresql.html) and [SQLite](/sqlite.html). This is
handy for integrating with asynchronous I/O
[web frameworks](/web-frameworks.html) like [Sanic](/sanic.html).
The project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/encode/databases/blob/master/LICENSE.md).

[**databases / databases / backends / aiopg.py**](https://github.com/encode/databases/blob/master/databases/backends/aiopg.py)

```python
# aiopg.py
import getpass
import json
import logging
import typing
import uuid

import aiopg
from aiopg.sa.engine import APGCompiler_psycopg2
~~from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from sqlalchemy.engine.interfaces import Dialect, ExecutionContext
from sqlalchemy.engine.result import ResultMetaData, RowProxy
from sqlalchemy.sql import ClauseElement
from sqlalchemy.types import TypeEngine

from databases.core import DatabaseURL
from databases.interfaces import ConnectionBackend, DatabaseBackend, TransactionBackend

logger = logging.getLogger("databases")


class AiopgBackend(DatabaseBackend):
    def __init__(
        self, database_url: typing.Union[DatabaseURL, str], **options: typing.Any
    ) -> None:
        self._database_url = DatabaseURL(database_url)
        self._options = options
        self._dialect = self._get_dialect()
        self._pool = None

    def _get_dialect(self) -> Dialect:
~~        dialect = PGDialect_psycopg2(
            json_serializer=json.dumps, json_deserializer=lambda x: x
        )
        dialect.statement_compiler = APGCompiler_psycopg2
        dialect.implicit_returning = True
        dialect.supports_native_enum = True
        dialect.supports_smallserial = True  # 9.2+
        dialect._backslash_escapes = False
        dialect.supports_sane_multi_rowcount = True  # psycopg 2.0.9+
        dialect._has_native_hstore = True
        dialect.supports_native_decimal = True

        return dialect

    def _get_connection_kwargs(self) -> dict:
        url_options = self._database_url.options

        kwargs = {}
        min_size = url_options.get("min_size")
        max_size = url_options.get("max_size")
        ssl = url_options.get("ssl")

        if min_size is not None:
            kwargs["minsize"] = int(min_size)
        if max_size is not None:


## ... source file continues with no further PGDialect_psycopg2 examples...

```


## Example 3 from sqlalchemy-utils
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

[**sqlalchemy-utils / sqlalchemy_utils / types / pg_composite.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/pg_composite.py)

```python
# pg_composite.py
from collections import namedtuple

import six
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
~~from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import _CreateDropBase
from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy.types import (
    SchemaType,
    to_instance,
    TypeDecorator,
    UserDefinedType
)

from .. import ImproperlyConfigured

psycopg2 = None
CompositeCaster = None
adapt = None
AsIs = None
register_adapter = None
try:
    import psycopg2
    from psycopg2.extras import CompositeCaster
    from psycopg2.extensions import adapt, AsIs, register_adapter
except ImportError:
    pass



## ... source file abbreviated to get to PGDialect_psycopg2 examples ...


            bind.execute(CreateCompositeType(self))

    def drop(self, bind=None, checkfirst=True):
        if (
            checkfirst and
            bind.dialect.has_type(bind, self.name, schema=self.schema)
        ):
            bind.execute(DropCompositeType(self))


def register_psycopg2_composite(dbapi_connection, composite):
    psycopg2.extras.register_composite(
        composite.name,
        dbapi_connection,
        globally=True,
        factory=composite.caster
    )

    def adapt_composite(value):
        adapted = [
            adapt(
                getattr(value, column.name)
                if not isinstance(column.type, TypeDecorator)
                else column.type.process_bind_param(
                    getattr(value, column.name),
~~                    PGDialect_psycopg2()
                )
            )
            for column in
            composite.columns
        ]
        for value in adapted:
            if hasattr(value, 'prepare'):
                value.prepare(dbapi_connection)
        values = [
            value.getquoted().decode(dbapi_connection.encoding)
            if six.PY3
            else value.getquoted()
            for value in adapted
        ]
        return AsIs("(%s)::%s" % (', '.join(values), composite.name))

    register_adapter(composite.type_cls, adapt_composite)


def before_create(target, connection, **kw):
    for name, composite in registered_composites.items():
        composite.create(connection, checkfirst=True)
        register_psycopg2_composite(
            connection.connection.connection,


## ... source file continues with no further PGDialect_psycopg2 examples...

```

