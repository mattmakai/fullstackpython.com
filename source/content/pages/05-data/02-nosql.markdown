title: NoSQL Data Stores
category: page
slug: no-sql-datastore
sort-order: 0502
meta: NoSQL data stores persistent data in different ways than traditional relational databases. Learn more about NoSQL on Full Stack Python.


# NoSQL Data Stores
Relational databases store the vast majority of web application 
persistent data. However, there are several alternative classifications of 
storage representations.

1. Key-value pair
2. Document-oriented
3. Column-family table
4. Graph

These persistent data storage representations are commonly used to augment,
rather than completely replace, relational databases. The underlying 
persistence type used by the NoSQL database often gives it different
performance characteristics than a relational database, with better results
on some types of read/writes and worse performance on others.


## Key-value Pair
Key-value pair data stores are based
on [hash map](http://en.wikipedia.org/wiki/Hash_table) data structures.


### Key-value pair data stores
* [Redis](http://redis.io/) is an open source in-memory key-value pair data 
  store. Redis is often called "the Swiss Army Knife of web application
  development." It can be used for caching, queuing, and storing session data 
  for faster access than a traditional relational database, among many other
  use cases. [Redis-py](https://github.com/andymccurdy/redis-py) is a solid
  Python client to use with Redis.


### Key-value pair resources
* "[How To Install and Use Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis)"
  is a guide for getting up with the extremely useful in-memory data store.

* This video on 
  [Scaling Redis at Twitter](https://www.youtube.com/watch?v=rP9EKvWt0zo) is
  a detailed look behind the scenes with a massive Redis deployment.

* [Walrus](http://charlesleifer.com/blog/walrus-lightweight-python-utilities-for-working-with-redis/)
  is a higher-level Python wrapper for Redis with some caching, querying
  and data structure components build into the library.


## Document-oriented
A document-oriented database provides a semi-structured representation for
nested data. 


### Document-oriented data stores
* [MongoDB](http://www.mongodb.org/) is an open source document-oriented 
  data store with a Binary Object Notation (BSON) storage format that is 
  JSON-style and familiar to web developers. 
  [PyMongo](http://docs.mongodb.org/ecosystem/drivers/python/) is the most
  commonly used client to interface with MongoDB through Python code.

* [Riak](http://basho.com/riak/) is an open source distributed data store
  focused on availability, fault tolerance and large scale deployments.

* [Apache CouchDB](http://couchdb.apache.org/) is also an open source project
  where the focus is on embracing RESTful-style HTTP access for working with 
  stored JSON data.

### Document-oriented data store resources
* [MongoDB for startups](http://www.optinidus.com/blogs/guide-to-mongodb-for-startups/) 
  is a guide about using non-relational databases in green field environments.

* The creator and maintainers of PyMongo review four decisions they regret
  from building the widely-used Python MongoDB driver.
    1. [start\_request](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-start-request/)
    1. [use\_greenlets](http://emptysqua.re/blog/it-seemed-like-a-good-idea-at-the-time-pymongo-use-greenlets/)
    1. ["copy\_database"](http://emptysqua.re/blog/good-idea-at-the-time-pymongo-copy-database/)
    1. The final post will cover MongoReplicaSetClient. 


## Column-family table
A the column-family table class of NoSQL data stores builds on the key-value
pair type. Each key-value pair is considered a row in the store while the
column family is similar to a table in the relational database model.


### Column-family table data stores
* Apache [HBase](https://hbase.apache.org/)

* Apache [Cassandra](http://cassandra.apache.org/)


## Graph
A graph database represents and stores data in three aspects: nodes, edges,
and properties. 

A *node* is an entity, such as a person or business. 

An *edge* is the relationship between two entities. For example, an 
edge could represent that a node for a person entity is an employee of a 
business entity. 

A *property* represents information about nodes. For example, an entity 
representing a person could have a property of "female" or "male".


### Graph data stores
* [Neo4j](http://www.neo4j.org/) is one of the most widely used graph 
  databases and runs on the Java Virtual Machine stack.

* [Cayley](https://github.com/google/cayley) is an open source graph data
  store written by Google primarily written in Go.

* [Titan](http://thinkaurelius.github.io/titan/) is a distributed graph
  database built for multi-node clusters.


### Graph data store resources
* [Introduction to Graph Databases](http://www.slideshare.net/maxdemarzi/introduction-to-graph-databases-12735789)
  covers trends in NoSQL data stores and compares graph databases to other 
  data store types.


## NoSQL third-party services
* [MongoHQ](http://www.mongohq.com/home) provides MongoDB as a service. It's
  easy to set up with either a standard LAMP stack or on Heroku.


## NoSQL data store resources
* [NoSQL databases: an overview](http://www.thoughtworks.com/insights/blog/nosql-databases-overview)
  explains what NoSQL means, how data is stored differently than in
  relational systems and what the Consistency, Availability and 
  Partition-Tolerance (CAP) Theorem means.

* [CAP Theorem overview](http://natishalom.typepad.com/nati_shaloms_blog/2010/10/nocap.html)
  presents the basic constraints all databases must trade off in operation.

* This post on [What is a NoSQL database? Learn By Writing One in Python](http://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/)
  is a detailed article that breaks the mystique behind what some forms
  of NoSQL databases are doing under the covers.

* [NoSQL Weekly](http://www.nosqlweekly.com/) is a free curated email 
  newsletter that aggregates articles, tutorials, and videos about 
  non-relational data stores.

* [NoSQL comparison](http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
  is a large list of popular, BigTable-based, special purpose, and other
  datastores with attributes and the best use cases for each one.



## NoSQL data stores learning checklist
<i class="fa fa-check-square-o"></i>
Understand why NoSQL data stores are better for some use cases than relational
databases. In general these benefits are only seen at large scale so they may
not be applicable to your web application.

<i class="fa fa-check-square-o"></i>
Integrate Redis into your project for a speed boost over slower persistent 
storage. Storing session data in memory is generally much faster than saving
that data in a traditional relational database that uses persistent storage. 
Note that when memory is flushed the data goes away so anything that needs to
be persistent must still be backed up to disk on a regular basis.

<i class="fa fa-check-square-o"></i>
Evaluate other use cases such as storing transient logs in document-oriented
data stores such as MongoDB.


### What's next?
