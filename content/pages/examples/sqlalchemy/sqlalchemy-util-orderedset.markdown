title: sqlalchemy.util OrderedSet Example Code
category: page
slug: sqlalchemy-util-orderedset-examples
sortorder: 500031150
toc: False
sidebartitle: sqlalchemy.util OrderedSet
meta: Example code for understanding how to use the OrderedSet class from the sqlalchemy.util module of the SQLAlchemy project.


`OrderedSet` is a class within the `sqlalchemy.util` module of the SQLAlchemy project.

<a href="/sqlalchemy-util-ordereddict-examples.html">OrderedDict</a>,
<a href="/sqlalchemy-util-set-creation-order-examples.html">set_creation_order</a>,
<a href="/sqlalchemy-util-symbol-examples.html">symbol</a>,
and <a href="/sqlalchemy-util-topological-examples.html">topological</a>
are several other callables with code examples from the same `sqlalchemy.util` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / autogenerate / compare.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/autogenerate/compare.py)

```python
# compare.py
import contextlib
import logging
import re

from sqlalchemy import event
from sqlalchemy import inspect
from sqlalchemy import schema as sa_schema
from sqlalchemy import types as sqltypes
~~from sqlalchemy.util import OrderedSet

from alembic.ddl.base import _fk_spec
from .render import _user_defined_render
from .. import util
from ..operations import ops
from ..util import compat
from ..util import sqla_compat

log = logging.getLogger(__name__)


def _populate_migration_script(autogen_context, migration_script):
    upgrade_ops = migration_script.upgrade_ops_list[-1]
    downgrade_ops = migration_script.downgrade_ops_list[-1]

    _produce_net_changes(autogen_context, upgrade_ops)
    upgrade_ops.reverse_into(downgrade_ops)


comparators = util.Dispatcher(uselist=True)


def _produce_net_changes(autogen_context, upgrade_ops):



## ... source file abbreviated to get to OrderedSet examples ...



    comparators.dispatch("schema", autogen_context.dialect.name)(
        autogen_context, upgrade_ops, schemas
    )


@comparators.dispatch_for("schema")
def _autogen_for_tables(autogen_context, upgrade_ops, schemas):
    inspector = autogen_context.inspector

    conn_table_names = set()

    version_table_schema = (
        autogen_context.migration_context.version_table_schema
    )
    version_table = autogen_context.migration_context.version_table

    for s in schemas:
        tables = set(inspector.get_table_names(schema=s))
        if s == version_table_schema:
            tables = tables.difference(
                [autogen_context.migration_context.version_table]
            )
        conn_table_names.update(zip([s] * len(tables), tables))

~~    metadata_table_names = OrderedSet(
        [(table.schema, table.name) for table in autogen_context.sorted_tables]
    ).difference([(version_table_schema, version_table)])

    _compare_tables(
        conn_table_names,
        metadata_table_names,
        inspector,
        upgrade_ops,
        autogen_context,
    )


def _compare_tables(
    conn_table_names,
    metadata_table_names,
    inspector,
    upgrade_ops,
    autogen_context,
):

    default_schema = inspector.bind.dialect.default_schema_name

~~    metadata_table_names_no_dflt_schema = OrderedSet(
        [
            (schema if schema != default_schema else None, tname)
            for schema, tname in metadata_table_names
        ]
    )

    tname_to_table = dict(
        (
            no_dflt_schema,
            autogen_context.table_key_to_table[
                sa_schema._get_table_key(tname, schema)
            ],
        )
        for no_dflt_schema, (schema, tname) in zip(
            metadata_table_names_no_dflt_schema, metadata_table_names
        )
    )
    metadata_table_names = metadata_table_names_no_dflt_schema

    for s, tname in metadata_table_names.difference(conn_table_names):
        name = "%s.%s" % (s, tname) if s else tname
        metadata_table = tname_to_table[(s, tname)]
        if autogen_context.run_filters(
            metadata_table, tname, "table", False, None


## ... source file abbreviated to get to OrderedSet examples ...


        onupdate=options.get("onupdate"),
        ondelete=options.get("ondelete"),
        deferrable=options.get("deferrable"),
        initially=options.get("initially"),
        name=params["name"],
    )
    conn_table.append_constraint(const)
    return const


@contextlib.contextmanager
def _compare_columns(
    schema,
    tname,
    conn_table,
    metadata_table,
    modify_table_ops,
    autogen_context,
    inspector,
):
    name = "%s.%s" % (schema, tname) if schema else tname
    metadata_cols_by_name = dict(
        (c.name, c) for c in metadata_table.c if not c.system
    )
    conn_col_names = dict((c.name, c) for c in conn_table.c)
~~    metadata_col_names = OrderedSet(sorted(metadata_cols_by_name))

    for cname in metadata_col_names.difference(conn_col_names):
        if autogen_context.run_filters(
            metadata_cols_by_name[cname], cname, "column", False, None
        ):
            modify_table_ops.ops.append(
                ops.AddColumnOp.from_column_and_tablename(
                    schema, tname, metadata_cols_by_name[cname]
                )
            )
            log.info("Detected added column '%s.%s'", name, cname)

    for colname in metadata_col_names.intersection(conn_col_names):
        metadata_col = metadata_cols_by_name[colname]
        conn_col = conn_table.c[colname]
        if not autogen_context.run_filters(
            metadata_col, colname, "column", False, conn_col
        ):
            continue
        alter_column_op = ops.AlterColumnOp(tname, colname, schema=schema)

        comparators.dispatch("column")(
            autogen_context,
            alter_column_op,


## ... source file continues with no further OrderedSet examples...

```

