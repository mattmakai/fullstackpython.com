title: flask.globals session Python code examples
category: page
slug: flask-globals-session-examples
sortorder: 500021001
toc: False
sidebartitle: flask.globals session
meta: Python example code for the session function from the flask.globals module of the Flask project.


session is a function within the flask.globals module of the Flask project.


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

[**Flask AppBuilder / flask_appbuilder / security / registerviews.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/security/registerviews.py)

```python
# registerviews.py
__author__ = "Daniel Gaspar"

import logging

~~from flask import flash, redirect, request, session, url_for
from flask_babel import lazy_gettext
from flask_openid import OpenIDResponse, SessionWrapper
from openid.consumer.consumer import CANCEL, Consumer, SUCCESS

from .forms import LoginForm_oid, RegisterUserDBForm, RegisterUserOIDForm
from .. import const as c
from .._compat import as_unicode
from ..validators import Unique
from ..views import expose, PublicFormView

log = logging.getLogger(__name__)


def get_first_last_name(fullname):
    names = fullname.split()
    if len(names) > 1:
        return names[0], " ".join(names[1:])
    elif names:
        return names[0], ""


class BaseRegisterUser(PublicFormView):
    """
        Make your own user registration view and inherit from this class if you


## ... source file abbreviated to get to session examples ...


class RegisterUserOIDView(BaseRegisterUser):
    """
        View for Registering a new user, auth OID mode
    """

    route_base = "/register"

    form = RegisterUserOIDForm
    default_view = "form_oid_post"

    @expose("/formoidone", methods=["GET", "POST"])
    def form_oid_post(self, flag=True):
        if flag:
            self.oid_login_handler(self.form_oid_post, self.appbuilder.sm.oid)
        form = LoginForm_oid()
        if form.validate_on_submit():
            session["remember_me"] = form.remember_me.data
            return self.appbuilder.sm.oid.try_login(
                form.openid.data, ask_for=["email", "fullname"]
            )
~~        resp = session.pop("oid_resp", None)
        if resp:
            self._init_vars()
            form = self.form.refresh()
            self.form_get(form)
            form.username.data = resp.email
            first_name, last_name = get_first_last_name(resp.fullname)
            form.first_name.data = first_name
            form.last_name.data = last_name
            form.email.data = resp.email
            widgets = self._get_edit_widget(form=form)
            # self.update_redirect()
            return self.render_template(
                self.form_template,
                title=self.form_title,
                widgets=widgets,
                form_action="form",
                appbuilder=self.appbuilder,
            )
        else:
            flash(as_unicode(self.error_message), "warning")
            return redirect(self.get_redirect())

    def oid_login_handler(self, f, oid):
        """


## ... source file continues with no further session examples...


```


## Example 2 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / utils / helpers.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/utils/helpers.py)

```python
# helpers.py
"""
import ast
import itertools
import logging
import operator
import os
import re
import time
import warnings
from datetime import datetime, timedelta
from email import message_from_string
from functools import wraps

import pkg_resources
import requests
import unidecode
from babel.core import get_locale_identifier
from babel.dates import format_date as babel_format_date
from babel.dates import format_datetime as babel_format_datetime
from babel.dates import format_timedelta as babel_format_timedelta
~~from flask import flash, g, redirect, request, session, url_for
from flask_allows import Permission
from flask_babelplus import lazy_gettext as _
from flask_login import current_user
from flask_themes2 import get_themes_list, render_theme_template
from jinja2 import Markup
from PIL import ImageFile
from pytz import UTC
from werkzeug.local import LocalProxy
from werkzeug.utils import ImportStringError, import_string

from flaskbb._compat import (iteritems, range_method, string_types, text_type,
                             to_bytes, to_unicode)
from flaskbb.extensions import babel, redis_store
from flaskbb.utils.settings import flaskbb_config

try:  # compat
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

logger = logging.getLogger(__name__)

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')



## ... source file abbreviated to get to session examples ...


            result.append(word)
    return text_type(delim.join(result))


def redirect_or_next(endpoint, **kwargs):
    """Redirects the user back to the page they were viewing or to a specified
    endpoint. Wraps Flasks :func:`Flask.redirect` function.

    :param endpoint: The fallback endpoint.
    """
    return redirect(request.args.get("next") or endpoint, **kwargs)


def render_template(template, **context):  # pragma: no cover
    """A helper function that uses the `render_theme_template` function
    without needing to edit all the views
    """
    if current_user.is_authenticated and current_user.theme:
        theme = current_user.theme
    else:
~~        theme = session.get("theme", flaskbb_config["DEFAULT_THEME"])
    return render_theme_template(theme, template, **context)


# TODO(anr): clean this up
def do_topic_action(topics, user, action, reverse):  # noqa: C901
    """Executes a specific action for topics. Returns a list with the modified
    topic objects.

    :param topics: A iterable with ``Topic`` objects.
    :param user: The user object which wants to perform the action.
    :param action: One of the following actions: locked, important and delete.
    :param reverse: If the action should be done in a reversed way.
                    For example, to unlock a topic, ``reverse`` should be
                    set to ``True``.
    """
    if not topics:
        return False

    from flaskbb.utils.requirements import (
        IsAtleastModeratorInForum,
        CanDeleteTopic,
        Has,
    )



## ... source file continues with no further session examples...


```


