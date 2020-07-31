title: sqlalchemy.orm.attributes InstrumentedAttribute Example Code
category: page
slug: sqlalchemy-orm-attributes-instrumentedattribute-examples
sortorder: 500031076
toc: False
sidebartitle: sqlalchemy.orm.attributes InstrumentedAttribute
meta: Example code for understanding how to use the InstrumentedAttribute class from the sqlalchemy.orm.attributes module of the SQLAlchemy project.


`InstrumentedAttribute` is a class within the `sqlalchemy.orm.attributes` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-attributes-queryableattribute-examples.html">QueryableAttribute</a>
and
<a href="/sqlalchemy-orm-attributes-flag-modified-examples.html">flag_modified</a>
are a couple of other callables within the `sqlalchemy.orm.attributes` package that also have code examples.

## Example 1 from SQLAlchemy Mixins
[SQLAlchemy Mixins](https://github.com/absent1706/sqlalchemy-mixins)
([PyPI package information](https://pypi.org/project/sqlalchemy-mixins/))
is a collection of
[mixins](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
useful for extending [SQLAlchemy](/sqlalchemy.html) and simplifying
your [database](/databases.html)-interacting code for some common
use cases. SQLAlchemy Mixins is open sourced under the
[MIT license](https://github.com/absent1706/sqlalchemy-mixins/blob/master/LICENSE.txt).

[**SQLAlchemy Mixins / sqlalchemy_mixins / eagerload.py**](https://github.com/absent1706/sqlalchemy-mixins/blob/master/sqlalchemy_mixins/./eagerload.py)

```python
# eagerload.py
try:
    from typing import List
except ImportError: # pragma: no cover
    pass

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import subqueryload
~~from sqlalchemy.orm.attributes import InstrumentedAttribute

from .session import SessionMixin

JOINED = 'joined'
SUBQUERY = 'subquery'


def eager_expr(schema):
    flat_schema = _flatten_schema(schema)
    return _eager_expr_from_flat_schema(flat_schema)


def _flatten_schema(schema):
    def _flatten(schema, parent_path, result):
        for path, value in schema.items():
~~            if isinstance(path, InstrumentedAttribute):
                path = path.key

            if isinstance(value, tuple):
                join_method, inner_schema = value[0], value[1]
            elif isinstance(value, dict):
                join_method, inner_schema = JOINED, value
            else:
                join_method, inner_schema = value, None

            full_path = parent_path + '.' + path if parent_path else path
            result[full_path] = join_method

            if inner_schema:
                _flatten(inner_schema, full_path, result)

    result = {}
    _flatten(schema, '', result)
    return result


def _eager_expr_from_flat_schema(flat_schema):
    result = []
    for path, join_method in flat_schema.items():
        if join_method == JOINED:


## ... source file continues with no further InstrumentedAttribute examples...

```


## Example 2 from sqlalchemy-utils
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


## Example 3 from WTForms-Alchemy
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

[**WTForms-Alchemy / wtforms_alchemy / validators.py**](https://github.com/kvesteri/wtforms-alchemy/blob/master/wtforms_alchemy/./validators.py)

```python
# validators.py
from collections.abc import Iterable, Mapping

import six
from sqlalchemy import Column
~~from sqlalchemy.orm.attributes import InstrumentedAttribute
from wtforms import ValidationError


class Unique(object):
    field_flags = ('unique', )

    def __init__(self, column, get_session=None, message=None):
        self.column = column
        self.message = message
        self.get_session = get_session

    @property
    def query(self):
        self._check_for_session(self.model)
        if self.get_session:
            return self.get_session().query(self.model)
        elif hasattr(self.model, 'query'):
            return getattr(self.model, 'query')
        else:
            raise Exception(
                'Validator requires either get_session or Flask-SQLAlchemy'
                ' styled query parameter'
            )



## ... source file continues with no further InstrumentedAttribute examples...

```

