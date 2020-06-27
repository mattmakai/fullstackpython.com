title: flask.templating render_template_string code examples
category: page
slug: flask-templating-render-template-string-examples
sortorder: 500021022
toc: False
sidebartitle: flask.templating render_template_string
meta: Python example code for the render_template_string function from the flask.templating module of the Flask project.


render_template_string is a function within the flask.templating module of the Flask project.


## Example 1 from Datadog Flask Example App
The [Datadog Flask example app](https://github.com/DataDog/trace-examples/tree/master/python/flask)
contains many examples of the [Flask](/flask.html) core functions
available to a developer using the [web framework](/web-frameworks.html).

[**Datadog Flask Example App / python/flask/app / blueprint.py**](https://github.com/DataDog/trace-examples/blob/master/python/flask/app/./blueprint.py)

```python
# blueprint.py
from ddtrace import Pin
~~from flask import abort, Blueprint, render_template_string

from .limiter import limiter


bp = Blueprint('bp', __name__, url_prefix='/bp/')

Pin.override(bp, service='flask-bp', app='flask', app_type='web')


@bp.before_request
def bp_before_request():
    print('Hook: bp_before_request')


@bp.before_app_request
def bp_before_app_request():
    print('Hook: bp_before_app_request')


@bp.before_app_first_request
def bp_before_app_first_request():
    print('Hook: bp_before_app_first_request')




## ... source file abbreviated to get to render_template_string examples ...


    print('Hook: bp_after_request')
    return response


@bp.after_app_request
def bp_after_app_request(response):
    print('Hook: bp_after_app_request')
    return response


@bp.teardown_request
def bp_teardown_request(response):
    print('Hook: bp_teardown_request')
    return response


@bp.teardown_app_request
def bp_teardown_app_request(response):
    print('Hook: bp_teardown_app_request')
    return response


@bp.route('/')
@limiter.limit('10 per second')
def index():
~~    return render_template_string('<h1>Blueprint</h1>')


@bp.route('/unknown')
@limiter.exempt
def unknown():
    abort(404)


@bp.errorhandler(404)
def bp_not_found(e):
    return 'oh no....', 404



## ... source file continues with no further render_template_string examples...

```

