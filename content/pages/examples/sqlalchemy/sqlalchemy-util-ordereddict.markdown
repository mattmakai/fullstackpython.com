title: sqlalchemy.util OrderedDict code examples
category: page
slug: sqlalchemy-util-ordereddict-examples
sortorder: 500031107
toc: False
sidebartitle: sqlalchemy.util OrderedDict
meta: Python example code for the OrderedDict class from the sqlalchemy.util module of the SQLAlchemy project.


OrderedDict is a class within the sqlalchemy.util module of the SQLAlchemy project.


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
~~from sqlalchemy.util import OrderedDict
from sqlalchemy.util import topological

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


## ... source file abbreviated to get to OrderedDict examples ...



    def drop_table(self, table):
        raise NotImplementedError("Can't drop table in batch mode")


class ApplyBatchImpl(object):
    def __init__(
        self,
        impl,
        table,
        table_args,
        table_kwargs,
        reflected,
        partial_reordering=(),
    ):
        self.impl = impl
        self.table = table  # this is a Table object
        self.table_args = table_args
        self.table_kwargs = table_kwargs
        self.temp_table_name = self._calc_temp_name(table.name)
        self.new_table = None

        self.partial_reordering = partial_reordering  # tuple of tuples
        self.add_col_ordering = ()  # tuple of tuples

~~        self.column_transfers = OrderedDict(
            (c.name, {"expr": c}) for c in self.table.c
        )
        self.existing_ordering = list(self.column_transfers)

        self.reflected = reflected
        self._grab_table_elements()

    @classmethod
    def _calc_temp_name(cls, tablename):
        return ("_alembic_tmp_%s" % tablename)[0:50]

    def _grab_table_elements(self):
        schema = self.table.schema
~~        self.columns = OrderedDict()
        for c in self.table.c:
            c_copy = c.copy(schema=schema)
            c_copy.unique = c_copy.index = False
            if isinstance(c.type, SchemaEventTarget):
                assert c_copy.type is not c.type
            self.columns[c.name] = c_copy
        self.named_constraints = {}
        self.unnamed_constraints = []
        self.indexes = {}
        self.new_indexes = {}
        for const in self.table.constraints:
            if _is_type_bound(const):
                continue
            elif self.reflected and isinstance(const, CheckConstraint):
                pass
            elif const.name:
                self.named_constraints[const.name] = const
            else:
                self.unnamed_constraints.append(const)

        for idx in self.table.indexes:
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
            topological.sort(pairs, col_by_idx, deterministic_order=True)
        )
~~        self.columns = OrderedDict((k, self.columns[k]) for k in sorted_)
~~        self.column_transfers = OrderedDict(
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
            list(self.named_constraints.values()) + self.unnamed_constraints
        ):



## ... source file continues with no further OrderedDict examples...

```

