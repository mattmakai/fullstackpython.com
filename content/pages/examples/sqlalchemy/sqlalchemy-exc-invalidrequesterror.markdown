title: sqlalchemy.exc InvalidRequestError code examples
category: page
slug: sqlalchemy-exc-invalidrequesterror-examples
sortorder: 500031002
toc: False
sidebartitle: sqlalchemy.exc InvalidRequestError
meta: Python example code for the InvalidRequestError class from the sqlalchemy.exc module of the SQLAlchemy project.


InvalidRequestError is a class within the sqlalchemy.exc module of the SQLAlchemy project.


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

[**GINO / src/gino / declarative.py**](https://github.com/python-gino/gino/blob/master/src/gino/./declarative.py)

```python
# declarative.py
import collections

import sqlalchemy as sa
~~from sqlalchemy.exc import InvalidRequestError

from . import json_support
from .exceptions import GinoException


class ColumnAttribute:
    """The type of the column wrapper attributes on GINO models.

    This is the core utility to enable GINO models so that:

    * Accessing a column attribute on a model class returns the column itself
    * Accessing a column attribute on a model instance returns the value for that column

    This utility is customizable by defining ``__attr_factory__`` in the model class.
    """

    def __init__(self, prop_name, column):
        self.prop_name = prop_name
        self.column = column

    def __get__(self, instance, owner):
        if instance is None:
            return self.column
        else:


## ... source file abbreviated to get to InvalidRequestError examples ...


            return
        sub_cls._column_name_map = column_name_map

        # handle __table_args__
        table_args = updates.get(
            "__table_args__", getattr(sub_cls, "__table_args__", None)
        )
        args, table_kw = (), {}
        if isinstance(table_args, dict):
            table_kw = table_args
        elif isinstance(table_args, tuple) and table_args:
            if isinstance(table_args[-1], dict):
                args, table_kw = table_args[0:-1], table_args[-1]
            else:
                args = table_args

        args = (*columns, *inspected_args, *args)
        for item in args:
            try:
                _table = getattr(item, "table", None)
~~            except InvalidRequestError:
                _table = None
            if _table is not None:
                raise ValueError(
                    "{} is already attached to another table. Please do not "
                    "use the same item twice. A common mistake is defining "
                    "constraints and indices in a super class - we are working"
                    " on making it possible."
                )
        rv = sa.Table(table_name, sub_cls.__metadata__, *args, **table_kw)
        for k, v in updates.items():
            setattr(sub_cls, k, v)
        for each_cls in sub_cls.__mro__[::-1]:
            for k, v in each_cls.__dict__.items():
                if isinstance(v, json_support.JSONProperty):
                    json_col = getattr(
                        sub_cls.__dict__.get(v.prop_name), "column", None
                    )
                    if not isinstance(json_col, sa.Column) or not isinstance(
                        json_col.type, sa.JSON
                    ):
                        raise AttributeError(
                            '{} "{}" requires a JSON[B] column "{}" '
                            "which is not found or has a wrong type.".format(
                                type(v).__name__, v.name, v.prop_name,


## ... source file continues with no further InvalidRequestError examples...


```

