title: SQLite
category: page
slug: sqlite
sortorder: 0304
toc: False
sidebartitle: SQLite
meta: SQLite is an relational database built into the Python standard library that uses a single file to store data. 


SQLite is an open source [relational database](/databases.html) included with 
the Python standard library as of Python 2.5. The pysqlite database driver 
is also included with the standard library so that no further external 
dependencies are required to access a SQLite database from within Python 
applications.

<img src="/img/logos/sqlite.jpg" class="shot" width="100%" alt="SQLite logo.">

<div class="well see-also">SQLite is an implementation of the <a href="/databases.html">relational database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### Useful SQLite tools and code
SQLite is used in such a wide variety of industries that there are open
source tools and example code for all kinds of edge case uses. Here are 
several tools and bits of code I have found useful while coding my 
applications:

* [sqlitebiter](http://sqlitebiter.readthedocs.io/en/latest/) 
  ([source code](https://github.com/thombashi/sqlitebiter)) is a command-line
  tool for converting various data formats such as comma-separated 
  values (CSV), HTML, Markdown and JSON (among others) into a SQLite database
  file.

* [Scout](http://scout.readthedocs.io/en/latest/)
  ([source code](https://github.com/coleifer/scout))
  is a [Flask](/flask.html)-powered search server for SQLite backends. The
  [introductory post](http://charlesleifer.com/blog/meet-scout-a-search-server-powered-by-sqlite/)
  is really handy for getting started with Scout.

* [Datasette](https://github.com/simonw/datasette) makes it easy to expose
  JSON [APIs](/application-programming-interfaces.html) from your SQLite
  database without coding up a custom web application. Make sure to
  check out the 
  [Datasette getting started guide](https://simonwillison.net/2017/Nov/13/datasette/) 
  as well.

* [SQLite Browser](http://sqlitebrowser.org/) is an open source graphical user 
  interface for working with SQLite.

* The 
  [Membership SQLite SQL scripts](https://github.com/membership/membership.db/tree/master/sqlite)
  provide example code for storing user accounts, roles and authentication 
  tokens in web applications.

* [ExtendsClass](https://extendsclass.com/sqlite-browser.html) is an online SQLite browser.


### SQLite tutorials
It's a good idea to brush up on the basics for using SQLite before you use 
the database in your project through SQL scripts or via an 
[object-relational mapper](/object-relational-mappers-orms.html). These
tutorials will help you get started.

* [A simple step-by-step SQLite tutorial](http://www.blog.pythonlibrary.org/2012/07/18/python-a-simple-step-by-step-sqlite-tutorial/)
  walks through creating databases as well as inserting, updating, querying and
  deleting data.

* [A Minimalist Guide to SQLite](http://tech.marksblogg.com/sqlite3-tutorial-and-guide.html)
  shows how to install SQLite, load data and work with the data stored in
  a new SQLite database.

* [Python SQLite3 Basics](http://nitratine.net/python-sqlite3-basics/) covers
  how to connect to a SQLite database in Python, executing statements,
  committing and retrieving saved values.

* [sqlite3 - embedded relational database](https://pymotw.com/3/sqlite3/) is an
  extensive tutorial showing many of the common create, read, update and delete 
  operations a developer would want to do with SQLite.

* The official 
  [sqlite3 module in the Python stdlib docs](https://docs.python.org/3/library/sqlite3.html)
  contains a bunch of scenarios with code for how to use the database from
  a Python application.

* [Finding bugs in SQLite, the easy way](http://lcamtuf.blogspot.com/2015/04/finding-bugs-in-sqlite-easy-way.html)
  explains how a bug was found - and quickly fixed - in the SQLite codebase.
  It's a great short read which shows that the code is well-tested and 
  maintained.

* [Data Analysis of 8.2 Million Rows with Python and SQLite](https://plot.ly/ipython-notebooks/big-data-analytics-with-pandas-and-sqlite/)
  explains how you can load a large dataset in to SQLite and visualize it
  using the Plotly service.

* [SQLite: The art of keep it simple](http://www.jarchitect.com/Blog/?p=2392)
  uses C code examples from SQLite's codebase to show how its design has been
  kept consistent and tight throughout 15+ years of active development.
  There's also a 
  [great design document on the SQLite site](http://sqlite.org/src4/doc/trunk/www/design.wiki) 
  that covers many of these principles.

* [My list of SQLite resources](http://charlesleifer.com/blog/my-list-of-python-and-sqlite-resources/)
  is a nice roundup of useful tools to use with SQLite and tutorials for
  learning more about the database.

* [Python SQLite3 tutorial](https://www.codementor.io/likegeeks/python-sqlite3-tutorial-database-programming-riqdhwx9z)
  provides another beginner's tutorial using the built-in `sqlite3`
  Python standard library module.

* [A SQLite tutorial with Python](https://stackabuse.com/a-sqlite-tutorial-with-python/)
  covers both SQL and Python code to interact with SQLite.


### Specific SQLite scenarios
These are solid resources if you are looking to solve a particular problem 
you are having with SQLite rather than going through a general tutorial.

* [Let's Build a Simple Database](https://cstack.github.io/db_tutorial/)
  is an *awesome* read where the author re-creates a SQLite-type database
  for learning purposes.

* [We are pretty happy with SQLite & not urgently interested in a fancier DBMS](http://beets.io/blog/sqlite-performance.html)
  gives the rationale behind one development teams' decision to stick to 
  SQLite instead of porting to another relational database such as 
  [MySQL](/mysql.html) or [PostgreSQL](/postgresql.html).

* This overview of SQLite as part of the 
  [Databaseology Lectures](https://www.youtube.com/watch?v=gpxnbly9bz4)
  is amazing because they are given by the creator and he shines a ton
  of light on how SQLite is built and why.

* [How SQLite is tested](https://www.sqlite.org/testing.html) digs into the
  nitty-gritty behind the quality assurance practices for testing potential
  SQLite releases.

* [Using the SQLite JSON1 and FTS5 Extensions with Python](http://charlesleifer.com/blog/using-the-sqlite-json1-and-fts5-extensions-with-python/)
  shows how to compile SQLite 3.9.0+ with json1 and fts5 (full-text search)
  support to use these new features.

* [SQLite with a fine-toothed comb](http://blog.regehr.org/archives/1292)
  digs into the internals of SQLite and shows some bugs found (and 
  since fixed) while the author was researching the SQLite source code.

* [Going Fast with SQLite and Python](http://charlesleifer.com/blog/going-fast-with-sqlite-and-python/)
  shares essential knowledge for working effectively with SQLite in Python,
  particularly when it comes to transactions, concurrency and commits.

* [Extending SQLite with Python](http://charlesleifer.com/blog/extending-sqlite-with-python/)
  uses the [Peewee](/peewee.html)
  [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
  to implement virtual tables and aggregates on top of SQLite.

* [SQLite Database Authorization and Access Control with Python](http://charlesleifer.com/blog/sqlite-database-authorization-and-access-control-with-python/)
  covers how to control access to the SQLite database connection and
  file even though SQLite normally allows unauthorized access by design.

* [Can I read and write to a SQLite database concurrently from multiple connections?](https://stackoverflow.com/questions/10325683/can-i-read-and-write-to-a-sqlite-database-concurrently-from-multiple-connections)
  answers one of the concerns that was an issue in earlier versions of
  SQLite that could have issues if more than one connection was writing
  to the database at one time.

* [Appropriate uses for SQLite](https://sqlite.org/whentouse.html) is an 
  official documentation page that explains what types of applications
  are designed to work well with SQLite as the backend.

* [How to corrupt a SQLite file](https://sqlite.org/howtocorrupt.html) 
  explains how the database file could potentially get corrupted if you
  really work at screwing it up.
