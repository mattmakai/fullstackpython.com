title: flask request Example Python Code
category: page
slug: flask-request-examples
sortorder: 500021010
toc: False
sidebartitle: flask request
meta: Python code examples for the request object from the Flask project used for building web applications.


The [Flask](/flask.html)
[request](https://flask.palletsprojects.com/en/1.1.x/reqcontext/)
([source code](https://github.com/pallets/flask/blob/master/src/flask/globals.py))
object is critical for [building web applications](/web-development.html)
with this [web framework](/web-framework.html). The request context
allows you to obtain data sent from the client such as a web browser 
so that you can appropriately handle generating the response.


## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or 
[Markdown](/markdown.html). FlaskBB is provided as open source 
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**flaskbb / flaskbb / app.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/app.py)

```python
# -*- coding: utf-8 -*-
"""
    flaskbb.app
    -----------
    manages the app creation and configuration process
    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import logging
import logging.config
import os
import sys
import time
import warnings
from datetime import datetime

~~from flask import Flask, request
from flask_login import current_user
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError, ProgrammingError


## ... code abbreviated here due to several hundred non-relevant lines ...


def configure_before_handlers(app):
    """Configures the before request handlers."""

~~    @app.before_request
    def update_lastseen():
        """Updates `lastseen` before every reguest if the user is
        authenticated."""
        if current_user.is_authenticated:
            current_user.lastseen = time_utcnow()
            db.session.add(current_user)
            db.session.commit()

    if app.config["REDIS_ENABLED"]:

~~        @app.before_request
        def mark_current_user_online():
            if current_user.is_authenticated:
                mark_online(current_user.username)
            else:
~~                mark_online(request.remote_addr, guest=True)

    app.pluggy.hook.flaskbb_request_processors(app=app)
```
