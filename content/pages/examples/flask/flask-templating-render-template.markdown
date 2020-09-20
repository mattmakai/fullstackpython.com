title: flask.templating render_template Example Code
category: page
slug: flask-templating-render-template-examples
sortorder: 500021031
toc: False
sidebartitle: flask.templating render_template
meta: Python example code that shows how to use the render_template callable from the flask.templating module of the Flask project.


[render_template](https://github.com/pallets/flask/blob/master/src/flask/templating.py)
is a [Flask](/flask.html) function from the `flask.templating` package.
`render_template` is used to generate output from a
[template file based on the Jinja2 engine](/template-engines.html)
that is found in the application's templates folder.

Note that `render_template` is typically imported directly from the `flask`
package instead of from `flask.templating`. It is the same function that is
imported, but there are less characters to type when you leave off
the `.templating` part.

<a href="/flask-templating-render-template-string-examples.html">render_template_string</a>
is another callable from the `flask.templating` package with code examples.

These topics are also useful while reading the `render_template` examples:

* [template engines](/template-engines.html), specifically [Jinja2](/jinja2.html)
* [Flask](/flask.html) and the concepts for [web frameworks](/web-frameworks.html)
* [Cascading Style Sheets (CSS)](/cascading-style-sheets.html) and [web design](/web-design.html)


## Example 1 from Braintree Flask app
[Braintree's Flask example payments app](https://github.com/braintree/braintree_flask_example)
demonstrates how to incorporate this payment provider's
[API](/application-programming-interfaces.html) into your
[Flask](/flask.html) [web application](/web-development.html).
The code is open sourced under the
[MIT license](https://github.com/braintree/braintree_flask_example/blob/master/LICENSE).

[**Braintree Flask app / app.py**](https://github.com/braintree/braintree_flask_example/blob/master/././app.py)

```python
# app.py
~~from flask import Flask, redirect, url_for, render_template, request, flash

import os
from os.path import join, dirname
from dotenv import load_dotenv
import braintree
from gateway import generate_client_token, transact, find_transaction

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

PORT = int(os.environ.get('PORT', 4567))

TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('new_checkout'))

@app.route('/checkouts/new', methods=['GET'])
def new_checkout():
    client_token = generate_client_token()
~~    return render_template('checkouts/new.html', client_token=client_token)

@app.route('/checkouts/<transaction_id>', methods=['GET'])
def show_checkout(transaction_id):
    transaction = find_transaction(transaction_id)
    result = {}
    if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        result = {
            'header': 'Sweet Success!',
            'icon': 'success',
            'message': 'Your test transaction has been successfully processed. See the Braintree API response and try again.'
        }
    else:
        result = {
            'header': 'Transaction Failed',
            'icon': 'fail',
            'message': 'Your test transaction has a status of ' + transaction.status + '. See the Braintree API response and try again.'
        }

~~    return render_template('checkouts/show.html', transaction=transaction, result=result)

@app.route('/checkouts', methods=['POST'])
def create_checkout():
    result = transact({
        'amount': request.form['amount'],
        'payment_method_nonce': request.form['payment_method_nonce'],
        'options': {
            "submit_for_settlement": True
        }
    })

    if result.is_success or result.transaction:
        return redirect(url_for('show_checkout',transaction_id=result.transaction.id))
    else:
        for x in result.errors.deep_errors: flash('Error: %s: %s' % (x.code, x.message))
        return redirect(url_for('new_checkout'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)



## ... source file continues with no further render_template examples...

```


## Example 2 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [Flask](/flask.html). The application can be used
as-is to run CTF events, or modified for custom rules for related
scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / CTFd / auth.py**](https://github.com/CTFd/CTFd/blob/master/./CTFd/auth.py)

```python
# auth.py
import base64

import requests
from flask import Blueprint
from flask import current_app as app
~~from flask import redirect, render_template, request, session, url_for
from itsdangerous.exc import BadSignature, BadTimeSignature, SignatureExpired

from CTFd.cache import clear_team_session, clear_user_session
from CTFd.models import Teams, UserFieldEntries, UserFields, Users, db
from CTFd.utils import config, email, get_app_config, get_config
from CTFd.utils import user as current_user
from CTFd.utils import validators
from CTFd.utils.config import is_teams_mode
from CTFd.utils.config.integrations import mlc_registration
from CTFd.utils.config.visibility import registration_visible
from CTFd.utils.crypto import verify_password
from CTFd.utils.decorators import ratelimit
from CTFd.utils.decorators.visibility import check_registration_visibility
from CTFd.utils.helpers import error_for, get_errors, markup
from CTFd.utils.logging import log
from CTFd.utils.modes import TEAMS_MODE
from CTFd.utils.security.auth import login_user, logout_user
from CTFd.utils.security.signing import unserialize
from CTFd.utils.validators import ValidationError

auth = Blueprint("auth", __name__)


@auth.route("/confirm", methods=["POST", "GET"])
@auth.route("/confirm/<data>", methods=["POST", "GET"])
@ratelimit(method="POST", limit=10, interval=60)
def confirm(data=None):
    if not get_config("verify_emails"):
        return redirect(url_for("challenges.listing"))

    if data and request.method == "GET":
        try:
            user_email = unserialize(data, max_age=1800)
        except (BadTimeSignature, SignatureExpired):
~~            return render_template(
                "confirm.html", errors=["Your confirmation link has expired"]
            )
        except (BadSignature, TypeError, base64.binascii.Error):
~~            return render_template(
                "confirm.html", errors=["Your confirmation token is invalid"]
            )

        user = Users.query.filter_by(email=user_email).first_or_404()
        if user.verified:
            return redirect(url_for("views.settings"))

        user.verified = True
        log(
            "registrations",
            format="[{date}] {ip} - successful confirmation for {name}",
            name=user.name,
        )
        db.session.commit()
        clear_user_session(user_id=user.id)
        email.successful_registration_notification(user.email)
        db.session.close()
        if current_user.authed():
            return redirect(url_for("challenges.listing"))
        return redirect(url_for("auth.login"))

    if current_user.authed() is False:
        return redirect(url_for("auth.login"))

    user = Users.query.filter_by(id=session["id"]).first_or_404()
    if user.verified:
        return redirect(url_for("views.settings"))

    if data is None:
        if request.method == "POST":
            email.verify_email_address(user.email)
            log(
                "registrations",
                format="[{date}] {ip} - {name} initiated a confirmation email resend",
            )
~~            return render_template(
                "confirm.html", infos=[f"Confirmation email sent to {user.email}!"]
            )
        elif request.method == "GET":
~~            return render_template("confirm.html")


@auth.route("/reset_password", methods=["POST", "GET"])
@auth.route("/reset_password/<data>", methods=["POST", "GET"])
@ratelimit(method="POST", limit=10, interval=60)
def reset_password(data=None):
    if config.can_send_mail() is False:
~~        return render_template(
            "reset_password.html",
            errors=[
                markup(
                    "This CTF is not configured to send email.<br> Please contact an organizer to have your password reset."
                )
            ],
        )

    if data is not None:
        try:
            email_address = unserialize(data, max_age=1800)
        except (BadTimeSignature, SignatureExpired):
~~            return render_template(
                "reset_password.html", errors=["Your link has expired"]
            )
        except (BadSignature, TypeError, base64.binascii.Error):
~~            return render_template(
                "reset_password.html", errors=["Your reset token is invalid"]
            )

        if request.method == "GET":
~~            return render_template("reset_password.html", mode="set")
        if request.method == "POST":
            password = request.form.get("password", "").strip()
            user = Users.query.filter_by(email=email_address).first_or_404()
            if user.oauth_id:
~~                return render_template(
                    "reset_password.html",
                    infos=[
                        "Your account was registered via an authentication provider and does not have an associated password. Please login via your authentication provider."
                    ],
                )

            pass_short = len(password) == 0
            if pass_short:
~~                return render_template(
                    "reset_password.html", errors=["Please pick a longer password"]
                )

            user.password = password
            db.session.commit()
            clear_user_session(user_id=user.id)
            log(
                "logins",
                format="[{date}] {ip} -  successful password reset for {name}",
                name=user.name,
            )
            db.session.close()
            email.password_change_alert(user.email)
            return redirect(url_for("auth.login"))

    if request.method == "POST":
        email_address = request.form["email"].strip()
        user = Users.query.filter_by(email=email_address).first()

        get_errors()

        if not user:
~~            return render_template(
                "reset_password.html",
                infos=[
                    "If that account exists you will receive an email, please check your inbox"
                ],
            )

        if user.oauth_id:
~~            return render_template(
                "reset_password.html",
                infos=[
                    "The email address associated with this account was registered via an authentication provider and does not have an associated password. Please login via your authentication provider."
                ],
            )

        email.forgot_password(email_address)

~~        return render_template(
            "reset_password.html",
            infos=[
                "If that account exists you will receive an email, please check your inbox"
            ],
        )
~~    return render_template("reset_password.html")


@auth.route("/register", methods=["POST", "GET"])
@check_registration_visibility
@ratelimit(method="POST", limit=10, interval=5)
def register():
    errors = get_errors()
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email_address = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        website = request.form.get("website")
        affiliation = request.form.get("affiliation")
        country = request.form.get("country")

        name_len = len(name) == 0
        names = Users.query.add_columns("name", "id").filter_by(name=name).first()
        emails = (
            Users.query.add_columns("email", "id")
            .filter_by(email=email_address)
            .first()
        )
        pass_short = len(password) == 0


## ... source file abbreviated to get to render_template examples ...


            errors.append(
                "Only email addresses under {domains} may register".format(
                    domains=get_config("domain_whitelist")
                )
            )
        if names:
            errors.append("That user name is already taken")
        if team_name_email_check is True:
            errors.append("Your user name cannot be an email address")
        if emails:
            errors.append("That email has already been used")
        if pass_short:
            errors.append("Pick a longer password")
        if pass_long:
            errors.append("Pick a shorter password")
        if name_len:
            errors.append("Pick a longer user name")
        if valid_website is False:
            errors.append("Websites must be a proper URL starting with http or https")
        if valid_country is False:
            errors.append("Invalid country")
        if valid_affiliation is False:
            errors.append("Please provide a shorter affiliation")

        if len(errors) > 0:
~~            return render_template(
                "register.html",
                errors=errors,
                name=request.form["name"],
                email=request.form["email"],
                password=request.form["password"],
            )
        else:
            with app.app_context():
                user = Users(name=name, email=email_address, password=password)

                if website:
                    user.website = website
                if affiliation:
                    user.affiliation = affiliation
                if country:
                    user.country = country

                db.session.add(user)
                db.session.commit()
                db.session.flush()

                for field_id, value in entries.items():
                    entry = UserFieldEntries(
                        field_id=field_id, value=value, user_id=user.id


## ... source file abbreviated to get to render_template examples ...



                if config.can_send_mail() and get_config(
                    "verify_emails"
                ):  # Confirming users is enabled and we can send email.
                    log(
                        "registrations",
                        format="[{date}] {ip} - {name} registered (UNCONFIRMED) with {email}",
                    )
                    email.verify_email_address(user.email)
                    db.session.close()
                    return redirect(url_for("auth.confirm"))
                else:  # Don't care about confirming users
                    if (
                        config.can_send_mail()
                    ):  # We want to notify the user that they have registered.
                        email.successful_registration_notification(user.email)

        log("registrations", "[{date}] {ip} - {name} registered with {email}")
        db.session.close()

        if is_teams_mode():
            return redirect(url_for("teams.private"))

        return redirect(url_for("challenges.listing"))
    else:
~~        return render_template("register.html", errors=errors)


@auth.route("/login", methods=["POST", "GET"])
@ratelimit(method="POST", limit=10, interval=5)
def login():
    errors = get_errors()
    if request.method == "POST":
        name = request.form["name"]

        if validators.validate_email(name) is True:
            user = Users.query.filter_by(email=name).first()
        else:
            user = Users.query.filter_by(name=name).first()

        if user:
            if user and verify_password(request.form["password"], user.password):
                session.regenerate()

                login_user(user)
                log("logins", "[{date}] {ip} - {name} logged in")

                db.session.close()
                if request.args.get("next") and validators.is_safe_url(
                    request.args.get("next")
                ):
                    return redirect(request.args.get("next"))
                return redirect(url_for("challenges.listing"))

            else:
                log("logins", "[{date}] {ip} - submitted invalid password for {name}")
                errors.append("Your username or password is incorrect")
                db.session.close()
~~                return render_template("login.html", errors=errors)
        else:
            log("logins", "[{date}] {ip} - submitted invalid account information")
            errors.append("Your username or password is incorrect")
            db.session.close()
~~            return render_template("login.html", errors=errors)
    else:
        db.session.close()
~~        return render_template("login.html", errors=errors)


@auth.route("/oauth")
def oauth_login():
    endpoint = (
        get_app_config("OAUTH_AUTHORIZATION_ENDPOINT")
        or get_config("oauth_authorization_endpoint")
        or "https://auth.majorleaguecyber.org/oauth/authorize"
    )

    if get_config("user_mode") == "teams":
        scope = "profile team"
    else:
        scope = "profile"

    client_id = get_app_config("OAUTH_CLIENT_ID") or get_config("oauth_client_id")

    if client_id is None:
        error_for(
            endpoint="auth.login",
            message="OAuth Settings not configured. "
            "Ask your CTF administrator to configure MajorLeagueCyber integration.",
        )
        return redirect(url_for("auth.login"))


## ... source file continues with no further render_template examples...

```


## Example 3 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / email.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/./email.py)

```python
# email.py
import logging
~~from flask import render_template
from flask_mail import Message
from flask_babelplus import lazy_gettext as _

from flaskbb.extensions import mail, celery


logger = logging.getLogger(__name__)


@celery.task
def send_reset_token(token, username, email):
    send_email(
        subject=_("Password Recovery Confirmation"),
        recipients=[email],
~~        text_body=render_template(
            "email/reset_password.txt",
            username=username,
            token=token
        ),
~~        html_body=render_template(
            "email/reset_password.html",
            username=username,
            token=token
        )
    )


@celery.task
def send_activation_token(token, username, email):
    send_email(
        subject=_("Account Activation"),
        recipients=[email],
~~        text_body=render_template(
            "email/activate_account.txt",
            username=username,
            token=token
        ),
~~        html_body=render_template(
            "email/activate_account.html",
            username=username,
            token=token
        )
    )


@celery.task
def send_async_email(*args, **kwargs):
    send_email(*args, **kwargs)


def send_email(subject, recipients, text_body, html_body, sender=None):
    msg = Message(subject, recipients=recipients, sender=sender)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)



## ... source file continues with no further render_template examples...

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

[**flask-base / app / email.py**](https://github.com/hack4impact/flask-base/blob/master/app/./email.py)

```python
# email.py
import os

~~from flask import render_template
from flask_mail import Message

from app import create_app
from app import mail


def send_email(recipient, subject, template, **kwargs):
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        msg = Message(
            app.config['EMAIL_SUBJECT_PREFIX'] + ' ' + subject,
            sender=app.config['EMAIL_SENDER'],
            recipients=[recipient])
~~        msg.body = render_template(template + '.txt', **kwargs)
~~        msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)



## ... source file continues with no further render_template examples...

```


## Example 5 from flask-bones
[flask-bones](https://github.com/cburmeister/flask-bones)
([demo](http://flask-bones.herokuapp.com/))
is large scale [Flask](/flask.html) example application built
with [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
([example Blueprint code](/flask-blueprints-blueprint-examples.html)).
This project is provided as open source under the
[MIT license](https://github.com/cburmeister/flask-bones/blob/master/LICENSE).

[**flask-bones / app / __init__.py**](https://github.com/cburmeister/flask-bones/blob/master/app/./__init__.py)

```python
# __init__.py
import time

~~from flask import Flask, g, render_template, request
import arrow
import requests

from app import config
from app.assets import assets
from app.auth import auth
from app.commands import create_db, drop_db, populate_db, recreate_db
from app.database import db
from app.extensions import lm, travis, mail, migrate, bcrypt, babel, rq, limiter
from app.user import user
from app.utils import url_for_other_page


def create_app(config=config.base_config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_jinja_env(app)
    register_commands(app)

    def get_locale():
        return request.accept_languages.best_match(config.SUPPORTED_LOCALES)

    if babel.locale_selector_func is None:
        babel.locale_selector_func = get_locale

    @app.before_request
    def before_request():
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
        g.pjax = 'X-PJAX' in request.headers

    @app.route('/', methods=['GET'])
    def index():
~~        return render_template('index.html')

    return app


def register_commands(app):
    for command in [create_db, drop_db, populate_db, recreate_db]:
        app.cli.command()(command)


def register_extensions(app):
    travis.init_app(app)
    db.init_app(app)
    lm.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    assets.init_app(app)
    babel.init_app(app)
    rq.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)


def register_blueprints(app):
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(auth)


def register_errorhandlers(app):

    def render_error(e):
~~        return render_template('errors/%s.html' % e.code), e.code

    for e in [
        requests.codes.INTERNAL_SERVER_ERROR,
        requests.codes.NOT_FOUND,
        requests.codes.UNAUTHORIZED,
    ]:
        app.errorhandler(e)(render_error)


def register_jinja_env(app):
    app.jinja_env.globals.update({
        'timeago': lambda x: arrow.get(x).humanize(),
        'url_for_other_page': url_for_other_page,
    })



## ... source file continues with no further render_template examples...

```


## Example 6 from flask-bookshelf
[flask-bookshelf](https://github.com/damyanbogoev/flask-bookshelf) is the
example [Flask](/flask.html) application that developers create when
going through
[this Flask series of blog posts](https://damyanon.net/tags/flask-series/).

[**flask-bookshelf / bookshelf / __init__.py**](https://github.com/damyanbogoev/flask-bookshelf/blob/master/bookshelf/./__init__.py)

```python
# __init__.py
~~from flask import abort, Flask, g, render_template, request, current_app
from flask_babel import Babel
from flask_security import current_user
from bookshelf.utils import get_instance_folder_path
from bookshelf.main.controllers import main
from bookshelf.admin.controllers import admin
from bookshelf.cache import cache
from bookshelf.config import configure_app
from bookshelf.data.models import db

app = Flask(
    __name__,
    instance_path=get_instance_folder_path(),
    instance_relative_config=True,
    template_folder="templates",
)

babel = Babel(app)
configure_app(app)
cache.init_app(app)
db.init_app(app)
app.jinja_env.add_extension("jinja2.ext.loopcontrols")


@app.url_defaults


## ... source file abbreviated to get to render_template examples ...




@app.before_request
def ensure_lang_support():
    lang_code = g.get("lang_code", None)
    if lang_code and lang_code not in app.config["SUPPORTED_LANGUAGES"].keys():
        abort(404)


@babel.localeselector
def get_locale():
    return g.get("lang_code", app.config["BABEL_DEFAULT_LOCALE"])


@babel.timezoneselector
def get_timezone():
    user = g.get("user", None)
    if user is not None:
        return user.timezone
    return "UTC"


@app.errorhandler(404)
def page_not_found(error):
    current_app.logger.error("Page not found: %s", (request.path, error))
~~    return render_template("404.htm"), 404


@app.errorhandler(500)
def internal_server_error(error):
    current_app.logger.error("Server Error: %s", (error))
~~    return render_template("500.htm"), 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    current_app.logger.error("Unhandled Exception: %s", (error))
~~    return render_template("500.htm"), 500


@app.context_processor
def inject_data():
    return dict(user=current_user, lang_code=g.get("lang_code", None))


@app.route("/")
@app.route("/<lang_code>/")
@cache.cached(300)
def home(lang_code=None):
~~    return render_template("index.htm")


app.register_blueprint(main, url_prefix="/main")
app.register_blueprint(main, url_prefix="/<lang_code>/main")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(admin, url_prefix="/<lang_code>/admin")



## ... source file continues with no further render_template examples...

```


## Example 7 from flaskex
[Flaskex](https://github.com/anfederico/Flaskex) is a working example
[Flask](/flask.html) web application intended as a base to build your
own applications upon. The application comes with pre-built sign up, log in
and related screens, as well as a database backend. Flaskex is provided
as open source under the
[MIT license](https://github.com/anfederico/Flaskex/blob/master/LICENSE.txt).

[**flaskex / app.py**](https://github.com/anfederico/Flaskex/blob/master/././app.py)

```python
# app.py

from scripts import tabledef
from scripts import forms
from scripts import helpers
~~from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only


@app.route('/', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if form.validate():
                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
~~        return render_template('login.html', form=form)
    user = helpers.get_user()
~~    return render_template('home.html', user=user)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = helpers.hash_password(request.form['password'])
            email = request.form['email']
            if form.validate():
                if not helpers.username_taken(username):
                    helpers.add_user(username, password, email)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Signup successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'User/Pass required'})
~~        return render_template('login.html', form=form)
    return redirect(url_for('login'))


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if session.get('logged_in'):
        if request.method == 'POST':
            password = request.form['password']
            if password != "":
                password = helpers.hash_password(password)
            email = request.form['email']
            helpers.change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
~~        return render_template('settings.html', user=user)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")



## ... source file continues with no further render_template examples...

```


## Example 8 from flask_jsondash
[Flask JSONDash](https://github.com/christabor/flask_jsondash) is a
configurable web application built in Flask that creates charts and
dashboards from arbitrary API endpoints. Everything for the web app
is configured in JSON. The code is provided as open source under the
[MIT license](https://github.com/christabor/flask_jsondash/blob/master/LICENSE).

[**flask_jsondash / flask_jsondash / charts_builder.py**](https://github.com/christabor/flask_jsondash/blob/master/flask_jsondash/./charts_builder.py)

```python
# charts_builder.py


import json
import os
import uuid
from datetime import datetime as dt

import jinja2
~~from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, send_from_directory, url_for)

from flask_jsondash import static, templates

from flask_jsondash import db
from flask_jsondash import settings
from flask_jsondash.utils import setting
from flask_jsondash.utils import adapter
from flask_jsondash import utils
from flask_jsondash.schema import (
    validate_raw_json, InvalidSchemaError,
)

TEMPLATE_DIR = os.path.dirname(templates.__file__)
STATIC_DIR = os.path.dirname(static.__file__)

REQUIRED_STATIC_FAMILES = ['D3']

charts = Blueprint(
    'jsondash',
    __name__,
    template_folder=TEMPLATE_DIR,
    static_url_path=STATIC_DIR,
    static_folder=STATIC_DIR,


## ... source file abbreviated to get to render_template examples ...


            opts.update(
                filter=dict(created_by=setting('JSONDASH_GLOBAL_USER')))
            views += list(adapter.read(**opts))
    else:
        views = list(adapter.read(**opts))
    if views:
        pagination = utils.paginator(count=len(views),
                                     page=page, per_page=per_page)
        opts.update(limit=pagination.limit, skip=pagination.skip)
        views = views[pagination.skip:pagination.next]
    else:
        pagination = None
    categorized = utils.categorize_views(views)
    kwargs = dict(
        total=len(views),
        views=categorized,
        view=None,
        paginator=pagination,
        creating=True,
        can_edit_global=auth(authtype='edit_global'),
        total_modules=sum([
            len(view.get('modules', [])) for view in views
            if isinstance(view, dict)
        ]),
    )
~~    return render_template('pages/charts_index.html', **kwargs)


@charts.route('/charts/<c_id>', methods=['GET'])
def view(c_id):
    if not auth(authtype='view', view_id=c_id):
        flash('You do not have access to view this dashboard.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    viewjson = adapter.read(c_id=c_id)
    if not viewjson:
        flash('Could not find view: {}'.format(c_id), 'error')
        return redirect(url_for('jsondash.dashboard'))
    if '_id' in viewjson:
        viewjson.pop('_id')
    if 'modules' not in viewjson:
        flash('Invalid configuration - missing modules.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    active_charts = [v.get('family') for v in viewjson['modules']
                     if v.get('family') is not None]
    if metadata(key='username') == viewjson.get('created_by'):
        can_edit = True
    else:
        can_edit = auth(authtype='edit_others', view_id=c_id)
    layout_type = viewjson.get('layout', 'freeform')
    kwargs = dict(
        id=c_id,
        view=viewjson,
        categories=get_categories(),
        num_rows=(
            None if layout_type == 'freeform' else utils.get_num_rows(viewjson)
        ),
        modules=utils.sort_modules(viewjson),
        assets=get_active_assets(active_charts),
        can_edit=can_edit,
        can_edit_global=auth(authtype='edit_global'),
        is_global=utils.is_global_dashboard(viewjson),
    )
~~    return render_template('pages/chart_detail.html', **kwargs)


@charts.route('/charts/<c_id>/delete', methods=['POST'])
def delete(c_id):
    dash_url = url_for('jsondash.dashboard')
    if not auth(authtype='delete'):
        flash('You do not have access to delete dashboards.', 'error')
        return redirect(dash_url)
    adapter.delete(c_id)
    flash('Deleted dashboard "{}"'.format(c_id))
    return redirect(dash_url)


@charts.route('/charts/<c_id>/update', methods=['POST'])
def update(c_id):
    if not auth(authtype='update'):
        flash('You do not have access to update dashboards.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    viewjson = adapter.read(c_id=c_id)
    if not viewjson:
        flash('Could not find view: {}'.format(c_id), 'error')
        return redirect(url_for('jsondash.dashboard'))
    form_data = request.form
    view_url = url_for('jsondash.view', c_id=c_id)


## ... source file continues with no further render_template examples...

```


## Example 9 from flask-phone-input
[flask-phone-input](https://github.com/miguelgrinberg/flask-phone-input)
is an example application that ties together the
[intTellInput.js](https://github.com/jackocnr/intl-tel-input)
JavaScript plugin with the
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) form-handling
library. flask-phone-input is provided as open source under the
[MIT license](https://github.com/miguelgrinberg/flask-phone-input/blob/1a1c227c044474ce0fe133493d7f8b0fb8312409/LICENSE).

[**flask-phone-input / app.py**](https://github.com/miguelgrinberg/flask-phone-input/blob/master/././app.py)

```python
# app.py
~~from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import phonenumbers
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
Bootstrap(app)


class PhoneForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhoneForm()
    if form.validate_on_submit():
        session['phone'] = form.phone.data
        return redirect(url_for('show_phone'))
~~    return render_template('index.html', form=form)


@app.route('/showphone')
def show_phone():
~~    return render_template('show_phone.html', phone=session['phone'])



## ... source file continues with no further render_template examples...

```


## Example 10 from flask-restx
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
    return url_for("restx_doc.static", filename=filename)


def ui_for(api):
~~    return render_template("swagger-ui.html", title=api.title, specs_url=api.specs_url)



## ... source file continues with no further render_template examples...

```


## Example 11 from flaskSaaS
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
        confirmUrl = url_for('userbp.confirm', token=token, _external=True)
~~        html = render_template('email/confirm.html',
                               confirm_url=confirmUrl)
        email.send(user.email, subject, html)
        flash('Check your emails to confirm your email address.', 'positive')
        return redirect(url_for('index'))
~~    return render_template('user/signup.html', form=form, title='Sign up')


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
    form = user_forms.Login()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is not None:
            if user.check_password(form.password.data):
		if user.confirmation == True:
			login_user(user)			
			flash('Succesfully signed in.', 'positive')
			return redirect(url_for('userbp.account'))
		else:
                    flash('Confirm your email address first.', 'negative')
                    return redirect(url_for('userbp.signin'))
            else:
                flash('The password you have entered is wrong.', 'negative')
                return redirect(url_for('userbp.signin'))
        else:
            flash('Unknown email address.', 'negative')
            return redirect(url_for('userbp.signin'))
~~    return render_template('user/signin.html', form=form, title='Sign in')


@userbp.route('/signout')
def signout():
    logout_user()
    flash('Succesfully signed out.', 'positive')
    return redirect(url_for('index'))


@userbp.route('/account')
@login_required
def account():
~~    return render_template('user/account.html', title='Account')


@userbp.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = user_forms.Forgot()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is not None:
            subject = 'Reset your password.'
            token = ts.dumps(user.email, salt='password-reset-key')
            resetUrl = url_for('userbp.reset', token=token, _external=True)
~~            html = render_template('email/reset.html', reset_url=resetUrl)
            email.send(user.email, subject, html)
            flash('Check your emails to reset your password.', 'positive')
            return redirect(url_for('index'))
        else:
            flash('Unknown email address.', 'negative')
            return redirect(url_for('userbp.forgot'))
~~    return render_template('user/forgot.html', form=form)


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
        else:
            flash('Unknown email address.', 'negative')
            return redirect(url_for('userbp.forgot'))
~~    return render_template('user/reset.html', form=form, token=token)

@app.route('/user/pay')
@login_required
def pay():
    user = models.User.query.filter_by(email=current_user.email).first()
    if user.paid == 0:
~~    	return render_template('user/buy.html', key=stripe_keys['publishable_key'], email=current_user.email)
    return "You already paid."

@app.route('/user/charge', methods=['POST'])
@login_required
def charge():
    amount = 500
    customer = stripe.Customer.create(email=current_user.email, source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Service Plan'
    )
    user = models.User.query.filter_by(email=current_user.email).first()
    user.paid = 1
    db.session.commit()
~~    return render_template('user/charge.html', amount=amount)

@app.route('/api/payFail', methods=['POST', 'GET'])
def payFail():
	content = request.json
	stripe_email = content['data']['object']['email']
	user = models.User.query.filter_by(email=stripe_email).first()
	if user is not None: 
		user.paid = 0
		db.session.commit()
	return "Response: User with associated email " + str(stripe_email) + " updated on our end (payment failure)."

@app.route('/api/paySuccess', methods=['POST', 'GET'])
def paySuccess():
	content = request.json
	stripe_email = content['data']['object']['email']
	user = models.User.query.filter_by(email=stripe_email).first()
	if user is not None: 
		user.paid = 1
		db.session.commit()
	return "Response: User with associated email " + str(stripe_email) + " updated on our end (paid)."




## ... source file continues with no further render_template examples...

```


## Example 12 from Flask-Security-Too
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
import warnings

import pkg_resources
~~from flask import _request_ctx_stack, current_app, render_template
from flask_login import AnonymousUserMixin, LoginManager
from flask_login import UserMixin as BaseUserMixin
from flask_login import current_user
from flask_principal import Identity, Principal, RoleNeed, UserNeed, identity_loaded
from itsdangerous import URLSafeTimedSerializer
from passlib.context import CryptContext
from werkzeug.datastructures import ImmutableList
from werkzeug.local import LocalProxy

from .babel import get_i18n_domain, have_babel
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
    ResetPasswordForm,
    SendConfirmationForm,


## ... source file abbreviated to get to render_template examples ...


                sms_service = cv("SMS_SERVICE", app=app)
                if sms_service == "Twilio":  # pragma: no cover
                    self._check_modules("twilio", "SMS")
                if state.phone_util_cls == PhoneUtil:
                    self._check_modules("phonenumbers", "SMS")

            secrets = cv("TOTP_SECRETS", app=app)
            issuer = cv("TOTP_ISSUER", app=app)
            if not secrets or not issuer:
                raise ValueError("Both TOTP_SECRETS and TOTP_ISSUER must be set")
            state.totp_factory(state.totp_cls(secrets, issuer))

        if cv("PASSWORD_COMPLEXITY_CHECKER", app=app) == "zxcvbn":
            self._check_modules("zxcvbn", "PASSWORD_COMPLEXITY_CHECKER")
        return state

    def _check_modules(self, module, config_name):  # pragma: no cover
        from importlib.util import find_spec

        module_exists = find_spec(module)
        if not module_exists:
            raise ValueError(f"{module} is required for {config_name}")

        return module_exists

~~    def render_template(self, *args, **kwargs):
~~        return render_template(*args, **kwargs)

    def render_json(self, cb):
        self._state._render_json = cb

    def want_json(self, fn):
        self._state._want_json = fn

    def unauthz_handler(self, cb):
        self._state._unauthz_handler = cb

    def unauthn_handler(self, cb):
        self._state._unauthn_handler = cb

    def reauthn_handler(self, cb):
        self._state._reauthn_handler = cb

    def password_validator(self, cb):
        self._state._password_validator = cb

    def __getattr__(self, name):
        return getattr(self._state, name, None)



## ... source file continues with no further render_template examples...

```


## Example 13 from Flask-SocketIO
[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
([PyPI package information](https://pypi.org/project/Flask-SocketIO/),
[official tutorial](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
and
[project documentation](https://flask-socketio.readthedocs.io/en/latest/))
is a code library by [Miguel Grinberg](https://blog.miguelgrinberg.com/index)
that provides Socket.IO integration for [Flask](/flask.html) applications.
This extension makes it easier to add bi-directional communications on the
web via the [WebSockets](/websockets.html) protocol.

The Flask-SocketIO project is open source under the
[MIT license](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/LICENSE).

[**Flask-SocketIO / example / sessions.py**](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/./example/sessions.py)

```python
# sessions.py
~~from flask import Flask, render_template, session, request, jsonify
from flask_login import LoginManager, UserMixin, current_user, login_user, \
    logout_user
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
app.config['SESSION_TYPE'] = 'filesystem'
login = LoginManager(app)
Session(app)
socketio = SocketIO(app, manage_session=False)


class User(UserMixin, object):
    def __init__(self, id=None):
        self.id = id


@login.user_loader
def load_user(id):
    return User(id)


@app.route('/')
def index():
~~    return render_template('sessions.html')


@app.route('/session', methods=['GET', 'POST'])
def session_access():
    if request.method == 'GET':
        return jsonify({
            'session': session.get('value', ''),
            'user': current_user.id
                if current_user.is_authenticated else 'anonymous'
        })
    data = request.get_json()
    if 'session' in data:
        session['value'] = data['session']
    elif 'user' in data:
        if data['user']:
            login_user(User(data['user']))
        else:
            logout_user()
    return '', 204


@socketio.on('get-session')
def get_session():
    emit('refresh-session', {


## ... source file continues with no further render_template examples...

```


## Example 14 from Flask-User
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


## ... source file abbreviated to get to render_template examples ...


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

    def _render_and_send_email(self, email, user, template_filename, **kwargs):
        kwargs['app_name'] = self.user_manager.USER_APP_NAME
        kwargs['email'] = email
        kwargs['user'] = user
        kwargs['user_manager'] = self.user_manager

~~        subject = render_template(template_filename+'_subject.txt', **kwargs)
        subject = subject.replace('\n', ' ')
        subject = subject.replace('\r', ' ')
~~        html_message = render_template(template_filename+'_message.html', **kwargs)
~~        text_message = render_template(template_filename+'_message.txt', **kwargs)

        self.user_manager.email_adapter.send_email_message(
            email, subject, html_message, text_message,
            self.sender_email, self.sender_name)





## ... source file continues with no further render_template examples...

```


## Example 15 from Flasky
[Flasky](https://github.com/miguelgrinberg/flasky) is a wonderful
example application by
[Miguel Grinberg](https://github.com/miguelgrinberg) that he builds
while teaching developers how to use [Flask](/flask.html) in
[his books and videos](https://courses.miguelgrinberg.com/). Flasky
is [open sourced under the MIT license](https://github.com/miguelgrinberg/flasky/blob/master/LICENSE).

[**Flasky / app / email.py**](https://github.com/miguelgrinberg/flasky/blob/master/./app/email.py)

```python
# email.py
from threading import Thread
~~from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
~~    msg.body = render_template(template + '.txt', **kwargs)
~~    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr



## ... source file continues with no further render_template examples...

```


## Example 16 from Datadog Flask Example App
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




## ... source file abbreviated to get to render_template examples ...


                'Blueprint endpoint that uses <code>render_template_string()</code>',
            ],
            links=[
                dict(label='GET /bp/', url=url_for('bp.index')),
            ],
        ),
        dict(
            rule='GET /bp/unknown',
            description=[
                'Blueprint endpoint that calls <code>abort(404)</code>',
            ],
            links=[
                dict(label='GET /bp/unkown', url=url_for('bp.unknown')),
            ],
        ),
        dict(
            rule='GET /static/test.txt',
            description=[
                'Endpoint to fetch a simple .txt static file.',
            ],
            links=[
                dict(label='GET /static/test.txt', url=url_for('static', filename='test.txt')),
            ],
        ),
    ]
~~    return render_template('index.jinja2', routes=routes)


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


app.url_map.add(Rule('/custom-endpoint/', endpoint='custom-endpoint', defaults=dict(msg='Hello')))
app.url_map.add(Rule('/custom-endpoint/<msg>', endpoint='custom-endpoint'))

@app.endpoint('custom-endpoint')


## ... source file continues with no further render_template examples...

```


## Example 17 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / util / mathjax.py**](https://github.com/indico/indico/blob/master/indico/util/mathjax.py)

```python
# mathjax.py

from __future__ import absolute_import

~~from flask import current_app, render_template


class MathjaxMixin(object):
    def _get_head_content(self):
~~        return render_template('mathjax_config.html') + unicode(current_app.manifest['mathjax.js'])



## ... source file continues with no further render_template examples...

```


## Example 18 from keras-flask-deploy-webapp
The
[keras-flask-deploy-webapp](https://github.com/mtobeiyf/keras-flask-deploy-webapp)
project combines the [Flask](/flask.html) [web framework](/web-frameworks.html)
with the [Keras deep learning library](https://keras.io/) to provide
an example image classifier that is easy to [deploy](/deployment.html).
The application can be quckly run in a [Docker](/docker.html) container
on your local development environment. The project is licensed under the
[GNU General Public License v3.0](https://github.com/mtobeiyf/keras-flask-deploy-webapp/blob/master/LICENSE).

[**keras-flask-deploy-webapp / app.py**](https://github.com/mtobeiyf/keras-flask-deploy-webapp/blob/master/././app.py)

```python
# app.py
import os
import sys

~~from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np
from util import base64_to_pil


app = Flask(__name__)



from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
model = MobileNetV2(weights='imagenet')

print('Model loaded. Check http://127.0.0.1:5000/')


MODEL_PATH = 'models/your_model.h5'



def model_predict(img, model):
    img = img.resize((224, 224))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
~~    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        img = base64_to_pil(request.json)


        preds = model_predict(img, model)

        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        result = str(pred_class[0][0][1])               # Convert to string
        result = result.replace('_', ' ').capitalize()
        
        return jsonify(result=result, probability=pred_proba)

    return None


if __name__ == '__main__':

    http_server = WSGIServer(('0.0.0.0', 5000), app)


## ... source file continues with no further render_template examples...

```


## Example 19 from newspie
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


## ... source file abbreviated to get to render_template examples ...




@APP.route('/category/<string:category>', methods=['GET', 'POST'])
def category(category):
    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('category', category=category, page=1))
    if request.method == 'POST' and category in CATEGORIES:
        return do_post(page, category)
    if category in CATEGORIES:
        params = {'page': page, 'category': category, 'pageSize': PAGE_SIZE}
        country = get_cookie('country')
        if country is not None:
            params.update({'country': country})
        response = requests.get(TOP_HEADLINES,
                                params=params,
                                headers={'Authorization': API_KEY})
        if response.status_code == 200:
            pages = count_pages(response.json())
            if page > pages:
                page = pages
                return redirect(url_for('category', category=category, page=page))
            articles = parse_articles(response.json())
            return render(articles, page, pages, country, category)
        elif response.status_code == 401:
~~            return render_template(CONFIG['VARIOUS']['401_TEMPLATE'])
    return redirect(url_for('category', category='general', page=page))


@APP.route('/search/<string:query>', methods=['GET', 'POST'])
def search(query):
    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('search', query=query, page=1))
    params = {
        'qInTitle': query,
        'sortBy': 'relevancy',
        'page': page,
        'pageSize': PAGE_SIZE
    }
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


## ... source file abbreviated to get to render_template examples ...


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
                'source':
                    article['source']['name']
            })
    return parsed_articles


def count_pages(response):
    pages = 0
    if response.get('status') == 'ok':
        pages = (-(-response.get('totalResults', 0) // PAGE_SIZE))
    return pages


def render(articles, page, pages, country, category):
    pages = pages if pages <= 12 else 12
~~    return render_template(CONFIG['VARIOUS']['TEMPLATE'],
                           articles=articles,
                           categories=CATEGORIES,
                           category=category,
                           countries=COUNTRIES,
                           country=country,
                           page=page,
                           pages=pages)


def get_cookie(key):
    cookie_value = request.cookies.get(key)
    return cookie_value


if __name__ == '__main__':
    APP.run()



## ... source file continues with no further render_template examples...

```


## Example 20 from Science Flask
[Science Flask](https://github.com/danielhomola/science_flask)
is a [Flask](/flask.html)-powered web application for online
scientific research tools. The project was built as a template
for any scientist or groups of scientists to use when working
together without having to really understand how the application
is built. The application includes an academic registration
process (only valid academic email addresses can be used), an
admin panel, logging, and analysis forms.

[@danielhomola](https://github.com/danielhomola) is the
primary creator of Science Flask and the project is open
source under the
[GNU General Public License](https://github.com/danielhomola/science_flask/blob/master/LICENSE).

[**Science Flask / frontend / views.py**](https://github.com/danielhomola/science_flask/blob/master/./frontend/views.py)

```python
# views.py
import datetime
import json
import os
import shutil
~~from flask import render_template, redirect, request, g, url_for, flash, abort,\
                  send_from_directory, session
from flask_login import login_required
from flask_security import current_user
from werkzeug.utils import secure_filename

from .analysis import run_analysis, terminate_analysis
from .view_functions import save_study, get_form, save_analysis, \
                           get_studies_array, get_analyses_array, \
                           get_user_folder, security_check
from backend.utils.check_uploaded_files import clear_up_study
from . import app, db, models
from .forms import UploadForm, AnalysisForm


@app.route('/')
def index():
~~    return render_template('index.html')

@app.route('/about')
def about():
~~    return render_template('about.html')

@app.route('/help')
def help():
~~    return render_template('help.html')

@app.route('/tc')
def tc():
~~    return render_template('tc.html')


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():

    if request.method == 'POST':
        form = UploadForm(data=get_form(request.values, request.files))
        try:
            check = request.form['check']
            if check == 'true':
                check = True
            else:
                check = False
        except:
            return json.dumps(dict(status='invalid'))

        if check:
            if form.validate_on_submit():
                return json.dumps(dict(status='OK'))
            else:
                return json.dumps(dict(status='errors', errors=form.errors))

        else:
            try:
                return save_study(form, request.files)
            except:
                user_folder = get_user_folder()
                study_folder = secure_filename(form.study_name.data)
                user_data_folder = os.path.join(user_folder, study_folder)
                clear_up_study(user_data_folder)
                return json.dumps(dict(status='invalid'))

    else:
        form = UploadForm()
        too_many_studies = 0
        if len(current_user.studies.all()) >= app.config['ACTIVE_STUDY_PER_USER']:
            too_many_studies = 1
        if current_user.num_studies >= app.config['STUDY_PER_USER']:
            too_many_studies = 2
~~        return render_template('upload.html', form=form,
                               too_many_studies=too_many_studies)


@app.route('/too_large_file')
@login_required
def too_large_file():
~~    return render_template('utils/max_file_size.html')


@app.route('/something_wrong/<page>')
@login_required
def something_wrong(page):
~~    return render_template('utils/something_wrong.html', page=page)


@app.route('/analysis/<int:user_id>_<int:study_id>', methods=['GET', 'POST'])
@login_required
def analysis(user_id, study_id):
    if not security_check(user_id, study_id):
        abort(403)

    if len(current_user.analyses.filter_by(status=1).all()) > 0:
~~        return render_template('utils/analysis_in_progress.html')

    if request.method == 'POST':
        form = AnalysisForm(data=get_form(request.values, request.files))
        try:
            check = request.form['check']
            if check == 'true':
                check = True
            else:
                check = False
        except:
            return json.dumps(dict(status='invalid'))

        if check:
            session['study_id'] = study_id
            if form.validate_on_submit():
                return json.dumps(dict(status='OK'))
            else:
                return json.dumps(dict(status='errors', errors=form.errors))

        else:
            try:
                save_analysis(form, study_id)
                task = run_analysis.apply_async(args=[current_user.id], countdown=1)
                session['task_id'] = task.id
                return json.dumps(dict(status='OK'))
            except:
                return json.dumps(dict(status='invalid'))

    else:
        form = AnalysisForm()
        too_many_analyses = 0
        if len(current_user.analyses.all()) >= app.config['ACTIVE_ANALYSIS_PER_USER']:
            too_many_analyses = 1
        if current_user.num_analyses >= app.config['ANALYSIS_PER_USER']:
            too_many_analyses = 2

        study = models.Studies.query.get(study_id)
        study_name = study.study_name
~~        return render_template('analysis.html', form=form, user_id=user_id,
                               study_id=study_id, study_name=study_name,
                               too_many_analyses=too_many_analyses)


@app.route('/profile')
@login_required
def profile():
    studies_array = get_studies_array()
    analyses_array = get_analyses_array()
    user_id = current_user.id
    if len(studies_array) > 0:
        study_id = studies_array[0]['id']
    else:
        study_id = 0

    if current_user.profile_intro == 0:
        profile_intro = True
        current_user.profile_intro = 1
        db.session.add(current_user)
        db.session.commit()
    else:
        profile_intro = False

    stats = {
        'active_studies': len(current_user.studies.all()),
        'all_studies': current_user.num_studies,
        'active_analyses': len(current_user.analyses.all()),
        'all_analyses': current_user.num_analyses
    }
~~    return render_template('profile.html', studies=studies_array, stats=stats,
                           analyses=analyses_array, profile_intro=profile_intro,
                           user_id=user_id, study_id=study_id)


@app.route('/delete_study/<int:user_id>_<int:study_id>/', methods=['POST'])
@login_required
def delete_study(user_id, study_id):
    if not security_check(user_id, study_id):
        abort(403)

    study = models.Studies.query.get(study_id)
    study_name = study.study_name
    for analysis in study.analyses.all():
        db.session.delete(analysis)
    db.session.delete(study)
    db.session.commit()

    user_folder = get_user_folder()
    study_folder = secure_filename(study_name)
    folder_to_delete = os.path.join(user_folder, study_folder)
    if os.path.exists(folder_to_delete):
        shutil.rmtree(folder_to_delete)
    return redirect(url_for('profile'))



## ... source file abbreviated to get to render_template examples ...




@app.route('/vis/<int:user_id>_<int:analysis_id>_<path:data_file>')
@login_required
def vis(user_id, analysis_id, data_file):
    if not security_check(user_id, analysis_id, True):
        abort(403)

    if data_file not in ['dataset1_2', 'dataset1', 'dataset2']:
        abort(403)

    analysis = models.Analyses.query.get(analysis_id)
    analysis_name = analysis.analysis_name
    study = models.Studies.query.get(analysis.study_id)
    study_name = study.study_name
    username = app.config['USER_PREFIX'] + str(current_user.id)
    analysis_folder = os.path.join(username, secure_filename(study_name),
                                   secure_filename(analysis_name))
    autocorr = bool(study.autocorr)
    dataset_names = [study.dataset1_type]
    if autocorr:
        dataset_names += study.dataset1_type
    else:
        dataset_names += [study.dataset2_type]

~~    return render_template('vis.html', analysis_folder=analysis_folder,
                           analysis_name=analysis_name, autocorr=autocorr,
                           user_id=user_id, analysis_id=analysis_id,
                           data_file=data_file,
                           dataset_names=dataset_names)


@app.errorhandler(403)
def forbidden_error(error):
    app.logger.error('403 - Forbidden request: %s', request.path)
~~    return render_template('utils/403.html'), 403


@app.errorhandler(404)
def not_found_error(error):
    if "/get_file/" not in request.path:
        app.logger.error('404 - Page not found: %s', request.path)
~~    return render_template('utils/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    app.logger.error('500 - Internal server error: %s', request.path)
~~    return render_template('utils/500.html'), 500


@app.errorhandler(500)
def all_exception_error(exception):
    db.session.rollback()
    app.logger.error('All other exception error: %s', request.path)
~~    return render_template('utils/500.html'), 500



@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])



## ... source file continues with no further render_template examples...

```


## Example 21 from tedivms-flask
[tedivm's flask starter app](https://github.com/tedivm/tedivms-flask) is a
base of [Flask](/flask.html) code and related projects such as
[Celery](/celery.html) which provides a template to start your own
Flask web app. The project comes baked with an admin panel,
[API authentication and authorization](/application-programming-interfaces.html),
[SQLAlchemy](/sqlalchemy.html) and many other common libraries that are
often used with Flask.

The project's code is provided as open source under the
[BSD 2-Clause "Simplified" license](https://github.com/tedivm/tedivms-flask/blob/master/LICENSE.txt).

[**tedivms-flask / app / __init__.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/./__init__.py)

```python
# __init__.py
import boto3
from celery import Celery
from datetime import datetime
import os
import requests
import yaml

~~from flask import Flask, session, render_template
from flask_mail import Mail
from flask_migrate import Migrate, MigrateCommand
from flask.sessions import SessionInterface
from flask_sqlalchemy import SQLAlchemy
from flask_user import user_logged_out
from flask_wtf.csrf import CSRFProtect

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from beaker.middleware import SessionMiddleware

db = SQLAlchemy()
csrf_protect = CSRFProtect()
mail = Mail()
migrate = Migrate()


def get_config():
    app = Flask(__name__)

    app.config.from_object('app.settings')
    if 'APPLICATION_SETTINGS' in os.environ:
        app.config.from_envvar(os.environ['APPLICATION_SETTINGS'])
    if 'AWS_SECRETS_MANAGER_CONFIG' in os.environ:


## ... source file abbreviated to get to render_template examples ...


    session_opts['session.secret'] = app.secret_key

    class BeakerSessionInterface(SessionInterface):
        def open_session(self, app, request):
            session = request.environ['beaker.session']
            return session

        def save_session(self, app, session, response):
            session.save()

    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.session_interface = BeakerSessionInterface()

    @user_logged_out.connect_via(app)
    def clear_session(sender, user, **extra):
        session.clear()


def init_celery_service(app):
    celery.conf.update(app.config)


def init_error_handlers(app):

    def show_error(status, message='An unknown error has occured.'):
~~        return render_template('pages/errors.html', error_code=status, message=message), status

    @app.errorhandler(401)
    def error_unauthorized(e):
        return show_error(401, 'Unauthorized')

    @app.errorhandler(403)
    def error_forbidden(e):
        return show_error(403, 'Forbidden')

    @app.errorhandler(404)
    def error_pagenotfound(e):
        return show_error(404, 'Page not found.')

    @app.errorhandler(500)
    def error_servererror(e):
        return show_error(500, 'An unknown error has occurred on the server.')



## ... source file continues with no further render_template examples...

```


## Example 22 from trape
[trape](https://github.com/jofpin/trape) is a research tool for tracking
people's activities that are logged digitally. The tool uses
[Flask](/flask.html) to create a web front end to view aggregated data
on an individual the application is set to track. The source code is
provided as open source under the MIT license, according to the
[README](https://github.com/jofpin/trape/blob/master/README.md).

[**trape / core / stats.py**](https://github.com/jofpin/trape/blob/master/./core/stats.py)

```python
# stats.py
from core.dependence import urllib2
import sys
import os
~~from flask import Flask, render_template, session, request, json, redirect, url_for, send_from_directory
from flask_cors import CORS
from trape import Trape
from core.db import Database

trape = Trape(1)

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

cors = CORS(app)

db = Database()

trape.header()


@app.route("/" + trape.stats_path)
def index():
    return trape.injectCSS_Paths(render_template("/login.html").replace('[LOGIN_SRC]', trape.JSFiles[2]['src']).replace('[LIBS_SRC]', trape.JSFiles[1]['src']))



## ... source file abbreviated to get to render_template examples ...


    server_code = ''
    if trape.nGrokUrl != '':
        server_code = str(trape.nGrokUrl) 
    else:
        server_code = str(trape.localIp) + ':' + str(trape.app_port) 

    codeToInject = codeToInject.replace('[HOST_ADDRESS]', server_code)
    codeToInject = codeToInject.replace('[YOUR_GMAPS_API_KEY]', trape.gmaps)
    return codeToInject

@app.route("/static/js/<JSFile>")
def busted(JSFile):
    code = ''
    mPath = ''
    if getattr(sys, 'frozen', False):
        mPath = sys._MEIPASS + '/'
    for obj in trape.JSFiles:
        if str(obj['src']) == str(JSFile):
            s_code = open(mPath + "static/js/" + obj['path'],"r") 
            code = s_code.read()
            s_code.close()
            break
    if code != '':
        return code
    else:
~~        return render_template('404.html') 

@app.route("/styles/<CSSFile>")
def style_redirect(CSSFile):
    code = ''
    for obj in trape.CSSFiles:
        if str(obj['src']) == str(CSSFile):
            code = obj['path']
            break
    return redirect(code)

@app.route("/static/files/<File>")
def file_redirect(File):
    uploads = os.path.join(os.getcwd(), './')
    return send_from_directory(directory=uploads, filename=File)



## ... source file continues with no further render_template examples...

```

