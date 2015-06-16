title: Object-relational Mappers
category: page
slug: object-relational-mappers-orms
sort-order: 0504
meta: Object-relational mappers (ORMs) provide a bridge between relational databases and object-oriented code. Learn about ORMs on Full Stack Python.


# Object-relational mappers (ORMs)
An object-relational mapper (ORM) is a code library that automates the
transfer of data stored in relational databases tables into objects that
are more commonly used in application code.


## Why are ORMs useful?
ORMs provide a high-level abstraction upon a 
[relational database](/databases.html) that allows a developer to write 
Python code instead of SQL to create, read, update and delete data and
schemas in their database. Developers can use the programming language they 
are comfortable with to work with a database instead of writing SQL 
statements or stored procedures. 

For example, without an ORM a developer would write the following SQL 
statement to retrieve every row in the USERS table where the 
``zip_code`` column is 94107:

    SELECT * FROM USERS WHERE zip_code=94107;


The equivalent Django ORM query would instead look like the following Python
code:

    # obtain everyone in the 94107 zip code and assign to users variable
    users = Users.objects.filter(zip_code=94107)


The ability to write Python code instead of SQL can speed up web application
development, especially at the beginning of a project. The potential 
development speed boost comes from not having to switch from Python code 
into writing declarative paradigm SQL statements. While some software
developers may not mind switching back and forth between languages, it's
typically easier to knock out a prototype or start a web application using
a single programming language.

ORMs also make it theoretically possible to switch an application between
various relational databases. For example, a developer could use SQLite for
local development and MySQL in production. A production application could
be switched from MySQL to PostgreSQL with minimal code modifications. 

In reality however, it's best to use the same database for local development
as is used in production. Otherwise unexpected errors could hit in production
that were not seen in a local development environment. Also, it's rare that
a project would switch from one database in production to another one unless
there was a pressing reason.

<div class="well see-also">
While you're learning about ORMs you should also read up on
<a href="/deployment.html">deployment</a> and check out the
<a href="/application-dependencies.html">application dependencies</a> page.
</div>


