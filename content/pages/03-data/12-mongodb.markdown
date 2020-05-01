title: MongoDB
category: page
slug: mongodb
sortorder: 0312
toc: False
sidebartitle: MongoDB
meta: MongoDB is a document-oriented NoSQL database often used as a persistence layer in Python applications.


[MongoDB](https://github.com/mongodb/mongo) is a document-oriented 
[NoSQL database](/no-sql-datastore.html) that is often used for
storing, querying and analyzing persistence data in Python applications.

<a href="https://github.com/mongodb/mongo" style="border: none;"><img src="/img/logos/mongodb.jpg" width="100%" alt="MongoDB logo." class="shot" /></a>

<div class="well see-also">MongoDB is an implementation of the <a href="/no-sql-datastore.html">NoSQL database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### General MongoDB tutorials
It is worth taking some time to learn the ins and outs of MongoDB before
connecting it to your Python application. The following tutorials are 
not specific to Python and will have you work directly with the MongoDB
command line and query language.

* [Getting Started with MongoDB - Part 1](https://code.tutsplus.com/tutorials/getting-started-with-mongodb-part-1--net-22879) 
  and 
  [Part 2](https://code.tutsplus.com/tutorials/getting-started-with-mongodb-part-2--net-23636)
  are programming language agnostic tutorials that show how to interact
  via querying and various operators such as `$in`, `$lte` and `$gte`.

* [An Introduction to MongoDB](https://scotch.io/tutorials/an-introduction-to-mongodb) 
  examines common commands frequently used to perform data operations.

* [MongoDB In 30 Minutes](https://www.youtube.com/watch?v=-56x56UppqQ)
   goes over the basics for creating, querying, updating and deleting data
   in MongoDB.

* [MongoDB queries do not always return all matching documents!](https://blog.meteor.com/mongodb-queries-dont-always-return-all-matching-documents-654b6594a827)
  walks through discovering that potential pitfalls on how MongoDB queries 
  operate that were non-intuitive to developers who are new to using this
  database.

* [On MongoDB](https://www.nemil.com/mongo/index.html) is not a tutorial
  but instead discusses the culture and adoption patterns around how MongoDB
  became such a common NoSQL database. This is a must read to understand
  both the strengths and many weaknesses Mongo has despite what you may
  read in other introductory tutorials.

* This 3-part series on monitoring MongoDB with
  [WiredTiger](https://www.datadoghq.com/blog/monitoring-mongodb-performance-metrics-wiredtiger/)
  [MMAP](https://www.datadoghq.com/blog/monitoring-mongodb-performance-metrics-mmap/)
  and
  [Datadog](https://www.datadoghq.com/blog/monitor-mongodb-performance-with-datadog/)
  explains how to install and configure agents and gather metrics out
  of your MongoDB instances.

* [How to Investigate MongoDB Query Performance](https://studio3t.com/knowledge-base/articles/mongodb-query-performance/)
  shows how to work with the MongoDB profiler, use the `explain` method 
  and check execution plans.

* [How to Optimize Performance of MongoDB](https://severalnines.com/blog/how-optimize-performance-mongodb)
  covers schema design, replication lag, resource provisioning and query
  efficiency.

* [Getting Started With Google Cloud Functions and MongoDB](https://thecodebarbarian.com/getting-started-with-google-cloud-functions-and-mongodb.html)
  shows how to connect Mongo with a 
  [Google Cloud Function](/google-cloud-functions.html) 
  to store persistent data while running on a serverless platform.


### MongoDB security
NoSQL databases can be a weak spot in a production deployment environment,
especially when default settings are built for ease of development instead
of proper access control. MongoDB is no exception with its loose default
security controls so make sure to lock down your instances.

* [For God's sake, secure your Mongo/Redis/etc!](https://medium.com/@shahinism/for-gods-sake-secure-your-mongo-redis-etc-4f310cf1bed2)
  explains the weak default security settings provided by many NoSQL 
  databases, including MongoDB. Make sure to automate locking down your
  NoSQL databases just as you would any other component in your stack.

* Before deploying a MongoDB instance to production, be sure to go through
  each of the items on the 
  [official MongoDB security checklist](https://docs.mongodb.com/manual/administration/security-checklist/).

* [The definitive guide to MongoDB security](https://opensource.com/article/19/1/mongodb-security)
  is a high-level overview for the multitude of tasks you must perform
  to lock down your MongoDB instances, such as appropriately using SSL 
  certificates and access-control lists.

* [MongoDB Security Basics For Your Deployments in AWS](https://www.mongodb.com/blog/post/mongodb-security-basics-for-your-deployments-in)
  is primarily a guide on AWS security from the perspective of using 
  installing and using MongoDB on your own instance. The post covers 
  authentication, SSL and firewalls.

* [Securing MongoDB using Let's Encrypt certificate](https://zohaib.me/securing-mongodb-using-lets-encrypt/)
  gives a configuration that encrypts that traffic coming from and
  going to your MongoDB instances using free 
  [Let's Encrypt certificates](https://letsencrypt.org/).

* This 4 post securing MongoDB series covers
  [Data Security Requirements for Regulatory Compliance](https://www.mongodb.com/blog/post/securing-mongodb-part-1-data-security-requirements-for-regulatory-compliance),
  [Database Access Control](https://www.mongodb.com/blog/post/securing-mongodb-part-2-database-access-control),
  [Database Auditing and Encryption](https://www.mongodb.com/blog/post/securing-mongodb-part-3-database-auditing-and-encryption)
  and 
  [Environmental Control & Database Management](https://www.mongodb.com/blog/post/securing-mongodb-part-4-environmental-control-and-database-management).

* Lightweight Directory Access Protocol (LDAP) is common in many 
  established company environments for security. This post on 
  [How to Configure LDAP Authentication for MongoDB](https://www.mongodb.com/blog/post/how-to-configure-LDAP-authentication-for-mongodb)
  goes over how to authenticate users via LDAP who are using MongoDB.


### Python with MongoDB resources
MongoDB is straightforward to use in a Python application when a driver
such as PyMongo is installed. The following tutorials show how to install,
configure and start using MongoDB with Python.

* [Introduction to MongoDB and Python](https://realpython.com/blog/python/introduction-to-mongodb-and-python/)
  shows how to use Python to interface with MongoDB via PyMongo and 
  MongoEngine.

* [How To Set Up Flask with MongoDB and Docker](https://www.digitalocean.com/community/tutorials/how-to-set-up-flask-with-mongodb-and-docker)
  combines the [Flask](/flask.html) web framework with MongoDB then
  containerizes the example application with [Docker](/docker.html).

* The [PyMongo project](https://api.mongodb.com/python/current/) creators 
  wrote a retrospective focusing on four decisions they would have done 
  differently with the benefit of hindsight:

    1. [start\_request](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-start-request/)
    1. [use\_greenlets](http://emptysqua.re/blog/it-seemed-like-a-good-idea-at-the-time-pymongo-use-greenlets/)
    1. [copy\_database](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-copy-database/)
    1. [MongoReplicaSetClient](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-mongoreplicasetclient/)

* [Python and MongoDB](https://talkpython.fm/episodes/show/2/python-and-mongodb)
  on the Talk Python to Me podcast has a great interview with the 
  MongoDB Python driver maintainer.

* [PyMongo Monday: Setting Up Your PyMongo Environment](https://www.mongodb.com/blog/post/pymongo-monday-setting-up-your-pymongo-environment)
  is an introduction to using MongoDB with Python code. This first
  part of the series shows how to set up the 
  [development environment](/development-environments.html) required
  for working with Mongo.

* [Testing MongoDB Failover in Your Python App](https://scalegrid.io/blog/pymongo-tutorial-testing-mongodb-failover-in-your-python-app/)
  shows show to switch to a MongoDB replica in production failure scenarios
  using the PyMongo library.

