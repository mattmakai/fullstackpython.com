title: django.db connections Example Code
category: page
slug: django-db-connections-examples
sortorder: 500011165
toc: False
sidebartitle: django.db connections
meta: Python example code for the connections callable from the django.db module of the Django project.


connections is a callable within the django.db module of the Django project.


## Example 1 from django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).

[**django-extensions / django_extensions / management / debug_cursor.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/management/debug_cursor.py)

```python
# debug_cursor.py
import six
import time
import traceback
from contextlib import contextmanager

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.backends import utils


@contextmanager
def monkey_patch_cursordebugwrapper(print_sql=None, print_sql_location=False, truncate=None, logger=six.print_, confprefix="DJANGO_EXTENSIONS"):
    if not print_sql:
        yield
    else:
        truncate = getattr(settings, '%s_PRINT_SQL_TRUNCATE' % confprefix, 1000)

        sqlparse = None
        if getattr(settings, '%s_SQLPARSE_ENABLED' % confprefix, True):
            try:
                import sqlparse

                sqlparse_format_kwargs_defaults = dict(
                    reindent_aligned=True,
                    truncate_strings=500,
                )
                sqlparse_format_kwargs = getattr(settings, '%s_SQLPARSE_FORMAT_KWARGS' % confprefix, sqlparse_format_kwargs_defaults)
            except ImportError:
                sqlparse = None

        pygments = None
        if getattr(settings, '%s_PYGMENTS_ENABLED' % confprefix, True):
            try:
                import pygments.lexers


## ... source file abbreviated to get to connections examples ...


                    if truncate:
                        raw_sql = raw_sql[:truncate]

                    if sqlparse:
                        raw_sql = sqlparse.format(raw_sql, **sqlparse_format_kwargs)

                    if pygments:
                        raw_sql = pygments.highlight(
                            raw_sql,
                            pygments.lexers.get_lexer_by_name("sql"),
                            pygments_formatter(**pygments_formatter_kwargs),
                        )

                    logger(raw_sql)
                    logger("Execution time: %.6fs [Database: %s]" % (execution_time, self.db.alias))
                    if print_sql_location:
                        logger("Location of SQL Call:")
                        logger(''.join(traceback.format_stack()))

        _CursorDebugWrapper = utils.CursorDebugWrapper

        class PrintCursorQueryWrapper(PrintQueryWrapperMixin, _CursorDebugWrapper):
            pass

        try:
~~            from django.db import connections
            _force_debug_cursor = {}
~~            for connection_name in connections:
                _force_debug_cursor[connection_name] = connections[connection_name].force_debug_cursor
        except Exception:
            connections = None

        utils.CursorDebugWrapper = PrintCursorQueryWrapper

        postgresql_base = None
        if django.VERSION >= (3, 0):
            try:
                from django.db.backends.postgresql import base as postgresql_base
                _PostgreSQLCursorDebugWrapper = postgresql_base.CursorDebugWrapper

                class PostgreSQLPrintCursorDebugWrapper(PrintQueryWrapperMixin, _PostgreSQLCursorDebugWrapper):
                    pass
            except (ImproperlyConfigured, TypeError):
                postgresql_base = None

        if postgresql_base:
            postgresql_base.CursorDebugWrapper = PostgreSQLPrintCursorDebugWrapper

        if connections:
~~            for connection_name in connections:
                connections[connection_name].force_debug_cursor = True

        yield

        utils.CursorDebugWrapper = _CursorDebugWrapper

        if postgresql_base:
            postgresql_base.CursorDebugWrapper = _PostgreSQLCursorDebugWrapper

        if connections:
~~            for connection_name in connections:
                connections[connection_name].force_debug_cursor = _force_debug_cursor[connection_name]



## ... source file continues with no further connections examples...

```

