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

[**Flask-Security-Too / flask_security / core.py**](https://github.com/Flask-Middleware/flask-security/blob/master/flask_security/./core.py)

```python
# core.py

from datetime import datetime, timedelta
import re
import typing as t
import warnings

import pkg_resources
from flask import _request_ctx_stack, current_app
~~from flask.json import JSONEncoder
from flask_login import AnonymousUserMixin, LoginManager
from flask_login import UserMixin as BaseUserMixin
from flask_login import current_user
from flask_principal import Identity, Principal, RoleNeed, UserNeed, identity_loaded
from flask_wtf import FlaskForm
from itsdangerous import URLSafeTimedSerializer
from passlib.context import CryptContext
from werkzeug.datastructures import ImmutableList
from werkzeug.local import LocalProxy

from .babel import FsDomain
from .decorators import (
    default_reauthn_handler,
    default_unauthn_handler,
    default_unauthz_handler,
)
from .forms import (
    ChangePasswordForm,
    ConfirmRegisterForm,
    ForgotPasswordForm,
    LoginForm,
    PasswordlessLoginForm,
    RegisterForm,
    RegisterFormMixin,


## ... source file continues with no further JSONEncoder examples...

```

