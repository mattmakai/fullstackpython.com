title: flask.views MethodView Example Code
category: page
slug: flask-views-methodview-examples
sortorder: 500021033
toc: False
sidebartitle: flask.views MethodView
meta: Example code for understanding how to use the MethodView class from the flask.views module of the Flask project.


[MethodView](https://github.com/pallets/flask/blob/master/src/flask/views.py)
is a class within the `flask.views` module of the [Flask](/flask.html)
project. `MethodView` is a
[Python Metaclass](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
that determines the methods, such as GET, POST, PUT, etc, that
a view defines.

<a href="/flask-views-view-examples.html">View</a>
and
<a href="/flask-views-http-method-funcs-examples.html">http_method_funcs</a>
are a couple of other callables within the `flask.views` package that also have code examples.

These subjects go along with the `MethodView` code examples:

* [web development](/web-development.html) and [web design](/web-design.html)
* [web framework concepts](/web-frameworks.html) and the [Flask framework](/flask.html)


## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / auth / views.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/auth/views.py)

```python
# views.py
import logging
from datetime import datetime

from flask import Blueprint, current_app, flash, g, redirect, request, url_for
~~from flask.views import MethodView
from flask_babelplus import gettext as _
from flask_login import (
    confirm_login,
    current_user,
    login_fresh,
    login_required,
    login_user,
    logout_user,
)

from flaskbb.auth.forms import (
    AccountActivationForm,
    ForgotPasswordForm,
    LoginForm,
    LoginRecaptchaForm,
    ReauthForm,
    RegisterForm,
    RequestActivationForm,
    ResetPasswordForm,
)
from flaskbb.extensions import db, limiter
from flaskbb.utils.helpers import (
    anonymous_required,
    enforce_recaptcha,


## ... source file abbreviated to get to MethodView examples ...


    get_available_languages,
    redirect_or_next,
    register_view,
    registration_enabled,
    render_template,
    requires_unactivated,
)
from flaskbb.utils.settings import flaskbb_config

from ..core.auth.authentication import StopAuthentication
from ..core.auth.registration import UserRegistrationInfo
from ..core.exceptions import PersistenceError, StopValidation, ValidationError
from ..core.tokens import TokenError
from .plugins import impl
from .services import (
    account_activator_factory,
    authentication_manager_factory,
    reauthentication_manager_factory,
    registration_service_factory,
    reset_service_factory,
)

logger = logging.getLogger(__name__)


~~class Logout(MethodView):
    decorators = [limiter.exempt, login_required]

    def get(self):
        logout_user()
        flash(_("Logged out"), "success")
        return redirect(url_for("forum.index"))


~~class Login(MethodView):
    decorators = [anonymous_required]

    def __init__(self, authentication_manager_factory):
        self.authentication_manager_factory = authentication_manager_factory

    def form(self):
        if enforce_recaptcha(limiter):
            return LoginRecaptchaForm()
        return LoginForm()

    def get(self):
        return render_template("auth/login.html", form=self.form())

    def post(self):
        form = self.form()
        if form.validate_on_submit():
            auth_manager = self.authentication_manager_factory()
            try:
                user = auth_manager.authenticate(
                    identifier=form.login.data, secret=form.password.data
                )
                login_user(user, remember=form.remember_me.data)
                return redirect_or_next(url_for("forum.index"))
            except StopAuthentication as e:
                flash(e.reason, "danger")
            except Exception:
                flash(_("Unrecoverable error while handling login"))

        return render_template("auth/login.html", form=form)


~~class Reauth(MethodView):
    decorators = [login_required, limiter.exempt]
    form = ReauthForm

    def __init__(self, reauthentication_factory):
        self.reauthentication_factory = reauthentication_factory

    def get(self):
        if not login_fresh():
            return render_template("auth/reauth.html", form=self.form())
        return redirect_or_next(current_user.url)

    def post(self):
        form = self.form()
        if form.validate_on_submit():

            reauth_manager = self.reauthentication_factory()
            try:
                reauth_manager.reauthenticate(
                    user=current_user, secret=form.password.data
                )
                confirm_login()
                flash(_("Reauthenticated."), "success")
                return redirect_or_next(current_user.url)
            except StopAuthentication as e:
                flash(e.reason, "danger")
            except Exception:
                flash(_("Unrecoverable error while handling reauthentication"))
                raise

        return render_template("auth/reauth.html", form=form)


~~class Register(MethodView):
    decorators = [anonymous_required, registration_enabled]

    def __init__(self, registration_service_factory):
        self.registration_service_factory = registration_service_factory

    def form(self):
        current_app.pluggy.hook.flaskbb_form_registration(form=RegisterForm)
        form = RegisterForm()

        form.language.choices = get_available_languages()
        form.language.default = flaskbb_config['DEFAULT_LANGUAGE']
        form.process(request.form)  # needed because a default is overriden
        return form

    def get(self):
        return render_template("auth/register.html", form=self.form())

    def post(self):
        form = self.form()
        if form.validate_on_submit():
            registration_info = UserRegistrationInfo(
                username=form.username.data,
                password=form.password.data,
                group=4,


## ... source file abbreviated to get to MethodView examples ...


            service = self.registration_service_factory()
            try:
                service.register(registration_info)
            except StopValidation as e:
                form.populate_errors(e.reasons)
                return render_template("auth/register.html", form=form)
            except PersistenceError:
                    logger.exception("Database error while persisting user")
                    flash(
                        _(
                            "Could not process registration due"
                            "to an unrecoverable error"
                        ), "danger"
                    )

                    return render_template("auth/register.html", form=form)

            current_app.pluggy.hook.flaskbb_event_user_registered(
                username=registration_info.username
            )
            return redirect_or_next(url_for('forum.index'))

        return render_template("auth/register.html", form=form)


~~class ForgotPassword(MethodView):
    decorators = [anonymous_required]
    form = ForgotPasswordForm

    def __init__(self, password_reset_service_factory):
        self.password_reset_service_factory = password_reset_service_factory

    def get(self):
        return render_template("auth/forgot_password.html", form=self.form())

    def post(self):
        form = self.form()
        if form.validate_on_submit():

            try:
                service = self.password_reset_service_factory()
                service.initiate_password_reset(form.email.data)
            except ValidationError:
                flash(
                    _(
                        "You have entered an username or email address that "
                        "is not linked with your account."
                    ), "danger"
                )
            else:
                flash(_("Email sent! Please check your inbox."), "info")
                return redirect(url_for("auth.forgot_password"))

        return render_template("auth/forgot_password.html", form=form)


~~class ResetPassword(MethodView):
    decorators = [anonymous_required]
    form = ResetPasswordForm

    def __init__(self, password_reset_service_factory):
        self.password_reset_service_factory = password_reset_service_factory

    def get(self, token):
        form = self.form()
        form.token.data = token
        return render_template("auth/reset_password.html", form=form)

    def post(self, token):
        form = self.form()
        if form.validate_on_submit():
            try:
                service = self.password_reset_service_factory()
                service.reset_password(
                    token, form.email.data, form.password.data
                )
            except TokenError as e:
                flash(e.reason, 'danger')
                return redirect(url_for('auth.forgot_password'))
            except StopValidation as e:
                form.populate_errors(e.reasons)
                form.token.data = token
                return render_template("auth/reset_password.html", form=form)
            except Exception:
                logger.exception("Error when resetting password")
                flash(_('Error when resetting password'))
                return redirect(url_for('auth.forgot_password'))
            finally:
                try:
                    db.session.commit()
                except Exception:
                    logger.exception(
                        "Error while finalizing database when resetting password"  # noqa
                    )
                    db.session.rollback()

            flash(_("Your password has been updated."), "success")
            return redirect(url_for("auth.login"))

        form.token.data = token
        return render_template("auth/reset_password.html", form=form)


~~class RequestActivationToken(MethodView):
    decorators = [requires_unactivated]
    form = RequestActivationForm

    def __init__(self, account_activator_factory):
        self.account_activator_factory = account_activator_factory

    def get(self):
        return render_template(
            "auth/request_account_activation.html", form=self.form()
        )

    def post(self):
        form = self.form()
        if form.validate_on_submit():
            activator = self.account_activator_factory()
            try:
                activator.initiate_account_activation(form.email.data)
            except ValidationError as e:
                form.populate_errors([(e.attribute, e.reason)])
            else:
                flash(
                    _(
                        "A new account activation token has been sent to "
                        "your email address."
                    ), "success"
                )
                return redirect(url_for('forum.index'))

        return render_template(
            "auth/request_account_activation.html", form=form
        )


~~class AutoActivateAccount(MethodView):
    decorators = [requires_unactivated]

    def __init__(self, account_activator_factory):
        self.account_activator_factory = account_activator_factory

    def get(self, token):
        activator = self.account_activator_factory()

        try:
            activator.activate_account(token)
        except TokenError as e:
            flash(e.reason, 'danger')
        except ValidationError as e:
            flash(e.reason, 'danger')
            return redirect(url_for('forum.index'))

        else:
            try:
                db.session.commit()
            except Exception:  # noqa
                logger.exception("Database error while activating account")
                db.session.rollback()
                flash(
                    _(
                        "Could not activate account due to an unrecoverable error"  # noqa
                    ), "danger"
                )

                return redirect(url_for('auth.request_activation_token'))

            flash(
                _("Your account has been activated and you can now login."),
                "success"
            )
            return redirect(url_for("forum.index"))

        return redirect(url_for('auth.activate_account'))


~~class ActivateAccount(MethodView):
    decorators = [requires_unactivated]
    form = AccountActivationForm

    def __init__(self, account_activator_factory):
        self.account_activator_factory = account_activator_factory

    def get(self):
        return render_template(
            "auth/account_activation.html",
            form=self.form()
        )

    def post(self):
        form = self.form()
        if form.validate_on_submit():
            token = form.token.data
            activator = self.account_activator_factory()
            try:
                activator.activate_account(token)
            except TokenError as e:
                form.populate_errors([('token', e.reason)])
            except ValidationError as e:
                flash(e.reason, 'danger')
                return redirect(url_for('forum.index'))


## ... source file continues with no further MethodView examples...

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

[**flask-restx / flask_restx / resource.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./resource.py)

```python
# resource.py
from __future__ import unicode_literals

from flask import request
~~from flask.views import MethodView
from werkzeug.wrappers import BaseResponse

from .model import ModelBase

from .utils import unpack


~~class Resource(MethodView):

    representations = None
    method_decorators = []

    def __init__(self, api=None, *args, **kwargs):
        self.api = api

    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)
        if meth is None and request.method == "HEAD":
            meth = getattr(self, "get", None)
        assert meth is not None, "Unimplemented method %r" % request.method

        for decorator in self.method_decorators:
            meth = decorator(meth)

        self.validate_payload(meth)

        resp = meth(*args, **kwargs)

        if isinstance(resp, BaseResponse):
            return resp

        representations = self.representations or {}


## ... source file continues with no further MethodView examples...

```


## Example 3 from sandman2
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

from flask import request, make_response
import flask
~~from flask.views import MethodView
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


def is_valid_method(model, resource=None):
    validation_function_name = 'is_valid_{}'.format(
        request.method.lower())
    if hasattr(model, validation_function_name):
        return getattr(model, validation_function_name)(request, resource)

~~class Service(MethodView):


    __model__ = None

    __json_collection_name__ = 'resources'

    def delete(self, resource_id):
        resource = self._resource(resource_id)
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().delete(resource)
        db.session().commit()
        return self._no_content_response()

    @etag
    def get(self, resource_id=None):
        if request.path.endswith('meta'):
            return self._meta()

        if resource_id is None:
            error_message = is_valid_method(self.__model__)
            if error_message:
                raise BadRequestException(error_message)


## ... source file continues with no further MethodView examples...

```

