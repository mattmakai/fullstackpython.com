NoSQL Data Stores
=================

:category: page
:slug: no-sql-datastore
:sort-order: 15


Relational databases store the vast majority of web application 
persistent data. However, there are several alternative classifications of 
storage representations.

1. Key-value pair
2. Document-oriented
3. Column-family table
4. Graph

These persistent data storage representations are commonly used to augment,
rather than completely replace, relational databases.

Document-Oriented
-----------------
A document-oriented database provides a semi-structured representation for
nested data. 


Key-Value Pair
--------------
Key-value pair data stores are based
on `hash map <http://en.wikipedia.org/wiki/Hash_table>`_ data structures.


Graph
-----
A graph database represent and store data in three aspects: nodes, edges,
and properties. 

A *node* is an entity, such as a person or business. 

An *edge* is the relationship between two entities. For example, an 
edge could represent that a node for a person entity is an employee of a 
business entity. 

A *property* represents information about nodes. For example, an entity 
representing a person could have a property of "female" or "male".

`Neo4j <http://www.neo4j.org/>`_ is one of the most widely used graph 
databases and runs on the Java Virtual Machine stack.


NoSQL third-party services
--------------------------
`MongoHQ <http://www.mongohq.com/home>`_ provides MongoDB as a service. It's
easy to set up with either a standard LAMP stack or on Heroku.


NoSQL data stores resources
---------------------------
`NoSQL Weekly <http://www.nosqlweekly.com/>`_ is a free curated email 
newsletter that aggregates articles, tutorials, and videos about 
non-relational data stores.



