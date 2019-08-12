title: Databases
category: page
slug: databases
sortorder: 0301
toc: False
sidebartitle: Relational Databases
meta: Relational databases serve the critical role of persisting data in many Python applications.


A database is an abstraction over an 
[operating system](/operating-systems.html)'s file system that makes
it easier for developers to build applications that create, read, update
and delete persistent data.

<img src="/img/logos/databases.jpg" width="100%" alt="PostgreSQL, SQLite and MySQL logos, copyright their respective owners." class="technical-diagram"  style="border-radius:5px;border:1px solid #999" />


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


## PostgreSQL database
PostgreSQL is the recommended relational database for working with Python
web applications. PostgreSQL's feature set, active development and stability
contribute to its usage as the backend for millions of applications live
on the Web today.

Learn more about using PostgreSQL with Python on the 
[PostgreSQL page](/postgresql.html).


## MySQL database
MySQL is another viable open source database implementation for Python 
applications. MySQL has a slightly easier initial learning curve than 
PostgreSQL but is not as feature rich.

Find out about Python applications with a MySQL backed on the dedicated 
[MySQL page](/mysql.html).


## Connecting to a database with Python
To work with a relational database using Python, you need to use a code 
library. The most common libraries for relational databases are:

* [psycopg2](http://initd.org/psycopg/) 
  ([source code](https://github.com/psycopg/psycopg2))
  for PostgreSQL.

* [MySQLdb](https://pypi.org/project/MySQL-python/1.2.5) 
  ([source code](https://github.com/farcepest/MySQLdb1)) 
  for MySQL. Note that this driver's development is mostly frozen so
  evaluating alternative drivers is wise if you are using 
  [MySQL](/mysql.html) as a backend.

* [cx\_Oracle](https://oracle.github.io/python-cx_Oracle/index.html) for 
  Oracle Database ([source code](https://github.com/oracle/python-cx_Oracle)).
  Oracle moved their
  [open source driver code from SourceForge to GitHub in 2017](https://blogs.oracle.com/developers/oracle-database-python-driver-now-on-github).


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


### SQL resources
You may plan to use an 
[object-relational mapper (ORM)](/object-relational-mappers-orms.html)
as your main way of interacting with a database, but you should still
learn the basics of SQL to create schemas and understand the SQL code
generated by the ORM. The following resources can help you get up to
speed on SQL if you have never previously used it.

* [Select Star SQL](https://selectstarsql.com/) is an interactive book for
  learning SQL. Highly recommended even if you feel you will only be working
  with an [object-relational mapper](/object-relational-mappers-orms.html)
  on your projects because you never know when you will need to drop into
  SQL to improve a generated query's slow performance.

* [A beginners guide to SQL](https://www.sohamkamani.com/blog/2016/07/07/a-beginners-guide-to-sql/)
  does a good job explaining the main keywords used in SQL statements
  such as `SELECT`, `WHERE`, `FROM`, `UPDATE` and `DELETE`.

* [SQL Tutorial](https://sqlzoo.net/) teaches the SQL basics that can be 
  used in all major relational database implementations.

* [Life of a SQL query](https://numeracy.co/blog/life-of-a-sql-query)
  explains what happens both conceptually and technically within a
  database when a SQL query is run. The author uses 
  [PostgreSQL](/postgresql.html) as the example database and SQL syntax
  throughout the post.

* [A Probably Incomplete, Comprehensive Guide to the Many Different Ways to JOIN Tables in SQL](https://blog.jooq.org/2017/01/12/a-probably-incomplete-comprehensive-guide-to-the-many-different-ways-to-join-tables-in-sql/)
  elaborates on one of the trickiest parts of writing SQL statements
  that bridge one or more tables: the `JOIN`.

* [Writing better SQL](http://www.craigkerstiens.com/2016/01/08/writing-better-sql/)
  is a short code styling guide to make your queries easier to read.

* [SQL Intermediate](https://www.dataquest.io/blog/sql-intermediate/) is a
  beyond-the-basics tutorial that uses open data from the 
  [US Consumer Financial Protection Bureau](https://www.consumerfinance.gov/)
  as examples for counting, querying and using views in PostgreSQL. 


### General database resources
* [How does a relational database work?](http://coding-geek.com/how-databases-work/)
  is a detailed longform post on the sorting, searching, merging and other
  operations we often take for granted when using an established relational 
  database such as PostgreSQL.

* [Databases 101](https://thomaslarock.com/2018/07/databases-101/) gives a
  great overview of the main relational database concepts that is relevant
  to even non-developers as an introduction.

* [Five Mistakes Beginners Make When Working With Databases](http://www.craigkerstiens.com/2016/06/07/five-mistakes-databases/)
  explains why you should not store images in databases as well as why to be 
  cautious with how you normalize your schema.

* [DB-Engines](http://db-engines.com/en/ranking) ranks the most popular
  database management systems.

* [DB Weekly](http://dbweekly.com/) is a weekly roundup of general database 
  articles and resources.

* [Designing Highly Scalable Database Architectures](https://www.red-gate.com/simple-talk/cloud/cloud-data/designing-highly-scalable-database-architectures/)
  covers horizontal and vertical scaling, replication and caching in
  relational database architectures.

* [Online migrations at scale](https://stripe.com/blog/online-migrations)
  is a great read on breaking down the complexity of a database schema
  migration for an operational database. The approach the author's team
  used was a 4-step dual writing pattern to carefully evolved the way
  data for subscriptions were stored so they could move to a new, more
  efficient storage model.

* [A one size fits all database doesn't fit anyone](https://www.allthingsdistributed.com/2018/06/purpose-built-databases-in-aws.html)
  explains Amazon Web Services' specific rationale for having so many types 
  of relational and non-relational databases on its platform but the article
  is also a good overview of various database models and their use cases.

* [SQL is 43 years old - here’s 8 reasons we still use it today](https://blog.sqlizer.io/posts/sql-43/)
  lists why SQL is commonly used by almost all developers even as the
  language approaches its fiftieth anniversary.

* [SQL keys in depth](https://begriffs.com/posts/2018-01-01-sql-keys-in-depth.html)
  provides a great explanation for what primary keys are and how you 
  should use them.

* [Exploring a data set in SQL](https://tapoueh.org/blog/2017/06/exploring-a-data-set-in-sql/)
  is a good example of how SQL alone can be used for 
  [data analysis](/data-analysis.html). This tutorial uses Spotify data
  to show how to extract what you are looking to learn from a data set.

* [Databases integration testing strategies](https://julien.danjou.info/blog/2014/db-integration-testing-strategies-python)
  covers a difficult topic that comes up on every real world project.

* GitLab provided their 
  [postmortem of a database outage on January 31](https://about.gitlab.com/2017/02/10/postmortem-of-database-outage-of-january-31/)
  as a way to be transparent to customers and help other development
  teams learn how they screwed up their database systems then found a way
  to recover.

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

