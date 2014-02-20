===========
Task Queues
===========

:category: page
:slug: task-queues
:sort-order: 09

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


Task Queue resources
--------------------
`Queues.io <http://queues.io/>`_ is a collection of task queue systems with
short summaries for each one. The task queues are not all compatible with
Python but ones that work with it are tagged with the "Python" keyword.

The `Celery <http://www.celeryproject.org/>`_ distributed task queue is the
most commonly used Python library for handling asynchronous tasks and 
scheduling.

The `RQ (Redis Queue) <http://python-rq.org/>`_ is a simple Python
library for queueing jobs and processing them in the background with workers.
It is backed by Redis and it is designed to have a low barrier to entry.
It should be integrated in your web stack easily.


