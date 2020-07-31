title: sqlalchemy.orm aliased Example Code
category: page
slug: sqlalchemy-orm-aliased-examples
sortorder: 500031061
toc: False
sidebartitle: sqlalchemy.orm aliased
meta: Python example code that shows how to use the aliased callable from the sqlalchemy.orm module of the SQLAlchemy project.


`aliased` is a callable within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-load-examples.html">Load</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">Mapper</a>,
<a href="/sqlalchemy-orm-query-examples.html">Query</a>,
<a href="/sqlalchemy-orm-relationshipproperty-examples.html">RelationshipProperty</a>,
<a href="/sqlalchemy-orm-session-examples.html">Session</a>,
<a href="/sqlalchemy-orm-synonymproperty-examples.html">SynonymProperty</a>,
<a href="/sqlalchemy-orm-attributes-examples.html">attributes</a>,
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
~~from sqlalchemy.orm import aliased, contains_eager
from sqlalchemy.orm.util import AliasedClass
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
        path = entity_path + RELATION_SPLITTER + relation_name \
               if entity_path else relation_name
        if relation_name not in entity.relations:
            raise KeyError("Incorrect path `{}`: "
                           "{} doesnt have `{}` relationship "
                           .format(path, entity, relation_name))
        relationship = getattr(entity, relation_name)
~~        alias = aliased(relationship.property.mapper.class_)
        aliases[path] = alias, relationship
        _parse_path_and_make_aliases(alias, path, nested_attrs, aliases)


def smart_query(query, filters=None, sort_attrs=None, schema=None):
    if not filters:
        filters = {}
    if not sort_attrs:
        sort_attrs = []
    if not schema:
        schema = {}

    root_cls = query._entity_zero().class_  # for example, User or Post
    attrs = list(filters.keys()) + \
        list(map(lambda s: s.lstrip(DESC_PREFIX), sort_attrs))
    aliases = OrderedDict({})
    _parse_path_and_make_aliases(root_cls, '', attrs, aliases)

    loaded_paths = []
    for path, al in aliases.items():
        relationship_path = path.replace(RELATION_SPLITTER, '.')
        query = query.outerjoin(al[0], al[1]) \
            .options(contains_eager(relationship_path, alias=al[0]))
        loaded_paths.append(relationship_path)


## ... source file continues with no further aliased examples...

```

