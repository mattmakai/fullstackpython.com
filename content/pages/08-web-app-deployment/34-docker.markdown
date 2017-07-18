title: Docker
category: page
slug: docker
sortorder: 0834
toc: False
sidebartitle: Docker
meta: Docker is a container management system often used for deploying web applications. Learn more about Docker on Full Stack Python.


# Docker
Docker is an [open source](https://github.com/docker/docker) 
infrastructure management platform for running and deploying software. The
Docker platform is constantly evolving so an exact definition is currently
a moving target.


## Why is Docker important?
Docker can package up applications along with their necessary operating system
dependencies for easier deployment across environments. In the long run it
has the potential to be the abstraction layer that easily manages containers
running on top of any type of server, regardless of whether that server is
on Amazon Web Services, Google Compute Engine, Linode, Rackspace or elsewhere.


## Python projects within Docker images
* This Docker image contains 
  [a Flask application configured to run with uWSGI and Nginx](https://github.com/tiangolo/uwsgi-nginx-flask-docker).
  You can also see the [image on Docker hub](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/).

* [minimal-docker-python-setup](https://github.com/OrangeTux/minimal-docker-python-setup) 
  contains an image with Nginx, uWSGI, Redis and Flask.


## Docker resources
* [What is Docker and When to Use It](https://www.ctl.io/developers/blog/post/what-is-docker-and-when-to-use-it/)
  clearly delineates what Docker is and what it isn't. This is a good article
  for when you're first wrapping your head around Docker conceptually.

* [Andrew Baker](https://github.com/atbaker) presented a fantastic tutorial 
  at [PyOhio](http://andrewtorkbaker.com/pyohio-docker-101-tutorial) on 
  [beginner and advanced Docker usage](https://github.com/atbaker/docker-tutorial). 
  Andrew also wrote the article [what containers can do for you](http://radar.oreilly.com/2015/01/what-containers-can-do-for-you.html)
  and created the
  [O'Reilly Introduction to Docker video](http://shop.oreilly.com/product/0636920035732.do) 
  that's well worth buying.

* [Docker curriculum](http://prakhar.me/docker-curriculum/) is a detailed
  tutorial created by a developer to show the exact steps for deploying an 
  application that relies on [Elasticsearch](https://www.elastic.co/). 

* [How to install Docker and get started](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-getting-started)
  provides a walkthrough for Ubuntu 13.04 for installing and beginning to
  use Docker for development.

* [It Really is the Future](http://blog.circleci.com/it-really-is-the-future/)
  discusses Docker and containers in the context of whether it's all just a
  bunch of hype or if this is a real trend for infrastructure automation.
  This is a great read to set the context for why these tools are important.

* [Docker Jumpstart](https://github.com/odewahn/docker-jumpstart/) is a 
  comprehensive introduction to what Docker is and how to get started with
  using the tool.

* If you want to quickly use Docker on Mac OS X, check out these concise
  instructions 
  [for setting up your Docker workflow on OS X in 60 seconds](https://www.twilio.com/blog/2015/07/docker-workflow-on-osx-in-60-seconds.html).

* [What the Bleep is Docker?](http://pythonforengineers.com/what-the-bleep-is-docker/)
  is a plain English explanation with examples of what Docker provides and
  what it can be used for in your environment.

* [Docker in Practice - A Guide for Engineers](https://zwischenzugs.wordpress.com/2015/03/14/docker-in-practice-a-guide-for-engineers/)
  is an explanation of the concepts and philosophy by the authors of the 
  new Manning Docker book in early access format.

* [Eight Docker Development Patterns](http://www.hokstad.com/docker/patterns)
  shares lessons learned and explains how to work with the containers so you 
  get more use out of them during development.

* [Building Docker containers from scratch](http://datakurre.pandala.org/2015/07/building-docker-containers-from-scratch.html)
  is a short tutorial for creating a Docker container with a specific
  configuration.

* [10 things to avoid in Docker containers](http://developerblog.redhat.com/2016/02/24/10-things-to-avoid-in-docker-containers/)
  provides a lot of "don'ts" that you'll want to consider before bumping
  up against the limitations of how containers should be used.


## Python-specific Docker resources
* [How to deploy Django using Docker](https://www.stavros.io/posts/how-deploy-django-docker/)
  assumes you already have the basic grasp of working with Docker and
  jumps right into a Django deployment. The post shows you how to set up
  your `Dockerfile` and explains that [GitLab CI](https://about.gitlab.com/) 
  can be used to to build this Docker image.

* [Hosting Python WSGI applications using Docker](http://blog.dscpl.com.au/2014/12/hosting-python-wsgi-applications-using.html)
  shows how to use Docker in WSGI application deployments specifically using
  mod\_wsgi.

* [How to Containerize Python Web Applications](https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications)
  is an extensive tutorial that uses a Flask application and deploys it
  using a Docker container.

* The [Docker is awesome](http://pritishc.com/blog/2015/09/03/docker-is-awesome/) 
  miniseries explains how to get a Django + AngularJS application running 
  under Docker. 
  [Part 2](http://pritishc.com/blog/2015/09/04/docker-is-awesome-part-ii/) 
  continues the tutorial.

* [Docker in Action - Fitter, Happier, More Productive ](https://realpython.com/blog/python/docker-in-action-fitter-happier-more-productive/)
  is a killer tutorial that shows how to combine Docker with CircleCI to
  continuously deploy a Flask application.

* [Deploying Django Applications in Docker](http://handlebarcreative.tumblr.com/post/104881545637/deploying-django-applications-in-docker)
  explains some of the concepts behind using Docker for Python deployments and
  shows how to specifically use it for deploying Django. 

* [A Docker primer – from zero to a running Django app](https://ochronus.com/docker-primer-django/)
  provides specific commands and expected output for running Django apps
  with Docker and Vagrant.

* [Using Docker and Docker Compose to replace virtualenv](https://www.calazan.com/using-docker-and-docker-compose-for-local-django-development-replacing-virtualenv/)
  is a tutorial for using Docker instead of virtualenv for dependency
  isolation.

* Lincoln Loop wrote up 
  [a closer look at Docker](https://lincolnloop.com/blog/closer-look-docker/)
  from the perspective of Python developers handling deployments.

* Curious how pip and Docker can be used together? Read this article on 
  [Efficient management Python projects dependencies with Docker](https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/).

* [Python virtual environments and Docker](http://blog.dscpl.com.au/2016/01/python-virtual-environments-and-docker.html)
  goes into detail on whether virtual environments should be used with Docker
  and how system packages can generally be a safer route to go.
