Web Framework
=============

:category: page
:slug: web-framework
:sort-order: 07

A web application framework is a collection of libraries that 
provide functionality to accomplish common operations for the web. These
common operations include:

1. URL routing
2. HTML, XML, JSON, and other output templating
3. Database manipulation
4. Cross-site request forgery (CSRF) and Cross-site scripting (XSS) protection

Not all web frameworks include functionality for all of the above 
functionality. Frameworks must balance between "being all things to all
people but very complicated" or doing only certain things well without
prescription for how to do other functions. 

For example, the Django web application framework includes an 
Object-Relational Mapping (ORM) layer that abstracts relational database 
read, write, query, and delete operations. However, the ORM layer in Django
does not work (without modification) on non-relational databases such 
`MongoDB <http://www.mongodb.org/>`_ and `Riak <http://docs.basho.com/>`_.
Other web frameworks such as Flask and Pyramid are generally easier to
use with non-relational databases by incorporating external Python libraries.


Web Framework Monitoring
------------------------
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


Web Framework Resources
-----------------------
`Django <http://www.djangoproject.com/>`_, 
`Flask <http://flask.pocoo.org/>`_,
`Bottle <http://bottlepy.org/docs/dev/>`_,
`Pyramid <http://www.pylonsproject.org/>`_, and
`web.py <http://webpy.org/>`_ are the most common Python web frameworks.
