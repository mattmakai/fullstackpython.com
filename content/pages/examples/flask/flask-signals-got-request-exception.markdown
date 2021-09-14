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
try:
    from flask.helpers import _endpoint_from_view_func
except ImportError:
    from flask.scaffold import _endpoint_from_view_func
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

from werkzeug import __version__ as werkzeug_version

if werkzeug_version.split('.')[0] >= '2':
    from werkzeug.wrappers import Response as BaseResponse
else:
    from werkzeug.wrappers import BaseResponse

from . import apidoc
from .mask import ParseError, MaskError
from .namespace import Namespace
from .postman import PostmanCollectionV1


## ... source file abbreviated to get to got_request_exception examples ...


            and current_app.propagate_exceptions
            and not isinstance(e, tuple(self._own_and_child_error_handlers.keys()))
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
                    result, HTTPStatus.INTERNAL_SERVER_ERROR
                )
                break
        else:
~~            got_request_exception.send(current_app._get_current_object(), exception=e)

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
                    }

        if include_message_in_response:
            default_data["message"] = default_data.get("message", str(e))

        data = getattr(e, "data", default_data)
        fallback_mediatype = None



## ... source file continues with no further got_request_exception examples...

```

