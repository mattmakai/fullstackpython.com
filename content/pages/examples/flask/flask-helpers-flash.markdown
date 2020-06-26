title: flask.helpers flash code examples
category: page
slug: flask-helpers-flash-examples
sortorder: 500021013
toc: False
sidebartitle: flask.helpers flash
meta: Python example code for the flash function from the flask.helpers module of the Flask project.


flash is a function within the flask.helpers module of the Flask project.


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

    route_base = "/register"


## ... source file abbreviated to get to flash examples ...


            ".activation",
            _external=True,
            activation_hash=register_user.registration_hash,
        )
        msg.html = self.render_template(
            self.email_template,
            url=url,
            username=register_user.username,
            first_name=register_user.first_name,
            last_name=register_user.last_name,
        )
        msg.recipients = [register_user.email]
        try:
            mail.send(msg)
        except Exception as e:
            log.error("Send email exception: {0}".format(str(e)))
            return False
        return True

    def add_registration(self, username, first_name, last_name, email, password=""):
        register_user = self.appbuilder.sm.add_register_user(
            username, first_name, last_name, email, password
        )
        if register_user:
            if self.send_email(register_user):
~~                flash(as_unicode(self.message), "info")
                return register_user
            else:
~~                flash(as_unicode(self.error_message), "danger")
                self.appbuilder.sm.del_register_user(register_user)
                return None

    @expose("/activation/<string:activation_hash>")
    def activation(self, activation_hash):
        reg = self.appbuilder.sm.find_register_user(activation_hash)
        if not reg:
            log.error(c.LOGMSG_ERR_SEC_NO_REGISTER_HASH.format(activation_hash))
~~            flash(as_unicode(self.false_error_message), "danger")
            return redirect(self.appbuilder.get_url_for_index)
        if not self.appbuilder.sm.add_user(
            username=reg.username,
            email=reg.email,
            first_name=reg.first_name,
            last_name=reg.last_name,
            role=self.appbuilder.sm.find_role(
                self.appbuilder.sm.auth_user_registration_role
            ),
            hashed_password=reg.password,
        ):
~~            flash(as_unicode(self.error_message), "danger")
            return redirect(self.appbuilder.get_url_for_index)
        else:
            self.appbuilder.sm.del_register_user(reg)
            return self.render_template(
                self.activation_template,
                username=reg.username,
                first_name=reg.first_name,
                last_name=reg.last_name,
                appbuilder=self.appbuilder,
            )

    def add_form_unique_validations(self, form):
        datamodel_user = self.appbuilder.sm.get_user_datamodel
        datamodel_register_user = self.appbuilder.sm.get_register_user_datamodel
        if len(form.username.validators) == 1:
            form.username.validators.append(Unique(datamodel_user, "username"))
            form.username.validators.append(Unique(datamodel_register_user, "username"))
        if len(form.email.validators) == 2:
            form.email.validators.append(Unique(datamodel_user, "email"))
            form.email.validators.append(Unique(datamodel_register_user, "email"))


class RegisterUserDBView(BaseRegisterUser):



## ... source file abbreviated to get to flash examples ...


        form = LoginForm_oid()
        if form.validate_on_submit():
            session["remember_me"] = form.remember_me.data
            return self.appbuilder.sm.oid.try_login(
                form.openid.data, ask_for=["email", "fullname"]
            )
        resp = session.pop("oid_resp", None)
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
            return self.render_template(
                self.form_template,
                title=self.form_title,
                widgets=widgets,
                form_action="form",
                appbuilder=self.appbuilder,
            )
        else:
~~            flash(as_unicode(self.error_message), "warning")
            return redirect(self.get_redirect())

    def oid_login_handler(self, f, oid):
        if request.args.get("openid_complete") != u"yes":
            return f(False)
        consumer = Consumer(SessionWrapper(self), oid.store_factory())
        openid_response = consumer.complete(
            request.args.to_dict(), oid.get_current_url()
        )
        if openid_response.status == SUCCESS:
            return self.after_login(OpenIDResponse(openid_response, []))
        elif openid_response.status == CANCEL:
            oid.signal_error(u"The request was cancelled")
            return redirect(oid.get_current_url())
        oid.signal_error(u"OpenID authentication error")
        return redirect(oid.get_current_url())

    def after_login(self, resp):
        session["oid_resp"] = resp

    def form_get(self, form):
        self.add_form_unique_validations(form)

    def form_post(self, form):


## ... source file continues with no further flash examples...

```


## Example 2 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / auth / plugins.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/auth/plugins.py)

```python
# plugins.py
~~from flask import flash, redirect, url_for
from flask_login import current_user, logout_user

