title: sqlalchemy.sql sqltypes Example Code
category: page
slug: sqlalchemy-sql-sqltypes-examples
sortorder: 500031116
toc: False
sidebartitle: sqlalchemy.sql sqltypes
meta: Python example code that shows how to use the sqltypes callable from the sqlalchemy.sql module of the SQLAlchemy project.


`sqltypes` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
<a href="/sqlalchemy-sql-extract-examples.html">extract</a>,
<a href="/sqlalchemy-sql-functions-examples.html">functions</a>,
<a href="/sqlalchemy-sql-operators-examples.html">operators</a>,
<a href="/sqlalchemy-sql-schema-examples.html">schema</a>,
<a href="/sqlalchemy-sql-select-examples.html">select</a>,
and <a href="/sqlalchemy-sql-table-examples.html">table</a>
are several other callables with code examples from the same `sqlalchemy.sql` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / ddl / oracle.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/ddl/oracle.py)

```python
# oracle.py
from sqlalchemy.ext.compiler import compiles
~~from sqlalchemy.sql import sqltypes

from .base import AddColumn
from .base import alter_table
from .base import ColumnComment
from .base import ColumnDefault
from .base import ColumnName
from .base import ColumnNullable
from .base import ColumnType
from .base import format_column_name
from .base import format_server_default
from .base import format_table_name
from .base import format_type
from .base import RenameTable
from .impl import DefaultImpl


class OracleImpl(DefaultImpl):
    __dialect__ = "oracle"
    transactional_ddl = False
    batch_separator = "/"
    command_terminator = ""
    type_synonyms = DefaultImpl.type_synonyms + (
        {"VARCHAR", "VARCHAR2"},
        {"BIGINT", "INTEGER", "SMALLINT", "DECIMAL", "NUMERIC", "NUMBER"},


## ... source file abbreviated to get to sqltypes examples ...


def visit_column_name(element, compiler, **kw):
    return "%s RENAME COLUMN %s TO %s" % (
        alter_table(compiler, element.table_name, element.schema),
        format_column_name(compiler, element.column_name),
        format_column_name(compiler, element.newname),
    )


@compiles(ColumnDefault, "oracle")
def visit_column_default(element, compiler, **kw):
    return "%s %s %s" % (
        alter_table(compiler, element.table_name, element.schema),
        alter_column(compiler, element.column_name),
        "DEFAULT %s" % format_server_default(compiler, element.default)
        if element.default is not None
        else "DEFAULT NULL",
    )


@compiles(ColumnComment, "oracle")
def visit_column_comment(element, compiler, **kw):
    ddl = "COMMENT ON COLUMN {table_name}.{column_name} IS {comment}"

    comment = compiler.sql_compiler.render_literal_value(
        (element.comment if element.comment is not None else ""),
~~        sqltypes.String(),
    )

    return ddl.format(
        table_name=element.table_name,
        column_name=element.column_name,
        comment=comment,
    )


@compiles(RenameTable, "oracle")
def visit_rename_table(element, compiler, **kw):
    return "%s RENAME TO %s" % (
        alter_table(compiler, element.table_name, element.schema),
        format_table_name(compiler, element.new_table_name, None),
    )


def alter_column(compiler, name):
    return "MODIFY %s" % format_column_name(compiler, name)


def add_column(compiler, column, **kw):
    return "ADD %s" % compiler.get_column_specification(column, **kw)



## ... source file continues with no further sqltypes examples...

```


## Example 2 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / dialects / asyncpg.py**](https://github.com/python-gino/gino/blob/master/src/gino/dialects/asyncpg.py)

