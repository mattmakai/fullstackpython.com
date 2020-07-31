title: sqlalchemy.util.langhelpers symbol Example Code
category: page
slug: sqlalchemy-util-langhelpers-symbol-examples
sortorder: 500031155
toc: False
sidebartitle: sqlalchemy.util.langhelpers symbol
meta: Python example code that shows how to use the symbol callable from the sqlalchemy.util.langhelpers module of the SQLAlchemy project.


`symbol` is a callable within the `sqlalchemy.util.langhelpers` module of the SQLAlchemy project.

<a href="/sqlalchemy-util-langhelpers-public-factory-examples.html">public_factory</a>
is another callable from the `sqlalchemy.util.langhelpers` package with code examples.

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

[**sqlalchemy-utils / sqlalchemy_utils / models.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./models.py)

```python
# models.py
from datetime import datetime

import sqlalchemy as sa
~~from sqlalchemy.util.langhelpers import symbol


class Timestamp(object):

    created = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)


@sa.event.listens_for(Timestamp, 'before_update', propagate=True)
def timestamp_before_update(mapper, connection, target):
    target.updated = datetime.utcnow()


~~NO_VALUE = symbol('NO_VALUE')
NOT_LOADED_REPR = '<not loaded>'


def _generic_repr_method(self, fields):
    state = sa.inspect(self)
    field_reprs = []
    if not fields:
        fields = state.mapper.columns.keys()
    for key in fields:
        value = state.attrs[key].loaded_value
        if value == NO_VALUE:
            value = NOT_LOADED_REPR
        else:
            value = repr(value)
        field_reprs.append('='.join((key, value)))

    return '%s(%s)' % (self.__class__.__name__, ', '.join(field_reprs))


def generic_repr(*fields):
    if len(fields) == 1 and callable(fields[0]):
        target = fields[0]
        target.__repr__ = lambda self: _generic_repr_method(self, fields=None)
        return target


## ... source file continues with no further symbol examples...

```

