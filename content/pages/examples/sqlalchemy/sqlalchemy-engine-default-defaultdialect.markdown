title: sqlalchemy.engine.default DefaultDialect code examples
category: page
slug: sqlalchemy-engine-default-defaultdialect-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.engine.default DefaultDialect
meta: Python example code for the DefaultDialect class from the sqlalchemy.engine.default module of the SQLAlchemy project.


DefaultDialect is a class within the sqlalchemy.engine.default module of the SQLAlchemy project.


## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / autogenerate / api.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/autogenerate/api.py)

```python
# api.py
"""Provide the 'autogenerate' feature which can produce migration operations
automatically."""

import contextlib

from sqlalchemy import inspect

from . import compare
from . import render
from .. import util
from ..operations import ops


def compare_metadata(context, metadata):
    """Compare a database schema to that given in a
    :class:`-sqlalchemy.schema.MetaData` instance.

    The database connection is presented in the context
    of a :class:`.MigrationContext` object, which
    provides database connectivity as well as optional
    comparison functions to use for datatypes and
    server defaults - see the "autogenerate" arguments
    at :meth:`.EnvironmentContext.configure`
    for details on these.

    The return format is a list of "diff" directives,
    each representing individual differences::

        from alembic.migration import MigrationContext
        from alembic.autogenerate import compare_metadata


## ... source file abbreviated to get to DefaultDialect examples ...


    imports=(),
    render_item=None,
    migration_context=None,
):
    """Render Python code given an :class:`.UpgradeOps` or
    :class:`.DowngradeOps` object.

    This is a convenience function that can be used to test the
    autogenerate output of a user-defined :class:`.MigrationScript` structure.

    """
    opts = {
        "sqlalchemy_module_prefix": sqlalchemy_module_prefix,
        "alembic_module_prefix": alembic_module_prefix,
        "render_item": render_item,
        "render_as_batch": render_as_batch,
    }

    if migration_context is None:
        from ..runtime.migration import MigrationContext
~~        from sqlalchemy.engine.default import DefaultDialect

        migration_context = MigrationContext.configure(
~~            dialect=DefaultDialect()
        )

    autogen_context = AutogenContext(migration_context, opts=opts)
    autogen_context.imports = set(imports)
    return render._indent(
        render._render_cmd_body(up_or_down_op, autogen_context)
    )


def _render_migration_diffs(context, template_args):
    """legacy, used by test_autogen_composition at the moment"""

    autogen_context = AutogenContext(context)

    upgrade_ops = ops.UpgradeOps([])
    compare._produce_net_changes(autogen_context, upgrade_ops)

    migration_script = ops.MigrationScript(
        rev_id=None,
        upgrade_ops=upgrade_ops,
        downgrade_ops=upgrade_ops.reverse(),
    )

    render._render_python_into_templatevars(


## ... source file continues with no further DefaultDialect examples...


```

