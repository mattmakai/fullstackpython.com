title: SQLite
category: page
slug: sqlite
sortorder: 0507
toc: False
sidebartitle: SQLite
meta: SQLite is an relational database built into the Python standard library that uses a single file to store data. 


# SQLite
SQLite is an open source relational database included with the Python standard
library as of Python 2.5. The pysqlite database driver is also included with
the standard library so that no further external dependencies are required to
access a SQLite database from within Python applications.

<img src="/img/sqlite.jpg" width="100%" alt="SQLite logo." class="technical-diagram" />

<div class="well see-also">SQLite is an implementation of the <a href="/databases.html">relational database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### SQLite resources 
* [sqlite3 - embedded relational database](https://pymotw.com/2/sqlite3/) is an
  extensive tutorial showing many of the common create, read, update and delete 
  operations a developer would want to do with SQLite.

* [A simple step-by-step SQLite tutorial](http://www.blog.pythonlibrary.org/2012/07/18/python-a-simple-step-by-step-sqlite-tutorial/)
  walks through creating databases as well as inserting, updating, querying and
  deleting data.

* [My list of SQLite resources](http://charlesleifer.com/blog/my-list-of-python-and-sqlite-resources/)
  is a nice roundup of useful tools to use with SQLite and tutorials for
  learning more about the database.

* [Extending SQLite with Python](http://charlesleifer.com/blog/extending-sqlite-with-python/)
  uses the Peewee 
  [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
  to implement virtual tables and aggregates on top of SQLite.

* [Using SQLite with Flask](http://flask.pocoo.org/docs/0.10/patterns/sqlite3/)
  explains how Flask code can directly query a SQLite database without an ORM.

* [SQLite Browser](http://sqlitebrowser.org/) is an open source graphical user 
  interface for working with SQLite.

* The official 
  [sqlite3 module in the Python stdlib docs](https://docs.python.org/3/library/sqlite3.html)
  contains a bunch of scenarios with code for how to use the database from
  a Python application.

* [Using the SQLite JSON1 and FTS5 Extensions with Python](http://charlesleifer.com/blog/using-the-sqlite-json1-and-fts5-extensions-with-python/)
  shows how to compile SQLite 3.9.0+ with json1 and fts5 (full-text search)
  support to use these new features.


* [SQLite with a fine-toothed comb](http://blog.regehr.org/archives/1292)
  digs into the internals of SQLite and shows some bugs found (and 
  since fixed) while the author was researching the SQLite source code.
