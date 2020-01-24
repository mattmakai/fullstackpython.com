title: Other Web Frameworks
category: page
slug: other-web-frameworks
sortorder: 0410
toc: False
sidebartitle: Other Web Frameworks
meta: Python has many web frameworks with differing philosophies. Learn more about frameworks on Full Stack Python.


Python has a significant number of newer and less frequently-used 
[web frameworks](/web-frameworks.html) that are still worth your time to 
investigate. The list on this page does not include the following web 
frameworks that have their own dedicated pages:

* [Django](/django.html)

* [Flask](/flask.html)

* [Pyramid](/pyramid.html)

* [TurboGears](/turbogears.html)

* [Bottle](/bottle.html)

* [Falcon](/falcon.html)

* [Morepath](/morepath.html)

* [Sanic](/sanic.html)


## web.py
[web.py](http://webpy.org/) is a Python web framework designed for simplicity
in building web applications.

* See this Reddit discussion on 
  [reasons why to not use web.py](http://www.reddit.com/r/Python/comments/2sjghv/is_there_any_reason_to_not_use_webpy/)
  for some insight into the state of the project.


## web2py
[Web2py](http://www.web2py.com/) is a batteries-included philosophy framework
with project structure based on model-view-controller patterns.


## CherryPy
[CherryPy](http://www.cherrypy.org/) is billed as a minimalist web framework,
from the perspective of the amount of code needed to write a web application
using the framework. The project has a 
[long history](https://w3techs.com/technologies/details/ws-cherrypy/all/all)
and made a major transition between the second and third release.


## Muffin
[Muffin](https://github.com/klen/muffin) is a web framework
built on top of the [asyncio](https://docs.python.org/3/library/asyncio.html)
module in the Python 3.4+ standard library. Muffin takes inspiration from
Flask with URL routes defined as decorators upon view functions. The 
[Peewee ORM](https://peewee.readthedocs.org/en/latest/) is used instead of 
the more common SQLAlchemy ORM.


## Ray
[Ray](https://rayframework.github.io/site/)
is a framework for building RESTful APIs, similar to [Falcon](/falcon.html). 
The [introductory post](https://medium.com/@felipevolpone/ray-a-new-python-web-framework-e5ec9d74bfb4) 
provides some initial code to get started with creating endpoints, adding 
authentication and protecting against malicious clients.


## Vibora
[Vibora](https://vibora.io/) is an asynchronous model framework similar to
[Sanic](/sanic.html) that was inspired by [Flask](/flask.html)'s syntax.
However, the framework's author rewrote many parts like the template engine
to maximize performance.


## Pecan
[Pecan](https://pecan.readthedocs.io/en/latest/index.html) is inspired by
CherryPy and [TurboGears](/turbogears.html). It purely focuses on HTTP
requests and responses via Python objects and does not integrate session
handling or [database](/databases.html) access.


## Masonite

[Masonite](https://docs.masoniteproject.com/) is a modern, developer
centric, batteries-included Python web framework. It uses the MVC
(Model-View-Controller) architecture pattern and comes with a lot of
functionality out of the box with an extremely extendable architecture.

Check out the following resources to learn more:

1. [5 reasons why people are choosing Masonite over Django](https://dev.to/masonite/5-reasons-why-people-are-choosing-masonite-over-django-ic3)
1. [MasoniteCasts](https://masonitecasts.com/)
1. [Dockerizing Masonite with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-masonite-with-postgres-gunicorn-and-nginx/)


## FastAPI

[FastAPI](https://docs.masoniteproject.com/) is a modern,
high-performance, batteries-included Python web framework that's
perfect for building RESTful APIs. It can handle both synchronous and
asynchronous requests and has built-in support for data validation,
JSON serialization, authentication and authorization, and OpenAPI
documentation.


Resources:

1. [Introducing FastAPI](https://medium.com/@tiangolo/introducing-fastapi-fdc1206d453f)
1. [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)
1. [Porting Flask to FastAPI for ML Model Serving](https://www.pluralsight.com/tech-blog/porting-flask-to-fastapi-for-ml-model-serving/)


### Other web framework resources
* This [roundup of 14 minimal Python frameworks](http://codecondo.com/14-minimal-web-frameworks-for-python/)
  contains both familiar and less known Python libraries.

* The [web micro-framework battle](http://www.slideshare.net/r1chardj0n3s/web-microframework-battle/)
  presentation goes over Bottle, Flask, and many other lesser known Python
  web frameworks.

* A Python newcomer asked the Python Subreddit to 
 [explain the differences between numerous Python web frameworks](http://www.reddit.com/r/Python/comments/28qr7c/can_anyone_explain_the_differences_between_web2py/)
 and received some interesting responses from other users.


## Other frameworks learning checklist
1. Read through the web frameworks listed above and check out their project
   websites. 

1. It's useful to know what other web frameworks exist besides Django and 
   Flask. However, when you're just starting to learn to program there are 
   significantly more tutorials and resources for [Django](/django.html) and 
   [Flask](/flask.html) on the web. My recommendation is to start with one of
   those two frameworks then expand your knowledge from there.

