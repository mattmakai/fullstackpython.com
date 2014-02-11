==============
Web Frameworks
==============

:category: page
:slug: web-frameworks
:sort-order: 08

A web application framework is a collection of libraries that 
provide functionality to accomplish common operations for the web. These
common operations include:

1. URL routing
2. HTML, XML, JSON, and other output format templating
3. Database manipulation
4. Security against Cross-site request forgery (CSRF) and other attacks

Not all web frameworks include functionality for all of the above 
functionality. Frameworks fall somewhere between simply executing a 
single use case and attempting to be everything to every developer with
increased complexity. 

For example, the Django web application framework includes an 
Object-Relational Mapping (ORM) layer that abstracts relational database 
read, write, query, and delete operations. However, Django's ORM
cannot work without significant modification on non-relational databases such 
`MongoDB <http://www.mongodb.org/>`_ and `Riak <http://docs.basho.com/>`_.
Other web frameworks such as Flask and Pyramid are generally easier to
use with non-relational databases by incorporating external Python libraries.
There is a spectrum between minimal functionality with easy extensibility and
including everything in the framework with tight integration.

------
Django
------
`Django <http://www.djangoproject.com/>`_ is a widely used Python web 
application framework with a "batteries-included" philosophy. The principle
behind batteries-included is that the common functionality for building
web applications should come with the framework instead of as a separate
library. For example, 
`URL routing <https://docs.djangoproject.com/en/dev/topics/http/urls/>`_, a 
`templating system <https://docs.djangoproject.com/en/dev/topics/templates/>`_,
`object-relational mapper <https://docs.djangoproject.com/en/dev/topics/db/>`_,
and a `database schema migrations <https://docs.djangoproject.com/en/dev/topics/migrations/>`_ 
(as of version 1.7) are all included with the `Django library <https://pypi.python.org/pypi/Django/1.6.2>`_.


Django resources
================
`2 Scoops of Django <http://twoscoopspress.com/products/two-scoops-of-django-1-6>`_ 
by Daniel Greenfield and Audrey Roy is well worth the price of admission if
you're serious about learning how to correctly develop Django websites.


`Effective Django <http://effectivedjango.com/>`_ and 
`Tango with Django <http://www.tangowithdjango.com/book/>`_ are a great free
introductions to using the most popular Python web framework.

DjangoCon US videos from 
`2013 <http://www.youtube.com/user/TheOpenBastion/videos>`_, 
`2012 <http://pyvideo.org/category/23/djangocon-2012>`_, 
`2011 <http://pyvideo.org/category/3/djangocon-2011>`_, as well as  
`earlier US and DjangoCon EU conferences <http://pyvideo.org/category>`_ are
all available free of charge.

The `Django subreddit <http://www.reddit.com/r/django>`_ often has links to
the latest resources for learning Django.

Lincoln Loop wrote a 
`Django Best Practices guide <http://lincolnloop.com/django-best-practices/>`_
for the community.

Steve Losh wrote an incredibly detailed `Django Advice guide <http://stevelosh.com/blog/2011/06/django-advice/>`_.


---------------------
Web Framework Logging
---------------------
Logging is a common mechanism for monitoring web applications written with a
web framework. Runtime exceptions that prevent code from running are 
important to log to investigate and fix the source of the problems. 
Informational and debugging logging also helps to understand how the 
application is performing even if code is working as intended.

Logging is often grouped into several categories:

1. Information
2. Debug
3. Warning
4. Error

Logging errors that occur while a web framework is running is crucial to
understanding how your application is performing. 
`Raven <http://raven.readthedocs.org/en/latest/>`_ is a Python client for the
`Sentry <https://github.com/getsentry/sentry>`_ exception logging and 
aggregation application. Raven provides the way to send exceptions to
Sentry, which should be deployed on a separate server from your production
infrastructure. Raven can also be used by Python scripts to send other
log data to Sentry for aggregation. Sentry provides a clean web application
interface for viewing the exceptions. Sentry can also be configured with a
mail plugin to send emails when exceptions occur.


Web Framework Resources
=======================
`Flask <http://flask.pocoo.org/>`_,
`Bottle <http://bottlepy.org/docs/dev/>`_,
`Pyramid <http://www.pylonsproject.org/>`_, and
`web.py <http://webpy.org/>`_ are the most common Python web frameworks other
than Django.


