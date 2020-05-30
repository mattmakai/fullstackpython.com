title: flask.cli with_appcontext Python code examples
category: page
slug: flask-cli-with-appcontext-examples
sortorder: 500021002
toc: False
sidebartitle: flask.cli with_appcontext
meta: Python example code for the with_appcontext function from the flask.cli module of the Flask project.


with_appcontext is a function within the flask.cli module of the Flask project.


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

[**Flask AppBuilder / flask_appbuilder / cli.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/./cli.py)

```python
# cli.py
from io import BytesIO
import os
import shutil
from urllib.request import urlopen
from zipfile import ZipFile

import click
from flask import current_app
~~from flask.cli import with_appcontext

from .const import AUTH_DB, AUTH_LDAP, AUTH_OAUTH, AUTH_OID, AUTH_REMOTE_USER


SQLA_REPO_URL = (
    "https://github.com/dpgaspar/Flask-AppBuilder-Skeleton/archive/master.zip"
)
MONGOENGIE_REPO_URL = (
    "https://github.com/dpgaspar/Flask-AppBuilder-Skeleton-me/archive/master.zip"
)
ADDON_REPO_URL = (
    "https://github.com/dpgaspar/Flask-AppBuilder-Skeleton-AddOn/archive/master.zip"
)


def echo_header(title):
    click.echo(click.style(title, fg="green"))
    click.echo(click.style("-" * len(title), fg="green"))


@click.group()
def fab():
    """ FAB flask group commands"""
    pass


@fab.command("create-admin")
@click.option("--username", default="admin", prompt="Username")
@click.option("--firstname", default="admin", prompt="User first name")
@click.option("--lastname", default="user", prompt="User last name")
@click.option("--email", default="admin@fab.org", prompt="Email")
@click.password_option()
~~@with_appcontext
def create_admin(username, firstname, lastname, email, password):
    """
        Creates an admin user
    """
    auth_type = {
        AUTH_DB: "Database Authentications",
        AUTH_OID: "OpenID Authentication",
        AUTH_LDAP: "LDAP Authentication",
        AUTH_REMOTE_USER: "WebServer REMOTE_USER Authentication",
        AUTH_OAUTH: "OAuth Authentication",
    }
    click.echo(
        click.style(
            "Recognized {0}.".format(
                auth_type.get(current_app.appbuilder.sm.auth_type, "No Auth method")
            ),
            fg="green",
        )
    )
    user = current_app.appbuilder.sm.find_user(username=username)
    if user:
        click.echo(click.style(f"Error! User already exists {username}", fg="red"))
        return
    user = current_app.appbuilder.sm.find_user(email=email)


## ... source file abbreviated to get to with_appcontext examples ...


        return
    role_admin = current_app.appbuilder.sm.find_role(
        current_app.appbuilder.sm.auth_role_admin
    )
    user = current_app.appbuilder.sm.add_user(
        username, firstname, lastname, email, role_admin, password
    )
    if user:
        click.echo(click.style("Admin User {0} created.".format(username), fg="green"))
    else:
        click.echo(click.style("No user created an error occured", fg="red"))


@fab.command("create-user")
@click.option("--role", default="Public", prompt="Role")
@click.option("--username", prompt="Username")
@click.option("--firstname", prompt="User first name")
@click.option("--lastname", prompt="User last name")
@click.option("--email", prompt="Email")
@click.password_option()
~~@with_appcontext
def create_user(role, username, firstname, lastname, email, password):
    """
        Create a user
    """
    user = current_app.appbuilder.sm.find_user(username=username)
    if user:
        click.echo(click.style(f"Error! User already exists {username}", fg="red"))
        return
    user = current_app.appbuilder.sm.find_user(email=email)
    if user:
        click.echo(click.style(f"Error! User already exists {username}", fg="red"))
        return
    role_object = current_app.appbuilder.sm.find_role(role)
    if not role_object:
        click.echo(click.style(f"Error! Role not found {role}", fg="red"))
        return
    user = current_app.appbuilder.sm.add_user(
        username, firstname, lastname, email, role_object, password
    )
    if user:
        click.echo(click.style("User {0} created.".format(username), fg="green"))
    else:
        click.echo(click.style("Error! No user created", fg="red"))


@fab.command("reset-password")
@click.option(
    "--username",
    default="admin",
    prompt="The username",
    help="Resets the password for a particular user.",
)
@click.password_option()
~~@with_appcontext
def reset_password(username, password):
    """
        Resets a user's password
    """
    user = current_app.appbuilder.sm.find_user(username=username)
    if not user:
        click.echo("User {0} not found.".format(username))
    else:
        current_app.appbuilder.sm.reset_password(user.id, password)
        click.echo(click.style("User {0} reseted.".format(username), fg="green"))


@fab.command("create-db")
~~@with_appcontext
def create_db():
    """
        Create all your database objects (SQLAlchemy specific).
    """
    from flask_appbuilder.models.sqla import Model

    engine = current_app.appbuilder.get_session.get_bind(mapper=None, clause=None)
    Model.metadata.create_all(engine)
    click.echo(click.style("DB objects created", fg="green"))


@fab.command("version")
~~@with_appcontext
def version():
    """
        Flask-AppBuilder package version
    """
    click.echo(
        click.style(
            "F.A.B Version: {0}.".format(current_app.appbuilder.version),
            bg="blue",
            fg="white",
        )
    )


@fab.command("security-cleanup")
~~@with_appcontext
def security_cleanup():
    """
        Cleanup unused permissions from views and roles.
    """
    current_app.appbuilder.security_cleanup()
    click.echo(click.style("Finished security cleanup", fg="green"))


@fab.command("security-converge")
@click.option(
    "--dry-run", "-d", is_flag=True, help="Dry run & print state transitions."
)
~~@with_appcontext
def security_converge(dry_run=False):
    """
        Converges security deletes previous_class_permission_name
    """
    state_transitions = current_app.appbuilder.security_converge(dry=dry_run)
    if dry_run:
        click.echo(click.style("Computed security converge:", fg="green"))
        click.echo(click.style("Add to Roles:", fg="green"))
        for _from, _to in state_transitions["add"].items():
            click.echo(f"Where {_from} add {_to}")
        click.echo(click.style("Del from Roles:", fg="green"))
        for pvm in state_transitions["del_role_pvm"]:
            click.echo(pvm)
        click.echo(click.style("Remove views:", fg="green"))
        for views in state_transitions["del_views"]:
            click.echo(views)
        click.echo(click.style("Remove permissions:", fg="green"))
        for perms in state_transitions["del_perms"]:
            click.echo(perms)
    else:
        click.echo(click.style("Finished security converge", fg="green"))


@fab.command("create-permissions")
~~@with_appcontext
def create_permissions():
    """
        Creates all permissions and add them to the ADMIN Role.
    """
    current_app.appbuilder.add_permissions(update_perms=True)
    click.echo(click.style("Created all permissions", fg="green"))


@fab.command("list-views")
~~@with_appcontext
def list_views():
    """
        List all registered views
    """
    echo_header("List of registered views")
    for view in current_app.appbuilder.baseviews:
        click.echo(
            "View:{0} | Route:{1} | Perms:{2}".format(
                view.__class__.__name__, view.route_base, view.base_permissions
            )
        )


@fab.command("list-users")
~~@with_appcontext
def list_users():
    """
        List all users on the database
    """
    echo_header("List of users")
    for user in current_app.appbuilder.sm.get_all_users():
        click.echo(
            "username:{0} | email:{1} | role:{2}".format(
                user.username, user.email, user.roles
            )
        )


@fab.command("create-app")
@click.option(
    "--name",
    prompt="Your new app name",
    help="Your application name, directory will have this name",
)
@click.option(
    "--engine",
    prompt="Your engine type, SQLAlchemy or MongoEngine",
    type=click.Choice(["SQLAlchemy", "MongoEngine"]),
    default="SQLAlchemy",


## ... source file continues with no further with_appcontext examples...


```


