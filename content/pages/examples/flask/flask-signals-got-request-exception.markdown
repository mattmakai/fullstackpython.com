title: flask.signals got_request_exception Example Code
category: page
slug: flask-signals-got-request-exception-examples
sortorder: 500021030
toc: False
sidebartitle: flask.signals got_request_exception
meta: Python example code that shows how to use the got_request_exception callable from the flask.signals module of the Flask project.


[got_request_exception](https://github.com/pallets/flask/blob/master/src/flask/signals.py)
is a signal defined in the [Flask](/flask.html) project's
`flask.signals` module that interrupts the WSGI flow when there is an
issue with the HTTP request. It can also be thrown by your own
view functions if there is an error and you want to raise it via a signal.

<a href="/flask-signals-namespace-examples.html">Namespace</a>
is another callable from the `flask.signals` package with code examples.

## Example 1 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / api.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./api.py)

```python
# api.py
from __future__ import unicode_literals

import difflib
import inspect
from itertools import chain
import logging
import operator
import re
import six
import sys
import warnings

from collections import OrderedDict
from functools import wraps, partial
from types import MethodType

from flask import url_for, request, current_app
from flask import make_response as original_flask_make_response
from flask.helpers import _endpoint_from_view_func
~~from flask.signals import got_request_exception

from jsonschema import RefResolver

from werkzeug.utils import cached_property
from werkzeug.datastructures import Headers
from werkzeug.exceptions import (
    HTTPException,
    MethodNotAllowed,
    NotFound,
    NotAcceptable,
    InternalServerError,
)
from werkzeug.wrappers import BaseResponse

from . import apidoc
from .mask import ParseError, MaskError
from .namespace import Namespace
from .postman import PostmanCollectionV1
from .resource import Resource
from .swagger import Swagger
from .utils import default_id, camel_to_dash, unpack
from .representations import output_json
from ._http import HTTPStatus



## ... source file abbreviated to get to got_request_exception examples ...


        except MethodNotAllowed as e:
            valid_route_method = e.valid_methods[0]
            rule, _ = adapter.match(method=valid_route_method, return_rule=True)
            return self.owns_endpoint(rule.endpoint)
        except NotFound:
            return self.catch_all_404s
        except Exception:
            pass

    def _has_fr_route(self):
        if self._should_use_fr_error_handler():
            return True
        if not request.url_rule:
            return False
        return self.owns_endpoint(request.url_rule.endpoint)

    def error_router(self, original_handler, e):
        if self._has_fr_route():
            try:
                return self.handle_error(e)
            except Exception as f:
                return original_handler(f)
        return original_handler(e)

    def handle_error(self, e):
~~        got_request_exception.send(current_app._get_current_object(), exception=e)

        if (
            not isinstance(e, HTTPException)
            and current_app.propagate_exceptions
            and not isinstance(e, tuple(self.error_handlers.keys()))
        ):

            exc_type, exc_value, tb = sys.exc_info()
            if exc_value is e:
                raise
            else:
                raise e

        include_message_in_response = current_app.config.get(
            "ERROR_INCLUDE_MESSAGE", True
        )
        default_data = {}

        headers = Headers()

        for typecheck, handler in six.iteritems(self._own_and_child_error_handlers):
            if isinstance(e, typecheck):
                result = handler(e)
                default_data, code, headers = unpack(


## ... source file continues with no further got_request_exception examples...

```

