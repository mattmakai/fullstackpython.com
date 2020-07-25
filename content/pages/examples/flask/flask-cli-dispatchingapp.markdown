title: flask.cli DispatchingApp Example Code
category: page
slug: flask-cli-dispatchingapp-examples
sortorder: 500021006
toc: False
sidebartitle: flask.cli DispatchingApp
meta: Example code for understanding how to use the DispatchingApp class from the flask.cli module of the Flask project.


[DispatchingApp](https://github.com/pallets/flask/blob/master/src/flask/cli.py)
is a class within the `flask.cli` module of the [Flask](/flask.html) project.
DispatchingApp is a special application that dispatches to a Flask app
if it is imported by name in a background thread.

<a href="/flask-cli-appgroup-examples.html">AppGroup</a>,
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

[**indico / indico / cli / devserver.py**](https://github.com/indico/indico/blob/master/indico/cli/devserver.py)

```python
# devserver.py

from __future__ import print_function, unicode_literals

import os

~~from flask.cli import DispatchingApp
from werkzeug.debug import DebuggedApplication
from werkzeug.exceptions import NotFound
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.serving import WSGIRequestHandler, run_simple
from werkzeug.urls import url_parse


try:
    import pywatchman
except ImportError:
    pywatchman = None


def run_cmd(info, **kwargs):
    if kwargs['reloader_type'] == 'watchman':
        if pywatchman is None:
            print('watchman is not available - you need to `pip install pywatchman`')
            return
        run_watchman()
        return
    run_server(info, **kwargs)




## ... source file abbreviated to get to DispatchingApp examples ...



    import logging
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.propagate = False
    werkzeug_logger.setLevel(logging.INFO)
    werkzeug_logger.addHandler(logging.StreamHandler())

    app = _make_wsgi_app(info, url, evalex_whitelist, proxy)
    run_simple(host, port, app,
               reloader_type=reloader_type, use_reloader=(reloader_type != 'none'),
               use_debugger=False, use_evalex=False, threaded=True, ssl_context=ssl_ctx,
               extra_files=extra_files, request_handler=QuietWSGIRequestHandler if quiet else None)


def _reset_state():
    from indico.core.celery import celery
    celery.flask_app = None


def _make_wsgi_app(info, url, evalex_whitelist, proxy):
    def _load_app():
        _reset_state()
        return info.load_app()

    url_data = url_parse(url)
~~    app = DispatchingApp(_load_app)
    app = DebuggedIndico(app, evalex_whitelist)
    app = _make_indico_dispatcher(app, url_data.path)
    if proxy:
        app = ProxyFix(app, x_for=1, x_proto=1, x_host=1)
    QuietWSGIRequestHandler.INDICO_URL_PREFIX = url_data.path.rstrip('/')
    return app


def _make_indico_dispatcher(wsgi_app, path):
    path = path.rstrip('/')
    if not path:
        return wsgi_app
    else:
        return DispatcherMiddleware(NotFound(), {
            path: wsgi_app
        })


class DebuggedIndico(DebuggedApplication):
    def __init__(self, *args, **kwargs):
        self._evalex_whitelist = None
        self._request_ip = None
        super(DebuggedIndico, self).__init__(*args, **kwargs)



## ... source file continues with no further DispatchingApp examples...

```