```python
# asyncpg.py
import inspect
import itertools
import time
import warnings

import asyncpg
from sqlalchemy import util, exc, sql
from sqlalchemy.dialects.postgresql import (  # noqa: F401
    ARRAY,
    CreateEnumType,
    DropEnumType,
    JSON,
    JSONB,
    json,
)
from sqlalchemy.dialects.postgresql.base import (
    ENUM,
    PGCompiler,
    PGDialect,
    PGExecutionContext,
)
~~from sqlalchemy.sql import sqltypes

from . import base

try:
    import click
except ImportError:
    click = None
JSON_COLTYPE = 114
JSONB_COLTYPE = 3802


class AsyncpgDBAPI(base.BaseDBAPI):
    Error = asyncpg.PostgresError, asyncpg.InterfaceError


class AsyncpgCompiler(PGCompiler):
    @property
    def bindtemplate(self):
        return self._bindtemplate

    @bindtemplate.setter
    def bindtemplate(self, val):
        self._bindtemplate = val.replace(":", "$")



## ... source file abbreviated to get to sqltypes examples ...


                return [util.text_type(elem) for elem in value]

        return process


class AsyncpgDialect(PGDialect, base.AsyncDialectMixin):
    driver = "asyncpg"
    supports_native_decimal = True
    dbapi_class = AsyncpgDBAPI
    statement_compiler = AsyncpgCompiler
    execution_ctx_cls = AsyncpgExecutionContext
    cursor_cls = DBAPICursor
    init_kwargs = set(
        itertools.chain(
            ("bakery", "prebake"),
            *[
                inspect.getfullargspec(f).kwonlydefaults.keys()
                for f in [asyncpg.create_pool, asyncpg.connect]
            ],
        )
    )
    colspecs = util.update_copy(
        PGDialect.colspecs,
        {
            ENUM: AsyncEnum,
~~            sqltypes.Enum: AsyncEnum,
~~            sqltypes.NullType: GinoNullType,
~~            sqltypes.JSON.JSONPathType: AsyncpgJSONPathType,
        },
    )

    def __init__(self, *args, bakery=None, **kwargs):
        self._pool_kwargs = {}
        self._init_hook = None
        for k in self.init_kwargs:
            if k in kwargs:
                if k == "init":
                    self._init_hook = kwargs.pop(k)
                else:
                    self._pool_kwargs[k] = kwargs.pop(k)
        super().__init__(*args, **kwargs)
        self._init_mixin(bakery)

    async def init_pool(self, url, loop, pool_class=None):
        if pool_class is None:
            pool_class = Pool
        return await pool_class(
            url, loop, bakery=self._bakery, init=self.on_connect(), **self._pool_kwargs
        )

    def transaction(self, raw_conn, args, kwargs):
        return Transaction(raw_conn.transaction(*args, **kwargs))


## ... source file abbreviated to get to sqltypes examples ...


            return self._init_hook

    async def set_isolation_level(self, connection, level):
        level = level.replace("_", " ")
        if level not in self._isolation_lookup:
            raise exc.ArgumentError(
                "Invalid value '%s' for isolation_level. "
                "Valid isolation levels for %s are %s"
                % (level, self.name, ", ".join(self._isolation_lookup))
            )
        await connection.execute(
            "SET SESSION CHARACTERISTICS AS TRANSACTION " "ISOLATION LEVEL %s" % level
        )
        await connection.execute("COMMIT")

    async def get_isolation_level(self, connection):
        val = await connection.fetchval("show transaction isolation level")
        return val.upper()

    async def has_schema(self, connection, schema):
        row = await connection.first(
            sql.text(
                "select nspname from pg_namespace " "where lower(nspname)=:schema"
            ).bindparams(
                sql.bindparam(
~~                    "schema", util.text_type(schema.lower()), type_=sqltypes.Unicode,
                )
            )
        )

        return bool(row)

    async def has_table(self, connection, table_name, schema=None):
        if schema is None:
            row = await connection.first(
                sql.text(
                    "select relname from pg_class c join pg_namespace n on "
                    "n.oid=c.relnamespace where "
                    "pg_catalog.pg_table_is_visible(c.oid) "
                    "and relname=:name"
                ).bindparams(
                    sql.bindparam(
~~                        "name", util.text_type(table_name), type_=sqltypes.Unicode
                    ),
                )
            )
        else:
            row = await connection.first(
                sql.text(
                    "select relname from pg_class c join pg_namespace n on "
                    "n.oid=c.relnamespace where n.nspname=:schema and "
                    "relname=:name"
                ).bindparams(
                    sql.bindparam(
~~                        "name", util.text_type(table_name), type_=sqltypes.Unicode,
                    ),
                    sql.bindparam(
~~                        "schema", util.text_type(schema), type_=sqltypes.Unicode,
                    ),
                )
            )
        return bool(row)

    async def has_sequence(self, connection, sequence_name, schema=None):
        if schema is None:
            row = await connection.first(
                sql.text(
                    "SELECT relname FROM pg_class c join pg_namespace n on "
                    "n.oid=c.relnamespace where relkind='S' and "
                    "n.nspname=current_schema() "
                    "and relname=:name"
                ).bindparams(
                    sql.bindparam(
~~                        "name", util.text_type(sequence_name), type_=sqltypes.Unicode,
                    )
                )
            )
        else:
            row = await connection.first(
                sql.text(
                    "SELECT relname FROM pg_class c join pg_namespace n on "
                    "n.oid=c.relnamespace where relkind='S' and "
                    "n.nspname=:schema and relname=:name"
                ).bindparams(
                    sql.bindparam(
~~                        "name", util.text_type(sequence_name), type_=sqltypes.Unicode,
                    ),
                    sql.bindparam(
~~                        "schema", util.text_type(schema), type_=sqltypes.Unicode,
                    ),
                )
            )

        return bool(row)

    async def has_type(self, connection, type_name, schema=None):
        if schema is not None:
            query = """
            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t, pg_catalog.pg_namespace n
                WHERE t.typnamespace = n.oid
                AND t.typname = :typname
                AND n.nspname = :nspname
                )
            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = :typname
                AND pg_type_is_visible(t.oid)
                )



## ... source file continues with no further sqltypes examples...

```


