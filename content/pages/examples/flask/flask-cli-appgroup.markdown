title: flask.cli AppGroup Example Code
category: page
slug: flask-cli-appgroup-examples
sortorder: 500021005
toc: False
sidebartitle: flask.cli AppGroup
meta: Example code for understanding how to use the AppGroup class from the flask.cli module of the Flask project.


[AppGroup](https://github.com/pallets/flask/blob/master/src/flask/cli.py)
is a class within the `flask.cli` module of the Flask project. It
works like the
[Click Group](https://click.palletsprojects.com/en/7.x/commands/)
class and automatically wraps the functions using
[with_appcontext](/flask-cli-with-appcontext-examples.html).

<a href="/flask-cli-dispatchingapp-examples.html">DispatchingApp</a>,
<a href="/flask-cli-flaskgroup-examples.html">FlaskGroup</a>,
<a href="/flask-cli-scriptinfo-examples.html">ScriptInfo</a>,
<a href="/flask-cli-pass-script-info-examples.html">pass_script_info</a>,
and <a href="/flask-cli-with-appcontext-examples.html">with_appcontext</a>
are several other callables with code examples from the same `flask.cli` package.

## Example 1 from indico
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


class IndicoFlaskGroup(FlaskGroup):

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
                if cmd._indico_plugin:
                    self._wrap_in_plugin_context(cmd._indico_plugin, cmd)
                rv[name] = cmd
        except Exception as exc:
            if 'No indico config found' not in unicode(exc):
                click.echo(click.style('Loading plugin commands failed:', fg='red', bold=True))
                click.echo(click.style(traceback.format_exc(), fg='red'))
            rv = {}
        self._indico_plugin_commands = rv
        return rv

    def get_command(self, ctx, name):
~~        rv = AppGroup.get_command(self, ctx, name)
        if rv is not None:
            return rv
        return self._get_indico_plugin_commands(ctx).get(name)

    def list_commands(self, ctx):
        rv = set(click.Group.list_commands(self, ctx))
        rv.update(self._get_indico_plugin_commands(ctx))
        return sorted(rv)


class LazyGroup(click.Group):

    def __init__(self, import_name, **kwargs):
        self._import_name = import_name
        super(LazyGroup, self).__init__(**kwargs)

    @cached_property
    def _impl(self):
        module, name = self._import_name.split(':', 1)
        return getattr(import_module(module), name)

    def get_command(self, ctx, cmd_name):
        return self._impl.get_command(ctx, cmd_name)



## ... source file continues with no further AppGroup examples...

```

