title: sqlalchemy.databases mysql Example Code
category: page
slug: sqlalchemy-databases-mysql-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.databases mysql
meta: Python example code that shows how to use the mysql callable from the sqlalchemy.databases module of the SQLAlchemy project.


`mysql` is a callable within the `sqlalchemy.databases` module of the SQLAlchemy project.



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

[**PyHive / pyhive / sqlalchemy_presto.py**](https://github.com/dropbox/PyHive/blob/master/pyhive/./sqlalchemy_presto.py)

```python
# sqlalchemy_presto.py

from __future__ import absolute_import
from __future__ import unicode_literals

import re
from sqlalchemy import exc
from sqlalchemy import types
from sqlalchemy import util
~~from sqlalchemy.databases import mysql
from sqlalchemy.engine import default
from sqlalchemy.sql import compiler
from sqlalchemy.sql.compiler import SQLCompiler

from pyhive import presto
from pyhive.common import UniversalSet


class PrestoIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = UniversalSet()


_type_map = {
    'boolean': types.Boolean,
~~    'tinyint': mysql.MSTinyInteger,
    'smallint': types.SmallInteger,
    'integer': types.Integer,
    'bigint': types.BigInteger,
    'real': types.Float,
    'double': types.Float,
    'varchar': types.String,
    'timestamp': types.TIMESTAMP,
    'date': types.DATE,
    'varbinary': types.VARBINARY,
}


class PrestoCompiler(SQLCompiler):
    def visit_char_length_func(self, fn, **kw):
        return 'length{}'.format(self.function_argspec(fn, **kw))


class PrestoTypeCompiler(compiler.GenericTypeCompiler):
    def visit_CLOB(self, type_, **kw):
        raise ValueError("Presto does not support the CLOB column type.")

    def visit_NCLOB(self, type_, **kw):
        raise ValueError("Presto does not support the NCLOB column type.")



## ... source file continues with no further mysql examples...

```

