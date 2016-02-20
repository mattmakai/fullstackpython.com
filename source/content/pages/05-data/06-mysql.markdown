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

<div class="well see-also">PostgreSQL is an implementation of the <a href="/databases.html">relational database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


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


### MySQL resources
* [28 Beginner's Tutorials for Learning about MySQL Databases](http://designm.ag/tutorials/28-beginners-tutorials-for-learning-about-mysql-databases/) 
  is a curated collection on various introductory MySQL topics.

* This tutorial shows how to install [MySQL on Ubuntu](http://www.cs.wcupa.edu/rkline/index/mysql-lin.html).

* [Graph Data From MySQL Database in Python](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/)
  is an interesting study with code of how to pull data out of MySQL and graph
  the data with Plotly.

* [Pinterest open sourced many of their MySQL tools](https://engineering.pinterest.com/blog/open-sourcing-pinterest-mysql-management-tools)
  to manage instances of the database.

* [Bye Bye MySQL & MongoDB, Guten Tag PostgreSQL](https://www.userlike.com/en/blog/2015/10/09/bye-by-mysql-and-mongodb-guten-tag-postgresql)
  goes into details for why the company Userlike migrated from their MySQL
  database setup to PostgreSQL.

* [Terrible Choices: MySQL](http://blog.ionelmc.ro/2014/12/28/terrible-choices-mysql/)
  is a blog post about specific deficiencies in MySQL's implementation that
  hinder its usage with Django's ORM.

