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

<a href="http://cassandra.apache.org/" style="border: none;"><img src="/source/static/img/logos/cassandra.png" width="100%" alt="Apache Cassandra project logo." class="technical-diagram" /></a>

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


