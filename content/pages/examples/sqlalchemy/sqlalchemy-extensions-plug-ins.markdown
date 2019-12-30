title: SQLAlchemy Extensions, Plug-ins and Related Libraries
category: page
slug: sqlalchemy-extensions-plug-ins-related-libraries
sortorder: 500030000
toc: False
sidebartitle: SQLAlchemy Extensions
meta: Python code extensions and plug-in example projects that show how to use the SQLAlchemy object-relational mapper.


[SQLAlchemy](/sqlalchemy.html) is a Python library for interacting
with [databases](/databases.html) either through SQL or with an
[object-relational mapper (ORM)](/object-relational-mappers-orms.html).

<a href="http://www.sqlalchemy.org/"><img src="/img/logos/sqlalchemy.jpg" width="100%" alt="SQLAlchemy logo." class="shot"></a> 

The following projects augment SQLAlchemy's capabilities by providing 
functionality not included with the library itself. For example, the
[Alembic](https://github.com/sqlalchemy/alembic) project makes it easier
to perform database schema migrations, which is frequently needed
as applications evolve and need to store additional data.


### Alembic
[Alembic](https://github.com/sqlalchemy/alembic) 
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI information](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make 
database schema changes. The Alembic project is open sourced under the 
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).


### flask-base
[flask-base](https://github.com/hack4impact/flask-base)
([project documentation](http://hack4impact.github.io/flask-base/))
provides boilerplate code for new [Flask](/flask.html) web apps.
The purpose of the boilerplate is to stitch together disparate
libraries that are commonly used in Flask projects, such as
[Redis](/redis.html) for fast caching and transient data storage, 
[SendGrid](https://www.twilio.com/sendgrid) for transactional email,
[SQLAlchemy](/sqlalchemy.html) for persistent data storage through a
[relational database](/databases.html) back end,
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) for form
handling, and many others.

flask-base is provided as open source under the 
[MIT license](https://github.com/hack4impact/flask-base/blob/master/LICENSE.md).


### flask-sqlalchemy
[flask-sqlalchemy](https://github.com/pallets/flask-sqlalchemy) 
([project documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
and
[PyPI information](https://pypi.org/project/Flask-SQLAlchemy/)) is a 
[Flask](/flask.html) extension that makes it easier to use 
[SQLAlchemy](/sqlalchemy.html) when building Flask apps. flask-sqlalchemy
provides helper functions that reduce the amount of common boilerplate 
code that you have to frequently write yourself if you did not use this 
library when combining Flask with SQLAlchemy.

flask-sqlalchemy is provided as open source under the 
[BSD 3-Clause "New" or "Revised" License](https://github.com/pallets/flask-sqlalchemy/blob/master/LICENSE.rst).


### GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with 
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).


### marshmallow-sqlalchemy
[marshmallow-sqlalchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy)
([project documentation](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/marshmallow-sqlalchemy/))
is a code library that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) with the 
[Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
data serialization tool.

The marshmallow-sqlalchemy project is provided as open source under the
[MIT license](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/LICENSE).


### sqlalchemy-utils
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

