=========
Databases
=========

:category: page
:slug: databases
:sort-order: 06

A database is an abstraction on top of an operating system's file system to 
ease creating, reading, updating, and deleting persistent data. The 
database storage abstraction most commonly used in Python web development is
sets of relational tables. Alternative storage abstractions are explained in
the `NoSQL <../no-sql-datastore.html>`_ section of this guide.

Relational databases store all data in a series of tables. Interconnections
between the tables are specified as *foreign keys*.

Databases storage implementations vary in complexity. SQLite, a database 
included with Python, creates a single file for all data per database. 
Other databases such as Oracle, PostgreSQL, and MySQL have more complicated
persistence schemes while offering additional advanced features that are 
useful for web application data storage.

`PostgreSQL <http://www.postgresql.org/>`_ and 
`MySQL <http://www.mysql.com/>`_ are two of the most common open source
databases for storing Python web application data.

`SQLite <http://www.sqlite.org/>`_ is a database that is stored in a single
file on disk. SQLite is built into Python but is only built for access
by a single connection at a time. Therefore is highly recommended to not
`run a production web application with SQLite <https://docs.djangoproject.com/en/dev/ref/databases/#database-is-locked-errors>`_.

----------
PostgreSQL
----------
PostgreSQL is the recommended relational database for working with Python
web applications. PostgreSQL's feature set, active development and stability
contribute to its usage as the backend for millions of applications live
on the Web today.

PostgreSQL resources
====================
This post on "`Use PostgreSQL with Django or Flask <http://killtheyak.com/use-postgresql-with-django-flask/>`_" 
is a great quickstart guide for either framework.

`PostgreSQL Weekly <http://postgresweekly.com/>`_ is a weekly newsletter of
PostgreSQL content from around the web.

`Scaling PostgreSQL at Braintree <https://www.braintreepayments.com/braintrust/scaling-postgresql-at-braintree-four-years-of-evolution>`_. Fascinating
inside look at the evolution of the database's usage at Braintree.

`Total security in a PostgreSQL database <http://www.ibm.com/developerworks/library/os-postgresecurity/>`_. 
There is no such thing as total security but this is a good article anyway.

`Understanding PostgreSQL performance <http://www.craigkerstiens.com/2012/10/01/understanding-postgres-performance/>`_

`Handling growth with Postgres <http://instagram-engineering.tumblr.com/post/40781627982/handling-growth-with-postgres-5-tips-from-instagram>`_ 
provides 5 specific tips from Instagram's engineering team on how to scale
the design of your PostgreSQL database.


------------------------------------
Connecting to a database with Python
------------------------------------
To work with a relational database using Python, you need to use a code 
library. The most common libraries for relational databases are:

`psycopg2 <http://initd.org/psycopg/>`_ for PostgreSQL

`MySQLdb <https://pypi.python.org/pypi/MySQL-python/1.2.4>`_ for MySQL

`cx_Oracle <http://cx-oracle.sourceforge.net/>`_ for Oracle

SQLite support is built into Python 2.7+ and therefore a separate library
is not necessary. Simply "import sqlite3" to begin interfacing with the 
single file-based database.


-------------------------
Object-Relational Mapping
-------------------------
Object-relational mappers (ORMs) allow developers to access data from a 
backend by writing with Python code instead of SQL queries. Each web 
application framework handles integrating ORMs differently. 

Django provides an ORM with its core functionality. Flask leaves using an 
ORM up to an extension, such as 
`Flask-SQLALchemy <http://pythonhosted.org/Flask-SQLAlchemy/>`_. 

Developers can also use ORMs without a web framework, such as when
creating a data analysis tool or a batch script without a user interface. The 
most widely used stand-alone ORM written for Python is currently
`SQLAlchemy <http://www.sqlalchemy.org/>`_.


-----------------------------
Database third-party services
-----------------------------
Numerous companies run scalable database servers as a hosted service. 
Depending on the provider, there can be several advantages to using a 
hosted database third-party service:

1. automated backups and recovery
2. tightened security configurations
3. easy vertical scaling

`Amazon Relational Database Service (RDS) <http://aws.amazon.com/rds/>`_ 
provides pre-configured MySQL and PostgreSQL instances. The instances can
be scaled to larger or smaller configurations based on storage and performance
needs.

`Google Cloud SQL <https://developers.google.com/cloud-sql/>`_ is a service
with managed, backed up, replicated, and auto-patched MySQL instances. Cloud
SQL integrates with Google App Engine but can be used independently as well.


Database resources
==================
`DB-Engines <http://db-engines.com/en/ranking>`_ ranks the most popular
database management systems.

`DB Weekly <http://dbweekly.com/>`_ is a new (as of Feb 2014) weekly roundup 
of general database articles and resources.

