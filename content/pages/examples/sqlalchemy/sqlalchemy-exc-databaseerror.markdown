title: sqlalchemy.exc DatabaseError Example Code
category: page
slug: sqlalchemy-exc-databaseerror-examples
sortorder: 500031036
toc: False
sidebartitle: sqlalchemy.exc DatabaseError
meta: Example code for understanding how to use the DatabaseError class from the sqlalchemy.exc module of the SQLAlchemy project.


`DatabaseError` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-invalidrequesterror-examples.html">InvalidRequestError</a>,
<a href="/sqlalchemy-exc-noinspectionavailable-examples.html">NoInspectionAvailable</a>,
<a href="/sqlalchemy-exc-nosuchtableerror-examples.html">NoSuchTableError</a>,
<a href="/sqlalchemy-exc-operationalerror-examples.html">OperationalError</a>,
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

[**indico / indico / web / rh.py**](https://github.com/indico/indico/blob/master/indico/web/rh.py)

```python
# rh.py

from __future__ import absolute_import, unicode_literals

import cProfile
import inspect
import itertools
import os
import time
from functools import partial, wraps

import jsonschema
from flask import current_app, g, redirect, request, session
~~from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.exceptions import BadRequest, Forbidden, MethodNotAllowed, NotFound
from werkzeug.routing import BuildError
from werkzeug.wrappers import Response

from indico.core import signals
from indico.core.config import config
from indico.core.db import db
from indico.core.db.sqlalchemy.core import handle_sqlalchemy_database_error
from indico.core.logger import Logger, sentry_set_tags
from indico.core.notifications import flush_email_queue, init_email_queue
from indico.util import fossilize
from indico.util.i18n import _
from indico.util.locators import get_locator
from indico.util.signals import values_from_signal
from indico.web.flask.util import url_for
from indico.web.util import is_signed_url_valid


HTTP_VERBS = {'GET', 'PATCH', 'POST', 'PUT', 'DELETE'}
logger = Logger.get('rh')


class RH(object):


## ... source file abbreviated to get to DatabaseError examples ...


        if request.method not in HTTP_VERBS:
            raise BadRequest

        res = ''
        g.rh = self
        sentry_set_tags({'rh': self.__class__.__name__})

        if self.EVENT_FEATURE is not None:
            self._check_event_feature()

        logger.info('%s %s [IP=%s] [PID=%s] [UID=%r]',
                    request.method, request.relative_url, request.remote_addr, os.getpid(), session.get('_user_id'))

        try:
            fossilize.clearCache()
            init_email_queue()
            self._check_csrf()
            res = self._do_process()
            signals.after_process.send()

            if self.commit:
                db.session.commit()
                flush_email_queue()
            else:
                db.session.rollback()
~~        except DatabaseError:
            db.session.rollback()
            handle_sqlalchemy_database_error()  # this will re-raise an exception
        except Exception:
            db.session.rollback()
            raise
        logger.debug('Request successful')

        if res is None:
            res = ''

        response = current_app.make_response(res)
        if self.DENY_FRAMES:
            response.headers['X-Frame-Options'] = 'DENY'
        return response


class RHSimple(RH):
    def __init__(self, func):
        RH.__init__(self)
        self.func = func

    def _process(self):
        rv = self.func()
        return rv


## ... source file continues with no further DatabaseError examples...

```

