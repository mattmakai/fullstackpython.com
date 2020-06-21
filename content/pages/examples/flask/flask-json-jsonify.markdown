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

    def _protect(f):
        if hasattr(f, "_permission_name"):
            permission_str = f._permission_name
        else:
            permission_str = f.__name__

        def wraps(self, *args, **kwargs):
            permission_str = "{}{}".format(PERMISSION_PREFIX, f._permission_name)
            if self.method_permission_name:


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

    def wraps(f):
        f._permission_name = name
        return f

    return wraps



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


    def post(self, user_id=None):
        if request.is_xhr:
            ids = request.get_json()["ids"]

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
            on_fail=FlashAndRedirect(


## ... source file abbreviated to get to jsonify examples ...


            )
            return redirect(url_for("management.overview"))

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


        )
    ]

    def post(self, group_id=None):
        if request.is_xhr:
            ids = request.get_json()["ids"]
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


    def post(self, report_id=None):

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

        reports = Report.query.filter(Report.zapped == None).all()
        report_list = []
        for report in reports:


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

[**sandman2 / sandman2 / service.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./service.py)

```python
# service.py

from flask import request, make_response
~~import flask
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

~~    response = flask.jsonify(resource.to_dict())
    response = add_link_headers(response, resource.links())
    return response


def is_valid_method(model, resource=None):
    validation_function_name = 'is_valid_{}'.format(
        request.method.lower())
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
        if request.path.endswith('meta'):
            return self._meta()

        if resource_id is None:
            error_message = is_valid_method(self.__model__)
            if error_message:
                raise BadRequestException(error_message)

            if 'export' in request.args: 
                return self._export(self._all_resources())

~~            return flask.jsonify({
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
        if not request.json:
            raise BadRequestException('No JSON data received')
        resource.update(request.json)
        db.session().merge(resource)
        db.session().commit()
        return jsonify(resource)

    @validate_fields
    def post(self):
        resource = self.__model__.query.filter_by(**request.json).first()


## ... source file abbreviated to get to jsonify examples ...


    def put(self, resource_id):
        resource = self.__model__.query.get(resource_id)
        if resource:
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
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
~~        return flask.jsonify(self.__model__.description())

    def _resource(self, resource_id):
        resource = self.__model__.query.get(resource_id)
        if not resource:
            raise NotFoundException()
        return resource

    def _all_resources(self):
        queryset = self.__model__.query
        args = {k: v for (k, v) in request.args.items() if k not in ('page', 'export')}
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

[**tedivms-flask / app / views / apis.py**](https://github.com/tedivm/tedivms-flask/blob/master/app/views/apis.py)

```python
# apis.py

from flask import Blueprint, redirect
~~from flask import request, url_for, jsonify, current_app

from app import db
from app.models import user_models
from app.utils.api import roles_accepted_api
from app.extensions.ldap import authenticate

import uuid

api_blueprint = Blueprint('api', __name__, template_folder='templates')

@api_blueprint.route('/api/credentials', methods=['POST'])
def api_create_credentials():
    username = request.form['username']
    password = request.form['password']
    label = request.form.get('label', None)
    user = user_models.User.query.filter(user_models.User.email == username).first()
    if not user:
        user = user_models.User.query.filter(user_models.User.username == username).first()
        if not user:
            abort(400)

    if current_app.config.get('USER_LDAP', False):
        if not authenticate(username, password):
            abort(401)
    else:
        if not current_app.user_manager.verify_password(password, user.password):
            abort(401)

    id = uuid.uuid4().hex[0:12]
    key = uuid.uuid4().hex
    hash = current_app.user_manager.hash_password(key)
    new_key = user_models.ApiKey(id=id, hash=hash, user_id=user.id, label=label)
    db.session.add(new_key)
    db.session.commit()

~~    return jsonify({'id': id,'key': key})



## ... source file continues with no further jsonify examples...

```

