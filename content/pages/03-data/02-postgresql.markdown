title: PostgreSQL
category: page
slug: postgresql
sortorder: 0302
toc: False
sidebartitle: PostgreSQL
meta: PostgreSQL is an open source relational database commonly used with Python applications.


[PostgreSQL](https://www.postgresql.org/), often written as "Postgres" and 
pronounced "Poss-gres", is an open source
[relational database](/databases.html) implementation frequently used by 
Python applications as a backend for data storage and retrieval.

<img src="/img/logos/postgresql.jpg" width="100%" alt="PostgreSQL logo." class="shot">


## How does PostgreSQL fit within the Python stack?
PostgreSQL is the default database choice for many Python developers, 
including the Django team when testing the 
[Django ORM](/object-relational-mappers-orms.html). PostgreSQL is often
viewed as more feature robust and stable when compared to MySQL, SQLServer 
and Oracle. All of those databases are reasonable choices. However, because 
PostgreSQL tends to be used by Python developers the drivers and example
code for using the database tend to be better documented and contain fewer
bugs for typical usage scenarios. If you try to use an Oracle database with
Django, you'll see there is far less example code for that setup compared
to PostgreSQL backend setups.

<div class="well see-also">PostgreSQL is an implementation of the <a href="/databases.html">relational database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Why is PostgreSQL a good database choice?
PostgreSQL's open source license allows developers to operate one or
more databases without licensing cost in their applications. The open 
source license operating model is much less expensive compared to Oracle 
or other proprietary databases, especially as replication and sharding
become necessary at large scale. In addition, because so many people 
ranging from independent developers to multinational organizations use 
PostgreSQL, it's often easier to find developers with PostgreSQL experience 
than other relational databases. There is also 
[ancedotal evidence that PostgreSQL fixes bugs faster than MySQL](https://blog.2ndquadrant.com/postgresql-better-mysql-1/), 
although to be fair there has not been a comprehensive study comparing
how the two projects handle defect resolution.

The PostgreSQL core team also releases frequent updates that greatly enhance 
the database's capabilities. For example, in the 
[PostgreSQL 9.4 release](https://www.postgresql.org/docs/9.4/static/release-9-4.html)
the [jsonb type](https://www.postgresql.org/docs/9.4/static/datatype-json.html)
was added to enhance JavaScript Object Notation ([JSON](http://www.json.org/))
storage capabilities so that in many cases a separate 
[NoSQL database](/no-sql-datastore.html) is not required in an application's
architecture.


## Connecting to PostgreSQL with Python
To work with relational databases in Python you need to use a database 
driver, which is also referred to as a database connector. The most common 
driver library for working with PostgreSQL is 
[psycopg2](https://www.psycopg.org/). There is 
[a list of all drivers on the PostgreSQL wiki](https://wiki.postgresql.org/wiki/Python),
including several libraries that are no longer maintained. If you're
working with the 
[asyncio Python stdlib module](https://docs.python.org/3/library/asyncio.html) 
you should also take a look at the 
[aiopg](https://github.com/aio-libs/aiopg) library which
wraps psycopg2's asychronouos features together.

To abstract the connection between tables and objects, many Python 
developers use an 
[object-relational mapper (ORM)](/object-relational-mappers-orms.html) 
to turn relational data from PostgreSQL into objects that can be used in
their Python application. For example, while PostgreSQL provides a 
relational database and psycopg is the common database connector, there
are many ORMs that can be used with varying web frameworks, as shown in the
table below.

<img src="/img/visuals/postgresql-orm-examples.png" width="100%" alt="Examples of how varying Python ORMs can work with PostgreSQL and the psycopg2 connector." class="technical-diagram" />

Learn more about 
[Python ORMs on that dedicated topic page](/object-relational-mappers-orms.html).


## PostgreSQL data safety
If you're on Linux it's easy to get PostgreSQL installed using a package manager.
However, once the database is installed and running your responsibility is just beginning.
Before you go live with a production application, make sure to:

1. Lock down access with 
   [a whitelist](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html) 
   in the `pg_hba.conf` file 
1. Enable [replication](https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-on-postgresql-on-an-ubuntu-12-04-vps)
   to another database that's preferrably on different infrastructure in 
   a separate location
1. Perform regular 
   [backups and test the restoration process](https://www.postgresql.org/docs/current/backup.html)
1. Ensure your application prevents 
   [SQL injection attacks](https://owasp.org/www-community/attacks/SQL_Injection)

When possible have someone qualified do a 
[PostgreSQL security audit](http://security.stackexchange.com/questions/2517/postgresql-security-audit)
to identify the biggest risks to your database. Small applications and 
bootstrapped companies often cannot afford a full audit in the beginning but
as an application grows over time it becomes a bigger target.

The data stored in your database is the lifeblood of your application. If you have
ever 
[accidentally dropped a production database](https://www.twilio.com/blog/2014/02/introducing-developer-evangelist-matt-makai.html) 
or been the victim of malicious activity such as SQL injection attacks, you'll
know it's far easier to recover when a bit of work has been performed 
beforehand on backups, replication and security measures.


### Python-specific PostgreSQL resources
Many quickstarts and tutorials exist specifically for Django, Flask and 
other web application frameworks. The ones below are some of the best
walkthroughs I've read.

* [Setting up PostgreSQL with Python 3 and psycopg on Ubuntu 16.04](/blog/postgresql-python-3-psycopg2-ubuntu-1604.html)
  provides instructions for getting a fresh Ubuntu install working with 
  PostgreSQL and Python 3.

* This post on 
  [using PostgreSQL with Django or Flask](http://killtheyak.com/use-postgresql-with-django-flask/)
  is a great quickstart guide for either framework.

* This article explains how and why PostgreSQL can handle 
  [full text searching](http://blog.lostpropertyhq.com/postgres-full-text-search-is-good-enough/)
  for many use cases. If you're going down this route, read
  [this blog post that explains how one developer implemented PostgreSQL full text search with SQLAlchemy](http://blog.garage-coding.com/2015/12/18/postgres-fulltext-search.html).

* [django-postgres-copy](http://django-postgres-copy.californiacivicdata.org/en/latest/)
  is a tool for bulk loading data into a PostgreSQL database based on Django models.
  [Say hello to our new open-source software for loading bulk data into PostgreSQL](http://www.californiacivicdata.org/2015/07/17/hello-django-postgres-copy/)
  is an introduction to using the tool in your own projects.

* [How to speed up tests in Django and PostgreSQL](http://nemesisdesign.net/blog/coding/how-to-speed-up-tests-django-postgresql/)
  explains some hacks for making your schema migration-backed run quicker.

* [Thinking psycopg3](https://www.varrazzo.com/blog/2020/03/06/thinking-psycopg3/)
  is written by a developer who has worked on this critical Python library
  for interacting with PostgreSQL since 2005. The author writes up thoughts
  on what should change if backwards-incompatible changes are ever introduced
  in a new hypothetical future version.

* [Records](https://pypi.org/project/records/) is a wrapper around the psycopg2
  driver that allows easy access to direct SQL access. It's worth a look if
  you prefer writing SQL over using an 
  [ORM](/object-relational-mappers-orms.html) like SQLAlchemy.

o [Postgres Joins and Django Querysets](http://lucasroesler.com/2017/02/postgres-joins-and-django-querysets/) 
  is a well done post with a specific example of how a standard 
  Django ORM query can lead to degraded performance due when obtaining
  data from many related tables. The `prefetch_related` command and 
  database performance monitoring tools can help analyze and alleviate
  some of the issues in these unoptimized queries.

* [Loading Google Analytics data to PostgreSQL using Python](https://www.compose.com/articles/loading-google-analytics-data-to-postgresql-using-python/)
  is a quality tutorial that combines [API calls](/api-integration.html)
  with psycopg and PostgreSQL to take data from Google Analytics and save
  it in a PostgreSQL database.

* [1M rows/s from Postgres to Python](https://magic.io/blog/asyncpg-1m-rows-from-postgres-to-python/)
  shows some benchmarks for the performance of the
  [asyncpg](https://github.com/magicstack/asyncpg) Python database client
  and why you may want to consider using it for data transfers.


### General PostgreSQL resources
PostgreSQL tutorials not specific to Python are also really helpful
for properly handling your data.

* [Why PostgreSQL? (5 years later)](http://www.craigkerstiens.com/2017/04/30/why-postgres-five-years-later/)
  covers the improvements that have been made to PostgreSQL over the
  past five years. It's amazing to see how far this project has come and
  how it continues to evolve.

* [The Internals of PostgreSQL](http://www.interdb.jp/pg/) is a book
  that goes into how PostgreSQL works, including core topics such as
  [query processing](http://www.interdb.jp/pg/pgsql03.html), 
  [concurrency control](http://www.interdb.jp/pg/pgsql05.html) and the
  [layout of heap table files](http://www.interdb.jp/pg/pgsql01.html).

* [PostgreSQL Weekly](http://postgresweekly.com/) is a weekly newsletter of
  PostgreSQL content from around the web.

* [My Favorite PostgreSQL Extensions - Part One](https://severalnines.com/database-blog/my-favorite-postgresql-extensions-part-one) 
  and 
  [part two](https://severalnines.com/database-blog/my-favorite-postgresql-extensions-part-two)
  are roundups of useful PostgreSQL extensions that augment the
  standard PostgreSQL functionality.

* [An introduction to PostgreSQL physical storage](http://rachbelaid.com/introduction-to-postgres-physical-storage/)
  provides a solid walkthrough of where PostgreSQL files are located on
  disk, how the files store your data and what mappings are important for
  the underlying database structure. This post is an easy read and well worth
  your time.

* Braintree wrote about their experiences [scaling PostgreSQL](https://www.braintreepayments.com/braintrust/scaling-postgresql-at-braintree-four-years-of-evolution). 
The post is an inside look at the evolution of Braintree's usage of the database.

* There is no such thing as total security but this IBM article covers 
  [hardening a PostgreSQL database](http://www.ibm.com/developerworks/library/os-postgresecurity/). 

* [Handling growth with Postgres](http://instagram-engineering.tumblr.com/post/40781627982/handling-growth-with-postgres-5-tips-from-instagram)
  provides 5 specific tips from Instagram's engineering team on how to scale
  the design of your PostgreSQL database.

* [Inserting And Using A New Record In Postgres](http://rob.conery.io/2015/02/09/inserting-using-new-record-postgres/)
  shows some SQL equivalents to what many developers just do in their ORM
  of choice.

* [Following a Select Statement Through Postgres Internals](http://patshaughnessy.net/2014/10/13/following-a-select-statement-through-postgres-internals)
  provides a fascinating look into the internal workings of PostgreSQL
  during a query.

* [Locating the recovery point just before a dropped table](https://blog.hagander.net/locating-the-recovery-point-just-before-a-dropped-table-230/)
  and 
  [logging transactions that dropped tables](https://blog.hagander.net/logging-transactions-that-dropped-tables-236/)
  are two posts that show you how to recover from an accidentally dropped
  table. In the first post the author shows how recovery is possible with
  recovery points while the second post shows how to put logging in place
  to assist in future recoveries.

* [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres)
  is a list of code libraries, tutorials and newsletters focused 
  specifically on PostgreSQL.

* While you can use a graphical interface for working with PostgreSQL, it's
  best to spend some time getting 
  [comfortable with the command-line interface](http://phili.pe/posts/postgresql-on-the-command-line/).

* Backing up databases is important because data loss can and does happen. 
  This article explains 
  [how to back up a PostgreSQL database hosted on an Amazon Web Services EC2 instance](http://www.n2ws.com/blog/how-to-backup-your-aws-cloud-based-postgresql-database.html)
  if managing your own database on a cloud server is your preferred setup.

* [Is bi-directional replication (BDR) in PostgreSQL transactional?](http://sdf.org/~riley/blog/2016/01/04/is-bi-directional-replication-bdr-in-postgres-transactional/)
  explores a relatively obscure topic with the final result that BDR is
  similar to data stores with eventual consistency rather than consistency
  as a requirement.

* [PostgreSQL-metrics](https://github.com/spotify/postgresql-metrics) is a 
  tool built by Spotify's engineers that extracts and outputs metrics from 
  an existing PostgreSQL database. There's also a way to extend the tools
  to pull custom metrics as well.

* [Creating a Document-Store Hybrid in Postgres 9.5](https://blog.andyet.com/2016/02/04/postgres-9.5-document-store-hybrid/)
  explains how to store and query JSON data, similar to how
  [NoSQL data stores](/no-sql-datastore.html) operate.

* This [slideshow on high availability for web applications](http://thebuild.com/presentations/pgha-fosdem-2016.pdf)
  has a good overview of various database setups common in production
  web applications.

* The 
  [JSONB data type](http://blog.heapanalytics.com/when-to-avoid-jsonb-in-a-postgresql-schema/)
  was introduced in PostgreSQL 9.4 to make it easier to store 
  semi-structured data that previously 
  [NoSQL databases](/no-sql-datastore.html) 
  such as MongoDB covered. However, there are times when using JSONB
  isn't a good idea and 
  [this blog post covers when to avoid the column type](http://blog.heapanalytics.com/when-to-avoid-jsonb-in-a-postgresql-schema/).


### PostgreSQL monitoring and performance
Monitoring one or more PostgreSQL instances and trying to performance tune
them is a rare skillset. Here are some resources to get you started if you
have to handle these issues in your applications.

* This 
  [guide to PostgreSQL monitoring](http://russ.garrett.co.uk/2015/10/02/postgres-monitoring-cheatsheet/)
  is handy for knowing what to measure and how to do it.

* Craig Kerstiens wrote a detailed post about 
  [understanding PostgreSQL performance](http://www.craigkerstiens.com/2012/10/01/understanding-postgres-performance/).

* The [Practical Guide to PostgreSQL Optimizations](https://tech.lendinghome.com/practical-guide-to-postgresql-optimizations-d7b9c2ad6a22)
  covers using cache sizes, restore configurations and shared buffers
  to improve database performance.

* This article on [performance tuning PostgreSQL](http://www.geekytidbits.com/performance-tuning-postgres/)
  shows how to find slow queries, tune indexes and modify your queries
  to run faster.

* [What PostgreSQL tells you about its performance](http://okigiveup.net/what-postgresql-tells-you-about-its-performance/)
  explains how to gather general performance metrics and provides the exact
  queries you should run to get them. The article also covers performance
  monitoring and how to analyze trigger functions.

* [PostgreSQL monitoring queries](https://github.com/nilenso/postgresql-monitoring)
  is a simple GitHub repository of SQL queries that can be run against
  a PostgreSQL instance to determine usage, caching and bloat.

* [PgSQL Indexes and "LIKE"](http://blog.cleverelephant.ca/2016/08/pgsql-text-pattern-ops.html)
  examines why LIKE queries do not take advantage of PostgreSQL indexes
  when the locale is set to something other than the default "C", which is
  for the North American UNIX default. The gist is that you need to
  build a special index to support LIKE whenever you use a locale other
  than "C".

* The [PostgreSQL page on PopSQL](https://popsql.io/learn-sql/postgresql/)
  has a ton of useful syntax snippets categorized by type of action you
  want to perform using SQL.
