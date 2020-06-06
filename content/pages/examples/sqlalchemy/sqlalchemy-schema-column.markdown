title: sqlalchemy.schema Column code examples
category: page
slug: sqlalchemy-schema-column-examples
sortorder: 500031001
toc: False
sidebartitle: sqlalchemy.schema Column
meta: Python example code for the Column class from the sqlalchemy.schema module of the SQLAlchemy project.


Column is a class within the sqlalchemy.schema module of the SQLAlchemy project.


## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / util / sqla_compat.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/util/sqla_compat.py)

```python
# sqla_compat.py
import re

from sqlalchemy import __version__
from sqlalchemy import inspect
from sqlalchemy import schema
from sqlalchemy import sql
from sqlalchemy import types as sqltypes
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CheckConstraint
~~from sqlalchemy.schema import Column
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.sql.elements import quoted_name
from sqlalchemy.sql.expression import _BindParamClause
from sqlalchemy.sql.expression import _TextClause as TextClause
from sqlalchemy.sql.visitors import traverse

from . import compat


def _safe_int(value):
    try:
        return int(value)
    except:
        return value


_vers = tuple(
    [_safe_int(x) for x in re.findall(r"(\d+|[abc]\d)", __version__)]
)
sqla_110 = _vers >= (1, 1, 0)
sqla_1115 = _vers >= (1, 1, 15)
sqla_120 = _vers >= (1, 2, 0)
sqla_1216 = _vers >= (1, 2, 16)
sqla_13 = _vers >= (1, 3)


## ... source file abbreviated to get to Column examples ...


def _find_columns(clause):
    """locate Column objects within the given expression."""

    cols = set()
    traverse(clause, {}, {"column": cols.add})
    return cols


def _remove_column_from_collection(collection, column):
    """remove a column from a ColumnCollection."""

    # workaround for older SQLAlchemy, remove the
    # same object that's present
    to_remove = collection[column.key]
    collection.remove(to_remove)


def _textual_index_column(table, text_):
    """a workaround for the Index construct's severe lack of flexibility"""
    if isinstance(text_, compat.string_types):
~~        c = Column(text_, sqltypes.NULLTYPE)
        table.append_column(c)
        return c
    elif isinstance(text_, TextClause):
        return _textual_index_element(table, text_)
    else:
        raise ValueError("String or text() construct expected")


~~class _textual_index_element(sql.ColumnElement):
    """Wrap around a sqlalchemy text() construct in such a way that
    we appear like a column-oriented SQL expression to an Index
    construct.

    The issue here is that currently the Postgresql dialect, the biggest
    recipient of functional indexes, keys all the index expressions to
    the corresponding column expressions when rendering CREATE INDEX,
    so the Index we create here needs to have a .columns collection that
    is the same length as the .expressions collection.  Ultimately
    SQLAlchemy should support text() expressions in indexes.

    See SQLAlchemy issue 3174.

    """

    __visit_name__ = "_textual_idx_element"

    def __init__(self, table, text):
        self.table = table
        self.text = text
        self.key = text.text
~~        self.fake_column = schema.Column(self.text.text, sqltypes.NULLTYPE)
        table.append_column(self.fake_column)

    def get_children(self):
        return [self.fake_column]


@compiles(_textual_index_element)
def _render_textual_index_column(element, compiler, **kw):
    return compiler.process(element.text, **kw)


class _literal_bindparam(_BindParamClause):
    pass


@compiles(_literal_bindparam)
def _render_literal_bindparam(element, compiler, **kw):
    return compiler.render_literal_bindparam(element, **kw)


def _get_index_expressions(idx):
    return list(idx.expressions)




## ... source file continues with no further Column examples...


```


## Example 2 from GINO
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
~~from sqlalchemy.schema import Column
from sqlalchemy.sql.elements import Label

from .declarative import Model


class Loader:
    """The abstract base class of loaders.

    Loaders are used to load raw database rows into expected results.
    :class:`-gino.engine.GinoEngine` will use the loader set on the ``loader`` value of
    the :meth:`-sqlalchemy.sql.expression.Executable.execution_options`, for example::

        from sqlalchemy import text, create_engine
~~        from gino.loader import ColumnLoader

        e = await create_engine("postgresql://localhost/gino", strategy="gino")
        q = text("SELECT now() as ts")
~~        loader = ColumnLoader("ts")
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
~~        | :class:`-sqlalchemy.schema.Column`,       | :class:`-ColumnLoader`   |
        | :class:`-sqlalchemy.sql.expression.Label` |                          |
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
~~        elif isinstance(value, Column):
~~            rv = ColumnLoader(value)
        elif isinstance(value, Label):
~~            rv = ColumnLoader(value.name)
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
        """Interface used by GINO to run the loader.


