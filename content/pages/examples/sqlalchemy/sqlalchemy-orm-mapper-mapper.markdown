title: sqlalchemy.orm.mapper Mapper Example Code
category: page
slug: sqlalchemy-orm-mapper-mapper-examples
sortorder: 500031085
toc: False
sidebartitle: sqlalchemy.orm.mapper Mapper
meta: Example code for understanding how to use the Mapper class from the sqlalchemy.orm.mapper module of the SQLAlchemy project.


`Mapper` is a class within the `sqlalchemy.orm.mapper` module of the SQLAlchemy project.



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
~~from sqlalchemy.orm.mapper import Mapper
from sqlalchemy.util import symbol
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



## ... source file continues with no further Mapper examples...

```

