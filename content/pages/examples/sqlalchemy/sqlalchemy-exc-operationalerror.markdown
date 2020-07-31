title: sqlalchemy.exc OperationalError Example Code
category: page
slug: sqlalchemy-exc-operationalerror-examples
sortorder: 500031041
toc: False
sidebartitle: sqlalchemy.exc OperationalError
meta: Example code for understanding how to use the OperationalError class from the sqlalchemy.exc module of the SQLAlchemy project.


`OperationalError` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-databaseerror-examples.html">DatabaseError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-invalidrequesterror-examples.html">InvalidRequestError</a>,
<a href="/sqlalchemy-exc-noinspectionavailable-examples.html">NoInspectionAvailable</a>,
<a href="/sqlalchemy-exc-nosuchtableerror-examples.html">NoSuchTableError</a>,
<a href="/sqlalchemy-exc-programmingerror-examples.html">ProgrammingError</a>,
and <a href="/sqlalchemy-exc-unsupportedcompilationerror-examples.html">UnsupportedCompilationError</a>
are several other callables with code examples from the same `sqlalchemy.exc` package.

## Example 1 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management that is
powered by [SQLAlchemy](/sqlalchemy.html) on the backend. The code
for this project is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / web / errors.py**](https://github.com/indico/indico/blob/master/indico/web/errors.py)

```python
# errors.py

from __future__ import absolute_import, unicode_literals

import traceback
from uuid import uuid4

from flask import g, jsonify, render_template, request, session
from itsdangerous import BadData
~~from sqlalchemy.exc import OperationalError
from werkzeug.exceptions import Forbidden, HTTPException

from indico.core.errors import NoReportError
from indico.legacy.common.cache import GenericCache
from indico.web.util import get_request_info
from indico.web.views import WPError


def render_error(exc, title, message, code, standalone=False):
    _save_error(exc, title, message)
    if _need_json_response():
        return _jsonify_error(exc, title, message, code)
    elif standalone:
        return render_template('standalone_error.html', error_message=title, error_description=message), code
    else:
        try:
            return WPError(title, message).getHTML(), code
~~        except OperationalError:
            return render_error(exc, title, message, code, standalone=True)


def load_error_data(uuid):
    return GenericCache('errors').get(uuid)


def _save_error(exc, title, message):
    if 'saved_error_uuid' in g:
        return
    if not _is_error_reportable(exc):
        return
    g.saved_error_uuid = uuid = unicode(uuid4())
    tb = traceback.format_exc()
    data = {'title': title,
            'message': message,
            'request_info': get_request_info(),
            'traceback': tb,
            'sentry_event_id': g.get('sentry_event_id')}
    GenericCache('errors').set(uuid, data, 7200)


def _need_json_response():
    return request.is_xhr or request.is_json


## ... source file continues with no further OperationalError examples...

```


## Example 2 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlalchemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / functions / database.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/database.py)

```python
# database.py
import itertools
import os
from collections.abc import Mapping, Sequence
from copy import copy

import sqlalchemy as sa
from sqlalchemy.engine.url import make_url
~~from sqlalchemy.exc import OperationalError, ProgrammingError

from ..utils import starts_with
from .orm import quote


def escape_like(string, escape_char='*'):
    return (
        string
        .replace(escape_char, escape_char * 2)
        .replace('%', escape_char + '%')
        .replace('_', escape_char + '_')
    )


def json_sql(value, scalars_to_json=True):
    scalar_convert = sa.text
    if scalars_to_json:
        def scalar_convert(a):
            return sa.func.to_json(sa.text(a))

    if isinstance(value, Mapping):
        return sa.func.json_build_object(
            *(
                json_sql(v, scalars_to_json=False)


## ... source file abbreviated to get to OperationalError examples ...


        text = "SELECT 1 FROM pg_database WHERE datname='%s'" % database
        return bool(get_scalar_result(engine, text))

    elif engine.dialect.name == 'mysql':
        text = ("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA "
                "WHERE SCHEMA_NAME = '%s'" % database)
        return bool(get_scalar_result(engine, text))

    elif engine.dialect.name == 'sqlite':
        if database:
            return database == ':memory:' or sqlite_file_exists(database)
        else:
            return True

    else:
        engine.dispose()
        engine = None
        text = 'SELECT 1'
        try:
            url.database = database
            engine = sa.create_engine(url)
            result = engine.execute(text)
            result.close()
            return True

~~        except (ProgrammingError, OperationalError):
            return False
        finally:
            if engine is not None:
                engine.dispose()


def create_database(url, encoding='utf8', template=None):

    url = copy(make_url(url))

    database = url.database

    if url.drivername.startswith('postgres'):
        url.database = 'postgres'
    elif url.drivername.startswith('mssql'):
        url.database = 'master'
    elif not url.drivername.startswith('sqlite'):
        url.database = None

    if url.drivername == 'mssql+pyodbc':
        engine = sa.create_engine(url, connect_args={'autocommit': True})
    elif url.drivername == 'postgresql+pg8000':
        engine = sa.create_engine(url, isolation_level='AUTOCOMMIT')
    else:


## ... source file continues with no further OperationalError examples...

```

