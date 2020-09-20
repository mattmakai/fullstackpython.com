title: flask.views View Example Code
category: page
slug: flask-views-view-examples
sortorder: 500021034
toc: False
sidebartitle: flask.views View
meta: Example code for understanding how to use the View class from the flask.views module of the Flask project.


[View](https://github.com/pallets/flask/blob/master/src/flask/views.py)
is a class within the `flask.views` module of the [Flask](/flask.html)
project. `View` provides an alternative way to use view functions
by subclassing this class and implementing `dispatch_request`
for the routing system. This is typically only used in more advanced
situations such as extending the Flask source code, rather than
a standard way of interacting with the framework.

<a href="/flask-views-methodview-examples.html">MethodView</a>
and
<a href="/flask-views-http-method-funcs-examples.html">http_method_funcs</a>
are a couple of other callables within the `flask.views` package that also have code examples.

These topics are also useful while reading the `View` examples:

* [web development](/web-development.html) and [web design](/web-design.html)
* [web framework concepts](/web-frameworks.html) and the [Flask framework](/flask.html)


## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / utils / views.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/utils/views.py)

```python
# views.py
from flaskbb.utils.helpers import render_template
~~from flask.views import View


~~class RenderableView(View):
    def __init__(self, template, view):
        self.template = template
        self.view = view

    def dispatch_request(self, *args, **kwargs):
        view_model = self.view(*args, **kwargs)
        return render_template(self.template, **view_model)



## ... source file continues with no further View examples...

```


## Example 2 from Datadog Flask Example App
The [Datadog Flask example app](https://github.com/DataDog/trace-examples/tree/master/python/flask)
contains many examples of the [Flask](/flask.html) core functions
available to a developer using the [web framework](/web-frameworks.html).

[**Datadog Flask Example App / python/flask/app / app.py**](https://github.com/DataDog/trace-examples/blob/master/python/flask/app/./app.py)

```python
# app.py
from ddtrace import patch_all; patch_all(flask=True, requests=True)  # noqa

from ddtrace import tracer

from flask import Flask, Response
from flask import after_this_request
from flask import abort, jsonify, render_template, url_for
~~from flask.views import View
from werkzeug.routing import Rule

from flask_caching import Cache
from flask_cors import CORS

import requests

from .blueprint import bp
from .exceptions import AppException
from .limiter import limiter
from .signals import connect_signals

app = Flask(__name__)

app.register_blueprint(bp)

connect_signals(app)

CORS(app)
Cache(app, config=dict(CACHE_TYPE='simple'))
limiter.init_app(app)


@app.context_processor


## ... source file abbreviated to get to View examples ...



@app.route('/stream')
def stream():
    def generate():
        for i in range(100):
            yield '{}\n'.format(i)

    return Response(generate(), mimetype='text/plain')


@app.route('/abort/<int:code>')
def abort_endpoint(code):
    abort(code)


@app.errorhandler(404)
def handle_404(e):
    return '404', 404


@app.errorhandler(500)
def handle_500(e):
    return '500', 500


~~class MyView(View):
    methods = ['GET']

    def dispatch_request(self, name):
        return 'Hello %s!' % name


app.add_url_rule('/hello/<name>', view_func=MyView.as_view('myview'))



## ... source file continues with no further View examples...

```

