title: Redis Queue (RQ)
category: page
slug: redis-queue-rq
sortorder: 0429
toc: False
sidebartitle: Redis Queue (RQ)
meta: Redis Queue (RQ) is a Python task queue built on top of Redis that executes work outside an HTTP request-response cycle.


[Redis Queue (RQ)](http://python-rq.org/) is a Python
[task queue](/task-queues.html) implementation that uses Redis to keep
track of tasks in the queue that need to be executed.

<a href="http://python-rq.org/" style="border: none;"><img src="/img/logos/redis-queue.png" width="100%" alt="Redis Queue (RQ) task queue Python project logo." style="border-radius: 5px;" width="100%" class="technical-diagram"></a>

<div class="well see-also">RQ is an implementation of the <a href="/task-queues.html">task queue</a> concept. Learn more in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


### RQ resources
* [Asynchronous Tasks in Python with Redis Queue](https://www.twilio.com/blog/asynchronous-tasks-in-python-with-redis-queue)
  is a quickstart-style tutorial that shows how to use RQ to fetch data 
  from the 
  [Mars Rover web API](https://data.nasa.gov/Space-Science/Mars-Rover-Photos-API/929k-jizu)
  and process URLs for each of the photos taken by NASA's Mars rover.
  There is also a follow-up post on
  [Scheduling Tasks in Python with Redis Queue and RQ Scheduler](https://www.twilio.com/blog/scheduling-tasks-in-python-with-redis-queue-and-rq-scheduler)
  that shows how to schedule tasks in advance, which is a common way of 
  working with [task queues](/task-queues.html).

* The [RQ intro post](http://nvie.com/posts/introducing-rq/) contains
  information on design decisions and how to use RQ in your projects.

* [International Space Station notifications with Python and Redis Queue (RQ)](https://www.twilio.com/blog/2015/11/international-space-station-notifications-with-python-redis-queue-and-twilio-copilot.html)
  shows how to combine the RQ task queue library with Flask to send
  text message notifications every time a condition is met - in this blog
  post's case that the ISS is currently flying over your location on
  Earth.

* [Asynchronous Tasks with Flask and Redis Queue](https://testdriven.io/asynchronous-tasks-with-flask-and-redis-queue)
  looks at how to configure RQ to handle long-running tasks in a Flask app.

* [How We Spotted and Fixed a Performance Degradation in Our Python Code](https://blog.redash.io/how-we-spotted-and-fixed-a-performance-degradation-in-our-python-code/)
  is a quick story about how an engineering team moving from [Celery](/celery.html)
  to RQ fixed some deficiencies in their RQ performance as they started
  to understand the difference between how the two tools execute workers.

* [Flask by Example - Implementing a Redis Task Queue](https://realpython.com/blog/python/flask-by-example-implementing-a-redis-task-queue/)
  explains how to install and use RQ in a [Flask](/flask.html) application.

* [rq-dashboard](https://github.com/eoranged/rq-dashboard) is an awesome
  [Flask](/flask.html)-based dashboard for viewing queues, workers and
  other critical information when using RQ.

* [Sending Confirmation Emails with Flask, Redis Queue, and Amazon SES](https://testdriven.io/sending-confirmation-emails-with-flask-rq-and-ses)
  shows how RQ fits into a real-world application that uses many
  libraries and third party APIs.

* [Background Tasks in Python using Redis Queue](https://timber.io/blog/background-tasks-in-python-using-task-queues/)
  gives a code example for web scraping data from the Goodreads website.
  Note that the first sentence in the post is not accurate: it's not the
  Python language that is linear, but instead the way workers in 
  [WSGI servers](/wsgi-servers.html) handle a single request at a time by
  blocking. Nevertheless, the example is a good one for understanding how
  RQ can execute.
