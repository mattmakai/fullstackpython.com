title: sqlalchemy.orm session code examples
category: page
slug: sqlalchemy-orm-session-examples
sortorder: 500031053
toc: False
sidebartitle: sqlalchemy.orm session
meta: Python example code for the session callable from the sqlalchemy.orm module of the SQLAlchemy project.


session is a callable within the sqlalchemy.orm module of the SQLAlchemy project.


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

[**graphene-sqlalchemy / graphene_sqlalchemy / tests / conftest.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/tests/conftest.py)

```python
# conftest.py
import pytest
from sqlalchemy import create_engine
~~from sqlalchemy.orm import sessionmaker

import graphene

from ..converter import convert_sqlalchemy_composite
from ..registry import reset_global_registry
from .models import Base, CompositeFullName

test_db_url = 'sqlite://'  # use in-memory database for tests


@pytest.fixture(autouse=True)
def reset_registry():
    reset_global_registry()

    @convert_sqlalchemy_composite.register(CompositeFullName)
    def convert_composite_class(composite, registry):
        return graphene.Field(graphene.Int)


@pytest.yield_fixture(scope="function")
def session_factory():
    engine = create_engine(test_db_url)
    Base.metadata.create_all(engine)

    yield sessionmaker(bind=engine)

    engine.dispose()


@pytest.fixture(scope="function")
~~def session(session_factory):
    return session_factory()



## ... source file continues with no further session examples...

```

