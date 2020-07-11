title: SQLAlchemy
category: page
slug: sqlalchemy
sortorder: 0306
toc: False
sidebartitle: SQLAlchemy
meta: SQLAlchemy is a popular Python-based object-relational mapper (ORM) that bridges database relations into objects.


[SQLAlchemy](http://www.sqlalchemy.org/) 
([source code](https://github.com/zzzeek/sqlalchemy)) is a well-regarded 
database toolkit and 
[object-relational mapper (ORM)](/object-relational-mappers-orms.html)
implementation written in Python. SQLAlchemy provides a generalized 
interface for creating and executing database-agnostic code without 
needing to write SQL statements.


<a href="http://www.sqlalchemy.org/"><img src="/img/logos/sqlalchemy.jpg" width="100%" alt="SQLAlchemy logo." class="shot"></a>


## Why is SQLAlchemy a good ORM choice?
SQLAlchemy isn't just an ORM- it also provides SQLAlchemy Core for performing
database work that is abstracted from the implementation differences between 
PostgreSQL, SQLite, etc. In some ways, the ORM is a bonus to Core that
automates commonly-required create, read, update and delete operations.

SQLAlchemy can be used with or without the ORM features. Any given project 
can choose to just use SQLAlchemy Core or both Core and the ORM. The 
following diagram shows a few example configurations with various 
application software stacks and backend databases. Any of these 
configurations can be a valid option depending on what type of application
you are coding.

<img src="/img/visuals/sqlalchemy-orm-example.png" width="100%" alt="Example SQLAlchemy configurations with different web frameworks." class="shot"></a>

A benefit many developers enjoy with SQLAlchemy is that it allows them 
to write Python code in their project to map from the database schema 
to the applications' Python objects. No SQL is required to create, 
maintain and query the database. The mapping allows SQLAlchemy to handle 
the underlying database so developers can work with their Python objects 
instead of writing bridge code to get data in and out of relational tables.

<div class="well see-also">SQLAlchemy is an implementation of the <a href="/object-relational-mappers-orms.html">object-relational mapping (ORM)</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


## How does SQLAlchemy code compare to raw SQL?
Below is an example of a SQLAlchemy model definition from the open source 
[compare-python-web-frameworks project](https://github.com/mattmakai/compare-python-web-frameworks/blob/master/flask_jinja_sqlalchemy/app.py)
that uses SQLAlchemy with Flask and Flask-SQLAlchemy.


    class Contact(db.Model):
        __tablename__ = 'contacts'
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(100))
        last_name = db.Column(db.String(100))
        phone_number = db.Column(db.String(32))

        def __repr__(self):
            return '<Contact {0} {1}: {2}>'.format(self.first_name,
                                                   self.last_name,
                                                   self.phone_number)

SQLAlchemy handles the table creation that otherwise we would have had
to write a create table statement like this one to do the work:
	
    CREATE TABLE CONTACTS(
	   ID INT PRIMARY KEY        NOT NULL,
	   FIRST_NAME     CHAR(100)  NOT NULL,
	   LAST_NAME      CHAR(100)  NOT NULL,
	   PHONE_NUMBER   CHAR(32)   NOT NULL,
	);


By using SQLAlchemy in our Python code, all records can be obtained with a 
line like `contacts = Contact.query.all()` instead of a plain SQL such as 
`SELECT * FROM contacts`. That may not look like much of a difference in
syntax but writing the queries in Python is often faster and easier for
many Python developers once multiple tables and specific filtering on fields 
for queries have to be written. In addition, SQLAlchemy abstracts away
idiosyncratic differences between database implementations in 
[SQLite](/sqlite.html), [MySQL](/mysql.html) and 
[PostgreSQL](/postgresql.html).


### SQLAlchemy Extensions, Plug-ins and Related Libraries
Take a look at the 
[SQLAlchemy extensions, plug-ins and related libraries](/sqlalchemy-extensions-plug-ins-related-libraries.html)
page for a curated list of useful code libraries to use with SQLAlchemy.


### Using SQLAlchemy with Web Frameworks
There is no reason why you cannot use the SQLAlchemy library in any 
application that requires a database backend. However, if you are
building a web app with [Flask](/flask.html), [Bottle](/bottle.html) or 
[another web framework](/other-web-frameworks.html) then take
a look at the following extensions. They provide some glue code along with
helper functions that can reduce the boilerplate code needed to connect
your application's code with the SQLAlchemy library.

* SQLAlchemy is typically used with Flask as the database
  ORM via the [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)
  extension.

* The [bottle-sqlalchemy](https://github.com/iurisilvio/bottle-sqlalchemy)
  extension for [Bottle](/bottle.html) provides a bridge between the standard
  SQLAlchemy library and Bottle. However, from my experience using the library
  it does not have quite as many helper functions as Flask-SQLAlchemy.

* [Pyramid](/pyramid.html) uses the 
  [alchemy scaffold](http://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/database/sqlalchemy.html)
  to make it easy to add SQLAlchemy to a Pyramid web app.

* While [Django](/django.html) does not yet support easy swapping of the 
  default Django backend ORM with SQLAlchemy (like it does for 
  [template engines](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-TEMPLATES)),
  there are hacks for 
  [using SQLAlchemy within Django projects](https://engineering.betterworks.com/2015/09/03/sqlalchemy-and-django/).

* [Morepath](/morepath.html) has easy-to-use support for SQLAlchemy via its
  [more.transaction](http://blog.startifact.com/posts/racing-the-morepath-sqlalchemy-integration.html) 
  module. There is a 
  [morepath-sqlalchemy demo](https://pypi.org/project/morepath-sqlalchemy/)
  that serves as a working example.

* [Merging Django ORM with SQLAlchemy for Easier Data Analysis](https://djangostars.com/blog/merging-django-orm-with-sqlalchemy-for-easier-data-analysis/)
  has details on why, how and when you may want to use SQLAlchemy to
  augment the [Django ORM](/django-orm.html).

* [Building a Simple Birthday App with Flask-SQLAlchemy](https://pybit.es/flask-sqlalchemy-bday-app.html)
  combines SQLAlchemy with Flask to create a birthday reminder application.


### SQLAlchemy resources
The best way to get comfortable with SQLAlchemy is to dig in and write
a database-driven application. The following resources can be helpful if 
you are having trouble getting started or are starting to run into some 
edge cases.

* There is an entire chapter in the 
  [Architecture of Open Source Applications book on SQLAlchemy](http://aosabook.org/en/sqlalchemy.html).
  The content is detailed and well worth reading to understand what is 
  executing under the covers.

* The 
  [SQLAlchemy cheatsheet](https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-sqlalchemy.rst)
  has many examples for querying, generating database metadata and many
  other common (and not so common) operations when working with Core and 
  the ORM.
  
* [10 reasons to love SQLAlchemy](http://pajhome.org.uk/blog/10_reasons_to_love_sqlalchemy.html)
  is a bit of a non-critical lovefest for the code library. However, the
  post makes some good points about the quality of SQLAlchemy's 
  documentation and what a pleasure it can be to use it in a Python project.

* [SQLAlchemy and Django](https://engineering.betterworks.com/2015/09/03/sqlalchemy-and-django/)
  explains how one development team uses the Django ORM for most of their
  standard queries but relies on SQLAlchemy for really advanced queries.

* This
  [SQLAlchemy tutorial](https://overiq.com/sqlalchemy/101/intro-to-sqlalchemy/) provides
  a slew of code examples that cover the basics for working with SQLAlchemy.

* [Implementing User Comments with SQLAlchemy](https://blog.miguelgrinberg.com/post/implementing-user-comments-with-sqlalchemy)
  gives a wonderful walkthrough of how to build your own online commenting
  system in Python using SQLAlchemy.

* [Master SQLAlchemy Relationships in a Performance Friendly Way](https://blog.theodo.com/2020/03/sqlalchemy-relationship-performance/)
  dives into code that shows how to improve performance when setting and 
  accessing relationship-based data in your models.

* [SQLAlchemy and data access in Python](https://talkpython.fm/episodes/show/5/sqlalchemy-and-data-access-in-python)
  is a podcast interview with the creator of SQLAlchemy that covers the
  project's history and how it has evolved over the past decade.

* Most Flask developers use SQLAlchemy as an ORM to relational databases.
  If you're unfamiliar with SQLAlchemy questions will often come up such as
  [what's the difference between flush and commit?](http://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit)
  that are important to understand as you build out your app.

* [SQLAlchemy in batches](https://code.oursky.com/batch-sqlalchemy-generating-top-playlist/)
  shows the code that a popular iOS application runs in background
  batch scripts which uses SQLAlchemy to generate playlists. They provide
  some context and advice for using SQLAlchemy in batch scripts.

* [Getting PostgreSQL transactions under control with SQLAlchemy](http://layer0.authentise.com/getting-postgresql-transactions-under-control-with-sqlalchemy.html)
  provides a quick introduction to the tool 
  [Chryso](https://pypi.org/project/chryso/) that they are working on
  to provide better transaction management in SQLAlchemy connections.


### SQLAlchemy compared to other ORMs
SQLAlchemy is one of many 
[Python object-relational mapper (ORM)](/object-relational-mappers-orms.html)
implementations. Several open source projects and articles are listed here 
to make it a bit easier to understand the differences between these
implementations.

* [Introduction to SQLAlchemy ORM for Django Developers](https://apirobot.me/posts/introduction-to-sqlalchemy-orm-for-django-developers)
  is written by a developer who typically used the [Django ORM](/django-orm.html)
  at work and then had a chance to try SQLAlchemy for one project. He covers
  differences in how each one handles transactions, models and queries.

* [SQLAlchemy vs Other ORMs](http://www.pythoncentral.io/sqlalchemy-vs-orms/)
  provides a detailed comparison of SQLAlchemy against alternatives.

* If you're interested in the differences between SQLAlchemy and the Django
  ORM I recommend reading
  [SQLAlchemy and You](http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/)
  by Armin Ronacher.

* This 
  [GitHub project named PythonORMSleepy](https://github.com/sloria/PythonORMSleepy) 
  implements the same Flask application with several different ORMs:
  SQLAlchemy, Peewee, MongoEngine, stdnet and PonyORM. Looking through the
  code is helpful for understanding the varying approaches each library
  takes to accomplish a similar objective. 

* Quora has several answers to the question of 
  [which is better and why: Django ORM or SQLALchemy](https://www.quora.com/Which-is-better-and-why-Djangos-ORM-or-SQLAlchemy)
  based on various developers' experiences.


## Open source code for learning SQLAlchemy
Many open source projects rely on SQLAlchemy. A great way to learn
how to properly work with this tool is to read the code that shows
how those projects use SQLAlchemy. This section alphabetically lists 
these code examples by class and function in the SQLAlchemy code base.
