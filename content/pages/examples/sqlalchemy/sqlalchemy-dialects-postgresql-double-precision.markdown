title: sqlalchemy.dialects.postgresql DOUBLE_PRECISION Example Code
category: page
slug: sqlalchemy-dialects-postgresql-double-precision-examples
sortorder: 500031010
toc: False
sidebartitle: sqlalchemy.dialects.postgresql DOUBLE_PRECISION
meta: Python example code that shows how to use the DOUBLE_PRECISION constant from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


`DOUBLE_PRECISION` is a constant within the `sqlalchemy.dialects.postgresql` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-postgresql-array-examples.html">ARRAY</a>,
<a href="/sqlalchemy-dialects-postgresql-bigint-examples.html">BIGINT</a>,
<a href="/sqlalchemy-dialects-postgresql-bit-examples.html">BIT</a>,
<a href="/sqlalchemy-dialects-postgresql-excludeconstraint-examples.html">ExcludeConstraint</a>,
<a href="/sqlalchemy-dialects-postgresql-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">JSON</a>,
<a href="/sqlalchemy-dialects-postgresql-tsvector-examples.html">TSVECTOR</a>,
<a href="/sqlalchemy-dialects-postgresql-array-examples.html">array</a>,
<a href="/sqlalchemy-dialects-postgresql-json-examples.html">json</a>,
and <a href="/sqlalchemy-dialects-postgresql-pypostgresql-examples.html">pypostgresql</a>
are several other callables with code examples from the same `sqlalchemy.dialects.postgresql` package.

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
from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from sqlalchemy.engine import reflection
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import (
    BinaryExpression, BooleanClauseList, Delete
)
from sqlalchemy.types import (
    VARCHAR, NullType, SMALLINT, INTEGER, BIGINT,
    DECIMAL, REAL, BOOLEAN, CHAR, DATE, TIMESTAMP)
~~from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

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
else:
    from alembic.ddl import postgresql

    from alembic.ddl.base import RenameTable
    compiles(RenameTable, 'redshift')(postgresql.visit_rename_table)

    if Version(alembic.__version__) >= Version('1.0.6'):
        from alembic.ddl.base import ColumnComment
        compiles(ColumnComment, 'redshift')(postgresql.visit_column_comment)


## ... source file continues with no further DOUBLE_PRECISION examples...

```


## Example 2 from GeoAlchemy2
[GeoAlchemy2](https://github.com/geoalchemy/geoalchemy2)
([project documentation](https://geoalchemy-2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/GeoAlchemy2/))
extends [SQLAlchemy](/sqlalchemy.html) with new data types for working
with geospatial databases, particularly [PostGIS](http://postgis.net/),
which is a spatial database extender for [PostgreSQL](/postgresql.html).
The project is provided as open source under the
[MIT license](https://github.com/geoalchemy/geoalchemy2/blob/master/COPYING.rst).

[**GeoAlchemy2 / geoalchemy2 / comparator.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./comparator.py)

```python
# comparator.py

from sqlalchemy import types as sqltypes
from sqlalchemy.types import UserDefinedType
~~from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.sql import operators
try:
    from sqlalchemy.sql.functions import _FunctionGenerator
except ImportError:  # SQLA < 0.9  # pragma: no cover
    from sqlalchemy.sql.expression import _FunctionGenerator


INTERSECTS = operators.custom_op('&&')
OVERLAPS_OR_TO_LEFT = operators.custom_op('&<')
OVERLAPS_OR_TO_RIGHT = operators.custom_op('&>')
OVERLAPS_OR_BELOW = operators.custom_op('&<|')
TO_LEFT = operators.custom_op('<<')
BELOW = operators.custom_op('<<|')
TO_RIGHT = operators.custom_op('>>')
CONTAINED = operators.custom_op('@')
OVERLAPS_OR_ABOVE = operators.custom_op('|&>')
ABOVE = operators.custom_op('|>>')
CONTAINS = operators.custom_op('-')
SAME = operators.custom_op('-=')
DISTANCE_CENTROID = operators.custom_op('<->')
DISTANCE_BOX = operators.custom_op('<#>')


class BaseComparator(UserDefinedType.Comparator):


## ... source file continues with no further DOUBLE_PRECISION examples...

```

