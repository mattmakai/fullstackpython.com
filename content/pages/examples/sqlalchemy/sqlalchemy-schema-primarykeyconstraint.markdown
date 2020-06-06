title: sqlalchemy.schema PrimaryKeyConstraint code examples
category: page
slug: sqlalchemy-schema-primarykeyconstraint-examples
sortorder: 500031007
toc: False
sidebartitle: sqlalchemy.schema PrimaryKeyConstraint
meta: Python example code for the PrimaryKeyConstraint class from the sqlalchemy.schema module of the SQLAlchemy project.


PrimaryKeyConstraint is a class within the sqlalchemy.schema module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
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
    """ Create a view on a given metadata

    :param name: The name of the view to create.
    :param selectable: An SQLAlchemy selectable e.g. a select() statement.
    :param metadata:
        An SQLAlchemy Metadata instance that stores the features of the
        database being described.
    :param indexes: An optional list of SQLAlchemy Index instances.
    :param aliases:
        An optional dictionary containing with keys as column names and values
        as column aliases.

    Same as for ``create_view`` except that a ``CREATE MATERIALIZED VIEW``


## ... source file continues with no further PrimaryKeyConstraint examples...


```

