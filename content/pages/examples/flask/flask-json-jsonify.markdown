title: flask.json jsonify code examples
category: page
slug: flask-json-jsonify-examples
sortorder: 500021012
toc: False
sidebartitle: flask.json jsonify
meta: Python example code for the jsonify function from the flask.json module of the Flask project.


jsonify is a function within the flask.json module of the Flask project.


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
    """
        Use this decorator to enable granular security permissions
        to your API methods (BaseApi and child classes).
        Permissions will be associated to a role, and roles are associated to users.

        allow_browser_login will accept signed cookies obtained from the normal MVC app::

            class MyApi(BaseApi):
                @expose('/dosonmething', methods=['GET'])
                @protect(allow_browser_login=True)


## ... source file abbreviated to get to jsonify examples ...


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
            response = make_response(
~~                jsonify(
                    {"message": str(FLAMSG_ERR_SEC_ACCESS_DENIED), "severity": "danger"}
                ),
                401,
            )
            response.headers["Content-Type"] = "application/json"
            return response

    f._permission_name = permission_str
    return functools.update_wrapper(wraps, f)


def permission_name(name):
    """
        Use this decorator to override the name of the permission.
        has_access will use the methods name has the permission name
        if you want to override this add this decorator to your methods.
        This is useful if you want to aggregate methods to permissions

        It will add '_permission_name' attribute to your method
        that will be inspected by BaseView to collect your view's
        permissions.

        Note that you should use @has_access to execute after @permission_name
        like on the following example.


## ... source file continues with no further jsonify examples...


