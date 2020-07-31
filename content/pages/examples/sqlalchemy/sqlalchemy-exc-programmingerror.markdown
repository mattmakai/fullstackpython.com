title: sqlalchemy.exc ProgrammingError Example Code
category: page
slug: sqlalchemy-exc-programmingerror-examples
sortorder: 500031042
toc: False
sidebartitle: sqlalchemy.exc ProgrammingError
meta: Example code for understanding how to use the ProgrammingError class from the sqlalchemy.exc module of the SQLAlchemy project.


`ProgrammingError` is a class within the `sqlalchemy.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-exc-argumenterror-examples.html">ArgumentError</a>,
<a href="/sqlalchemy-exc-dataerror-examples.html">DataError</a>,
<a href="/sqlalchemy-exc-databaseerror-examples.html">DatabaseError</a>,
<a href="/sqlalchemy-exc-integrityerror-examples.html">IntegrityError</a>,
<a href="/sqlalchemy-exc-invalidrequesterror-examples.html">InvalidRequestError</a>,
<a href="/sqlalchemy-exc-noinspectionavailable-examples.html">NoInspectionAvailable</a>,
<a href="/sqlalchemy-exc-nosuchtableerror-examples.html">NoSuchTableError</a>,
<a href="/sqlalchemy-exc-operationalerror-examples.html">OperationalError</a>,
and <a href="/sqlalchemy-exc-unsupportedcompilationerror-examples.html">UnsupportedCompilationError</a>
are several other callables with code examples from the same `sqlalchemy.exc` package.

## Example 1 from sqlalchemy-utils
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


## ... source file abbreviated to get to ProgrammingError examples ...


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


## ... source file continues with no further ProgrammingError examples...

```

