title: flask.cli FlaskGroup Example Code
category: page
slug: flask-cli-flaskgroup-examples
sortorder: 500021007
toc: False
sidebartitle: flask.cli FlaskGroup
meta: Example code for understanding how to use the FlaskGroup class from the flask.cli module of the Flask project.


[FlaskGroup](https://github.com/pallets/flask/blob/master/src/flask/cli.py)
is a class within the `flask.cli` module of the [Flask project](/flask.html).
FlaskGroup is a subclass of [AppGroup](/flask-cli-appgroup-examples.html)
that provides for loading more commands from a configured Flask app.
Generally, only advanced use cases will need to use this class.

<a href="/flask-cli-appgroup-examples.html">AppGroup</a>,
<a href="/flask-cli-dispatchingapp-examples.html">DispatchingApp</a>,
<a href="/flask-cli-scriptinfo-examples.html">ScriptInfo</a>,
<a href="/flask-cli-pass-script-info-examples.html">pass_script_info</a>,
and <a href="/flask-cli-with-appcontext-examples.html">with_appcontext</a>
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


## Example 2 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / cli / util.py**](https://github.com/indico/indico/blob/master/indico/cli/util.py)

```python
# util.py

from __future__ import unicode_literals

import traceback
from importlib import import_module

import click
~~from flask.cli import AppGroup, FlaskGroup, ScriptInfo
from flask_pluginengine import wrap_in_plugin_context
from werkzeug.utils import cached_property




def _create_app(info):
    from indico.web.flask.app import make_app
    return make_app(set_path=True)


~~class IndicoFlaskGroup(FlaskGroup):

    def __init__(self, **extra):
        super(IndicoFlaskGroup, self).__init__(create_app=_create_app, add_default_commands=False,
                                               add_version_option=False, set_debug_flag=False, **extra)
        self._indico_plugin_commands = None

    def _load_plugin_commands(self):
        assert False

    def _wrap_in_plugin_context(self, plugin, cmd):
        cmd.callback = wrap_in_plugin_context(plugin, cmd.callback)
        for subcmd in getattr(cmd, 'commands', {}).viewvalues():
            self._wrap_in_plugin_context(plugin, subcmd)

    def _get_indico_plugin_commands(self, ctx):
        if self._indico_plugin_commands is not None:
            return self._indico_plugin_commands
        try:
            from indico.core import signals
            from indico.util.signals import named_objects_from_signal
            ctx.ensure_object(ScriptInfo).load_app()
            cmds = named_objects_from_signal(signals.plugin.cli.send(), plugin_attr='_indico_plugin')
            rv = {}
            for name, cmd in cmds.viewitems():


## ... source file continues with no further FlaskGroup examples...

```

