title: sqlalchemy.types Integer code examples
category: page
slug: sqlalchemy-types-integer-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.types Integer
meta: Python example code for the Integer class from the sqlalchemy.types module of the SQLAlchemy project.


Integer is a class within the sqlalchemy.types module of the SQLAlchemy project.


## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / operations / schemaobj.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/operations/schemaobj.py)

```python
# schemaobj.py
from sqlalchemy import schema as sa_schema
~~from sqlalchemy.types import Integer
from sqlalchemy.types import NULLTYPE

from .. import util
from ..util.compat import string_types


class SchemaObjects(object):
    def __init__(self, migration_context=None):
        self.migration_context = migration_context

    def primary_key_constraint(self, name, table_name, cols, schema=None):
        m = self.metadata()
        columns = [sa_schema.Column(n, NULLTYPE) for n in cols]
        t = sa_schema.Table(table_name, m, *columns, schema=schema)
        p = sa_schema.PrimaryKeyConstraint(*[t.c[n] for n in cols], name=name)
        t.append_constraint(p)
        return p

    def foreign_key_constraint(
        self,
        name,
        source,
        referent,
        local_cols,


## ... source file abbreviated to get to Integer examples ...


        return f

    def unique_constraint(self, name, source, local_cols, schema=None, **kw):
        t = sa_schema.Table(
            source,
            self.metadata(),
            *[sa_schema.Column(n, NULLTYPE) for n in local_cols],
            schema=schema
        )
        kw["name"] = name
        uq = sa_schema.UniqueConstraint(*[t.c[n] for n in local_cols], **kw)
        # TODO: need event tests to ensure the event
        # is fired off here
        t.append_constraint(uq)
        return uq

    def check_constraint(self, name, source, condition, schema=None, **kw):
        t = sa_schema.Table(
            source,
            self.metadata(),
~~            sa_schema.Column("x", Integer),
            schema=schema,
        )
        ck = sa_schema.CheckConstraint(condition, name=name, **kw)
        t.append_constraint(ck)
        return ck

    def generic_constraint(self, name, table_name, type_, schema=None, **kw):
        t = self.table(table_name, schema=schema)
        types = {
            "foreignkey": lambda name: sa_schema.ForeignKeyConstraint(
                [], [], name=name
            ),
            "primary": sa_schema.PrimaryKeyConstraint,
            "unique": sa_schema.UniqueConstraint,
            "check": lambda name: sa_schema.CheckConstraint("", name=name),
            None: sa_schema.Constraint,
        }
        try:
            const = types[type_]
        except KeyError:
            raise TypeError(
                "'type' can be one of %s"
                % ", ".join(sorted(repr(x) for x in types))
            )


## ... source file continues with no further Integer examples...


```

