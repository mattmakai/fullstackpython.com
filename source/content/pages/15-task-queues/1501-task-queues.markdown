title: Task Queues
category: page
slug: task-queues
sort-order: 15

# Task queues
Task queues handle background work that need to be processed outside the
usual HTTP request-response cycle. These tasks are handled asynchronously 
because HTTP requests must be responded back to by the server as fast as 
possible otherwise the user experience in the web browser will suffer. The 
most common types of jobs for task queues include

* calculating computationally expensive data analytics

* scheduling periodic jobs such as batch processes

* spreading out large numbers of independent database inserts over time 
  instead of all at once

* aggregating collected data values on a fixed interval, such as every
  15 minutes


## Task queue projects
* The [Celery](http://www.celeryproject.org/) distributed task queue is the
  most commonly used Python library for handling asynchronous tasks and 
  scheduling.

* The [RQ (Redis Queue)](http://python-rq.org/) is a simple Python
  library for queueing jobs and processing them in the background with workers.
  RQ is backed by Redis and it is designed to have a low barrier to entry.
  The [intro post](http://nvie.com/posts/introducing-rq/) contains information
  on design decisions and how to use RQ.

* [Taskmaster](https://github.com/dcramer/taskmaster) is a lightweight simple
  distributed queue for handling large volumes of one-off tasks. 


## Task queue resources
* [Distributing work without Celery](http://justcramer.com/2012/05/04/distributing-work-without-celery/)
  provides a scenario in which Celery and RabbitMQ are not the right tool
  for scheduling asynchronous jobs.

* [Queues.io](http://queues.io/) is a collection of task queue systems with
  short summaries for each one. The task queues are not all compatible with
  Python but ones that work with it are tagged with the "Python" keyword.

* [Why Task Queues](http://www.slideshare.net/bryanhelmig/task-queues-comorichweb-12962619) 
  is a presentation for what task queues are and why they are needed. 

* [How to use Celery with RabbitMQ](https://www.digitalocean.com/community/articles/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps)
  is a detail walkthrough for using these tools on an Ubuntu VPS.

* Heroku has a clear walkthrough for using 
  [RQ for background tasks](https://devcenter.heroku.com/articles/python-rq).

* [Introducing Celery for Python+Django](http://www.linuxforu.com/2013/12/introducing-celery-pythondjango/) 
  provides an introduction to the Celery task queue.

* The "Django in Production" series by 
  [Rob Golding](https://twitter.com/robgolding63) contains a post 
  specifically on [Background Tasks](http://www.robgolding.com/blog/2011/11/27/django-in-production-part-2---background-tasks/).
