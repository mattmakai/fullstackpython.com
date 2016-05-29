title: MySQL
category: page
slug: mysql
sortorder: 0506
toc: False
sidebartitle: MySQL
meta: MySQL is an open source database often used by Python developers for storing and retrieving data.


# MySQL
MySQL is an open source [relational database](/databases.html) 
implementation for storing and retrieving data.

<img src="/img/mysql.png" width="100%" alt="MySQL logo." class="technical-diagram" />


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
[MySQLdb](https://pypi.python.org/pypi/MySQL-python/1.2.5) did not work
in its existing form with Python 3 and there were no plans to update it.
Therefore a fork of MySQLdb named 
[mysqlclient](https://pypi.python.org/pypi/mysqlclient) added Python 3
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

* [mysqlclient](https://mysqlclient.readthedocs.io/en/latest/) is a fork
  of MySQLdb that supports Python 2 and 3.

* [MySQL Connector](http://dev.mysql.com/doc/connector-python/en/)
  is Oracle's "official" (Oracle currently owns MySQL) Python connector.
  The driver supports Python 2 and 3, just make sure to check the 
  [version guide](http://dev.mysql.com/doc/connector-python/en/) for what
  releases work with which Python versions.

* [MySQLdb](https://pypi.python.org/pypi/MySQL-python/1.2.5) supports
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
developers learn PostgreSQL if they do not already know MySQL.


### Python-specific MySQL resources
* [Python 3.4.0 with MySQL database](http://stackoverflow.com/questions/23376103/python-3-4-0-with-mysql-database)
  and 
  [Python 3 and MySQL](http://stackoverflow.com/questions/4960048/python-3-and-mysql)
  provide context for the commonly asked question about which database
  MySQL driver to use with Python 3.

* [Terrible Choices: MySQL](http://blog.ionelmc.ro/2014/12/28/terrible-choices-mysql/)
  is a blog post about specific deficiencies in MySQL's implementation that
  hinder its usage with Django's ORM.

* [Graph Data From MySQL Database in Python](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/)
  is an interesting study with code of how to pull data out of MySQL and graph
  the data with Plotly.

* [MySQL Python tutorial](http://zetcode.com/db/mysqlpython/) uses the
  MySQLdb driver to connect to a MySQL server instance and shows some
  examples for inserting and querying data.


### General MySQL resources
* [28 Beginner's Tutorials for Learning about MySQL Databases](http://designm.ag/tutorials/28-beginners-tutorials-for-learning-about-mysql-databases/) 
  is a curated collection on various introductory MySQL topics.

* This tutorial shows how to install [MySQL on Ubuntu](http://www.cs.wcupa.edu/rkline/index/mysql-lin.html).

* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
  doesn't have the most original title but it's a good walkthrough of your
  first few steps in MySQL for creating users and working with tables.

* [Pinterest open sourced many of their MySQL tools](https://engineering.pinterest.com/blog/open-sourcing-pinterest-mysql-management-tools)
  to manage instances of the database.

* [Bye Bye MySQL & MongoDB, Guten Tag PostgreSQL](https://www.userlike.com/en/blog/2015/10/09/bye-by-mysql-and-mongodb-guten-tag-postgresql)
  goes into details for why the company Userlike migrated from their MySQL
  database setup to PostgreSQL.

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

