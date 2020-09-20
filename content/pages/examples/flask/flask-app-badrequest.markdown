title: flask.app BadRequest Example Code
category: page
slug: flask-app-badrequest-examples
sortorder: 500021000
toc: False
sidebartitle: flask.app BadRequest
meta: Example code for understanding how to use the BadRequest class from the flask.app module of the Flask project.


[BadRequest](https://github.com/pallets/flask/blob/master/src/flask/app.py)
is an [Exception](https://docs.python.org/3/library/exceptions.html#Exception)
imported into the [Flask](/flask.html) [web framework](/web-frameworks.html)
from the [Werkzeug](https://github.com/pallets/werkzeug) project. It can occur
at runtime when an
[invalid POST request is sent to a URL route](https://stackoverflow.com/questions/14105452/what-is-the-cause-of-the-bad-request-error-when-submitting-form-in-flask-applica)
that accepts POSTs.

<a href="/flask-app-flask-examples.html">Flask</a>,
<a href="/flask-app-headers-examples.html">Headers</a>,
and <a href="/flask-app-immutabledict-examples.html">ImmutableDict</a>
are several other callables with code examples from the same `flask.app` package.

These subjects go along with the `BadRequest` code examples:

* [web development](/web-development.html) and [web design](/web-design.html)
* [Flask](/flask.html) and [web framework](/web-frameworks.html) concepts


## Example 1 from Flask AppBuilder
[Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder)
([documentation](https://flask-appbuilder.readthedocs.io/en/latest/)
and
[example apps](https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples))
is a web application generator that uses Flask to automatically create
the code for database-driven applications based on parameters set
by the user. The generated applications include default security settings,
forms, and internationalization support.

Flask App Builder is provided under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/LICENSE).

[**Flask AppBuilder / flask_appbuilder / api / __init__.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/api/__init__.py)

```python
# __init__.py
import functools
import json
import logging
import re
import traceback
from typing import Callable, Dict, List, Optional, Set
import urllib.parse

from apispec import APISpec, yaml_utils
from apispec.exceptions import DuplicateComponentNameError
from flask import Blueprint, current_app, jsonify, make_response, request, Response
from flask_babel import lazy_gettext as _
import jsonschema
from marshmallow import Schema, ValidationError
from marshmallow_sqlalchemy.fields import Related, RelatedList
import prison
from sqlalchemy.exc import IntegrityError
~~from werkzeug.exceptions import BadRequest
import yaml

from .convert import Model2SchemaConverter
from .schemas import get_info_schema, get_item_schema, get_list_schema
from .._compat import as_unicode
from ..const import (
    API_ADD_COLUMNS_RES_KEY,
    API_ADD_COLUMNS_RIS_KEY,
    API_ADD_TITLE_RES_KEY,
    API_ADD_TITLE_RIS_KEY,
    API_DESCRIPTION_COLUMNS_RES_KEY,
    API_DESCRIPTION_COLUMNS_RIS_KEY,
    API_EDIT_COLUMNS_RES_KEY,
    API_EDIT_COLUMNS_RIS_KEY,
    API_EDIT_TITLE_RES_KEY,
    API_EDIT_TITLE_RIS_KEY,
    API_FILTERS_RES_KEY,
    API_FILTERS_RIS_KEY,
    API_LABEL_COLUMNS_RES_KEY,
    API_LABEL_COLUMNS_RIS_KEY,
    API_LIST_COLUMNS_RES_KEY,
    API_LIST_COLUMNS_RIS_KEY,
    API_LIST_TITLE_RES_KEY,
    API_LIST_TITLE_RIS_KEY,


## ... source file abbreviated to get to BadRequest examples ...


    API_SELECT_COLUMNS_RIS_KEY,
    API_SHOW_COLUMNS_RES_KEY,
    API_SHOW_COLUMNS_RIS_KEY,
    API_SHOW_TITLE_RES_KEY,
    API_SHOW_TITLE_RIS_KEY,
    API_URI_RIS_KEY,
    PERMISSION_PREFIX,
)
from ..exceptions import FABException, InvalidOrderByColumnFABException
from ..security.decorators import permission_name, protect

log = logging.getLogger(__name__)


def get_error_msg():
    if current_app.config.get("FAB_API_SHOW_STACKTRACE"):
        return traceback.format_exc()
    return "Fatal error"


def safe(f):

    def wraps(self, *args, **kwargs):
        try:
            return f(self, *args, **kwargs)
~~        except BadRequest as e:
            return self.response_400(message=str(e))
        except Exception as e:
            logging.exception(e)
            return self.response_500(message=get_error_msg())

    return functools.update_wrapper(wraps, f)


def rison(schema=None):

    def _rison(f):
        def wraps(self, *args, **kwargs):
            value = request.args.get(API_URI_RIS_KEY, None)
            kwargs["rison"] = dict()
            if value:
                try:
                    kwargs["rison"] = prison.loads(value)
                except prison.decoder.ParserException:
                    if current_app.config.get("FAB_API_ALLOW_JSON_QS", True):
                        try:
                            kwargs["rison"] = json.loads(
                                urllib.parse.parse_qs(f"{API_URI_RIS_KEY}={value}").get(
                                    API_URI_RIS_KEY
                                )[0]


## ... source file continues with no further BadRequest examples...

```


## Example 2 from Flask-WTF
[Flask-WTF](https://github.com/lepture/flask-wtf)
([project documentation](https://flask-wtf.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/Flask-WTF/))
provides a bridge between [Flask](/flask.html) and the the
[WTForms](https://wtforms.readthedocs.io/en/2.3.x/) form-handling library.
It makes it easier to use WTForms by reducing boilerplate code and
shorter examples for common form operations as well as common security
practices such as [CSRF](/cross-site-request-forgery-csrf.html).

[**Flask-WTF / flask_wtf / csrf.py**](https://github.com/lepture/flask-wtf/blob/master/flask_wtf/./csrf.py)

```python
# csrf.py
import hashlib
import logging
import os
import warnings
from urllib.parse import urlparse
from functools import wraps

from flask import Blueprint, current_app, g, request, session
from itsdangerous import BadData, SignatureExpired, URLSafeTimedSerializer
~~from werkzeug.exceptions import BadRequest
from werkzeug.security import safe_str_cmp
from wtforms import ValidationError
from wtforms.csrf.core import CSRF

from ._compat import FlaskWTFDeprecationWarning

__all__ = ('generate_csrf', 'validate_csrf', 'CSRFProtect')
logger = logging.getLogger(__name__)


def generate_csrf(secret_key=None, token_key=None):

    secret_key = _get_config(
        secret_key, 'WTF_CSRF_SECRET_KEY', current_app.secret_key,
        message='A secret key is required to use CSRF.'
    )
    field_name = _get_config(
        token_key, 'WTF_CSRF_FIELD_NAME', 'csrf_token',
        message='A field name is required to use CSRF.'
    )

    if field_name not in g:
        s = URLSafeTimedSerializer(secret_key, salt='wtf-csrf-token')



## ... source file abbreviated to get to BadRequest examples ...


        warnings.warn(FlaskWTFDeprecationWarning(
            '"@csrf.error_handler" is deprecated. Use the standard Flask '
            'error system with "@app.errorhandler(CSRFError)" instead. This '
            'will be removed in 1.0.'
        ), stacklevel=2)

        @wraps(view)
        def handler(reason):
            response = current_app.make_response(view(reason))
            raise CSRFError(response=response)

        self._error_response = handler
        return view


class CsrfProtect(CSRFProtect):

    def __init__(self, app=None):
        warnings.warn(FlaskWTFDeprecationWarning(
            '"flask_wtf.CsrfProtect" has been renamed to "CSRFProtect" '
            'and will be removed in 1.0.'
        ), stacklevel=2)
        super().__init__(app=app)


~~class CSRFError(BadRequest):

    description = 'CSRF validation failed.'


def same_origin(current_uri, compare_uri):
    current = urlparse(current_uri)
    compare = urlparse(compare_uri)

    return (
        current.scheme == compare.scheme
        and current.hostname == compare.hostname
        and current.port == compare.port
    )



## ... source file continues with no further BadRequest examples...

```


## Example 3 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / errors.py**](https://github.com/indico/indico/blob/master/indico/core/errors.py)

```python
# errors.py


~~from werkzeug.exceptions import BadRequest, Forbidden, HTTPException, NotFound

from indico.util.i18n import _
from indico.util.string import to_unicode


def get_error_description(exception):
    try:
        description = exception.description
    except AttributeError:
        return to_unicode(exception.message)
    if isinstance(exception, Forbidden) and description == Forbidden.description:
        return _(u"You are not allowed to access this page.")
    elif isinstance(exception, NotFound) and description == NotFound.description:
        return _(u"The page you are looking for doesn't exist.")
~~    elif isinstance(exception, BadRequest) and description == BadRequest.description:
        return _(u"The request was invalid or contained invalid arguments.")
    else:
        return to_unicode(description)


class IndicoError(Exception):


class NoReportError(IndicoError):

    @classmethod
    def wrap_exc(cls, exc):
        assert isinstance(exc, HTTPException)
        exc._disallow_report = True
        return exc


class UserValueError(NoReportError):
    http_status_code = 400



## ... source file continues with no further BadRequest examples...

```

