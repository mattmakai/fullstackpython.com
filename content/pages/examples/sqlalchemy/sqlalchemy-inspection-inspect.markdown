title: sqlalchemy.inspection inspect code examples
category: page
slug: sqlalchemy-inspection-inspect-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.inspection inspect
meta: Python example code for the inspect function from the sqlalchemy.inspection module of the SQLAlchemy project.


inspect is a function within the sqlalchemy.inspection module of the SQLAlchemy project.


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
~~from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy  # pylint: disable=import-error,no-name-in-module
from sqlalchemy.ext.automap import automap_base
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


## ... source file abbreviated to get to inspect examples ...


        """
        result_dict = {}
        for column in self.__table__.columns.keys():  # pylint: disable=no-member
            value = result_dict[column] = getattr(self, column, None)
            if isinstance(value, Decimal):
                result_dict[column] = float(result_dict[column])
            elif isinstance(value, datetime.datetime):
                result_dict[column] = value.isoformat()
            elif isinstance(value, datetime.time):
                result_dict[column] = value.strftime("%H:%M:%S")
        return result_dict

    def links(self):
        """Return a dictionary of links to related resources that should be
        included in the *Link* header of an HTTP response.

        :rtype: dict

        """
        link_dict = {'self': self.resource_uri()}
~~        for relationship in inspect(  # pylint: disable=maybe-no-member
                self.__class__).relationships:
            if 'collection' not in relationship.key:
                instance = getattr(self, relationship.key)
                if instance:
                    link_dict[str(relationship.key)] = instance.resource_uri()
        return link_dict

    def resource_uri(self):
        """Return the URI to this specific resource.

        :rtype: str

        """
        return self.__url__ + '/' + str(getattr(self, self.primary_key()))

    def update(self, attributes):
        """Update the current instance based on attribute->value items in
        *attributes*.

        :param dict attributes: Dictionary of attributes to be updated
        :rtype: :class:`sandman2.model.Model`
        """
        for attribute in attributes:
            setattr(self, attribute, attributes[attribute])


## ... source file continues with no further inspect examples...


```

