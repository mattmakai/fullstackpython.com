title: sqlalchemy.sql.compiler SQLCompiler Example Code
category: page
slug: sqlalchemy-sql-compiler-sqlcompiler-examples
sortorder: 500031118
toc: False
sidebartitle: sqlalchemy.sql.compiler SQLCompiler
meta: Example code for understanding how to use the SQLCompiler class from the sqlalchemy.sql.compiler module of the SQLAlchemy project.


`SQLCompiler` is a class within the `sqlalchemy.sql.compiler` module of the SQLAlchemy project.



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
from sqlalchemy.databases import mysql
from sqlalchemy.engine import default
from sqlalchemy.sql import compiler
~~from sqlalchemy.sql.compiler import SQLCompiler

from pyhive import presto
from pyhive.common import UniversalSet


class PrestoIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = UniversalSet()


_type_map = {
    'boolean': types.Boolean,
    'tinyint': mysql.MSTinyInteger,
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


~~class PrestoCompiler(SQLCompiler):
    def visit_char_length_func(self, fn, **kw):
        return 'length{}'.format(self.function_argspec(fn, **kw))


class PrestoTypeCompiler(compiler.GenericTypeCompiler):
    def visit_CLOB(self, type_, **kw):
        raise ValueError("Presto does not support the CLOB column type.")

    def visit_NCLOB(self, type_, **kw):
        raise ValueError("Presto does not support the NCLOB column type.")

    def visit_DATETIME(self, type_, **kw):
        raise ValueError("Presto does not support the DATETIME column type.")

    def visit_FLOAT(self, type_, **kw):
        return 'DOUBLE'

    def visit_TEXT(self, type_, **kw):
        if type_.length:
            return 'VARCHAR({:d})'.format(type_.length)
        else:
            return 'VARCHAR'




## ... source file continues with no further SQLCompiler examples...

```

