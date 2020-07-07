title: sqlalchemy.orm Query Example Code
category: page
slug: sqlalchemy-orm-query-examples
sortorder: 500031052
toc: False
sidebartitle: sqlalchemy.orm Query
meta: Example code for understanding how to use the Query class from the sqlalchemy.orm module of the SQLAlchemy project.


Query is a class within the sqlalchemy.orm module of the SQLAlchemy project.


## Example 1 from SQLAlchemy Mixins
[SQLAlchemy Mixins](https://github.com/absent1706/sqlalchemy-mixins)
([PyPI package information](https://pypi.org/project/sqlalchemy-mixins/))
is a collection of
[mixins](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
useful for extending [SQLAlchemy](/sqlalchemy.html) and simplifying
your [database](/databases.html)-interacting code for some common
use cases. SQLAlchemy Mixins is open sourced under the
[MIT license](https://github.com/absent1706/sqlalchemy-mixins/blob/master/LICENSE.txt).

[**SQLAlchemy Mixins / sqlalchemy_mixins / session.py**](https://github.com/absent1706/sqlalchemy-mixins/blob/master/sqlalchemy_mixins/./session.py)

```python
# session.py
~~from sqlalchemy.orm import Session, scoped_session, Query
from .utils import classproperty


class NoSessionError(RuntimeError):
    pass


class SessionMixin:
    _session = None

    @classmethod
    def set_session(cls, session):
        cls._session = session

    @classproperty
    def session(cls):
        if cls._session is not None:
            return cls._session
        else:
            raise NoSessionError('Cant get session.'
                                 'Please, call SaActiveRecord.set_session()')

    @classproperty
    def query(cls):


## ... source file continues with no further Query examples...

```

