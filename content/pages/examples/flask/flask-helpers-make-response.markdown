title: flask.helpers make_response Example Code
category: page
slug: flask-helpers-make-response-examples
sortorder: 500021020
toc: False
sidebartitle: flask.helpers make_response
meta: Python example code that shows how to use the make_response callable from the flask.helpers module of the Flask project.


[make_response](https://github.com/pallets/flask/blob/master/src/flask/helpers.py)
is a function in the `flask.helpers` module of the [Flask](/flask.html)
[web framework](/web-framework.html). `make_response` is for adding additional
HTTP headers to a response within a view's code. Sometimes views do not return
a response object so it's unclear how to add headers to the response, which
is where `make_response` is particularly useful in solving that specific
problem.

`make_response` can also be imported directly from the `flask` module
instead of `flask.helpers` so you will typically see that shortcut
in example code.

<a href="/flask-helpers-flash-examples.html">flash</a>,
<a href="/flask-helpers-get-root-path-examples.html">get_root_path</a>,
<a href="/flask-helpers-safe-join-examples.html">safe_join</a>,
<a href="/flask-helpers-send-file-examples.html">send_file</a>,
and <a href="/flask-helpers-url-for-examples.html">url_for</a>
are several other callables with code examples from the same `flask.helpers` package.

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

[**Flask AppBuilder / flask_appbuilder / security / decorators.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/security/decorators.py)

```python
# decorators.py
import functools
import logging

~~from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
from flask_jwt_extended import verify_jwt_in_request
from flask_login import current_user

from .._compat import as_unicode
from ..const import (
    FLAMSG_ERR_SEC_ACCESS_DENIED,
    LOGMSG_ERR_SEC_ACCESS_DENIED,
    PERMISSION_PREFIX,
)

log = logging.getLogger(__name__)


def protect(allow_browser_login=False):

    def _protect(f):
        if hasattr(f, "_permission_name"):
            permission_str = f._permission_name
        else:
            permission_str = f.__name__

        def wraps(self, *args, **kwargs):
            permission_str = "{}{}".format(PERMISSION_PREFIX, f._permission_name)
            if self.method_permission_name:


## ... source file abbreviated to get to make_response examples ...


    return functools.update_wrapper(wraps, f)


def has_access_api(f):
    if hasattr(f, "_permission_name"):
        permission_str = f._permission_name
    else:
        permission_str = f.__name__

    def wraps(self, *args, **kwargs):
        permission_str = "{}{}".format(PERMISSION_PREFIX, f._permission_name)
        if self.method_permission_name:
            _permission_name = self.method_permission_name.get(f.__name__)
            if _permission_name:
                permission_str = "{}{}".format(PERMISSION_PREFIX, _permission_name)
        if permission_str in self.base_permissions and self.appbuilder.sm.has_access(
            permission_str, self.class_permission_name
        ):
            return f(self, *args, **kwargs)
        else:
            log.warning(
                LOGMSG_ERR_SEC_ACCESS_DENIED.format(
                    permission_str, self.__class__.__name__
                )
            )
~~            response = make_response(
                jsonify(
                    {"message": str(FLAMSG_ERR_SEC_ACCESS_DENIED), "severity": "danger"}
                ),
                401,
            )
            response.headers["Content-Type"] = "application/json"
            return response

    f._permission_name = permission_str
    return functools.update_wrapper(wraps, f)


def permission_name(name):

    def wraps(f):
        f._permission_name = name
        return f

    return wraps



## ... source file continues with no further make_response examples...

```


## Example 2 from Flask-HTTPAuth
[Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth)
([documentation](https://flask-httpauth.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/Flask-HTTPAuth/))
is a [Flask](/flask.html) framework extension that creates
Basic and Digest HTTP authentication for routes. This project
is primarily built and maintained by
[Miguel Grinberg](https://blog.miguelgrinberg.com/). It is provided
as open source under the
[MIT license](https://github.com/miguelgrinberg/Flask-HTTPAuth/blob/master/LICENSE).

[**Flask-HTTPAuth / flask_httpauth.py**](https://github.com/miguelgrinberg/Flask-HTTPAuth/blob/master/././flask_httpauth.py)

```python
# flask_httpauth.py

from base64 import b64decode
from functools import wraps
from hashlib import md5
from random import Random, SystemRandom
~~from flask import request, make_response, session, g
from werkzeug.datastructures import Authorization
from werkzeug.security import safe_str_cmp

__version__ = '4.1.1dev'


class HTTPAuth(object):
    def __init__(self, scheme=None, realm=None, header=None):
        self.scheme = scheme
        self.realm = realm or "Authentication Required"
        self.header = header
        self.get_password_callback = None
        self.get_user_roles_callback = None
        self.auth_error_callback = None

        def default_get_password(username):
            return None

        def default_auth_error(status):
            return "Unauthorized Access", status

        self.get_password(default_get_password)
        self.error_handler(default_auth_error)

    def get_password(self, f):
        self.get_password_callback = f
        return f

    def get_user_roles(self, f):
        self.get_user_roles_callback = f
        return f

    def error_handler(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            res = f(*args, **kwargs)
~~            res = make_response(res)
            if res.status_code == 200:
                res.status_code = 401
            if 'WWW-Authenticate' not in res.headers.keys():
                res.headers['WWW-Authenticate'] = self.authenticate_header()
            return res
        self.auth_error_callback = decorated
        return decorated

    def authenticate_header(self):
        return '{0} realm="{1}"'.format(self.scheme, self.realm)

    def get_auth(self):
        auth = None
        if self.header is None or self.header == 'Authorization':
            auth = request.authorization
            if auth is None and 'Authorization' in request.headers:
                try:
                    auth_type, token = request.headers['Authorization'].split(
                        None, 1)
                    auth = Authorization(auth_type, {'token': token})
                except (ValueError, KeyError):
                    pass
        elif self.header in request.headers:
            auth = Authorization(self.scheme,


## ... source file continues with no further make_response examples...

```


## Example 3 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / cors.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./cors.py)

```python
# cors.py
from __future__ import unicode_literals

from datetime import timedelta
~~from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(
    origin=None,
    methods=None,
    headers=None,
    expose_headers=None,
    max_age=21600,
    attach_to_all=True,
    automatic_options=True,
    credentials=False,
):
    if methods is not None:
        methods = ", ".join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ", ".join(x.upper() for x in headers)
    if expose_headers is not None and not isinstance(expose_headers, str):
        expose_headers = ", ".join(x.upper() for x in expose_headers)
    if not isinstance(origin, str):
        origin = ", ".join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers["allow"]

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == "OPTIONS":
                resp = current_app.make_default_options_response()
            else:
~~                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != "OPTIONS":
                return resp

            h = resp.headers

            h["Access-Control-Allow-Origin"] = origin
            h["Access-Control-Allow-Methods"] = get_methods()
            h["Access-Control-Max-Age"] = str(max_age)
            if credentials:
                h["Access-Control-Allow-Credentials"] = "true"
            if headers is not None:
                h["Access-Control-Allow-Headers"] = headers
            if expose_headers is not None:
                h["Access-Control-Expose-Headers"] = expose_headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator



## ... source file continues with no further make_response examples...

```


## Example 4 from Flask-Security-Too
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

[**Flask-Security-Too / flask_security / views.py**](https://github.com/Flask-Middleware/flask-security/blob/master/flask_security/./views.py)

```python
# views.py

import time

from flask import (
    Blueprint,
    abort,
    after_this_request,
    current_app,
    jsonify,
    request,
    session,
)
from flask_login import current_user
from werkzeug.datastructures import MultiDict
from werkzeug.local import LocalProxy

from .changeable import change_user_password
from .confirmable import (
    confirm_email_token_status,
    confirm_user,
    send_confirmation_instructions,
)
from .decorators import anonymous_user_required, auth_required, unauth_csrf
from .passwordless import login_token_status, send_login_instructions
from .quart_compat import get_quart_status
from .unified_signin import (
    us_signin,
    us_signin_send_code,
    us_qrcode,
    us_setup,
    us_setup_validate,
    us_verify,
    us_verify_link,
    us_verify_send_code,
)


## ... source file abbreviated to get to make_response examples ...


    get_message,
    get_post_login_redirect,
    get_post_logout_redirect,
    get_post_register_redirect,
    get_post_verify_redirect,
    get_request_attr,
    get_url,
    json_error_response,
    login_user,
    logout_user,
    send_mail,
    slash_url_suffix,
    suppress_form_csrf,
    url_for_security,
)

if get_quart_status():  # pragma: no cover
    from quart import make_response, redirect

    async def _commit(response=None):
        _datastore.commit()
        return response


else:
~~    from flask import make_response, redirect

    def _commit(response=None):
        _datastore.commit()
        return response


_security = LocalProxy(lambda: current_app.extensions["security"])
_datastore = LocalProxy(lambda: _security.datastore)


def default_render_json(payload, code, headers, user):
    if headers is None:
        headers = dict()
    headers["Content-Type"] = "application/json"
    payload = dict(meta=dict(code=code), response=payload)
~~    return make_response(jsonify(payload), code, headers)


def _ctx(endpoint):
    return _security._run_ctx_processor(endpoint)


@unauth_csrf(fall_through=True)
def login():

    if current_user.is_authenticated and request.method == "POST":

        if _security._want_json(request):
            payload = json_error_response(
                errors=get_message("ANONYMOUS_USER_REQUIRED")[0]
            )
            return _security._render_json(payload, 400, None, None)
        else:
            return redirect(get_url(_security.post_login_view))

    form_class = _security.login_form

    if request.is_json:
        if request.content_length:
            form = form_class(MultiDict(request.get_json()), meta=suppress_form_csrf())


## ... source file continues with no further make_response examples...

```


## Example 5 from newspie
[NewsPie](https://github.com/skamieniarz/newspie) is a minimalistic news
aggregator created with [Flask](/flask.html) and the
[News API](https://newsapi.org/).

NewsPie is provided as open source under the
[MIT license](https://github.com/skamieniarz/newspie/blob/master/LICENSE).

[**newspie / news.py**](https://github.com/skamieniarz/newspie/blob/master/././news.py)

```python
# news.py
import configparser
import json
import logging
import os

import requests
import requests_cache
from dateutil import parser
~~from flask import (Flask, make_response, redirect, render_template, request,
                   url_for)

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
API_KEY = os.environ.get('NEWS_API_KEY')
TOP_HEADLINES = CONFIG['ENDPOINTS']['TOP_HEADLINES']
EVERYTHING = CONFIG['ENDPOINTS']['EVERYTHING']
PAGE_SIZE = int(CONFIG['VARIOUS']['PAGE_SIZE'])

CATEGORIES = ('general', 'sports', 'business', 'entertainment', 'health',
              'science', 'technology')
with open('data/countries.json') as json_file:
    COUNTRIES = json.load(json_file)

logging.basicConfig(level=logging.DEBUG)
requests_cache.install_cache(cache_name='news_cache',
                             backend='sqlite',
                             expire_after=300)

APP = Flask(__name__)


@APP.route('/', methods=['GET', 'POST'])
def root():


## ... source file abbreviated to get to make_response examples ...


    if request.method == 'POST':
        return do_post(page, category='search', current_query=query)
    response = requests.get(EVERYTHING,
                            params=params,
                            headers={'Authorization': API_KEY})
    pages = count_pages(response.json())
    if page > pages:
        page = pages
        return redirect(url_for('search', query=query, page=page))
    articles = parse_articles(response.json())
    return render(articles,
                  page,
                  pages,
                  country=get_cookie('country'),
                  category='search')


def do_post(page, category='general', current_query=None):
    new_query = request.form.get('search_query')
    country = request.form.get('country')
    next_page = request.form.get('next_page')
    previous_page = request.form.get('previous_page')
    if new_query is not None and new_query != '':
        return redirect(url_for('search', query=new_query, page=1))
    if country is not None and country != get_cookie('country'):
~~        response = make_response(
            redirect(url_for('category', category=category, page=1)))
        response.set_cookie('country', country)
        return response
    if next_page is not None:
        page = int(next_page) + 1
    elif previous_page is not None:
        page = int(previous_page) - 1
    if category == 'search':
        return redirect(url_for('search', query=current_query, page=page))
    return redirect(url_for('category', category=category, page=page))


def parse_articles(response):
    parsed_articles = []
    if response.get('status') == 'ok':
        for article in response.get('articles'):
            parsed_articles.append({
                'published_at':
                    parser.isoparse(article['publishedAt']
                                   ).strftime('%Y-%m-%d %H:%M'),
                'title':
                    article['title'],
                'url':
                    article['url'],


## ... source file continues with no further make_response examples...

```


## Example 6 from sandman2
[sandman2](https://github.com/jeffknupp/sandman2)
([project documentation](https://sandman2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/sandman2/))
is a code library for automatically generating
[RESTful APIs](/application-programming-interfaces.html) from
existing database schemas. This approach is handy for solving
straightforward situations where you want to put an abstraction
layer between one or more applications and your
[relational database](/databases.html) to prevent or reduce
direct database access.

The sandman2 project is provided under the
[Apache License 2.0](https://github.com/jeffknupp/sandman2/blob/master/LICENSE).

[**sandman2 / sandman2 / service.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./service.py)

```python
# service.py

~~from flask import request, make_response
import flask
from flask.views import MethodView
from sqlalchemy import asc, desc

from sandman2.exception import NotFoundException, BadRequestException
from sandman2.model import db
from sandman2.decorators import etag, validate_fields


def add_link_headers(response, links):
    link_string = '<{}>; rel=self'.format(links['self'])
    for link in links.values():
        link_string += ', <{}>; rel=related'.format(link)
    response.headers['Link'] = link_string
    return response


def jsonify(resource):

    response = flask.jsonify(resource.to_dict())
    response = add_link_headers(response, resource.links())
    return response




## ... source file abbreviated to get to make_response examples ...


            for key, value in args.items():
                if value.startswith('%'):
                    filters.append(getattr(self.__model__, key).like(str(value), escape='/'))
                elif key == 'sort':
                    direction = desc if value.startswith('-') else asc
                    order.append(direction(getattr(self.__model__, value.lstrip('-'))))
                elif key == 'limit':
                    limit = int(value)
                elif hasattr(self.__model__, key):
                    filters.append(getattr(self.__model__, key) == value)
                else:
                    raise BadRequestException('Invalid field [{}]'.format(key))
            queryset = queryset.filter(*filters).order_by(*order)
        if 'page' in request.args:
            resources = queryset.paginate(page=int(request.args['page']), per_page=limit).items
        else:
            queryset = queryset.limit(limit)
            resources = queryset.all()
        return [r.to_dict() for r in resources]

    def _export(self, collection):
        fieldnames = collection[0].keys()
        faux_csv = ','.join(fieldnames) + '\r\n'
        for resource in collection:
            faux_csv += ','.join((str(x) for x in resource.values())) + '\r\n'
~~        response = make_response(faux_csv)
        response.mimetype = 'text/csv'
        return response


    @staticmethod
    def _no_content_response():
~~        response = make_response()
        response.status_code = 204
        return response

    @staticmethod
    def _created_response(resource):
        response = jsonify(resource)
        response.status_code = 201
        return response



## ... source file continues with no further make_response examples...

```

