title: flask.templating render_template_string Example Code
category: page
slug: flask-templating-render-template-string-examples
sortorder: 500021032
toc: False
sidebartitle: flask.templating render_template_string
meta: Python example code that shows how to use the render_template_string callable from the flask.templating module of the Flask project.


[render_template_string](https://github.com/pallets/flask/blob/master/src/flask/templating.py)
is a [Flask](/flask.html) function from the `flask.templating` package.
`render_template` is used to generate output from a string
that is passed in rather than from a file in the templates folder.

Note that `render_template_string` is sometimes imported from the `flask`
package instead of from `flask.templating`. It is the same function that is
imported, but there are less characters to type when you leave off
the `.templating` part.

<a href="/flask-templating-render-template-examples.html">render_template</a>
is another callable from the `flask.templating` package with code examples.

These subjects go along with the `render_template_string` code examples:

* [template engines](/template-engines.html), specifically [Jinja2](/jinja2.html)
* [Flask](/flask.html) and the concepts for [web frameworks](/web-frameworks.html)
* [Cascading Style Sheets (CSS)](/cascading-style-sheets.html) and [web design](/web-design.html)


## Example 1 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [Flask](/flask.html). The application can be used
as-is to run CTF events, or modified for custom rules for related
scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / tests / test_themes.py**](https://github.com/CTFd/CTFd/blob/master/./tests/test_themes.py)

```python
# test_themes.py

import os
import shutil

import pytest
~~from flask import render_template, render_template_string, request
from jinja2.exceptions import TemplateNotFound
from jinja2.sandbox import SecurityError
from werkzeug.test import Client

from CTFd.config import TestingConfig
from CTFd.utils import get_config, set_config
from tests.helpers import create_ctfd, destroy_ctfd, gen_user, login_as_user


def test_themes_run_in_sandbox():
    app = create_ctfd()
    with app.app_context():
        try:
            app.jinja_env.from_string(
                "{{ ().__class__.__bases__[0].__subclasses__()[40]('./test_utils.py').read() }}"
            ).render()
        except SecurityError:
            pass
        except Exception as e:
            raise e
    destroy_ctfd(app)


def test_themes_cant_access_configpy_attributes():


## ... source file abbreviated to get to render_template_string examples ...


            except TemplateNotFound:
                pass
            try:
                r = client.get("/themes/foo_fallback/static/js/pages/main.dev.js")
            except TemplateNotFound:
                pass
    destroy_ctfd(app)

    app = create_ctfd()
    with app.app_context():
        set_config("ctf_theme", "foo_fallback")
        assert app.config["THEME_FALLBACK"] == True
        with app.test_client() as client:
            r = client.get("/")
            assert r.status_code == 200
            r = client.get("/themes/foo_fallback/static/js/pages/main.dev.js")
            assert r.status_code == 200
    destroy_ctfd(app)

    os.rmdir(os.path.join(app.root_path, "themes", "foo_fallback"))


def test_theme_template_loading_by_prefix():
    app = create_ctfd()
    with app.test_request_context():
~~        tpl1 = render_template_string("{% extends 'core/page.html' %}", content="test")
        tpl2 = render_template("page.html", content="test")
        assert tpl1 == tpl2


def test_theme_template_disallow_loading_admin_templates():
    app = create_ctfd()
    with app.app_context():
        try:
            filename = os.path.join(
                app.root_path, "themes", "foo_disallow", "admin", "malicious.html"
            )
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            set_config("ctf_theme", "foo_disallow")
            with open(filename, "w") as f:
                f.write("malicious")

            with pytest.raises(TemplateNotFound):
~~                render_template_string("{% include 'admin/malicious.html' %}")
        finally:
            shutil.rmtree(
                os.path.join(app.root_path, "themes", "foo_disallow"),
                ignore_errors=True,
            )



## ... source file continues with no further render_template_string examples...

```


## Example 2 from Flask-User
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

[**Flask-User / flask_user / tests / tst_app.py**](https://github.com/lingthio/Flask-User/blob/master/flask_user/tests/tst_app.py)

```python
# tst_app.py
import os
import datetime
~~from flask import Flask, render_template_string, request
from flask_babelex import Babel
from flask_user import login_required, roles_required, UserManager, UserMixin

ORM_type = 'SQLAlchemy'   # SQLAlchemy  or MongoEngine


app = Flask(__name__)

class ConfigClass(object):
    SECRET_KEY = 'Test with short key'  # Less than 32 bytes

    SQLALCHEMY_DATABASE_URI = 'sqlite:///tst_app.sqlite'    # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    MONGODB_SETTINGS = {
        'db': 'tst_app',
        'host': 'mongodb://localhost:27017/tst_app'
    }

    MAIL_USERNAME =           os.getenv('MAIL_USERNAME',        'email@example.com')
    MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD',        'password')
    MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER',  '"TestApp" <noreply@example.com>')
    MAIL_SERVER =             os.getenv('MAIL_SERVER',          'smtp.gmail.com')
    MAIL_PORT =           int(os.getenv('MAIL_PORT',            '465'))


## ... source file abbreviated to get to render_template_string examples ...


    assert user_manager.USER_EMAIL_SENDER_EMAIL=='noreply@example.com'

    db_manager = user_manager.db_manager
    db_manager.drop_all_tables()
    db_manager.create_all_tables()

    token = user_manager.generate_token('abc', 123, 'xyz')
    data_items = user_manager.token_manager.verify_token(token, 3600)
    assert data_items is not None
    assert data_items[0] == 'abc'
    assert data_items[1] == 123
    assert data_items[2] == 'xyz'

    user = db_manager.add_user(username='member', email='member@example.com',
            password=user_manager.hash_password('Password1'), email_confirmed_at=datetime.datetime.utcnow())
    db_manager.commit()

    user = db_manager.add_user(username='user007', email='admin@example.com',
            password=user_manager.hash_password('Password1'))
    db_manager.add_user_role(user, 'secret')
    db_manager.add_user_role(user, 'agent')
    db_manager.commit()

    @app.route('/')
    def home_page():
~~        return render_template_string("""
            {% extends "flask_user_layout.html" %}
            {% block content %}
            <h2>{%trans%}Home Page{%endtrans%}</h2>
            <p><a href="{{ url_for('user.login') }}">{%trans%}Sign in{%endtrans%}</a></p>
            {% endblock %}
            {% extends "flask_user_layout.html" %}
            {% block content %}
            <h2>{%trans%}Profile Page{%endtrans%}</h2>
            <p> {%trans%}Hello{%endtrans%}
                {{ current_user.username or current_user.email }},</p>
            <p> <a href="{{ url_for('user.change_username') }}">
                {%trans%}Change username{%endtrans%}</a></p>
            <p> <a href="{{ url_for('user.change_password') }}">
                {%trans%}Change password{%endtrans%}</a></p>
            <p> <a href="{{ url_for('user.logout') }}?next={{ url_for('user.login') }}">
                {%trans%}Sign out{%endtrans%}</a></p>
            {% endblock %}
            {% extends "flask_user_layout.html" %}
            {% block content %}
            <h2>{%trans%}Admin Page{%endtrans%}</h2>
            {% endblock %}



## ... source file continues with no further render_template_string examples...

```


## Example 3 from Datadog Flask Example App
The [Datadog Flask example app](https://github.com/DataDog/trace-examples/tree/master/python/flask)
contains many examples of the [Flask](/flask.html) core functions
available to a developer using the [web framework](/web-frameworks.html).

[**Datadog Flask Example App / python/flask/app / blueprint.py**](https://github.com/DataDog/trace-examples/blob/master/python/flask/app/./blueprint.py)

```python
# blueprint.py
from ddtrace import Pin
~~from flask import abort, Blueprint, render_template_string

from .limiter import limiter


bp = Blueprint('bp', __name__, url_prefix='/bp/')

Pin.override(bp, service='flask-bp', app='flask', app_type='web')


@bp.before_request
def bp_before_request():
    print('Hook: bp_before_request')


@bp.before_app_request
def bp_before_app_request():
    print('Hook: bp_before_app_request')


@bp.before_app_first_request
def bp_before_app_first_request():
    print('Hook: bp_before_app_first_request')




## ... source file abbreviated to get to render_template_string examples ...


    print('Hook: bp_after_request')
    return response


@bp.after_app_request
def bp_after_app_request(response):
    print('Hook: bp_after_app_request')
    return response


@bp.teardown_request
def bp_teardown_request(response):
    print('Hook: bp_teardown_request')
    return response


@bp.teardown_app_request
def bp_teardown_app_request(response):
    print('Hook: bp_teardown_app_request')
    return response


@bp.route('/')
@limiter.limit('10 per second')
def index():
~~    return render_template_string('<h1>Blueprint</h1>')


@bp.route('/unknown')
@limiter.exempt
def unknown():
    abort(404)


@bp.errorhandler(404)
def bp_not_found(e):
    return 'oh no....', 404



## ... source file continues with no further render_template_string examples...

```

