title: sqlalchemy.engine.strategies EngineStrategy Example Code
category: page
slug: sqlalchemy-engine-strategies-enginestrategy-examples
sortorder: 500031030
toc: False
sidebartitle: sqlalchemy.engine.strategies EngineStrategy
meta: Example code for understanding how to use the EngineStrategy class from the sqlalchemy.engine.strategies module of the SQLAlchemy project.


`EngineStrategy` is a class within the `sqlalchemy.engine.strategies` module of the SQLAlchemy project.

<a href="/sqlalchemy-engine-strategies-mockenginestrategy-examples.html">MockEngineStrategy</a>
is another callable from the `sqlalchemy.engine.strategies` package with code examples.

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

[**GINO / src/gino / strategies.py**](https://github.com/python-gino/gino/blob/master/src/gino/./strategies.py)

```python
# strategies.py
import asyncio
from copy import copy

from sqlalchemy.engine import url
from sqlalchemy import util
~~from sqlalchemy.engine.strategies import EngineStrategy

from .engine import GinoEngine


~~class GinoStrategy(EngineStrategy):

    name = "gino"
    engine_cls = GinoEngine

    async def create(self, name_or_url, loop=None, **kwargs):
        engine_cls = self.engine_cls
        u = url.make_url(name_or_url)
        if loop is None:
            loop = asyncio.get_event_loop()
        if u.drivername in {"postgresql", "postgres"}:
            u = copy(u)
            u.drivername = "postgresql+asyncpg"

        dialect_cls = u.get_dialect()

        pop_kwarg = kwargs.pop

        dialect_args = {}
        for k in util.get_cls_kwargs(dialect_cls).union(
            getattr(dialect_cls, "init_kwargs", set())
        ):
            if k in kwargs:
                dialect_args[k] = pop_kwarg(k)



## ... source file continues with no further EngineStrategy examples...

```

