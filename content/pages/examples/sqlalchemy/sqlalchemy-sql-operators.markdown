title: sqlalchemy.sql operators Example Code
category: page
slug: sqlalchemy-sql-operators-examples
sortorder: 500031113
toc: False
sidebartitle: sqlalchemy.sql operators
meta: Python example code that shows how to use the operators callable from the sqlalchemy.sql module of the SQLAlchemy project.


`operators` is a callable within the `sqlalchemy.sql` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-clauseelement-examples.html">ClauseElement</a>,
<a href="/sqlalchemy-sql-select-examples.html">Select</a>,
<a href="/sqlalchemy-sql-column-examples.html">column</a>,
<a href="/sqlalchemy-sql-expression-examples.html">expression</a>,
<a href="/sqlalchemy-sql-extract-examples.html">extract</a>,
<a href="/sqlalchemy-sql-functions-examples.html">functions</a>,
<a href="/sqlalchemy-sql-schema-examples.html">schema</a>,
<a href="/sqlalchemy-sql-select-examples.html">select</a>,
<a href="/sqlalchemy-sql-sqltypes-examples.html">sqltypes</a>,
and <a href="/sqlalchemy-sql-table-examples.html">table</a>
are several other callables with code examples from the same `sqlalchemy.sql` package.

## Example 1 from GeoAlchemy2
[GeoAlchemy2](https://github.com/geoalchemy/geoalchemy2)
([project documentation](https://geoalchemy-2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/GeoAlchemy2/))
extends [SQLAlchemy](/sqlalchemy.html) with new data types for working
with geospatial databases, particularly [PostGIS](http://postgis.net/),
which is a spatial database extender for [PostgreSQL](/postgresql.html).
The project is provided as open source under the
[MIT license](https://github.com/geoalchemy/geoalchemy2/blob/master/COPYING.rst).

[**GeoAlchemy2 / geoalchemy2 / comparator.py**](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/./comparator.py)

```python
# comparator.py

from sqlalchemy import types as sqltypes
from sqlalchemy.types import UserDefinedType
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
~~from sqlalchemy.sql import operators
try:
    from sqlalchemy.sql.functions import _FunctionGenerator
except ImportError:  # SQLA < 0.9  # pragma: no cover
    from sqlalchemy.sql.expression import _FunctionGenerator


~~INTERSECTS = operators.custom_op('&&')
~~OVERLAPS_OR_TO_LEFT = operators.custom_op('&<')
~~OVERLAPS_OR_TO_RIGHT = operators.custom_op('&>')
~~OVERLAPS_OR_BELOW = operators.custom_op('&<|')
~~TO_LEFT = operators.custom_op('<<')
~~BELOW = operators.custom_op('<<|')
~~TO_RIGHT = operators.custom_op('>>')
~~CONTAINED = operators.custom_op('@')
~~OVERLAPS_OR_ABOVE = operators.custom_op('|&>')
~~ABOVE = operators.custom_op('|>>')
~~CONTAINS = operators.custom_op('-')
~~SAME = operators.custom_op('-=')
~~DISTANCE_CENTROID = operators.custom_op('<->')
~~DISTANCE_BOX = operators.custom_op('<#>')


class BaseComparator(UserDefinedType.Comparator):

    key = None

    def __getattr__(self, name):


        if not name.lower().startswith('st_'):
            raise AttributeError


        func_ = _FunctionGenerator(expr=self.expr)
        return getattr(func_, name)

    def intersects(self, other):
        return self.operate(INTERSECTS, other, result_type=sqltypes.Boolean)

    def overlaps_or_to_left(self, other):
        return self.operate(OVERLAPS_OR_TO_LEFT, other,
                            result_type=sqltypes.Boolean)

    def overlaps_or_to_right(self, other):


## ... source file continues with no further operators examples...

```


## Example 2 from SQLAlchemy Mixins
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


## ... source file abbreviated to get to operators examples ...


                attr = attr.lstrip(DESC_PREFIX)
            parts = attr.rsplit(RELATION_SPLITTER, 1)
            entity, attr_name = aliases[parts[0]][0], prefix + parts[1]
        else:
            entity, attr_name = root_cls, attr
        try:
            query = query.order_by(*entity.order_expr(attr_name))
        except KeyError as e:
            raise KeyError("Incorrect order path `{}`: {}".format(attr, e))

    if schema:
        flat_schema = _flatten_schema(schema)
        not_loaded_part = {path: v for path, v in flat_schema.items()
                           if path not in loaded_paths}
        query = query.options(*_eager_expr_from_flat_schema(
            not_loaded_part))

    return query


class SmartQueryMixin(InspectionMixin, EagerLoadMixin):
    __abstract__ = True

    _operators = {
        'isnull': lambda c, v: (c == None) if v else (c != None),
~~        'exact': operators.eq,
~~        'ne': operators.ne,  # not equal or is not (for None)

~~        'gt': operators.gt,  # greater than , >
~~        'ge': operators.ge,  # greater than or equal, >=
~~        'lt': operators.lt,  # lower than, <
~~        'le': operators.le,  # lower than or equal, <=

~~        'in': operators.in_op,
~~        'notin': operators.notin_op,
        'between': lambda c, v: c.between(v[0], v[1]),

~~        'like': operators.like_op,
~~        'ilike': operators.ilike_op,
~~        'startswith': operators.startswith_op,
        'istartswith': lambda c, v: c.ilike(v + '%'),
~~        'endswith': operators.endswith_op,
        'iendswith': lambda c, v: c.ilike('%' + v),
        'contains': lambda c, v: c.ilike('%{v}%'.format(v=v)),

        'year': lambda c, v: extract('year', c) == v,
        'year_ne': lambda c, v: extract('year', c) != v,
        'year_gt': lambda c, v: extract('year', c) > v,
        'year_ge': lambda c, v: extract('year', c) >= v,
        'year_lt': lambda c, v: extract('year', c) < v,
        'year_le': lambda c, v: extract('year', c) <= v,

        'month': lambda c, v: extract('month', c) == v,
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


## ... source file abbreviated to get to operators examples ...


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
            else:
                if OPERATOR_SPLITTER in attr:
                    attr_name, op_name = attr.rsplit(OPERATOR_SPLITTER, 1)
                    if op_name not in cls._operators:
                        raise KeyError('Expression `{}` has incorrect '
                                       'operator `{}`'.format(attr, op_name))
                    op = cls._operators[op_name]
                else:
~~                    attr_name, op = attr, operators.eq

                if attr_name not in valid_attributes:
                    raise KeyError('Expression `{}` '
                                   'has incorrect attribute `{}`'
                                   .format(attr, attr_name))

                column = getattr(mapper, attr_name)
                expressions.append(op(column, value))

        return expressions

    @classmethod
    def order_expr(cls_or_alias, *columns):
        if isinstance(cls_or_alias, AliasedClass):
            mapper, cls = cls_or_alias, inspect(cls_or_alias).mapper.class_
        else:
            mapper = cls = cls_or_alias

        expressions = []
        for attr in columns:
            fn, attr = (desc, attr[1:]) if attr.startswith(DESC_PREFIX) \
                        else (asc, attr)
            if attr not in cls.sortable_attributes:
                raise KeyError('Cant order {} by {}'.format(cls, attr))


## ... source file continues with no further operators examples...

```

