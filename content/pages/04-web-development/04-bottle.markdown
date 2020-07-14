title: Bottle
category: page
slug: bottle
sortorder: 0404
toc: False
sidebartitle: Bottle
meta: Bottle is a Python web framework contained within a single source file. Learn more about Bottle on Full Stack Python.


[Bottle](http://bottlepy.org/docs/dev/index.html) 
([source code](https://github.com/bottlepy/bottle)) is a 
[WSGI-compliant](/wsgi-servers.html)
[single source file](https://github.com/defnull/bottle/blob/master/bottle.py)
web framework with no external dependencies other than the Python
[standard library (stdlib)](https://docs.python.org/3/library/).

<a href="http://bottlepy.org/docs/dev/index.html" style="border: none;"><img src="/img/logos/bottle.png" width="100%" alt="Official Bottle logo." class="technical-diagram"></a>


## Should I use Bottle for web development?
Bottle is awesome for a few web development situations:

1. Prototyping ideas 
1. Learning how web frameworks are built
1. Building and running simple personal web applications 


#### Prototyping
Prototyping simple ideas is often easier with Bottle than a more
opinionated web framework like [Django](/django.html) because Django
projects start with a significant amount of boilerplate code. The
[Model-View-Template](https://docs.djangoproject.com/en/3.0/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)
structure for Django apps within projects makes maintaining projects
easier, but it can be cumbersome on starter projects where you're
just playing with random ideas so you aren't worried about your 
application's long-term code structure.


#### Learning about frameworks
Bottle is contained 
[within a single large source file](https://github.com/bottlepy/bottle/blob/master/bottle.py) 
named `bottle.py` so it provides great reading when learning how 
[WSGI](/wsgi-servers.html) web frameworks work. Everything you need to learn 
about how your web application's code connects with the Bottle framework is 
contained within that single source code.


#### Personal projects
Personal projects can be deployed with Bottle as the only dependency.
If you've never performed a [Python web app deployment](/deployment.html)
before, the number of concepts and steps can be daunting. By packaging
`bottle.py` with your app's source code, you can skip some of the
steps to more easily get your web application up and running. 


<div class="well see-also">Bottle is an implementation of the <a href="/web-frameworks.html">web frameworks</a> concept. Learn how these pieces fit together in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Bottle resources
* [Configuring Python 3, Bottle and Gunicorn for Development on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html)
  is a quick tutorial for getting an out-of-the-box default Ubuntu 16.04
  image ready for Bottle development with 
  [Green Unicorn](/green-unicorn-gunicorn.html) as the 
  [WSGI server](/wsgi-servers.html).

* Check out these Full Stack Python Bottle tutorials that'll teach you 
  how to write a few small but very useful Bottle web apps:

    * [Creating Bar Chart Visuals with Bokeh, Bottle and Python 3](/blog/python-bottle-bokeh-bar-charts.html)
    * [Dialing Outbound Phone Calls with a Bottle Web App](/blog/dial-outbound-phone-calls-python-bottle.html)
    * [How to Monitor Python / Bottle Web Apps](/blog/monitor-python-web-applications.html)
    * [Replying to SMS Text Messages with Python and Bottle](/blog/reply-sms-text-messages-python-bottle.html)

* Digital Ocean provides an extensive [introductory post on Bottle](https://www.digitalocean.com/community/articles/how-to-use-the-bottle-micro-framework-to-develop-python-web-apps).

* [First Steps with Python and Bottle](https://www.youtube.com/watch?v=qakG9BYJ1tw&list=PLqrz4nXepkz63z1y4-oHfZHWy11gSoAn0)
  is a quick 4 minute introduction that I created for developers so they
  can get the simplest possible Bottle web app running. There is also a 
  [companion blog post with the code](https://www.twilio.com/blog/2016/11/first-steps-python-bottle-web-framework.html).

* [Getting Started with Python, Bottle and Twilio SMS / MMS](https://www.twilio.com/blog/2016/08/getting-started-python-bottle-twilio-sms-mms.html)
  shows how to build a simple Bottle web application that can send and 
  receive text and picture messages. 
  [How to Make and Receive Phone Calls with Python, Bottle and Twilio Voice](https://www.twilio.com/blog/2016/11/make-receive-phone-calls-python-bottle-twilio-voice.html)
  is a similar beginner's tutorial for handling phone calls with a Bottle
  app using [Twilio](/twilio.html).

* [Developing With Bottle](https://realpython.com/blog/python/developing-with-bottle-part-1/) details how to create a basic application with Bottle.

* The [official Bottle tutorial](http://bottlepy.org/docs/dev/tutorial.html)
  provides a thorough view of basic concepts and features for the framework.

* [Running a Bottle app with Gunicorn](http://blog.yprez.com/running-a-bottle-app-with-gunicorn.html)
  shows how to execute a simple Bottle web app with 
  [Green Unicorn](/green-unicorn-gunicorn.html).

* Here's a short code snippet for
  [creating a RESTful API with Bottle and MongoDB](http://myadventuresincoding.wordpress.com/2011/01/02/creating-a-rest-api-in-python-using-bottle-and-mongodb/).

* [Bottle, full stack without Django](http://www.avelino.xxx/2014/12/bottle-full-stack-without-django)
  does a nice job of connecting SQLAlchemy with Bottle and building an example
  application using the framework.

* [Using bottle.py in Production](http://nongraphical.com/2012/08/using-bottle-py-in-production/)
  has some good tips on deploying a Bottle app to a production environment.

* [Jinja2 Templates and Bottle](http://reliablybroken.com/b/2013/12/jinja2-templates-and-bottle/)
  shows how to use Jinja instead of the built-in templating engine for
  Bottle page rendering.

* [Python patterns](https://taoofmac.com/space/blog/2013/08/11/2300)
  contains a setup that combines Bottle, [Celery](/celery.html) and
  [Peewee](/peewee.html) as the developer's choice for backend 
  [web development](/web-development.html). The developer also uses
  [Vim](/vim.html) as the primary editor for working with Bottle.


## Open source Bottle example projects
* [Pattle](https://github.com/thekad/pasttle) is a pastebin clone built with
  Bottle.

* [Decanter](http://gengo.github.io/decanter/) is a library for structuring
  Bottle projects.

* [compare-python-web-frameworks](https://github.com/mattmakai/compare-python-web-frameworks)
  provides an example application using Bottle as one of the implementations.


## Bottle framework learning checklist
1. [Download Bottle](https://github.com/defnull/bottle/raw/master/bottle.py)
   or install via pip with ``pip install bottle`` on your local development
   machine.

1. Work through the official
   [Bottle tutorial](http://bottlepy.org/docs/dev/tutorial.html).

1. Start coding your Bottle app based on what you learned in the official
   tutorial plus reading open source example applications found above.

1. Move on to the [deployment section](/deployment.html) to get your initial
   Bottle application on the web.

