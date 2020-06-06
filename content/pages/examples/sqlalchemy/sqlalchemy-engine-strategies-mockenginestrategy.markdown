title: sqlalchemy.engine.strategies MockEngineStrategy code examples
category: page
slug: sqlalchemy-engine-strategies-mockenginestrategy-examples
sortorder: 500031001
toc: False
sidebartitle: sqlalchemy.engine.strategies MockEngineStrategy
meta: Python example code for the MockEngineStrategy class from the sqlalchemy.engine.strategies module of the SQLAlchemy project.


MockEngineStrategy is a class within the sqlalchemy.engine.strategies module of the SQLAlchemy project.


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



## ... source file abbreviated to get to MockEngineStrategy examples ...


        except AttributeError:
            return False
        else:
            return meth()

    def execute(self, sql, execution_options=None):
        """Execute a SQL construct or string statement.

        The underlying execution mechanics are used, that is
        if this is "offline mode" the SQL is written to the
        output buffer, otherwise the SQL is emitted on
        the current SQLAlchemy connection.

        """
        self.impl._exec(sql, execution_options)

    def _stdout_connection(self, connection):
        def dump(construct, *multiparams, **params):
            self.impl._exec(construct)

~~        return MockEngineStrategy.MockConnection(self.dialect, dump)

    @property
    def bind(self):
        """Return the current "bind".

        In online mode, this is an instance of
        :class:`sqlalchemy.engine.Connection`, and is suitable
        for ad-hoc execution of any kind of usage described
        in :ref:`sqlexpression_toplevel` as well as
        for usage with the :meth:`sqlalchemy.schema.Table.create`
        and :meth:`sqlalchemy.schema.MetaData.create_all` methods
        of :class:`-sqlalchemy.schema.Table`,
        :class:`-sqlalchemy.schema.MetaData`.

        Note that when "standard output" mode is enabled,
        this bind will be a "mock" connection handler that cannot
        return results and is only appropriate for a very limited
        subset of commands.

        """
        return self.connection

    @property
    def config(self):


## ... source file continues with no further MockEngineStrategy examples...


```

