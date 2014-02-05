Task Queues
===========

:category: page
:slug: task-queues
:sort-order: 15

Task queues handle asynchronous jobs that need to be processed outside the
usual HTTP request-response cycle. The most common types of jobs for task 
queues include

* calculating computationally expensive data analytics

* scheduling periodic jobs such as batch processes

* spreading out large numbers of independent database inserts over time 
  instead of all at once


Task Queue Resources
--------------------
The `Celery <http://www.celeryproject.org/>`_ distributed task queue is the
most commonly used Python library for handling asynchronous tasks and 
scheduling.

The `RQ (Redis Queue) <http://python-rq.org/>`_ is a simple Python
library for queueing jobs and processing them in the background with workers.
It is backed by Redis and it is designed to have a low barrier to entry.
It should be integrated in your web stack easily.

