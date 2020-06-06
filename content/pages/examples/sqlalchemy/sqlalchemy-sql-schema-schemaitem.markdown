title: sqlalchemy.sql.schema SchemaItem code examples
category: page
slug: sqlalchemy-sql-schema-schemaitem-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.sql.schema SchemaItem
meta: Python example code for the SchemaItem class from the sqlalchemy.sql.schema module of the SQLAlchemy project.


SchemaItem is a class within the sqlalchemy.sql.schema module of the SQLAlchemy project.


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
    """
    The default ``gino`` extension on
    :class:`-sqlalchemy.sql.expression.Executable` constructs for implicit
    execution.

    Instances of this class are created when visiting the ``gino`` property of
    :class:`-sqlalchemy.sql.expression.Executable` instances (also referred as
    queries or clause elements), for example::

        await User.query.gino.first()

    This allows GINO to add the asynchronous query APIs (:meth:`all`,
    :meth:`first`, :meth:`one`, :meth:`one_or_none`, :meth:`scalar`,
    :meth:`status`, :meth:`iterate`) to SQLAlchemy query clauses without
    messing up with existing synchronous ones.


## ... source file abbreviated to get to SchemaItem examples ...


    `Alembic <http://alembic.zzzcomputing.com/>`_. In usual cases, you would
    want to define one global :class:`-.Gino` instance, usually under the name
    of ``db``, representing the database used in your application.

    You may define tables in `the official way <http://bit.ly/2G25fdc>`_
    SQLAlchemy core recommended, but more often in GINO we define model classes
    with ``db.Model`` as their parent class to represent tables, for its
    objective interface and CRUD operations. Please read :doc:`/how-to/crud`
    for more information.

    For convenience, :class:`Gino` instance delegated all properties publicly
    exposed by :mod:`sqlalchemy`, so that you can define tables / models
    without importing :mod:`sqlalchemy`::

        id = db.Column(db.BigInteger(), primary_key=True)

    Similar to :class:`-sqlalchemy.schema.MetaData`, a :class:`-.Gino` object
    can bind to a :class:`-gino.engine.GinoEngine` instance, hereby allowing
    `"implicit execution" <http://bit.ly/2oTUcKY>`_ through the ``gino``
    extension on :class:`-sqlalchemy.sql.expression.Executable` or
~~    :class:`-sqlalchemy.schema.SchemaItem` constructs::

        await User.query.gino.first()
        await db.gino.create_all()

    Differently, GINO encourages the use of implicit execution and manages
    transactional context correctly.

    Binding to a connection object is not supported.

    To set a bind property, you can simply set your
    :class:`-gino.engine.GinoEngine` object on :attr:`db.bind <Gino.bind>`, or
    set it to ``None`` to unbind. However, the creation of engine usually
    happens at the same time. Therefore, GINO provided several convenient ways
    doing so:

    1. :meth:`-Gino.with_bind` returning an asynchronous context manager::

        async with db.with_bind('postgresql://...') as engine:

    2. :meth:`-Gino.set_bind` and :meth:`-Gino.pop_bind`::

        engine = await db.set_bind('postgresql://...')
        await db.pop_bind().close()



## ... source file abbreviated to get to SchemaItem examples ...



    Default is :class:`(CRUDModel, ) <gino.crud.CRUDModel>`.

    """

    query_executor = GinoExecutor
    """
    The overridable ``gino`` extension class on
    :class:`-sqlalchemy.sql.expression.Executable`.

    This class will be set as the getter method of the property ``gino`` on
    :class:`-sqlalchemy.sql.expression.Executable` and its subclasses, if
    ``ext`` and ``query_ext`` arguments are both ``True``. Default is
    :class:`GinoExecutor`.

    """

    schema_visitor = GinoSchemaVisitor
    """
    The overridable ``gino`` extension class on
~~    :class:`-sqlalchemy.schema.SchemaItem`.

    This class will be set as the getter method of the property ``gino`` on
~~    :class:`-sqlalchemy.schema.SchemaItem` and its subclasses, if ``ext`` and
    ``schema_ext`` arguments are both ``True``. Default is
    :class:`-gino.schema.GinoSchemaVisitor`.

    """

    no_delegate = {"create_engine", "engine_from_config"}
    """
    A set of symbols from :mod:`sqlalchemy` which is not delegated by
    :class:`Gino`.

    """

    def __init__(
        self,
        bind=None,
        model_classes=None,
        query_ext=True,
        schema_ext=True,
        ext=True,
        **kwargs
    ):
        """
        :param bind: A :class:`-.engine.GinoEngine` instance to bind. Also
                     accepts string or :class:`-sqlalchemy.engine.url.URL`,
                     which will be passed to
                     :func:`-gino.create_engine` when this :class:`Gino`
                     instance is awaited. Default is ``None``.
        :param model_classes: A :class:`tuple` of base class and mixin classes
                              to create the :attr:`-.Gino.Model` class. Default
                              is :class:`(CRUDModel, ) <gino.crud.CRUDModel>`.
        :param query_ext: Boolean value to control the installation of the
                          ``gino`` extension on
                          :class:`-sqlalchemy.sql.expression.Executable` for
                          implicit execution. Default is to install (``True``).
        :param schema_ext: Boolean value to control the installation of the
                           ``gino`` extension on
~~                           :class:`-sqlalchemy.schema.SchemaItem` for implicit
                           execution. Default is to install (``True``).
        :param ext: Boolean value to control the installation of the two
                    ``gino`` extensions. ``False`` for no extension at all,
                    while it depends on the two individual switches when this
                    is set to ``True`` (default).
        :param kwargs: Other arguments accepted by
                       :class:`-sqlalchemy.schema.MetaData`.

        """
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

    # noinspection PyPep8Naming
    @property
    def Model(self):
        """
        Declarative base class for models, subclass of
        :class:`gino.declarative.Model`. Defining subclasses of this class will
        result new tables added to this :class:`Gino` metadata.

        """
        return self._model

    @property
    def bind(self):
        """
        An :class:`-.engine.GinoEngine` to which this :class:`Gino` is bound.

        This is a simple property with no getter or setter hook - what you set
        is what you get. To achieve the same result as it is in SQLAlchemy -
        setting a string or :class:`-sqlalchemy.engine.url.URL` and getting an
        engine instance, use :meth:`set_bind` (or ``await`` on this
        :class:`Gino` object after setting a string or
        :class:`-sqlalchemy.engine.url.URL`).


## ... source file continues with no further SchemaItem examples...


```

