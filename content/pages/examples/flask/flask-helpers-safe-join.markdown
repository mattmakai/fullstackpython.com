title: flask.helpers safe_join Example Code
category: page
slug: flask-helpers-safe-join-examples
sortorder: 500021021
toc: False
sidebartitle: flask.helpers safe_join
meta: Python example code that shows how to use the safe_join callable from the flask.helpers module of the Flask project.


`safe_join` is a callable within the `flask.helpers` module of the Flask project.

<a href="/flask-helpers-flash-examples.html">flash</a>,
<a href="/flask-helpers-get-root-path-examples.html">get_root_path</a>,
<a href="/flask-helpers-make-response-examples.html">make_response</a>,
<a href="/flask-helpers-send-file-examples.html">send_file</a>,
and <a href="/flask-helpers-url-for-examples.html">url_for</a>
are several other callables with code examples from the same `flask.helpers` package.

## Example 1 from CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [Flask](/flask.html). The application can be used
as-is to run CTF events, or modified for custom rules for related
scenarios. CTFd is open sourced under the
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).

[**CTFd / CTFd / __init__.py**](https://github.com/CTFd/CTFd/blob/master/./CTFd/__init__.py)

```python
# __init__.py
import datetime
import os
import sys
import weakref
from distutils.version import StrictVersion

import jinja2
from flask import Flask, Request
~~from flask.helpers import safe_join
from flask_migrate import upgrade
from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.utils import cached_property

import CTFd.utils.config
from CTFd import utils
from CTFd.constants.themes import ADMIN_THEME, DEFAULT_THEME
from CTFd.plugins import init_plugins
from CTFd.utils.crypto import sha256
from CTFd.utils.initialization import (
    init_events,
    init_logs,
    init_request_processors,
    init_template_filters,
    init_template_globals,
)
from CTFd.utils.migrations import create_database, migrations, stamp_latest_revision
from CTFd.utils.sessions import CachingSessionInterface
from CTFd.utils.updates import update_check

__version__ = "3.4.0"
__channel__ = "oss"


## ... source file abbreviated to get to safe_join examples ...


            self.cache[cache_key] = template
        return template


class ThemeLoader(FileSystemLoader):

    DEFAULT_THEMES_PATH = os.path.join(os.path.dirname(__file__), "themes")
    _ADMIN_THEME_PREFIX = ADMIN_THEME + "/"

    def __init__(
        self,
        searchpath=DEFAULT_THEMES_PATH,
        theme_name=None,
        encoding="utf-8",
        followlinks=False,
    ):
        super(ThemeLoader, self).__init__(searchpath, encoding, followlinks)
        self.theme_name = theme_name

    def get_source(self, environment, template):
        if template.startswith(self._ADMIN_THEME_PREFIX):
            if self.theme_name != ADMIN_THEME:
                raise jinja2.TemplateNotFound(template)
            template = template[len(self._ADMIN_THEME_PREFIX) :]
        theme_name = self.theme_name or str(utils.get_config("ctf_theme"))
~~        template = safe_join(theme_name, "templates", template)
        return super(ThemeLoader, self).get_source(environment, template)


def confirm_upgrade():
    if sys.stdin.isatty():
        print("/*\\ CTFd has updated and must update the database! /*\\")
        print("/*\\ Please backup your database before proceeding! /*\\")
        print("/*\\ CTFd maintainers are not responsible for any data loss! /*\\")
        if input("Run database migrations (Y/N)").lower().strip() == "y":  # nosec B322
            return True
        else:
            print("/*\\ Ignored database migrations... /*\\")
            return False
    else:
        return True


def run_upgrade():
    upgrade()
    utils.set_config("ctf_version", __version__)


def create_app(config="CTFd.config.Config"):
    app = CTFdFlask(__name__)


## ... source file continues with no further safe_join examples...

```

