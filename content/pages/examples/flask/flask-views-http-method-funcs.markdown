title: flask.views http_method_funcs Example Code
category: page
slug: flask-views-http-method-funcs-examples
sortorder: 500021035
toc: False
sidebartitle: flask.views http_method_funcs
meta: Python example code that shows how to use the http_method_funcs callable from the flask.views module of the Flask project.


`http_method_funcs` is an immutable Python set within the
[flask.views module](https://github.com/pallets/flask/blob/master/src/flask/views.py)
of the [Flask](/flask.html) project. It contains strings of the HTTP methods
"get", "post", "head", "options", "delete", "put", "trace", and "patch",
which is useful for checking if an HTTP method is valid by comparing it
against the items in this set.

<a href="/flask-views-methodview-examples.html">MethodView</a>
and
<a href="/flask-views-view-examples.html">View</a>
are a couple of other callables within the `flask.views` package that also have code examples.

These subjects go along with the `http_method_funcs` code examples:

* [web development](/web-development.html) and [web design](/web-design.html)
* [web framework concepts](/web-frameworks.html) and the [Flask framework](/flask.html)


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
from __future__ import unicode_literals

import inspect
import warnings
import logging
from collections import namedtuple, OrderedDict

import six
from flask import request
~~from flask.views import http_method_funcs

from ._http import HTTPStatus
from .errors import abort
from .marshalling import marshal, marshal_with
from .model import Model, OrderedModel, SchemaModel
from .reqparse import RequestParser
from .utils import merge

ResourceRoute = namedtuple("ResourceRoute", "resource urls route_doc kwargs")


class Namespace(object):

    def __init__(
        self,
        name,
        description=None,
        path=None,
        decorators=None,
        validate=None,
        authorizations=None,
        ordered=False,
        **kwargs
    ):


## ... source file abbreviated to get to http_method_funcs examples ...


        return (self._path or ("/" + self.name)).rstrip("/")

    def add_resource(self, resource, *urls, **kwargs):
        route_doc = kwargs.pop("route_doc", {})
        self.resources.append(ResourceRoute(resource, urls, route_doc, kwargs))
        for api in self.apis:
            ns_urls = api.ns_urls(self, urls)
            api.register_resource(self, resource, *ns_urls, **kwargs)

    def route(self, *urls, **kwargs):

        def wrapper(cls):
            doc = kwargs.pop("doc", None)
            if doc is not None:
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

