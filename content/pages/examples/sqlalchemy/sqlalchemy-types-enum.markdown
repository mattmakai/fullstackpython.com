title: sqlalchemy.types Enum Example Code
category: page
slug: sqlalchemy-types-enum-examples
sortorder: 500031138
toc: False
sidebartitle: sqlalchemy.types Enum
meta: Example code for understanding how to use the Enum class from the sqlalchemy.types module of the SQLAlchemy project.


`Enum` is a class within the `sqlalchemy.types` module of the SQLAlchemy project.

<a href="/sqlalchemy-types-boolean-examples.html">BOOLEAN</a>,
<a href="/sqlalchemy-types-boolean-examples.html">Boolean</a>,
<a href="/sqlalchemy-types-date-examples.html">DATE</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DATETIME</a>,
<a href="/sqlalchemy-types-date-examples.html">Date</a>,
<a href="/sqlalchemy-types-datetime-examples.html">DateTime</a>,
<a href="/sqlalchemy-types-float-examples.html">FLOAT</a>,
<a href="/sqlalchemy-types-float-examples.html">Float</a>,
<a href="/sqlalchemy-types-integer-examples.html">INTEGER</a>,
<a href="/sqlalchemy-types-integer-examples.html">Integer</a>,
<a href="/sqlalchemy-types-interval-examples.html">Interval</a>,
<a href="/sqlalchemy-types-nulltype-examples.html">NULLTYPE</a>,
<a href="/sqlalchemy-types-nulltype-examples.html">NullType</a>,
<a href="/sqlalchemy-types-string-examples.html">String</a>,
<a href="/sqlalchemy-types-text-examples.html">TEXT</a>,
<a href="/sqlalchemy-types-time-examples.html">TIME</a>,
<a href="/sqlalchemy-types-text-examples.html">Text</a>,
<a href="/sqlalchemy-types-time-examples.html">Time</a>,
<a href="/sqlalchemy-types-typeengine-examples.html">TypeEngine</a>,
<a href="/sqlalchemy-types-userdefinedtype-examples.html">UserDefinedType</a>,
and <a href="/sqlalchemy-types-to-instance-examples.html">to_instance</a>
are several other callables with code examples from the same `sqlalchemy.types` package.

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

[**graphene-sqlalchemy / graphene_sqlalchemy / enums.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./enums.py)

```python
# enums.py
import six
from sqlalchemy.orm import ColumnProperty
~~from sqlalchemy.types import Enum as SQLAlchemyEnumType

from graphene import Argument, Enum, List

from .utils import EnumValue, to_enum_value_name, to_type_name


def _convert_sa_to_graphene_enum(sa_enum, fallback_name=None):
    if not isinstance(sa_enum, SQLAlchemyEnumType):
        raise TypeError(
            "Expected sqlalchemy.types.Enum, but got: {!r}".format(sa_enum)
        )
    enum_class = sa_enum.enum_class
    if enum_class:
        if all(to_enum_value_name(key) == key for key in enum_class.__members__):
~~            return Enum.from_enum(enum_class)
        name = enum_class.__name__
        members = [
            (to_enum_value_name(key), value.value)
            for key, value in enum_class.__members__.items()
        ]
    else:
        sql_enum_name = sa_enum.name
        if sql_enum_name:
            name = to_type_name(sql_enum_name)
        elif fallback_name:
            name = fallback_name
        else:
            raise TypeError("No type name specified for {!r}".format(sa_enum))
        members = [(to_enum_value_name(key), key) for key in sa_enum.enums]
~~    return Enum(name, members)


def enum_for_sa_enum(sa_enum, registry):
    if not isinstance(sa_enum, SQLAlchemyEnumType):
        raise TypeError(
            "Expected sqlalchemy.types.Enum, but got: {!r}".format(sa_enum)
        )
    enum = registry.get_graphene_enum_for_sa_enum(sa_enum)
    if not enum:
        enum = _convert_sa_to_graphene_enum(sa_enum)
        registry.register_enum(sa_enum, enum)
    return enum


def enum_for_field(obj_type, field_name):
    from .types import SQLAlchemyObjectType

    if not isinstance(obj_type, type) or not issubclass(obj_type, SQLAlchemyObjectType):
        raise TypeError(
            "Expected SQLAlchemyObjectType, but got: {!r}".format(obj_type))
    if not field_name or not isinstance(field_name, six.string_types):
        raise TypeError(
            "Expected a field name, but got: {!r}".format(field_name))
    registry = obj_type._meta.registry


## ... source file abbreviated to get to Enum examples ...


        if name != enum.__name__ or custom_options != enum.custom_options:
            raise ValueError(
                "Sort enum for {} has already been customized".format(obj_type)
            )
    else:
        members = []
        default = []
        fields = obj_type._meta.fields
        get_name = get_symbol_name or _default_sort_enum_symbol_name
        for field_name in fields:
            if only_fields and field_name not in only_fields:
                continue
            orm_field = registry.get_orm_field_for_graphene_field(obj_type, field_name)
            if not isinstance(orm_field, ColumnProperty):
                continue
            column = orm_field.columns[0]
            if only_indexed and not (column.primary_key or column.index):
                continue
            asc_name = get_name(column.name, True)
            asc_value = EnumValue(asc_name, column.asc())
            desc_name = get_name(column.name, False)
            desc_value = EnumValue(desc_name, column.desc())
            if column.primary_key:
                default.append(asc_value)
            members.extend(((asc_name, asc_value), (desc_name, desc_value)))
~~        enum = Enum(name, members)
        enum.default = default  # store default as attribute
        enum.custom_options = custom_options
        registry.register_sort_enum(obj_type, enum)
    return enum


def sort_argument_for_object_type(
    obj_type,
    enum_name=None,
    only_fields=None,
    only_indexed=None,
    get_symbol_name=None,
    has_default=True,
):
    enum = sort_enum_for_object_type(
        obj_type,
        enum_name,
        only_fields=only_fields,
        only_indexed=only_indexed,
        get_symbol_name=get_symbol_name,
    )
    if not has_default:
        enum.default = None



## ... source file continues with no further Enum examples...

```

