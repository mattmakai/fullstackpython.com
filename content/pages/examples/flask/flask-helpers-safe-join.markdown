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

[**CTFd / CTFd / views.py**](https://github.com/CTFd/CTFd/blob/master/./CTFd/views.py)

```python
# views.py
import os

from flask import Blueprint, abort
from flask import current_app as app
from flask import redirect, render_template, request, send_file, session, url_for
~~from flask.helpers import safe_join
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
from CTFd.utils.config import is_setup


## ... source file abbreviated to get to safe_join examples ...


                        abort(403)
                else:
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
~~    filename = safe_join(app.root_path, "themes", theme, "static", path)
    if os.path.isfile(filename):
        return send_file(filename)
    else:
        abort(404)



## ... source file continues with no further safe_join examples...

```

