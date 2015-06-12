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
Python code instead of SQL to create, read, update and delete data in
their database. Developers can use the programming language they are
comfortable with, in our case Python, to work with data and not have to
write SQL statements or stored procedures.

However, Python ORM libraries are not required for accessing relational 
databases. In fact, the low-level access is typically provided by another 
library, such as [psycopg](http://initd.org/psycopg/) (for PostgreSQL)
or [MySQL-python](https://pypi.python.org/pypi/MySQL-python/1.2.5) (for 
MySQL).

Developers can also use ORMs without a web framework, such as when
creating a data analysis tool or a batch script without a user interface. 


<div class="well see-also">
While you're learning about ORMs you should also read up on
<a href="/deployment.html">deployment</a> and check out the
<a href="/application-dependencies.html">application dependencies</a> page.
</div>


## What are the downsides of using an ORM?
There are numerous downsides of ORMs, including

1. impedance mismatch
1. difficulty writing complex queries
1. potential for reduced performance
1. shifting complexity into the application from the database layer


## Django's ORM
The [Django](/django.html) web framework comes with its own built-in 
object-relational mapping module, generally referred to as "the Django ORM".

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


## SQLAlchemy
[SQLAlchemy](http://www.sqlalchemy.org/) is currently the most respected 
Python ORM because it typically get the abstraction level "just right" and 
seems to make complex database queries easier to write than the Django ORM 
in most cases. SQLAlchemy is typically used with Flask as the database ORM
via the [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) 
extension.


## Peewee
[Peewee](https://peewee.readthedocs.org/en/latest/) is another Python ORM 
written to be 
[simpler, smaller and more hackable](http://charlesleifer.com/blog/the-case-for-peewee-small-hackable-and-fun/) 
than SQLAlchemy. The analogy used by the core Peewee author is that Peewee 
is to SQLAlchemy as SQLite is to PostgreSQL. An ORM does not have to work 
for every exhaustive use case in order to be useful.


## Schema migrations
Schema migrations, for example when you need to add a new column to an
existing table in your database, are not technically part of ORMs. However,
since ORMs typically lead to a hands-off approach to the database (at the
developers peril in many cases), libraries to perform schema migrations 
often go hand-in-hand with Python ORM usage on web application projects.

Database schema migrations are a complex topic and deserve their own page. 
For now, we'll lump schema migration resources under ORM links below. 



### General ORM resources
* This article does a solid job of explaing what 
  [ORM impedance mismatch](http://www.agiledata.org/essays/impedanceMismatch.html)
  is at a high level and provides diagrams to visualize why the problem
  occurs. There's also a detailed overview of [what ORMs are](http://www.agiledata.org/essays/mappingObjects.html)
  on another page of the website.

* Martin Fowler addresses the 
  [ORM hate](http://martinfowler.com/bliki/OrmHate.html)
  in an essay about how ORMs are often misused but that they do provide
  benefits to developers.


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
