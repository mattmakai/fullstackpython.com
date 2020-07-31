title: sqlalchemy.orm.properties ColumnProperty Example Code
category: page
slug: sqlalchemy-orm-properties-columnproperty-examples
sortorder: 500031086
toc: False
sidebartitle: sqlalchemy.orm.properties ColumnProperty
meta: Example code for understanding how to use the ColumnProperty class from the sqlalchemy.orm.properties module of the SQLAlchemy project.


`ColumnProperty` is a class within the `sqlalchemy.orm.properties` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-properties-relationshipproperty-examples.html">RelationshipProperty</a>
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

~~    if isinstance(expr, ColumnProperty):
        return expr.columns[0].type
    elif isinstance(expr, RelationshipProperty):
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


## ... source file abbreviated to get to ColumnProperty examples ...


        return [mixed.table]
    elif isinstance(mixed, sa.orm.attributes.InstrumentedAttribute):
        return mixed.parent.tables
    elif isinstance(mixed, sa.orm.query._ColumnEntity):
        mixed = mixed.expr

    mapper = get_mapper(mixed)

    polymorphic_mappers = get_polymorphic_mappers(mapper)
    if polymorphic_mappers:
        tables = sum((m.tables for m in polymorphic_mappers), [])
    else:
        tables = mapper.tables
    return tables


def get_columns(mixed):
    if isinstance(mixed, sa.sql.selectable.Selectable):
        return mixed.c
    if isinstance(mixed, sa.orm.util.AliasedClass):
        return sa.inspect(mixed).mapper.columns
    if isinstance(mixed, sa.orm.Mapper):
        return mixed.columns
    if isinstance(mixed, InstrumentedAttribute):
        return mixed.property.columns
~~    if isinstance(mixed, ColumnProperty):
        return mixed.columns
    if isinstance(mixed, sa.Column):
        return [mixed]
    if not isclass(mixed):
        mixed = mixed.__class__
    return sa.inspect(mixed).columns


def table_name(obj):
    class_ = getattr(obj, 'class_', obj)

    try:
        return class_.__tablename__
    except AttributeError:
        pass

    try:
        return class_.__table__.name
    except AttributeError:
        pass


def getattrs(obj, attrs):
    return map(partial(getattr, obj), attrs)


## ... source file abbreviated to get to ColumnProperty examples ...


