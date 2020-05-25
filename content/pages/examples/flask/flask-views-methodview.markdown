title: flask.views MethodView Python code examples
category: page
slug: flask-views-methodview-examples
sortorder: 500021000
toc: False
sidebartitle: flask.views MethodView
meta: Python example code for the MethodView class from the flask.views module of the Flask project.


MethodView is a class within the flask.views module of the Flask project.


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

[**sandman2 / sandman2 / service.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./service.py)

```python
"""Automatically generated REST API services from SQLAlchemy
ORM models or a database introspection."""

# Third-party imports
from flask import request, make_response
import flask
~~from flask.views import MethodView
from sqlalchemy import asc, desc

# Application imports
from sandman2.exception import NotFoundException, BadRequestException
from sandman2.model import db
from sandman2.decorators import etag, validate_fields


def add_link_headers(response, links):
    """Return *response* with the proper link headers set, based on the contents
    of *links*.

    :param response: :class:`flask.Response` response object for links to be
                     added
    :param dict links: Dictionary of links to be added
    :rtype :class:`flask.Response` :
    """
    link_string = '<{}>; rel=self'.format(links['self'])
    for link in links.values():
        link_string += ', <{}>; rel=related'.format(link)
    response.headers['Link'] = link_string
    return response




## ... source file abbreviated to get to MethodView examples ...


def jsonify(resource):
    """Return a Flask ``Response`` object containing a
    JSON representation of *resource*.

    :param resource: The resource to act as the basis of the response
    """

    response = flask.jsonify(resource.to_dict())
    response = add_link_headers(response, resource.links())
    return response


def is_valid_method(model, resource=None):
    """Return the error message to be sent to the client if the current
    request passes fails any user-defined validation."""
    validation_function_name = 'is_valid_{}'.format(
        request.method.lower())
    if hasattr(model, validation_function_name):
        return getattr(model, validation_function_name)(request, resource)

~~class Service(MethodView):

    """The *Service* class is a generic extension of Flask's *MethodView*,
    providing default RESTful functionality for a given ORM resource.

    Each service has an associated *__model__* attribute which represents the
    ORM resource it exposes. Services are JSON-only. HTML-based representation
    is available through the admin interface.
    """

    #: The sandman2.model.Model-derived class to expose
    __model__ = None

    #: The string used to describe the elements when a collection is
    #: returned.
    __json_collection_name__ = 'resources'

    def delete(self, resource_id):
        """Return an HTTP response object resulting from a HTTP DELETE call.

        :param resource_id: The value of the resource's primary key
        """
        resource = self._resource(resource_id)
        error_message = is_valid_method(self.__model__, resource)
        if error_message:


## ... source file continues with no further MethodView examples...


```

