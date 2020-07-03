title: sqlalchemy.orm.attributes InstrumentedAttribute code examples
category: page
slug: sqlalchemy-orm-attributes-instrumentedattribute-examples
sortorder: 500031058
toc: False
sidebartitle: sqlalchemy.orm.attributes InstrumentedAttribute
meta: Python example code for the InstrumentedAttribute class from the sqlalchemy.orm.attributes module of the SQLAlchemy project.


InstrumentedAttribute is a class within the sqlalchemy.orm.attributes module of the SQLAlchemy project.


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

[**sqlalchemy-utils / sqlalchemy_utils / path.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./path.py)

```python
# path.py
import sqlalchemy as sa
~~from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.util.langhelpers import symbol

from .utils import str_coercible


@str_coercible
class Path(object):
    def __init__(self, path, separator='.'):
        if isinstance(path, Path):
            self.path = path.path
        else:
            self.path = path
        self.separator = separator

    @property
    def parts(self):
        return self.path.split(self.separator)

    def __iter__(self):
        for part in self.parts:
            yield part

    def __len__(self):
        return len(self.parts)


## ... source file abbreviated to get to InstrumentedAttribute examples ...


        return "%s('%s')" % (self.__class__.__name__, self.path)

    def index(self, element):
        return self.parts.index(element)

    def __getitem__(self, slice):
        result = self.parts[slice]
        if isinstance(result, list):
            return self.__class__(
                self.separator.join(result),
                separator=self.separator
            )
        return result

    def __eq__(self, other):
        return self.path == other.path and self.separator == other.separator

    def __ne__(self, other):
        return not (self == other)

    def __unicode__(self):
        return self.path


def get_attr(mixed, attr):
~~    if isinstance(mixed, InstrumentedAttribute):
        return getattr(
            mixed.property.mapper.class_,
            attr
        )
    else:
        return getattr(mixed, attr)


@str_coercible
class AttrPath(object):
    def __init__(self, class_, path):
        self.class_ = class_
        self.path = Path(path)
        self.parts = []
        last_attr = class_
        for value in self.path:
            last_attr = get_attr(last_attr, value)
            self.parts.append(last_attr)

    def __iter__(self):
        for part in self.parts:
            yield part

    def __invert__(self):


## ... source file continues with no further InstrumentedAttribute examples...

```

