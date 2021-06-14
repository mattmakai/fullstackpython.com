title: uWSGI
category: page
slug: uwsgi
sortorder: 0524
toc: False
sidebartitle: uWSGI
meta: uWSGI is a Python WSGI server implementation typically used for running Python web applications.


[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) 
([source code](https://github.com/unbit/uwsgi)), pronounced "mu wiz gee", 
is a [Web Server Gateway Interface (WSGI) server](/wsgi-servers.html)
implementation that is typically used to run Python web applications.

<a href="https://uwsgi-docs.readthedocs.io/en/latest/" style="border: none;"><img src="/img/logos/uwsgi.png" width="100%" alt="Official uWSGI logo." class="shot"></a>


### uWSGI resources
* [Configuring uWSGI for Production Deployment](https://www.techatbloomberg.com/blog/configuring-uwsgi-production-deployment/)
  explains how Bloomberg uses uWSGI as a production WSGI server
  for some of their Python projects and how to set it up for your
  own applications.

* The official [Django](/django.html) framework docs on 
  [how to use Django with uWSGI](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/uwsgi/)
  along with the corresponding official
  [uWSGI Django docs](https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
  are great places to start when you are trying to [deploy](/deployment.html)
  your Django project.

* [The uWSGI Swiss Army Knife](https://lincolnloop.com/blog/uwsgi-swiss-army-knife/)
  examines a few lesser-known uWSGI features that support serving static 
  files, working with SSL, caching and asynchronous task execution.

* [How To Serve Django Applications with uWSGI and Nginx on Debian 8](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-debian-8)
  shows how to set up a [Django](/django.html) web app on Debian Linux that
  uses [Nginx](/nginx.html) as a [web server](/web-servers.html) and reverse 
  proxy for the uWSGI server.

* The official 
  [uWSGI quickstart](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)
  is awesome because it shows you how to code a quick WSGI application without
  using a framework then builds up an example with deploying a traditional 
  Django web app.
