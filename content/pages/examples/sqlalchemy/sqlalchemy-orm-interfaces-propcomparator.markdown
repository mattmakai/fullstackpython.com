title: sqlalchemy.orm.interfaces PropComparator Example Code
category: page
slug: sqlalchemy-orm-interfaces-propcomparator-examples
sortorder: 500031084
toc: False
sidebartitle: sqlalchemy.orm.interfaces PropComparator
meta: Example code for understanding how to use the PropComparator class from the sqlalchemy.orm.interfaces module of the SQLAlchemy project.


`PropComparator` is a class within the `sqlalchemy.orm.interfaces` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-interfaces-mapperproperty-examples.html">MapperProperty</a>
is another callable from the `sqlalchemy.orm.interfaces` package with code examples.

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
~~from sqlalchemy.orm.interfaces import MapperProperty, PropComparator
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



## ... source file abbreviated to get to PropComparator examples ...


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

        self.id = list(map(self._column_to_property, self._id_cols))

~~    class Comparator(PropComparator):
        def __init__(self, prop, parentmapper):
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


## ... source file continues with no further PropComparator examples...

```

