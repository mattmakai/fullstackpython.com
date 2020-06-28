title: sqlalchemy.dialects.postgresql.psycopg2 PGDialect_psycopg2 code examples
category: page
slug: sqlalchemy-dialects-postgresql-psycopg2-pgdialect-psycopg2-examples
sortorder: 500031014
toc: False
sidebartitle: sqlalchemy.dialects.postgresql.psycopg2 PGDialect_psycopg2
meta: Python example code for the PGDialect_psycopg2 class from the sqlalchemy.dialects.postgresql.psycopg2 module of the SQLAlchemy project.


PGDialect_psycopg2 is a class within the sqlalchemy.dialects.postgresql.psycopg2 module of the SQLAlchemy project.


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

