title: flask.cli with_appcontext Example Code
category: page
slug: flask-cli-with-appcontext-examples
sortorder: 500021010
toc: False
sidebartitle: flask.cli with_appcontext
meta: Python example code that shows how to use the with_appcontext callable from the flask.cli module of the Flask project.


[with_appcontext](https://github.com/pallets/flask/blob/master/src/flask/cli.py)
is a [Flask](/flask.html) decorator in the `flask.cli` module that
wraps a callback to guarantee it will be called with a script's
application context. Any callbacks registered with `app.cli` are
wrapped with this function by default.

<a href="/flask-cli-appgroup-examples.html">AppGroup</a>,
<a href="/flask-cli-dispatchingapp-examples.html">DispatchingApp</a>,
<a href="/flask-cli-flaskgroup-examples.html">FlaskGroup</a>,
<a href="/flask-cli-scriptinfo-examples.html">ScriptInfo</a>,
and <a href="/flask-cli-pass-script-info-examples.html">pass_script_info</a>
are several other callables with code examples from the same `flask.cli` package.

## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / cli / main.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/cli/main.py)

```python
# main.py
import binascii
import logging
import os
import sys
import time
import traceback
from datetime import datetime

import click
import click_log
from celery.bin.celery import CeleryCommand
from flask import current_app
~~from flask.cli import FlaskGroup, ScriptInfo, with_appcontext
from flask_alembic import alembic_click
from jinja2 import Environment, FileSystemLoader
from sqlalchemy_utils.functions import database_exists
from werkzeug.utils import import_string

from flaskbb import create_app
from flaskbb.cli.utils import (EmailType, FlaskBBCLIError, get_version,
                               prompt_config_path, prompt_save_user,
                               write_config)
from flaskbb.extensions import alembic, celery, db, whooshee
from flaskbb.utils.populate import (create_default_groups,
                                    create_default_settings, create_latest_db,
                                    create_test_data, create_welcome_forum,
                                    insert_bulk_data, run_plugin_migrations,
                                    update_settings_from_fixture)
from flaskbb.utils.translations import compile_translations


logger = logging.getLogger(__name__)
click_log.basic_config(logger)


class FlaskBBGroup(FlaskGroup):
    def __init__(self, *args, **kwargs):


## ... source file abbreviated to get to with_appcontext examples ...


                   "'instance' next to the package or module is assumed to "
                   "be the instance path.")
@click.option("--version", expose_value=False, callback=get_version,
              is_flag=True, is_eager=True, help="Show the FlaskBB version.")
@click.pass_context
@click_log.simple_verbosity_option(logger)
def flaskbb(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


flaskbb.add_command(alembic_click, "db")


@flaskbb.command()
@click.option("--welcome", "-w", default=True, is_flag=True,
              help="Disable the welcome forum.")
@click.option("--force", "-f", default=False, is_flag=True,
              help="Doesn't ask for confirmation.")
@click.option("--username", "-u", help="The username of the user.")
@click.option("--email", "-e", type=EmailType(),
              help="The email address of the user.")
@click.option("--password", "-p", help="The password of the user.")
@click.option("--no-plugins", "-n", default=False, is_flag=True,
              help="Don't run the migrations for the default plugins.")
~~@with_appcontext
def install(welcome, force, username, email, password, no_plugins):
    click.secho("[+] Installing FlaskBB...", fg="cyan")
    if database_exists(db.engine.url):
        if force or click.confirm(click.style(
            "Existing database found. Do you want to delete the old one and "
            "create a new one?", fg="magenta")
        ):
            db.drop_all()
        else:
            sys.exit(0)

    create_latest_db()

    click.secho("[+] Creating default settings...", fg="cyan")
    create_default_groups()
    create_default_settings()

    click.secho("[+] Creating admin user...", fg="cyan")
    prompt_save_user(username, email, password, "admin")

    if welcome:
        click.secho("[+] Creating welcome forum...", fg="cyan")
        create_welcome_forum()



## ... source file abbreviated to get to with_appcontext examples ...



    if fixture or all_latest:
        try:
            settings = import_string(
                "flaskbb.fixtures.{}".format(fixture)
            )
            settings = settings.fixture
        except ImportError:
            raise FlaskBBCLIError("{} fixture is not available"
                                  .format(fixture), fg="red")

        click.secho("[+] Updating fixtures...", fg="cyan")
        count = update_settings_from_fixture(
            fixture=settings, overwrite_group=force, overwrite_setting=force
        )
        click.secho("[+] {settings} settings in {groups} setting groups "
                    "updated.".format(groups=len(count), settings=sum(
                        len(settings) for settings in count.values())
                    ), fg="green")


@flaskbb.command("celery", add_help_option=False,
                 context_settings={"ignore_unknown_options": True,
                                   "allow_extra_args": True})
@click.pass_context
~~@with_appcontext
def start_celery(ctx):
    CeleryCommand(celery).execute_from_commandline(
        ["flaskbb celery"] + ctx.args
    )


@flaskbb.command("shell", short_help="Runs a shell in the app context.")
~~@with_appcontext
def shell_command():
    import code
    banner = "Python %s on %s\nInstance Path: %s" % (
        sys.version,
        sys.platform,
        current_app.instance_path,
    )
    ctx = {"db": db}

    startup = os.environ.get("PYTHONSTARTUP")
    if startup and os.path.isfile(startup):
        with open(startup, "r") as f:
            eval(compile(f.read(), startup, "exec"), ctx)

    ctx.update(current_app.make_shell_context())

    try:
        import IPython
        IPython.embed(banner1=banner, user_ns=ctx)
    except ImportError:
        code.interact(banner=banner, local=ctx)


@flaskbb.command("urls", short_help="Show routes for the app.")
@click.option("--route", "-r", "order_by", flag_value="rule", default=True,
              help="Order by route")
@click.option("--endpoint", "-e", "order_by", flag_value="endpoint",
              help="Order by endpoint")
@click.option("--methods", "-m", "order_by", flag_value="methods",
              help="Order by methods")
~~@with_appcontext
def list_urls(order_by):
    from flask import current_app

    rules = sorted(
        current_app.url_map.iter_rules(),
        key=lambda rule: getattr(rule, order_by)
    )

    max_rule_len = max(len(rule.rule) for rule in rules)
    max_rule_len = max(max_rule_len, len("Route"))

    max_endpoint_len = max(len(rule.endpoint) for rule in rules)
    max_endpoint_len = max(max_endpoint_len, len("Endpoint"))

    max_method_len = max(len(", ".join(rule.methods)) for rule in rules)
    max_method_len = max(max_method_len, len("Methods"))

    column_header_len = max_rule_len + max_endpoint_len + max_method_len + 4
    column_template = "{:<%s}  {:<%s}  {:<%s}" % (
        max_rule_len, max_endpoint_len, max_method_len
    )

    click.secho(column_template.format("Route", "Endpoint", "Methods"),
                fg="blue", bold=True)


## ... source file continues with no further with_appcontext examples...

```

