title: Django Templates
category: page
slug: django-templates
sortorder: 0715
toc: False
sidebartitle: Django Templates
meta: Django has its own template engine referred to as Django templates and is similar to Jinja with some minor differences.


# Django Templates
The [Django web framework](/django.html) contains its own 
[template engine](/template-engines.html) for generating HTML, XML and other
output formats.

<a href="https://docs.djangoproject.com/en/dev/topics/templates/" style="border: none;"><img src="/source/static/img/logos/django.png" width="100%" alt="Django web framework logo. Trademark Django Software Foundation." style="border-radius: 5px;" width="100%" class="technical-diagram"></a>


## What's the difference between a "project template" and Django templates?
A project template contains the files and code to start a new web application.
For example, when you run `django-admin.py startproject abc`, the Django
admin script creates a new `abc` directory along with several Python 
configuration so the web app can be run by a [WSGI server](/wsgi-servers.html).

Django templates are different from a project template because they live 
within a project and are written by the developer to generate output, most
commonly HTML.

<div class="well see-also">Django templates are an implementation of the <a href="/template-engines.html">template engines</a> concept. Learn more in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>



