title: sqlalchemy.sql.elements Label code examples
category: page
slug: sqlalchemy-sql-elements-label-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.sql.elements Label
meta: Python example code for the Label class from the sqlalchemy.sql.elements module of the SQLAlchemy project.


Label is a class within the sqlalchemy.sql.elements module of the SQLAlchemy project.


## Example 1 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / loader.py**](https://github.com/python-gino/gino/blob/master/src/gino/./loader.py)

```python
# loader.py
import types
import warnings

from sqlalchemy import select
from sqlalchemy.schema import Column
~~from sqlalchemy.sql.elements import Label

from .declarative import Model


class Loader:
    """The abstract base class of loaders.

    Loaders are used to load raw database rows into expected results.
    :class:`-gino.engine.GinoEngine` will use the loader set on the ``loader`` value of
    the :meth:`-sqlalchemy.sql.expression.Executable.execution_options`, for example::

        from sqlalchemy import text, create_engine
        from gino.loader import ColumnLoader

        e = await create_engine("postgresql://localhost/gino", strategy="gino")
        q = text("SELECT now() as ts")
        loader = ColumnLoader("ts")
        ts = await e.first(q.execution_options(loader=loader))  # datetime

    """

    @classmethod
    def get(cls, value):
        """Automatically create a loader based on the type of the given value.

        +-------------------------------------------+--------------------------+
        | value type                                | loader type              |
        +===========================================+==========================+
        | :class:`tuple`                            | :class:`-TupleLoader`    |
        +-------------------------------------------+--------------------------+
        | :func:`callable`                          | :class:`-CallableLoader` |
        +-------------------------------------------+--------------------------+
        | :class:`-sqlalchemy.schema.Column`,       | :class:`-ColumnLoader`   |
~~        | :class:`-sqlalchemy.sql.expression.Label` |                          |
        +-------------------------------------------+--------------------------+
        | :class:`-gino.declarative.Model`          | :class:`-ModelLoader`    |
        +-------------------------------------------+--------------------------+
        | :class:`-gino.crud.Alias`                 | :class:`-AliasLoader`    |
        +-------------------------------------------+--------------------------+
        | :class:`-Loader`                          | as is                    |
        +-------------------------------------------+--------------------------+
        | any other types                           | :class:`-ValueLoader`    |
        +-------------------------------------------+--------------------------+

        :param value: Any supported value above.
        :return: A loader instance.
        """
        from .crud import Alias

        if isinstance(value, Loader):
            rv = value
        elif isinstance(value, type) and issubclass(value, Model):
            rv = ModelLoader(value)
        elif isinstance(value, Alias):
            rv = AliasLoader(value)
        elif isinstance(value, Column):
            rv = ColumnLoader(value)
~~        elif isinstance(value, Label):
            rv = ColumnLoader(value.name)
        elif isinstance(value, tuple):
            rv = TupleLoader(value)
        elif callable(value):
            rv = CallableLoader(value)
        else:
            rv = ValueLoader(value)
        return rv

    @property
    def query(self):
        """Generate a query from this loader.

        This is an experimental feature, not all loaders support this.

        :return: A query instance with the ``loader`` execution option set to self.
        """
        rv = select(self.get_columns())
        from_clause = self.get_from()
        if from_clause is not None:
            rv = rv.select_from(from_clause)
        return rv.execution_options(loader=self)

    def do_load(self, row, context):


## ... source file continues with no further Label examples...


```

