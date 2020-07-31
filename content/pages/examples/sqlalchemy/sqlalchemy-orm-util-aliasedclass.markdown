title: sqlalchemy.orm.util AliasedClass Example Code
category: page
slug: sqlalchemy-orm-util-aliasedclass-examples
sortorder: 500031093
toc: False
sidebartitle: sqlalchemy.orm.util AliasedClass
meta: Example code for understanding how to use the AliasedClass class from the sqlalchemy.orm.util module of the SQLAlchemy project.


`AliasedClass` is a class within the `sqlalchemy.orm.util` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-util-aliasedinsp-examples.html">AliasedInsp</a>
and
<a href="/sqlalchemy-orm-util-identity-key-examples.html">identity_key</a>
are a couple of other callables within the `sqlalchemy.orm.util` package that also have code examples.

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
~~from sqlalchemy.orm.util import AliasedClass
from sqlalchemy.sql import operators, extract

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


## ... source file abbreviated to get to AliasedClass examples ...


        'month_ne': lambda c, v: extract('month', c) != v,
        'month_gt': lambda c, v: extract('month', c) > v,
        'month_ge': lambda c, v: extract('month', c) >= v,
        'month_lt': lambda c, v: extract('month', c) < v,
        'month_le': lambda c, v: extract('month', c) <= v,

        'day': lambda c, v: extract('day', c) == v,
        'day_ne': lambda c, v: extract('day', c) != v,
        'day_gt': lambda c, v: extract('day', c) > v,
        'day_ge': lambda c, v: extract('day', c) >= v,
        'day_lt': lambda c, v: extract('day', c) < v,
        'day_le': lambda c, v: extract('day', c) <= v,
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
~~        if isinstance(cls_or_alias, AliasedClass):
            mapper, cls = cls_or_alias, inspect(cls_or_alias).mapper.class_
        else:
            mapper = cls = cls_or_alias

        expressions = []
        valid_attributes = cls.filterable_attributes
        for attr, value in filters.items():
            if attr in cls.hybrid_methods:
                method = getattr(cls, attr)
                expressions.append(method(value, mapper=mapper))
            else:
                if OPERATOR_SPLITTER in attr:
                    attr_name, op_name = attr.rsplit(OPERATOR_SPLITTER, 1)
                    if op_name not in cls._operators:
                        raise KeyError('Expression `{}` has incorrect '
                                       'operator `{}`'.format(attr, op_name))
                    op = cls._operators[op_name]
                else:
                    attr_name, op = attr, operators.eq

                if attr_name not in valid_attributes:
                    raise KeyError('Expression `{}` '
                                   'has incorrect attribute `{}`'
                                   .format(attr, attr_name))

                column = getattr(mapper, attr_name)
                expressions.append(op(column, value))

        return expressions

    @classmethod
    def order_expr(cls_or_alias, *columns):
~~        if isinstance(cls_or_alias, AliasedClass):
            mapper, cls = cls_or_alias, inspect(cls_or_alias).mapper.class_
        else:
            mapper = cls = cls_or_alias

        expressions = []
        for attr in columns:
            fn, attr = (desc, attr[1:]) if attr.startswith(DESC_PREFIX) \
                        else (asc, attr)
            if attr not in cls.sortable_attributes:
                raise KeyError('Cant order {} by {}'.format(cls, attr))

            expr = fn(getattr(mapper, attr))
            expressions.append(expr)
        return expressions

    @classmethod
    def smart_query(cls, filters=None, sort_attrs=None, schema=None):
        return smart_query(cls.query, filters, sort_attrs, schema)

    @classmethod
    def where(cls, **filters):
        return cls.smart_query(filters)

    @classmethod


## ... source file continues with no further AliasedClass examples...

```

