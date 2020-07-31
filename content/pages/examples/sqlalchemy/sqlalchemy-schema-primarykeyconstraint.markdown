title: sqlalchemy.schema PrimaryKeyConstraint Example Code
category: page
slug: sqlalchemy-schema-primarykeyconstraint-examples
sortorder: 500031106
toc: False
sidebartitle: sqlalchemy.schema PrimaryKeyConstraint
meta: Example code for understanding how to use the PrimaryKeyConstraint class from the sqlalchemy.schema module of the SQLAlchemy project.


`PrimaryKeyConstraint` is a class within the `sqlalchemy.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-schema-checkconstraint-examples.html">CheckConstraint</a>,
<a href="/sqlalchemy-schema-column-examples.html">Column</a>,
<a href="/sqlalchemy-schema-createindex-examples.html">CreateIndex</a>,
<a href="/sqlalchemy-schema-createtable-examples.html">CreateTable</a>,
<a href="/sqlalchemy-schema-ddlelement-examples.html">DDLElement</a>,
<a href="/sqlalchemy-schema-foreignkey-examples.html">ForeignKey</a>,
<a href="/sqlalchemy-schema-foreignkeyconstraint-examples.html">ForeignKeyConstraint</a>,
<a href="/sqlalchemy-schema-index-examples.html">Index</a>,
and <a href="/sqlalchemy-schema-table-examples.html">Table</a>
are several other callables with code examples from the same `sqlalchemy.schema` package.

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

[**sqlalchemy-utils / sqlalchemy_utils / view.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./view.py)

```python
# view.py
import sqlalchemy as sa
from sqlalchemy.ext import compiler
~~from sqlalchemy.schema import DDLElement, PrimaryKeyConstraint


class CreateView(DDLElement):
    def __init__(self, name, selectable, materialized=False):
        self.name = name
        self.selectable = selectable
        self.materialized = materialized


@compiler.compiles(CreateView)
def compile_create_materialized_view(element, compiler, **kw):
    return 'CREATE {}VIEW {} AS {}'.format(
        'MATERIALIZED ' if element.materialized else '',
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


class DropView(DDLElement):
    def __init__(self, name, materialized=False, cascade=True):
        self.name = name
        self.materialized = materialized
        self.cascade = cascade



## ... source file abbreviated to get to PrimaryKeyConstraint examples ...


    name,
    selectable,
    indexes=None,
    metadata=None,
    aliases=None
):
    if indexes is None:
        indexes = []
    if metadata is None:
        metadata = sa.MetaData()
    if aliases is None:
        aliases = {}
    args = [
        sa.Column(
            c.name,
            c.type,
            key=aliases.get(c.name, c.name),
            primary_key=c.primary_key
        )
        for c in selectable.c
    ] + indexes
    table = sa.Table(name, metadata, *args)

    if not any([c.primary_key for c in selectable.c]):
        table.append_constraint(
~~            PrimaryKeyConstraint(*[c.name for c in selectable.c])
        )
    return table


def create_materialized_view(
    name,
    selectable,
    metadata,
    indexes=None,
    aliases=None
):
    table = create_table_from_selectable(
        name=name,
        selectable=selectable,
        indexes=indexes,
        metadata=None,
        aliases=aliases
    )

    sa.event.listen(
        metadata,
        'after_create',
        CreateView(name, selectable, materialized=True)
    )


## ... source file continues with no further PrimaryKeyConstraint examples...

```

