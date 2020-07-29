title: sqlalchemy.engine.strategies MockEngineStrategy Example Code
category: page
slug: sqlalchemy-engine-strategies-mockenginestrategy-examples
sortorder: 500031031
toc: False
sidebartitle: sqlalchemy.engine.strategies MockEngineStrategy
meta: Example code for understanding how to use the MockEngineStrategy class from the sqlalchemy.engine.strategies module of the SQLAlchemy project.


`MockEngineStrategy` is a class within the `sqlalchemy.engine.strategies` module of the SQLAlchemy project.

<a href="/sqlalchemy-engine-strategies-enginestrategy-examples.html">EngineStrategy</a>
is another callable from the `sqlalchemy.engine.strategies` package with code examples.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / runtime / migration.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/runtime/migration.py)

```python
# migration.py
from contextlib import contextmanager
import logging
import sys

from sqlalchemy import Column
from sqlalchemy import literal_column
from sqlalchemy import MetaData
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.engine import Connection
from sqlalchemy.engine import url as sqla_url
~~from sqlalchemy.engine.strategies import MockEngineStrategy

from .. import ddl
from .. import util
from ..util import sqla_compat
from ..util.compat import callable
from ..util.compat import EncodedIO

log = logging.getLogger(__name__)


class _ProxyTransaction(object):
    def __init__(self, migration_context):
        self.migration_context = migration_context

    @property
    def _proxied_transaction(self):
        return self.migration_context._transaction

    def rollback(self):
        self._proxied_transaction.rollback()

    def commit(self):
        self._proxied_transaction.commit()



## ... source file continues with no further MockEngineStrategy examples...

```

