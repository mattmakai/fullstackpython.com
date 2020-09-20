title: flask.helpers flash Example Code
category: page
slug: flask-helpers-flash-examples
sortorder: 500021018
toc: False
sidebartitle: flask.helpers flash
meta: Python example code that shows how to use the flash callable from the flask.helpers module of the Flask project.


[flash](https://github.com/pallets/flask/blob/master/src/flask/helpers.py)
is a function within the `flask.helpers` module of the [Flask](/flask.html)
framework. `flash` passes a string message to the *next* request. The
following request can access it in a template by using the
`get_flashed_messages` function.

`flash` can also be imported directly from the `flask` module instead
of `flask.helpers` so you will often see that shortcut in example code.

<a href="/flask-helpers-get-root-path-examples.html">get_root_path</a>,
<a href="/flask-helpers-make-response-examples.html">make_response</a>,
<a href="/flask-helpers-safe-join-examples.html">safe_join</a>,
<a href="/flask-helpers-send-file-examples.html">send_file</a>,
and <a href="/flask-helpers-url-for-examples.html">url_for</a>
are several other callables with code examples from the same `flask.helpers` package.

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



## ... source file abbreviated to get to flash examples ...


            'icon': 'success',
            'message': 'Your test transaction has been successfully processed. See the Braintree API response and try again.'
        }
    else:
        result = {
            'header': 'Transaction Failed',
            'icon': 'fail',
            'message': 'Your test transaction has a status of ' + transaction.status + '. See the Braintree API response and try again.'
        }

    return render_template('checkouts/show.html', transaction=transaction, result=result)

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
~~        for x in result.errors.deep_errors: flash('Error: %s: %s' % (x.code, x.message))
        return redirect(url_for('new_checkout'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)



## ... source file continues with no further flash examples...

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


## Example 3 from FlaskBB
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


## Example 4 from flask-bones
[flask-bones](https://github.com/cburmeister/flask-bones)
([demo](http://flask-bones.herokuapp.com/))
is large scale [Flask](/flask.html) example application built
with [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
([example Blueprint code](/flask-blueprints-blueprint-examples.html)).
This project is provided as open source under the
[MIT license](https://github.com/cburmeister/flask-bones/blob/master/LICENSE).

[**flask-bones / app / user / views.py**](https://github.com/cburmeister/flask-bones/blob/master/app/user/views.py)

```python
# views.py
~~from flask import request, redirect, url_for, render_template, flash, g
from flask_babel import gettext
from flask_login import login_required
from app.user.models import User
from .forms import EditUserForm

from ..user import user


@user.route('/list', methods=['GET', 'POST'])
@login_required
def list():

    from app.database import DataTable
    datatable = DataTable(
        model=User,
        columns=[User.remote_addr],
        sortable=[User.username, User.email, User.created_ts],
        searchable=[User.username, User.email],
        filterable=[User.active],
        limits=[25, 50, 100],
        request=request
    )

    if g.pjax:
        return render_template('users.html', datatable=datatable)

    return render_template('list.html', datatable=datatable)


@user.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    user = User.query.filter_by(id=id).first_or_404()
    form = EditUserForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        user.update()
~~        flash(
            gettext('User {username} edited'.format(username=user.username)),
            'success'
        )
    return render_template('edit.html', form=form, user=user)


@user.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete(id):
    user = User.query.filter_by(id=id).first_or_404()
    user.delete()
~~    flash(
        gettext('User {username} deleted').format(username=user.username),
        'success'
    )
    return redirect(url_for('.list'))



## ... source file continues with no further flash examples...

```


## Example 5 from flask-bookshelf
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


## Example 6 from flask_jsondash
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


## Example 7 from flask-login
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


## Example 8 from Flask-Security-Too
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


## ... source file abbreviated to get to flash examples ...


        string = string.encode("utf-8")
    return string


def hash_data(data):
    return _hashing_context.hash(encode_string(data))


def verify_hash(hashed_data, compare_data):
    return _hashing_context.verify(encode_string(compare_data), hashed_data)


def suppress_form_csrf():
    if get_request_attr("fs_ignore_csrf"):
        return {"csrf": False}
    if (
        config_value("CSRF_IGNORE_UNAUTH_ENDPOINTS")
        and not current_user.is_authenticated
    ):
        return {"csrf": False}
    return {}


def do_flash(message, category=None):
    if config_value("FLASH_MESSAGES"):
~~        flash(message, category)


def get_url(endpoint_or_url, qparams=None):
    try:
        return transform_url(url_for(endpoint_or_url), qparams)
    except Exception:
        if _security.redirect_host:
            url = transform_url(
                endpoint_or_url, qparams, netloc=_security.redirect_host
            )
        else:
            url = transform_url(endpoint_or_url, qparams)

        return url


def slash_url_suffix(url, suffix):

    return url.endswith("/") and ("%s/" % suffix) or ("/%s" % suffix)


def transform_url(url, qparams=None, **kwargs):
    if not url:
        return url


## ... source file continues with no further flash examples...

```


## Example 9 from Flask-User
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

[**Flask-User / flask_user / user_manager__views.py**](https://github.com/lingthio/Flask-User/blob/master/flask_user/./user_manager__views.py)

```python
# user_manager__views.py


from datetime import datetime
try:
    from urllib.parse import quote, unquote    # Python 3
except ImportError:
    from urllib import quote, unquote          # Python 2

~~from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from .decorators import login_required
from . import signals
from .translation_utils import gettext as _    # map _() to gettext()


class UserManager__Views(object):


    @login_required
    def change_password_view(self):

        form = self.ChangePasswordFormClass(request.form)

        if request.method == 'POST':
            if not form.validate():
~~                flash(_('There was an error changing your password.'), 'error')
                return redirect(url_for('user.change_password'))

            new_password = form.new_password.data
            password_hash = self.hash_password(new_password)

            current_user.password = password_hash
            self.db_manager.save_object(current_user)
            self.db_manager.commit()

            if self.USER_ENABLE_EMAIL and self.USER_SEND_PASSWORD_CHANGED_EMAIL:
                self.email_manager.send_password_changed_email(current_user)

            signals.user_changed_password.send(current_app._get_current_object(), user=current_user)

~~            flash(_('Your password has been changed successfully.'), 'success')

            safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_CHANGE_PASSWORD_ENDPOINT)
            return redirect(safe_next_url)

        self.prepare_domain_translations()
        return render_template(self.USER_CHANGE_PASSWORD_TEMPLATE, form=form)


    @login_required
    def change_username_view(self):

        form = self.ChangeUsernameFormClass(request.form)

        if request.method == 'POST' and form.validate():

            new_username = form.new_username.data
            current_user.username=new_username
            self.db_manager.save_object(current_user)
            self.db_manager.commit()

            if self.USER_ENABLE_EMAIL and self.USER_SEND_USERNAME_CHANGED_EMAIL:
                self.email_manager.send_username_changed_email(current_user)

            signals.user_changed_username.send(current_app._get_current_object(), user=current_user)

~~            flash(_("Your username has been changed to '%(username)s'.", username=new_username), 'success')

            safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_CHANGE_USERNAME_ENDPOINT)
            return redirect(safe_next_url)

        self.prepare_domain_translations()
        return render_template(self.USER_CHANGE_USERNAME_TEMPLATE, form=form)


    def confirm_email_view(self, token):
        data_items = self.token_manager.verify_token(
            token,
            self.USER_CONFIRM_EMAIL_EXPIRATION)

        user = None
        user_email = None
        if data_items:
            user, user_email = self.db_manager.get_user_and_user_email_by_id(data_items[0])

        if not user or not user_email:
~~            flash(_('Invalid confirmation token.'), 'error')
            return redirect(url_for('user.login'))

        user_email.email_confirmed_at=datetime.utcnow()
        self.db_manager.save_user_and_user_email(user, user_email)
        self.db_manager.commit()

        signals.user_confirmed_email.send(current_app._get_current_object(), user=user)

~~        flash(_('Your email has been confirmed.'), 'success')

        safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_CONFIRM_ENDPOINT)
        if self.USER_AUTO_LOGIN_AFTER_CONFIRM:
            return self._do_login_user(user, safe_next_url)  # auto-login
        else:
            return redirect(url_for('user.login') + '?next=' + quote(safe_next_url))  # redirect to login page


    @login_required
    def edit_user_profile_view(self):
        form = self.EditUserProfileFormClass(request.form, obj=current_user)

        if request.method == 'POST' and form.validate():
            form.populate_obj(current_user)

            self.db_manager.save_object(current_user)
            self.db_manager.commit()

            return redirect(self._endpoint_url(self.USER_AFTER_EDIT_USER_PROFILE_ENDPOINT))

        self.prepare_domain_translations()
        return render_template(self.USER_EDIT_USER_PROFILE_TEMPLATE, form=form)

    @login_required


## ... source file abbreviated to get to flash examples ...


            user_email.is_primary=True
            self.db_manager.save_object(user_email)
            self.db_manager.commit()

        elif action == 'confirm':
            self._send_confirm_email_email(user_email.user, user_email)
        else:
            return self.unauthorized_view()

        return redirect(url_for('user.manage_emails'))


    def forgot_password_view(self):

        form = self.ForgotPasswordFormClass(request.form)

        if request.method == 'POST' and form.validate():
            email = form.email.data
            user, user_email = self.db_manager.get_user_and_user_email_by_email(email)

            if user and user_email:
                self.email_manager.send_reset_password_email(user, user_email)

                signals.user_forgot_password.send(current_app._get_current_object(), user=user)

~~            flash(_(
                "A reset password email has been sent to '%(email)s'. Open that email and follow the instructions to reset your password.",
                email=email), 'success')

            return redirect(self._endpoint_url(self.USER_AFTER_FORGOT_PASSWORD_ENDPOINT))

        self.prepare_domain_translations()
        return render_template(self.USER_FORGOT_PASSWORD_TEMPLATE, form=form)

    @login_required
    def manage_emails_view(self):

        user_emails = self.db_manager.find_user_emails(user=current_user)
        form = self.AddEmailFormClass()

        if request.method == "POST" and form.validate():
            new_email = form.email.data
            user_email = self.db_manager.add_user_email(user=current_user, email=new_email)
            self.db_manager.save_object(user_email)
            self.db_manager.commit()
            return redirect(url_for('user.manage_emails'))

        self.prepare_domain_translations()
        return render_template(self.USER_MANAGE_EMAILS_TEMPLATE,
                      user_emails=user_emails,
                      form=form,
                      )

    @login_required
    def invite_user_view(self):

        invite_user_form = self.InviteUserFormClass(request.form)

        if request.method == 'POST' and invite_user_form.validate():
            email = invite_user_form.email.data
            user, user_email = self.db_manager.get_user_and_user_email_by_email(email)
            if user:
~~                flash("User with that email has already registered", "error")
                return redirect(url_for('user.invite_user'))

            user_invitation = self.db_manager.add_user_invitation(
                email=email,
                invited_by_user_id=current_user.id)
            self.db_manager.commit()

            try:
                self.email_manager.send_invite_user_email(current_user, user_invitation)
            except Exception as e:
                self.db_manager.delete_object(user_invitation)
                self.db_manager.commit()
                raise

            signals \
                .user_sent_invitation \
                .send(current_app._get_current_object(), user_invitation=user_invitation,
                      form=invite_user_form)

~~            flash(_('Invitation has been sent.'), 'success')

            safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_INVITE_ENDPOINT)
            return redirect(safe_next_url)

        self.prepare_domain_translations()
        return render_template(self.USER_INVITE_USER_TEMPLATE, form=invite_user_form)


    def login_view(self):


        safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_LOGIN_ENDPOINT)
        safe_reg_next = self._get_safe_next_url('reg_next', self.USER_AFTER_REGISTER_ENDPOINT)

        if self.call_or_get(current_user.is_authenticated) and self.USER_AUTO_LOGIN_AT_LOGIN:
            return redirect(safe_next_url)

        login_form = self.LoginFormClass(request.form)  # for login.html
        register_form = self.RegisterFormClass()  # for login_or_register.html
        if request.method != 'POST':
            login_form.next.data = register_form.next.data = safe_next_url
            login_form.reg_next.data = register_form.reg_next.data = safe_reg_next

        if request.method == 'POST' and login_form.validate():


## ... source file abbreviated to get to flash examples ...


            if self.USER_ENABLE_USERNAME:
                user = self.db_manager.find_user_by_username(login_form.username.data)

                if not user and self.USER_ENABLE_EMAIL:
                    user, user_email = self.db_manager.get_user_and_user_email_by_email(login_form.username.data)
            else:
                user, user_email = self.db_manager.get_user_and_user_email_by_email(login_form.email.data)

            if user:
                safe_next_url = self.make_safe_url(login_form.next.data)
                return self._do_login_user(user, safe_next_url, login_form.remember_me.data)

        self.prepare_domain_translations()
        template_filename = self.USER_LOGIN_AUTH0_TEMPLATE if self.USER_ENABLE_AUTH0 else self.USER_LOGIN_TEMPLATE
        return render_template(template_filename,
                      form=login_form,
                      login_form=login_form,
                      register_form=register_form)

    def logout_view(self):

        signals.user_logged_out.send(current_app._get_current_object(), user=current_user)

        logout_user()

~~        flash(_('You have signed out successfully.'), 'success')

        safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_LOGOUT_ENDPOINT)
        return redirect(safe_next_url)

    def register_view(self):

        safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_LOGIN_ENDPOINT)
        safe_reg_next_url = self._get_safe_next_url('reg_next', self.USER_AFTER_REGISTER_ENDPOINT)

        login_form = self.LoginFormClass()  # for login_or_register.html
        register_form = self.RegisterFormClass(request.form)  # for register.html

        invite_token = request.values.get("token")

        if self.USER_REQUIRE_INVITATION and not invite_token:
