title: sqlalchemy.orm CompositeProperty Example Code
category: page
slug: sqlalchemy-orm-compositeproperty-examples
sortorder: 500031055
toc: False
sidebartitle: sqlalchemy.orm CompositeProperty
meta: Example code for understanding how to use the CompositeProperty class from the sqlalchemy.orm module of the SQLAlchemy project.


`CompositeProperty` is a class within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
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
<a href="/sqlalchemy-orm-interfaces-examples.html">interfaces</a>,
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

[**graphene-sqlalchemy / graphene_sqlalchemy / types.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./types.py)

```python
# types.py
from collections import OrderedDict

import sqlalchemy
from sqlalchemy.ext.hybrid import hybrid_property
~~from sqlalchemy.orm import (ColumnProperty, CompositeProperty,
                            RelationshipProperty)
from sqlalchemy.orm.exc import NoResultFound

from graphene import Field
from graphene.relay import Connection, Node
from graphene.types.objecttype import ObjectType, ObjectTypeOptions
from graphene.types.utils import yank_fields_from_attrs
from graphene.utils.orderedtype import OrderedType

from .converter import (convert_sqlalchemy_column,
                        convert_sqlalchemy_composite,
                        convert_sqlalchemy_hybrid_method,
                        convert_sqlalchemy_relationship)
from .enums import (enum_for_field, sort_argument_for_object_type,
                    sort_enum_for_object_type)
from .registry import Registry, get_global_registry
from .resolvers import get_attr_resolver, get_custom_resolver
from .utils import get_query, is_mapped_class, is_mapped_instance


class ORMField(OrderedType):
    def __init__(
        self,
        model_attr=None,


## ... source file abbreviated to get to CompositeProperty examples ...


        if attr_name not in all_model_attrs:
            raise ValueError((
                "Cannot map ORMField to a model attribute.\n"
                "Field: '{}.{}'"
            ).format(obj_type.__name__, orm_field_name,))
        orm_field.kwargs['model_attr'] = attr_name

    orm_fields = OrderedDict(custom_orm_fields_items)
    for orm_field_name in auto_orm_field_names:
        if orm_field_name in orm_fields:
            continue
        orm_fields[orm_field_name] = ORMField(model_attr=orm_field_name)

    fields = OrderedDict()
    for orm_field_name, orm_field in orm_fields.items():
        attr_name = orm_field.kwargs.pop('model_attr')
        attr = all_model_attrs[attr_name]
        resolver = get_custom_resolver(obj_type, orm_field_name) or get_attr_resolver(obj_type, attr_name)

        if isinstance(attr, ColumnProperty):
            field = convert_sqlalchemy_column(attr, registry, resolver, **orm_field.kwargs)
        elif isinstance(attr, RelationshipProperty):
            batching_ = orm_field.kwargs.pop('batching', batching)
            field = convert_sqlalchemy_relationship(
                attr, obj_type, connection_field_factory, batching_, orm_field_name, **orm_field.kwargs)
~~        elif isinstance(attr, CompositeProperty):
            if attr_name != orm_field_name or orm_field.kwargs:
                raise ValueError(
                    "ORMField kwargs for composite fields must be empty. "
                    "Field: {}.{}".format(obj_type.__name__, orm_field_name))
            field = convert_sqlalchemy_composite(attr, registry, resolver)
        elif isinstance(attr, hybrid_property):
            field = convert_sqlalchemy_hybrid_method(attr, resolver, **orm_field.kwargs)
        else:
            raise Exception('Property type is not supported')  # Should never happen

        registry.register_orm_field(obj_type, orm_field_name, attr)
        fields[orm_field_name] = field

    return fields


class SQLAlchemyObjectTypeOptions(ObjectTypeOptions):
    model = None  # type: sqlalchemy.Model
    registry = None  # type: sqlalchemy.Registry
    connection = None  # type: sqlalchemy.Type[sqlalchemy.Connection]
    id = None  # type: str


class SQLAlchemyObjectType(ObjectType):


## ... source file continues with no further CompositeProperty examples...

```

