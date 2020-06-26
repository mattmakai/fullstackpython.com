title: flask.ctx has_app_context code examples
category: page
slug: flask-ctx-has-app-context-examples
sortorder: 500021006
toc: False
sidebartitle: flask.ctx has_app_context
meta: Python example code for the has_app_context function from the flask.ctx module of the Flask project.


has_app_context is a function within the flask.ctx module of the Flask project.


## Example 1 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / marshalling.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./marshalling.py)

```python
# marshalling.py
from __future__ import unicode_literals

from collections import OrderedDict
from functools import wraps
from six import iteritems

~~from flask import request, current_app, has_app_context

from .mask import Mask, apply as apply_mask
from .utils import unpack


def make(cls):
    if isinstance(cls, type):
        return cls()
    return cls


def marshal(data, fields, envelope=None, skip_none=False, mask=None, ordered=False):
    out, has_wildcards = _marshal(data, fields, envelope, skip_none, mask, ordered)

    if has_wildcards:
        from .fields import Wildcard

        items = []
        keys = []
        for dkey, val in fields.items():
            key = dkey
            if isinstance(val, dict):
                value = marshal(data, val, skip_none=skip_none, ordered=ordered)
            else:


## ... source file abbreviated to get to has_app_context examples ...



    out = OrderedDict(items) if ordered else dict(items)

    if envelope:
        out = OrderedDict([(envelope, out)]) if ordered else {envelope: out}

    return out, has_wildcards["present"]


class marshal_with(object):

    def __init__(
        self, fields, envelope=None, skip_none=False, mask=None, ordered=False
    ):
        self.fields = fields
        self.envelope = envelope
        self.skip_none = skip_none
        self.ordered = ordered
        self.mask = Mask(mask, skip=True)

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            mask = self.mask
~~            if has_app_context():
                mask_header = current_app.config["RESTX_MASK_HEADER"]
                mask = request.headers.get(mask_header) or mask
            if isinstance(resp, tuple):
                data, code, headers = unpack(resp)
                return (
                    marshal(
                        data,
                        self.fields,
                        self.envelope,
                        self.skip_none,
                        mask,
                        self.ordered,
                    ),
                    code,
                    headers,
                )
            else:
                return marshal(
                    resp, self.fields, self.envelope, self.skip_none, mask, self.ordered
                )

        return wrapper




## ... source file continues with no further has_app_context examples...

```