~~            flash("Registration is invite only", "error")
            return redirect(url_for('user.login'))

        user_invitation = None
        if invite_token and self.db_manager.UserInvitationClass:
            data_items = self.token_manager.verify_token(invite_token, self.USER_INVITE_EXPIRATION)
            if data_items:
                user_invitation_id = data_items[0]
                user_invitation = self.db_manager.get_user_invitation_by_id(user_invitation_id)

            if not user_invitation:
~~                flash("Invalid invitation token", "error")
                return redirect(url_for('user.login'))

            register_form.invite_token.data = invite_token

        if request.method != 'POST':
            login_form.next.data = register_form.next.data = safe_next_url
            login_form.reg_next.data = register_form.reg_next.data = safe_reg_next_url
            if user_invitation:
                register_form.email.data = user_invitation.email

        if request.method == 'POST' and register_form.validate():
            user = self.db_manager.add_user()
            register_form.populate_obj(user)
            user_email = self.db_manager.add_user_email(user=user, is_primary=True)
            register_form.populate_obj(user_email)

            user.password = self.hash_password(user.password)

            request_email_confirmation = self.USER_ENABLE_CONFIRM_EMAIL
            if user_invitation:
                if user_invitation.email.lower() == register_form.email.data.lower():
                    user_email.email_confirmed_at=datetime.utcnow()
                    request_email_confirmation = False



