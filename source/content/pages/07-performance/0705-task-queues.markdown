title: Task Queues
category: page
slug: task-queues
sort-order: 073
choice1url: /logging.html
choice1icon: fa-align-left fa-inverse
choice1text: How do I monitor my app and its task queues with logging?
choice2url: /web-analytics.html
choice2icon: fa-dashboard
choice2text: How can I learn more about the users of my application? 
choice3url: /monitoring.html
choice3icon: fa-bar-chart-o fa-inverse
choice3text: What tools exist for monitoring a live web application?
choice4url:
choice4icon:
choice4text:


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


## Task queues learning checklist
<i class="fa fa-check-square-o"></i> 
Pick a slow function in your project that is called during an HTTP request.

<i class="fa fa-check-square-o"></i> 
Determine if you can precompute the results on a fixed interval instead of
during the HTTP request. If so, create a separate function you can call
from elsewhere then store the precomputed value in the database.

<i class="fa fa-check-square-o"></i> 
Read the Celery documentation and the links in the resources section below
to understand how the project works.

<i class="fa fa-check-square-o"></i> 
Install a message broker such as RabbitMQ or Redis and then add Celery to your 
project. Configure Celery to work with the installed message broker.

<i class="fa fa-check-square-o"></i> 
Use Celery to invoke the function from step one on a regular basis.

<i class="fa fa-check-square-o"></i>
Have the HTTP request function use the precomputed value instead of the 
slow running code it originally relied upon.
 

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
  is a detailed walkthrough for using these tools on an Ubuntu VPS.

* Heroku has a clear walkthrough for using 
  [RQ for background tasks](https://devcenter.heroku.com/articles/python-rq).

* [Introducing Celery for Python+Django](http://www.linuxforu.com/2013/12/introducing-celery-pythondjango/) 
  provides an introduction to the Celery task queue.

* The "Django in Production" series by 
  [Rob Golding](https://twitter.com/robgolding63) contains a post 
  specifically on [Background Tasks](http://www.robgolding.com/blog/2011/11/27/django-in-production-part-2---background-tasks/).

* [Asynchronous Processing in Web Applications Part One](http://blog.thecodepath.com/2012/11/15/asynchronous-processing-in-web-applications-part-1-a-database-is-not-a-queue/) 
  and [Part Two](http://blog.thecodepath.com/2013/01/06/asynchronous-processing-in-web-applications-part-2-developers-need-to-understand-message-queues/)
  are great reads for understanding the difference between a task queue and
  why you shouldn't use your database as one.


### What's next after task queues?
