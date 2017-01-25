title: MongoDB
category: page
slug: mongodb
sortorder: 0914
toc: False
sidebartitle: MongoDB
meta: MongoDB is a document-oriented NoSQL database often used as a persistence layer in Python applications.


# MongoDB
[MongoDB](https://github.com/mongodb/mongo) is a document-oriented 
[NoSQL database](/no-sql-datastore.html) that is often used for
storing, querying and analyzing persistence data in Python applications.

<a href="https://github.com/mongodb/mongo" style="border: none;"><img src="/source/static/img/logos/mongodb.jpg" width="100%" alt="MongoDB logo." class="technical-diagram" /></a>

<div class="well see-also">MongoDB is an implementation of the <a href="/no-sql-datastore.html">NoSQL database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### General MongoDB introductions
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

* [MongoDB In 30 Minutes](https://www.youtube.com/watch?list=PL1Z_7yg6Pa3AhqCOTQKm9X_Sl9xLdMKYo&v=pWbMrx5rVBE)
   goes over the basics for creating, querying, updating and deleting data
   in MongoDB.

* [MongoDB queries do not always return all matching documents!](https://blog.meteor.com/mongodb-queries-dont-always-return-all-matching-documents-654b6594a827)
  walks through discovering that potential pitfalls on how MongoDB queries 
  operate that were non-intuitive to developers who are new to using this
  database.


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

* [10 tips to improve your MongoDB security](https://scalegrid.io/blog/10-tips-to-improve-your-mongodb-security/)
  provides concrete steps to take such as disabling the REST interface
  and other default bits that can be exploited if you are not intentionally
  using them.

* [MongoDB Security Basics For Your Deployments in AWS](https://www.mongodb.com/blog/post/mongodb-security-basics-for-your-deployments-in)
  is primarily a guide on AWS security from the perspective of using 
  installing and using MongoDB on your own instance. The post covers 
  authentication, SSL and firewalls.


### Python with MongoDB resources
MongoDB is straightforward to use in a Python application when a driver
such as PyMongo is installed. The following tutorials show how to install,
configure and start using MongoDB with Python.

* [Introduction to MongoDB and Python](https://realpython.com/blog/python/introduction-to-mongodb-and-python/)
  shows how to use Python to interface with MongoDB via PyMongo and 
  MongoEngine.

* A [Gentle Introduction to MongoDB using Pymongo](http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/)
  reviews a connection configuration file, the basics for data insertion,
  aggregation and updating records.

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
