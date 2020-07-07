title: sqlalchemy.orm RelationshipProperty Example Code
category: page
slug: sqlalchemy-orm-relationshipproperty-examples
sortorder: 500031053
toc: False
sidebartitle: sqlalchemy.orm RelationshipProperty
meta: Example code for understanding how to use the RelationshipProperty class from the sqlalchemy.orm module of the SQLAlchemy project.


RelationshipProperty is a class within the sqlalchemy.orm module of the SQLAlchemy project.


## Example 1 from SQLAlchemy Mixins
[SQLAlchemy Mixins](https://github.com/absent1706/sqlalchemy-mixins)
([PyPI package information](https://pypi.org/project/sqlalchemy-mixins/))
is a collection of
[mixins](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
useful for extending [SQLAlchemy](/sqlalchemy.html) and simplifying
your [database](/databases.html)-interacting code for some common
use cases. SQLAlchemy Mixins is open sourced under the
[MIT license](https://github.com/absent1706/sqlalchemy-mixins/blob/master/LICENSE.txt).

[**SQLAlchemy Mixins / sqlalchemy_mixins / inspection.py**](https://github.com/absent1706/sqlalchemy-mixins/blob/master/sqlalchemy_mixins/./inspection.py)

```python
# inspection.py
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
~~from sqlalchemy.orm import RelationshipProperty

from .utils import classproperty


Base = declarative_base()


class InspectionMixin(Base):
    __abstract__ = True

    @classproperty
    def columns(cls):
        return inspect(cls).columns.keys()

    @classproperty
    def primary_keys_full(cls):
        mapper = cls.__mapper__
        return [
            mapper.get_property_by_column(column)
            for column in mapper.primary_key
        ]

    @classproperty
    def primary_keys(cls):


## ... source file continues with no further RelationshipProperty examples...

```

