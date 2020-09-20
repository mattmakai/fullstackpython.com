title: flask.helpers url_for Example Code
category: page
slug: flask-helpers-url-for-examples
sortorder: 500021023
toc: False
sidebartitle: flask.helpers url_for
meta: Python example code that shows how to use the url_for callable from the flask.helpers module of the Flask project.


[url_for](https://github.com/pallets/flask/blob/master/src/flask/helpers.py)
is function in the [Flask](/flask.html) `flask.helpers` module.
`url_for` generates a URL to an endpoint using the method passed in
as an argument.

Note that `url_for` is typically imported directly from `flask` instead of
from `flask.helpers`, even though it is defined within the `helpers` module.
It is the same function that is imported, but it's less characters to type
when you leave off the `.helpers` part.

<a href="/flask-helpers-flash-examples.html">flash</a>,
<a href="/flask-helpers-get-root-path-examples.html">get_root_path</a>,
<a href="/flask-helpers-make-response-examples.html">make_response</a>,
<a href="/flask-helpers-safe-join-examples.html">safe_join</a>,
and <a href="/flask-helpers-send-file-examples.html">send_file</a>
are several other callables with code examples from the same `flask.helpers` package.

## Example 1 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [Flask](/flask.html). The application can be used
as-is to run CTF events, or modified for custom rules for related
scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / tests / test_views.py**](https://github.com/CTFd/CTFd/blob/master/./tests/test_views.py)

```python
# test_views.py

import os

~~from flask import url_for
from freezegun import freeze_time

from CTFd.cache import clear_pages
from CTFd.utils import set_config
from CTFd.utils.config.pages import get_pages
from CTFd.utils.encoding import hexencode
from tests.helpers import (
    create_ctfd,
    destroy_ctfd,
    gen_challenge,
    gen_file,
    gen_page,
    login_as_user,
    register_user,
)


def test_index():
    app = create_ctfd()
    with app.app_context():
        with app.test_client() as client:
            r = client.get("/")
            assert r.status_code == 200
    destroy_ctfd(app)


## ... source file abbreviated to get to url_for examples ...


        register_user(app)
        client = login_as_user(app)
        r = client.get("/profile")
        assert r.status_code == 200
    destroy_ctfd(app)


def test_user_can_access_files():
    app = create_ctfd()
    with app.app_context():
        from CTFd.utils.uploads import rmdir

        chal = gen_challenge(app.db)
        chal_id = chal.id
        path = app.config.get("UPLOAD_FOLDER")

        location = os.path.join(path, "test_file_path", "test.txt")
        directory = os.path.dirname(location)
        model_path = os.path.join("test_file_path", "test.txt")

        try:
            os.makedirs(directory)
            with open(location, "wb") as obj:
                obj.write("testing file load".encode())
            gen_file(app.db, location=model_path, challenge_id=chal_id)
~~            url = url_for("views.files", path=model_path)

            set_config("challenge_visibility", "public")
            with app.test_client() as client:
                r = client.get(url)

                assert r.status_code == 200
                assert r.get_data(as_text=True) == "testing file load"

            set_config("challenge_visibility", "private")
            with app.test_client() as client:
                r = client.get(url)

                assert r.status_code == 403
                assert r.get_data(as_text=True) != "testing file load"

            register_user(app)
            client = login_as_user(app)
            r = client.get(url)
            assert r.status_code == 200
            assert r.get_data(as_text=True) == "testing file load"

            with freeze_time("2017-10-5"):
                set_config("start", "1507262400")
                for v in ("public", "private"):


## ... source file abbreviated to get to url_for examples ...


        finally:
            rmdir(directory)
    destroy_ctfd(app)


def test_user_can_access_files_with_auth_token():
    app = create_ctfd()
    with app.app_context():
        from CTFd.utils.uploads import rmdir

        chal = gen_challenge(app.db)
        chal_id = chal.id
        path = app.config.get("UPLOAD_FOLDER")

        md5hash = hexencode(os.urandom(16))

        location = os.path.join(path, md5hash, "test.txt")
        directory = os.path.dirname(location)
        model_path = os.path.join(md5hash, "test.txt")

        try:
            os.makedirs(directory)
            with open(location, "wb") as obj:
                obj.write("testing file load".encode())
            gen_file(app.db, location=model_path, challenge_id=chal_id)
~~            url = url_for("views.files", path=model_path)

            register_user(app)
            with login_as_user(app) as client:
                req = client.get("/api/v1/challenges/1")
                data = req.get_json()
                file_url = data["data"]["files"][0]

            with app.test_client() as client:
                r = client.get(url)
                assert r.status_code == 403
                assert r.get_data(as_text=True) != "testing file load"

                r = client.get(
~~                    url_for(
                        "views.files",
                        path=model_path,
                        token="random_token_that_shouldnt_work",
                    )
                )
                assert r.status_code == 403
                assert r.get_data(as_text=True) != "testing file load"

                r = client.get(file_url)
                assert r.status_code == 200
                assert r.get_data(as_text=True) == "testing file load"

                set_config("challenge_visibility", "admins")
                r = client.get(file_url)
                assert r.status_code == 403
                assert r.get_data(as_text=True) != "testing file load"
                set_config("challenge_visibility", "private")

                with freeze_time("2017-10-5"):
                    set_config("start", "1507262400")

                    r = client.get(file_url)
                    assert r.status_code == 403
                    assert r.get_data(as_text=True) != "testing file load"


## ... source file continues with no further url_for examples...

```


## Example 2 from Flask AppBuilder
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

[**Flask AppBuilder / flask_appbuilder / menu.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/./menu.py)

```python
# menu.py
from typing import List

~~from flask import current_app, url_for
from flask_babel import gettext as __

from .api import BaseApi, expose
from .basemanager import BaseManager
from .security.decorators import permission_name, protect


class MenuItem(object):
    def __init__(self, name, href="", icon="", label="", childs=None, baseview=None):
        self.name = name
        self.href = href
        self.icon = icon
        self.label = label
        self.childs = childs or []
        self.baseview = baseview

    def get_url(self):
        if not self.href:
            if not self.baseview:
                return ""
            else:
~~                return url_for(f"{self.baseview.endpoint}.{self.baseview.default_view}")
        else:
            try:
~~                return url_for(self.href)
            except Exception:
                return self.href

    def __repr__(self):
        return self.name


class Menu(object):
    def __init__(self, reverse=True, extra_classes=""):
        self.menu = []
        if reverse:
            extra_classes = extra_classes + "navbar-inverse"
        self.extra_classes = extra_classes

    @property
    def reverse(self):
        return "navbar-inverse" in self.extra_classes

    def get_list(self):
        return self.menu

    def get_flat_name_list(self, menu: "Menu" = None, result: List = None) -> List:
        menu = menu or self.menu
        result = result or []


## ... source file continues with no further url_for examples...

```


## Example 3 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / markup.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/./markup.py)

```python
# markup.py
import logging
import re

import mistune
~~from flask import url_for
from jinja2 import Markup
from pluggy import HookimplMarker
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

impl = HookimplMarker('flaskbb')

logger = logging.getLogger(__name__)

_re_user = re.compile(r'@(\w+)', re.I)


def userify(match):
    value = match.group(1)
    user = "<a href='{url}'>@{user}</a>".format(
~~        url=url_for("user.profile", username=value, _external=False),
        user=value
    )
    return user


class FlaskBBRenderer(mistune.Renderer):

    def __init__(self, **kwargs):
        super(FlaskBBRenderer, self).__init__(**kwargs)

    def paragraph(self, text):

        text = _re_user.sub(userify, text)
        return super(FlaskBBRenderer, self).paragraph(text)

    def block_code(self, code, lang):
        if lang:
            try:
                lexer = get_lexer_by_name(lang, stripall=True)
            except ClassNotFound:
                lexer = None
        else:
            lexer = None
        if not lexer:


## ... source file continues with no further url_for examples...

```


## Example 4 from flask-base
[flask-base](https://github.com/hack4impact/flask-base)
([project documentation](http://hack4impact.github.io/flask-base/))
provides boilerplate code for new [Flask](/flask.html) web apps.
The purpose of the boilerplate is to stitch together disparate
libraries that are commonly used in Flask projects, such as
[Redis](/redis.html) for fast caching and transient data storage,
[SendGrid](https://www.twilio.com/sendgrid) for transactional email,
[SQLAlchemy](/sqlalchemy.html) for persistent data storage through a
[relational database](/databases.html) backend,
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) for form
handling and many others.

flask-base is provided as open source under the
[MIT license](https://github.com/hack4impact/flask-base/blob/master/LICENSE.md).

[**flask-base / app / utils.py**](https://github.com/hack4impact/flask-base/blob/master/app/./utils.py)

```python
# utils.py
~~from flask import url_for
from wtforms.fields import Field
from wtforms.widgets import HiddenInput
from wtforms.compat import text_type


def register_template_utils(app):

    @app.template_test()
    def equalto(value, other):
        return value == other

    @app.template_global()
    def is_hidden_field(field):
        from wtforms.fields import HiddenField
        return isinstance(field, HiddenField)

    app.add_template_global(index_for_role)


def index_for_role(role):
~~    return url_for(role.index)


class CustomSelectField(Field):
    widget = HiddenInput()

    def __init__(self, label='', validators=None, multiple=False,
                 choices=[], allow_custom=True, **kwargs):
        super(CustomSelectField, self).__init__(label, validators, **kwargs)
        self.multiple = multiple
        self.choices = choices
        self.allow_custom = allow_custom

    def _value(self):
        return text_type(self.data) if self.data is not None else ''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[1]
            self.raw_data = [valuelist[1]]
        else:
            self.data = ''



## ... source file continues with no further url_for examples...

```


## Example 5 from flask-bones
[flask-bones](https://github.com/cburmeister/flask-bones)
([demo](http://flask-bones.herokuapp.com/))
is large scale [Flask](/flask.html) example application built
with [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
([example Blueprint code](/flask-blueprints-blueprint-examples.html)).
This project is provided as open source under the
[MIT license](https://github.com/cburmeister/flask-bones/blob/master/LICENSE).

[**flask-bones / app / utils.py**](https://github.com/cburmeister/flask-bones/blob/master/app/./utils.py)

```python
# utils.py
~~from flask import request, url_for


def url_for_other_page(**kwargs):
    url_for_args = request.args.copy()
    if 'pjax' in url_for_args:
        url_for_args.pop('_pjax')
    for key, value in kwargs.items():
        url_for_args[key] = value
~~    return url_for(request.endpoint, **url_for_args)



## ... source file continues with no further url_for examples...

```


## Example 6 from Flask-Bootstrap
[flask-bootstrap](https://github.com/mbr/flask-bootstrap)
([PyPI package information](https://pypi.org/project/Flask-Bootstrap/))
makes it easier to use the [Bootstrap CSS framework](/bootstrap-css.html)
in your [Flask](/flask.html) applications with less boilerplate
code. The project was primarily created by
[Marc Brinkmann @mbr](https://github.com/mbr) and the source code is
open sourced under the
[Apache 2.0 license](https://github.com/mbr/flask-bootstrap/blob/master/LICENSE).

[**Flask-Bootstrap / flask_bootstrap / __init__.py**](https://github.com/mbr/flask-bootstrap/blob/master/flask_bootstrap/./__init__.py)

```python
# __init__.py

import re

~~from flask import Blueprint, current_app, url_for

try:
    from wtforms.fields import HiddenField
except ImportError:

    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:

    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


from .forms import render_form

__version__ = '3.3.7.1.dev1'
BOOTSTRAP_VERSION = re.sub(r'^(\d+\.\d+\.\d+).*', r'\1', __version__)
JQUERY_VERSION = '1.12.4'
HTML5SHIV_VERSION = '3.7.3'
RESPONDJS_VERSION = '1.4.2'


class CDN(object):

    def get_resource_url(self, filename):
        raise NotImplementedError


class StaticCDN(object):

    def __init__(self, static_endpoint='static', rev=False):
        self.static_endpoint = static_endpoint
        self.rev = rev

    def get_resource_url(self, filename):
        extra_args = {}

        if self.rev and current_app.config['BOOTSTRAP_QUERYSTRING_REVVING']:
            extra_args['bootstrap'] = __version__

~~        return url_for(self.static_endpoint, filename=filename, **extra_args)


class WebCDN(object):

    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_resource_url(self, filename):
        return self.baseurl + filename


class ConditionalCDN(object):

    def __init__(self, confvar, primary, fallback):
        self.confvar = confvar
        self.primary = primary
        self.fallback = fallback

    def get_resource_url(self, filename):
        if current_app.config[self.confvar]:
            return self.primary.get_resource_url(filename)
        return self.fallback.get_resource_url(filename)




## ... source file continues with no further url_for examples...

```


## Example 7 from flask-debugtoolbar
[Flask Debug-toolbar](https://github.com/flask-debugtoolbar/flask-debugtoolbar)
([documentation](https://flask-debugtoolbar.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/Flask-DebugToolbar/))
is a [Flask](/flask.html) conversion of the popular
[Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
project. This extension creates a sidebar with useful debugging
information when you are running a Flask application in development
mode. The project is provided as open source under
[this license](https://github.com/flask-debugtoolbar/flask-debugtoolbar/blob/master/LICENSE).

[**flask-debugtoolbar / flask_debugtoolbar / toolbar.py**](https://github.com/flask-debugtoolbar/flask-debugtoolbar/blob/master/flask_debugtoolbar/./toolbar.py)

```python
# toolbar.py
try:
    from urllib.parse import unquote
except ImportError:
    from urllib import unquote

~~from flask import url_for, current_app
from werkzeug.utils import import_string


class DebugToolbar(object):

    _cached_panel_classes = {}

    def __init__(self, request, jinja_env):
        self.jinja_env = jinja_env
        self.request = request
        self.panels = []

        self.template_context = {
~~            'static_path': url_for('_debug_toolbar.static', filename='')
        }

        self.create_panels()

    def create_panels(self):
        activated = self.request.cookies.get('fldt_active', '')
        activated = unquote(activated).split(';')

        for panel_class in self._iter_panels(current_app):
            panel_instance = panel_class(jinja_env=self.jinja_env,
                                         context=self.template_context)

            if panel_instance.dom_id() in activated:
                panel_instance.is_active = True

            self.panels.append(panel_instance)

    def render_toolbar(self):
        context = self.template_context.copy()
        context.update({'panels': self.panels})

        template = self.jinja_env.get_template('base.html')
        return template.render(**context)



## ... source file continues with no further url_for examples...

```


## Example 8 from flask-login
[Flask-Login](https://github.com/maxcountryman/flask-login)
([project documentation](https://flask-login.readthedocs.io/en/latest/)
and [PyPI package](https://pypi.org/project/Flask-Login/))
is a [Flask](/flask.html) extension that provides user session
management, which handles common tasks such as logging in
and out of a [web application](/web-development.html) and
managing associated user session data. Flask-Login is
open sourced under the
[MIT license](https://github.com/maxcountryman/flask-login/blob/master/LICENSE).

[**flask-login / flask_login / utils.py**](https://github.com/maxcountryman/flask-login/blob/master/flask_login/./utils.py)

```python
# utils.py


import hmac
from hashlib import sha512
from functools import wraps
from werkzeug.local import LocalProxy
from werkzeug.security import safe_str_cmp
from werkzeug.urls import url_decode, url_encode

~~from flask import (_request_ctx_stack, current_app, request, session, url_for,
                   has_request_context)

from ._compat import text_type, urlparse, urlunparse
from .config import COOKIE_NAME, EXEMPT_METHODS
from .signals import user_logged_in, user_logged_out, user_login_confirmed


current_user = LocalProxy(lambda: _get_user())


def encode_cookie(payload, key=None):
    return u'{0}|{1}'.format(payload, _cookie_digest(payload, key=key))


def decode_cookie(cookie, key=None):
    try:
        payload, digest = cookie.rsplit(u'|', 1)
        if hasattr(digest, 'decode'):
            digest = digest.decode('ascii')  # pragma: no cover
    except ValueError:
        return

    if safe_str_cmp(_cookie_digest(payload, key=key), digest):
        return payload


def make_next_param(login_url, current_url):
    l_url = urlparse(login_url)
    c_url = urlparse(current_url)

    if (not l_url.scheme or l_url.scheme == c_url.scheme) and \
            (not l_url.netloc or l_url.netloc == c_url.netloc):
        return urlunparse(('', '', c_url.path, c_url.params, c_url.query, ''))
    return current_url


def expand_login_view(login_view):
    if login_view.startswith(('https://', 'http://', '/')):
        return login_view
    else:
        if request.view_args is None:
~~            return url_for(login_view)
        else:
~~            return url_for(login_view, **request.view_args)


def login_url(login_view, next_url=None, next_field='next'):
    base = expand_login_view(login_view)

    if next_url is None:
        return base

    parsed_result = urlparse(base)
    md = url_decode(parsed_result.query)
    md[next_field] = make_next_param(base, next_url)
    netloc = current_app.config.get('FORCE_HOST_FOR_REDIRECTS') or \
        parsed_result.netloc
    parsed_result = parsed_result._replace(netloc=netloc,
                                           query=url_encode(md, sort=True))
    return urlunparse(parsed_result)


def login_fresh():
    return session.get('_fresh', False)


def login_user(user, remember=False, duration=None, force=False, fresh=True):
    if not force and not user.is_active:


## ... source file continues with no further url_for examples...

```


## Example 9 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / apidoc.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./apidoc.py)

```python
# apidoc.py
from __future__ import unicode_literals

~~from flask import url_for, Blueprint, render_template


class Apidoc(Blueprint):

    def __init__(self, *args, **kwargs):
        self.registered = False
        super(Apidoc, self).__init__(*args, **kwargs)

    def register(self, *args, **kwargs):
        super(Apidoc, self).register(*args, **kwargs)
        self.registered = True


apidoc = Apidoc(
    "restx_doc",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/swaggerui",
)


@apidoc.add_app_template_global
def swagger_static(filename):
~~    return url_for("restx_doc.static", filename=filename)


def ui_for(api):
    return render_template("swagger-ui.html", title=api.title, specs_url=api.specs_url)



## ... source file continues with no further url_for examples...

```


## Example 10 from flaskSaaS
[flaskSaas](https://github.com/alectrocute/flaskSaaS) is a boilerplate
starter project to build a software-as-a-service (SaaS) web application
in [Flask](/flask.html), with [Stripe](/stripe.html) for billing. The
boilerplate relies on many common Flask extensions such as
[Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/),
[Flask-Login](https://flask-login.readthedocs.io/en/latest/),
[Flask-Admin](https://flask-admin.readthedocs.io/en/latest/), and
many others. The project is provided as open source under the
[MIT license](https://github.com/alectrocute/flaskSaaS/blob/master/LICENSE).

[**flaskSaaS / app / views / user.py**](https://github.com/alectrocute/flaskSaaS/blob/master/app/views/user.py)

```python
# user.py
~~from flask import (Blueprint, render_template, redirect, request, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required, current_user
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import user as user_forms
from app.toolbox import email
import stripe
import json
from json import dumps

stripe_keys = {
	'secret_key': "sk_test_GvpPOs0XFxeP0fQiWMmk6HYe",
	'publishable_key': "pk_test_UU62FhsIB6457uPiUX6mJS5x"
}

stripe.api_key = stripe_keys['secret_key']

ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

userbp = Blueprint('userbp', __name__, url_prefix='/user')


@userbp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = user_forms.SignUp()
    if form.validate_on_submit():
        user = models.User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data,
            email=form.email.data,
            confirmation=False,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        subject = 'Please confirm your email address.'
        token = ts.dumps(user.email, salt='email-confirm-key')
~~        confirmUrl = url_for('userbp.confirm', token=token, _external=True)
        html = render_template('email/confirm.html',
                               confirm_url=confirmUrl)
        email.send(user.email, subject, html)
        flash('Check your emails to confirm your email address.', 'positive')
        return redirect(url_for('index'))
    return render_template('user/signup.html', form=form, title='Sign up')


@userbp.route('/confirm/<token>', methods=['GET', 'POST'])
def confirm(token):
    try:
        email = ts.loads(token, salt='email-confirm-key', max_age=86400)
    except:
        abort(404)
    user = models.User.query.filter_by(email=email).first()
    user.confirmation = True
    db.session.commit()
    flash(
        'Your email address has been confirmed, you can sign in.', 'positive')
    return redirect(url_for('userbp.signin'))


@userbp.route('/signin', methods=['GET', 'POST'])
def signin():


## ... source file abbreviated to get to url_for examples ...


            return redirect(url_for('userbp.signin'))
    return render_template('user/signin.html', form=form, title='Sign in')


@userbp.route('/signout')
def signout():
    logout_user()
    flash('Succesfully signed out.', 'positive')
    return redirect(url_for('index'))


@userbp.route('/account')
@login_required
def account():
    return render_template('user/account.html', title='Account')


@userbp.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = user_forms.Forgot()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is not None:
            subject = 'Reset your password.'
            token = ts.dumps(user.email, salt='password-reset-key')
~~            resetUrl = url_for('userbp.reset', token=token, _external=True)
            html = render_template('email/reset.html', reset_url=resetUrl)
            email.send(user.email, subject, html)
            flash('Check your emails to reset your password.', 'positive')
            return redirect(url_for('index'))
        else:
            flash('Unknown email address.', 'negative')
            return redirect(url_for('userbp.forgot'))
    return render_template('user/forgot.html', form=form)


@userbp.route('/reset/<token>', methods=['GET', 'POST'])
def reset(token):
    try:
        email = ts.loads(token, salt='password-reset-key', max_age=86400)
    except:
        abort(404)
    form = user_forms.Reset()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=email).first()
        if user is not None:
            user.password = form.password.data
            db.session.commit()
            flash('Your password has been reset, you can sign in.', 'positive')
            return redirect(url_for('userbp.signin'))


## ... source file continues with no further url_for examples...

```


## Example 11 from Flask-Security-Too
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

~~from flask import _request_ctx_stack, current_app, flash, g, request, session, url_for
from flask.json import JSONEncoder
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


## ... source file abbreviated to get to url_for examples ...


        return url


def slash_url_suffix(url, suffix):

    return url.endswith("/") and ("%s/" % suffix) or ("/%s" % suffix)


def transform_url(url, qparams=None, **kwargs):
    if not url:
        return url
    link_parse = urlsplit(url)
    if qparams:
        current_query = dict(parse_qsl(link_parse.query))
        current_query.update(qparams)
        link_parse = link_parse._replace(query=urlencode(current_query))
    return urlunsplit(link_parse._replace(**kwargs))


def get_security_endpoint_name(endpoint):
    return f"{_security.blueprint_name}.{endpoint}"


def url_for_security(endpoint, **values):
    endpoint = get_security_endpoint_name(endpoint)
~~    return url_for(endpoint, **values)


def validate_redirect_url(url):
    if url is None or url.strip() == "":
        return False
    url_next = urlsplit(url)
    url_base = urlsplit(request.host_url)
    if (url_next.netloc or url_next.scheme) and url_next.netloc != url_base.netloc:
        base_domain = current_app.config.get("SERVER_NAME")
        if (
            config_value("REDIRECT_ALLOW_SUBDOMAINS")
            and base_domain
            and (
                url_next.netloc == base_domain
                or url_next.netloc.endswith(f".{base_domain}")
            )
        ):
            return True
        else:
            return False
    return True


def get_post_action_redirect(config_key, declared=None):


## ... source file continues with no further url_for examples...

```


## Example 12 from Flask-User
[Flask-User](https://github.com/lingthio/Flask-User)
([PyPI information](https://pypi.org/project/Flask-User/)
and
[project documentation](https://flask-user.readthedocs.io/en/latest/))
is a [Flask](/flask.html) extension that makes it easier to add
custom user account management and authentication to the projects
you are building. The extension supports persistent data storage
through both [relational databases](/databases.html) and
[MongoDB](/mongodb.html). The project is provided as open source under
the [MIT license](https://github.com/lingthio/Flask-User/blob/master/LICENSE.txt).

[**Flask-User / flask_user / email_manager.py**](https://github.com/lingthio/Flask-User/blob/master/flask_user/./email_manager.py)

```python
# email_manager.py


~~from flask import render_template, url_for

from flask_user import ConfigError

class EmailManager(object):

    def __init__(self, app):
        self.app = app
        self.user_manager = app.user_manager
        self.sender_name = self.user_manager.USER_EMAIL_SENDER_NAME
        self.sender_email = self.user_manager.USER_EMAIL_SENDER_EMAIL

        if not self.sender_email:
            raise ConfigError('Config setting USER_EMAIL_SENDER_EMAIL is missing.')

        if '@' not in self.sender_email:
            raise ConfigError('Config setting USER_EMAIL_SENDER_EMAIL is not a valid email address.')


    def send_confirm_email_email(self, user, user_email):
        
        if not self.user_manager.USER_ENABLE_EMAIL: return
        if not self.user_manager.USER_ENABLE_CONFIRM_EMAIL: return

        email = user_email.email if user_email else user.email

        object_id = user_email.id if user_email else user.id
        token = self.user_manager.generate_token(object_id)
~~        confirm_email_link = url_for('user.confirm_email', token=token, _external=True)

        self._render_and_send_email(
            email,
            user,
            self.user_manager.USER_CONFIRM_EMAIL_TEMPLATE,
            confirm_email_link=confirm_email_link,
        )

    def send_password_changed_email(self, user):

        if not self.user_manager.USER_ENABLE_EMAIL: return
        if not self.user_manager.USER_SEND_PASSWORD_CHANGED_EMAIL: return

        user_or_user_email_object = self.user_manager.db_manager.get_primary_user_email_object(user)
        email = user_or_user_email_object.email

        self._render_and_send_email(
            email,
            user,
            self.user_manager.USER_PASSWORD_CHANGED_EMAIL_TEMPLATE,
        )

    def send_reset_password_email(self, user, user_email):

        if not self.user_manager.USER_ENABLE_EMAIL: return
        assert self.user_manager.USER_ENABLE_FORGOT_PASSWORD

        email = user_email.email if user_email else user.email

        token = self.user_manager.generate_token(user.id)
~~        reset_password_link = url_for('user.reset_password', token=token, _external=True)

        self._render_and_send_email(
            email,
            user,
            self.user_manager.USER_RESET_PASSWORD_EMAIL_TEMPLATE,
            reset_password_link=reset_password_link,
        )

    def send_invite_user_email(self, user, user_invitation):

        if not self.user_manager.USER_ENABLE_EMAIL: return
        if not self.user_manager.USER_ENABLE_INVITE_USER: return

        invited_by_user = user

        email = user_invitation.email

        user = self.user_manager.db_manager.UserClass(email=email)

        token = self.user_manager.generate_token(user_invitation.id)
~~        accept_invitation_link = url_for('user.register', token=token, _external=True)

        self._render_and_send_email(
            email,
            user,
            self.user_manager.USER_INVITE_USER_EMAIL_TEMPLATE,
            accept_invitation_link=accept_invitation_link,
            invited_by_user=invited_by_user,
        )

    def send_registered_email(self, user, user_email, request_email_confirmation):

        if not self.user_manager.USER_ENABLE_EMAIL: return
        if not self.user_manager.USER_SEND_REGISTERED_EMAIL: return

        email = user_email.email if user_email else user.email

        if request_email_confirmation:
            token = self.user_manager.generate_token(user_email.id if user_email else user.id)
~~            confirm_email_link = url_for('user.confirm_email', token=token, _external=True)
        else:
            confirm_email_link = None

        self._render_and_send_email(
            email,
            user,
            self.user_manager.USER_REGISTERED_EMAIL_TEMPLATE,
            confirm_email_link=confirm_email_link,
        )

    def send_username_changed_email(self, user):

        if not self.user_manager.USER_ENABLE_EMAIL: return
        if not self.user_manager.USER_SEND_USERNAME_CHANGED_EMAIL: return

        user_or_user_email_object = self.user_manager.db_manager.get_primary_user_email_object(user)
        email = user_or_user_email_object.email

        self._render_and_send_email(
            email,
            user,
            self.user_manager.USER_USERNAME_CHANGED_EMAIL_TEMPLATE,
        )



## ... source file continues with no further url_for examples...

```


## Example 13 from Flasky
[Flasky](https://github.com/miguelgrinberg/flasky) is a wonderful
example application by
[Miguel Grinberg](https://github.com/miguelgrinberg) that he builds
while teaching developers how to use [Flask](/flask.html) in
[his books and videos](https://courses.miguelgrinberg.com/). Flasky
is [open sourced under the MIT license](https://github.com/miguelgrinberg/flasky/blob/master/LICENSE).

[**Flasky / app / models.py**](https://github.com/miguelgrinberg/flasky/blob/master/./app/models.py)

```python
# models.py
from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
~~from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
from app.exceptions import ValidationError
from . import db, login_manager


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:


## ... source file abbreviated to get to url_for examples ...



    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        if user.id is None:
            return False
        return self.followed.filter_by(
            followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        if user.id is None:
            return False
        return self.followers.filter_by(
            follower_id=user.id).first() is not None

    @property
    def followed_posts(self):
        return Post.query.join(Follow, Follow.followed_id == Post.author_id)\
            .filter(Follow.follower_id == self.id)

    def to_json(self):
        json_user = {
~~            'url': url_for('api.get_user', id=self.id),
            'username': self.username,
            'member_since': self.member_since,
            'last_seen': self.last_seen,
~~            'posts_url': url_for('api.get_user_posts', id=self.id),
~~            'followed_posts_url': url_for('api.get_user_followed_posts',
                                          id=self.id),
            'post_count': self.posts.count()
        }
        return json_user

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):


## ... source file abbreviated to get to url_for examples ...


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

    def to_json(self):
        json_post = {
~~            'url': url_for('api.get_post', id=self.id),
            'body': self.body,
            'body_html': self.body_html,
            'timestamp': self.timestamp,
~~            'author_url': url_for('api.get_user', id=self.author_id),
~~            'comments_url': url_for('api.get_post_comments', id=self.id),
            'comment_count': self.comments.count()
        }
        return json_post

    @staticmethod
    def from_json(json_post):
        body = json_post.get('body')
        if body is None or body == '':
            raise ValidationError('post does not have a body')
        return Post(body=body)


db.event.listen(Post.body, 'set', Post.on_changed_body)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    disabled = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i',
                        'strong']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

    def to_json(self):
        json_comment = {
~~            'url': url_for('api.get_comment', id=self.id),
~~            'post_url': url_for('api.get_post', id=self.post_id),
            'body': self.body,
            'body_html': self.body_html,
            'timestamp': self.timestamp,
~~            'author_url': url_for('api.get_user', id=self.author_id),
        }
        return json_comment

    @staticmethod
    def from_json(json_comment):
        body = json_comment.get('body')
        if body is None or body == '':
            raise ValidationError('comment does not have a body')
        return Comment(body=body)


db.event.listen(Comment.body, 'set', Comment.on_changed_body)



## ... source file continues with no further url_for examples...

```


## Example 14 from Datadog Flask Example App
The [Datadog Flask example app](https://github.com/DataDog/trace-examples/tree/master/python/flask)
contains many examples of the [Flask](/flask.html) core functions
available to a developer using the [web framework](/web-frameworks.html).

[**Datadog Flask Example App / python/flask/app / app.py**](https://github.com/DataDog/trace-examples/blob/master/python/flask/app/./app.py)

```python
# app.py
from ddtrace import patch_all; patch_all(flask=True, requests=True)  # noqa

from ddtrace import tracer

from flask import Flask, Response
from flask import after_this_request
~~from flask import abort, jsonify, render_template, url_for
from flask.views import View
from werkzeug.routing import Rule

from flask_caching import Cache
from flask_cors import CORS

import requests

from .blueprint import bp
from .exceptions import AppException
from .limiter import limiter
from .signals import connect_signals

app = Flask(__name__)

app.register_blueprint(bp)

connect_signals(app)

CORS(app)
Cache(app, config=dict(CACHE_TYPE='simple'))
limiter.init_app(app)




## ... source file abbreviated to get to url_for examples ...


@app.after_request
def after_request(response):
    print('Hook: after_request')
    return response


@app.teardown_request
def teardown_request(response):
    print('Hook: teardown_request')
    return response


@app.teardown_appcontext
def teardown_appcontext(appcontext):
    print('Hook: teardown_appcontext')


@app.route('/')
@limiter.limit('10 per second')
def index():
    routes = [
        dict(
            rule='GET /',
            description=['Endpoint for this page, which uses <code>render_template()</code>.'],
            links=[
~~                dict(label='GET /', url=url_for('index')),
            ],
        ),
        dict(
            rule='GET /joke',
            description=[
                'Endpoint which uses <code>requests</code> to fetch a joke from icanhazdadjoke.com.',
                'This endpoint also registers a <code>flask.after_this_request</code> hook.'
            ],
            links=[
~~                dict(label='GET /joke', url=url_for('joke')),
            ],
        ),
        dict(
            rule='GET /json',
            description=[
                'Endpoint which uses <code>jsonify</code> to return a JSON object to the user.',
            ],
            links=[
~~                dict(label='GET /json', url=url_for('json')),
            ],
        ),
        dict(
            rule='GET /custom-endpoint/<msg>',
            description=[
                ('Endpoint which was registered manually using <code>@app.endpoint()</code> '
                 'and <code>app.add_url_rule()</code>'),
                'This endpoint also has a /custom-endpoint/ url configured with a default <msg>',
                ('We have also attached a @tracer.wrap() to the endpoint and added a '
                 'with tracer.trace(): to the body of the view as well.'),
            ],
            links=[
~~                dict(label='GET /custom-endpoint', url=url_for('custom-endpoint')),
~~                dict(label='GET /custom-endpoint/hello', url=url_for('custom-endpoint', msg='hello')),
            ],
        ),
        dict(
            rule='GET /custom-error',
            description=[
                'Endpoint which raises a customer user-defined Exception (non HTTPException)',
            ],
            links=[
~~                dict(label='GET /custom-error', url=url_for('custom_error')),
            ],
        ),
        dict(
            rule='GET /stream',
            description=[
                'Endpoint which uses a generator to stream the response back to the user.',
            ],
            links=[
~~                dict(label='GET /stream', url=url_for('stream')),
            ],
        ),
        dict(
            rule='GET /abort/<int:code>',
            description=[
                'Endpoint which calls <code>abort(code)</code> for us',
            ],
            links=[
~~                dict(label='GET /abort/{}'.format(code), url=url_for('abort_endpoint', code=code))
                for code in [400, 401, 403, 404, 500]
            ],
        ),
        dict(
            rule='GET /hello/<name>',
            description=[
                'Endpoint which was generated from a <code>flask.views.View</code>',
            ],
            links=[
~~                dict(label='GET /hello/Flask', url=url_for('myview', name='Flask')),
            ],
        ),
        dict(
            rule='GET /bp/<name>',
            description=[
                'Blueprint endpoint that uses <code>render_template_string()</code>',
            ],
            links=[
~~                dict(label='GET /bp/', url=url_for('bp.index')),
            ],
        ),
        dict(
            rule='GET /bp/unknown',
            description=[
                'Blueprint endpoint that calls <code>abort(404)</code>',
            ],
            links=[
~~                dict(label='GET /bp/unkown', url=url_for('bp.unknown')),
            ],
        ),
        dict(
            rule='GET /static/test.txt',
            description=[
                'Endpoint to fetch a simple .txt static file.',
            ],
            links=[
~~                dict(label='GET /static/test.txt', url=url_for('static', filename='test.txt')),
            ],
        ),
    ]
    return render_template('index.jinja2', routes=routes)


@app.route('/joke')
def joke():
    res = requests.get('https://icanhazdadjoke.com/', headers=dict(Accept='text/plain'))
    res.raise_for_status()

    @after_this_request
    def after_joke(response):
        print('Hook: after_this_request')
        return response

    return res.content


@app.route('/json')
def json():
    return jsonify(hello='world')




## ... source file continues with no further url_for examples...

```

