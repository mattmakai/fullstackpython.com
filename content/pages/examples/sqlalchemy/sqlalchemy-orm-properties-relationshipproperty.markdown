title: sqlalchemy.orm.properties RelationshipProperty code examples
category: page
slug: sqlalchemy-orm-properties-relationshipproperty-examples
sortorder: 500031001
toc: False
sidebartitle: sqlalchemy.orm.properties RelationshipProperty
meta: Python example code for the RelationshipProperty class from the sqlalchemy.orm.properties module of the SQLAlchemy project.


RelationshipProperty is a class within the sqlalchemy.orm.properties module of the SQLAlchemy project.


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
~~from sqlalchemy.orm.properties import ColumnProperty, RelationshipProperty
from sqlalchemy.orm.query import _ColumnEntity
from sqlalchemy.orm.session import object_session
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



## ... source file abbreviated to get to RelationshipProperty examples ...


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
    """
    Return the associated type with given Column, InstrumentedAttribute,
~~    ColumnProperty, RelationshipProperty or other similar SQLAlchemy construct.

    For constructs wrapping columns this is the column type. For relationships
    this function returns the relationship mapper class.

    :param expr:
        SQLAlchemy Column, InstrumentedAttribute, ColumnProperty or other
        similar SA construct.

    ::

        class User(Base):
            __tablename__ = 'user'
            id = sa.Column(sa.Integer, primary_key=True)
            name = sa.Column(sa.String)


        class Article(Base):
            __tablename__ = 'article'
            id = sa.Column(sa.Integer, primary_key=True)
            author_id = sa.Column(sa.Integer, sa.ForeignKey(User.id))
            author = sa.orm.relationship(User)


        get_type(User.__table__.c.name)  # sa.String()
        get_type(User.name)  # sa.String()
        get_type(User.name.property)  # sa.String()

        get_type(Article.author)  # User


    .. versionadded: 0.30.9
    """
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
    """
    Produce a CAST expression but only if given expression is not of given type
    already.

    Assume we have a model with two fields id (Integer) and name (String).

    ::

        import sqlalchemy as sa
        from sqlalchemy_utils import cast_if


        cast_if(User.id, sa.Integer)    # "user".id
        cast_if(User.name, sa.String)   # "user".name
        cast_if(User.id, sa.String)     # CAST("user".id AS TEXT)


    This function supports scalar values as well.



## ... source file abbreviated to get to RelationshipProperty examples ...


        if name == alias:
            return entity


def get_polymorphic_mappers(mixed):
    if isinstance(mixed, AliasedInsp):
        return mixed.with_polymorphic_mappers
    else:
        return mixed.polymorphic_map.values()


def get_query_descriptor(query, entity, attr):
    if attr in query_labels(query):
        return attr
    else:
        entity = get_query_entity_by_alias(query, entity)
        if entity:
            descriptor = get_descriptor(entity, attr)
            if (
                hasattr(descriptor, 'property') and
~~                isinstance(descriptor.property, sa.orm.RelationshipProperty)
            ):
                return
            return descriptor


def get_descriptor(entity, attr):
    mapper = sa.inspect(entity)

    for key, descriptor in get_all_descriptors(mapper).items():
        if attr == key:
            prop = (
                descriptor.property
                if hasattr(descriptor, 'property')
                else None
            )
            if isinstance(prop, ColumnProperty):
                if isinstance(entity, sa.orm.util.AliasedClass):
                    for c in mapper.selectable.c:
                        if c.key == attr:
                            return c
                else:
                    # If the property belongs to a class that uses
                    # polymorphic inheritance we have to take into account
                    # situations where the attribute exists in child class


## ... source file continues with no further RelationshipProperty examples...


```

