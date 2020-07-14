title: Celery
category: page
slug: celery
sortorder: 0428
toc: False
sidebartitle: Celery
meta: Celery is a task queue for executing work outside a Python web application HTTP request-response cycle.


[Celery](https://docs.celeryproject.org/en/stable/) is a [task queue](/task-queues.html) 
implementation for [Python web applications](/web-development.html) used
to asynchronously execute work outside the HTTP request-response cycle.

<a href="https://docs.celeryproject.org/en/stable/" style="border:none"><img src="/img/logos/celery.png" alt="Celery task queue project logo." class="shot" width="100%"></a>

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


### Celery tutorials and advice
Celery is a powerful tool that can be difficult to wrap your mind around
at first. Be sure to read up on [task queue](/task-queues.html) concepts
then dive into these specific Celery tutorials.

* [A 4 Minute Intro to Celery](https://www.youtube.com/watch?v=68QWZU_gCDA) is
  a short introductory task queue screencast.

* This blog post series on 
  [Celery's architecture](https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/), 
  [Celery in the wild: tips and tricks to run async tasks in the real world](https://www.vinta.com.br/blog/2018/celery-wild-tips-and-tricks-run-async-tasks-real-world/)
  and
  [dealing with resource-consuming tasks on Celery](https://www.vinta.com.br/blog/2018/dealing-resource-consuming-tasks-celery/)
  provide great context for how Celery works and how to handle some of the 
  trickier bits to working with the task queue.

* [How to use Celery with RabbitMQ](https://www.digitalocean.com/community/articles/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps)
  is a detailed walkthrough for using these tools on an Ubuntu VPS.

* [Celery - Best Practices](https://denibertovic.com/posts/celery-best-practices/)
  explains things you should not do with Celery and shows some underused 
  features for making task queues easier to work with.

* [Celery Best Practices](https://blog.balthazar-rouberol.com/celery-best-practices) 
  is a different author's follow up to the above best practices post that
  builds upon some of his own learnings from 3+ years using Celery.

* [Common Issues Using Celery (And Other Task Queues)](https://adamj.eu/tech/2020/02/03/common-celery-issues-on-django-projects/)
  contains good advice about mistakes to avoid in your task configurations, 
  such as database transaction usage and retrying failed tasks.

* [Asynchronous Processing in Web Applications Part One](http://blog.thecodepath.com/2012/11/15/asynchronous-processing-in-web-applications-part-1-a-database-is-not-a-queue/) 
  and [Part Two](http://blog.thecodepath.com/2013/01/06/asynchronous-processing-in-web-applications-part-2-developers-need-to-understand-message-queues/)
  are great reads for understanding the difference between a task queue and
  why you shouldn't use your database as one.

* [My Experiences With A Long-Running Celery-Based Microprocess](https://theblog.workey.co/my-experiences-with-a-long-running-celery-based-microprocess-b2cc30da94f5)
  gives some good tips and advice based on experience with Celery workers
  that take a long time to complete their jobs.

* [Checklist to build great Celery async tasks](http://celerytaskschecklist.com/)
  is a site specifically designed to give you a list of good practices to 
  follow as you design your task queue configuration and deploy to 
  development, staging and production environments.

* Heroku wrote about how to 
  [secure Celery](https://engineering.heroku.com/blogs/2014-09-15-securing-celery)
  when tasks are otherwise sent over unencrypted networks.

* [Unit testing Celery tasks](https://www.python-celery.com/2018/05/01/unit-testing-celery-tasks/)
  explains three strategies for testing code within functions that Celery 
  executes. The post concludes that calling Celery tasks synchronously to test
  them is the best strategy without any downsides. However, keep in mind that 
  any testing method that is not the same as how the function will execute 
  in a production environment can potentially lead to overlooked bugs. There 
  is also an 
  [open source Git repository with all of the source code](https://github.com/ZoomerAnalytics/python-celery-unit-testing)
  from the post.

* [Rollbar monitoring of Celery in a Django app](https://www.mattlayman.com/blog/2017/django-celery-rollbar/)
  explains how to use [Rollbar](/rollbar.html) to monitor tasks. Super
  useful when workers invariably die for no apparent reason.

* [3 Gotchas for Working with Celery](https://wiredcraft.com/blog/3-gotchas-for-celery/)
  are things to keep in mind when you're new to the Celery task queue 
  implementation.

* [Dask and Celery](http://matthewrocklin.com/blog/work/2016/09/13/dask-and-celery) 
  compares Dask.distributed with Celery for Python projects. The post gives
  code examples to show how to execute tasks with either task queue.

* [Python+Celery: Chaining jobs?](https://stackoverflow.com/questions/3901101/pythoncelery-chaining-jobs)
  explains that Celery tasks should be dependent upon each other using 
  Celery chains, not direct dependencies between tasks.


### Celery with web frameworks
Celery is typically used with a [web framework](/web-frameworks.html) such as
[Django](/django.html), [Flask](/flask.html) or [Pyramid](/pyramid.html).
These resources show you how to integrate the Celery task queue with the
web framework of your choice.

* [How to Use Celery and RabbitMQ with Django](https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html)
  is a great tutorial that shows how to both install and set up a basic
  task with Django.

* Miguel Grinberg wrote a nice post on using the 
  [task queue Celery with Flask](http://blog.miguelgrinberg.com/post/using-celery-with-flask). 
  He gives an overview of Celery followed by specific code to set up the task
  queue and integrate it with Flask.

* [Setting up an asynchronous task queue for Django using Celery and Redis](http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/)
  is a straightforward tutorial for setting up the Celery task queue for 
  Django web applications using the Redis broker on the back end.

* [A Guide to Sending Scheduled Reports Via Email Using Django And Celery](https://hashedin.com/a-guide-to-sending-scheduled-reports-via-email-using-django-and-celery/)
  shows you how to use 
  [django-celery](https://github.com/celery/django-celery)
  in your application. Note however there are other ways of integrating
  Celery with Django that do not require the django-celery dependency.

* [Flask asynchronous background tasks with Celery and Redis](http://allynh.com/blog/flask-asynchronous-background-tasks-with-celery-and-redis/)
  combines Celery with [Redis](/redis.html) as the broker and 
  [Flask](/flask.html) for the example application's framework.

* [Celery and Django and Docker: Oh My!](https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/)
  shows how to create Celery tasks for Django within a [Docker](/docker.html)
  container. It also provides some 

* [Asynchronous Tasks With Django and Celery](https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/)
  shows how to integrate Celery with [Django](/django.html) and create Periodic Tasks.

* [Getting Started Scheduling Tasks with Celery](http://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/)
  is a detailed walkthrough for setting up Celery with Django (although
  Celery can also be used without a problem with other frameworks).

* [Introducing Celery for Python+Django](http://www.linuxforu.com/2013/12/introducing-celery-pythondjango/) 
  provides an introduction to the Celery task queue with Django as the
  intended framework for building a web application.

* [Asynchronous Tasks with Falcon and Celery](https://testdriven.io/asynchronous-tasks-with-falcon-and-celery)
  configures Celery with the [Falcon](/falcon.html) framework, which is 
  less commonly-used in web tutorials.

* [Custom Celery task states](https://www.distributedpython.com/2018/09/28/celery-task-states/)
  is an advanced post on creating custom states, which is especially useful 
  for transient states in your application that are not covered by the 
  default Celery configuration.

* [Asynchronous Tasks with Django and Celery](https://testdriven.io/blog/django-and-celery/)
  looks at how to configure Celery to handle long-running tasks in a
  Django app.

### Celery deployment resources
Celery and its broker run separately from your web and WSGI servers so it 
adds some additional complexity to your [deployments](/deployment.html). The 
following resources walk you through how to handle deployments and get the
right configuration settings in place.

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
  provides some solid advice on retry delays, the `-Ofair` flag and global
  task timeouts for Celery.
