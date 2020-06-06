title: sqlalchemy.exc OperationalError code examples
category: page
slug: sqlalchemy-exc-operationalerror-examples
sortorder: 500031004
toc: False
sidebartitle: sqlalchemy.exc OperationalError
meta: Python example code for the OperationalError class from the sqlalchemy.exc module of the SQLAlchemy project.


OperationalError is a class within the sqlalchemy.exc module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / functions / database.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/functions/database.py)

```python
# database.py
try:
    from collections.abc import Mapping, Sequence
except ImportError:  # For python 2.7 support
    from collections import Mapping, Sequence
import itertools
import os
from copy import copy

import sqlalchemy as sa
from sqlalchemy.engine.url import make_url
~~from sqlalchemy.exc import OperationalError, ProgrammingError

from ..utils import starts_with
from .orm import quote


def escape_like(string, escape_char='*'):
    """
    Escape the string paremeter used in SQL LIKE expressions.

    ::

        from sqlalchemy_utils import escape_like


        query = session.query(User).filter(
            User.name.ilike(escape_like('John'))
        )


    :param string: a string to escape
    :param escape_char: escape character
    """
    return (
        string


## ... source file abbreviated to get to OperationalError examples ...



    elif engine.dialect.name == 'sqlite':
        if database:
            return database == ':memory:' or sqlite_file_exists(database)
        else:
            # The default SQLAlchemy database is in memory,
            # and :memory is not required, thus we should support that use-case
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
    """Issue the appropriate CREATE DATABASE statement.

    :param url: A SQLAlchemy engine URL.
    :param encoding: The encoding to create the database as.
    :param template:
        The name of the template from which to create the new database. At the
        moment only supported by PostgreSQL driver.

    To create a database, you can pass a simple URL that would have
    been passed to ``create_engine``. ::

        create_database('postgresql://postgres@localhost/name')

    You may also pass the url from an existing engine. ::

        create_database(engine.url)



## ... source file continues with no further OperationalError examples...


```