```


## Example 2 from FlaskBB
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
# -*- coding: utf-8 -*-
"""
    flaskbb.management.views
    ------------------------

    This module handles the management views.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
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


## ... source file abbreviated to get to jsonify examples ...


        if request.is_xhr:
            ids = request.get_json()["ids"]

            data = []
            for user in User.query.filter(User.id.in_(ids)).all():
                # do not delete current user
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

~~            return jsonify(
                message="{} users deleted.".format(len(data)),
                category="success",
                data=data,
                status=200
            )

        user = User.query.filter_by(id=user_id).first_or_404()

        if current_user.id == user.id:
            flash(_("You cannot delete yourself.", "danger"))
            return redirect(url_for("management.users"))

        user.delete()
        flash(_("User deleted."), "success")
        return redirect(url_for("management.users"))


class AddUser(MethodView):
    decorators = [
        allows.requires(
            IsAdmin,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to manage users"),
                level="danger",


## ... source file abbreviated to get to jsonify examples ...


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

~~            return jsonify(
                message="{} users banned.".format(len(data)),
                category="success",
                data=data,
                status=200
            )

        user = User.query.filter_by(id=user_id).first_or_404()
        # Do not allow moderators to ban admins
        if Permission(IsAdmin, identity=user) and Permission(
                Not(IsAdmin), identity=current_user):
            flash(_("A moderator cannot ban an admin user."), "danger")
            return redirect(url_for("management.overview"))

        if not current_user.id == user.id and user.ban():
            flash(_("User is now banned."), "success")
        else:
            flash(_("Could not ban user."), "danger")
        return redirect(url_for("management.banned_users"))


class UnbanUser(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,


## ... source file abbreviated to get to jsonify examples ...


            return redirect(url_for("management.overview"))

        # ajax request
        if request.is_xhr:
            ids = request.get_json()["ids"]

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

~~            return jsonify(
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


## ... source file abbreviated to get to jsonify examples ...


    ]

    def post(self, group_id=None):
        if request.is_xhr:
            ids = request.get_json()["ids"]
            # TODO: Get rid of magic numbers
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

~~                return jsonify(
                    message="{} groups deleted.".format(len(data)),
                    category="success",
                    data=data,
                    status=200
                )
~~            return jsonify(
                message=_("You cannot delete one of the standard groups."),
                category="danger",
                data=None,
                status=404
            )

        if group_id is not None:
            if group_id <= 6:  # there are 6 standard groups
                flash(
                    _(
                        "You cannot delete the standard groups. "
                        "Try renaming it instead.", "danger"
                    )
                )
                return redirect(url_for("management.groups"))

            group = Group.query.filter_by(id=group_id).first_or_404()
            group.delete()
            flash(_("Group deleted."), "success")
            return redirect(url_for("management.groups"))

        flash(_("No group chosen."), "danger")
        return redirect(url_for("management.groups"))



## ... source file abbreviated to get to jsonify examples ...



        # AJAX request
        if request.is_xhr:
            ids = request.get_json()["ids"]
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

~~            return jsonify(
                message="{} reports marked as read.".format(len(data)),
                category="success",
                data=data,
                status=200
            )

        # mark single report as read
        if report_id:
            report = Report.query.filter_by(id=report_id).first_or_404()
            if report.zapped:
                flash(
                    _("Report %(id)s is already marked as read.", id=report.id),
                    "success"
                )
                return redirect(url_for("management.reports"))

            report.zapped_by = current_user.id
            report.zapped = time_utcnow()
            report.save()
            flash(_("Report %(id)s marked as read.", id=report.id), "success")
            return redirect(url_for("management.reports"))

        # mark all as read
        reports = Report.query.filter(Report.zapped == None).all()


## ... source file abbreviated to get to jsonify examples ...


    ]

    def post(self, report_id=None):

        if request.is_xhr:
            ids = request.get_json()["ids"]
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

~~            return jsonify(
                message="{} reports deleted.".format(len(data)),
                category="success",
                data=data,
                status=200
            )

        report = Report.query.filter_by(id=report_id).first_or_404()
        report.delete()
        flash(_("Report deleted."), "success")
        return redirect(url_for("management.reports"))


class CeleryStatus(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to access the management settings"),  # noqa
                level="danger",
                endpoint="management.overview"
            )
        )
    ]

    def get(self):
        celery_inspect = celery.control.inspect()
        try:
            celery_running = True if celery_inspect.ping() else False
        except Exception:
            # catching Exception is bad, and just catching ConnectionError
            # from redis is also bad because you can run celery with other
            # brokers as well.
            celery_running = False

~~        return jsonify(celery_running=celery_running, status=200)


class ManagementOverview(MethodView):
    decorators = [
        allows.requires(
            IsAtleastModerator,
            on_fail=FlashAndRedirect(
                message=_("You are not allowed to access the management panel"),
                level="danger",
                endpoint="forum.index"
            )
        )
    ]

    def get(self):
        # user and group stats
        banned_users = User.query.filter(
            Group.banned == True, Group.id == User.primary_group_id
        ).count()
        if not current_app.config["REDIS_ENABLED"]:
            online_users = User.query.filter(User.lastseen >= time_diff()
                                             ).count()
        else:
            online_users = len(get_online_users())


## ... source file continues with no further jsonify examples...


```


