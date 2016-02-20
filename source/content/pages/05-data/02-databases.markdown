title: Databases
category: page
slug: databases
sortorder: 0502
toc: False
sidebartitle: Relational Databases
meta: Relational databases serve the critical role of persisting data in many Python applications.


# Databases
A database is an abstraction on top of an operating system's file system to 
ease creating, reading, updating, and deleting persistent data. 


## Why are databases necessary?
At a high level web applications store data and present it to users in a 
useful way. For example, Google stores data about roads and provides 
directions to get from one location to another by driving through the 
[Maps](https://www.google.com/maps/) application. Driving directions are 
possible because the data is stored in a structured format. 

Databases make structured storage reliable and fast. They also give you a 
mental framework for how the data should be saved and retrieved instead of 
having to figure out what to do with the data every time you build a new 
application.

<div class="well see-also">Databases are a concept with many implementations, including <a href="/postgresql.html">PostgreSQL</a>, <a href="/mysql.html">MySQL</a> and <a href="/sqlite.html">SQLite</a>. Non-relational databases called <a href="/no-sql-datastore.html">NoSQL data stores</a> also exist.  Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Relational databases
The database storage abstraction most commonly used in Python web development 
is sets of relational tables. Alternative storage abstractions are explained 
on the [NoSQL](/no-sql-datastore.html) page.

Relational databases store data in a series of tables. Interconnections
between the tables are specified as *foreign keys*. A foreign key is a
unique reference from one row in a relational table to another row in
a table, which can be the same table but is most commonly a different table.

Databases storage implementations vary in complexity. SQLite, a database 
included with Python, creates a single file for all data per database. 
Other databases such as [PostgreSQL](/postgresql.html),
[MySQL](/mysql.html), Oracle and Microsoft SQL Server have more 
complicated persistence schemes while offering additional advanced features 
that are useful for web application data storage. These advanced
features include but are not limited to:

1. data replication between a master database and one or more read-only slave 
   instances
1. advanced column types that can efficiently store semi-structured data
   such as JavaScript Object Notation (JSON)
1. sharding, which allows horizontal scaling of multiple databases that 
   each serve as read-write instances at the cost of latency in data
   consistency
1. monitoring, statistics and other useful runtime information for
   database schemas and tables

Typically web applications start with a single database instance such
as PostgreSQL with a straightforward schema. Over time the database 
schema evolves to a more complex structure using schema migrations and 
advanced features such as replication, sharding and monitoring become
more useful as database utilization increases based on the application
users' needs.


## Most common databases for Python web apps
[PostgreSQL](http://www.postgresql.org/) and 
[MySQL](http://www.mysql.com/) are two of the most common open source
databases for storing Python web applications' data.

[SQLite](http://www.sqlite.org/) is a database that is stored in a single
file on disk. SQLite is built into Python but is only built for access
by a single connection at a time. Therefore is highly recommended to not
[run a production web application with SQLite](https://docs.djangoproject.com/en/dev/ref/databases/#database-is-locked-errors).


## PostgreSQL
PostgreSQL is the recommended relational database for working with Python
web applications. PostgreSQL's feature set, active development and stability
contribute to its usage as the backend for millions of applications live
on the Web today.

Learn more about using PostgreSQL with Python on the 
[PostgreSQL page](/postgresql.html).


## MySQL
MySQL is another viable open source database implementation for Python 
applications. MySQL has a slightly easier initial learning curve than 
PostgreSQL but is not as feature rich.

Find out about Python applications with a MySQL backed on the dedicated 
[MySQL page](/mysql.html).


## Connecting to a database with Python
To work with a relational database using Python, you need to use a code 
library. The most common libraries for relational databases are:

* [psycopg2](http://initd.org/psycopg/) for PostgreSQL

* [MySQLdb](https://pypi.python.org/pypi/MySQL-python/1.2.5) for MySQL

* [cx\_Oracle](http://cx-oracle.sourceforge.net/) for Oracle

SQLite support is built into Python 2.7+ and therefore a separate library
is not necessary. Simply "import sqlite3" to begin interfacing with the 
single file-based database.


## Object-relational Mapping
Object-relational mappers (ORMs) allow developers to access data from a 
backend by writing Python code instead of SQL queries. Each web 
application framework handles integrating ORMs differently. There's 
[an entire page on object-relational mapping](/object-relational-mappers-orms.html) 
(ORMs) that you should read to get a handle on this subject.


## Database third-party services
Numerous companies run scalable database servers as a hosted service.
Hosted databases can often provide automated backups and recovery,
tightened security configurations and easy vertical scaling, depending on the
provider.

* [Amazon Relational Database Service (RDS)](http://aws.amazon.com/rds/)
  provides pre-configured MySQL and PostgreSQL instances. The instances can
  be scaled to larger or smaller configurations based on storage and performance
  needs.

* [Google Cloud SQL](https://developers.google.com/cloud-sql/) is a service
  with managed, backed up, replicated, and auto-patched MySQL instances. Cloud
  SQL integrates with Google App Engine but can be used independently as well.

* [BitCan](http://www.gobitcan.com/) provides both MySQL and MongoDB hosted
  databases with extensive backup services.

* [ElephantSQL](https://www.elephantsql.com/) is a software-as-a-service company
  that hosts PostgreSQL databases and handles the server configuration, backups
  and data connections on top of Amazon Web Services instances.


## General database resources
* [How does a relational database work?](http://coding-geek.com/how-databases-work/)
  is a detailed longform post on the sorting, searching, merging and other
  operations we often take for granted when using an established relational 
  database such as PostgreSQL.

* [Why I Love Databases](https://medium.com/@jeeyoungk/why-i-love-databases-1d4cc433685f)
  is a great read on the CAP Theorem, distributed systems and other topics
  that are at the core of database theory and implementation. Well worth
  the time to read.

* [Writing better SQL](http://www.craigkerstiens.com/2016/01/08/writing-better-sql/)
  is a short code styling guide to make your queries easier to read.

* [DB-Engines](http://db-engines.com/en/ranking) ranks the most popular
  database management systems.

* [DB Weekly](http://dbweekly.com/) is a weekly roundup of general database 
  articles and resources.

* [Databases integration testing strategies](https://julien.danjou.info/blog/2014/db-integration-testing-strategies-python)
  covers a difficult topic that comes up on every real world project.

* [Asynchronous Python and Databases](http://techspot.zzzeek.org/2015/02/15/asynchronous-python-and-databases/)
  is an in-depth article covering why many Python database drivers cannot
  be used without modification due to the differences in blocking versus
  asychronous event models. Definitely worth a read if you are using
  [WebSockets](/websockets.html) via Tornado or gevent.

* [PostgreSQL vs. MS SQL Server](http://www.pg-versus-ms.com/) is one
  perspective on the differences between the two database servers from a
  data analyst.


## Databases learning checklist
1. Install PostgreSQL on your server. Assuming you went with Ubuntu run 
   ``sudo apt-get install postgresql``.

1. Make sure the [psycopg2](http://initd.org/psycopg/) library is in your
   application's dependencies.

1. Configure your web application to connect to the PostgreSQL instance.

1. Create models in your ORM, either with Django's 
   [built-in ORM](https://docs.djangoproject.com/en/dev/topics/db/) or
   [SQLAlchemy with Flask](http://www.sqlalchemy.org/). 

1. Build your database tables or sync the ORM models with the PostgreSQL 
   instance, if you're using an ORM.

1. Start creating, reading, updating and deleting data in the database 
   from your web application.

