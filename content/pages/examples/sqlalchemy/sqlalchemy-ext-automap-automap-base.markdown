title: sqlalchemy.ext.automap automap_base Example Code
category: page
slug: sqlalchemy-ext-automap-automap-base-examples
sortorder: 500031046
toc: False
sidebartitle: sqlalchemy.ext.automap automap_base
meta: Python example code that shows how to use the automap_base callable from the sqlalchemy.ext.automap module of the SQLAlchemy project.


`automap_base` is a callable within the `sqlalchemy.ext.automap` module of the SQLAlchemy project.



## Example 1 from SQLAthanor
[SQLAthanor](https://github.com/insightindustry/sqlathanor)
([PyPI package information](https://pypi.org/project/sqlathanor/)
and
[project documentation](https://sqlathanor.readthedocs.io/en/latest/index.html))
is a [SQLAlchemy](/sqlalchemy.html) extension that provides serialization and
deserialization support for JSON, CSV, YAML and Python dictionaries.
This project is similar to [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
with one major difference: SQLAthanor works through SQLAlchemy models
while Marshmallow is less coupled to SQLAlchemy because it requires
separate representations of the serialization objects. Both libraries
have their uses depending on whether the project plans to use SQLAlchemy
for object representations or would prefer to avoid that couping.
SQLAthanor is open sourced under the
[MIT license](https://github.com/insightindustry/sqlathanor/blob/master/LICENSE).

[**SQLAthanor / sqlathanor / automap.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./automap.py)

```python
# automap.py


import sqlalchemy

try:
~~    from sqlalchemy.ext.automap import automap_base as SA_automap_base
    SUPPORTS_AUTOMAP = True
except ImportError:
    SUPPORTS_AUTOMAP = False
    SA_automap_base = bool

from validator_collection import checkers

from sqlathanor import BaseModel
from sqlathanor.errors import SQLAlchemySupportError


~~def automap_base(declarative_base = None,
                 **kwargs):

    if not SUPPORTS_AUTOMAP:
        raise SQLAlchemySupportError(
            'automap is only available in SQLAlchemy v.0.9.1 and higher, ' + \
            'but you are using %s. Please upgrade.' % sqlalchemy.__version__
        )

    if declarative_base is None:
        cls = BaseModel
    elif isinstance(declarative_base, BaseModel) or declarative_base == BaseModel:
        cls = declarative_base
    elif isinstance(declarative_base, tuple):
        for item in declarative_base:
            if item == BaseModel or isinstance(item, BaseModel):
                cls = declarative_base
                break
    else:
        cls = kwargs.pop('cls', None)
        if cls is None and checkers.is_iterable(declarative_base):
            class_list = [BaseModel]
            class_list.extend([x for x in declarative_base])
        elif cls is None and not checkers.is_iterable(declarative_base):
            class_list = [BaseModel, declarative_base]


## ... source file continues with no further automap_base examples...

```


## Example 2 from sandman2
[sandman2](https://github.com/jeffknupp/sandman2)
([project documentation](https://sandman2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/sandman2/))
is a code library for automatically generating
[RESTful APIs](/application-programming-interfaces.html) from
existing database schemas. This approach is handy for solving
straightforward situations where you want to put an abstraction
layer between one or more applications and your
[relational database](/databases.html) to prevent or reduce
direct database access.

The sandman2 project is provided under the
[Apache License 2.0](https://github.com/jeffknupp/sandman2/blob/master/LICENSE).

[**sandman2 / sandman2 / model.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./model.py)

```python
# model.py

import datetime
from decimal import Decimal

from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy  # pylint: disable=import-error,no-name-in-module
~~from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class Model(object):


    __url__ = None

    __version__ = '1'

    __methods__ = {
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'HEAD',
        'OPTIONS'
        }

    @classmethod
    def required(cls):
        columns = []


## ... source file abbreviated to get to automap_base examples ...


                instance = getattr(self, relationship.key)
                if instance:
                    link_dict[str(relationship.key)] = instance.resource_uri()
        return link_dict

    def resource_uri(self):
        return self.__url__ + '/' + str(getattr(self, self.primary_key()))

    def update(self, attributes):
        for attribute in attributes:
            setattr(self, attribute, attributes[attribute])
        return self

    @classmethod
    def description(cls):

        description = {}
        for column in cls.__table__.columns:  # pylint: disable=no-member
            column_description = str(column.type)
            if not column.nullable:
                column_description += ' (required)'
            description[column.name] = column_description
        return description

DeclarativeModel = declarative_base(cls=(db.Model, Model))
~~AutomapModel = automap_base(DeclarativeModel)



## ... source file continues with no further automap_base examples...

```