## ... source file abbreviated to get to flash examples ...



        self.prepare_domain_translations()
        return render_template(self.USER_RESEND_CONFIRM_EMAIL_TEMPLATE, form=form)


    def reset_password_view(self, token):

        if self.call_or_get(current_user.is_authenticated):
            logout_user()

        data_items = self.token_manager.verify_token(
            token,
            self.USER_RESET_PASSWORD_EXPIRATION)

        user = None
        if data_items:
            user_id = data_items[0]
            user = self.db_manager.get_user_by_id(user_id)

            user_or_user_email_object = self.db_manager.get_primary_user_email_object(user)
            user_or_user_email_object.email_confirmed_at = datetime.utcnow()
            self.db_manager.save_object(user_or_user_email_object)
            self.db_manager.commit()

        if not user:
~~            flash(_('Your reset password token is invalid.'), 'error')
            return redirect(self._endpoint_url('user.login'))


        form = self.ResetPasswordFormClass(request.form)

        if request.method == 'POST' and form.validate():
            password_hash = self.hash_password(form.new_password.data)
            user.password=password_hash
            self.db_manager.save_object(user)
            self.db_manager.commit()

            if self.USER_ENABLE_EMAIL and self.USER_SEND_PASSWORD_CHANGED_EMAIL:
                self.email_manager.send_password_changed_email(user)

            signals.user_reset_password.send(current_app._get_current_object(), user=user)

