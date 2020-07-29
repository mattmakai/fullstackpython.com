title: sqlalchemy.events SchemaEventTarget Example Code
category: page
slug: sqlalchemy-events-schemaeventtarget-examples
sortorder: 500031033
toc: False
sidebartitle: sqlalchemy.events SchemaEventTarget
meta: Example code for understanding how to use the SchemaEventTarget class from the sqlalchemy.events module of the SQLAlchemy project.


`SchemaEventTarget` is a class within the `sqlalchemy.events` module of the SQLAlchemy project.



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
~~from sqlalchemy.events import SchemaEventTarget
from sqlalchemy.util import OrderedDict
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


## ... source file abbreviated to get to SchemaEventTarget examples ...


        self.table_kwargs = table_kwargs
        self.temp_table_name = self._calc_temp_name(table.name)
        self.new_table = None

        self.partial_reordering = partial_reordering  # tuple of tuples
        self.add_col_ordering = ()  # tuple of tuples

        self.column_transfers = OrderedDict(
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
        self.columns = OrderedDict()
        for c in self.table.c:
            c_copy = c.copy(schema=schema)
            c_copy.unique = c_copy.index = False
~~            if isinstance(c.type, SchemaEventTarget):
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


## ... source file abbreviated to get to SchemaEventTarget examples ...


            try:
                for idx in self._gather_indexes_from_both_tables():
                    op_impl.create_index(idx)
            finally:
                self.new_table.name = self.temp_table_name

    def alter_column(
        self,
        table_name,
        column_name,
        nullable=None,
        server_default=False,
        name=None,
        type_=None,
        autoincrement=None,
        **kw
    ):
        existing = self.columns[column_name]
        existing_transfer = self.column_transfers[column_name]
        if name is not None and name != column_name:
            existing.name = name
            existing_transfer["name"] = name

        if type_ is not None:
            type_ = sqltypes.to_instance(type_)
~~            if isinstance(existing.type, SchemaEventTarget):
                existing.type._create_events = (
                    existing.type.create_constraint
                ) = False

            self.impl.cast_for_batch_migrate(
                existing, existing_transfer, type_
            )

            existing.type = type_


        if nullable is not None:
            existing.nullable = nullable
        if server_default is not False:
            if server_default is None:
                existing.server_default = None
            else:
                sql_schema.DefaultClause(server_default)._set_parent(existing)
        if autoincrement is not None:
            existing.autoincrement = bool(autoincrement)

    def _setup_dependencies_for_add_column(
        self, colname, insert_before, insert_after
    ):


## ... source file continues with no further SchemaEventTarget examples...

```

