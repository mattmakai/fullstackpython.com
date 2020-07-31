title: sqlalchemy.orm attributes Example Code
category: page
slug: sqlalchemy-orm-attributes-examples
sortorder: 500031062
toc: False
sidebartitle: sqlalchemy.orm attributes
meta: Python example code that shows how to use the attributes callable from the sqlalchemy.orm module of the SQLAlchemy project.


`attributes` is a callable within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-load-examples.html">Load</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">Mapper</a>,
<a href="/sqlalchemy-orm-query-examples.html">Query</a>,
<a href="/sqlalchemy-orm-relationshipproperty-examples.html">RelationshipProperty</a>,
<a href="/sqlalchemy-orm-session-examples.html">Session</a>,
<a href="/sqlalchemy-orm-synonymproperty-examples.html">SynonymProperty</a>,
<a href="/sqlalchemy-orm-aliased-examples.html">aliased</a>,
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
~~    def get(self, state, dict_, passive=attributes.PASSIVE_OFF):
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


## ... source file abbreviated to get to attributes examples ...


            self.property = prop
            self._parententity = parentmapper

        def __eq__(self, other):
            discriminator = six.text_type(type(other).__name__)
            q = self.property._discriminator_col == discriminator
            other_id = identity(other)
            for index, id in enumerate(self.property._id_cols):
                q &= id == other_id[index]
            return q

        def __ne__(self, other):
            return -(self == other)

        def is_type(self, other):
            mapper = sa.inspect(other)
            class_names = [six.text_type(other.__name__)]
            class_names.extend([
                six.text_type(submapper.class_.__name__)
                for submapper in mapper._inheriting_mappers
            ])

            return self.property._discriminator_col.in_(class_names)

    def instrument_class(self, mapper):
~~        attributes.register_attribute(
            mapper.class_,
            self.key,
            comparator=self.Comparator(self, mapper),
            parententity=mapper,
            doc=self.doc,
            impl_class=GenericAttributeImpl,
            parent_token=self
        )


def generic_relationship(*args, **kwargs):
    return GenericRelationshipProperty(*args, **kwargs)


        target = session.query(target_class).get(id)

        return target

    def get_state_discriminator(self, state):
        discriminator = self.parent_token.discriminator
        if isinstance(discriminator, hybrid_property):
            return getattr(state.obj(), discriminator.__name__)
        else:
            return state.attrs[discriminator.key].value

    def get_state_id(self, state):
        return tuple(state.attrs[id.key].value for id in self.parent_token.id)

    def set(self, state, dict_, initiator,
~~            passive=attributes.PASSIVE_OFF,
            check_old=None,
            pop=False):

        dict_[self.key] = initiator

        if initiator is None:
            for id in self.parent_token.id:
                dict_[id.key] = None
            dict_[self.parent_token.discriminator.key] = None
        else:
            class_ = type(initiator)
            mapper = class_mapper(class_)

            pk = mapper.identity_key_from_instance(initiator)[1]

            discriminator = six.text_type(class_.__name__)

            for index, id in enumerate(self.parent_token.id):
                dict_[id.key] = pk[index]
            dict_[self.parent_token.discriminator.key] = discriminator


class GenericRelationshipProperty(MapperProperty):



## ... source file continues with no further attributes examples...

```

