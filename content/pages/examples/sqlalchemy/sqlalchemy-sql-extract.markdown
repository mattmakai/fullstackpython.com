title: sqlalchemy.sql extract Example Code
category: page
slug: sqlalchemy-sql-extract-examples
sortorder: 500031111
toc: False
sidebartitle: sqlalchemy.sql extract
meta: Python example code that shows how to use the extract callable from the sqlalchemy.sql module of the SQLAlchemy project.


`extract` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
<a href="/sqlalchemy-sql-functions-examples.html">functions</a>,
<a href="/sqlalchemy-sql-operators-examples.html">operators</a>,
<a href="/sqlalchemy-sql-schema-examples.html">schema</a>,
<a href="/sqlalchemy-sql-select-examples.html">select</a>,
<a href="/sqlalchemy-sql-sqltypes-examples.html">sqltypes</a>,
and <a href="/sqlalchemy-sql-table-examples.html">table</a>
are several other callables with code examples from the same `sqlalchemy.sql` package.

## Example 1 from SQLAlchemy Mixins
[SQLAlchemy Mixins](https://github.com/absent1706/sqlalchemy-mixins)
([PyPI package information](https://pypi.org/project/sqlalchemy-mixins/))
is a collection of
[mixins](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
useful for extending [SQLAlchemy](/sqlalchemy.html) and simplifying
your [database](/databases.html)-interacting code for some common
use cases. SQLAlchemy Mixins is open sourced under the
[MIT license](https://github.com/absent1706/sqlalchemy-mixins/blob/master/LICENSE.txt).

[**SQLAlchemy Mixins / sqlalchemy_mixins / smartquery.py**](https://github.com/absent1706/sqlalchemy-mixins/blob/master/sqlalchemy_mixins/./smartquery.py)

```python
# smartquery.py
try:
    from typing import List
except ImportError:  # pragma: no cover
    pass

from collections import OrderedDict

import sqlalchemy
from sqlalchemy import asc, desc, inspect
from sqlalchemy.orm import aliased, contains_eager
from sqlalchemy.orm.util import AliasedClass
~~from sqlalchemy.sql import operators, extract

from .eagerload import _flatten_schema, _eager_expr_from_flat_schema, \
    EagerLoadMixin
from .inspection import InspectionMixin
from .utils import classproperty

RELATION_SPLITTER = '___'
OPERATOR_SPLITTER = '__'

DESC_PREFIX = '-'


def _parse_path_and_make_aliases(entity, entity_path, attrs, aliases):
    relations = {}
    for attr in attrs:
        if RELATION_SPLITTER in attr:
            relation_name, nested_attr = attr.split(RELATION_SPLITTER, 1)
            if relation_name in relations:
                relations[relation_name].append(nested_attr)
            else:
                relations[relation_name] = [nested_attr]

    for relation_name, nested_attrs in relations.items():
        path = entity_path + RELATION_SPLITTER + relation_name \


## ... source file abbreviated to get to extract examples ...


class SmartQueryMixin(InspectionMixin, EagerLoadMixin):
    __abstract__ = True

    _operators = {
        'isnull': lambda c, v: (c == None) if v else (c != None),
        'exact': operators.eq,
        'ne': operators.ne,  # not equal or is not (for None)

        'gt': operators.gt,  # greater than , >
        'ge': operators.ge,  # greater than or equal, >=
        'lt': operators.lt,  # lower than, <
        'le': operators.le,  # lower than or equal, <=

        'in': operators.in_op,
        'notin': operators.notin_op,
        'between': lambda c, v: c.between(v[0], v[1]),

        'like': operators.like_op,
        'ilike': operators.ilike_op,
        'startswith': operators.startswith_op,
        'istartswith': lambda c, v: c.ilike(v + '%'),
        'endswith': operators.endswith_op,
        'iendswith': lambda c, v: c.ilike('%' + v),
        'contains': lambda c, v: c.ilike('%{v}%'.format(v=v)),

~~        'year': lambda c, v: extract('year', c) == v,
~~        'year_ne': lambda c, v: extract('year', c) != v,
~~        'year_gt': lambda c, v: extract('year', c) > v,
~~        'year_ge': lambda c, v: extract('year', c) >= v,
~~        'year_lt': lambda c, v: extract('year', c) < v,
~~        'year_le': lambda c, v: extract('year', c) <= v,

~~        'month': lambda c, v: extract('month', c) == v,
~~        'month_ne': lambda c, v: extract('month', c) != v,
~~        'month_gt': lambda c, v: extract('month', c) > v,
~~        'month_ge': lambda c, v: extract('month', c) >= v,
~~        'month_lt': lambda c, v: extract('month', c) < v,
~~        'month_le': lambda c, v: extract('month', c) <= v,

~~        'day': lambda c, v: extract('day', c) == v,
~~        'day_ne': lambda c, v: extract('day', c) != v,
~~        'day_gt': lambda c, v: extract('day', c) > v,
~~        'day_ge': lambda c, v: extract('day', c) >= v,
~~        'day_lt': lambda c, v: extract('day', c) < v,
~~        'day_le': lambda c, v: extract('day', c) <= v,
    }

    @classproperty
    def filterable_attributes(cls):
        return cls.relations + cls.columns + \
               cls.hybrid_properties + cls.hybrid_methods

    @classproperty
    def sortable_attributes(cls):
        return cls.columns + cls.hybrid_properties

    @classmethod
    def filter_expr(cls_or_alias, **filters):
        if isinstance(cls_or_alias, AliasedClass):
            mapper, cls = cls_or_alias, inspect(cls_or_alias).mapper.class_
        else:
            mapper = cls = cls_or_alias

        expressions = []
        valid_attributes = cls.filterable_attributes
        for attr, value in filters.items():
            if attr in cls.hybrid_methods:
                method = getattr(cls, attr)
                expressions.append(method(value, mapper=mapper))


## ... source file continues with no further extract examples...

```

