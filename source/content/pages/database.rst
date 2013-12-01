Database
========

:category: page
:slug: database
:sort-order: 05

A database is an abstraction on top of an operating system's file system to 
ease creating, reading, updating, and deleting persistent data. The 
database storage abstraction most commonly used in Python web development is
sets of relational tables.

Relational Databases
--------------------
Relational databases store all data in a series of tables. Interconnections
between the tables are specified as *foreign keys*.

Databases storage implementations vary in complexity. SQLite, a database 
included with Python, creates a single file for all data per database. More 
complicated databases such as Oracle, PostgreSQL, and MySQL are more tightly
coupled with the operating system after installation.

`PostgreSQL <http://www.postgresql.org/>`_ and 
`MySQL <http://www.mysql.com/>`_ are two of the most common open source
databases.

`SQLite <http://www.sqlite.org/>`_ is a database that is stored in a single
file on disk. SQLite is built into Python but is only built for access
by a single connection at a time.


Database resources
------------------
`DB-Engines <http://db-engines.com/en/ranking>`_ ranks the most popular
database management systems.

