title: flask.app Headers code examples
category: page
slug: flask-app-headers-examples
sortorder: 500021002
toc: False
sidebartitle: flask.app Headers
meta: Python example code for the Headers class from the flask.app module of the Flask project.


Headers is a class within the flask.app module of the Flask project.


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

from collections import OrderedDict
from functools import wraps, partial
from types import MethodType

from flask import url_for, request, current_app
from flask import make_response as original_flask_make_response
from flask.helpers import _endpoint_from_view_func
from flask.signals import got_request_exception

from jsonschema import RefResolver

from werkzeug.utils import cached_property
~~from werkzeug.datastructures import Headers
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

RE_RULES = re.compile("(<.*>)")

HEADERS_BLACKLIST = ("Content-Length",)

DEFAULT_REPRESENTATIONS = [("application/json", output_json)]


## ... source file abbreviated to get to Headers examples ...


                return self.handle_error(e)
            except Exception as f:
                return original_handler(f)
        return original_handler(e)

    def handle_error(self, e):
        got_request_exception.send(current_app._get_current_object(), exception=e)

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

~~        headers = Headers()

        for typecheck, handler in six.iteritems(self._own_and_child_error_handlers):
            if isinstance(e, typecheck):
                result = handler(e)
                default_data, code, headers = unpack(
                    result, HTTPStatus.INTERNAL_SERVER_ERROR
                )
                break
        else:
            if isinstance(e, HTTPException):
                code = HTTPStatus(e.code)
                if include_message_in_response:
                    default_data = {"message": getattr(e, "description", code.phrase)}
                headers = e.get_response().headers
            elif self._default_error_handler:
                result = self._default_error_handler(e)
                default_data, code, headers = unpack(
                    result, HTTPStatus.INTERNAL_SERVER_ERROR
                )
            else:
                code = HTTPStatus.INTERNAL_SERVER_ERROR
                if include_message_in_response:
                    default_data = {
                        "message": code.phrase,


## ... source file continues with no further Headers examples...

```