~~            flash(_("Your password has been reset successfully."), 'success')

            safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_RESET_PASSWORD_ENDPOINT)
            if self.USER_AUTO_LOGIN_AFTER_RESET_PASSWORD:
                return self._do_login_user(user, safe_next_url)  # auto-login
            else:
                return redirect(url_for('user.login') + '?next=' + quote(safe_next_url))  # redirect to login page

        self.prepare_domain_translations()
        return render_template(self.USER_RESET_PASSWORD_TEMPLATE, form=form)

    def unauthenticated_view(self):
        url = request.url
~~        flash(_("You must be signed in to access '%(url)s'.", url=url), 'error')

        safe_next_url = self.make_safe_url(url)
        return redirect(self._endpoint_url(self.USER_UNAUTHENTICATED_ENDPOINT)+'?next='+quote(safe_next_url))


    def unauthorized_view(self):
        url = request.script_root + request.path
~~        flash(_("You do not have permission to access '%(url)s'.", url=url), 'error')

        return redirect(self._endpoint_url(self.USER_UNAUTHORIZED_ENDPOINT))



    def _send_registered_email(self, user, user_email, request_email_confirmation):
        um =  current_app.user_manager

        if self.USER_ENABLE_EMAIL and self.USER_SEND_REGISTERED_EMAIL:

            self.email_manager.send_registered_email(user, user_email, request_email_confirmation)

            if request_email_confirmation:
                email = user_email.email if user_email else user.email