## Example 3 from Flask-WTF
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
from functools import wraps

~~from flask import Blueprint, current_app, g, request, session
from itsdangerous import BadData, SignatureExpired, URLSafeTimedSerializer
from werkzeug.exceptions import BadRequest
from werkzeug.security import safe_str_cmp
from wtforms import ValidationError
from wtforms.csrf.core import CSRF

from ._compat import FlaskWTFDeprecationWarning, string_types, urlparse

__all__ = ('generate_csrf', 'validate_csrf', 'CSRFProtect')
logger = logging.getLogger(__name__)


def generate_csrf(secret_key=None, token_key=None):
    """Generate a CSRF token. The token is cached for a request, so multiple
    calls to this function will generate the same token.

    During testing, it might be useful to access the signed token in
    ``g.csrf_token`` and the raw token in ``session['csrf_token']``.

    :param secret_key: Used to securely sign the token. Default is
        ``WTF_CSRF_SECRET_KEY`` or ``SECRET_KEY``.
    :param token_key: Key where token is stored in session for comparison.
        Default is ``WTF_CSRF_FIELD_NAME`` or ``'csrf_token'``.
    """

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

~~        if field_name not in session:
            session[field_name] = hashlib.sha1(os.urandom(64)).hexdigest()

        try:
            token = s.dumps(session[field_name])
        except TypeError:
            session[field_name] = hashlib.sha1(os.urandom(64)).hexdigest()
            token = s.dumps(session[field_name])

        setattr(g, field_name, token)

    return g.get(field_name)


def validate_csrf(data, secret_key=None, time_limit=None, token_key=None):
    """Check if the given data is a valid CSRF token. This compares the given
    signed token to the one stored in the session.

    :param data: The signed CSRF token to be checked.
    :param secret_key: Used to securely sign the token. Default is
        ``WTF_CSRF_SECRET_KEY`` or ``SECRET_KEY``.
    :param time_limit: Number of seconds that the token is valid. Default is
        ``WTF_CSRF_TIME_LIMIT`` or 3600 seconds (60 minutes).
    :param token_key: Key where token is stored in session for comparison.
        Default is ``WTF_CSRF_FIELD_NAME`` or ``'csrf_token'``.


## ... source file abbreviated to get to session examples ...


    .. versionchanged:: 0.14
        Raises ``ValidationError`` with a specific error message rather than
        returning ``True`` or ``False``.
    """

    secret_key = _get_config(
        secret_key, 'WTF_CSRF_SECRET_KEY', current_app.secret_key,
        message='A secret key is required to use CSRF.'
    )
    field_name = _get_config(
        token_key, 'WTF_CSRF_FIELD_NAME', 'csrf_token',
        message='A field name is required to use CSRF.'
    )
    time_limit = _get_config(
        time_limit, 'WTF_CSRF_TIME_LIMIT', 3600, required=False
    )

    if not data:
        raise ValidationError('The CSRF token is missing.')

~~    if field_name not in session:
        raise ValidationError('The CSRF session token is missing.')

    s = URLSafeTimedSerializer(secret_key, salt='wtf-csrf-token')

    try:
        token = s.loads(data, max_age=time_limit)
    except SignatureExpired:
        raise ValidationError('The CSRF token has expired.')
    except BadData:
        raise ValidationError('The CSRF token is invalid.')

    if not safe_str_cmp(session[field_name], token):
        raise ValidationError('The CSRF tokens do not match.')


def _get_config(
    value, config_name, default=None,
    required=True, message='CSRF is not configured.'
):
    """Find config value based on provided value, Flask config, and default
    value.

    :param value: already provided config value
    :param config_name: Flask ``config`` key


## ... source file continues with no further session examples...


```

