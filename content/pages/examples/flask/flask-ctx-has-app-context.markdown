title: flask.ctx has_app_context Example Code
category: page
slug: flask-ctx-has-app-context-examples
sortorder: 500021012
toc: False
sidebartitle: flask.ctx has_app_context
meta: Python example code that shows how to use the has_app_context callable from the flask.ctx module of the Flask project.


[has_app_context](https://github.com/pallets/flask/blob/master/src/flask/ctx.py)
is a function in the `flask.ctx` module that is similar to
[has_request_context](/flask-ctx-has-request-context-examples.html)
but for the
[application context](https://flask.palletsprojects.com/en/1.1.x/appcontext/)
rather than the request.

<a href="/flask-ctx-after-this-request-examples.html">after_this_request</a>
and
<a href="/flask-ctx-has-request-context-examples.html">has_request_context</a>
are a couple of other callables within the `flask.ctx` package that also have code examples.

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


## Example 2 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / util / i18n.py**](https://github.com/indico/indico/blob/master/indico/util/i18n.py)

```python
# i18n.py

import ast
import re
import textwrap
import traceback
import warnings
from contextlib import contextmanager

from babel import negotiate_locale
from babel.core import LOCALE_ALIASES, Locale
from babel.messages.pofile import read_po
from babel.support import NullTranslations, Translations
~~from flask import current_app, g, has_app_context, has_request_context, request, session
from flask_babelex import Babel, Domain, get_domain
from flask_pluginengine import current_plugin
from speaklater import is_lazy_string, make_lazy_string
from werkzeug.utils import cached_property

from indico.core.config import config
from indico.util.caching import memoize_request


LOCALE_ALIASES = dict(LOCALE_ALIASES, en='en_GB')
RE_TR_FUNCTION = re.compile(r'''_\("([^"]*)"\)|_\('([^']*)'\)''', re.DOTALL | re.MULTILINE)

babel = Babel()
_use_context = object()


def get_translation_domain(plugin_name=_use_context):
    if plugin_name is None:
        return get_domain()
    else:
        plugin = None
~~        if has_app_context():
            from indico.core.plugins import plugin_engine
            plugin = plugin_engine.get_plugin(plugin_name) if plugin_name is not _use_context else current_plugin
        if plugin:
            return plugin.translation_domain
        else:
            return get_domain()


def gettext_unicode(*args, **kwargs):
    from indico.util.string import inject_unicode_debug
    func_name = kwargs.pop('func_name', 'ugettext')
    plugin_name = kwargs.pop('plugin_name', None)
    force_unicode = kwargs.pop('force_unicode', False)

    if not isinstance(args[0], unicode):
        args = [(text.decode('utf-8') if isinstance(text, str) else text) for text in args]
        using_unicode = force_unicode
    else:
        using_unicode = True

    translations = get_translation_domain(plugin_name).get_translations()
    res = getattr(translations, func_name)(*args, **kwargs)
    res = inject_unicode_debug(res)
    if not using_unicode:


## ... source file continues with no further has_app_context examples...

```

