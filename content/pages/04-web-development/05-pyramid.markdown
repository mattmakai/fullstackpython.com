title: Pyramid
category: page
slug: pyramid
sortorder: 0405
toc: False
sidebartitle: Pyramid
meta: Pyramid is a Python web framework that grew out of the Pylons project. Learn more about Pyramid on Full Stack Python. 


[Pyramid](http://www.pylonsproject.org/projects/pyramid/about) is an open 
source [WSGI](/wsgi-servers.html) web framework based on the 
Model-View-Controller (MVC) architectural pattern.

<a href="http://www.pylonsproject.org/" style="border: none;"><img src="/img/logos/pyramid.jpg" style="border-radius: 5px;" width="100%" alt="Pyramid web framework logo." class="technical-diagram" /></a>


<div class="well see-also">Pyramid is an implementation of the <a href="/web-frameworks.html">web frameworks</a> concept. Learn how these parts fit together in the <a href="/web-development.html">web development</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


### Open source Pyramid example apps
These projects provide solid starting code to learn from as you are building
your own applications.

* [pyramid\_blogr](https://github.com/Pylons/pyramid_blogr) is an example 
  project that shows how to build a blog with Pyramid modeled on the 
  [Flaskr](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial) 
  tutorial.

* [pyramid-blogr-cf](https://github.com/cewing/pyramid-blogr-cf) is another
  Pyramid web app that has a similar title to the one above but this one
  is intended for teaching [web development](/web-development.html) to new
  developers.

* [pyramid\_appengine](https://github.com/twillis/pyramid_appengine)
  provides a project skeleton for running Pyramid on 
  [Google App Engine](/platform-as-a-service.html).


### Pyramid-specific packages
The following packages are designed to make Pyramid play nicely with existing
open source libraries by reducing the boilerplate you need to add to your
project.

* [pyramid_celery](https://github.com/sontek/pyramid_celery) and 
  [pyramid_rq](https://github.com/wichert/pyramid_rq) make it easier 
  to use the [Celery](/celery.html) [task queue](/task-queues.html) in your 
  Pyramid applications for handling asynchronous work.

* [pyramid_zipkin](http://pyramid-zipkin.readthedocs.io/en/latest/) provides
  distributed tracing via the [Zipkin](https://zipkin.io/) library.

* [Ramses](https://ramses.tech/) 
  ([source code](https://github.com/ramses-tech/ramses)) is a RESTful web API
  generation framework, similar in concept (but not in implementation 
  details) to how Django REST Framework works with [Django](/django.html).


### Pyramid resources
Pyramid has fantastic official project documentation on its site. Other
resources are harder to come by compared to other established
[web frameworks](/web-frameworks.html) such as [Django](/django.html) and
[Flask](/flask.html), but there are enough tutorials out there for you to
learn Pyramid if you choose to build your web applications with it.

* [Try Pyramid](https://trypyramid.com/) is the official marketing website for 
  Pyramid, with resources for extending your Pyramid apps. It also provides 
  some sample "hello world!" code.

* [An introduction to the Pyramid web framework for Python](https://opensource.com/article/18/5/pyramid-framework)
  provides a detailed configuration and more than trivial code to
  build a "to do" application. This post is one in a four part series
  that compares Pyramid to [Flask](/flask.html), [Django](/django.html) 
  and Tornado so there is some commentary on how this framework compares
  to the others.

* The [first Pyramid app](http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/firstapp.html)
  is a good place to start getting your hands dirty with an example project.

* Six Feet Up explains why Pyramid is their choice for 
  [rapid development projects](http://www.sixfeetup.com/blog/pyramid-for-rapid-development-projects)
  in that blog post.

* [Build a chat app with Pyramid, SQLDB, and Bluemix](http://www.ibm.com/developerworks/cloud/library/cl-chatapp-bluemix-app/index.html)
  is a Pyramid application walkthrough specific to IBM's Bluemix platform.

* [Developing Web Apps Using the Python Pyramid Framework](https://www.youtube.com/watch?v=kRKOWNdT72A)
  is a video from San Francisco Python with an overview of how to install,
  get started and build a web app with the Pyramid framework.

* This [podcast interview with the primary author of the Pyramid framework](http://www.talkpythontome.com/episodes/show/3/pyramid-web-framework)
  explains how Pyramid sprang from Pylons and how Pyramid compares to other 
  modern frameworks.

* [Anyone using the Pyramid framework?](https://www.reddit.com/r/Python/comments/6yn74i/anyone_using_the_pyramid_framework/)
  is a good /r/Python thread with responses by current users as well as
  frustrations by developers who tried and decided against sticking with
  the framework.
