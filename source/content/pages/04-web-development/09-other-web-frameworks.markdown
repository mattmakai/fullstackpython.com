title: Other Web Frameworks
category: page
slug: other-web-frameworks
sort-order: 0409
meta: Python has dozens of web frameworks with differing philosophies. Learn more about lesser known frameworks on Full Stack Python.
choice1url: /deployment.html
choice1icon: fa-share fa-inverse
choice1text: How do I deploy a web app once I'm done coding?
choice2url: /web-frameworks.html
choice2icon: fa-code fa-inverse
choice2text: I'd like to go back to reviewing other web frameworks.
choice3url: /cascading-style-sheets.html
choice3icon: fa-css3 fa-inverse
choice3text: How do I style the user interface I built for my web app?
choice4url: /source-control.html
choice4icon: fa-code-fork fa-inverse
choice4text: How can I version and store my source code so I don't lose it?


# Other Web Frameworks
Python has a significant number of web frameworks outside the usual Django,
Flask and Bottle suspects.


## Pyramid
The [Pyramid framework](http://www.pylonsproject.org/) stems from the Pylons
project which develops a set of open source web application frameworks. 
Pyramid applications are built using a model-view-controller architecture.


## TurboGears2
[TurboGears2](http://www.turbogears.org) born as a full stack layer on top
of Pylons is now a standalone web framework that can act both as a full stack
solution (like Django) or as a micro framework.


## Falcon
[Falcon](http://falconframework.org/) is a minimalist web framework designed
with web application speed as a top priority.


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
[long history](http://w3techs.com/technologies/details/ws-cherrypy/all/all) 
and made a major transition between the second and third release. There's an 
[interesting recent discussion](https://groups.google.com/forum/#!msg/cherrypy-users/lT1cxovGyy8/JKCPrE51CXIJ) 
about moving the project forward, especially the number of open outstanding
issues that exist in the tracker.


## Muffin
[Muffin](https://github.com/klen/muffin) is a web framework
built on top of the [asyncio](https://docs.python.org/3/library/asyncio.html)
module in the Python 3.4+ standard library. Muffin takes inspiration from
Flask with URL routes defined as decorators upon view functions. The 
[Peewee ORM](https://peewee.readthedocs.org/en/latest/) is used instead of 
the more common SQLAlchemy ORM.

Muffin has limited documentation, but 
[an example app](https://github.com/klen/muffin/tree/develop/example) 
is bundled with the framework's source code.


## Other web framework resources
* This [roundup of 14 minimal Python frameworks](http://codecondo.com/14-minimal-web-frameworks-for-python/)
  contains both familiar and less known Python libraries.

* The [web micro-framework battle](http://www.slideshare.net/r1chardj0n3s/web-microframework-battle/)
  presentation goes over Bottle, Flask, and many other lesser known Python
  web frameworks.

* A Python newcomer asked the Python Subreddit to 
 [explain the differences between numerous Python web frameworks](http://www.reddit.com/r/Python/comments/28qr7c/can_anyone_explain_the_differences_between_web2py/)
 and received some interesting responses from other users.


## Other frameworks learning checklist
<i class="fa fa-check-square-o"></i> 
Read through the web frameworks listed above and check out their project
websites. 

<i class="fa fa-check-square-o"></i> 
It's useful to know what other web frameworks exist besides Django and Flask.
However, when you're just starting to learn to program there are significantly 
more tutorials and resources for [Django](/django.html) and 
[Flask](/flask.html) on the web. My recommendation is to start with one of
those two frameworks then expand your knowledge from there.


### What do you need to learn next?
