title: PostgreSQL
category: page
slug: postgresql
sort-order: 0505
meta: PostgreSQL is an open source relational database commonly used with Python applications.


# PostgreSQL
[PostgreSQL](http://www.postgresql.org/), often written as "Postgres" and 
pronounced "Poss-gres", is an open source
[relational database](/databases.html) implementation frequently used by 
Python applications as a backed for data storage and retrieval.


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



## Why is PostgreSQL a good database choice?
PostgreSQL's open source license allows developers to operate one or
more databases without licensing cost in their applications. That operating 
model is much less expensive compared to Oracle or other proprietary
databases. In addition, because so many people ranging from independent
developers to multinational organizations use PostgreSQL, it's often easier
to find developers with PostgreSQL experience than other relational databases.

The PostgreSQL core team also releases frequent updates that greatly enhance 
the database's capabilities. For example, in the 
[PostgreSQL 9.4 release](http://www.postgresql.org/docs/9.4/static/release-9-4.html)
the [jsonb type](http://www.postgresql.org/docs/9.4/static/datatype-json.html)
was added to enhance JavaScript Object Notation ([JSON](http://www.json.org/))
storage capabilities so that in many cases a separate 
[NoSQL database](/no-sql-datastore.html) is not required in an application's
architecture.


## Connecting to PostgreSQL with Python
To work with relational databases in Python you need to use a database 
driver, which is also referred to as a database connector. The most common 
driver library for working with PostgreSQL is 
[psycopg2](http://initd.org/psycopg/).

In addition to the database driver, many Python developers use an 
[object-relational mapper (ORM)](/object-relational-mappers-orms.html) with 
to turn relational data from PostgreSQL into objects that can be used in
their Python application. For example, while PostgreSQL provides a 
relational database and psycopg is the common database connector, there
are many ORMs that can be used with varying web frameworks, as shown in the
table below.

<img src="theme/img/postgresql-orm-examples.png" width="100%" alt="Examples of how varying Python ORMs can work with PostgreSQL and the psycopg2 connector." class="technical-diagram" />

Learn more about 
[Python ORMs on that dedicated topic page](/object-relational-mappers-orms.html).


### PostgreSQL resources
* This post on 
  [using PostgreSQL with Django or Flask](http://killtheyak.com/use-postgresql-with-django-flask/)
  is a great quickstart guide for either framework.

* [PostgreSQL: The Nice Bits](https://russ.garrett.co.uk/talks/postgres-gds/) is a 
  good overview slideshow of why PostgreSQL is a great relational database.

* [PostgreSQL Weekly](http://postgresweekly.com/) is a weekly newsletter of
  PostgreSQL content from around the web.

* Braintree wrote about their experiences [scaling PostgreSQL](https://www.braintreepayments.com/braintrust/scaling-postgresql-at-braintree-four-years-of-evolution). 
The post is an inside look at the evolution of Braintree's usage of the database.

* This post estimates the [costs of a PostgreSQL connection](http://hans.io/blog/2014/02/19/postgresql_connection/index.html).

* There is no such thing as total security but this IBM article covers 
  [hardening a PostgreSQL database](http://www.ibm.com/developerworks/library/os-postgresecurity/). 

* Craig Kerstiens wrote a detailed post about [understanding PostgreSQL performance](http://www.craigkerstiens.com/2012/10/01/understanding-postgres-performance/).

* [Handling growth with Postgres](http://instagram-engineering.tumblr.com/post/40781627982/handling-growth-with-postgres-5-tips-from-instagram)
  provides 5 specific tips from Instagram's engineering team on how to scale
  the design of your PostgreSQL database.

* [Inserting And Using A New Record In Postgres](http://rob.conery.io/2015/02/09/inserting-using-new-record-postgres/)
  shows some SQL equivalents to what many developers just do in their ORM
  of choice.

* [Following a Select Statement Through Postgres Internals](http://patshaughnessy.net/2014/10/13/following-a-select-statement-through-postgres-internals)
  provides a fascinating look into the internal workings of PostgreSQL
  during a query.

* This article explains how and why PostgreSQL can handle [full text searching](http://blog.lostpropertyhq.com/postgres-full-text-search-is-good-enough/)
  for many use cases.

* If you're just getting started with PostgreSQL here are 
  [10 beginner tasks you should know how to execute](https://eye.raze.mx/10-beginner-postgresql-tasks-you-should-know/).

* The title's a bit presumptuous but here's a useful list of 
  [7 PostgreSQL data migration hacks you should be using, but aren't](http://engineering.tilt.com/7-postgresql-data-migration-hacks/).

* This guide to 
  [PostgreSQL monitoring](http://russ.garrett.co.uk/2015/10/02/postgres-monitoring-cheatsheet/)
  is handy for knowing what to measure and how to do it.

* While you can use a graphical interface for working with PostgreSQL, it's
  best to spend some time getting 
  [comfortable with the command-line interface](http://phili.pe/posts/postgresql-on-the-command-line/).

* Backing up databases is important because data loss can and does happen. This
  article explains 
  [how to back up a PostgreSQL database hosted on an Amazon Web Services EC2 instance](http://www.n2ws.com/blog/how-to-backup-your-aws-cloud-based-postgresql-database.html)
  if managing your own database on a cloud server is your preferred setup.

* [How to fix undead PostgreSQL queries](https://tech.zalando.com/blog/hack-to-terminate-tcp-conn-postgres/)
  shows a bit of a hack for when what to do when you can't kill certain PostgreSQL
  queries.

* [Is bi-directional replication (BDR) in PostgreSQL transactional?](http://sdf.org/~riley/blog/2016/01/04/is-bi-directional-replication-bdr-in-postgres-transactional/)
  explores a relatively obscure topic with the final result that BDR is
  similar to data stores with eventual consistency rather than consistency
  as a requirement.

* [PostgreSQL-metrics](https://github.com/spotify/postgresql-metrics) is a 
  tool built by Spotify's engineers that extracts and outputs metrics from 
  an existing PostgreSQL database. There's also a way to extend the tools
  to pull custom metrics as well.

