title: Celery
category: page
slug: celery
sortorder: 0726
toc: False
sidebartitle: Celery
meta: Celery is a task queue to perform work outside a Python web application HTTP request-response cycle.


# Celery
[Celery](http://www.celeryproject.org/) is a [task queue](/task-queues.html) 
implementation for [Python web applications](/web-development.html) used
to asynchronously execute work outside the HTTP request-response cycle.

<a href="http://www.celeryproject.org/" style="border: none;"><img src="/source/static/img/logos/celery.png" width="100%" alt="Celery task queue project logo." style="border-radius: 5px;" width="100%" class="technical-diagram"></a>

<div class="well see-also">Celery is an implementation of the <a href="/task-queues.html">task queue</a> concept. Learn more in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Why is Celery useful?
[Task queues](/task-queues.html) and the Celery implementation in particular 
are one of the trickier parts of a Python web application stack to 
understand. 

If you are a junior developer it can be unclear why moving work 
outside the HTTP request-response cycle is important. In short, you want your [WSGI server](/wsgi-servers.html) to respond to incoming requests as quickly 
as possible because each request ties up a worker process until the response 
is finished. Moving work off those workers by spinning up asynchronous jobs
as tasks in a queue is a straightforward way to improve WSGI server response
times.


## What's the difference between Celeryd and Celerybeat?
Celery can be used to run batch jobs in the background on a
regular schedule. A key concept in Celery is the difference between the 
Celery daemon (celeryd), which executes tasks, Celerybeat, which is a 
scheduler. Think of Celeryd as a tunnel-vision set of one or more workers 
that handle whatever tasks you put in front of them. Each worker will
perform a task and when the task is completed will pick up the next one.
The cycle will repeat continously, only waiting idly when there are no more
tasks to put in front of them.

Celerybeat on the other hand is like a boss who keeps track of when tasks
should be executed. Your application can tell Celerybeat to execute a task
at time intervals, such as every 5 seconds or once a week. Celerybeat can
also be instructed to run tasks on a specific date or time, such as 5:03pm
every Sunday. When the interval or specific time is hit, Celerybeat will
hand the job over to Celeryd to execute on the next available worker.


### Celery tutorials
Celery is a powerful tool that can be difficult to wrap your mind around
at first. Be sure to read up on [task queue](/task-queues.html) concepts
then dive into these specific Celery tutorials.

* [Getting Started Scheduling Tasks with Celery](http://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/)
  is a detailed walkthrough for setting up Celery with Django (although
  Celery can also be used without a problem with other frameworks).

* [Introducing Celery for Python+Django](http://www.linuxforu.com/2013/12/introducing-celery-pythondjango/) 
  provides an introduction to the Celery task queue with Django as the
  intended framework for building a web application.

* [How to use Celery with RabbitMQ](https://www.digitalocean.com/community/articles/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps)
  is a detailed walkthrough for using these tools on an Ubuntu VPS.

* [Celery - Best Practices](https://denibertovic.com/posts/celery-best-practices/)
  explains things you should not do with Celery and shows some underused 
  features for making task queues easier to work with.

* [Asynchronous Processing in Web Applications Part One](http://blog.thecodepath.com/2012/11/15/asynchronous-processing-in-web-applications-part-1-a-database-is-not-a-queue/) 
  and [Part Two](http://blog.thecodepath.com/2013/01/06/asynchronous-processing-in-web-applications-part-2-developers-need-to-understand-message-queues/)
  are great reads for understanding the difference between a task queue and
  why you shouldn't use your database as one.

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

* [Asynchronous Tasks With Django and Celery](https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/)
  shows how to integrate Celery with [Django](/django.html) and create Periodic Tasks.


### Celery deployment resources
* The "Django in Production" series by 
  [Rob Golding](https://twitter.com/robgolding63) contains a post 
  specifically on [Background Tasks](http://www.robgolding.com/blog/2011/11/27/django-in-production-part-2---background-tasks/).

* [How to run celery as a daemon?](https://pythad.github.io/articles/2016-12/how-to-run-celery-as-a-daemon-in-production)
  is a short post with the minimal code for running the Celery daemon and
  Celerybeat as system services on Linux.

* [Celery in Production](http://www.caktusgroup.com/blog/2014/09/29/celery-production/)
  on the Caktus Group blog contains good practices from their experience 
  using Celery with RabbitMQ, monitoring tools and other aspects not often
  discussed in existing documentation.

* [Three quick tips from two years with Celery](https://library.launchkit.io/three-quick-tips-from-two-years-with-celery-c05ff9d7f9eb)
  provides some solid advice on retry delays, the -Ofair flag and global
  task timeouts for Celery.
