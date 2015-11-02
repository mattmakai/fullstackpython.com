title: Databases
category: page
slug: databases
sort-order: 0502
meta: Relational databases a critical part of Python web applications. Learn more about persisting data in databases at Full Stack Python.


# Databases
A database is an abstraction on top of an operating system's file system to 
ease creating, reading, updating, and deleting persistent data. 


## Why are databases necessary?
At a high level web applications store data and present it to users in a 
useful way. For example, Google stores data about roads and provides 
directions to get from one location to another by driving through the 
[Maps](https://www.google.com/maps/) application. Driving directions are 
possible because the data is stored in a structured way. 

Databases make structured storage reliable and fast. They also give you a 
mental framework for how the data should be saved and retrieved instead of 
having to figure out what to do with the data every time you build a new 
application.

<div class="well see-also">
While you're learning about relational databases you should also read up on
<a href="/object-relational-mappers-orms.html">object-relational mappers (ORMs)</a> 
and check out the
<a href="/web-frameworks.html">web frameworks</a> page.
</div>


## Relational databases
The database storage abstraction most commonly used in Python web development 
is sets of relational tables. Alternative storage abstractions are explained 
in the [NoSQL](../no-sql-datastore.html) section of this guide.

Relational databases store all data in a series of tables. Interconnections
between the tables are specified as *foreign keys*.

Databases storage implementations vary in complexity. SQLite, a database 
included with Python, creates a single file for all data per database. 
Other databases such as Oracle, PostgreSQL, and MySQL have more complicated
persistence schemes while offering additional advanced features that are 
useful for web application data storage.

[PostgreSQL](http://www.postgresql.org/) and 
[MySQL](http://www.mysql.com/) are two of the most common open source
databases for storing Python web application data.

[SQLite](http://www.sqlite.org/) is a database that is stored in a single
file on disk. SQLite is built into Python but is only built for access
by a single connection at a time. Therefore is highly recommended to not
[run a production web application with SQLite](https://docs.djangoproject.com/en/dev/ref/databases/#database-is-locked-errors).


## PostgreSQL
PostgreSQL is the recommended relational database for working with Python
web applications. PostgreSQL's feature set, active development and stability
contribute to its usage as the backend for millions of applications live
on the Web today.


### PostgreSQL resources
* This post on 
  [using PostgreSQL with Django or Flask](http://killtheyak.com/use-postgresql-with-django-flask/)
  is a great quickstart guide for either framework.

* [PostgreSQL Weekly](http://postgresweekly.com/) is a weekly newsletter of
  PostgreSQL content from around the web.

* Braintree wrote about their experiences [scaling PostgreSQL](https://www.braintreepayments.com/braintrust/scaling-postgresql-at-braintree-four-years-of-evolution). 
The post is an inside look at the evolution of Braintree's usage of the database.

* This post estimates the [costs of a PostgreSQL connection](http://hans.io/blog/2014/02/19/postgresql_connection/index.html).

* There is no such thing as total security but this IBM article covers 
  [hardening a PostgreSQL database](http://www.ibm.com/developerworks/library/os-postgresecurity/). 

* Craig Kerstiens wrote a detailed post about [understanding PostgreSQL performance](http://www.craigkerstiens.com/2012/10/01/understanding-postgres-performance/).

* [Handling growth with Postgres](http://instagram-engineering.tumblr.com/post/40781627982/handling-growth-with-postgres-5-tips-from-instagram)
  provides 5 specific tips from Instagram's engineering team on how to scale
  the design of your PostgreSQL database.

* [Inserting And Using A New Record In Postgres](http://rob.conery.io/2015/02/09/inserting-using-new-record-postgres/)
  shows some SQL equivalents to what many developers just do in their ORM
  of choice.

* [Following a Select Statement Through Postgres Internals](http://patshaughnessy.net/2014/10/13/following-a-select-statement-through-postgres-internals)
  provides a fascinating look into the internal workings of PostgreSQL
  during a query.

* This article explains how and why PostgreSQL can handle [full text searching](http://blog.lostpropertyhq.com/postgres-full-text-search-is-good-enough/)
  for many use cases.

* If you're just getting started with PostgreSQL here are 
  [10 beginner tasks you should know how to execute](https://eye.raze.mx/10-beginner-postgresql-tasks-you-should-know/).

* The title's a bit presumptuous but here's a useful list of 
  [7 PostgreSQL data migration hacks you should be using, but aren't](http://engineering.tilt.com/7-postgresql-data-migration-hacks/).

* This guide to 
  [PostgreSQL monitoring](http://russ.garrett.co.uk/2015/10/02/postgres-monitoring-cheatsheet/)
  is handy for knowing what to measure and how to do it.

* While you can use a graphical interface for working with PostgreSQL, it's
  best to spend some time getting 
  [comfortable with the command-line interface](http://phili.pe/posts/postgresql-on-the-command-line/).


## MySQL
MySQL is another viable open source database backend option for Python web 
applications. MySQL has a slightly easier initial learning curve than 
PostgreSQL. The database is deployed in production at some of the highest 
trafficked sites such as 
[Twitter](https://blog.twitter.com/2012/mysql-twitter), 
[Facebook](https://www.facebook.com/notes/facebook-engineering/mysql-and-database-engineering-mark-callaghan/10150599729938920)
and [many others major organizations](http://www.mysql.com/customers/).
However, since the company focused on MySQL development, 
[MySQL AB](http://en.wikipedia.org/wiki/MySQL_AB), was 
purchased by Sun Microsystems (which was in turn purchased by Oracle), there
have been major defections away from the database by
[Wikipedia](http://www.zdnet.com/wikipedia-moving-from-mysql-to-mariadb-7000008912/) 
and [Google](http://readwrite.com/2013/09/14/google-waves-goodbye-to-mysql-in-favor-of-mariadb). 
MySQL remains a viable database option but I always recommend new Python 
developers learn PostgreSQL if they do not already know MySQL.


### MySQL resources
* [28 Beginner's Tutorials for Learning about MySQL Databases](http://designm.ag/tutorials/28-beginners-tutorials-for-learning-about-mysql-databases/) 
  is a curated collection on various introductory MySQL topics.

* This tutorial shows how to install [MySQL on Ubuntu](http://www.cs.wcupa.edu/rkline/index/mysql-lin.html).

* [Terrible Choices: MySQL](http://blog.ionelmc.ro/2014/12/28/terrible-choices-mysql/)
  is a blog post about specific deficiencies in MySQL's implementation that
  hinder its usage with Django's ORM.

* [Graph Data From MySQL Database in Python](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/)
  is an interesting study with code of how to pull data out of MySQL and graph
  the data with Plotly.

* [Pinterest open sourced many of their MySQL tools](https://engineering.pinterest.com/blog/open-sourcing-pinterest-mysql-management-tools)
  to manage instances of the database.


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


## General database resources
* [How does a relational database work?](http://coding-geek.com/how-databases-work/)
  is a detailed longform post on the sorting, searching, merging and other
  operations we often take for granted when using an established relational 
  database such as PostgreSQL.

* [Why I Love Databases](https://medium.com/@jeeyoungk/why-i-love-databases-1d4cc433685f)
  is a great read on the CAP Theorem, distributed systems and other topics
  that are at the core of database theory and implementation. Well worth
  the time to read.

* [DB-Engines](http://db-engines.com/en/ranking) ranks the most popular
  database management systems.

* [DB Weekly](http://dbweekly.com/) is a weekly roundup of general database 
  articles and resources.

* [A different view](http://blog.isotoma.com/2014/05/a-different-view/) 
  provides some perspective on the impedance mismatch between ORMs and
  traditional SQL queries.

* [Databases integration testing strategies](https://julien.danjou.info/blog/2014/db-integration-testing-strategies-python)
  covers a difficult topic that comes up on every real world project.

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

