title: Jinja2
category: page
slug: jinja2
sort-order: 0417
meta: Jinja2 is a template engine written in Python for outputting formats such as HTML and XML.


# Jinja2
Jinja2 is a Python [template engine](/template-engines.html) used to create
HTML, XML or other markup formats that are returned to the user via an
HTTP response.


## Why is Jinja2 useful?
Jinja2 didn't invent the templating concept. In fact, Jinja2's syntax is
inspired by Django's built-in template engine, which was released years
earlier. There were many template engines, such as [JavaServer Pages (JSPs)](https://en.wikipedia.org/wiki/JavaServer_Pages) 

Jinja2 is most useful because it has consistent template tag syntax and the
project is cleanly extracted as 
[an independent open source project](https://github.com/mitsuhiko/jinja2) so
it can be used a dependency by other code libraries.

Jinja2 strikes a thoughtful balance on the template engine spectrum where
on one end you can embed arbitrary code in the templates and the other
end a developer can code whatever she wants.



## What projects depend on Jinja2?
Jinja2 is a commonly-used templating engine for
[web frameworks](/web-frameworks.html) such as [Flask](/flask.html), 
[Bottle](/bottle.html) [Morepath](/morepath.html) and, as of its 1.8 update,
optionally [Django](/django.html) as well. Jinja2 is also used as a template
language by [configuration management](/configuration-management.html) tool 
Ansible and the [static site generator](/static-site-generators.html) Pelican,
among many other similar tools.

The idea is that if a developer already knows Jinja2 from working with one 
project then the exact same syntax and style can be used in another project 
that requires templating. The re-use reduces the learning curve and saves the
open source project author from having to reinvent a new templating style.


### Jinja2 resources
* Real Python has a nice 
  [Jinja2 primer](https://realpython.com/blog/python/primer-on-jinja-templating/)
  with many code examples to show how to use the template engine.

* The [second part of the Flask mega tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates) 
  is all about Jinja2 templates. It walks through control flow, template inheritance
  and other standard features of the engine.

* [Upgrading to Jinja2 Templates in Django 1.8 With Admin](http://jonathanchu.is/posts/upgrading-jinja2-templates-django-18-with-admin/)
  shows how to fix an issue that can occur with Django 1.8 and using Jinja2 as
  the template engine.

* The official 
  [Jinja2 template designer documentation](http://jinja.pocoo.org/docs/dev/templates/)
  is exceptionally useful both as a reference as well as a full read-through
  to understand how to properly work with template tags.
