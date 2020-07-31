title: sqlalchemy.sql.schema SchemaItem Example Code
category: page
slug: sqlalchemy-sql-schema-schemaitem-examples
sortorder: 500031131
toc: False
sidebartitle: sqlalchemy.sql.schema SchemaItem
meta: Example code for understanding how to use the SchemaItem class from the sqlalchemy.sql.schema module of the SQLAlchemy project.


`SchemaItem` is a class within the `sqlalchemy.sql.schema` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-schema-column-examples.html">Column</a>
is another callable from the `sqlalchemy.sql.schema` package with code examples.

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

[**GINO / src/gino / api.py**](https://github.com/python-gino/gino/blob/master/src/gino/./api.py)

```python
# api.py
import weakref

import sqlalchemy as sa
from sqlalchemy.engine.url import make_url, URL
from sqlalchemy.sql.base import Executable
~~from sqlalchemy.sql.schema import SchemaItem

from . import json_support
from .crud import CRUDModel
from .declarative import declarative_base, declared_attr
from .exceptions import UninitializedError
from .schema import GinoSchemaVisitor, patch_schema


class GinoExecutor:

    __slots__ = ("_query",)

    def __init__(self, query):
        self._query = query

    @property
    def query(self):
        return self._query

    def model(self, model):
        if model is not None:
            model = weakref.ref(model)
        return self.execution_options(model=model)



## ... source file abbreviated to get to SchemaItem examples ...


        self,
        bind=None,
        model_classes=None,
        query_ext=True,
        schema_ext=True,
        ext=True,
        **kwargs
    ):
        super().__init__(bind=bind, **kwargs)
        if model_classes is None:
            model_classes = self.model_base_classes
        self._model = declarative_base(self, model_classes)
        self.declared_attr = declared_attr
        self.quoted_name = sa.sql.quoted_name
        from .bakery import Bakery

        self._bakery = Bakery()
        for mod in json_support, sa:
            for key in mod.__all__:
                if not hasattr(self, key) and key not in self.no_delegate:
                    setattr(self, key, getattr(mod, key))
        if ext:
            if query_ext:
                Executable.gino = property(self.query_executor)
            if schema_ext:
~~                SchemaItem.gino = property(self.schema_visitor)
                patch_schema(self)

    @property
    def Model(self):
        return self._model

    @property
    def bind(self):
        if self._bind is None:
            return _PlaceHolder(UninitializedError("Gino engine is not initialized."))
        return self._bind

    @bind.setter
    def bind(self, bind):
        self._bind = bind

    async def set_bind(self, bind, loop=None, **kwargs):
        if isinstance(bind, str):
            bind = make_url(bind)
        if isinstance(bind, URL):
            from . import create_engine

            bind = await create_engine(bind, loop=loop, bakery=self._bakery, **kwargs)
        self.bind = bind


## ... source file continues with no further SchemaItem examples...

```

