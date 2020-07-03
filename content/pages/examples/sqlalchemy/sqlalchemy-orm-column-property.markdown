title: sqlalchemy.orm column_property code examples
category: page
slug: sqlalchemy-orm-column-property-examples
sortorder: 500031047
toc: False
sidebartitle: sqlalchemy.orm column_property
meta: Python example code for the column_property callable from the sqlalchemy.orm module of the SQLAlchemy project.


column_property is a callable within the sqlalchemy.orm module of the SQLAlchemy project.


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



## ... source file abbreviated to get to column_property examples ...


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
    pets = relationship("Pet", secondary=association_table, backref="reporters", order_by="Pet.id")
    articles = relationship("Article", backref="reporter")
    favorite_article = relationship("Article", uselist=False)

    @hybrid_property
    def hybrid_prop(self):
        return self.first_name

~~    column_prop = column_property(
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
        return []


editor_table = Table("editors", Base.metadata, autoload=True)

mapper(ReflectedEditor, editor_table)


## ... source file continues with no further column_property examples...

```

