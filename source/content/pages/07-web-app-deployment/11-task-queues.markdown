title: Task Queues
category: page
slug: task-queues
sortorder: 0711
toc: False
sidebartitle: Task Queues
meta: Task queues handle asynchronous jobs outside a Python web application HTTP request-response cycle.


# Task queues
Task queues manage background work that must be executed outside the usual
HTTP request-response cycle.


## Why are task queues necessary?
Tasks are handled asynchronously either because they are not initiated by 
an HTTP request or because they are long-running jobs that would dramatically
reduce the performance of an HTTP response.

For example, a web application could poll the GitHub API every 10 minutes to
collect the names of the top 100 starred repositories. A task queue would
handle invoking code to call the GitHub API, process the results and store them
in a persistent database for later use.

Another example is when a database query would take too long during the HTTP
request-response cycle. The query could be performed in the background on a
fixed interval with the results stored in the database. When an
HTTP request comes in that needs those results a query would simply fetch the
precalculated result instead of re-executing the longer query.
This precalculation scenario is a form of [caching](/caching.html) enabled 
by task queues.

Other types of jobs for task queues include

* spreading out large numbers of independent database inserts over time 
  instead of inserting everything at once

* aggregating collected data values on a fixed interval, such as every
  15 minutes

* scheduling periodic jobs such as batch processes


## Task queue projects
The defacto standard Python task queue is Celery. The other task queue 
projects that arise tend to come from the perspective that Celery is overly
complicated for simple use cases. My recommendation is to put the effort into
Celery's reasonable learning curve as it is worth the time it takes to 
understand how to use the project.

