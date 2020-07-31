title: sqlalchemy.util topological Example Code
category: page
slug: sqlalchemy-util-topological-examples
sortorder: 500031153
toc: False
sidebartitle: sqlalchemy.util topological
meta: Python example code that shows how to use the topological callable from the sqlalchemy.util module of the SQLAlchemy project.


`topological` is a callable within the `sqlalchemy.util` module of the SQLAlchemy project.

<a href="/sqlalchemy-util-ordereddict-examples.html">OrderedDict</a>,
<a href="/sqlalchemy-util-orderedset-examples.html">OrderedSet</a>,
<a href="/sqlalchemy-util-set-creation-order-examples.html">set_creation_order</a>,
and <a href="/sqlalchemy-util-symbol-examples.html">symbol</a>
are several other callables with code examples from the same `sqlalchemy.util` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / operations / batch.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/operations/batch.py)

```python
# batch.py
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy import Index
from sqlalchemy import MetaData
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import schema as sql_schema
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy import types as sqltypes
from sqlalchemy.events import SchemaEventTarget
from sqlalchemy.util import OrderedDict
~~from sqlalchemy.util import topological

from ..util import exc
from ..util.sqla_compat import _columns_for_constraint
from ..util.sqla_compat import _fk_is_self_referential
from ..util.sqla_compat import _is_type_bound
from ..util.sqla_compat import _remove_column_from_collection


class BatchOperationsImpl(object):
    def __init__(
        self,
        operations,
        table_name,
        schema,
        recreate,
        copy_from,
        table_args,
        table_kwargs,
        reflect_args,
        reflect_kwargs,
        naming_convention,
        partial_reordering,
    ):
        self.operations = operations


## ... source file abbreviated to get to topological examples ...


            self.indexes[idx.name] = idx

        for k in self.table.kwargs:
            self.table_kwargs.setdefault(k, self.table.kwargs[k])

    def _adjust_self_columns_for_partial_reordering(self):
        pairs = set()

        col_by_idx = list(self.columns)

        if self.partial_reordering:
            for tuple_ in self.partial_reordering:
                for index, elem in enumerate(tuple_):
                    if index > 0:
                        pairs.add((tuple_[index - 1], elem))
        else:
            for index, elem in enumerate(self.existing_ordering):
                if index > 0:
                    pairs.add((col_by_idx[index - 1], elem))

        pairs.update(self.add_col_ordering)

        pairs = [p for p in pairs if p[0] != p[1]]

        sorted_ = list(
~~            topological.sort(pairs, col_by_idx, deterministic_order=True)
        )
        self.columns = OrderedDict((k, self.columns[k]) for k in sorted_)
        self.column_transfers = OrderedDict(
            (k, self.column_transfers[k]) for k in sorted_
        )

    def _transfer_elements_to_new_table(self):
        assert self.new_table is None, "Can only create new table once"

        m = MetaData()
        schema = self.table.schema

        if self.partial_reordering or self.add_col_ordering:
            self._adjust_self_columns_for_partial_reordering()

        self.new_table = new_table = Table(
            self.temp_table_name,
            m,
            *(list(self.columns.values()) + list(self.table_args)),
            schema=schema,
            **self.table_kwargs
        )

        for const in (


## ... source file continues with no further topological examples...

```

