title: Morepath
category: page
slug: morepath
sortorder: 0407
toc: False
sidebartitle: Morepath
meta: Morepath is a Python web framework with a model-driven design approach. Learn more about Morepath on Full Stack Python. 


# Morepath
[Morepath](http://morepath.readthedocs.org/en/latest/) is a micro web 
framework with a model-driven approach to creating web applications and web
APIs.

Morepath's framework philosophy is that the data models should drive the
creation via the web framework. By default the framework routes URLs directly 
to model code, unlike for example Django which requires explicit URL routing
by the developer.


## Why is Morepath an interesting web framework?
Simple [CRUD web applications and APIs](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) 
can be tedious to build when they are driven straight from data models without
much logic between the model and the view. Learn more about how Morepath
[compares with other web frameworks](http://morepath.readthedocs.org/en/latest/compared.html)
from the creator.

With the rise of front end JavaScript frameworks, many Python web frameworks 
are first being used to build 
[RESTful APIs](/application-programming-interfaces.html) that return JSON
instead rendering HTML via a templating system. Morepath appears to have 
been created with the RESTful API model approach in mind and cuts out the 
assumption that templates will drive the user interface.


### Morepath resources
* [On the Morepath](http://blog.startifact.com/posts/on-the-morepath.html)
  is a blog post by Startifact on how they use Morepath and some of the
  features of the framework.

* [A Summer with Morepath](http://blog.stacktrace.ch/post/132538261985)
  describes the author's experience using Morepath, such as how he built
  a framework around Morepath's core functionality. He eventually became
  a core contributor to Morepath based on the application he created.

* [Build a better batching UI with Morepath and Jinja2](http://blog.startifact.com/posts/morepath-batching-example.html)
  is an introductory post on building a simple web application with the 
  framework. The code for the application is also 
  [open source and available on GitHub](https://github.com/morepath/morepath_batching).

* Morepath's creator gave a 
  [great talk on the motivation and structure for the new framework](https://www.youtube.com/watch?v=gyDKMAWPyuY) 
  at EuroPython 2014.

