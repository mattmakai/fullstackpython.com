title: sqlalchemy.ext.automap automap_base code examples
category: page
slug: sqlalchemy-ext-automap-automap-base-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.ext.automap automap_base
meta: Python example code for the automap_base function from the sqlalchemy.ext.automap module of the SQLAlchemy project.


automap_base is a function within the sqlalchemy.ext.automap module of the SQLAlchemy project.


## Example 1 from sandman2
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
"""Module containing code related to *sandman2* ORM models."""

# Standard library imports
import datetime
from decimal import Decimal

# Third-party imports
from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy  # pylint: disable=import-error,no-name-in-module
~~from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class Model(object):

    """The sandman2 Model class is the base class for all RESTful resources.
    There is a one-to-one mapping between a table in the database and a
    :class:`sandman2.model.Model`.
    """

    #: The relative URL this resource should live at.
    __url__ = None

    #: The API version of this resource (not yet used).
    __version__ = '1'

    #: The HTTP methods this resource supports (default=all).
    __methods__ = {
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',


## ... source file abbreviated to get to automap_base examples ...


            setattr(self, attribute, attributes[attribute])
        return self

    @classmethod
    def description(cls):
        """Return a field->data type dictionary describing this model
        as reported by the database.

        :rtype: dict
        """

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