## Do I have to use an ORM for my web application?
Python ORM libraries are not required for accessing relational 
databases. In fact, the low-level access is typically provided by another 
library called a *database connector*, such as 
[psycopg](http://initd.org/psycopg/) (for PostgreSQL)
or [MySQL-python](https://pypi.python.org/pypi/MySQL-python/1.2.5) (for 
MySQL). Take a look at the table below which shows how ORMs can work with
different web frameworks and connectors and relational databases.

<img src="theme/img/orm-examples.png" width="100%" alt="Examples of how varying Python ORMs can work with different connectors and backends." class="technical-diagram" />

The above table shows for example that SQLAlchemy can work with or without 
an accompanying web framework as well as varying database connectors. 
Developers can also use ORMs without a web framework, such as when creating 
a data analysis tool or a batch script without a user interface. 


## What are the downsides of using an ORM?
There are numerous downsides of ORMs, including

1. Impedance mismatch
1. Potential for reduced performance
1. Shifting complexity from the database into the application code


### Impedance mismatch
The phrase "impedance mismatch" is commonly used in conjunction with ORMs.
Impedance mismatch is a catch-all term for the difficulties that occur when
moving data between relational tables and application objects. The gist
is that the way a developer uses objects is different from how data is
stored and joined in relational tables.

This article does a solid job of explaing what 
  [ORM impedance mismatch](http://www.agiledata.org/essays/impedanceMismatch.html)
  is at a high level and provides diagrams to visualize why the problem
  occurs. 


### Potential for reduced performance
One of the concerns that's associated with any higher-level abstraction or
framework is potential for reduced performance. With ORMs, the performance
hit comes from the translation of application code into a corresponding SQL 
statement which may not be tuned properly. 

ORMs are also often easy to try but difficult to master. For example, a
beginner using Django might not know about the 
[`select_related()` function](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#select-related) 
or how that can dramatically improve some queries' performance with
foreign key relationships. There are dozens of performance tips and tricks
for every ORM and it's possible that investing time in learning those
quirks may be better spent just learning SQL and how to write stored
procedures.

There's a lot of hand-waving "may or may not" and "potential for" in this
section. In most cases ORMs are good enough for roughly 80-90% of use cases 
and in 10-20% of database interactions there can be major performance 
improvements by having a knowledgeable database adminstrator write tuned
SQL statements to replace the ORM's generated SQL code.


### Shifting complexity from the DB into the app code
The code for working with an application's data has to live somewhere. Before
ORMs were common, database stored procedures were used to encapsulate the
database logic. With an ORM, the data manipulation code instead lives in the 
application's codebase. The addition of data handling code in the codebase
generally isn't an issue with a sound application design, but it does 
increase the total amount of Python code instead of splitting code between 
the application and the database stored procedures.


## Python ORM Implementations
There are numerous ORM implementations written in Python, including
1. [The Django ORM](https://docs.djangoproject.com/en/1.8/topics/db/)
1. [SQLAlchemy](http://www.sqlalchemy.org/)
1. [Peewee](https://peewee.readthedocs.org/en/latest/)
1. [PonyORM](http://ponyorm.com/)
1. [SQLObject](http://sqlobject.org/)

There are several other ORMs, such as Canonical's 
[Storm](https://storm.canonical.com/), but most of them do not appear to
currently be under active development. Learn more about the major ORMs
below.


### Django's ORM
The [Django](/django.html) web framework comes with 
its own built-in object-relational mapping module, generally referred to 
as "the Django ORM" or "Django's ORM".

[Django's ORM](https://docs.djangoproject.com/en/dev/topics/db/) works well
for simple and medium-complexity database operations. However, there are often
complaints that the ORM makes complex queries much more complicated than
writing straight SQL or using [SQLAlchemy](http://www.sqlalchemy.org/). 

It's technically possible to drop down to SQL but it ties the queries to a 
specific database implementation. The ORM is coupled closely with Django so
replacing the default ORM with SQLAlchemy is currently a hack workaround. Note
though that some of the Django core committers believe it is only a matter of
time before the default ORM is replaced with SQLAlchemy. It will be a large
effort to get that working though so it's likely to come in Django 1.9 or 
later.

Since the majority of Django projects are tied to the default ORM, it's best to
read up on advanced use cases and tools for doing your best work within the
existing framework.


### SQLAlchemy
[SQLAlchemy](http://www.sqlalchemy.org/) is 
currently the most respected Python ORM because it typically get the 
abstraction level "just right" and seems to make complex database queries 
easier to write than the Django ORM in most cases. SQLAlchemy is typically 
used with Flask as the database ORM via the 
[Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) 
extension.


### Peewee
[Peewee](https://peewee.readthedocs.org/en/latest/) is a Python ORM 
written to be 
"[simpler, smaller and more hackable](http://charlesleifer.com/blog/the-case-for-peewee-small-hackable-and-fun/)"
than SQLAlchemy. The analogy used by the core Peewee author is that Peewee 
is to SQLAlchemy as SQLite is to PostgreSQL. An ORM does not have to work 
for every exhaustive use case in order to be useful.


### Pony
[Pony ORM](http://ponyorm.com/) is another Python ORM with a slight twist in
its licensing model. The project is multi-licensed. Pony is free for use 
on open source projects but has a 
[commercial license](http://ponyorm.com/license-and-pricing.html) that
is required for commercial projects. The license is a one-time payment 
and does not necessitate a recurring fee.


### SQLObject
[SQLObject](http://sqlobject.org/) is an ORM that has been under active
open source development since 
[before 2003](http://sqlobject.org/News1.html#sqlobject-0-5). 



## Schema migrations
Schema migrations, for example when you need to add a new column to an
existing table in your database, are not technically part of ORMs. However,
since ORMs typically lead to a hands-off approach to the database (at the
developers peril in many cases), libraries to perform schema migrations 
often go hand-in-hand with Python ORM usage on web application projects.

Database schema migrations are a complex topic and deserve their own page. 
For now, we'll lump schema migration resources under ORM links below. 



### General ORM resources
* There's also a detailed overview of [what ORMs are](http://www.agiledata.org/essays/mappingObjects.html)
  on another page of the website.
  
* Martin Fowler addresses the 
  [ORM hate](http://martinfowler.com/bliki/OrmHate.html)
  in an essay about how ORMs are often misused but that they do provide
  benefits to developers.

* If you're confused about the difference between a connector, such as 
  MySQL-python and an ORM like SQLAlchemy, read this 
  [StackOverflow answer](http://stackoverflow.com/questions/2550292/purpose-of-sqlalchemy-over-mysqldb)
  on the topic.


### Django ORM resources
* [Django models, encapsulation and data integrity](http://www.dabapps.com/blog/django-models-and-encapsulation/)
  is a detailed article by Tom Christie on encapsulating Django models for
  data integrity.

* [Django Debug Toolbar](http://django-debug-toolbar.readthedocs.org/en/1.2/) 
  is a powerful Django ORM database query inspection tool. Highly recommended
  during development to ensure you're writing reasonable query code. 
  [Django Silk](http://mtford.co.uk/blog/2/) is another inspection tool and
  has capabilities to do more than just SQL inspection.

* [Making a specific Django app faster](http://reinout.vanrees.org/weblog/2014/05/06/making-faster.html)
  is a Django performance blog post with some tips on measuring performance
  and optimizing based on the measured results.

* [Why I Hate the Django ORM](https://speakerdeck.com/alex/why-i-hate-the-django-orm)
  is Alex Gaynor's overview of the bad designs decisions, some of which he
  made, while building the Django ORM.

* [Going Beyond Django ORM with Postgres](https://speakerdeck.com/craigkerstiens/going-beyond-django-orm-with-postgres)
  is specific to using PostgreSQL with Django.

* [Migrating a Django app from MySQL to PostgreSQL](http://www.calazan.com/migrating-django-app-from-mysql-to-postgresql/)
  is a quick look at how to move from MySQL to PostgreSQL. However, my guess
  is that any Django app that's been running for awhile on one 
  [relational database](/databases.html) will require a lot more work to 
  port over to another backend even with the power of the ORM.

* [Django Model Descriptors](http://blog.kevinastone.com/django-model-descriptors.html)
  discusses and shows how to incorporate business logic into Django models
  to reduce complexity from the views and make the code easier to reuse across
  separate views.

* [Supporting both Django 1.7 and South](http://treyhunner.com/2014/03/migrating-to-django-1-dot-7/)
  explains the difficulty of supporting Django 1.7 and maintaining South 
  migrations for Django 1.6 then goes into how it can be done.

* [Adding basic search to your Django site](https://www.calazan.com/adding-basic-search-to-your-django-site/)
  shows how to write generic queries that'll allow you to provide site 
  search via the Django ORM without relying on another tool like 
  ElasticSearch. This is great for small sites before you scale them up with
  a more robust search engine.

* [How to use Django's Proxy Models](https://www.wellfireinteractive.com/blog/using-django-proxy-models)
  is a solid post on a Django ORM concept that doesn't frequently get a lot
  of love or explanation.

* [Tightening Django Admin Logins](http://tech.marksblogg.com/django-admin-logins.html)
  shows you how to log authentication failures, create an IP addresses white
  list and combine fail2ban with the authentication failures list.

* [Django 1.7: Database Migrations Done Right](https://markusholtermann.eu/2014/09/django-17-database-migrations-done-right/)
  explains why South was not directly integrated into Django, how migrations
  are built and shows how backwards migrations work.

* [Squashing and optimizing migrations in Django](http://www.rkblog.rk.edu.pl/w/p/squashing-and-optimizing-migrations-django/)
  shows a simple example with code for how to use the migrations integrated
  into Django 1.7.


### SQLAlchemy resources
* If you're interested in the differences between SQLAlchemy and the Django
  ORM I highly recommend reading 
  [SQLAlchemy and You](http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/)
  by Armin Ronacher.

* [SQLAlchemy vs Other ORMs](http://www.pythoncentral.io/sqlalchemy-vs-orms/)
  provides a detailed comparison of SQLAlchemy against alternatives.

* Most Flask developers use SQLAlchemy as an ORM to relational databases.
  If you're unfamiliar with SQLAlchemy questions will often come up such as
  [what's the difference between flush and commit?](http://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit)
  that are important to understand as you build out your app.


### Peewee resources
* [Managing database connections with Peewee](http://charlesleifer.com/blog/managing-database-connections-with-peewee/)
  explains the connection pool and ExecutionContext of the ORM.

* [Shortcomings in the Django ORM and a look at Peewee](http://charlesleifer.com/blog/shortcomings-in-the-django-orm-and-a-look-at-peewee-a-lightweight-alternative/)
  from the author of the Peewee ORM explains how some of the design 
  decisions made in Peewee were in reaction to parts of the Django ORM
  that didn't work so well in practice.

* [How to make a Flask blog in one hour or less](http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/)
  is a well written tutorial that uses the 
  [Peewee ORM](https://peewee.readthedocs.org/en/latest/) instead of 
  SQLAlchemy for the blog back end.


### Pony ORM resources
* [Why you should give Pony ORM a chance](http://jakeaustwick.me/why-you-should-give-ponyorm-a-chance/)
  explains some of the benefits of Pony ORM that make it worth trying out.

* [An intro to Pony ORM](http://www.blog.pythonlibrary.org/2014/07/21/python-101-an-intro-to-pony-orm/)
  shows the basics of how to use the library, such as creating databases
  and manipulating data.

* The Pony ORM author explains on a Stack Overflow answer 
  [how Pony ORM works behind the scenes](http://stackoverflow.com/questions/16115713/how-pony-orm-does-its-tricks).
  Worth a read whether or not you're using the ORM just to find out how
  some of the magic coding works.


### SQLObject resources
* This post on 
  [Object-Relational Mapping with SQLObject](http://www.andypatterns.com/index.php/blog/object_relational_mapping_pattern_-_using_sqlobj/) 
  explains the concept behind ORMs and shows the Python code for how they 
  can be used.

* Ian Bicking presented on SQLObject back in 2004 with a talk on
  [SQLObject and Database Programming in Python](http://www.ianbicking.org/docs/sqlobject-presentation/sqlobject-and-database-programming.html).

