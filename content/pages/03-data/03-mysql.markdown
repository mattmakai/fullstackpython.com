title: MySQL
category: page
slug: mysql
sortorder: 0303
toc: False
sidebartitle: MySQL
meta: MySQL is an open source database often used by Python developers for storing and retrieving data.


MySQL is an open source [relational database](/databases.html) 
implementation for storing and retrieving data.

<img src="/img/logos/mysql.png" width="100%" alt="MySQL logo." class="shot">


## MySQL or PostgreSQL?
MySQL is a viable open source database implementation for Python web 
applications. MySQL has a slightly easier initial learning curve than 
[PostgreSQL](/postgresql.html). However, PostgreSQL's design is often 
preferred by Python web developers, especially when data migrations are
run as an application evolves.

<div class="well see-also">MySQL is an implementation of the <a href="/databases.html">relational database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Python Drivers for MySQL 
Accessing MySQL from a Python application requires a database driver (also
called a "connector"). While it is possible to write a driver as part of
your application, in practice most developers use an existing open source 
driver.

There was a major issue with MySQL drivers since the introduction of 
Python 3. One of the most popular libraries called 
[MySQLdb](https://pypi.org/project/MySQL-python/1.2.5) did not work
in its existing form with Python 3 and there were no plans to update it.
Therefore a fork of MySQLdb named 
[mysqlclient](https://pypi.org/project/mysqlclient) added Python 3
compatibility. 

The mysqlclient fork was good in that existing MySQLdb users could drop
mysqlclient into existing projects that were upgrading to Python 3. However,
the fork often causes confusion when searching for which Python driver to
use with MySQL. Many developer simply decide to use 
[PostgreSQL](/postgresql.html) because there is better support for Python
drivers in the PostgreSQL community. 

With that driver support context in mind, it's absolutely possible to build
a Python 3 web application with MySQL as a backend. Here is a list of
drivers along with whether it supports Python 2, 3 or both.

* [mysqlclient](https://pypi.org/project/mysqlclient) is a fork
  of MySQLdb that supports Python 2 and 3.

* [MySQL Connector](http://dev.mysql.com/doc/connector-python/en/)
  is Oracle's "official" (Oracle currently owns MySQL) Python connector.
  The driver supports Python 2 and 3, just make sure to check the 
  [version guide](http://dev.mysql.com/doc/connector-python/en/) for what
  releases work with which Python versions.

* [MySQLdb](https://pypi.org/project/MySQL-python/1.2.5) supports
  Python 2 and was frequently used by Python web applications before the
  mass migration to Python 3 began.

* [PyMySQL](https://github.com/PyMySQL/PyMySQL) is a pure Python 
  (no C low-level code) implementation that attempts to be a drop-in
  replacement for MySQLdb. However, some MySQL APIs are not supported
  by the driver so whether or not your application can use this connector
  will depend on what you're building.


## What organizations use MySQL?
The database is deployed in production at some of the highest 
trafficked sites such as 
[Uber](https://eng.uber.com/mysql-migration/),
[Twitter](https://blog.twitter.com/2012/mysql-twitter), 
[Facebook](https://www.facebook.com/notes/facebook-engineering/mysql-and-database-engineering-mark-callaghan/10150599729938920)
and [many others major organizations](http://www.mysql.com/customers/).
However, since
[MySQL AB](http://en.wikipedia.org/wiki/MySQL_AB), the company that 
developed MySQL, was purchased by Sun Microsystems (which was in turn 
purchased by Oracle), there have been major defections away from the 
database by 
[Wikipedia](http://www.zdnet.com/wikipedia-moving-from-mysql-to-mariadb-7000008912/) 
and [Google](http://readwrite.com/2013/09/14/google-waves-goodbye-to-mysql-in-favor-of-mariadb). 
MySQL remains a viable database option but I always recommend new Python 
developers learn [PostgreSQL](/postgresql.html) if they do not already know 
MySQL.


### Python-specific MySQL resources
The following resources show you how to work with MySQL in your
Python code either directly through SQL queries or less directly with an
[object-relational mapper (ORM)](/object-relational-mappers-orms.html)
like [SQLAlchemy](/sqlalchemy.html) or the [Django ORM](/django-orm.html).

* [Python MySQL tutorial](https://pynative.com/python-mysql-tutorial/)
  uses the MySQL Connector Python library to demonstrate how to run
  queries and stored procedures in your Python applications.

* [Python 3.4.0 with MySQL database](http://stackoverflow.com/questions/23376103/python-3-4-0-with-mysql-database)
  and 
  [Python 3 and MySQL](http://stackoverflow.com/questions/4960048/python-3-and-mysql)
  provide context for the commonly asked question about which database
  MySQL driver to use with Python 3.

* [Terrible Choices: MySQL](http://blog.ionelmc.ro/2014/12/28/terrible-choices-mysql/)
  is a blog post about specific deficiencies in MySQL's implementation that
  hinder its usage with Django's ORM.

* [MySQL Python tutorial](http://zetcode.com/db/mysqlpython/) uses the
  MySQLdb driver to connect to a MySQL server instance and shows some
  examples for inserting and querying data.


### General MySQL resources
There are many programming language agnostic tutorials for MySQL.
A handful of the best of these tutorials are listed below.

* [How to Install and Use MySQL on Ubuntu 16.04](/blog/install-mysql-ubuntu-1604.html)
  is a quick tutorial for getting up and running on Ubuntu Linux.

* [28 Beginner's Tutorials for Learning about MySQL Databases](http://designm.ag/tutorials/28-beginners-tutorials-for-learning-about-mysql-databases/) 
  is a curated collection on various introductory MySQL topics.

* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
  doesn't have the most original title but it's a good walkthrough of your
  first few steps in MySQL for creating users and working with tables.

* [mycli](https://www.mycli.net/) is a command line interface for MySQL
  that includes command completion and other super handy features.

* [Bye Bye MySQL & MongoDB, Guten Tag PostgreSQL](https://www.userlike.com/en/blog/2015/10/09/bye-by-mysql-and-mongodb-guten-tag-postgresql)
  goes into details for why the company Userlike migrated from their MySQL
  database setup to PostgreSQL.

* [MySQL sharding at Quora](https://www.quora.com/q/quoraengineering/MySQL-sharding-at-Quora)
  provides details behind Quora's at-scale infrastructure and
  how their MySQL sharding evolved over time.

* [Growing up with MySQL](https://nylas.com/blog/growing-up-with-mysql/) is
  a story about how one company went through dramatic growth and had to keep
  up with it by quickly scaling their MySQL database.

* [Monitoring MySQL metrics](https://www.datadoghq.com/blog/monitoring-mysql-performance-metrics/)
  is the first of a three part series, with the other parts on 
  [collecting metrics](https://www.datadoghq.com/blog/collecting-mysql-statistics-and-metrics/)
  and 
  [monitoring & collecting specifically with the DataDog tool](https://www.datadoghq.com/blog/mysql-monitoring-with-datadog/). The series explains what
  metrics you should be collecting and monitoring in your production
  database along with the purpose for why those metrics are important.

* [gh-ost](https://githubengineering.com/gh-ost-github-s-online-migration-tool-for-mysql/)
  ([source code](https://github.com/github/gh-ost)) is a schema migration
  tool built by GitHub and open sourced to the development community.
  The advantages of gh-ost are sustainable workloads on the master node
  to allow it to keep serving inbound query requests and the ability
  to pause the migration. The post on how to use gh-ost pairs nicely with
  GitHub's detailed write-up on how they perform backups, failover and 
  schema migrations in 
  [MySQL infrastructure testing automation at GitHub](https://githubengineering.com/mysql-testing-automation-at-github/).

* The 
  [unofficial MySQL optimizers guide](http://www.unofficialmysqlguide.com/)
  is intended for experienced developers who need to get better performance
  out of MySQL for their specific use cases.
 
* [The Ultimate Postgres vs MySQL Blog Post](https://dev.to/dmfay/the-ultimate-postgres-vs-mysql-blog-post-1l5f)
  provides comparisons of data types, default values, arrays, joins and
  many other differences between MySQL and PostgreSQL.
