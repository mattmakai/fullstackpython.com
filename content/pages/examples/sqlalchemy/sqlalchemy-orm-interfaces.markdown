title: sqlalchemy.orm interfaces Example Code
category: page
slug: sqlalchemy-orm-interfaces-examples
sortorder: 500031067
toc: False
sidebartitle: sqlalchemy.orm interfaces
meta: Python example code that shows how to use the interfaces callable from the sqlalchemy.orm module of the SQLAlchemy project.


`interfaces` is a callable within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-load-examples.html">Load</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">Mapper</a>,
<a href="/sqlalchemy-orm-query-examples.html">Query</a>,
<a href="/sqlalchemy-orm-relationshipproperty-examples.html">RelationshipProperty</a>,
<a href="/sqlalchemy-orm-session-examples.html">Session</a>,
<a href="/sqlalchemy-orm-synonymproperty-examples.html">SynonymProperty</a>,
<a href="/sqlalchemy-orm-aliased-examples.html">aliased</a>,
<a href="/sqlalchemy-orm-attributes-examples.html">attributes</a>,
<a href="/sqlalchemy-orm-backref-examples.html">backref</a>,
<a href="/sqlalchemy-orm-class-mapper-examples.html">class_mapper</a>,
<a href="/sqlalchemy-orm-column-property-examples.html">column_property</a>,
<a href="/sqlalchemy-orm-composite-examples.html">composite</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">mapper</a>,
<a href="/sqlalchemy-orm-mapperlib-examples.html">mapperlib</a>,
<a href="/sqlalchemy-orm-object-mapper-examples.html">object_mapper</a>,
<a href="/sqlalchemy-orm-object-session-examples.html">object_session</a>,
<a href="/sqlalchemy-orm-query-examples.html">query</a>,
<a href="/sqlalchemy-orm-relationship-examples.html">relationship</a>,
<a href="/sqlalchemy-orm-session-examples.html">session</a>,
<a href="/sqlalchemy-orm-sessionmaker-examples.html">sessionmaker</a>,
and <a href="/sqlalchemy-orm-strategies-examples.html">strategies</a>
are several other callables with code examples from the same `sqlalchemy.orm` package.

## Example 1 from graphene-sqlalchemy
[graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy)
([project documentation](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/)
and
[PyPI package information](https://pypi.org/project/graphene-sqlalchemy/))
is a [SQLAlchemy](/sqlalchemy.html) integration for
[Graphene](https://graphene-python.org/), which makes it easier to build
GraphQL-based [APIs](/application-programming-interfaces.html) into Python
[web applications](/web-development.html). The package allows you to
subclass SQLAlchemy classes and build queries around them with custom
code to match the backend queries with the GraphQL-based request queries.
The project is provided as open source under the
[MIT license](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/LICENSE.md).

[**graphene-sqlalchemy / graphene_sqlalchemy / converter.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./converter.py)

```python
# converter.py
from enum import EnumMeta

from singledispatch import singledispatch
from sqlalchemy import types
from sqlalchemy.dialects import postgresql
~~from sqlalchemy.orm import interfaces, strategies

from graphene import (ID, Boolean, Dynamic, Enum, Field, Float, Int, List,
                      String)
from graphene.types.json import JSONString

from .batching import get_batch_resolver
from .enums import enum_for_sa_enum
from .fields import (BatchSQLAlchemyConnectionField,
                     default_connection_field_factory)
from .registry import get_global_registry
from .resolvers import get_attr_resolver, get_custom_resolver

try:
    from sqlalchemy_utils import ChoiceType, JSONType, ScalarListType, TSVectorType
except ImportError:
    ChoiceType = JSONType = ScalarListType = TSVectorType = object


is_selectin_available = getattr(strategies, 'SelectInLoader', None)


def get_column_doc(column):
    return getattr(column, "doc", None)


def is_column_nullable(column):
    return bool(getattr(column, "nullable", True))


def convert_sqlalchemy_relationship(relationship_prop, obj_type, connection_field_factory, batching,
                                    orm_field_name, **field_kwargs):
    def dynamic_type():
        direction = relationship_prop.direction
        child_type = obj_type._meta.registry.get_type_for_model(relationship_prop.mapper.entity)
        batching_ = batching if is_selectin_available else False

        if not child_type:
            return None

~~        if direction == interfaces.MANYTOONE or not relationship_prop.uselist:
            return _convert_o2o_or_m2o_relationship(relationship_prop, obj_type, batching_, orm_field_name,
                                                    **field_kwargs)

~~        if direction in (interfaces.ONETOMANY, interfaces.MANYTOMANY):
            return _convert_o2m_or_m2m_relationship(relationship_prop, obj_type, batching_,
                                                    connection_field_factory, **field_kwargs)

    return Dynamic(dynamic_type)


def _convert_o2o_or_m2o_relationship(relationship_prop, obj_type, batching, orm_field_name, **field_kwargs):
    child_type = obj_type._meta.registry.get_type_for_model(relationship_prop.mapper.entity)

    resolver = get_custom_resolver(obj_type, orm_field_name)
    if resolver is None:
        resolver = get_batch_resolver(relationship_prop) if batching else \
            get_attr_resolver(obj_type, relationship_prop.key)

    return Field(child_type, resolver=resolver, **field_kwargs)


def _convert_o2m_or_m2m_relationship(relationship_prop, obj_type, batching, connection_field_factory, **field_kwargs):
    child_type = obj_type._meta.registry.get_type_for_model(relationship_prop.mapper.entity)

    if not child_type._meta.connection:
        return Field(List(child_type), **field_kwargs)

    if connection_field_factory is None:


## ... source file continues with no further interfaces examples...

```