def get_query_descriptor(query, entity, attr):
    if attr in query_labels(query):
        return attr
    else:
        entity = get_query_entity_by_alias(query, entity)
        if entity:
            descriptor = get_descriptor(entity, attr)
            if (
                hasattr(descriptor, 'property') and
                isinstance(descriptor.property, sa.orm.RelationshipProperty)
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
~~            if isinstance(prop, ColumnProperty):
                if isinstance(entity, sa.orm.util.AliasedClass):
                    for c in mapper.selectable.c:
                        if c.key == attr:
                            return c
                else:
                    return getattr(prop.parent.class_, attr)
            else:

                if isinstance(entity, sa.orm.util.AliasedClass):
                    return getattr(entity, attr)
                try:
                    return getattr(mapper.class_, attr)
                except AttributeError:
                    pass


def get_all_descriptors(expr):
    if isinstance(expr, sa.sql.selectable.Selectable):
        return expr.c
    insp = sa.inspect(expr)
    try:
        polymorphic_mappers = get_polymorphic_mappers(insp)
    except sa.exc.NoInspectionAvailable:
        return get_mapper(expr).all_orm_descriptors


## ... source file continues with no further ColumnProperty examples...

```


## Example 2 from WTForms-Alchemy
[wtforms-alchemy](git@github.com:kvesteri/wtforms-alchemy.git)
([documentation](https://wtforms-alchemy.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/WTForms-Alchemy/))
is a [WTForms](https://wtforms.readthedocs.io/en/2.2.1/) extension toolkit
for easier creation of [SQLAlchemy](/sqlalchemy.html) model based forms.
While this project primarily focuses on proper form handling, it also
has many good examples of how to use various parts of SQLAlchemy in
its code base. The project is provided as open source under the
[MIT license](https://github.com/kvesteri/wtforms-alchemy/blob/master/LICENSE).

[**WTForms-Alchemy / wtforms_alchemy / generator.py**](https://github.com/kvesteri/wtforms-alchemy/blob/master/wtforms_alchemy/./generator.py)

```python
# generator.py
import inspect
from collections import OrderedDict
from decimal import Decimal
from enum import Enum

import six
import sqlalchemy as sa
~~from sqlalchemy.orm.properties import ColumnProperty
from sqlalchemy_utils import types
from wtforms import (
    BooleanField,
    Field,
    FloatField,
    PasswordField,
    TextAreaField
)
from wtforms.widgets import CheckboxInput, TextArea
from wtforms_components import (
    ColorField,
    DateField,
    DateIntervalField,
    DateTimeField,
    DateTimeIntervalField,
    DateTimeLocalField,
    DecimalField,
    DecimalIntervalField,
    EmailField,
    IntegerField,
    IntIntervalField,
    SelectField,
    StringField,
    TimeField


## ... source file abbreviated to get to ColumnProperty examples ...



    WIDGET_MAP = OrderedDict((
        (BooleanField, CheckboxInput),
        (ColorField, ColorInput),
        (DateField, DateInput),
        (DateTimeField, DateTimeInput),
        (DateTimeLocalField, DateTimeLocalInput),
        (DecimalField, NumberInput),
        (EmailField, EmailInput),
        (FloatField, NumberInput),
        (IntegerField, NumberInput),
        (TextAreaField, TextArea),
        (TimeField, TimeInput),
        (StringField, TextInput)
    ))

    def __init__(self, form_class):
        self.form_class = form_class
        self.model_class = self.form_class.Meta.model
        self.meta = self.form_class.Meta
        self.TYPE_MAP.update(self.form_class.Meta.type_map)

    def create_form(self, form):
        attrs = OrderedDict()
        for key, property_ in sa.inspect(self.model_class).attrs.items():
~~            if not isinstance(property_, ColumnProperty):
                continue
            if self.skip_column_property(property_):
                continue
            attrs[key] = property_

        for attr in translated_attributes(self.model_class):
            attrs[attr.key] = attr.property

        return self.create_fields(form, self.filter_attributes(attrs))

    def filter_attributes(self, attrs):
        if self.meta.only:
            attrs = OrderedDict([
                (key, prop)
                for key, prop in map(self.validate_attribute, self.meta.only)
                if key
            ])
        else:
            if self.meta.include:
                attrs.update([
                    (key, prop)
                    for key, prop
                    in map(self.validate_attribute, self.meta.include)
                    if key


## ... source file abbreviated to get to ColumnProperty examples ...



            if self.meta.exclude:
                for key in self.meta.exclude:
                    try:
                        del attrs[key]
                    except KeyError:
                        if self.meta.attr_errors:
                            raise InvalidAttributeException(key)
        return attrs

    def validate_attribute(self, attr_name):
        try:
            attr = getattr(self.model_class, attr_name)
        except AttributeError:
            try:
                translation_class = (
                    self.model_class.__translatable__['class']
                )
                attr = getattr(translation_class, attr_name)
            except AttributeError:
                if self.meta.attr_errors:
                    raise InvalidAttributeException(attr_name)
                else:
                    return None, None
        try:
~~            if not isinstance(attr.property, ColumnProperty):
                if self.meta.attr_errors:
                    raise InvalidAttributeException(attr_name)
                else:
                    return None, None
        except AttributeError:
            raise AttributeTypeException(attr_name)
        return attr_name, attr.property

    def create_fields(self, form, properties):
        for key, prop in properties.items():
            column = prop.columns[0]
            try:
                field = self.create_field(prop, column)
            except UnknownTypeException:
                if not self.meta.skip_unknown_types:
                    raise
                else:
                    continue

            if not hasattr(form, key):
                setattr(form, key, field)

    def skip_column_property(self, column_property):
        if column_property._is_polymorphic_discriminator:


## ... source file continues with no further ColumnProperty examples...

```

