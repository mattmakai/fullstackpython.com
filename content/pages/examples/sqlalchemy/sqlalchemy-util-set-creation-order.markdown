title: sqlalchemy.util set_creation_order Example Code
category: page
slug: sqlalchemy-util-set-creation-order-examples
sortorder: 500031151
toc: False
sidebartitle: sqlalchemy.util set_creation_order
meta: Python example code that shows how to use the set_creation_order callable from the sqlalchemy.util module of the SQLAlchemy project.


`set_creation_order` is a callable within the `sqlalchemy.util` module of the SQLAlchemy project.

<a href="/sqlalchemy-util-ordereddict-examples.html">OrderedDict</a>,
<a href="/sqlalchemy-util-orderedset-examples.html">OrderedSet</a>,
<a href="/sqlalchemy-util-symbol-examples.html">symbol</a>,
and <a href="/sqlalchemy-util-topological-examples.html">topological</a>
are several other callables with code examples from the same `sqlalchemy.util` package.

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
from sqlalchemy.orm import attributes, class_mapper, ColumnProperty
from sqlalchemy.orm.interfaces import MapperProperty, PropComparator
from sqlalchemy.orm.session import _state_session
~~from sqlalchemy.util import set_creation_order

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

        target = session.query(target_class).get(id)



## ... source file abbreviated to get to set_creation_order examples ...


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

    def __init__(self, discriminator, id, doc=None):
        super(GenericRelationshipProperty, self).__init__()
        self._discriminator_col = discriminator
        self._id_cols = id
        self._id = None
        self._discriminator = None
        self.doc = doc

~~        set_creation_order(self)

    def _column_to_property(self, column):
        if isinstance(column, hybrid_property):
            attr_key = column.__name__
            for key, attr in self.parent.all_orm_descriptors.items():
                if key == attr_key:
                    return attr
        else:
            for key, attr in self.parent.attrs.items():
                if isinstance(attr, ColumnProperty):
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


## ... source file continues with no further set_creation_order examples...

```

