title: sqlalchemy.types Integer code examples
category: page
slug: sqlalchemy-types-integer-examples
sortorder: 500031082
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


## ... source file continues with no further Integer examples...

```