## Example 3 from flaskSaaS
[flaskSaas](https://github.com/alectrocute/flaskSaaS) is a boilerplate
starter project to build a software-as-a-service (SaaS) web application
in [Flask](/flask.html), with [Stripe](/stripe.html) for billing. The
boilerplate relies on many common Flask extensions such as
[Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/),
[Flask-Login](https://flask-login.readthedocs.io/en/latest/),
[Flask-Admin](https://flask-admin.readthedocs.io/en/latest/), and
many others. The project is provided as open source under the
[MIT license](https://github.com/alectrocute/flaskSaaS/blob/master/LICENSE).

[**flaskSaaS / app / views / main.py**](https://github.com/alectrocute/flaskSaaS/blob/master/app/views/main.py)

```python
# main.py
~~from flask import render_template, jsonify
from app import app
import random


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
~~    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

## ... source file continues with no further jsonify examples...


```


## Example 4 from sandman2
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

[**sandman2 / sandman2 / app.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./app.py)

```python
# app.py
"""Sandman2 main application setup code."""

# Third-party imports
~~from flask import Flask, current_app, jsonify
from sqlalchemy.sql import sqltypes

# Application imports
from sandman2.exception import (
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    NotAcceptableException,
    NotImplementedException,
    ConflictException,
    ServerErrorException,
    ServiceUnavailableException,
    )
from sandman2.service import Service
from sandman2.model import db, Model, AutomapModel
from sandman2.admin import CustomAdminView
from flask_admin import Admin
from flask_httpauth import HTTPBasicAuth

# Augment sandman2's Model class with the Automap and Flask-SQLAlchemy model
# classes
auth = HTTPBasicAuth()

def get_app(


## ... source file abbreviated to get to jsonify examples ...


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.classes = []
    db.init_app(app)
    admin = Admin(app, base_template='layout.html', template_mode='bootstrap3')
    _register_error_handlers(app)
    if user_models:
        with app.app_context():
            _register_user_models(user_models, admin, schema=schema)
    elif reflect_all:
        with app.app_context():
            _reflect_all(exclude_tables, admin, read_only, schema=schema)

    @app.route('/')
    def index():
        """Return a list of routes to the registered classes."""
        routes = {}
        for cls in app.classes:
            routes[cls.__model__.__name__] = '{}{{/{}}}'.format(
                cls.__model__.__url__,
                cls.__model__.primary_key())
~~        return jsonify(routes)
    return app


def _register_error_handlers(app):
    """Register error-handlers for the application.

    :param app: The application instance
    """
    @app.errorhandler(BadRequestException)
    @app.errorhandler(ForbiddenException)
    @app.errorhandler(NotAcceptableException)
    @app.errorhandler(NotFoundException)
    @app.errorhandler(ConflictException)
    @app.errorhandler(ServerErrorException)
    @app.errorhandler(NotImplementedException)
    @app.errorhandler(ServiceUnavailableException)
    def handle_application_error(error):  # pylint:disable=unused-variable
        """Handler used to send JSON error messages rather than default HTML
        ones."""
        response = jsonify(error.to_dict())
        response.status_code = error.code
        return response




## ... source file continues with no further jsonify examples...


```


## Example 5 from tedivms-flask
[tedivm's flask starter app](https://github.com/tedivm/tedivms-flask) is a
base of [Flask](/flask.html) code and related projects such as
[Celery](/celery.html) which provides a template to start your own
Flask web app. The project comes baked with an admin panel,
[API authentication and authorization](/application-programming-interfaces.html),
[SQLAlchemy](/sqlalchemy.html) and many other common libraries that are
often used with Flask.

The project's code is provided as open source under the
[BSD 2-Clause "Simplified" license](https://github.com/tedivm/tedivms-flask/blob/master/LICENSE.txt).

[**tedivms-flask / app / views / apikeys.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/views/apikeys.py)

```python
# apikeys.py
from flask import Blueprint, redirect, render_template, current_app
~~from flask import request, url_for, flash, send_from_directory, jsonify, render_template_string
from flask_user import current_user, login_required, roles_accepted

~~from flask import Flask, session, redirect, url_for, request, render_template, jsonify, abort
from app import db
from app.models import user_models as users
from app.utils import forms

import time
import uuid


# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@apikeys_blueprint.route'
apikeys_blueprint = Blueprint('apikeys', __name__, template_folder='templates')


@apikeys_blueprint.route('/user/apikeys')
@roles_accepted('dev', 'admin')
def apikeys_index():
    all_keys = users.ApiKey.query.filter_by(user_id=current_user.id).all()
    return render_template("apikeys/list.html", keys=all_keys)


@apikeys_blueprint.route('/user/create_apikey', methods=['GET', 'POST'])
@roles_accepted('dev', 'admin')
def apikeys_create():
    form = users.ApiKeyForm(request.form)
    if request.method == 'POST' and form.validate():


## ... source file continues with no further jsonify examples...


```

