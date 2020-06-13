title: flask.cli FlaskGroup code examples
category: page
slug: flask-cli-flaskgroup-examples
sortorder: 500021001
toc: False
sidebartitle: flask.cli FlaskGroup
meta: Python example code for the FlaskGroup class from the flask.cli module of the Flask project.


FlaskGroup is a class within the flask.cli module of the Flask project.


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


~~class FlaskBBGroup(FlaskGroup):
    def __init__(self, *args, **kwargs):
        super(FlaskBBGroup, self).__init__(*args, **kwargs)
        self._loaded_flaskbb_plugins = False

    def _load_flaskbb_plugins(self, ctx):
        if self._loaded_flaskbb_plugins:
            return

        try:
            app = ctx.ensure_object(ScriptInfo).load_app()
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


## ... source file continues with no further FlaskGroup examples...


```

