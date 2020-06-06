title: sqlalchemy.events SchemaEventTarget code examples
category: page
slug: sqlalchemy-events-schemaeventtarget-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.events SchemaEventTarget
meta: Python example code for the SchemaEventTarget class from the sqlalchemy.events module of the SQLAlchemy project.


SchemaEventTarget is a class within the sqlalchemy.events module of the SQLAlchemy project.


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
            # ensure that the type object was copied,
            # as we may need to modify it in-place
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
                # TODO: we are skipping reflected CheckConstraint because
                # we have no way to determine _is_type_bound() for these.
                pass
            elif const.name:
                self.named_constraints[const.name] = const
            else:
                self.unnamed_constraints.append(const)

        for idx in self.table.indexes:
            self.indexes[idx.name] = idx

        for k in self.table.kwargs:
            self.table_kwargs.setdefault(k, self.table.kwargs[k])



## ... source file abbreviated to get to SchemaEventTarget examples ...


        name=None,
        type_=None,
        autoincrement=None,
        **kw
    ):
        existing = self.columns[column_name]
        existing_transfer = self.column_transfers[column_name]
        if name is not None and name != column_name:
            # note that we don't change '.key' - we keep referring
            # to the renamed column by its old key in _create().  neat!
            existing.name = name
            existing_transfer["name"] = name

        if type_ is not None:
            type_ = sqltypes.to_instance(type_)
            # old type is being discarded so turn off eventing
            # rules. Alternatively we can
            # erase the events set up by this type, but this is simpler.
            # we also ignore the drop_constraint that will come here from
            # Operations.implementation_for(alter_column)
~~            if isinstance(existing.type, SchemaEventTarget):
                existing.type._create_events = (
                    existing.type.create_constraint
                ) = False

            self.impl.cast_for_batch_migrate(
                existing, existing_transfer, type_
            )

            existing.type = type_

            # we *dont* however set events for the new type, because
            # alter_column is invoked from
            # Operations.implementation_for(alter_column) which already
            # will emit an add_constraint()

        if nullable is not None:
            existing.nullable = nullable
        if server_default is not False:
            if server_default is None:
                existing.server_default = None
            else:
                sql_schema.DefaultClause(server_default)._set_parent(existing)
        if autoincrement is not None:
            existing.autoincrement = bool(autoincrement)


## ... source file continues with no further SchemaEventTarget examples...


```

