title: sqlalchemy.orm.properties RelationshipProperty Example Code
category: page
slug: sqlalchemy-orm-properties-relationshipproperty-examples
sortorder: 500031087
toc: False
sidebartitle: sqlalchemy.orm.properties RelationshipProperty
meta: Example code for understanding how to use the RelationshipProperty class from the sqlalchemy.orm.properties module of the SQLAlchemy project.


`RelationshipProperty` is a class within the `sqlalchemy.orm.properties` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-properties-columnproperty-examples.html">ColumnProperty</a>
is another callable from the `sqlalchemy.orm.properties` package with code examples.

## Example 1 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlalchemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / functions / orm.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/orm.py)

```python
# orm.py
from collections import OrderedDict
from functools import partial
from inspect import isclass
from operator import attrgetter

import six
import sqlalchemy as sa
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import mapperlib
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm.exc import UnmappedInstanceError
~~from sqlalchemy.orm.properties import ColumnProperty, RelationshipProperty
from sqlalchemy.orm.query import _ColumnEntity
from sqlalchemy.orm.session import object_session
from sqlalchemy.orm.util import AliasedInsp

from ..utils import is_sequence


def get_class_by_table(base, table, data=None):
    found_classes = set(
        c for c in base._decl_class_registry.values()
        if hasattr(c, '__table__') and c.__table__ is table
    )
    if len(found_classes) > 1:
        if not data:
            raise ValueError(
                "Multiple declarative classes found for table '{0}'. "
                "Please provide data parameter for this function to be able "
                "to determine polymorphic scenarios.".format(
                    table.name
                )
            )
        else:
            for cls in found_classes:
                mapper = sa.inspect(cls)
                polymorphic_on = mapper.polymorphic_on.name
                if polymorphic_on in data:
                    if data[polymorphic_on] == mapper.polymorphic_identity:
                        return cls
            raise ValueError(
                "Multiple declarative classes found for table '{0}'. Given "
                "data row does not match any polymorphic identity of the "
                "found classes.".format(
                    table.name
                )
            )
    elif found_classes:
        return found_classes.pop()
    return None


def get_type(expr):
    if hasattr(expr, 'type'):
        return expr.type
    elif isinstance(expr, InstrumentedAttribute):
        expr = expr.property

    if isinstance(expr, ColumnProperty):
        return expr.columns[0].type
~~    elif isinstance(expr, RelationshipProperty):
        return expr.mapper.class_
    raise TypeError("Couldn't inspect type.")


def cast_if(expression, type_):
    try:
        expr_type = get_type(expression)
    except TypeError:
        expr_type = expression
        check_type = type_().python_type
    else:
        check_type = type_

    return (
        sa.cast(expression, type_)
        if not isinstance(expr_type, check_type)
        else expression
    )


def get_column_key(model, column):
    mapper = sa.inspect(model)
    try:
        return mapper.get_property_by_column(column).key


## ... source file continues with no further RelationshipProperty examples...

```

