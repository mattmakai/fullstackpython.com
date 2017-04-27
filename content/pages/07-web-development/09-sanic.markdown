title: Sanic
category: page
slug: sanic
sortorder: 0709
toc: False
sidebartitle: Sanic
meta: Sanic is a Python web framework built with uvloop and designed for fast HTTP responses via asynchronous request handling. 


# Sanic
[Sanic](https://github.com/channelcat/sanic) is a 
[Python web framework](/web-frameworks.html) built on 
[uvloop](https://magic.io/blog/uvloop-blazing-fast-python-networking/) and 
designed for fast HTTP responses via asynchronous request handling. 

<a href="https://github.com/channelcat/sanic" style="border:none"><img src="/img/logos/sanic.png" width="100%" alt="Sanic web framework logo." class="technical-diagram" style="border-radius:6px"></a>


## What are the tradeoffs of using Sanic?
Sanic cannot be developed or deployed on Windows due to its 
necessary [uvloop](https://github.com/MagicStack/uvloop) dependency.

<div class="well see-also">Sanic is an implementation of the <a href="/web-frameworks.html">web framework</a> concept. Learn how these parts fit together in the <a href="/web-development.html">web development</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>

There was 
[an excellent discussion on the /r/python subreddit](https://www.reddit.com/r/Python/comments/5ryiq7/sticking_with_flask_vs_switching_to_one_of_the/) 
about using one of the newer async frameworks such as Sanic or Japronto 
compared with a traditional [web framework](/web-frameworks.html) like 
[Django](/django.html). One of the major tradeoff of adopting a newer
framework is simply that the code library ecosystem has not, and may never,
grow up around that framework. You have to accept the risk that you will
need to build a significant amount of the plumbing yourself rather than
`pip` installing existing, well-tested libraries.


## Sanic tutorials
Sanic is under very active development and is still in its infancy as a
web framework. The following tutorials will get you started but there is
a chance you will have to work through errors as Sanic is regularly updated.

* [Getting started with Sanic: the asynchronous, uvloop based web framework for Python 3.5+](https://www.twilio.com/blog/2016/12/getting-started-with-sanic-the-asynchronous-uvloop-based-web-framework-for-python-3-5.html)
  is a "Hello, World!" style post for the framework and also shows how
  to respond to SMS text messages using [Twilio](/twilio.html).

* [Fixing bugs and handling 186k requests/second using Python](https://hackernoon.com/fixing-bugs-and-handling-186k-requests-second-using-python-2e75d2f9f4f6)
  is a fun benchmarking exercise that a developer ran when testing out 
  Sanic on a Digital Ocean droplet.

* [Exploring Asyncio - uvloop, sanic and motor](http://masnun.rocks/2016/11/17/exploring-asyncio-uvloop-sanic-motor/)
  explains why asyncio is important to the Python community and how
  uvloop & sanic fit into the bigger picture.

* [Python Sanic Tutorial](https://www.youtube.com/watch?v=WiGsWfwh0yY) is a
  video tutorial on how to write your first Sanic web apps.

