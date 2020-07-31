title: sqlalchemy.util symbol Example Code
category: page
slug: sqlalchemy-util-symbol-examples
sortorder: 500031152
toc: False
sidebartitle: sqlalchemy.util symbol
meta: Python example code that shows how to use the symbol callable from the sqlalchemy.util module of the SQLAlchemy project.


`symbol` is a callable within the `sqlalchemy.util` module of the SQLAlchemy project.

<a href="/sqlalchemy-util-ordereddict-examples.html">OrderedDict</a>,
<a href="/sqlalchemy-util-orderedset-examples.html">OrderedSet</a>,
<a href="/sqlalchemy-util-set-creation-order-examples.html">set_creation_order</a>,
and <a href="/sqlalchemy-util-topological-examples.html">topological</a>
are several other callables with code examples from the same `sqlalchemy.util` package.

## Example 1 from SQLAlchemy filters
[SQLAlchemy filters](https://github.com/juliotrigo/sqlalchemy-filters)
         provides filtering, sorting and pagination for [SQLAlchemy](/sqlalchemy.html)
         query objects, which is particularly useful when building
         [web APIs](/application-programming-interfaces.html). SQLAlchemy filters
         is open sourced under the
         [Apache License version 2.0](https://github.com/juliotrigo/sqlalchemy-filters/blob/master/LICENSE).

[**SQLAlchemy filters / sqlalchemy_filters / models.py**](https://github.com/juliotrigo/sqlalchemy-filters/blob/master/sqlalchemy_filters/./models.py)

```python
# models.py
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.mapper import Mapper
~~from sqlalchemy.util import symbol
import types

from .exceptions import BadQuery, FieldNotFound, BadSpec


class Field(object):

    def __init__(self, model, field_name):
        self.model = model
        self.field_name = field_name

    def get_sqlalchemy_field(self):
        if self.field_name not in self._get_valid_field_names():
            raise FieldNotFound(
                'Model {} has no column `{}`.'.format(
                    self.model, self.field_name
                )
            )
        sqlalchemy_field = getattr(self.model, self.field_name)

        if isinstance(sqlalchemy_field, types.MethodType):
            sqlalchemy_field = sqlalchemy_field()

        return sqlalchemy_field

    def _get_valid_field_names(self):
        inspect_mapper = inspect(self.model)
        columns = inspect_mapper.columns
        orm_descriptors = inspect_mapper.all_orm_descriptors

        column_names = columns.keys()
        hybrid_names = [
            key for key, item in orm_descriptors.items()
            if _is_hybrid_property(item) or _is_hybrid_method(item)
        ]

        return set(column_names) | set(hybrid_names)


def _is_hybrid_property(orm_descriptor):
~~    return orm_descriptor.extension_type == symbol('HYBRID_PROPERTY')


def _is_hybrid_method(orm_descriptor):
~~    return orm_descriptor.extension_type == symbol('HYBRID_METHOD')


def get_query_models(query):
    models = [col_desc['entity'] for col_desc in query.column_descriptions]
    models.extend(mapper.class_ for mapper in query._join_entities)

    if (
        hasattr(query, '_select_from_entity') and
        (query._select_from_entity is not None)
    ):
        model_class = (
            query._select_from_entity.class_
            if isinstance(query._select_from_entity, Mapper)  # sqlalchemy>=1.1
            else query._select_from_entity  # sqlalchemy==1.0
        )
        if model_class not in models:
            models.append(model_class)

    return {model.__name__: model for model in models}


def get_model_from_spec(spec, query, default_model=None):
    models = get_query_models(query)
    if not models:


## ... source file continues with no further symbol examples...

```