from . import impl
from ..core.auth.authentication import ForceLogout
from ..extensions import db
from ..user.models import User
from ..utils.settings import flaskbb_config
from .services.authentication import (
    BlockUnactivatedUser,
    ClearFailedLogins,
    DefaultFlaskBBAuthProvider,
    MarkFailedLogin,
)
from .services.factories import account_activator_factory
from .services.reauthentication import (
    ClearFailedLoginsOnReauth,
    DefaultFlaskBBReauthProvider,
    MarkFailedReauth,
)
from .services.registration import (
    AutoActivateUserPostProcessor,
    AutologinPostProcessor,
    EmailUniquenessValidator,
    SendActivationPostProcessor,


## ... source file abbreviated to get to flash examples ...




@impl(trylast=True)
def flaskbb_reauth_attempt(user, secret):
    return DefaultFlaskBBReauthProvider().reauthenticate(user, secret)


@impl
def flaskbb_reauth_failed(user):
    MarkFailedReauth().handle_reauth_failure(user)


@impl
def flaskbb_post_reauth(user):
    ClearFailedLoginsOnReauth().handle_post_reauth(user)


@impl
def flaskbb_errorhandlers(app):

    @app.errorhandler(ForceLogout)
    def handle_force_logout(error):
        if current_user:
            logout_user()
            if error.reason:
~~                flash(error.reason, "danger")
        return redirect(url_for("forum.index"))


@impl
def flaskbb_gather_registration_validators():
    blacklist = [
        w.strip() for w in flaskbb_config["AUTH_USERNAME_BLACKLIST"].split(",")
    ]

    requirements = UsernameRequirements(
        min=flaskbb_config["AUTH_USERNAME_MIN_LENGTH"],
        max=flaskbb_config["AUTH_USERNAME_MAX_LENGTH"],
        blacklist=blacklist,
    )

    return [
        EmailUniquenessValidator(User),
        UsernameUniquenessValidator(User),
        UsernameValidator(requirements),
    ]


@impl
def flaskbb_registration_post_processor(user):


## ... source file continues with no further flash examples...

```


## Example 3 from flask-bookshelf
[flask-bookshelf](https://github.com/damyanbogoev/flask-bookshelf) is the
example [Flask](/flask.html) application that developers create when
going through
[this Flask series of blog posts](https://damyanon.net/tags/flask-series/).

[**flask-bookshelf / bookshelf / admin / controllers.py**](https://github.com/damyanbogoev/flask-bookshelf/blob/master/bookshelf/admin/controllers.py)

```python
# controllers.py
from sqlalchemy import exc
~~from flask import Blueprint, render_template, flash
from flask import current_app, redirect, request, url_for
from flask_security.decorators import roles_required
from bookshelf.admin.forms.author_forms import CreateAuthorForm
from bookshelf.cache import cache
from bookshelf.data.models import Author, db


admin = Blueprint("admin", __name__, template_folder="templates")


@admin.route("/")
@roles_required("admin")
def index():
    return render_template("admin_index.htm")


@admin.route("/author/create", methods=["GET", "POST"])
@roles_required("admin")
def create_author():
    form = CreateAuthorForm(request.form)
    if request.method == "POST" and form.validate():
        names = form.names.data
        current_app.logger.info("Adding a new author %s.", (names))
        author = Author(names)

        try:
            db.session.add(author)
            db.session.commit()
            cache.clear()
~~            flash("Author successfully created.")
        except exc.SQLAlchemyError as e:
~~            flash("Author was not created.")
            current_app.logger.error(e)

            return redirect(url_for("admin.create_author"))

        return redirect(url_for("main.display_authors"))

    return render_template("create_author.htm", form=form)



## ... source file continues with no further flash examples...

```


## Example 4 from flask_jsondash
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


## ... source file abbreviated to get to flash examples ...


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
    return render_template('pages/charts_index.html', **kwargs)


@charts.route('/charts/<c_id>', methods=['GET'])
def view(c_id):
    if not auth(authtype='view', view_id=c_id):
~~        flash('You do not have access to view this dashboard.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    viewjson = adapter.read(c_id=c_id)
    if not viewjson:
~~        flash('Could not find view: {}'.format(c_id), 'error')
        return redirect(url_for('jsondash.dashboard'))
    if '_id' in viewjson:
        viewjson.pop('_id')
    if 'modules' not in viewjson:
~~        flash('Invalid configuration - missing modules.', 'error')
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
    return render_template('pages/chart_detail.html', **kwargs)


@charts.route('/charts/<c_id>/delete', methods=['POST'])
def delete(c_id):
    dash_url = url_for('jsondash.dashboard')
    if not auth(authtype='delete'):
~~        flash('You do not have access to delete dashboards.', 'error')
        return redirect(dash_url)
    adapter.delete(c_id)
~~    flash('Deleted dashboard "{}"'.format(c_id))
    return redirect(dash_url)


@charts.route('/charts/<c_id>/update', methods=['POST'])
def update(c_id):
    if not auth(authtype='update'):
~~        flash('You do not have access to update dashboards.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    viewjson = adapter.read(c_id=c_id)
    if not viewjson:
~~        flash('Could not find view: {}'.format(c_id), 'error')
        return redirect(url_for('jsondash.dashboard'))
    form_data = request.form
    view_url = url_for('jsondash.view', c_id=c_id)
    edit_raw = 'edit-raw' in request.form
    now = str(dt.now())
    if edit_raw:
        try:
            conf = form_data.get('config')
            data = validate_raw_json(conf, date=now, id=c_id)
            data = db.reformat_data(data, c_id)
        except InvalidSchemaError as e:
~~            flash(str(e), 'error')
            return redirect(view_url)
        except (TypeError, ValueError) as e:
~~            flash('Invalid JSON config. "{}"'.format(e), 'error')
            return redirect(view_url)
    else:
        modules = db.format_charts(form_data)
        layout = form_data['mode']
        if layout == 'grid' and modules and modules[0].get('row') is None:
~~            flash('Cannot use grid layout without '
                  'specifying row(s)! Edit JSON manually '
                  'to override this.', 'error')
            return redirect(view_url)
        category = form_data.get('category', '')
        category_override = form_data.get('category_new', '')
        category = category_override if category_override != '' else category
        data = dict(
            category=category if category != '' else 'uncategorized',
            name=form_data['name'],
            layout=layout,
            modules=modules,
            id=c_id,
            date=now,
        )
    data.update(**metadata(exclude=['created_by']))
    data.update(**check_global())
    if edit_raw:
        adapter.update(c_id, data=data, fmt_charts=False)
    else:
        adapter.update(c_id, data=data)
~~    flash('Updated view "{}"'.format(c_id))
    return redirect(view_url)


def check_global():
    global_enabled = setting('JSONDASH_GLOBALDASH')
    global_flag = request.form.get('is_global') is not None
    can_make_global = auth(authtype='edit_global')
    if all([global_flag, global_enabled, can_make_global]):
        return dict(created_by=setting('JSONDASH_GLOBAL_USER'))
    return dict()


@charts.route('/charts/create', methods=['POST'])
def create():
    if not auth(authtype='create'):
~~        flash('You do not have access to create dashboards.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    data = request.form
    new_id = str(uuid.uuid1())
    d = dict(
        name=data['name'],
        modules=db.format_charts(data),
        date=str(dt.now()),
        id=new_id,
        layout=data.get('mode', 'grid'),
    )
    d.update(**metadata())
    d.update(**check_global())
    adapter.create(data=d)
~~    flash('Created new dashboard "{}"'.format(data['name']))
    return redirect(url_for('jsondash.view', c_id=new_id))


@charts.route('/charts/<c_id>/clone', methods=['POST'])
def clone(c_id):
    if not auth(authtype='clone'):
~~        flash('You do not have access to clone dashboards.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    viewjson = adapter.read(c_id=c_id)
    if not viewjson:
~~        flash('Could not find view: {}'.format(c_id), 'error')
        return redirect(url_for('jsondash.dashboard'))
    newname = 'Clone of {}'.format(viewjson['name'])
    data = dict(
        name=newname,
        modules=viewjson['modules'],
        date=str(dt.now()),
        id=str(uuid.uuid1()),
        layout=viewjson['layout'],
    )
    data.update(**metadata())
    adapter.create(data=data)
~~    flash('Created new dashboard clone "{}"'.format(newname))
    return redirect(url_for('jsondash.view', c_id=data['id']))



## ... source file continues with no further flash examples...

```


## Example 5 from flask-login
[Flask-Login](https://github.com/maxcountryman/flask-login)
([project documentation](https://flask-login.readthedocs.io/en/latest/)
and [PyPI package](https://pypi.org/project/Flask-Login/))
is a [Flask](/flask.html) extension that provides user session
management, which handles common tasks such as logging in
and out of a [web application](/web-development.html) and
managing associated user session data. Flask-Login is
open sourced under the
[MIT license](https://github.com/maxcountryman/flask-login/blob/master/LICENSE).

[**flask-login / flask_login / login_manager.py**](https://github.com/maxcountryman/flask-login/blob/master/flask_login/./login_manager.py)

```python
# login_manager.py


import warnings
from datetime import datetime, timedelta

~~from flask import (_request_ctx_stack, abort, current_app, flash, redirect,
                   has_app_context, request, session)

from ._compat import text_type
from .config import (COOKIE_NAME, COOKIE_DURATION, COOKIE_SECURE,
                     COOKIE_HTTPONLY, COOKIE_SAMESITE, LOGIN_MESSAGE,
                     LOGIN_MESSAGE_CATEGORY, REFRESH_MESSAGE,
                     REFRESH_MESSAGE_CATEGORY, ID_ATTRIBUTE,
                     AUTH_HEADER_NAME, SESSION_KEYS, USE_SESSION_FOR_NEXT)
from .mixins import AnonymousUserMixin
from .signals import (user_loaded_from_cookie, user_loaded_from_header,
                      user_loaded_from_request, user_unauthorized,
                      user_needs_refresh, user_accessed, session_protected)
from .utils import (login_url as make_login_url, _create_identifier,
                    _user_context_processor, encode_cookie, decode_cookie,
                    make_next_param, expand_login_view)


class LoginManager(object):
    def __init__(self, app=None, add_context_processor=True):
        self.anonymous_user = AnonymousUserMixin

        self.login_view = None

        self.blueprint_login_views = {}


## ... source file abbreviated to get to flash examples ...


        self.init_app(app, add_context_processor)

    def init_app(self, app, add_context_processor=True):
        app.login_manager = self
        app.after_request(self._update_remember_cookie)

        if add_context_processor:
            app.context_processor(_user_context_processor)

    def unauthorized(self):
        user_unauthorized.send(current_app._get_current_object())

        if self.unauthorized_callback:
            return self.unauthorized_callback()

        if request.blueprint in self.blueprint_login_views:
            login_view = self.blueprint_login_views[request.blueprint]
        else:
            login_view = self.login_view

        if not login_view:
            abort(401)

        if self.login_message:
            if self.localize_callback is not None:
~~                flash(self.localize_callback(self.login_message),
                      category=self.login_message_category)
            else:
~~                flash(self.login_message, category=self.login_message_category)

        config = current_app.config
        if config.get('USE_SESSION_FOR_NEXT', USE_SESSION_FOR_NEXT):
            login_url = expand_login_view(login_view)
            session['_id'] = self._session_identifier_generator()
            session['next'] = make_next_param(login_url, request.url)
            redirect_url = make_login_url(login_view)
        else:
            redirect_url = make_login_url(login_view, next_url=request.url)

        return redirect(redirect_url)

    def user_loader(self, callback):
        self._user_callback = callback
        return self.user_callback

    @property
    def user_callback(self):
        return self._user_callback

    def request_loader(self, callback):
        self._request_callback = callback
        return self.request_callback

    @property
    def request_callback(self):
        return self._request_callback

    def unauthorized_handler(self, callback):
        self.unauthorized_callback = callback
        return callback

    def needs_refresh_handler(self, callback):
        self.needs_refresh_callback = callback
        return callback

    def needs_refresh(self):
        user_needs_refresh.send(current_app._get_current_object())

        if self.needs_refresh_callback:
            return self.needs_refresh_callback()

        if not self.refresh_view:
            abort(401)

        if self.needs_refresh_message:
            if self.localize_callback is not None:
~~                flash(self.localize_callback(self.needs_refresh_message),
                      category=self.needs_refresh_message_category)
            else:
~~                flash(self.needs_refresh_message,
                      category=self.needs_refresh_message_category)

        config = current_app.config
        if config.get('USE_SESSION_FOR_NEXT', USE_SESSION_FOR_NEXT):
            login_url = expand_login_view(self.refresh_view)
            session['_id'] = self._session_identifier_generator()
            session['next'] = make_next_param(login_url, request.url)
            redirect_url = make_login_url(self.refresh_view)
        else:
            login_url = self.refresh_view
            redirect_url = make_login_url(login_url, next_url=request.url)

        return redirect(redirect_url)

    def header_loader(self, callback):
        print('LoginManager.header_loader is deprecated. Use ' +
              'LoginManager.request_loader instead.')
        self._header_callback = callback
        return callback

    def _update_request_context_with_user(self, user=None):

        ctx = _request_ctx_stack.top
        ctx.user = self.anonymous_user() if user is None else user


## ... source file continues with no further flash examples...

```


## Example 6 from tedivms-flask
[tedivm's flask starter app](https://github.com/tedivm/tedivms-flask) is a
base of [Flask](/flask.html) code and related projects such as
[Celery](/celery.html) which provides a template to start your own
Flask web app. The project comes baked with an admin panel,
[API authentication and authorization](/application-programming-interfaces.html),
[SQLAlchemy](/sqlalchemy.html) and many other common libraries that are
often used with Flask.

The project's code is provided as open source under the
[BSD 2-Clause "Simplified" license](https://github.com/tedivm/tedivms-flask/blob/master/LICENSE.txt).

[**tedivms-flask / app / views / misc_views.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/views/misc_views.py)

```python
# misc_views.py

from flask import Blueprint, redirect, render_template, current_app, abort
~~from flask import request, url_for, flash, send_from_directory, jsonify, render_template_string
from flask_user import current_user, login_required, roles_accepted

from app import db
from app.models.user_models import UserProfileForm, User, UsersRoles, Role
from app.utils.forms import ConfirmationForm
import uuid, json, os
import datetime

main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/')
def member_page():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    return render_template('pages/member_base.html')

@main_blueprint.route('/admin')
@roles_accepted('admin')
def admin_page():
    return redirect(url_for('main.user_admin_page'))

@main_blueprint.route('/users')
@roles_accepted('admin')
def user_admin_page():


## ... source file abbreviated to get to flash examples ...



    form = UserProfileForm()
    roles = Role.query.all()
    form.roles.choices = [(x.id,x.name) for x in roles]

    if form.validate():
        user = User.query.filter(User.email == request.form['email']).first()
        if not user:
            user = User(email=form.email.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        password=current_app.user_manager.hash_password(form.password.data),
                        active=True,
                        email_confirmed_at=datetime.datetime.utcnow())
            db.session.add(user)
            db.session.commit()
            allowed_roles = form.roles.data
            for role in roles:
                if role.id not in allowed_roles:
                    if role in user.roles:
                        user.roles.remove(role)
                else:
                    if role not in user.roles:
                        user.roles.append(role)
            db.session.commit()
~~            flash('You successfully created the new user.', 'success')
            return redirect(url_for('main.user_admin_page'))
~~        flash('A user with that email address already exists', 'error')
    return render_template('pages/admin/create_user.html', form=form)


@main_blueprint.route('/users/<user_id>/delete', methods=['GET', 'POST'])
@roles_accepted('admin')
def delete_user_page(user_id):
    if current_app.config.get('USER_LDAP', False):
        abort(400)
    form = ConfirmationForm()
    user = User.query.filter(User.id == user_id).first()
    if not user:
        abort(404)
    if form.validate():
        db.session.query(UsersRoles).filter_by(user_id = user_id).delete()
        db.session.query(User).filter_by(id = user_id).delete()
        db.session.commit()
~~        flash('You successfully deleted your user!', 'success')
        return redirect(url_for('main.user_admin_page'))
    return render_template('pages/admin/delete_user.html', form=form)


@main_blueprint.route('/users/<user_id>/edit', methods=['GET', 'POST'])
@roles_accepted('admin')
def edit_user_page(user_id):
    if current_app.config.get('USER_LDAP', False):
        abort(400)

    user = User.query.filter(User.id == user_id).first()
    if not user:
        abort(404)

    form = UserProfileForm(obj=user)
    roles = Role.query.all()
    form.roles.choices = [(x.id,x.name) for x in roles]

    if form.validate():
        if 'password' in request.form and len(request.form['password']) >= 8:
            user.password = current_app.user_manager.hash_password(request.form['password'])
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.active = form.active.data

        allowed_roles = form.roles.data
        for role in roles:
            if role.id not in allowed_roles:
                if role in user.roles:
                    user.roles.remove(role)
            else:
                if role not in user.roles:
                    user.roles.append(role)

        db.session.commit()
~~        flash('You successfully edited the user.', 'success')
        return redirect(url_for('main.user_admin_page'))

    form.roles.data = [role.id for role in user.roles]
    return render_template('pages/admin/edit_user.html', form=form)

@main_blueprint.route('/pages/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    if current_app.config.get('USER_LDAP', False):
        abort(400)

    form = UserProfileForm(request.form, obj=current_user)

    if request.method == 'POST' and form.validate():
        form.populate_obj(current_user)

        db.session.commit()

        return redirect(url_for('main.user_profile_page'))

    return render_template('pages/user_profile_page.html',
                           current_user=current_user,
                           form=form)



## ... source file continues with no further flash examples...

```

