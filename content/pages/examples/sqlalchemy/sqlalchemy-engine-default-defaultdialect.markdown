title: sqlalchemy.engine.default DefaultDialect Example Code
category: page
slug: sqlalchemy-engine-default-defaultdialect-examples
sortorder: 500031026
toc: False
sidebartitle: sqlalchemy.engine.default DefaultDialect
meta: Example code for understanding how to use the DefaultDialect class from the sqlalchemy.engine.default module of the SQLAlchemy project.


`DefaultDialect` is a class within the `sqlalchemy.engine.default` module of the SQLAlchemy project.



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
    )

    compare._populate_migration_script(autogen_context, migration_script)

    return migration_script


def render_python_code(
    up_or_down_op,
    sqlalchemy_module_prefix="sa.",
    alembic_module_prefix="op.",
    render_as_batch=False,
    imports=(),
    render_item=None,
    migration_context=None,
):
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

    autogen_context = AutogenContext(context)

    upgrade_ops = ops.UpgradeOps([])
    compare._produce_net_changes(autogen_context, upgrade_ops)

    migration_script = ops.MigrationScript(
        rev_id=None,
        upgrade_ops=upgrade_ops,
        downgrade_ops=upgrade_ops.reverse(),
    )

    render._render_python_into_templatevars(
        autogen_context, migration_script, template_args


## ... source file continues with no further DefaultDialect examples...

```

