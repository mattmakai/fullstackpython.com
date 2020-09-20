title: flask.app ImmutableDict Example Code
category: page
slug: flask-app-immutabledict-examples
sortorder: 500021003
toc: False
sidebartitle: flask.app ImmutableDict
meta: Example code for understanding how to use the ImmutableDict class from the flask.app module of the Flask project.


[ImmutableDict](https://github.com/pallets/flask/blob/master/src/flask/app.py)
is a class within the flask.app module of the [Flask](/flask.html)
framework that is actually imported from the Werkzeug
[datastructures module](https://github.com/pallets/werkzeug/blob/master/src/werkzeug/datastructures.py).
The `ImmutableDict` class wraps a
[standard Python dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
so that values cannot be modified after initially being set.

<a href="/flask-app-badrequest-examples.html">BadRequest</a>,
<a href="/flask-app-flask-examples.html">Flask</a>,
and <a href="/flask-app-headers-examples.html">Headers</a>
are several other callables with code examples from the same `flask.app` package.

These topics are also useful while reading the `ImmutableDict` examples:

* [web development](/web-development.html) and [web design](/web-design.html)
* [Flask](/flask.html) and [web framework](/web-frameworks.html) concepts


## Example 1 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management.
The code is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / config.py**](https://github.com/indico/indico/blob/master/indico/core/config.py)

```python
# config.py

from __future__ import absolute_import, unicode_literals

import ast
import codecs
import os
import re
import socket
import warnings
from datetime import timedelta

import pytz
from celery.schedules import crontab
from flask import current_app, g
from flask.helpers import get_root_path
~~from werkzeug.datastructures import ImmutableDict
from werkzeug.urls import url_parse

from indico.util.caching import make_hashable
from indico.util.fs import resolve_link
from indico.util.packaging import package_is_editable
from indico.util.string import crc32, snakify


DEFAULTS = {
    'ATTACHMENT_STORAGE': 'default',
    'AUTH_PROVIDERS': {},
    'BASE_URL': None,
    'CACHE_BACKEND': 'files',
    'CACHE_DIR': '/opt/indico/cache',
    'CATEGORY_CLEANUP': {},
    'CELERY_BROKER': None,
    'CELERY_CONFIG': {},
    'CELERY_RESULT_BACKEND': None,
    'COMMUNITY_HUB_URL': 'https://hub.getindico.io',
    'CUSTOMIZATION_DEBUG': False,
    'CUSTOMIZATION_DIR': None,
    'CUSTOM_COUNTRIES': {},
    'CUSTOM_LANGUAGES': {},
    'DB_LOG': False,


## ... source file abbreviated to get to ImmutableDict examples ...


        allowed |= set(INTERNAL_DEFAULTS)
    for key in set(data) - allowed:
        warnings.warn('Ignoring unknown config key {}'.format(key))
    return {k: v for k, v in data.iteritems() if k in allowed}


def load_config(only_defaults=False, override=None):
    data = dict(DEFAULTS, **INTERNAL_DEFAULTS)
    if not only_defaults:
        path = get_config_path()
        config = _sanitize_data(_parse_config(path))
        data.update(config)
        env_override = os.environ.get('INDICO_CONF_OVERRIDE')
        if env_override:
            data.update(_sanitize_data(ast.literal_eval(env_override)))
        resolved_path = resolve_link(path) if os.path.islink(path) else path
        resolved_path = None if resolved_path == os.devnull else resolved_path
        data['CONFIG_PATH'] = path
        data['CONFIG_PATH_RESOLVED'] = resolved_path
        if resolved_path is not None:
            data['LOGGING_CONFIG_PATH'] = os.path.join(os.path.dirname(resolved_path), data['LOGGING_CONFIG_FILE'])

    if override:
        data.update(_sanitize_data(override, allow_internal=True))
    _postprocess_config(data)
~~    return ImmutableDict(data)


class IndicoConfig(object):

    __slots__ = ('_config', '_exc')

    def __init__(self, config=None, exc=AttributeError):
        object.__setattr__(self, '_config', config)
        object.__setattr__(self, '_exc', exc)

    @property
    def data(self):
        try:
            return self._config or current_app.config['INDICO']
        except KeyError:
            raise RuntimeError('config not loaded')

    @property
    def hash(self):
        return crc32(repr(make_hashable(sorted(self.data.items()))))

    @property
    def CONFERENCE_CSS_TEMPLATES_BASE_URL(self):
        return self.BASE_URL + '/css/confTemplates'


## ... source file continues with no further ImmutableDict examples...

```

