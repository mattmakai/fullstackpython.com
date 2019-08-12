title: Django Templates
category: page
slug: django-templates
sortorder: 0414
toc: False
sidebartitle: Django Templates
meta: Django has its own template engine referred to as Django templates and is similar to Jinja with some minor differences.


The [Django web framework](/django.html) contains its own 
[template engine](/template-engines.html) for generating HTML, XML and other
output formats.

<a href="https://docs.djangoproject.com/en/dev/topics/templates/" style="border: none;"><img src="/img/logos/django.png" width="100%" alt="Django web framework logo. Trademark Django Software Foundation." style="border-radius: 5px;" width="100%" class="technical-diagram"></a>


## What's the difference between a "project template" and Django templates?
A project template contains the files and code to start a new web application.
For example, when you run `django-admin.py startproject abc`, the Django
admin script creates a new `abc` directory along with several Python 
configuration so the web app can be run by a [WSGI server](/wsgi-servers.html).

Django templates are different from a project template because they live 
within a project and are written by the developer to generate output, most
commonly HTML.

<div class="well see-also">Django templates are an implementation of the <a href="/template-engines.html">template engines</a> concept. Learn more in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


### Django template resources
* [Make ALL Your Django Forms Better](https://www.caktusgroup.com/blog/2018/06/18/make-all-your-django-forms-better/)
  presents some tricks for customizing Django templates to handle
  the widgets on your site.

* [Python Templating Performance Showdown: Django vs Jinja](http://blog.sendwithus.com/python-templating-performance-showdown-django-vs-jinja/)
  provides some benchmarks for how Django templates compare with 
  [Jinja](/jinja2.html) templates. Note that as with any benchmarks
  these only provide a few data points that can be useful rather than
  a definitive statement that one tool is always faster than the other.

* [Reconciling Backend Templates with Frontend Components](https://hackernoon.com/reconciling-djangos-mvc-templates-with-react-components-3aa986cf510a)
  explains how to use React components with the traditional
  server-side Django templates despite some mismatch in how
  each tool approaches the end goal of rendering a webpage.

* [When and how to use Django TemplateView](https://www.agiliq.com/blog/2017/12/when-and-how-use-django-templateview/)
  is not specifically about using the Django template engine, but instead 
  how to use the `TemplateView` in your views which lead directly into 
  rendering a template.
