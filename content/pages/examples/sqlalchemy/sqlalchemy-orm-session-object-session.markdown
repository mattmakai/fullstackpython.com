title: sqlalchemy.orm.session object_session code examples
category: page
slug: sqlalchemy-orm-session-object-session-examples
sortorder: 500031001
toc: False
sidebartitle: sqlalchemy.orm.session object_session
meta: Python example code for the object_session function from the sqlalchemy.orm.session module of the SQLAlchemy project.


object_session is a function within the sqlalchemy.orm.session module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
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
from sqlalchemy.orm.properties import ColumnProperty, RelationshipProperty
from sqlalchemy.orm.query import _ColumnEntity
~~from sqlalchemy.orm.session import object_session
from sqlalchemy.orm.util import AliasedInsp

from ..utils import is_sequence


def get_class_by_table(base, table, data=None):
    """
    Return declarative class associated with given table. If no class is found
    this function returns `None`. If multiple classes were found (polymorphic
    cases) additional `data` parameter can be given to hint which class
    to return.

    ::

        class User(Base):
            __tablename__ = 'entity'
            id = sa.Column(sa.Integer, primary_key=True)
            name = sa.Column(sa.String)


        get_class_by_table(Base, User.__table__)  # User class


    This function also supports models using single table inheritance.


## ... source file abbreviated to get to object_session examples ...


    """
    Return the bind for given SQLAlchemy Engine / Connection / declarative
    model object.

    :param obj: SQLAlchemy Engine / Connection / declarative model object

    ::

        from sqlalchemy_utils import get_bind


        get_bind(session)  # Connection object

        get_bind(user)

    """
    if hasattr(obj, 'bind'):
        conn = obj.bind
    else:
        try:
~~            conn = object_session(obj).bind
        except UnmappedInstanceError:
            conn = obj

    if not hasattr(conn, 'execute'):
        raise TypeError(
            'This method accepts only Session, Engine, Connection and '
            'declarative model objects.'
        )
    return conn


def get_primary_keys(mixed):
    """
    Return an OrderedDict of all primary keys for given Table object,
    declarative class or declarative class instance.

    :param mixed:
        SA Table object, SA declarative class or SA declarative class instance

    ::

        get_primary_keys(User)

        get_primary_keys(User())


## ... source file abbreviated to get to object_session examples ...


                else:
                    tmp.append(value)
            last = tmp
        elif isinstance(last, InstrumentedAttribute):
            last = getter(last.property.mapper.class_)
        elif last is None:
            return None
        else:
            last = getter(last)
        if condition is not None:
            if is_sequence(last):
                last = [v for v in last if condition(v)]
            else:
                if not condition(last):
                    return None

    return last


def is_deleted(obj):
~~    return obj in sa.orm.object_session(obj).deleted


def has_changes(obj, attrs=None, exclude=None):
    """
    Simple shortcut function for checking if given attributes of given
    declarative model object have changed during the session. Without
    parameters this checks if given object has any modificiations. Additionally
    exclude parameter can be given to check if given object has any changes
    in any attributes other than the ones given in exclude.


    ::


        from sqlalchemy_utils import has_changes


        user = User()

        has_changes(user, 'name')  # False

        user.name = u'someone'

        has_changes(user, 'name')  # True


## ... source file continues with no further object_session examples...


```

