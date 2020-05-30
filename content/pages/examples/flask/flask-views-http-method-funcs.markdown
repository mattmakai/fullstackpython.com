title: flask.views http_method_funcs Python code examples
category: page
slug: flask-views-http-method-funcs-examples
sortorder: 500021002
toc: False
sidebartitle: flask.views http_method_funcs
meta: Python example code for the http_method_funcs function from the flask.views module of the Flask project.


http_method_funcs is a function within the flask.views module of the Flask project.


## Example 1 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / namespace.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./namespace.py)

```python
# namespace.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import inspect
import warnings
import logging
from collections import namedtuple

import six
from flask import request
~~from flask.views import http_method_funcs

from ._http import HTTPStatus
from .errors import abort
from .marshalling import marshal, marshal_with
from .model import Model, OrderedModel, SchemaModel
from .reqparse import RequestParser
from .utils import merge

# Container for each route applied to a Resource using @ns.route decorator
ResourceRoute = namedtuple("ResourceRoute", "resource urls route_doc kwargs")


class Namespace(object):
    """
    Group resources together.

    Namespace is to API what :class:`flask:flask.Blueprint` is for :class:`flask:flask.Flask`.

    :param str name: The namespace name
    :param str description: An optional short description
    :param str path: An optional prefix path. If not provided, prefix is ``/+name``
    :param list decorators: A list of decorators to apply to each resources
    :param bool validate: Whether or not to perform validation on this namespace
    :param bool ordered: Whether or not to preserve order on models and marshalling


## ... source file abbreviated to get to http_method_funcs examples ...


    def route(self, *urls, **kwargs):
        """
        A decorator to route resources.
        """

        def wrapper(cls):
            doc = kwargs.pop("doc", None)
            if doc is not None:
                # build api doc intended only for this route
                kwargs["route_doc"] = self._build_doc(cls, doc)
            self.add_resource(cls, *urls, **kwargs)
            return cls

        return wrapper

    def _build_doc(self, cls, doc):
        if doc is False:
            return False
        unshortcut_params_description(doc)
        handle_deprecations(doc)
~~        for http_method in http_method_funcs:
            if http_method in doc:
                if doc[http_method] is False:
                    continue
                unshortcut_params_description(doc[http_method])
                handle_deprecations(doc[http_method])
                if "expect" in doc[http_method] and not isinstance(
                    doc[http_method]["expect"], (list, tuple)
                ):
                    doc[http_method]["expect"] = [doc[http_method]["expect"]]
        return merge(getattr(cls, "__apidoc__", {}), doc)

    def doc(self, shortcut=None, **kwargs):
        """A decorator to add some api documentation to the decorated object"""
        if isinstance(shortcut, six.text_type):
            kwargs["id"] = shortcut
        show = shortcut if isinstance(shortcut, bool) else True

        def wrapper(documented):
            documented.__apidoc__ = self._build_doc(
                documented, kwargs if show else False
            )
            return documented

        return wrapper


## ... source file continues with no further http_method_funcs examples...


```