## Example 3 from sandman2
[sandman2](https://github.com/jeffknupp/sandman2)
([project documentation](https://sandman2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/sandman2/))
is a code library for automatically generating
[RESTful APIs](/application-programming-interfaces.html) from
existing database schemas. This approach is handy for solving
straightforward situations where you want to put an abstraction
layer between one or more applications and your
[relational database](/databases.html) to prevent or reduce
direct database access.

The sandman2 project is provided under the
[Apache License 2.0](https://github.com/jeffknupp/sandman2/blob/master/LICENSE).

[**sandman2 / sandman2 / app.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./app.py)

```python
# app.py

from flask import Flask, current_app, jsonify
~~from sqlalchemy.sql import sqltypes

from sandman2.exception import (
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    NotAcceptableException,
    NotImplementedException,
    ConflictException,
    ServerErrorException,
    ServiceUnavailableException,
    )
from sandman2.service import Service
from sandman2.model import db, Model, AutomapModel
from sandman2.admin import CustomAdminView
from flask_admin import Admin
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

def get_app(
        database_uri,
        exclude_tables=None,
        user_models=None,
        reflect_all=True,


## ... source file abbreviated to get to sqltypes examples ...


def _reflect_all(exclude_tables=None, admin=None, read_only=False, schema=None):
    AutomapModel.prepare(  # pylint:disable=maybe-no-member
        db.engine, reflect=True, schema=schema)
    for cls in AutomapModel.classes:
        if exclude_tables and cls.__table__.name in exclude_tables:
            continue
        if read_only:
            cls.__methods__ = {'GET'}
        register_model(cls, admin)


def register_model(cls, admin=None):
    cls.__url__ = '/{}'.format(cls.__name__.lower())
    service_class = type(
        cls.__name__ + 'Service',
        (Service,),
        {
            '__model__': cls,
        })

    cols = list(cls().__table__.primary_key.columns)

    primary_key_type = 'string'
    if len(cols) == 1:
        col_type = cols[0].type
~~        if isinstance(col_type, sqltypes.String):
            primary_key_type = 'string'
~~        elif isinstance(col_type, sqltypes.Integer):
            primary_key_type = 'int'
~~        elif isinstance(col_type, sqltypes.Numeric):
            primary_key_type = 'float'

    register_service(service_class, primary_key_type)
    if admin is not None:
        admin.add_view(CustomAdminView(cls, db.session))


def _register_user_models(user_models, admin=None, schema=None):
    if any([issubclass(cls, AutomapModel) for cls in user_models]):
        AutomapModel.prepare(  # pylint:disable=maybe-no-member
                               db.engine, reflect=True, schema=schema)

    for user_model in user_models:
        register_model(user_model, admin)



## ... source file continues with no further sqltypes examples...

```

