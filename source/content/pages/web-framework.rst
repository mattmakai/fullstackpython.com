Web Framework
=============

:category: page
:slug: web-framework
:sort-order: 7

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


