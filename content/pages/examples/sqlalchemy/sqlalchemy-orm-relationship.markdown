title: sqlalchemy.orm relationship Example Code
category: page
slug: sqlalchemy-orm-relationship-examples
sortorder: 500031072
toc: False
sidebartitle: sqlalchemy.orm relationship
meta: Python example code that shows how to use the relationship callable from the sqlalchemy.orm module of the SQLAlchemy project.


`relationship` is a callable within the `sqlalchemy.orm` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-columnproperty-examples.html">ColumnProperty</a>,
<a href="/sqlalchemy-orm-compositeproperty-examples.html">CompositeProperty</a>,
<a href="/sqlalchemy-orm-load-examples.html">Load</a>,
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

[**graphene-sqlalchemy / graphene_sqlalchemy / tests / models.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/tests/models.py)

```python
# models.py
from __future__ import absolute_import

import enum

from sqlalchemy import (Column, Date, Enum, ForeignKey, Integer, String, Table,
                        func, select)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
~~from sqlalchemy.orm import column_property, composite, mapper, relationship

PetKind = Enum("cat", "dog", name="pet_kind")


class HairKind(enum.Enum):
    LONG = 'long'
    SHORT = 'short'


Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("pet_id", Integer, ForeignKey("pets.id")),
    Column("reporter_id", Integer, ForeignKey("reporters.id")),
)


class Editor(Base):
    __tablename__ = "editors"
    editor_id = Column(Integer(), primary_key=True)
    name = Column(String(100))



## ... source file abbreviated to get to relationship examples ...


    pet_kind = Column(PetKind, nullable=False)
    hair_kind = Column(Enum(HairKind, name="hair_kind"), nullable=False)
    reporter_id = Column(Integer(), ForeignKey("reporters.id"))


class CompositeFullName(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __composite_values__(self):
        return self.first_name, self.last_name

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Reporter(Base):
    __tablename__ = "reporters"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(30), doc="First name")
    last_name = Column(String(30), doc="Last name")
    email = Column(String(), doc="Email")
    favorite_pet_kind = Column(PetKind)
~~    pets = relationship("Pet", secondary=association_table, backref="reporters", order_by="Pet.id")
~~    articles = relationship("Article", backref="reporter")
~~    favorite_article = relationship("Article", uselist=False)

    @hybrid_property
    def hybrid_prop(self):
        return self.first_name

    column_prop = column_property(
        select([func.cast(func.count(id), Integer)]), doc="Column property"
    )

    composite_prop = composite(CompositeFullName, first_name, last_name, doc="Composite")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer(), primary_key=True)
    headline = Column(String(100))
    pub_date = Column(Date())
    reporter_id = Column(Integer(), ForeignKey("reporters.id"))


class ReflectedEditor(type):

    @classmethod
    def __subclasses__(cls):


## ... source file continues with no further relationship examples...

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

[**sqlalchemy-datatables / tests / models.py**](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/./tests/models.py)

```python
# models.py
import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
~~from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    birthday = Column(Date)
~~    address = relationship('Address', uselist=False, backref=backref('user'))

    def __unicode__(self):
        return '%s' % self.name

    def __repr__(self):
        return '<%s#%s>' % (self.__class__.__name__, self.id)

    @hybrid_property
    def dummy(self):
        return self.name[0:3]

    @dummy.expression
    def dummy(cls):
        return func.substr(cls.name, 0, 3)


class Address(Base):

    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    description = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))



## ... source file continues with no further relationship examples...

```

