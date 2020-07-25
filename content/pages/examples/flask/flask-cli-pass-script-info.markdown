title: flask.cli pass_script_info Example Code
category: page
slug: flask-cli-pass-script-info-examples
sortorder: 500021009
toc: False
sidebartitle: flask.cli pass_script_info
meta: Python example code that shows how to use the pass_script_info callable from the flask.cli module of the Flask project.


[pass_script_info](https://github.com/pallets/flask/blob/master/src/flask/cli.py)
is simply a decorator around the [ScriptInfo](/flask-cli-scriptinfo-examples.html)
class within this same `flask.cli` module.

<a href="/flask-cli-appgroup-examples.html">AppGroup</a>,
<a href="/flask-cli-dispatchingapp-examples.html">DispatchingApp</a>,
<a href="/flask-cli-flaskgroup-examples.html">FlaskGroup</a>,
<a href="/flask-cli-scriptinfo-examples.html">ScriptInfo</a>,
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

[**indico / indico / cli / core.py**](https://github.com/indico/indico/blob/master/indico/cli/core.py)

```python
# core.py

from __future__ import unicode_literals

import click
~~from flask.cli import AppGroup, pass_script_info

from indico.cli.util import IndicoFlaskGroup, LazyGroup


click.disable_unicode_literals_warning = True
__all__ = ('cli_command', 'cli_group')


_cli = AppGroup()
cli_command = _cli.command
cli_group = _cli.group
del _cli


def _get_indico_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    import indico
    message = 'Indico v{}'.format(indico.__version__)
    click.echo(message, ctx.color)
    ctx.exit()


@click.group(cls=IndicoFlaskGroup)


## ... source file abbreviated to get to pass_script_info examples ...


@click.option('--min-age', type=click.IntRange(1), default=1, metavar='N',
              help='Delete files at least N days old (default: 1)')
def cleanup(temp, cache, verbose, dry_run, min_age):
    from .cleanup import cleanup_cmd
    if not temp and not cache:
        raise click.UsageError('You need to specify what to delete')
    cleanup_cmd(temp, cache, min_age=min_age, dry_run=dry_run, verbose=(verbose or dry_run))


@cli.command(with_appcontext=False)
@click.option('--host', '-h', default='127.0.0.1', metavar='HOST', help='The ip/host to bind to.')
@click.option('--port', '-p', default=None, type=int, metavar='PORT', help='The port to bind to.')
@click.option('--url', '-u', default=None, metavar='URL',
              help='The URL used to access indico. Defaults to `http(s)://host:port`')
@click.option('--ssl', '-s', is_flag=True, help='Use SSL.')
@click.option('--ssl-key', '-K', type=click.Path(exists=True, dir_okay=False), help='The SSL private key to use.')
@click.option('--ssl-cert', '-C', type=click.Path(exists=True, dir_okay=False), help='The SSL cert key to use.')
@click.option('--quiet', '-q', is_flag=True, help='Disable logging of requests for most static files.')
@click.option('--enable-evalex', is_flag=True,
              help="Enable the werkzeug debugger's python shell in tracebacks and via /console")
@click.option('--evalex-from', multiple=True,
              help='Restrict the debugger shell to the given ips (can be used multiple times)')
@click.option('--proxy', is_flag=True, help='Use the ip and protocol provided by the proxy.')
@click.option('--reloader', 'reloader_type', type=click.Choice(['auto', 'none', 'stat', 'watchdog', 'watchman']),
              default='auto', help='The type of auto-reloader to use.')
~~@pass_script_info
def run(info, **kwargs):
    from indico.cli.devserver import run_cmd
    if bool(kwargs['ssl_key']) != bool(kwargs['ssl_cert']):
        raise click.BadParameter('ssl-key and ssl-cert must be used together')
    run_cmd(info, **kwargs)


@cli.command(short_help='Run a shell in the app context.')
@click.option('-v', '--verbose', is_flag=True, help='Show verbose information on the available objects')
@click.option('-r', '--request-context', is_flag=True, help='Run the shell inside a Flask request context')
def shell(verbose, request_context):
    from .shell import shell_cmd
    shell_cmd(verbose, request_context)



## ... source file continues with no further pass_script_info examples...

```