## Example 2 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / cli / plugins.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/cli/plugins.py)

```python
# plugins.py
# -*- coding: utf-8 -*-
"""
    flaskbb.cli.plugins
    -------------------

    This module contains all plugin commands.

    :copyright: (c) 2016 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import sys
import os

import click
from flask import current_app
~~from flask.cli import with_appcontext

from flaskbb.extensions import db
from flaskbb.cli.main import flaskbb
from flaskbb.cli.utils import validate_plugin, get_cookiecutter
from flaskbb.plugins.models import PluginRegistry, PluginStore
from flaskbb.plugins.utils import remove_zombie_plugins_from_db


@flaskbb.group()
def plugins():
    """Plugins command sub group. If you want to run migrations or do some
    i18n stuff checkout the corresponding command sub groups."""
    pass


@plugins.command("list")
~~@with_appcontext
def list_plugins():
    """Lists all installed plugins."""
    enabled_plugins = current_app.pluggy.list_plugin_distinfo()
    if len(enabled_plugins) > 0:
        click.secho("[+] Enabled Plugins:", fg="blue", bold=True)
        for plugin in enabled_plugins:
            p_mod = plugin[0]
            p_dist = plugin[1]
            click.secho("\t- {}\t({}), version {}".format(
                current_app.pluggy.get_name(p_mod).title(), p_dist.key,
                p_dist.version), bold=True
            )

    disabled_plugins = current_app.pluggy.list_disabled_plugins()
    if len(disabled_plugins) > 0:
        click.secho("[+] Disabled Plugins:", fg="yellow", bold=True)
        for plugin in disabled_plugins:
            p_mod = plugin[0]
            p_dist = plugin[1]
            click.secho("\t- {}\t({}), version {}".format(
                p_mod.title(), p_dist.key,
                p_dist.version), bold=True
            )


@plugins.command("enable")
@click.argument("plugin_name")
~~@with_appcontext
def enable_plugin(plugin_name):
    """Enables a plugin."""
    validate_plugin(plugin_name)
    plugin = PluginRegistry.query.filter_by(name=plugin_name).first_or_404()

    if plugin.enabled:
        click.secho("Plugin '{}' is already enabled.".format(plugin.name))

    plugin.enabled = True
    plugin.save()
    click.secho("[+] Plugin '{}' enabled.".format(plugin.name), fg="green")


@plugins.command("disable")
@click.argument("plugin_name")
~~@with_appcontext
def disable_plugin(plugin_name):
    """Disables a plugin."""
    validate_plugin(plugin_name)
    plugin = PluginRegistry.query.filter_by(name=plugin_name).first_or_404()

    if not plugin.enabled:
        click.secho("Plugin '{}' is already disabled.".format(plugin.name))

    plugin.enabled = False
    plugin.save()
    click.secho("[+] Plugin '{}' disabled.".format(plugin.name), fg="green")


@plugins.command("install")
@click.argument("plugin_name")
@click.option("--force", "-f", default=False, is_flag=True,
              help="Overwrites existing settings")
def install(plugin_name, force):
    """Installs a plugin (no migrations)."""
    validate_plugin(plugin_name)
    plugin = PluginRegistry.query.filter_by(name=plugin_name).first_or_404()

    if not plugin.enabled:
        click.secho("[+] Can't install disabled plugin. "


## ... source file abbreviated to get to with_appcontext examples ...


    else:
        click.secho("[+] Nothing to install.", fg="green")


@plugins.command("uninstall")
@click.argument("plugin_name")
def uninstall(plugin_name):
    """Uninstalls a plugin (no migrations)."""
    validate_plugin(plugin_name)
    plugin = PluginRegistry.query.filter_by(name=plugin_name).first_or_404()

    if plugin.is_installed:
        PluginStore.query.filter_by(plugin_id=plugin.id).delete()
        db.session.commit()
        click.secho("[+] Plugin has been uninstalled.", fg="green")
    else:
        click.secho("[+] Nothing to uninstall.", fg="green")


@plugins.command("cleanup")
~~@with_appcontext
def cleanup():
    """Removes zombie plugins from FlaskBB.

    A zombie plugin is a plugin
    which exists in the database but isn't installed in the env anymore.
    """
    deleted_plugins = remove_zombie_plugins_from_db()
    if len(deleted_plugins) > 0:
        click.secho("[+] Removed following zombie plugins from FlaskBB: ",
                    fg="green", nl=False)
        click.secho("{}".format(", ".join(deleted_plugins)))
    else:
        click.secho("[+] No zombie plugins found.", fg="green")


@plugins.command("new")
@click.option("--template", "-t", type=click.STRING,
              default="https://github.com/sh4nks/cookiecutter-flaskbb-plugin",
              help="Path to a cookiecutter template or to a valid git repo.")
@click.option("--out-dir", "-o", type=click.Path(), default=None,
              help="The location for the new FlaskBB plugin.")
@click.option("--force", "-f", is_flag=True, default=False,
              help="Overwrite the contents of output directory if it exists")
def new_plugin(template, out_dir, force):


## ... source file continues with no further with_appcontext examples...


```

