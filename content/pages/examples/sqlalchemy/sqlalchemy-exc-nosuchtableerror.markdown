title: sqlalchemy.exc NoSuchTableError Example Code
category: page
slug: sqlalchemy-exc-nosuchtableerror-examples
sortorder: 500031040
toc: False
sidebartitle: sqlalchemy.exc NoSuchTableError
meta: Example code for understanding how to use the NoSuchTableError class from the sqlalchemy.exc module of the SQLAlchemy project.


`NoSuchTableError` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-databaseerror-examples.html">DatabaseError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-invalidrequesterror-examples.html">InvalidRequestError</a>,
<a href="/sqlalchemy-exc-noinspectionavailable-examples.html">NoInspectionAvailable</a>,
<a href="/sqlalchemy-exc-operationalerror-examples.html">OperationalError</a>,
<a href="/sqlalchemy-exc-programmingerror-examples.html">ProgrammingError</a>,
and <a href="/sqlalchemy-exc-unsupportedcompilationerror-examples.html">UnsupportedCompilationError</a>
are several other callables with code examples from the same `sqlalchemy.exc` package.

## Example 1 from PyHive
[PyHive](https://github.com/dropbox/PyHive)
([PyPI package information](https://pypi.org/project/PyHive/))
is a set of [DB-API](https://www.python.org/dev/peps/pep-0249/)
and
[SQLAlchemy](/sqlalchemy.html)
interfaces that make it easier to use [Presto](https://prestodb.io/)
and [Apache Hive](http://hive.apache.org/) with Python.
[Dropbox's engineering team](https://www.dropbox.com/jobs/teams/engineering)
created this code library, open sourced it and put it out under
the [Apache 2.0 license](https://github.com/dropbox/PyHive/blob/master/LICENSE).

[**PyHive / pyhive / tests / sqlalchemy_test_case.py**](https://github.com/dropbox/PyHive/blob/master/pyhive/tests/sqlalchemy_test_case.py)

```python
# sqlalchemy_test_case.py
from __future__ import absolute_import
from __future__ import unicode_literals

import abc
import contextlib
import functools

import pytest
import sqlalchemy
from builtins import object
from future.utils import with_metaclass
~~from sqlalchemy.exc import NoSuchTableError
from sqlalchemy.schema import Index
from sqlalchemy.schema import MetaData
from sqlalchemy.schema import Table
from sqlalchemy.sql import expression


def with_engine_connection(fn):
    @functools.wraps(fn)
    def wrapped_fn(self, *args, **kwargs):
        engine = self.create_engine()
        try:
            with contextlib.closing(engine.connect()) as connection:
                fn(self, engine, connection, *args, **kwargs)
        finally:
            engine.dispose()
    return wrapped_fn


class SqlAlchemyTestCase(with_metaclass(abc.ABCMeta, object)):
    @with_engine_connection
    def test_basic_query(self, engine, connection):
        rows = connection.execute('SELECT * FROM one_row').fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].number_of_rows, 1)  # number_of_rows is the column name


## ... source file continues with no further NoSuchTableError examples...

```

