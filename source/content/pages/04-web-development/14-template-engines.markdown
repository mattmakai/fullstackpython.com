title: Template Engines
category: page
slug: template-engines
sortorder: 0414
toc: False
sidebartitle: Template Engines
meta: Template engines provide programmatic output of formatted content such as HTML, XML or PDF.


# Template Engines
Template engines process template files, which provide an intermediate format 
between your Python code and a desired output format, such as HTML or PDF.


## Why are template engines important?
Template engines allow developers to generate a desired content type, such 
as HTML, while using some of the data and programming constructs such as 
conditionals and for loops to manipulate the output. Template files that are 
created by developers and then processed by the template engine consist of
prewritten markup and template tag blocks where data is inserted.

For example, look at the first ten source lines of HTML of this webpage:

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

Every one of the HTML lines above is standard for each page on Full Stack Python,
with the exception of the `<meta name="description"...` line which provides
a unique short description of what the individual page contains.

The [base.html Jinja template](https://github.com/makaimc/fullstackpython.com/blob/gh-pages/source/theme/templates/base.html) used to generate Full Stack Python
allows every page on the site to have consistent HTML but 
dynamically generate the pieces that need to change between pages when 
the [static site generator](/static-site-generator.html) executes. The below
code from the `base.html` template shows that the meta description is up to child 
templates to create.

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


In a typical [WSGI application](/wsgi-servers.html), the template engine would 
generate the HTML output response when an HTTP request comes in for a 
particular URL. 


## Python template engines
There are several popular Python template engines. A template engine implementation 
will fall somewhere on the spectrum between allowing arbitrary code execution and 
granting only a limited set of capabilities via template tags. A rough visual of
the code in template spectrum can be seen below for four of the major Python
template engines.

<img src="/img/template-logic-spectrum.png" width="100%" alt="Spectrum between no logic in templates and the ability to run arbitrary code." class="technical-diagram" style="border-radius: 5px;">



### Jinja
[Jinja](http://jinja.pocoo.org/), also known as "Jinja2", is a popular Python 
template engine written as an independent open source project, unlike some
template engines that are provided as part of a larger web framework.

Major Python open source applications such as the 
[configuration management](/configuration-management.html) tools Ansible
and [SaltStack](https://github.com/saltstack/salt)
as well as the [static site generator](/static-site-generator.html) Pelican use
the Jinja template engine by default for generating output files.

There's a whole lot more to learn about Jinja on the [Jinja2](/jinja2.html) page.


### Django templating
Django comes with its 
[own template engine](https://docs.djangoproject.com/en/dev/topics/templates/)
in addition to supporting (as of Django 1.9) drop-in replacement with other
template engines such as Jinja.


### Mako
[Mako](http://www.makotemplates.org/) is the default templating engine for
the [Pyramid web framework](/pyramid.html) and has wide support as a replacement
template engine for many [other web frameworks](/other-web-frameworks.html).


### Template engine resources
* [A template engine in 500 lines or less](http://aosabook.org/en/500L/a-template-engine.html)
  is an article by [Ned Batchelder](http://nedbatchelder.com/) provides a  
  template engine in 252 lines of Python that can be used to understand how
  template engines work under the cover.

* [A Primer on Jinja Templating](https://realpython.com/blog/python/primer-on-jinja-templating/)
  shows how to use the major parts of this fantastic template engine.

* [Template fragment gotchas](http://agiliq.com/blog/2015/08/template-fragment-caching-gotchas/) 
  is a collection of situations that can trip up a developer or designer when
  working with templates.

* This 
  [template engines site](http://www.simple-is-better.org/template/index.html)
  contains a range of information from what templates engines are to listing
  more esoteric Python template engines.
