title: flask.cli ScriptInfo Python code examples
category: page
slug: flask-cli-scriptinfo-examples
sortorder: 500021001
toc: False
sidebartitle: flask.cli ScriptInfo
meta: Python example code for the ScriptInfo class from the flask.cli module of the Flask project.


ScriptInfo is a class within the flask.cli module of the Flask project.


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
    flaskbb.cli.commands
    --------------------

    This module contains the main commands.

    :copyright: (c) 2016 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
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
        super(FlaskBBGroup, self).__init__(*args, **kwargs)
        self._loaded_flaskbb_plugins = False

    def _load_flaskbb_plugins(self, ctx):
        if self._loaded_flaskbb_plugins:
            return

        try:
~~            app = ctx.ensure_object(ScriptInfo).load_app()
            app.pluggy.hook.flaskbb_cli(cli=self, app=app)
            self._loaded_flaskbb_plugins = True
        except Exception:
            logger.error(
                "Error while loading CLI Plugins",
                exc_info=traceback.format_exc()
            )
        else:
            shell_context_processors = app.pluggy.hook.flaskbb_shell_context()
            for p in shell_context_processors:
                app.shell_context_processor(p)

    def get_command(self, ctx, name):
        self._load_flaskbb_plugins(ctx)
        return super(FlaskBBGroup, self).get_command(ctx, name)

    def list_commands(self, ctx):
        self._load_flaskbb_plugins(ctx)
        return super(FlaskBBGroup, self).list_commands(ctx)


def make_app(script_info):
    config_file = getattr(script_info, "config_file", None)
    instance_path = getattr(script_info, "instance_path", None)
    return create_app(config_file, instance_path)


def set_config(ctx, param, value):
    """This will pass the config file to the create_app function."""
~~    ctx.ensure_object(ScriptInfo).config_file = value


def set_instance(ctx, param, value):
    """This will pass the instance path on the script info which can then
    be used in 'make_app'."""
    ctx.ensure_object(ScriptInfo).instance_path = value


@click.group(cls=FlaskBBGroup, create_app=make_app, add_version_option=False,
             invoke_without_command=True)
@click.option("--config", expose_value=False, callback=set_config,
              required=False, is_flag=False, is_eager=True, metavar="CONFIG",
              help="Specify the config to use either in dotted module "
                   "notation e.g. 'flaskbb.configs.default.DefaultConfig' "
                   "or by using a path like '/path/to/flaskbb.cfg'")
@click.option("--instance", expose_value=False, callback=set_instance,
              required=False, is_flag=False, is_eager=True, metavar="PATH",
              help="Specify the instance path to use. By default the folder "
                   "'instance' next to the package or module is assumed to "
                   "be the instance path.")
@click.option("--version", expose_value=False, callback=get_version,
              is_flag=True, is_eager=True, help="Show the FlaskBB version.")
@click.pass_context
@click_log.simple_verbosity_option(logger)


## ... source file continues with no further ScriptInfo examples...


```

