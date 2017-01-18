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

<a href="" style="border: none;"><img src="/source/static/img/logos/mongodb.jpg" width="100%" alt="MongoDB logo." class="technical-diagram" /></a>

<div class="well see-also">MongoDB is an implementation of the <a href="/no-sql-datastore.html">NoSQL database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### Introduction to MongoDB tutorials
* [Introduction to MongoDB and Python](https://realpython.com/blog/python/introduction-to-mongodb-and-python/)
  shows how to use Python to interface with MongoDB via PyMongo and MongoEngine.

* [MongoDB In 30 Minutes](https://www.youtube.com/watch?list=PL1Z_7yg6Pa3AhqCOTQKm9X_Sl9xLdMKYo&v=pWbMrx5rVBE)
   goes over the basics for creating, querying, updating and deleting data
   in MongoDB.


### Specific MongoDB resources
* The [PyMongo project](https://api.mongodb.com/python/current/) creators 
  wrote a retrospective focusing on four decisions they would have done 
  differently with the benefit of hindsight:

    1. [start\_request](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-start-request/)
    1. [use\_greenlets](http://emptysqua.re/blog/it-seemed-like-a-good-idea-at-the-time-pymongo-use-greenlets/)
    1. [copy\_database](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-copy-database/)
    1. [MongoReplicaSetClient](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-mongoreplicasetclient/)

* [MongoDB queries do not always return all matching documents!](https://engineering.meteor.com/mongodb-queries-dont-always-return-all-matching-documents-654b6594a827)
  walks through discovering that potential pitfalls on how MongoDB queries 
  operate that were non-intuitive to some developers.

* [Python and MongoDB](https://talkpython.fm/episodes/show/2/python-and-mongodb)
  on the Talk Python to Me podcast has a great interview with the 
  MongoDB Python driver maintainer

