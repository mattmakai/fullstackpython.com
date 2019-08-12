title: Peewee
category: page
slug: peewee
sortorder: 0307
toc: False
sidebartitle: Peewee
meta: Peewee is a object-relational mapper (ORM) implementation for bridging relational data and Python objects.


[Peewee](http://docs.peewee-orm.com/en/latest/) 
([source code](https://github.com/coleifer/peewee)) is a 
[object-relational mapper (ORM)](/object-relational-mappers-orms.html) 
implementation for bridging data stored in
[relational database tables](/databases.html) with Python objects.

<a href="http://docs.peewee-orm.com/en/latest/"><img src="/img/logos/peewee.png" width="100%" alt="Peewee logo." class="technical-diagram"></a>


## What makes Peewee a useful ORM?
Peewee can be an easier library to wrap your head around than SQLAlchemy
and other ORMs. It is designed to be easier to hack on and understand, 
similar to how [Bottle](/bottle.html) is a smaller, one-file 
[web framework](/web-frameworks.html) compared to the comprehensive 
[Django](/django.html) framework. If you are just getting started with
web development, it may be worth using Peewee for your database mapping
and operations, especially if you use a microframework such as Flask or
Bottle.

Peewee can be used with pretty much any web framework (although using it
with [Django](/django.html) would currently be complicated due to its 
tight built-in ORM coupling) or without a web framework. In the latter 
case Peewee is good for pulling data out of a relational database in a
script or Jupyter notebook. 

Any of the common relational database backends such as 
[PostgreSQL](/postgresql.html), [MySQL](/mysql.html) or 
[SQLite](/sqlite.html) are supported, although a database driver is
still required. The chart below shows a few example configurations
that could use Peewee as an ORM.

<img src="/img/visuals/peewee-orm-example.png" width="100%" alt="Example Peewee configurations with different web frameworks." class="technical-diagram"></a>

<div class="well see-also">Peewee is an implementation of the <a href="/object-relational-mappers-orms.html">object-relational mapping (ORM)</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


## How does Peewee compare to other Python ORMs?
The analogy used by the core Peewee author is that Peewee
is to [SQLAlchemy](/sqlalchemy.html) as [SQLite](/sqlite.html) is to 
[PostgreSQL](/postgresql.html). An 
[ORM](/object-relational-mappers-orms.html) does not have to work for 
every exhaustive use case in order to be useful.



### Peewee resources
Peewee is a much newer library than several other Python ORMs.
For example, Peewee's [first public commit was in 2010](https://github.com/coleifer/peewee/commit/4fd56bd35c27861337861233a7f362474157af57), 
compared to 
[2005 for SQLAlchemy](https://github.com/zzzeek/sqlalchemy/commit/ec052c6a1f1fb0236bd367c510d82f076cb67bc9).
The project is still over five years old though and matured substantially
in development during that time. However, there are typically less resources
and examples available to demonstrate how to use Peewee in your projects
than some other ORMs that have been around for a longer period of time.

Many of the best resources come from the project's author, Charles Leifer,
on his blog and on the official site. There are also hundreds of questions 
answered on the 
[Stack Overflow peewee tag](http://stackoverflow.com/questions/tagged/peewee),
so as usual that can be a rich source of examples for your Peewee-powered
Python applications.

* [An encrypted command-line diary with Python](http://charlesleifer.com/blog/dear-diary-an-encrypted-command-line-diary-with-python/)
  is an awesome walkthrough explaining how to use SQLite, SQLCipher and
  Peewee to create an encrypted file with your contents, diary or otherwise.

* [An Intro to Peewee – Another Python ORM](http://www.blog.pythonlibrary.org/2014/07/17/an-intro-to-peewee-another-python-orm/)
  is a short tutorial that walks through creating a database model mapping,
  adding data, deleting records and querying fields.

* [Introduction to peewee](http://jonathansoma.com/tutorials/webapps/intro-to-peewee/)
  uses an example public dataset, loads it into a [SQLite](/sqlite.html)
  database and shows how to query it using Peewee.

* [Shortcomings in the Django ORM and a look at Peewee](http://charlesleifer.com/blog/shortcomings-in-the-django-orm-and-a-look-at-peewee-a-lightweight-alternative/)
  from the author of the Peewee ORM explains how some of the design
  decisions made in Peewee were in reaction to parts of the Django ORM
  that didn't work so well in practice.

* The [official Peewee quickstart documentation](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html)
  along with the 
  [example Twitter clone app](http://docs.peewee-orm.com/en/latest/peewee/example.html)
  will walk you through the ins and outs of your first couple Peewee-powered
  projects.

* [Flask and Peewee 101](https://benjaminjchapman.wordpress.com/2014/01/14/flask-and-peewee-101/)
  has some basic code for querying with Peewee and populating a drop-down in
  a [Jinja2](/jinja2.html) template. Note that the 
  [Flask-peewee](http://flask-peewee.readthedocs.io/en/latest/) extension
  is no longer maintained, although you do not need to use it to work with
  both Flask and Peewee in an application.

* [How to make a Flask blog in one hour or less](http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/)
  is a well written tutorial that uses the
  [Peewee ORM](https://peewee.readthedocs.org/en/latest/) instead of
  SQLAlchemy for the blog back end.

* These posts on 
  [querying the top item by group with Peewee ORM](http://charlesleifer.com/blog/techniques-for-querying-lists-of-objects-and-determining-the-top-related-item/) 
  and 
  [querying the top N objects per group with Peewee ORM](http://charlesleifer.com/blog/querying-the-top-n-objects-per-group-with-peewee-orm/)
  provide working examples on how to properly query your data via Peewee.

* There was a good discussion in a 
  [Python subreddit thread](https://www.reddit.com/r/Python/comments/4tnqai/choosing_a_python_ormpeewee_vs_sqlalchemy/)
  about the differences between Peewee and SQLAlchemy. Charles Leifer 
  even chimed in to add his own fair assessment of the differences in the
  ORMs.

* [peewee-async](https://peewee-async.readthedocs.io/en/latest/) 
  ([source code](https://github.com/05bit/peewee-async)) is an alpha
  library for using Python 3's 
  [asyncio](https://docs.python.org/3/library/asyncio.html) standard library
  with Peewee. This library is worth watching if you use an async 
  [web framework](/web-frameworks.html) and want to have Peewee serve as your
  application's ORM.

* [Accessing remote MySQL database with peewee](https://stackoverflow.com/questions/16448198/accessing-remote-mysql-database-with-peewee)
  debugs a question where the original author had issues accessing a remote
  [MySQL](/mysql.html) database because they did not properly include the
  `Model` class from 
  [peewee.py](https://github.com/coleifer/peewee/blob/master/peewee.py)
  when instantiating a mapper class.
