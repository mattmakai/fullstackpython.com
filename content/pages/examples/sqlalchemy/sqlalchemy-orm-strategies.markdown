title: sqlalchemy.orm strategies code examples
category: page
slug: sqlalchemy-orm-strategies-examples
sortorder: 500031055
toc: False
sidebartitle: sqlalchemy.orm strategies
meta: Python example code for the strategies callable from the sqlalchemy.orm module of the SQLAlchemy project.


strategies is a callable within the sqlalchemy.orm module of the SQLAlchemy project.


## Example 1 from graphene-sqlalchemy
[graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy)
([project documentation](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/)
and
[PyPI package information](https://pypi.org/project/graphene-sqlalchemy/))
is a [SQLAlchemy](/sqlalchemy.html) integration for
[Graphene](https://graphene-python.org/), which makes it easier to build
GraphQL-based [APIs](/application-programming-interfaces.html) into Python
[web applications](/web-development.html). The package allows you to
subclass SQLAlchemy classes and build queries around them with custom
code to match the backend queries with the GraphQL-based request queries.
The project is provided as open source under the
[MIT license](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/LICENSE.md).

[**graphene-sqlalchemy / graphene_sqlalchemy / batching.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./batching.py)

```python
# batching.py
import sqlalchemy
from promise import dataloader, promise
~~from sqlalchemy.orm import Session, strategies
from sqlalchemy.orm.query import QueryContext


def get_batch_resolver(relationship_prop):

~~    selectin_loader = strategies.SelectInLoader(relationship_prop, (('lazy', 'selectin'),))

    class RelationshipLoader(dataloader.DataLoader):
        cache = False

        def batch_load_fn(self, parents):  # pylint: disable=method-hidden
            child_mapper = relationship_prop.mapper
            parent_mapper = relationship_prop.parent
            session = Session.object_session(parents[0])

            for parent in parents:
                assert session is Session.object_session(parent)
                assert parent not in session.dirty

            states = [(sqlalchemy.inspect(parent), True) for parent in parents]

            query_context = QueryContext(session.query(parent_mapper.entity))

            selectin_loader._load_for_path(
                query_context,
                parent_mapper._path_registry,
                states,
                None,
                child_mapper,
            )


## ... source file continues with no further strategies examples...

```

