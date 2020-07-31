title: sqlalchemy.orm Load Example Code
category: page
slug: sqlalchemy-orm-load-examples
sortorder: 500031056
toc: False
sidebartitle: sqlalchemy.orm Load
meta: Example code for understanding how to use the Load class from the sqlalchemy.orm module of the SQLAlchemy project.


`Load` is a class within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">Mapper</a>,
<a href="/sqlalchemy-orm-query-examples.html">Query</a>,
<a href="/sqlalchemy-orm-relationshipproperty-examples.html">RelationshipProperty</a>,
<a href="/sqlalchemy-orm-session-examples.html">Session</a>,
<a href="/sqlalchemy-orm-synonymproperty-examples.html">SynonymProperty</a>,
<a href="/sqlalchemy-orm-aliased-examples.html">aliased</a>,
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

## Example 1 from SQLAlchemy filters
[SQLAlchemy filters](https://github.com/juliotrigo/sqlalchemy-filters)
         provides filtering, sorting and pagination for [SQLAlchemy](/sqlalchemy.html)
         query objects, which is particularly useful when building
         [web APIs](/application-programming-interfaces.html). SQLAlchemy filters
         is open sourced under the
         [Apache License version 2.0](https://github.com/juliotrigo/sqlalchemy-filters/blob/master/LICENSE).

[**SQLAlchemy filters / sqlalchemy_filters / loads.py**](https://github.com/juliotrigo/sqlalchemy-filters/blob/master/sqlalchemy_filters/./loads.py)

```python
# loads.py
~~from sqlalchemy.orm import Load

from .exceptions import BadLoadFormat
from .models import Field, auto_join, get_model_from_spec, get_default_model


class LoadOnly(object):

    def __init__(self, load_spec):
        self.load_spec = load_spec

        try:
            field_names = load_spec['fields']
        except KeyError:
            raise BadLoadFormat('`fields` is a mandatory attribute.')
        except TypeError:
            raise BadLoadFormat(
                'Load spec `{}` should be a dictionary.'.format(load_spec)
            )

        self.field_names = field_names

    def get_named_models(self):
        if "model" in self.load_spec:
            return {self.load_spec['model']}
        return set()

    def format_for_sqlalchemy(self, query, default_model):
        load_spec = self.load_spec
        field_names = self.field_names

        model = get_model_from_spec(load_spec, query, default_model)
        fields = [Field(model, field_name) for field_name in field_names]

~~        return Load(model).load_only(
            *[field.get_sqlalchemy_field() for field in fields]
        )


def get_named_models(loads):
    models = set()
    for load in loads:
        models.update(load.get_named_models())
    return models


def apply_loads(query, load_spec):
    if (
        isinstance(load_spec, list) and
        all(map(lambda item: isinstance(item, str), load_spec))
    ):
        load_spec = {'fields': load_spec}

    if isinstance(load_spec, dict):
        load_spec = [load_spec]

    loads = [LoadOnly(item) for item in load_spec]

    default_model = get_default_model(query)


## ... source file continues with no further Load examples...

```

