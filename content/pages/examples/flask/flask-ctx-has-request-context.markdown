title: flask.ctx has_request_context code examples
category: page
slug: flask-ctx-has-request-context-examples
sortorder: 500021005
toc: False
sidebartitle: flask.ctx has_request_context
meta: Python example code for the has_request_context function from the flask.ctx module of the Flask project.


has_request_context is a function within the flask.ctx module of the Flask project.


## Example 1 from Flask AppBuilder
[Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder)
([documentation](https://flask-appbuilder.readthedocs.io/en/latest/)
and
[example apps](https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples))
is a web application generator that uses Flask to automatically create
the code for database-driven applications based on parameters set
by the user. The generated applications include default security settings,
forms, and internationalization support.

Flask App Builder is provided under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/LICENSE).

[**Flask AppBuilder / flask_appbuilder / babel / manager.py**](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/babel/manager.py)

```python
# manager.py
import os

~~from flask import has_request_context, request, session
from flask_babel import Babel

from .views import LocaleView
from ..basemanager import BaseManager


class BabelManager(BaseManager):

    babel = None
    locale_view = None

    def __init__(self, appbuilder):
        super(BabelManager, self).__init__(appbuilder)
        app = appbuilder.get_app
        app.config.setdefault("BABEL_DEFAULT_LOCALE", "en")
        if not app.config.get("LANGUAGES"):
            app.config["LANGUAGES"] = {"en": {"flag": "us", "name": "English"}}
        appbuilder_parent_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), os.pardir
        )
        appbuilder_translations_path = os.path.join(
            appbuilder_parent_dir, "translations"
        )
        if "BABEL_TRANSLATION_DIRECTORIES" in app.config:


## ... source file abbreviated to get to has_request_context examples ...


            )
        else:
            translations_path = appbuilder_translations_path + ";translations"
        app.config["BABEL_TRANSLATION_DIRECTORIES"] = translations_path
        self.babel = Babel(app)
        self.babel.locale_selector_func = self.get_locale

    def register_views(self):
        self.locale_view = LocaleView()
        self.appbuilder.add_view_no_menu(self.locale_view)

    @property
    def babel_default_locale(self):
        return self.appbuilder.get_app.config["BABEL_DEFAULT_LOCALE"]

    @property
    def languages(self):
        return self.appbuilder.get_app.config["LANGUAGES"]

    def get_locale(self):
~~        if has_request_context():
            # locale selector for API searches for request args
            for arg, value in request.args.items():
                if arg == "_l_":
                    if value in self.languages:
                        return value
                    else:
                        return self.babel_default_locale
            locale = session.get("locale")
            if locale:
                return locale
            session["locale"] = self.babel_default_locale
            return session["locale"]


## ... source file continues with no further has_request_context examples...


```


## Example 2 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / forum / locals.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/forum/locals.py)

```python
# locals.py
# -*- coding: utf-8 -*-
"""
    flaskbb.forum.locals
    --------------------
    Thread local helpers for FlaskBB

    :copyright: 2017, the FlaskBB Team
    :license: BSD, see license for more details
"""

~~from flask import _request_ctx_stack, has_request_context, request
from werkzeug.local import LocalProxy

from .models import Category, Forum, Post, Topic


@LocalProxy
def current_post():
    return _get_item(Post, 'post_id', 'post')


@LocalProxy
def current_topic():
    if current_post:
        return current_post.topic
    return _get_item(Topic, 'topic_id', 'topic')


@LocalProxy
def current_forum():
    if current_topic:
        return current_topic.forum
    return _get_item(Forum, 'forum_id', 'forum')


@LocalProxy
def current_category():
    if current_forum:
        return current_forum.category
    return _get_item(Category, 'category_id', 'category')


def _get_item(model, view_arg, name):
    if (
~~        has_request_context() and
        not getattr(_request_ctx_stack.top, name, None) and
        view_arg in request.view_args
    ):
        setattr(
            _request_ctx_stack.top,
            name,
            model.query.filter_by(id=request.view_args[view_arg]).first()
        )

    return getattr(_request_ctx_stack.top, name, None)


## ... source file continues with no further has_request_context examples...


```

