title: Template Engines
category: page
slug: template-engines
sortorder: 0411
toc: False
sidebartitle: Template Engines
meta: Template engines provide programmatic output of formatted string content such as HTML, XML or PDF.


Template engines take in tokenized strings and produce rendered strings with
values in place of the tokens as output. Templates are typically used as
an intermediate format written by developers to programmatically 
produce one or more desired output formats, commonly HTML, XML or PDF.


## Why are template engines important?
Template engines allow developers to generate desired content types, such 
as HTML, while using some of the data and programming constructs such as 
conditionals and for loops to manipulate the output. Template files that are 
created by developers and then processed by the template engine consist of
prewritten markup and template tag blocks where data is inserted.

For example, look at the first ten source lines of HTML of this webpage:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Matt Makai">
  <meta name="description" content="Template engines provide programmatic output of formatted content such as HTML, XML or PDF.">
  <link rel="shortcut icon" href="//static.fullstackpython.com/fsp-fav.png">
```

Every one of the HTML lines above is standard for each page on Full Stack 
Python, with the exception of the `<meta name="description"...` line which 
provides a unique short description of what the individual page contains.

The 
[base.html Jinja template](https://github.com/mattmakai/fullstackpython.com/blob/master/theme/templates/base.html)
used to generate Full Stack Python allows every page on the site to have 
consistent HTML but dynamically generate the pieces that need to change 
between pages when the [static site generator](/static-site-generator.html) 
executes. The below code from the `base.html` template shows that the meta 
description is up to child templates to generate.

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Matt Makai">
  {% block meta_header %}{% endblock %}
  <link rel="shortcut icon" href="//static.fullstackpython.com/fsp-fav.png">
```

In a typical [WSGI application](/wsgi-servers.html), the template engine 
would generate the HTML output response when an HTTP request comes in for a 
particular URL. 


## Python template engines
There are several popular Python template engines. A template engine 
implementation will fall somewhere on the spectrum between allowing 
arbitrary code execution and granting only a limited set of capabilities 
via template tags. A rough visual of the code in template spectrum can be 
seen below for four of the major Python template engines.

<img src="/img/visuals/template-logic-spectrum.png" width="100%" alt="Spectrum between no logic in templates and the ability to run arbitrary code." class="technical-diagram" style="border-radius: 5px;">


### Jinja (Jinja2)
[Jinja](/jinja2.html), also known and referred to as "Jinja2", is a popular 
Python template engine written as a self-contained open source project. Some
template engines, such as [Django templates](/django-templates.html) are 
provided as part of a larger [web framework](/web-frameworks.html), which
can make them difficult to reuse in projects outside their coupled library.

Major Python open source applications such as the 
[configuration management](/configuration-management.html) tools Ansible
and [SaltStack](https://github.com/saltstack/salt)
as well as the [static site generator](/static-site-generator.html) Pelican 
use the Jinja template engine by default for generating output files.

There is a whole lot more to learn about Jinja on the 
[Jinja2 page](/jinja2.html).


### Django templating
Django comes with its 
[own template engine](https://docs.djangoproject.com/en/dev/topics/templates/)
in addition to supporting (as of Django 1.9) drop-in replacement with other
template engines such as Jinja.


### Mako template engine
[Mako](/mako.html) was the default templating engine for the 
Pylons web framework and is one of many template engines supported by 
[Pyramid](/pyramid.html). Mako has wide support as a replacement
template engine for many [other web frameworks](/other-web-frameworks.html)
as well.


### Other Python template engine implementations
There are numerous Python template engine implementations that range from
weekend hacks to actively developed mature libraries. These template
engines are listed alphabetically:

* [Chameleon](https://chameleon.readthedocs.io/en/latest/) is an
  HTML and XML template engine that supports both 
  [Python 2 and 3](/python-2-or-3.html).

* [Cheetah](https://pythonhosted.org/Cheetah/)

* [Diazo](http://docs.diazo.org/en/latest/)

* [evoque](https://pypi.org/project/evoque/)

* [Genshi](https://genshi.edgewall.org/)

* [Juno](https://github.com/breily/juno)

* [Myghty](https://pythonhosted.org/Myghty/whatsitdo.html)

* [pyratemp](https://pypi.org/project/pyratemp/0.3.2)

* [pystache](https://github.com/defunkt/pystache)


### Template engine implementation comparisons
There are many Python template engine implementations in addition to the
ones listed above. These resources can help you select a Python template 
engine implementation that works well for your project.

* This 
  [template engines site](http://www.simple-is-better.org/template/index.html)
  contains a range of information from what templates engines are to listing
  more esoteric Python template engines.

* [Python Template Engine Comparison](http://lucumr.pocoo.org/2008/1/1/python-template-engine-comparison/)
  is an older but still relevant post by the creator of 
  [Jinja](/jinja2.html) that explains why and how he switches between Mako, 
  Jinja and Genshi for various projects he works on. 

* [Python Web Frameworks: What are the advantages and disadvantages of using Mako vs. Jinja2?](https://www.quora.com/Python-Web-Frameworks/Python-Web-Frameworks-What-are-the-advantages-and-disadvantages-of-using-Mako-vs-Jinja2)
  has some good answers from developers on Quora about using Mako compared
  with Jinja2.


### Template engine resources
Template engines are often used with web frameworks a black box where input 
goes in, and rendered text magically appears out the other side. However,
when something unexpected returns from a template engine it is useful to
know how they work to aid your debugging. The following resources examine
existing template engine design as well as how to build your own engine
when that's necessary for your projects.

* [How a template engine works](https://fengsp.github.io/blog/2016/8/how-a-template-engine-works/)
  uses the template module in Tornado as an example to step through how
  a template engine produces output, from parsing the incoming string to
  rendering the final output.

* [A template engine in 500 lines or less](http://aosabook.org/en/500L/a-template-engine.html)
  is an article by [Ned Batchelder](http://nedbatchelder.com/) provides a  
  template engine in 252 lines of Python that can be used to understand how
  template engines work under the cover.

* [The world's simplest Python template engine](https://makina-corpus.com/blog/metier/2016/the-worlds-simplest-python-template-engine)
  shows how the `format()` function can implement a simple template engine
  with conditionals, loops and method invocations.

* [When to use a Templating Engine (in Python)?](http://stackoverflow.com/questions/1030622/when-to-use-a-templating-engine-in-python)
  is a Stack Overflow question with a useful answer on why and when to
  use an existing template engine.

* [Template Engines](http://interactivepython.org/runestone/static/webfundamentals/Frameworks/templates.html)
  uses Jinja as an implementation example to explain the tasks that
  template engines can be used to perform.

* [Approach: Building a toy template engine in Python](http://alexmic.net/building-a-template-engine/)
  walks through how to create your own simple template engine in Python 
  to understand the basics of how most template engines work.
