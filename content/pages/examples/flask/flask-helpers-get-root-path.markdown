title: flask.helpers get_root_path Example Code
category: page
slug: flask-helpers-get-root-path-examples
sortorder: 500021019
toc: False
sidebartitle: flask.helpers get_root_path
meta: Python example code that shows how to use the get_root_path callable from the flask.helpers module of the Flask project.


[get_root_path](https://github.com/pallets/flask/blob/master/src/flask/helpers.py)
is a function within the `flask.helpers` module of the [Flask](/flask.html)
framework. `get_root_path` returns the filesystem path to a package
or the current working directly if the path cannot be found.

<a href="/flask-helpers-flash-examples.html">flash</a>,
<a href="/flask-helpers-make-response-examples.html">make_response</a>,
<a href="/flask-helpers-safe-join-examples.html">safe_join</a>,
<a href="/flask-helpers-send-file-examples.html">send_file</a>,
and <a href="/flask-helpers-url-for-examples.html">url_for</a>
are several other callables with code examples from the same `flask.helpers` package.

## Example 1 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / cli / setup.py**](https://github.com/indico/indico/blob/master/indico/cli/setup.py)

```python
# setup.py

from __future__ import unicode_literals

import os
import re
import shutil
import socket
import sys
from operator import attrgetter
from smtplib import SMTP

import click
from click import wrap_text
~~from flask.helpers import get_root_path
from pkg_resources import iter_entry_points
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import PathCompleter, WordCompleter
from prompt_toolkit.layout.lexers import SimpleLexer
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token
from pytz import all_timezones, common_timezones
from redis import RedisError, StrictRedis
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import NullPool
from terminaltables import AsciiTable
from werkzeug.urls import url_parse

from indico.core.db.sqlalchemy.util.models import import_all_models
from indico.util.console import cformat
from indico.util.string import validate_email


click.disable_unicode_literals_warning = True


def _echo(msg=''):
    click.echo(msg, err=True)


## ... source file abbreviated to get to get_root_path examples ...



def _prompt_abort():
    _confirm('Continue anyway?', abort=True)


def _copy(src, dst, force=False):
    if not force and os.path.exists(dst):
        _echo(cformat('%{yellow!}{}%{reset}%{yellow} already exists; not copying %{yellow!}{}')
              .format(dst, src))
        return
    _echo(cformat('%{green}Copying %{green!}{}%{reset}%{green} -> %{green!}{}').format(src, dst))
    shutil.copy(src, dst)


def _link(src, dst):
    _echo(cformat('%{cyan}Linking %{cyan!}{}%{reset}%{cyan} -> %{cyan!}{}').format(dst, src))
    if os.path.exists(dst) or os.path.islink(dst):
        os.unlink(dst)
    os.symlink(src, dst)


def _get_dirs(target_dir):
    if not os.path.isdir(target_dir):
        _echo(cformat('%{red}Directory not found:%{red!} {}').format(target_dir))
        sys.exit(1)
~~    return get_root_path('indico'), os.path.abspath(target_dir)


PROMPT_TOOLKIT_STYLE = style_from_dict({
    Token.HELP: '#aaaaaa',
    Token.PROMPT: '#5f87ff',
    Token.DEFAULT: '#dfafff',
    Token.BRACKET: '#ffffff',
    Token.COLON: '#ffffff',
    Token.INPUT: '#aaffaa',
})


def _prompt(message, default='', path=False, list_=None, required=True, validate=None, allow_invalid=False,
            password=False, help=None):
    def _get_prompt_tokens(cli):
        rv = [
            (Token.PROMPT, message),
            (Token.COLON, ': '),
        ]
        if first and help:
            rv.insert(0, (Token.HELP, wrap_text(help) + '\n'))
        return rv

    completer = None


## ... source file abbreviated to get to get_root_path examples ...



        if dev:
            config_data += [
                b'',
                b'# Development options',
                b'DB_LOG = True',
                b'DEBUG = True',
                b'SMTP_USE_CELERY = False'
            ]

        config = b'\n'.join(x for x in config_data if x is not None)

        if dev:
            if not os.path.exists(self.data_root_path):
                os.mkdir(self.data_root_path)

        _echo()
        for path in self._missing_dirs:
            _echo(cformat('%{magenta}Creating %{magenta!}{}%{reset}%{magenta}').format(path))
            os.mkdir(path)

        _echo(cformat('%{magenta}Creating %{magenta!}{}%{reset}%{magenta}').format(self.config_path))
        with open(self.config_path, 'wb') as f:
            f.write(config + b'\n')

~~        package_root = get_root_path('indico')
        _copy(os.path.normpath(os.path.join(package_root, 'logging.yaml.sample')),
              os.path.join(self.config_dir_path, 'logging.yaml'))

        if not dev:
            _link(os.path.join(package_root, 'web', 'static'), os.path.join(self.data_root_path, 'web', 'static'))
            _copy(os.path.join(package_root, 'web', 'indico.wsgi'),
                  os.path.join(self.data_root_path, 'web', 'indico.wsgi'),
                  force=True)

        if create_config_link:
            _link(self.config_path, config_link_path)

        _echo()
        _echo(cformat('%{green}Indico has been configured successfully!'))
        if not dev and not create_config_link:
            _echo(cformat('Run %{green!}export INDICO_CONFIG={}%{reset} to use your config file')
                  .format(self.config_path))

        if self.old_archive_dir:
            _echo(cformat('Check %{green!}https://git.io/vHP6o%{reset} for a guide on how to '
                          'import data from Indico v1.2'))
        else:
            _echo(cformat('You can now run %{green!}indico db prepare%{reset} to initialize your Indico database'))



## ... source file continues with no further get_root_path examples...

```

