title: flask.helpers send_file Example Code
category: page
slug: flask-helpers-send-file-examples
sortorder: 500021022
toc: False
sidebartitle: flask.helpers send_file
meta: Python example code that shows how to use the send_file callable from the flask.helpers module of the Flask project.


[send_file](https://github.com/pallets/flask/blob/master/src/flask/helpers.py)
is function in the [Flask](/flask.html) `flask.helpers` module.
`send_file` transfers the contents of a file to the client using the most
efficient method available and configured in the Flask settings. It
attempts to guess the correct mimetype to use but it can also be
explicitly configured.

Note that `send_file` is usually imported directly from `flask` instead of
from `flask.helpers`, even though it is defined within the `helpers` module.
It's the same function that is imported, but it's less characters to type
when you leave off the `.helpers` part.

<a href="/flask-helpers-flash-examples.html">flash</a>,
<a href="/flask-helpers-get-root-path-examples.html">get_root_path</a>,
<a href="/flask-helpers-make-response-examples.html">make_response</a>,
<a href="/flask-helpers-safe-join-examples.html">safe_join</a>,
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

[**CTFd / CTFd / views.py**](https://github.com/CTFd/CTFd/blob/master/./CTFd/views.py)

```python
# views.py
import os

from flask import Blueprint, abort
from flask import current_app as app
~~from flask import redirect, render_template, request, send_file, session, url_for
from flask.helpers import safe_join
from sqlalchemy.exc import IntegrityError

from CTFd.cache import cache
from CTFd.constants.config import (
    AccountVisibilityTypes,
    ChallengeVisibilityTypes,
    ConfigTypes,
    RegistrationVisibilityTypes,
    ScoreVisibilityTypes,
)
from CTFd.models import (
    Admins,
    Files,
    Notifications,
    Pages,
    Teams,
    Users,
    UserTokens,
    db,
)
from CTFd.utils import config, get_config, set_config
from CTFd.utils import user as current_user
from CTFd.utils import validators


## ... source file abbreviated to get to send_file examples ...


                    abort(403)

                if team:
                    if team.banned:
                        abort(403)
                else:
                    pass

                if file_id != f.id:
                    abort(403)

            except (BadTimeSignature, SignatureExpired, BadSignature):
                abort(403)

    uploader = get_uploader()
    try:
        return uploader.download(f.location)
    except IOError:
        abort(404)


@views.route("/themes/<theme>/static/<path:path>")
def themes(theme, path):
    filename = safe_join(app.root_path, "themes", theme, "static", path)
    if os.path.isfile(filename):
~~        return send_file(filename)
    else:
        abort(404)



## ... source file continues with no further send_file examples...

```


## Example 2 from Flask-VueJs-Template
[Flask-VueJs-Template](https://github.com/gtalarico/flask-vuejs-template)
([demo site](https://flask-vuejs-template.herokuapp.com/))
is a minimal [Flask](/flask.html) boilerplate starter project that
combines Flask, [Vue.js](https://www.fullstackpython.com/vuejs.html),
and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).
The project provides some sensible defaults that are easy to continue
building on, and the source code is open source under the
[MIT license](https://github.com/gtalarico/flask-vuejs-template/blob/master/LICENSE.md).

[**Flask-VueJs-Template / app / __init__.py**](https://github.com/gtalarico/flask-vuejs-template/blob/master/app/./__init__.py)

```python
# __init__.py
import os
~~from flask import Flask, current_app, send_file

from .api import api_bp
from .client import client_bp

app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
~~    return send_file(entry)





## ... source file continues with no further send_file examples...

```

