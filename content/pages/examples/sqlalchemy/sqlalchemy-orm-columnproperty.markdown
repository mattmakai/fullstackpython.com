title: sqlalchemy.orm ColumnProperty Example Code
category: page
slug: sqlalchemy-orm-columnproperty-examples
sortorder: 500031054
toc: False
sidebartitle: sqlalchemy.orm ColumnProperty
meta: Example code for understanding how to use the ColumnProperty class from the sqlalchemy.orm module of the SQLAlchemy project.


`ColumnProperty` is a class within the `sqlalchemy.orm` module of the SQLAlchemy project.

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

[**graphene-sqlalchemy / graphene_sqlalchemy / enums.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./enums.py)

```python
# enums.py
import six
~~from sqlalchemy.orm import ColumnProperty
from sqlalchemy.types import Enum as SQLAlchemyEnumType

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
            return Enum.from_enum(enum_class)
        name = enum_class.__name__
        members = [
            (to_enum_value_name(key), value.value)
            for key, value in enum_class.__members__.items()
        ]
    else:
        sql_enum_name = sa_enum.name
        if sql_enum_name:


## ... source file abbreviated to get to ColumnProperty examples ...


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
    orm_field = registry.get_orm_field_for_graphene_field(obj_type, field_name)
    if orm_field is None:
        raise TypeError("Cannot get {}.{}".format(obj_type._meta.name, field_name))
~~    if not isinstance(orm_field, ColumnProperty):
        raise TypeError(
            "{}.{} does not map to model column".format(obj_type._meta.name, field_name)
        )
    column = orm_field.columns[0]
    sa_enum = column.type
    if not isinstance(sa_enum, SQLAlchemyEnumType):
        raise TypeError(
            "{}.{} does not map to enum column".format(obj_type._meta.name, field_name)
        )
    enum = registry.get_graphene_enum_for_sa_enum(sa_enum)
    if not enum:
        fallback_name = obj_type._meta.name + to_type_name(field_name)
        enum = _convert_sa_to_graphene_enum(sa_enum, fallback_name)
        registry.register_enum(sa_enum, enum)
    return enum


def _default_sort_enum_symbol_name(column_name, sort_asc=True):
    return to_enum_value_name(column_name) + ("_ASC" if sort_asc else "_DESC")


def sort_enum_for_object_type(
    obj_type, name=None, only_fields=None, only_indexed=None, get_symbol_name=None
):
    name = name or obj_type._meta.name + "SortEnum"
    registry = obj_type._meta.registry
    enum = registry.get_sort_enum_for_object_type(obj_type)
    custom_options = dict(
        only_fields=only_fields,
        only_indexed=only_indexed,
        get_symbol_name=get_symbol_name,
    )
    if enum:
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
~~            if not isinstance(orm_field, ColumnProperty):
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
        enum = Enum(name, members)
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


## ... source file continues with no further ColumnProperty examples...

```


## Example 2 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management that is
powered by [SQLAlchemy](/sqlalchemy.html) on the backend. The code
for this project is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / marshmallow.py**](https://github.com/indico/indico/blob/master/indico/core/marshmallow.py)

```python
# marshmallow.py

from __future__ import absolute_import, unicode_literals

from inspect import getmro

from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import SchemaOpts
from marshmallow import fields, post_dump, post_load, pre_load
from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import ModelConverter
from marshmallow_sqlalchemy import ModelSchema as MSQLAModelSchema
~~from sqlalchemy.orm import ColumnProperty
from sqlalchemy.sql.elements import Label
from webargs.flaskparser import parser as webargs_flask_parser

from indico.core import signals
from indico.core.db.sqlalchemy import PyIntEnum, UTCDateTime
from indico.web.args import parser as indico_webargs_flask_parser


mm = Marshmallow()


def _is_column_property(prop):
    return hasattr(prop, 'columns') and isinstance(prop.columns[0], Label)


class IndicoModelConverter(ModelConverter):
    SQLA_TYPE_MAPPING = ModelConverter.SQLA_TYPE_MAPPING.copy()
    SQLA_TYPE_MAPPING.update({
        UTCDateTime: fields.DateTime,
        PyIntEnum: EnumField
    })

    def _get_field_kwargs_for_property(self, prop):
        kwargs = super(IndicoModelConverter, self)._get_field_kwargs_for_property(prop)


## ... source file continues with no further ColumnProperty examples...

```


## Example 3 from sqlalchemy-utils
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

[**sqlalchemy-utils / sqlalchemy_utils / generic.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./generic.py)

```python
# generic.py
from collections.abc import Iterable

import six
import sqlalchemy as sa
from sqlalchemy.ext.hybrid import hybrid_property
~~from sqlalchemy.orm import attributes, class_mapper, ColumnProperty
from sqlalchemy.orm.interfaces import MapperProperty, PropComparator
from sqlalchemy.orm.session import _state_session
from sqlalchemy.util import set_creation_order

from .exceptions import ImproperlyConfigured
from .functions import identity


class GenericAttributeImpl(attributes.ScalarAttributeImpl):
    def get(self, state, dict_, passive=attributes.PASSIVE_OFF):
        if self.key in dict_:
            return dict_[self.key]

        session = _state_session(state)
        if session is None:
            return None

        discriminator = self.get_state_discriminator(state)
        target_class = state.class_._decl_class_registry.get(discriminator)

        if target_class is None:
            return None

        id = self.get_state_id(state)


## ... source file abbreviated to get to ColumnProperty examples ...


            for index, id in enumerate(self.parent_token.id):
                dict_[id.key] = pk[index]
            dict_[self.parent_token.discriminator.key] = discriminator


class GenericRelationshipProperty(MapperProperty):

    def __init__(self, discriminator, id, doc=None):
        super(GenericRelationshipProperty, self).__init__()
        self._discriminator_col = discriminator
        self._id_cols = id
        self._id = None
        self._discriminator = None
        self.doc = doc

        set_creation_order(self)

    def _column_to_property(self, column):
        if isinstance(column, hybrid_property):
            attr_key = column.__name__
            for key, attr in self.parent.all_orm_descriptors.items():
                if key == attr_key:
                    return attr
        else:
            for key, attr in self.parent.attrs.items():
~~                if isinstance(attr, ColumnProperty):
                    if attr.columns[0].name == column.name:
                        return attr

    def init(self):
        def convert_strings(column):
            if isinstance(column, six.string_types):
                return self.parent.columns[column]
            return column

        self._discriminator_col = convert_strings(self._discriminator_col)
        self._id_cols = convert_strings(self._id_cols)

        if isinstance(self._id_cols, Iterable):
            self._id_cols = list(map(convert_strings, self._id_cols))
        else:
            self._id_cols = [self._id_cols]

        self.discriminator = self._column_to_property(self._discriminator_col)

        if self.discriminator is None:
            raise ImproperlyConfigured(
                'Could not find discriminator descriptor.'
            )



## ... source file continues with no further ColumnProperty examples...

```

