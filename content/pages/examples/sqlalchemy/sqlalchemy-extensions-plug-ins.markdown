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


### Amazon Redshift SQLAlchemy Dialect
[Amazon Redshift SQLAlchemy Dialect](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
that can communicate with the [AWS Redshift](https://aws.amazon.com/redshift/)
data store. The SQL is essentially [PostgreSQL](/postgresql.html)
and requires [psycopg2](https://www.psycopg.org/) to properly
operate. This project and its code are open sourced under the
[MIT license](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/LICENSE).


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


### GeoAlchemy2
[GeoAlchemy2](https://github.com/geoalchemy/geoalchemy2) 
([project documentation](https://geoalchemy-2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/GeoAlchemy2/))
extends [SQLAlchemy](/sqlalchemy.html) with new data types for working
with geospatial databases, particularly [PostGIS](http://postgis.net/),
which is a spatial database extender for [PostgreSQL](/postgresql.html).
The project is provided as open source under the 
[MIT license](https://github.com/geoalchemy/geoalchemy2/blob/master/COPYING.rst).


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


### graphene-sqlalchemy
[graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy)
([project documentation](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/)
and
[PyPI package information](https://pypi.org/project/graphene-sqlalchemy/))
is a [SQLAlchemy](/sqlalchemy.html) integration for 
[Graphene](https://graphene-python.org/), which makes it easier to build
GraphQL-based [APIs](/application-programming-interfaces.html) into Python
[web applications](/web-development.html). The package allows you to
subclass SQLAlchemy classes and build queries around them with custom
code to match the backend queries with the GraphQL-based request queries.
The project is provided as open source under the
[MIT license](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/LICENSE.md).


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


### PyHive
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


### sqlacodegen
[sqlacodegen](https://github.com/agronholm/sqlacodegen) 
([PyPI package information](https://pypi.org/project/sqlacodegen/))
is a tool for
reading from an existing [relational database](/databases.html) to
generate code to create [SQLAlchemy](/sqlalchemy.html) models based
on that database. The project is primarily written and maintained
by [Alex Grönholm (agronholm)](https://github.com/agronholm) and it
is open sourced under the 
[MIT license](https://github.com/agronholm/sqlacodegen/blob/master/LICENSE).


### sqlalchemy-clickhouse
[sqlalchemy-clickhouse](https://github.com/cloudflare/sqlalchemy-clickhouse)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
for communicating with the open source [ClickHouse](https://clickhouse.tech/)
database management system. ClickHouse is column-oriented and therefore
better for some use cases and worse for others compared to a traditional
[relational database](/databases.html). 

The code for this project is open sourced under the
[MIT license](https://github.com/cloudflare/sqlalchemy-clickhouse/blob/master/LICENSE.txt)
while ClickHouse is provided as open source under the
[Apache License 2.0](https://github.com/ClickHouse/ClickHouse/blob/master/LICENSE).


### sqlalchemy-datatables
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


### SQLAlchemy filters
[SQLAlchemy filters](https://github.com/juliotrigo/sqlalchemy-filters)
provides filtering, sorting and pagination for [SQLAlchemy](/sqlalchemy.html) 
query objects, which is particularly useful when building
[web APIs](/application-programming-interfaces.html). SQLAlchemy filters
is open sourced under the 
[Apache License version 2.0](https://github.com/juliotrigo/sqlalchemy-filters/blob/master/LICENSE).


### SQLAlchemy Mixins
[SQLAlchemy Mixins](https://github.com/absent1706/sqlalchemy-mixins)
([PyPI package information](https://pypi.org/project/sqlalchemy-mixins/))
is a collection of
[mixins](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
useful for extending [SQLAlchemy](/sqlalchemy.html) and simplifying
your [database](/databases.html)-interacting code for some common
use cases. SQLAlchemy Mixins is open sourced under the
[MIT license](https://github.com/absent1706/sqlalchemy-mixins/blob/master/LICENSE.txt).


### sqlalchemy-utils
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


### SQLAthanor
[SQLAthanor](https://github.com/insightindustry/sqlathanor)
([PyPI package information](https://pypi.org/project/sqlathanor/)
and
[project documentation](https://sqlathanor.readthedocs.io/en/latest/index.html))
is a [SQLAlchemy](/sqlalchemy.html) extension that provides serialization and 
deserialization support for JSON, CSV, YAML and Python dictionaries.
This project is similar to [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) 
with one major difference: SQLAthanor works through SQLAlchemy models
while Marshmallow is less coupled to SQLAlchemy because it requires 
separate representations of the serialization objects. Both libraries
have their uses depending on whether the project plans to use SQLAlchemy
for object representations or would prefer to avoid that couping.
SQLAthanor is open sourced under the
[MIT license](https://github.com/insightindustry/sqlathanor/blob/master/LICENSE).


### wtforms-alchemy
[wtforms-alchemy](git@github.com:kvesteri/wtforms-alchemy.git)
([documentation](https://wtforms-alchemy.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/WTForms-Alchemy/))
is a [WTForms](https://wtforms.readthedocs.io/en/2.2.1/) extension toolkit 
for easier creation of [SQLAlchemy](/sqlalchemy.html) model based forms.
While this project primarily focuses on proper form handling, it also
has many good examples of how to use various parts of SQLAlchemy in
its code base. The project is provided as open source under the
[MIT license](https://github.com/kvesteri/wtforms-alchemy/blob/master/LICENSE).

