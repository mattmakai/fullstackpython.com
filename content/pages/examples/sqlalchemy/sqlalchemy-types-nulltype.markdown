title: sqlalchemy.types NULLTYPE Example Code
category: page
slug: sqlalchemy-types-nulltype-examples
sortorder: 500031128
toc: False
sidebartitle: sqlalchemy.types NULLTYPE
meta: Python example code that shows how to use the NULLTYPE constant from the sqlalchemy.types module of the SQLAlchemy project.


NULLTYPE is a constant within the sqlalchemy.types module of the SQLAlchemy project.


## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / ddl / postgresql.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/ddl/postgresql.py)

```python
# postgresql.py
import logging
import re

from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import text
from sqlalchemy import types as sqltypes
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.dialects.postgresql import ExcludeConstraint
from sqlalchemy.dialects.postgresql import INTEGER
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql.expression import UnaryExpression
~~from sqlalchemy.types import NULLTYPE

from .base import alter_column
from .base import alter_table
from .base import AlterColumn
from .base import ColumnComment
from .base import compiles
from .base import format_column_name
from .base import format_table_name
from .base import format_type
from .base import RenameTable
from .impl import DefaultImpl
from .. import util
from ..autogenerate import render
from ..operations import ops
from ..operations import schemaobj
from ..operations.base import BatchOperations
from ..operations.base import Operations
from ..util import compat
from ..util import sqla_compat


log = logging.getLogger(__name__)




## ... source file continues with no further NULLTYPE examples...

```

