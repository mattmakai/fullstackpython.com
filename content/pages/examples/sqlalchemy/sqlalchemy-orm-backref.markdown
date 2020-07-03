title: sqlalchemy.orm backref code examples
category: page
slug: sqlalchemy-orm-backref-examples
sortorder: 500031045
toc: False
sidebartitle: sqlalchemy.orm backref
meta: Python example code for the backref callable from the sqlalchemy.orm module of the SQLAlchemy project.


backref is a callable within the sqlalchemy.orm module of the SQLAlchemy project.


## Example 1 from sqlalchemy-datatables
[sqlalchemy-datatables](https://github.com/Pegase745/sqlalchemy-datatables)
([PyPI package information](https://pypi.org/project/sqlalchemy-datatables/))
is a helper library that makes it easier to use [SQLAlchemy](/sqlalchemy.html)
with the jQuery [JavaScript](/javascript.html)
[DataTables](https://datatables.net/) plugin. This library is designed to
be [web framework](/web-frameworks.html) agnostic and provides code examples
for both [Flask](/flask.html) and [Pyramid](/pyramid.html).

The project is built and maintained by
[Michel Nemnom (Pegase745)](https://github.com/Pegase745) and is open
sourced under the
[MIT license](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/LICENSE).

[**sqlalchemy-datatables / tests / models.py**](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/./tests/models.py)

```python
# models.py
import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
~~from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    birthday = Column(Date)
~~    address = relationship('Address', uselist=False, backref=backref('user'))

    def __unicode__(self):
        return '%s' % self.name

    def __repr__(self):
        return '<%s#%s>' % (self.__class__.__name__, self.id)

    @hybrid_property
    def dummy(self):
        return self.name[0:3]

    @dummy.expression
    def dummy(cls):
        return func.substr(cls.name, 0, 3)


class Address(Base):

    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    description = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))



## ... source file continues with no further backref examples...

```

