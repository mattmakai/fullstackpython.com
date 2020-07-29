title: sqlalchemy.exc InvalidRequestError Example Code
category: page
slug: sqlalchemy-exc-invalidrequesterror-examples
sortorder: 500031038
toc: False
sidebartitle: sqlalchemy.exc InvalidRequestError
meta: Example code for understanding how to use the InvalidRequestError class from the sqlalchemy.exc module of the SQLAlchemy project.


`InvalidRequestError` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-databaseerror-examples.html">DatabaseError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-noinspectionavailable-examples.html">NoInspectionAvailable</a>,
<a href="/sqlalchemy-exc-nosuchtableerror-examples.html">NoSuchTableError</a>,
<a href="/sqlalchemy-exc-operationalerror-examples.html">OperationalError</a>,
and <a href="/sqlalchemy-exc-programmingerror-examples.html">ProgrammingError</a>
are several other callables with code examples from the same `sqlalchemy.exc` package.

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

    def __init__(self, prop_name, column):
        self.prop_name = prop_name
        self.column = column

    def __get__(self, instance, owner):
        if instance is None:
            return self.column
        else:
            return instance.__values__.get(self.prop_name)

    def __set__(self, instance, value):
        instance.__values__[self.prop_name] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete value.")




## ... source file abbreviated to get to InvalidRequestError examples ...


                    updates[k] = sub_cls.__attr_factory__(k, v)
                elif isinstance(v, (sa.Index, sa.Constraint)):
                    inspected_args.append(v)
                elif isinstance(v, json_support.JSONProperty):
                    updates[k] = v
        if table_name is None:
            return
        sub_cls._column_name_map = column_name_map

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

        json_prop_names = set()
        for each_cls in sub_cls.__mro__[::-1]:
            for k, v in each_cls.__dict__.items():
                if isinstance(v, json_support.JSONProperty):
                    if not v.name:
                        v.name = k
                    json_prop_names.add(v.prop_name)
                    json_col = getattr(
                        sub_cls.__dict__.get(v.prop_name), "column", None
                    )
                    if not isinstance(json_col, sa.Column) or not isinstance(
                        json_col.type, sa.JSON


## ... source file continues with no further InvalidRequestError examples...

```

