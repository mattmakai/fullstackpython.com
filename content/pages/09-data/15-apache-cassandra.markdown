title: Apache Cassandra
category: page
slug: apache-cassandra
sortorder: 0915
toc: False
sidebartitle: Apache Cassandra
meta: Apache Cassandra is a column-family NoSQL data store occasionally used for persisting data in Python applications.


# Apache Cassandra
[Apache Cassandra](http://cassandra.apache.org/) is a column-family NoSQL 
data store occasionally used for persisting data in 
[Python web applications](/web-development.html) and 
[data projects](/data.html).

<a href="http://cassandra.apache.org/" style="border: none;"><img src="/img/logos/cassandra.png" width="100%" alt="Apache Cassandra project logo." class="technical-diagram" /></a>

<div class="well see-also">Apache Cassandra is an implementation of the <a href="/no-sql-datastore.html">NoSQL database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


## Python with Cassandra resources
* [DataStax's Python Cassandra driver](https://datastax.github.io/python-driver/)
  can be installed as an 
  [application dependency](/application-dependencies.html) to make it
  easier to access and work with Cassandra in your Python applications.

* [Async Python and Cassandra with Gevent](http://rustyrazorblade.com/2016/02/async-python-and-cassandra-with-gevent/)
  explains how you monkeypatch [gevent](http://www.gevent.org/) into 
  a Python 2.7 application and work with Cassandra using gevent's coroutines.
  Note that this post could have instead been written with 
  [asycnio](https://docs.python.org/3/library/asyncio.html) if it were
  coded with Python 3.

* [How to Install and Use Cassandra on Django](http://www.slothparadise.com/how-to-install-and-use-cassandra-on-django/)
  instructs how to use Cassandra with Django 1.8 but it should still be
  relevant for newer Django versions as well.

* [Using Cassandra with Python and uWSGI](http://blog.turret.io/using-cassandra-with-python-and-uwsgi/)
  gives some short example code for connecting to a Cassandra cluster outside
  the HTTP request-response cycle to prevent timeouts and blocking issues with
  [WSGI servers](/wsgi-servers.html).


## General Cassandra resources
Apache Cassandra can be used independently of Python applications for
data storage and querying. The learning curve for getting started is similar
to other [NoSQL data stores](/no-sql-datastore.html) but scaling, performance
and monitoring can be challenging. The following resources focus on addressing
those issues based on teams that have felt the pain and often released their
resulting tools as open source projects.

* The official 
  [getting started documentation for Cassandra](http://cassandra.apache.org/doc/latest/getting_started/index.html) 
  provides installation, configuration, and basic querying information.

* [Monitoring Cassandra at Scale](http://engineeringblog.yelp.com/2016/06/monitoring-cassandra-at-scale.html)
  explains how the Yelp engineering team uses Cassandra to complement their 
  MySQL and ElasticSearch instances. The post does a nice job of enumerating
  the warning signs to monitor and provides a short example of an issue with
  replication that could be caught by their approach.

* [How Not To Use Cassandra Like An RDBMS (and what will happen if you do)](https://opencredo.com/how-not-to-use-cassandra-like-an-rdbms-and-what-will-happen-if-you-do/)
  gives examples in Cassandra's query language CQL of operations that are 
  typical with [relational databases](/databases.html) but go *terribly* wrong
  with Cassandra, due to its NoSQL architecture that is optimized for other
  types of operations.
  
* [Backup and Recovery for Apache Cassandra and Scale-Out Databases](https://www.youtube.com/watch?v=krGmn4D2fgY)
  covers issues encountered when trying to take snapshot backups of Cassandra 
  due to partitions and consistency lag time that occur with just about every
  Cassandra setup.