~~                flash(_('A confirmation email has been sent to %(email)s with instructions to complete your registration.', email=email), 'success')
            else:
~~                flash(_('You have registered successfully.'), 'success')


    def _send_confirm_email_email(self, user, user_email):

        if self.USER_ENABLE_EMAIL and self.USER_ENABLE_CONFIRM_EMAIL:
            self.email_manager.send_confirm_email_email(user, user_email)

            email = user_email.email if user_email else user.email
~~            flash(_('A confirmation email has been sent to %(email)s with instructions to complete your registration.', email=email), 'success')


    def _do_login_user(self, user, safe_next_url, remember_me=False):
        if not user: return self.unauthenticated()

        if not user.active:
~~            flash(_('Your account has not been enabled.'), 'error')
            return redirect(url_for('user.login'))

        if self.USER_ENABLE_EMAIL \
                and self.USER_ENABLE_CONFIRM_EMAIL \
                and not current_app.user_manager.USER_ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL \
                and not self.db_manager.user_has_confirmed_email(user):
            url = url_for('user.resend_email_confirmation')
~~            flash(_('Your email address has not yet been confirmed. Check your email Inbox and Spam folders for the confirmation email or <a href="%(url)s">Re-send confirmation email</a>.', url=url), 'error')
            return redirect(url_for('user.login'))

        login_user(user, remember=remember_me)

        signals.user_logged_in.send(current_app._get_current_object(), user=user)

~~        flash(_('You have signed in successfully.'), 'success')

        return redirect(safe_next_url)


    def _get_safe_next_url(self, param_name, default_endpoint):

        if param_name in request.args:
            safe_next_url = current_app.user_manager.make_safe_url(unquote(request.args[param_name]))

        else:
            safe_next_url = self._endpoint_url(default_endpoint)

        return safe_next_url


    def _endpoint_url(self, endpoint):
        return url_for(endpoint) if endpoint else '/'



## ... source file continues with no further flash examples...

```


## Example 10 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / util / roles.py**](https://github.com/indico/indico/blob/master/indico/util/roles.py)

```python
# roles.py

from __future__ import unicode_literals

import csv

~~from flask import flash, session

from indico.core.errors import UserValueError
from indico.modules.events.roles.forms import ImportMembersCSVForm
from indico.modules.users import User
from indico.util.i18n import _, ngettext
from indico.util.string import to_unicode, validate_email
from indico.web.flask.templating import get_template_module
from indico.web.util import jsonify_data, jsonify_template


class ImportRoleMembersMixin(object):

    logger = None

    def import_members_from_csv(self, f):
        reader = csv.reader(f.read().splitlines())
        emails = set()

        for num_row, row in enumerate(reader, 1):
            if len(row) != 1:
                raise UserValueError(_('Row {}: malformed CSV data').format(num_row))
            email = to_unicode(row[0]).strip().lower()

            if email and not validate_email(email):
                raise UserValueError(_('Row {row}: invalid email address: {email}').format(row=num_row, email=email))
            if email in emails:
                raise UserValueError(_('Row {}: email address is not unique').format(num_row))
            emails.add(email)

        users = set(User.query.filter(-User.is_deleted, User.all_emails.in_(emails)))
        users_emails = {user.email for user in users}
        unknown_emails = emails - users_emails
        new_members = users - self.role.members
        return new_members, users, unknown_emails

    def _process(self):
        form = ImportMembersCSVForm()

        if form.validate_on_submit():
            new_members, users, unknown_emails = self.import_members_from_csv(form.source_file.data)
            if form.remove_existing.data:
                deleted_members = self.role.members - users
                for member in deleted_members:
                    self.logger.info('User {} removed from role {} by {}'.format(member, self.role, session.user))
                self.role.members = users
            else:
                self.role.members |= users
            for user in new_members:
                self.logger.info('User {} added to role {} by {}'.format(user, self.role, session.user))
~~            flash(ngettext("{} member has been imported.",
                           "{} members have been imported.",
                           len(users)).format(len(users)), 'success')
            if unknown_emails:
~~                flash(ngettext("There is no user with this email address: {}",
                               "There are no users with these email addresses: {}",
                               len(unknown_emails)).format(', '.join(unknown_emails)), 'warning')
            tpl = get_template_module('events/roles/_roles.html')
            return jsonify_data(html=tpl.render_role(self.role, collapsed=False, email_button=False))
        return jsonify_template('events/roles/import_members.html', form=form, role=self.role)



## ... source file continues with no further flash examples...

```


## Example 11 from tedivms-flask
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

