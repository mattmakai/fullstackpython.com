title: flask.app Headers Example Code
category: page
slug: flask-app-headers-examples
sortorder: 500021002
toc: False
sidebartitle: flask.app Headers
meta: Example code for understanding how to use the Headers class from the flask.app module of the Flask project.


[Headers](https://github.com/pallets/flask/blob/master/src/flask/app.py)
is class within the `flask.app` module of the [Flask](/flask.html)
[web framework](/web-frameworks.html) that is imported from the
[datastructures](https://github.com/pallets/werkzeug/blob/master/src/werkzeug/datastructures.py)
module of the [Werkzeug](https://palletsprojects.com/p/werkzeug/) project.
Headers handles the
[HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
from [requests](/flask-globals-request-examples.html) and responses for
Flask web applications.

<a href="/flask-app-badrequest-examples.html">BadRequest</a>,
<a href="/flask-app-flask-examples.html">Flask</a>,
and <a href="/flask-app-immutabledict-examples.html">ImmutableDict</a>
are several other callables with code examples from the same `flask.app` package.

These topics are also useful while reading the `Headers` examples:

* [web development](/web-development.html) and [web design](/web-design.html)
* [Flask](/flask.html) and [web framework](/web-frameworks.html) concepts


## Example 1 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [Flask](/flask.html). The application can be used
as-is to run CTF events, or modified for custom rules for related
scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / tests / helpers.py**](https://github.com/CTFd/CTFd/blob/master/./tests/helpers.py)

```python
# helpers.py
import datetime
import gc
import random
import string
import uuid
from collections import namedtuple
from unittest.mock import Mock, patch

import requests
from flask.testing import FlaskClient
from sqlalchemy.engine.url import make_url
from sqlalchemy_utils import drop_database
~~from werkzeug.datastructures import Headers

from CTFd import create_app
from CTFd.cache import cache, clear_standings
from CTFd.config import TestingConfig
from CTFd.models import (
    Awards,
    ChallengeComments,
    ChallengeFiles,
    Challenges,
    Comments,
    Fails,
    Fields,
    Files,
    Flags,
    Hints,
    Notifications,
    PageComments,
    PageFiles,
    Pages,
    Solves,
    Tags,
    TeamComments,
    Teams,
    Tokens,
    Tracking,
    Unlocks,
    UserComments,
    Users,
)

text_type = str
binary_type = bytes


FakeRequest = namedtuple("FakeRequest", ["form"])


class CTFdTestClient(FlaskClient):
    def open(self, *args, **kwargs):
        if kwargs.get("json") is not None:
            with self.session_transaction() as sess:
~~                api_key_headers = Headers({"CSRF-Token": sess.get("nonce")})
~~                headers = kwargs.pop("headers", Headers())
                if isinstance(headers, dict):
~~                    headers = Headers(headers)
                headers.extend(api_key_headers)
                kwargs["headers"] = headers
        return super(CTFdTestClient, self).open(*args, **kwargs)


def create_ctfd(
    ctf_name="CTFd",
    ctf_description="CTF description",
    name="admin",
    email="admin@ctfd.io",
    password="password",
    user_mode="users",
    setup=True,
    enable_plugins=False,
    application_root="/",
    config=TestingConfig,
):
    if enable_plugins:
        config.SAFE_MODE = False
    else:
        config.SAFE_MODE = True

    config.APPLICATION_ROOT = application_root
    url = make_url(config.SQLALCHEMY_DATABASE_URI)


## ... source file continues with no further Headers examples...

```


## Example 2 from flask-restx
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

