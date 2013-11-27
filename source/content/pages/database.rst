Database
========

:category: page
:slug: database
:sort-order: 05

A database is an abstraction on top of an operating system's file system to 
ease creating, reading, updating, and deleting persistent data. The 
abstraction is most commonly represented as a set of relational tables.
Alternative abstractions include graph databases where data is stored in 
both nodes and edges of a graph, as well as key-value pair data stores based
on `hash map <http://en.wikipedia.org/wiki/Hash_table>`_ data structures.

Relational Databases
--------------------
Relational databases store all data in a series of tables. Interconnections
between the tables are specified as *foreign keys*.

Databases storage implementations vary in complexity. SQLite, a database 
included with Python, creates a single file for all data per database. More 
complicated databases such as Oracle, PostgreSQL, and MySQL are more tightly
coupled with the operating system after installation.


Graph Databases
---------------
A graph database represent and store data in three aspects: nodes, edges,
and properties. 

A *node* is an entity, such as a person or business. 

An *edge* is the relationship between two entities. For example, an 
edge could represent that a node for a person entity is an employee of a 
business entity. 

A *property* represents information about nodes. For example, an entity 
representing a person could have a property of "female" or "male".


Database resources
------------------
`DB-Engines <http://db-engines.com/en/ranking>`_ ranks the most popular
database management systems.

`PostgreSQL <http://www.postgresql.org/>`_ and 
`MySQL <http://www.mysql.com/>`_ are two of the most common open source
databases.

`SQLite <http://www.sqlite.org/>`_ is a database that is stored in a single
file on disk. SQLite is built into Python but is only built for access
by a single connection at a time.

