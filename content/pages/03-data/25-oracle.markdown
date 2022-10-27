title: Oracle
category: page
slug: Oracle
sortorder: 0325
toc: False
sidebartitle: Oracle
meta: Oracle Database is an enterprise relational database management system.


[Oracle Database](http://www.oracle.com/) is an enterprise
[relational database](/databases.html). It can run transaction processing, 
data warehousing, and multi-model database workloads such as machine 
learning, spatial, and graph analysis. Recent versions of Oracle Database 
also added support for JSON and blockchain use cases, and the software
can be run in on-premise, cloud or hybrid environments.

<img src="/img/logos/oracle.jpg" width="100%" alt="Oracle logo." class="shot">


## How does Oracle fit with Python?
The Python community and Oracle have a long history. The excellent Python Database API-compliant "cx_Oracle" interface for Oracle Database was first created by the user community in 1998 and is now being enhanced and maintained by Oracle. The [cx_Oracle](https://oracle.github.io/python-cx_Oracle/) module also underpins the [Oracle Machine Learning for Python](https://www.youtube.com/watch?v=P861m__PEMQ) engine. Oracle's high-performance  GraalVM framework supports an implementation of Python called [GraalPython](https://github.com/oracle/graalpython).


## Why is Oracle Database a great choice?
Oracle Database is cross-platform, supporting multiple hardware platforms and various operating systems. Developers and companies of all sizes rely on its proven industry-leading performance, scalability, reliability, and security.
As data volumes rise exponentially, new data types and data models are required to support modern applications. Oracle Database supports the following data types at no extra cost:

*	[JSON](https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/index.html)
*	[Blockchain](https://docs.oracle.com/en/database/oracle/oracle-database/21/nfcon/details-oracle-blockchain-table-282449857.html)
*	[XML](https://www.oracle.com/database/technologies/appdev/xmldb.html)
*	[Object](https://docs.oracle.com/database/121/ADOBJ/adobjint.htm#ADOBJ00101)
*	[Graph](https://www.oracle.com/database/graph/)
*	[Spatial](https://www.oracle.com/database/spatial/)
*	[Time Series](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmcon/time-series.html)
*	Relational

With support for scale-out database clusters, sharded distributed systems, and disaster recovery with continuous application availability, there is no shortage of features to guarantee the Database continues to run uninterrupted 24/7.   

Oracle makes its enterprise-class database readily available to developers with its free on-premises edition Oracle Database XE or on the Oracle public cloud with an Always Free Cloud account.  In addition, Oracle Autonomous Database is a popular choice for developers as no database management or tuning is required, leaving developers to do what they do best – writing code for their applications.  


## Connecting to Oracle Database with Python
As with any database, applications require a connector or driver to connect to the Oracle Database. The Python DB API-compliant [cx_Oracle](https://github.com/oracle/python-cx_Oracle) interface provides developers access to standard and advanced Oracle Database features, such as SQL execution and document storage APIs.  It also gives users access to network traffic encryption capabilities and Oracle's leading high availability features.

[Code examples](https://oracle.github.io/python-cx_Oracle/samples/tutorial/Python-and-Oracle-Database-Scripting-for-the-Future.html) and free workshops such as the introductory [Python and Oracle for Developers Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=766) and a full-stack development workshop using [Python with SQLAlchemy to Oracle Database](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=911&clear=180&session=16650643444916) are available.

<img src="/img/visuals/cx-oracle.jpg" width="100%" alt="cx Oracle driver." class="technical-diagram" />

You can use many Python frameworks and [object-relational mappers (ORMs)](/object-relational-mappers-orms.html) with Oracle Database. ORMs abstract the tables and objects in a relational database to objects that Python developers can manipulate and operate on. [SQLAlchemy](/sqlalchemy.html) and Django are popular ORMs.  SQLAlchemy is used by Pandas, which is very popular with Oracle users.
The table below shows the relationship between web framework, ORM, driver, and the Oracle Database.

<img src="/img/visuals/oracle-orm-examples.png" width="100%" alt="Examples of how varying Python ORMs can work with Oracle and the cx Oracle connector." class="technical-diagram" />

Learn more about
[Python ORMs on that dedicated topic page](/object-relational-mappers-orms.html).

ORMs provide a familiar programming model for Python developers, but sometimes you want that extra performance and operate closer to SQL objects. Oracle cx_Oracle offers several [functions](https://oracle.github.io/python-cx_Oracle/samples/tutorial/Python-and-Oracle-Database-Scripting-for-the-Future.html#binding) to deliver that performance. These functions include fetching data, binding data, executing PL/SQL, operating on LOBs, JSON documents, message passing with Oracle Advanced Queuing, and more.


## Oracle and Data Safety
According to Gartner, Oracle has one of the [highest data safety ratings](https://www.gartner.com/reviews/market/cloud-database-management-systems/vendor/oracle/product/oracle-database) in the industry, with a wide range of features for data protection and high availability. These features include:

*	[Database encryption](https://www.oracle.com/database/technologies/security/advanced-security.html)

*	[Access control to rows](https://www.oracle.com/database/technologies/security/label-security.html) in a table

*	[Database vault](https://www.oracle.com/database/technologies/security/db-vault.html) to restrict privileges and access

*	[Data redaction, subsetting, and masking](https://www.oracle.com/database/technologies/security/data-masking-subsetting.html)

*	All in one data security service in the Oracle Cloud with [Data Safe](https://www.oracle.com/database/technologies/security/data-safe.html)

*	Oracle also provides free tools such as the [Database Assessment Tool (DBSAT)](https://www.oracle.com/database/technologies/security/dbsat.html) to help you identify and remedy potential vulnerabilities.

Oracle also provides numerous data recovery features, including:

*	Backup capabilities with [RMAN](https://www.oracle.com/database/technologies/high-availability/rman.html)

*	Restore point features with [Database Flashback](https://www.oracle.com/database/technologies/high-availability/flashback.html)

*	[Application continuity](https://www.oracle.com/database/technologies/high-availability/app-continuity.html) in the event of database failover to a standby

For an overview of Oracle’s security and high availability architecture, see the following white papers:

*	[Maximum Availability Architecture](https://www.oracle.com/a/tech/docs/maa-onpremises-overview.pdf) (MAA)

*	[Maximum Security Architecture](https://blogs.oracle.com/cloudsecurity/post/oracles-maximum-security-architecture-for-database-security) (MSA)


## Python Specific Oracle Database resources
Many quick starts, tutorials, and workshops exist specifically for Python developers using Oracle Database. Below are some of the best ones to start with.


###Getting Started
If you are looking for a fast way to get started with Python and Oracle Database, check out these two quick start tutorials. These tutorials walk you through installing and setting up the environment you need to connect Python to Oracle Database.

*	[Quick Start: Developing Python Applications for Oracle Database](https://www.oracle.com/database/technologies/appdev/python/quickstartpythononprem.html)

*	[Quick Start: Developing Python Applications for Oracle Autonomous Database](https://www.oracle.com/database/technologies/appdev/python/quickstartpythononprem.html)

Once you have done one of these, then continue with the popular [Python and Oracle Database Tutorial: Scripting for the Future](https://oracle.github.io/python-cx_Oracle/samples/tutorial/Python-and-Oracle-Database-Scripting-for-the-Future.html) to dive deeper to master the Python cx_Oracle interface and see how to build great Oracle Database applications.


###Using Different Frameworks with Oracle
*	[How to Run SQL Queries with Pandas](https://www.oracle.com/news/connect/run-sql-data-queries-with-pandas.html) is a good blog using Pandas for quick and easy data manipulation in Python.

*	[Using Oracle with Pandas in OCI Data Science Notebooks](https://docs.oracle.com/en-us/iaas/tools/ads-sdk/latest/user_guide/loading_data/efficient_use_of_oracle_rdbms_with_ads.html) dives deeper into using Pandas with large datasets in data science applications.

*	[Using SQLAlchemy with Oracle Database](https://docs.sqlalchemy.org/en/14/dialects/oracle.html) provides an excellent toolkit for Python developers using SQLAlchemy as their ORM.

*	[Using Django with Python and Oracle Database](https://www.oracle.com/webfolder/technetwork/tutorials/obe/db/oow10/python_django/python_django.htm) is a tutorial from Oracle and shows the Django Framework with Python to an Oracle Database.

*	[Connecting Pony ORM to the Database](https://docs.ponyorm.org/database.html) is a friendly guide on using Pony with databases.

*	[How to use Python Flask with Oracle Database](https://blogs.oracle.com/opal/post/how-to-use-python-flask-with-oracle-database).

*	[Part 1: Docker for Oracle Database Applications in Node.js and Python](https://blogs.oracle.com/opal/post/part-1-docker-for-oracle-database-applications-in-nodejs-and-python).

*	[Part 2: Docker for Oracle Database Applications in Node.js and Python](https://blogs.oracle.com/opal/post/part-2-docker-for-oracle-database-applications-in-nodejs-and-python).

*	[Faster JSON with Python cx_Oracle and Oracle Database 21’s new OSON storage format](https://blogs.oracle.com/opal/post/faster-json-with-python-cx_oracle-81-and-oracle-database-21s-new-oson-storage-format).


###Workshops
The following hands-on, free workshops provide step-by-step instructions and walkthroughs in a live environment.

*	[Use Python with Oracle Database 19c](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=635&clear=180&session=3484600041895) is an Oracle LiveLabs workshop that shows how to write Python code to connect to and read data from an Oracle Database, including JSON data.

*	[Python and Oracle for Developers](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=766&p210_type=2&session=3484600041895) is an Oracle LiveLabs workshop that explores the features of the Python cx_Oracle interface for Oracle Database, including efficient techniques for connection management and statement handling.

*	[Full Stack Development using Python and deployment via OKE](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=911&clear=180&session=3484600041895) is an Oracle LiveLabs workshop that explores how to build and deploy a simple cloud-native application using the most common frameworks and the Oracle Cloud Infrastructure services.


## Cloud Development with Oracle Database
The following resources are good starting points for those looking to build applications in the Oracle Cloud and deploy applications in Docker containers and Kubernetes.

*	[The Complete Guide To Getting Up And Running With Docker And Kubernetes On The Oracle Cloud](https://blogs.oracle.com/developers/post/the-complete-guide-to-getting-up-and-running-with-docker-and-kubernetes-on-the-oracle-cloud).

*	[Oracle Cloud Blog](https://www.oc-blog.com/) has lots of interesting information on different aspects of Oracle Cloud.

For developers looking to focus on application development in the Oracle Cloud and not have to worry about managing the Oracle Database, the Autonomous Database is a good choice. All management, including patching and upgrades, scalability, and security, are entirely autonomous. The following resources offer you a glimpse of its capabilities.

*	[Julien Dontcheff’s Database Blog](https://juliandontcheff.wordpress.com/category/autonomous/) is a good collection of technical posts with the Autonomous Database.

*	[SQL Maria](https://sqlmaria.com/category/autonomous-database/) also has some excellent posts on all things Oracle Database including Autonomous.

*	[An Introduction to Autonomous Database](https://questoraclecommunity.org/learn/blogs/oracles-autonomous-database-an-introduction/) gives you a good overview.

*	[Autonomous Database for researchers](https://blogs.oracle.com/research/post/a-roadmap-of-oracle-autonomous-database-benefits-for-research) is a good blog with details on some autonomous features.  


##General Oracle Database Resources
Here are some Oracle tutorials and resources not specific to Python that can help you take advantage of the Oracle Database features.

*	[Oracle Technical Architecture](https://www.oracle.com/webfolder/technetwork/tutorials/architecture-diagrams/18/technical-architecture/database-technical-architecture.html) is from Oracle and has nice visuals and short paragraphs on the architecture of the Oracle Database.

*	[Oracle Database Internals](https://databaseinternalmechanism.com/oracle-database-internals/) is an excellent post explaining the architecture of the Oracle Database.

*	This [Oracle Performance Tuning](https://blog.quest.com/oracle-performance-tuning-a-5-step-approach-to-optimized-performance/) blog has a 5-step approach to tuning Oracle.

*	[Oracle RAC](https://databaseinternalmechanism.com/oracle-rac/) is another good post on the concepts of RAC, Oracle’s Real Application Cluster software for database high availability.

*	The [Oracle Database Security](https://www.oracle.com/database/technologies/security.html) web page has lots of information on Oracle’s solutions for security called “defense in depth.”

*	This is a good post on the [Top 5 Reasons to choose Oracle](https://www.dbta.com/Editorial/News-Flashes/Top-5-Reasons-to-Use-an-Oracle-Database-144191.aspx) for a production database.
