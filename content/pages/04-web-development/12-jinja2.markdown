title: Jinja2
category: page
slug: jinja2
sortorder: 0412
toc: False
sidebartitle: Jinja2
meta: Jinja2 is a template engine written in Python for outputting formats such as HTML and XML.


Jinja, also commonly referred to as 
"[Jinja2](http://jinja.pocoo.org/docs/dev/)" to specify the newest 
release version, is a Python [template engine](/template-engines.html) 
used to create HTML, XML or other markup formats that are returned to the 
user via an HTTP response.

<a href="http://jinja.pocoo.org/docs/dev/"  style="border: none;"><img src="/img/logos/jinja.png" width="100%" alt="Logo for the Jinja template engine project." style="border-radius: 5px;" width="100%" class="technical-diagram"></a>

## Why is Jinja2 useful?
Jinja2 is useful because it has consistent template tag syntax and the
project is cleanly extracted as 
[an independent open source project](https://github.com/mitsuhiko/jinja2) so
it can be used as a dependency by other code libraries.

<div class="well see-also">Jinja2 is an implementation of the <a href="/template-engines.html">template engines</a> concept. Learn more in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


Jinja2 strikes a thoughtful balance on the template engine spectrum where
on one end you can embed arbitrary code in the templates and the other
end a developer can code whatever she wants.


## Jinja2 origin and development
The first recorded public released of Jinja2 was in 
[2008 with 2.0rc1](http://jinja.pocoo.org/docs/dev/changelog/#version-2-0rc1).
Since then the engine has seen numerous updates and remains in active
development.

Jinja2 engine certainly wasn't the first template engine. In fact, Jinja2's 
syntax is inspired by Django's built-in template engine, which was released 
several years earlier. There were many template systems, such as 
[JavaServer Pages (JSPs)](https://en.wikipedia.org/wiki/JavaServer_Pages),
that originated almost a decade before Jinja2. Jinja2 built upon the concepts
of other template engines and today is widely used by the Python community.


## What projects depend on Jinja2?
Jinja2 is a commonly-used templating engine for
[web frameworks](/web-frameworks.html) such as [Flask](/flask.html), 
[Bottle](/bottle.html), [Morepath](/morepath.html) and, as of its 1.8 update,
optionally [Django](/django.html) as well. Jinja2 is also used as a template
language by [configuration management](/configuration-management.html) tool 
Ansible and the [static site generator](/static-site-generator.html) Pelican,
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

* When you want to use Jinja2 outside of a [web framework](/web-frameworks.html) or 
  other existing tool, here's a 
  [handy quick load function snippet](http://www.pydanny.com/jinja2-quick-load-function.html)
  so the template engine can be easily used from a script or the REPL.

* When working with Jinja2 in combination with LaTeX, some of Jinja2's blocks
  can conflict with LaTeX commands. Check out this post on
  [LaTeX templates with Python and Jinja2 to generate PDFs](http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs)
  to resolve those issues.

* When you use Jinja2 for long enough, eventually you'll want to escape
  large blocks of Jinja2-like text in your templates. To do so, you'll
  need the ["raw" template tag](http://stackoverflow.com/questions/25359898/escape-jinja2-syntax-in-a-jinja2-template).

* [Python Templating Performance Showdown: Django vs Jinja](https://blog.sendwithus.com/python-templating-performance-showdown-django-vs-jinja/)
  puts together some benchmarks for how 
  [Django templates](/django-templates.html) compare with Jinja templates.
  The usual benchmarking caveats apply here but there are some interesting
  tests that examine how the template engines handle large numbers of 
  variables and other factors.

* [Universal Jinja](https://whatisjasongoldstein.com/writing/universal-jinja/)
  presents a high-level overview of what you could do using the Jinja-like
  [Nunchuks library](https://mozilla.github.io/nunjucks/) to perform
  server-side template rendering for Django applications.

