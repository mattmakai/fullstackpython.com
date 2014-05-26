title: Databases
category: page
slug: databases
sort-order: 041
choice1url: /no-sql-datastore.html
choice1icon: fa-inbox
choice1text: What about non-relational data stores hipsters tell me to use? 
choice2url: /wsgi-servers.html
choice2icon: fa-css3 fa-inverse
choice2text: My app is running but looks awful. How do I style the interface?
choice3url: /javascript.html
choice3icon: fa-html5 fa-inverse
choice3text: How do I create a better user experience with JavaScript?
choice4url: /logging.html
choice4icon: fa-align-left fa-inverse
choice4text: How do I log issues when they occur in my app?


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

* Craig Kerstien's wrote a detailed post about [understanding PostgreSQL performance](http://www.craigkerstiens.com/2012/10/01/understanding-postgres-performance/).

* [Handling growth with Postgres](http://instagram-engineering.tumblr.com/post/40781627982/handling-growth-with-postgres-5-tips-from-instagram)
  provides 5 specific tips from Instagram's engineering team on how to scale
  the design of your PostgreSQL database.


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


## Connecting to a database with Python
To work with a relational database using Python, you need to use a code 
library. The most common libraries for relational databases are:

* [psycopg2](http://initd.org/psycopg/) for PostgreSQL

* [MySQLdb](https://pypi.python.org/pypi/MySQL-python/1.2.4) for MySQL

* [cx\_Oracle](http://cx-oracle.sourceforge.net/) for Oracle

SQLite support is built into Python 2.7+ and therefore a separate library
is not necessary. Simply "import sqlite3" to begin interfacing with the 
single file-based database.


## Object-Relational Mapping
Object-relational mappers (ORMs) allow developers to access data from a 
backend by writing Python code instead of SQL queries. Each web 
application framework handles integrating ORMs differently. 

Django provides an ORM with its core functionality. Flask leaves using an 
ORM up to an extension, such as 
[Flask-SQLALchemy](http://pythonhosted.org/Flask-SQLAlchemy/). 

Developers can also use ORMs without a web framework, such as when
creating a data analysis tool or a batch script without a user interface. 
Currently, the most widely used stand-alone ORM written for Python is
[SQLAlchemy](http://www.sqlalchemy.org/).


## Database third-party services
Numerous companies run scalable database servers as a hosted service. 
Depending on the provider, there can be several advantages to using a 
hosted database third-party service:

1. automated backups and recovery
2. tightened security configurations
3. easy vertical scaling

[Amazon Relational Database Service (RDS)](http://aws.amazon.com/rds/) 
provides pre-configured MySQL and PostgreSQL instances. The instances can
be scaled to larger or smaller configurations based on storage and performance
needs.

[Google Cloud SQL](https://developers.google.com/cloud-sql/) is a service
with managed, backed up, replicated, and auto-patched MySQL instances. Cloud
SQL integrates with Google App Engine but can be used independently as well.


## Database resources
* [DB-Engines](http://db-engines.com/en/ranking) ranks the most popular
  database management systems.

* [DB Weekly](http://dbweekly.com/) is a weekly roundup of general database 
  articles and resources.

* [SQLAlchemy vs Other ORMs](http://www.pythoncentral.io/sqlalchemy-vs-orms/)
  provides a detailed comparison of SQLAlchemy against alternatives.

* [A different view](http://blog.isotoma.com/2014/05/a-different-view/) 
  provides some perspective on the impedance mismatch between ORMs and
  traditional SQL queries.


## Databases learning checklist
<i class="fa fa-check-square-o"></i>
Install PostgreSQL on your server. Assuming you went with Ubuntu run 
``sudo apt-get install postgresql``.

<i class="fa fa-check-square-o"></i>
Make sure the [psycopg2](http://initd.org/psycopg/) library is part of your
application dependencies.

<i class="fa fa-check-square-o"></i>
Configure your web application to connect to the PostgreSQL instance.

<i class="fa fa-check-square-o"></i>
Create models in your ORM, either with Django's 
[built-in ORM](https://docs.djangoproject.com/en/dev/topics/db/) or
[SQLAlchemy with Flask](http://www.sqlalchemy.org/). 

<i class="fa fa-check-square-o"></i>
Sync the ORM models with the PostgreSQL instance.

<i class="fa fa-check-square-o"></i>
Start creating, reading, updating and deleting data in the database from your 
web application.


### What's next to get your app running?
