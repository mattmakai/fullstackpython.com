title: Django ORM
category: page
slug: django-orm
sortorder: 0308
toc: False
sidebartitle: Django ORM
meta: Django comes with a default object-relational mapping layer for multiple backends in Python web apps.


The [Django](/django.html) [web framework](/web-frameworks.html) includes
a default 
[object-relational mapping layer (ORM)](/object-relational-mappers-orms.html)
that can be used to interact with application [data](/data.html) from various 
[relational databases](/databases.html) such as [SQLite](/sqlite.html),
[PostgreSQL](/postgresql.html) and [MySQL](/mysql.html).

<a href="https://docs.djangoproject.com/en/dev/topics/db/" style="border: none;"><img src="/img/logos/django.png" width="100%" alt="Official Django logo. Trademark Django Software Foundation." class="shot"></a>


<div class="well see-also">The Django ORM is an implementation of the <a href="/object-relational-mappers-orms.html">object-relational mapping (ORM)</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


### Django ORM resources
The Django ORM has evolved over the past dozen years since it was created
make sure to not only read up on the latest tutorials but also learn about
newer optimizations, such as 
[prefetch_related](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#prefetch-related) 
and
[select_related](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#select-related),
that have been added throughout the project's history.

* [Django models, encapsulation and data integrity](http://www.dabapps.com/blog/django-models-and-encapsulation/)
  is a detailed article by Tom Christie on encapsulating Django models for
  data integrity.

* [Django Debug Toolbar](http://django-debug-toolbar.readthedocs.org/en/1.8/)
  is a powerful Django ORM database query inspection tool. Highly recommended
  during development to ensure you're writing reasonable query code.
  [Django Silk](http://mtford.co.uk/blog/2/) is another inspection tool and
  has capabilities to do more than just SQL inspection.

* [Django QuerySet Examples (with SQL code included)](https://davit.tech/django-queryset-examples/)
  teaches how QuerySets work and shows the corresponding SQL code behind the
  Python code you write to use the ORM.

* [Making a specific Django app faster](http://reinout.vanrees.org/weblog/2014/05/06/making-faster.html)
  is a Django performance blog post with some tips on measuring performance
  and optimizing based on the measured results.

* [Why I Hate the Django ORM](https://speakerdeck.com/alex/why-i-hate-the-django-orm)
  is Alex Gaynor's overview of the bad designs decisions, some of which he
  made, while building the Django ORM.

* [Going Beyond Django ORM with Postgres](https://speakerdeck.com/craigkerstiens/going-beyond-django-orm-with-postgres)
  is specific to using PostgreSQL with Django.

* [How to view Django ORM SQL queries](https://mrcoles.com/how-view-django-orm-sql-queries/)
  along with 
  [django-sql-explorer](https://github.com/groveco/django-sql-explorer)
  allow you to better understand the SQL code that is generated from the 
  Django ORM.

* [Migrating a Django app from MySQL to PostgreSQL](http://www.calazan.com/migrating-django-app-from-mysql-to-postgresql/)
  is a quick look at how to move from MySQL to PostgreSQL. However, my guess
  is that any Django app that's been running for awhile on one
  [relational database](/databases.html) will require a lot more work to
  port over to another backend even with the power of the ORM.

* [Adding basic search to your Django site](https://www.calazan.com/adding-basic-search-to-your-django-site/)
  shows how to write generic queries that'll allow you to provide site
  search via the Django ORM without relying on another tool like
  ElasticSearch. This is great for small sites before you scale them up with
  a more robust search engine.

* The 
  [Django ORM Cookbook](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/)
  provides code recipes for various ways to use the Django ORM to insert and
  query data.

* [How to use Django's Proxy Models](http://benlopatin.com/using-django-proxy-models/)
  is a solid post on a Django ORM concept that doesn't frequently get a lot
  of love or explanation.

* [Tightening Django Admin Logins](http://tech.marksblogg.com/django-admin-logins.html)
  shows you how to log authentication failures, create an IP addresses white
  list and combine fail2ban with the authentication failures list.

* [How to Turn Django Admin Into a Lightweight Dashboard](https://hakibenita.com/how-to-turn-django-admin-into-a-lightweight-dashboard)
  and
  [How to Use Grouping Sets in Django](https://hakibenita.com/how-to-use-grouping-sets-in-django)
  are two great posts on how to add custom features to the Django Admin
  as well as optimize with more advanced SQL when the first attempt
  at the queries get slow due to larger amounts of data.

* [Sorting querysets with NULLs in Django](https://www.isotoma.com/blog/2015/11/23/sorting-querysets-with-nulls-in-django/)
  shows what to do if you're struggling with the common issue of sorting
  columns that contain NULL values.

* [Best Practices working with Django models in Python](http://steelkiwi.com/blog/best-practices-working-django-models-python/)
  has a ton of great advice on proper model naming conventions, quirks to 
  avoid with `ForeignKey` field relationships, handling IDs and many other 
  edge cases that come up when frequently working with Django's ORM.

* [Merging Django ORM with SQLAlchemy for Easier Data Analysis](https://djangostars.com/blog/merging-django-orm-with-sqlalchemy-for-easier-data-analysis/)
  provides rationale for using the [SQLAlchemy](/sqlalchemy.html) ORM
  instead of Django's default ORM in some situations.

* [Working with huge data sets in Django](https://blog.labdigital.nl/working-with-huge-data-sets-in-django-169453bca049)
  explains how to slice the data you retrieve by query into pages and then
  use `prefetch_related` on a subset of the data rather than your whole
  data set.

* [Solving performance problems in the Django ORM](https://medium.com/@hansonkd/performance-problems-in-the-django-orm-1f62b3d04785)
  gives a slew of great code snippets to use with `django.db.connection` so 
  you can discover issues such as unexpected extra queries and problematic 
  key relationships.

* [Full-text search in Django with PostgreSQL](https://www.paulox.net/2017/12/22/full-text-search-in-django-with-postgresql/)
  is a very detailed example that shows how to work specifically with
  a [PostgreSQL](/postgresql.html) backend.

* [Django Anti-Patterns: Signals](https://lincolnloop.com/blog/django-anti-patterns-signals/)
  explains why you should avoid using Django ORM's 
  [signals](https://docs.djangoproject.com/en/dev/topics/signals/) feature
  in your applications if you want to make them easier to maintain.

* [Django ORM optimization story on selecting the least possible](https://www.peterbe.com/plog/django-orm-optimization-story-on-selecting-the-least-possible)
  goes through one developer's Django ORM code refactoring to optimize the
  performance and results of a single query.

* [Fixing your Django async job - database integration](https://spapas.github.io/2019/02/25/django-fix-async-db/)
  is a great article on how to properly integrate the 
  [RQ task queue](/redis-queue-rq.html) with a Django backend.


### Django migrations resources
[Django migrations](https://docs.djangoproject.com/en/dev/topics/migrations/) 
were added in 
[version 1.7](https://docs.djangoproject.com/en/dev/releases/1.7/). Django
projects prior to 1.7 used the 
[South project](https://south.readthedocs.io/en/latest/), which is now 
deprecated and merged into Django. Migrations can be tricky to wrap your
head around as you're getting started with the overall framework but the
following resources should get you past the initial hurdles.

* [Django Migrations - a Primer](https://realpython.com/blog/python/django-migrations-a-primer/)
  takes you through the new migrations system integrated in the Django core as of Django 1.7, looking specifically at a solid workflow that you can use for creating and applying migrations.

* [Django 1.7: Database Migrations Done Right](https://markusholtermann.eu/2014/09/django-17-database-migrations-done-right/)
  explains why South was not directly integrated into Django, how migrations
  are built and shows how backwards migrations work.

* [Executing custom SQL in Django migrations](https://www.endpoint.com/blog/2016/09/17/executing-custom-sql-in-django-migration)
  examines how you can hook in straight SQL that will run during a Django 
  migration.

* [Squashing and optimizing migrations in Django](http://www.rkblog.rk.edu.pl/w/p/squashing-and-optimizing-migrations-django/)
  shows a simple example with code for how to use the migrations integrated
  into Django 1.7.

* [Supporting both Django 1.7 and South](http://treyhunner.com/2014/03/migrating-to-django-1-dot-7/)
  explains the difficulty of supporting Django 1.7 and maintaining South
  migrations for Django 1.6 then goes into how it can be done.

* [Writing unit tests for Django migrations](https://www.caktusgroup.com/blog/2016/02/02/writing-unit-tests-django-migrations/)
  contains a ton of awesome code examples for testing your
  migrations to ensure data migrations work well throughout
  the lifecycle of your Django project.

* [Strategies for reducing memory usage in Django migrations](https://www.azavea.com/blog/2017/02/23/strategies-reducing-memory-usage-django-migrations/)
  shows the large memory usage problem that often occurs with Django 
  migrations at scale and what you can do to mitigate the issue.

* [How to Create Django Data Migrations](https://simpleisbetterthancomplex.com/tutorial/2017/09/26/how-to-create-django-data-migrations.html)
  has a straightforward blog ORM modeling example to show how to perform
  data migration.

* [Keeping data integrity with Django migrations](https://cheesecakelabs.com/blog/keeping-data-integrity-django-migrations/)
  shows two table modification scenarios, one where a column needs to be
  added to an existing table, and another where a `Many-to-Many` field needs
  to be converted to a standard `ForeignKey` column while retaining all
  of the data.

* [Double-checked locking with Django ORM](https://lukeplant.me.uk/blog/posts/double-checked-locking-with-django-orm/)
  shows how you can implement a double-checking locking pattern in the
  Django ORM with [PostgreSQL](/postgresql.html), which is useful
  when you want to prevent multiple processes from accessing the same
  data at the same time.

* [Using Django Check Constraints for the Sum of Percentage Fields](https://adamj.eu/tech/2020/03/10/django-check-constraints-sum-percentage-fields/)
  shows how you can combine several `PositiveIntegerField` model
  fields with a checking constraint and a web form that ensures
  all of the fields sum up to a precise amount, such as 100%.

