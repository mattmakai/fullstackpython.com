title: sqlalchemy.orm session Example Code
category: page
slug: sqlalchemy-orm-session-examples
sortorder: 500031073
toc: False
sidebartitle: sqlalchemy.orm session
meta: Python example code that shows how to use the session callable from the sqlalchemy.orm module of the SQLAlchemy project.


`session` is a callable within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-load-examples.html">Load</a>,
<a href="/sqlalchemy-orm-mapper-examples.html">Mapper</a>,
<a href="/sqlalchemy-orm-query-examples.html">Query</a>,
<a href="/sqlalchemy-orm-relationshipproperty-examples.html">RelationshipProperty</a>,
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


## Example 2 from sqlalchemy-datatables
[sqlalchemy-datatables](https://github.com/Pegase745/sqlalchemy-datatables)
([PyPI package information](https://pypi.org/project/sqlalchemy-datatables/))
is a helper library that makes it easier to use [SQLAlchemy](/sqlalchemy.html)
with the jQuery [JavaScript](/javascript.html)
[DataTables](https://datatables.net/) plugin. This library is designed to
be [web framework](/web-frameworks.html) agnostic and provides code examples
for both [Flask](/flask.html) and [Pyramid](/pyramid.html).

The project is built and maintained by
[Michel Nemnom (Pegase745)](https://github.com/Pegase745) and is open
sourced under the
[MIT license](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/LICENSE).

[**sqlalchemy-datatables / tests / conftest.py**](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/./tests/conftest.py)

```python
# conftest.py
from __future__ import print_function

import itertools
from datetime import datetime, timedelta

import faker
import pytest
from sqlalchemy import create_engine
~~from sqlalchemy.orm import sessionmaker

from .models import Address, Base, User


def populate(session):
    users = []
    f = faker.Faker(seed=1)
    addresses = [Address(description=d) for d in ['Street', 'Avenue', 'Road']]
~~    session.add_all(addresses)

    for i, addr in zip(range(0, 50), itertools.cycle(addresses)):
        user = User(
            name=f.name(),
            address=addr,
            birthday=datetime(1970, 1, 2) + timedelta(days=10 * i))
        users.append(user)

~~    session.add_all(users)
~~    session.commit()


@pytest.fixture(scope="session")
def engine():
    print("TestCase: Using sqlite database")
    return create_engine('sqlite:///', echo=False)


@pytest.fixture(scope="session")
~~def session(engine):
    sessionmaker_ = sessionmaker(bind=engine)
    session = sessionmaker_()
    Base.metadata.create_all(engine)
    populate(session)

    yield session

~~    session.close()



## ... source file continues with no further session examples...

```

