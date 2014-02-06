Databases
=========

:category: page
:slug: databases
:sort-order: 05

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
databases.

`SQLite <http://www.sqlite.org/>`_ is a database that is stored in a single
file on disk. SQLite is built into Python but is only built for access
by a single connection at a time. Therefore is highly recommended to not
`run a production web application with SQLite <https://docs.djangoproject.com/en/dev/ref/databases/#database-is-locked-errors>`_.


Database connections with Python
--------------------------------
To work with a relational database using Python, you need to use a code 
library. The most common libraries for relational databases are:

`psycopg2 <http://initd.org/psycopg/>`_ for PostgreSQL

`MySQLdb <https://pypi.python.org/pypi/MySQL-python/1.2.4>`_ for MySQL

`cx_Oracle <http://cx-oracle.sourceforge.net/>`_ for Oracle

SQLite support is built into Python 2.7+ and therefore a separate library
is not necessary. Simply "import sqlite3" to begin interfacing with the 
single file-based database.


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
------------------
`DB-Engines <http://db-engines.com/en/ranking>`_ ranks the most popular
database management systems.

`PostgreSQL Weekly <http://postgresweekly.com/>`_ is a weekly newsletter of
PostgreSQL content from around the web.