## ... source file abbreviated to get to Column examples ...


        return []

    def get_from(self):
        """Generate a clause to be used in
        :meth:`-sqlalchemy.sql.expression.Select.select_from` from this loader.

        This is an experimental feature, this method is supposed to be called by
        :attr:`-query`.

        :return: A :class:`-sqlalchemy.sql.expression.FromClause` instance, or ``None``.
        """
        return None

    def __getattr__(self, item):
        return getattr(self.query, item)


_none = object()


~~def _get_column(model, column_or_name) -> Column:
    if isinstance(column_or_name, str):
        return getattr(model, column_or_name)

~~    if isinstance(column_or_name, Column):
        if column_or_name in model:
            return column_or_name
        raise AttributeError(
~~            "Column {} does not belong to model {}".format(column_or_name, model)
        )

    raise TypeError(
        "Unknown column {} with type {}".format(column_or_name, type(column_or_name))
    )


class ModelLoader(Loader):
    """A loader that loads a row into a GINO model instance.

    This loader generates an instance of the given ``model`` type and fills the instance
    with attributes according to the other given parameters:

    * Load each column attribute listed in the given ``columns`` positional arguments.
    * If ``columns`` is not given, all defined columns of the ``model`` will be loaded.
    * For each keyword argument, its value will be used to generate a loader using
      :meth:`Loader.get`, and the loaded value will be :func:`setattr` to the model
      instance under the name of the key.

    .. note:

        The loader does not affect the query. You must have the values in the SQL result
        before you can use loaders to load them into model instances.



## ... source file abbreviated to get to Column examples ...


        ).execution_options(
            loader=ModelLoader(User, id=1)
        )

    ``1`` is then converted into a :class:`-ValueLoader` and mocked the ``id`` attribute
    of all returned ``User`` instances as ``1``.

    Nest another :class:`-ModelLoader`::

        sqlalchemy.select(
            [user.outerjoin(Company)]
        ).execution_options(
            loader=ModelLoader(User, company=Company)
        )

    Likewise, ``Company`` is converted into a :class:`-ModelLoader` to load the
    ``Company`` columns from the joined result, and the ``Company`` instances are set to
    the ``company`` attribute of each ``User`` instance using :func:`setattr`.

    :param model: A subclass of :class:`-gino.declarative.Model` to instantiate.
~~    :param columns: A list of :class:`-sqlalchemy.schema.Column` or :class:`str` to
                    load, default is all the columns in the model.
    :param extras: Additional attributes to load on the model instance.
    """

    def __init__(self, model, *columns, **extras):
        self.model = model
        self._distinct = None
        if columns:
            self.columns = [_get_column(model, name) for name in columns]
        else:
            self.columns = model
        self.extras = dict((key, self.get(value)) for key, value in extras.items())
        self.on_clause = None

    def _do_load(self, row):
        values = dict((c.name, row[c]) for c in self.columns if c in row)
        if all((v is None) for v in values.values()):
            return None
        rv = self.model()
        for c in self.columns:
            if c in row:
                # noinspection PyProtectedMember
                instance_key = self.model._column_name_map.invert_get(c.name)
                rv.__values__[instance_key] = row[c]


## ... source file abbreviated to get to Column examples ...


        self.extras.update((key, self.get(value)) for key, value in extras.items())
        return self

    def on(self, on_clause):
        """Specify the ``on_clause`` for generating joined queries.

        This is an experimental feature, used by :meth:`-get_from`.

        :param on_clause: An expression to feed into
                          :func:`-sqlalchemy.sql.expression.join`.
        :return: ``self`` for chaining.
        """

        self.on_clause = on_clause
        return self

    def distinct(self, *columns):
        """Configure this loader to reuse instances that have the same values of all the
        give columns.

~~        :param columns: Preferably :class:`-sqlalchemy.schema.Column` instances.
        :return: ``self`` for chaining.
        """
        self._distinct = columns
        return self

    def none_as_none(self, enabled=True):
        """Deprecated method for compatibility, does nothing."""
        if not enabled:
            warnings.warn(
                "Disabling none_as_none is not supported.", DeprecationWarning,
            )
        return self


class AliasLoader(ModelLoader):
    """The same as :class:`-ModelLoader`, kept for compatibility."""

    def __init__(self, alias, *columns, **extras):
        super().__init__(alias, *columns, **extras)


~~class ColumnLoader(Loader):
    """Load a given column in the row.

    :param column: The column name as :class:`str`, or a
~~                   :class:`-sqlalchemy.schema.Column` instance to avoid name conflict.
    """

    def __init__(self, column):
        self.column = column

    def do_load(self, row, context):
        """Interface used by GINO to run the loader.

        :param row: A :class:`-sqlalchemy.engine.RowProxy` instance.
        :param context: Not used.
        :return: The value of the specified column, followed by ``True``.
        """

        return row[self.column], True


class TupleLoader(Loader):
    """Load multiple values into a tuple.

    :param values: A :class:`tuple`, each item is converted into a loader with
                   :func:`Loader.get`.
    """

    def __init__(self, values):


## ... source file continues with no further Column examples...


```

