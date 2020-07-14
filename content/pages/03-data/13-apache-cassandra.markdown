title: Apache Cassandra
category: page
slug: apache-cassandra
sortorder: 0313
toc: False
sidebartitle: Apache Cassandra
meta: Apache Cassandra is a column-family NoSQL data store occasionally used for persisting data in Python applications.


[Apache Cassandra](http://cassandra.apache.org/) is a column-family NoSQL 
data store designed for write-heavy persistent storage in 
[Python web applications](/web-development.html) and 
[data projects](/data.html).

<a href="http://cassandra.apache.org/" style="border: none;"><img src="/img/logos/cassandra.png" width="100%" alt="Apache Cassandra project logo." class="shot" /></a>

<div class="well see-also">Apache Cassandra is an implementation of the <a href="/no-sql-datastore.html">NoSQL database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


## Python with Cassandra resources
Cassandra is commonly used with Python for write-heavy application demands.
The following tutorials walk through several of the helper libraries that
can be used to interact with Cassandra, with and without web frameworks such
as [Django](/django.html).

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

* [Using Cassandra with Python and uWSGI](http://blog.turret.io/using-cassandra-with-python-and-uwsgi/)
  gives some short example code for connecting to a Cassandra cluster outside
  the HTTP request-response cycle to prevent timeouts and blocking issues with
  [WSGI servers](/wsgi-servers.html).

* The Stack Overflow thread asking about the 
  [best Cassandra library/driver for Python?](https://stackoverflow.com/questions/10430417/best-cassandra-library-wrapper-for-python)
  has a good answer on why to use the 
  [datastax/python-driver](https://github.com/datastax/python-driver)
  project due to its CQL support and active development.

* [Cassandra performance in Python: Avoid namedtuple](https://rhye.org/post/python-cassandra-namedtuple-performance/)
  covers the performance penalty of using the `namedtuple` type with the
  DataStax Cassandra Python driver and how you can work around it.


## How Companies Use Cassandra
These resources are written by engineering teams at organizations that
have large scale Cassandra deployments. The posts cover topics such as
monitoring, scaling and usage with billions of records.

* [How Discord Stores Billions of Messages](https://blog.discordapp.com/how-discord-stores-billions-of-messages-7fa6ec7ee4c7)
  talks about the evolution of Discord's very large scale message store
  system from a [MongoDB](/mongodb.html) instance to Cassandra for storing 
  messages in a distributed, replicated cluster.

* [Monitoring Cassandra at Scale](http://engineeringblog.yelp.com/2016/06/monitoring-cassandra-at-scale.html)
  explains how the Yelp engineering team uses Cassandra to complement their 
  MySQL and ElasticSearch instances. The post does a nice job of enumerating
  the warning signs to monitor and provides a short example of an issue with
  replication that could be caught by their approach.

* [How Uber Manages A Million Writes Per Second Using Mesos And Cassandra Across Multiple Datacenters ](http://highscalability.com/blog/2016/9/28/how-uber-manages-a-million-writes-per-second-using-mesos-and.html)
  shows why Uber needs accurate real-time data at large scale to make their
  driver and passenger operations run properly. The post goes into the
  overall architecture they use including cluster size, tolerable latency
  and other libraries in their stack.


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

* [How Not To Use Cassandra Like An RDBMS (and what will happen if you do)](https://opencredo.com/how-not-to-use-cassandra-like-an-rdbms-and-what-will-happen-if-you-do/)
  gives examples in Cassandra's query language CQL of operations that are 
  typical with [relational databases](/databases.html) but go *terribly* wrong
  with Cassandra, due to its NoSQL architecture that is optimized for other
  types of operations.

* [Cassandra Query Language (CQL) Tutorial](http://abiasforaction.net/cassandra-query-language-cql-tutorial/)
  explains the concepts and syntax behind the data management language that 
  is Cassandra's equivalent to relational database SQL.

* [Backup and Recovery for Apache Cassandra and Scale-Out Databases](https://www.youtube.com/watch?v=krGmn4D2fgY)
  covers issues encountered when trying to take snapshot backups of Cassandra 
  due to partitions and consistency lag time that occur with just about every
  Cassandra setup.

* [Getting the Most Out of Cassandra](https://www.youtube.com/watch?v=Q9EA8E-eLf0)
  is a video for on data modeling and application development for developers
  new to Cassandra.

* [The Total Newbie’s Guide to Cassandra](https://blog.insightdatascience.com/the-total-newbies-guide-to-cassandra-e63bce0316a4)
  compares Cassandra to traditional [relational databases](/databases.html).

* [On Cassandra Collections, Updates, and Tombstones](https://www.sestevez.com/on-cassandra-collections-updates-and-tombstones/)
  and
  [Undetectable tombstones in Apache Cassandra](http://thelastpickle.com/blog/2018/07/05/undetectable-tombstones-in-apache-cassandra.html)
  present how developers often use Cassandra collections incorrectly
  when they are not experienced with how the data store operates. 

* [When to use Cassandra and when to steer clear](https://towardsdatascience.com/when-to-use-cassandra-and-when-to-steer-clear-72b7f2cede76)
  explains the advantages Cassandra provides such as high throughput on
  writes (versus reads) and availability. The disadvantages are also
  given such as strong consistency, typical relational database-style
  (ACID) transactions and reads without knowing the primary key of the 
  record you want to access. These are common database tradeoffs you need
  to understand based on your workload and decide upon *before* you build 
  out your whole data architecture!

* [Analyzing Cassandra Performance with Flame Graphs](http://thelastpickle.com/blog/2018/01/16/cassandra-flame-graphs.html)
  and
  [Garbage Collection Tuning for Apache Cassandra](http://thelastpickle.com/blog/2018/04/11/gc-tuning.html)
  are two posts in a series on how to debug issues in operational 
  Cassandra deployments using appropriate data visualization, especially
  when the issue is due to the Java Virtual Machine (JVM)'s garbage 
  collection methods.

