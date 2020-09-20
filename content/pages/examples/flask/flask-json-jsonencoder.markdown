title: flask.json JSONEncoder Example Code
category: page
slug: flask-json-jsonencoder-examples
sortorder: 500021024
toc: False
sidebartitle: flask.json JSONEncoder
meta: Example code for understanding how to use the JSONEncoder class from the flask.json module of the Flask project.


[JSONEncoder](https://github.com/pallets/flask/blob/master/src/flask/json/__init__.py)
is a class within the [Flask](/flask.html) project under the `flask.json`
module. `JSONEncoder` is the default [JSON](https://www.json.org/json-en.html)
encoder for Flask and was designed to handle more types than Python's
standard library [json](https://docs.python.org/3/library/json.html) module.


<a href="/flask-json-jsonify-examples.html">jsonify</a>
is another callable from the `flask.json` package with code examples.

## Example 1 from Flask-Security-Too
[Flask-Security-Too](https://github.com/Flask-Middleware/flask-security/)
([PyPi page](https://pypi.org/project/Flask-Security-Too/) and
[project documentation](https://flask-security-too.readthedocs.io/en/stable/))
is a maintained fork of the original
[Flask-Security](https://github.com/mattupstate/flask-security) project that
makes it easier to add common security features to [Flask](/flask.html)
web applications. A few of the critical goals of the Flask-Security-Too
project are ensuring JavaScript client-based single-page applications (SPAs)
can work securely with Flask-based backends and that guidance by the
[OWASP](https://owasp.org/) organization is followed by default.

The Flask-Security-Too project is provided as open source under the
[MIT license](https://github.com/Flask-Middleware/flask-security/blob/master/LICENSE).

[**Flask-Security-Too / flask_security / utils.py**](https://github.com/Flask-Middleware/flask-security/blob/master/flask_security/./utils.py)

```python
# utils.py
import abc
import base64
import datetime
from functools import partial
import hashlib
import hmac
import time
from typing import Dict, List
import warnings
from datetime import timedelta
from urllib.parse import parse_qsl, parse_qs, urlsplit, urlunsplit, urlencode
import urllib.request
import urllib.error

from flask import _request_ctx_stack, current_app, flash, g, request, session, url_for
~~from flask.json import JSONEncoder
from flask_login import login_user as _login_user
from flask_login import logout_user as _logout_user
from flask_login import current_user
from flask_login import COOKIE_NAME as REMEMBER_COOKIE_NAME
from flask_principal import AnonymousIdentity, Identity, identity_changed, Need
from flask_wtf import csrf
from wtforms import validators, ValidationError
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.local import LocalProxy
from werkzeug.datastructures import MultiDict

from .quart_compat import best
from .signals import user_authenticated

_security = LocalProxy(lambda: current_app.extensions["security"])

_datastore = LocalProxy(lambda: _security.datastore)

_pwd_context = LocalProxy(lambda: _security.pwd_context)

_hashing_context = LocalProxy(lambda: _security.hashing_context)

localize_callback = LocalProxy(lambda: _security.i18n_domain.gettext)



## ... source file abbreviated to get to JSONEncoder examples ...


        accept_mimetypes.best = best
    if accept_mimetypes.best == "application/json":
        return True
    return False


def json_error_response(errors):
    if isinstance(errors, str):
        response_json = dict(error=errors)
    elif isinstance(errors, dict):
        response_json = dict(errors=errors)
    else:
        raise TypeError("The errors argument should be either a str or dict.")

    return response_json


~~class FsJsonEncoder(JSONEncoder):

    def default(self, obj):
        from .babel import is_lazy_string

        if is_lazy_string(obj):
            return str(obj)
        else:
~~            return JSONEncoder.default(self, obj)


class SmsSenderBaseClass(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def send_sms(self, from_number, to_number, msg):  # pragma: no cover
        return


class DummySmsSender(SmsSenderBaseClass):
    def send_sms(self, from_number, to_number, msg):  # pragma: no cover
        return


class SmsSenderFactory:
    senders = {"Dummy": DummySmsSender}

    @classmethod
    def createSender(cls, name, *args, **kwargs):
        return cls.senders[name](*args, **kwargs)


    return _security._render_json(payload, code, headers=None, user=user)


def default_want_json(req):
    if req.is_json:
        return True
    accept_mimetypes = req.accept_mimetypes
    if not hasattr(req.accept_mimetypes, "best"):  # pragma: no cover


## ... source file continues with no further JSONEncoder examples...

```

