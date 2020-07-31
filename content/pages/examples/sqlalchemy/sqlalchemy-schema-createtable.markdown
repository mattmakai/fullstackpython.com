title: sqlalchemy.schema CreateTable Example Code
category: page
slug: sqlalchemy-schema-createtable-examples
sortorder: 500031101
toc: False
sidebartitle: sqlalchemy.schema CreateTable
meta: Example code for understanding how to use the CreateTable class from the sqlalchemy.schema module of the SQLAlchemy project.


`CreateTable` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-ddlelement-examples.html">DDLElement</a>,
<a href="/sqlalchemy-schema-foreignkey-examples.html">ForeignKey</a>,
<a href="/sqlalchemy-schema-foreignkeyconstraint-examples.html">ForeignKeyConstraint</a>,
<a href="/sqlalchemy-schema-index-examples.html">Index</a>,
<a href="/sqlalchemy-schema-primarykeyconstraint-examples.html">PrimaryKeyConstraint</a>,
and <a href="/sqlalchemy-schema-table-examples.html">Table</a>
are several other callables with code examples from the same `sqlalchemy.schema` package.

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


## ... source file abbreviated to get to CreateTable examples ...


  \s* \) \s*                # Arbitrary whitespace and literal ')'
    Redshift defines a TIMTESTAMPTZ column type as an alias
    of TIMESTAMP WITH TIME ZONE.
    https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html

    Adding an explicit type to the RedshiftDialect allows us follow the
    SqlAlchemy conventions for "vendor-specific types."

    https://docs.sqlalchemy.org/en/13/core/type_basics.html#vendor-specific-types
    Structured tuple of table/view name and schema name.
        Construct a new RelationKey with an explicit schema name.
        Return *key* with one level of double quotes removed.

        Redshift stores some identifiers without quotes in internal tables,
        even though the name must be quoted elsewhere.
        In particular, this happens for tables named as a keyword.
    Handles Redshift-specific ``CREATE TABLE`` syntax.

    Users can specify the `diststyle`, `distkey`, `sortkey` and `encode`
    properties per table and per column.

    Table level properties can be set using the dialect specific syntax. For
    example, to specify a distribution key and style you apply the following:

    >>> import sqlalchemy as sa
~~    >>> from sqlalchemy.schema import CreateTable
    >>> engine = sa.create_engine('redshift+psycopg2://example')
    >>> metadata = sa.MetaData()
    >>> user = sa.Table(
    ...     'user',
    ...     metadata,
    ...     sa.Column('id', sa.Integer, primary_key=True),
    ...     sa.Column('name', sa.String),
    ...     redshift_diststyle='KEY',
    ...     redshift_distkey='id',
    ...     redshift_interleaved_sortkey=['id', 'name'],
    ... )
    >>> print(CreateTable(user).compile(engine))
    <BLANKLINE>
    CREATE TABLE "user" (
        id INTEGER NOT NULL,
        name VARCHAR,
        PRIMARY KEY (id)
    ) DISTSTYLE KEY DISTKEY (id) INTERLEAVED SORTKEY (id, name)
    <BLANKLINE>
    <BLANKLINE>

    A single sort key can be applied without a wrapping list:

    >>> customer = sa.Table(


## ... source file continues with no further CreateTable examples...

```