* The [Celery](http://www.celeryproject.org/) distributed task queue is the
  most commonly used Python library for handling asynchronous tasks and 
  scheduling.

* The [RQ (Redis Queue)](http://python-rq.org/) is a simple Python
  library for queueing jobs and processing them in the background with workers.
  RQ is backed by Redis and is designed to have a low barrier to entry.
  The [intro post](http://nvie.com/posts/introducing-rq/) contains information
  on design decisions and how to use RQ.

* [Taskmaster](https://github.com/dcramer/taskmaster) is a lightweight simple
  distributed queue for handling large volumes of one-off tasks. 

* [Huey](http://huey.readthedocs.org/en/latest/) is a simple task queue that
  uses Redis on the backend but otherwise does not depend on other libraries. 
  The project was previously known as Invoker and the author changed the name.

* [Huey](http://huey.readthedocs.org/en/latest/) is a Redis-based task 
  queue that aims to provide a simple, yet flexible framework for 
  executing tasks. Huey supports task scheduling, crontab-like repeating 
  tasks, result storage and automatic retry in the event of failure.


## Hosted message and task queue services
Task queue third party services aim to solve the complexity issues that arise
when scaling out a large deployment of distributed task queues.

* [Iron.io](http://www.iron.io/) is a distributed messaging service platform 
  that works with many types of task queues such as Celery. It also is built
  to work with other IaaS and PaaS environments such as Amazon Web Services
  and Heroku.

* [Amazon Simple Queue Service (SQS)](http://aws.amazon.com/sqs/) is a
  set of five APIs for creating, sending, receiving, modifying and deleting
  messages.

* [CloudAMQP](http://www.cloudamqp.com/) is at its core managed servers with
  RabbitMQ installed and configured. This service is an option if you are 
  using RabbitMQ and do not want to maintain RabbitMQ installations on your 
  own servers.

## Open source examples that use task queues
* Take a look at the code in this open source 
  [Flask application](https://www.twilio.com/docs/howto/walkthrough/appointment-reminders/python/flask) 
  and 
  [this Django application](https://www.twilio.com/docs/howto/walkthrough/appointment-reminders/python/django) 
  for examples of how to use and deploy Celery with a Redis broker to
  send text messages with these frameworks. 

* [flask-celery-example](https://github.com/thrisp/flask-celery-example) is
  a simple Flask application with Celery as a task queue and Redis as
  the broker.


## Task queue resources
* [Getting Started Scheduling Tasks with Celery](http://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/)
  is a detailed walkthrough for setting up Celery with Django (although
  Celery can also be used without a problem with other frameworks).

* [International Space Station notifications with Python and Redis Queue (RQ)](https://www.twilio.com/blog/2015/11/international-space-station-notifications-with-python-redis-queue-and-twilio-copilot.html)
  shows how to combine the RQ task queue library with Flask to send 
  text message notifications every time a condition is met - in this blog
  post's case that the ISS is currently flying over your location on
  Earth.

* [Evaluating persistent, replicated message queues](http://www.warski.org/blog/2014/07/evaluating-persistent-replicated-message-queues/)
  is a detailed comparison of Amazon SQS, MongoDB, RabbitMQ, HornetQ and
  Kafka's designs and performance.

* [Queues.io](http://queues.io/) is a collection of task queue systems with
  short summaries for each one. The task queues are not all compatible with
  Python but ones that work with it are tagged with the "Python" keyword.

* [Why Task Queues](http://www.slideshare.net/bryanhelmig/task-queues-comorichweb-12962619) 
  is a presentation for what task queues are and why they are needed. 

* Flask by Example [Implementing a Redis Task Queue](https://realpython.com/blog/python/flask-by-example-implementing-a-redis-task-queue/)
  provides a detailed walkthrough of setting up workers to use RQ with
  Redis.

* [How to use Celery with RabbitMQ](https://www.digitalocean.com/community/articles/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps)
  is a detailed walkthrough for using these tools on an Ubuntu VPS.

* Heroku has a clear walkthrough for using 
  [RQ for background tasks](https://devcenter.heroku.com/articles/python-rq).

* [Introducing Celery for Python+Django](http://www.linuxforu.com/2013/12/introducing-celery-pythondjango/) 
  provides an introduction to the Celery task queue.

* [Celery - Best Practices](https://denibertovic.com/posts/celery-best-practices/)
  explains things you should not do with Celery and shows some underused 
  features for making task queues easier to work with.

* The "Django in Production" series by 
  [Rob Golding](https://twitter.com/robgolding63) contains a post 
  specifically on [Background Tasks](http://www.robgolding.com/blog/2011/11/27/django-in-production-part-2---background-tasks/).

* [Asynchronous Processing in Web Applications Part One](http://blog.thecodepath.com/2012/11/15/asynchronous-processing-in-web-applications-part-1-a-database-is-not-a-queue/) 
  and [Part Two](http://blog.thecodepath.com/2013/01/06/asynchronous-processing-in-web-applications-part-2-developers-need-to-understand-message-queues/)
  are great reads for understanding the difference between a task queue and
  why you shouldn't use your database as one.

* [Celery in Production](http://www.caktusgroup.com/blog/2014/09/29/celery-production/)
  on the Caktus Group blog contains good practices from their experience 
  using Celery with RabbitMQ, monitoring tools and other aspects not often
  discussed in existing documentation.

* [A 4 Minute Intro to Celery](https://www.youtube.com/watch?v=68QWZU_gCDA) is
  a short introductory task queue screencast.

* Heroku wrote about how to 
  [secure Celery](https://engineering.heroku.com/blogs/2014-09-15-securing-celery)
  when tasks are otherwise sent over unencrypted networks.

* Miguel Grinberg wrote a nice post on using the 
  [task queue Celery with Flask](http://blog.miguelgrinberg.com/post/using-celery-with-flask). 
  He gives an overview of Celery followed by specific code to set up the task
  queue and integrate it with Flask.

* [3 Gotchas for Working with Celery](https://wiredcraft.com/blog/3-gotchas-for-celery/)
  are things to keep in mind when you're new to the Celery task queue 
  implementation.

* [Deferred Tasks and Scheduled Jobs with Celery 3.1, Django 1.7 and Redis](https://godjango.com/63-deferred-tasks-and-scheduled-jobs-with-celery-31-django-17-and-redis/)
  is a video along with code that shows how to set up Celery with Redis as the
  broker in a Django application.

* [Setting up an asynchronous task queue for Django using Celery and Redis](http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/)
  is a straightforward tutorial for setting up the Celery task queue for 
  Django web applications using the Redis broker on the back end.

* [Background jobs with Django and Celery](http://django.zone/blog/posts/background-jobs-django-and-celery/)
  shows the code and a simple explanation of how to use Celery with 
  [Django](/django.html).

* [Asynchronous Tasks With Django and Celery](https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/)
  shows how to integrate Celery with [Django](/django.html) and create Periodic Tasks.

* [Three quick tips from two years with Celery](https://library.launchkit.io/three-quick-tips-from-two-years-with-celery-c05ff9d7f9eb)
  provides some solid advice on retry delays, the -Ofair flag and global
  task timeouts for Celery.


## Task queue learning checklist
1. Pick a slow function in your project that is called during an HTTP 
   request.

1. Determine if you can precompute the results on a fixed interval instead 
   of during the HTTP request. If so, create a separate function you can call
   from elsewhere then store the precomputed value in the database.

1. Read the Celery documentation and the links in the resources section below
   to understand how the project works.

1. Install a message broker such as RabbitMQ or Redis and then add Celery to 
   your project. Configure Celery to work with the installed message broker.

1. Use Celery to invoke the function from step one on a regular basis.

1. Have the HTTP request function use the precomputed value instead of the 
   slow running code it originally relied upon.
 
