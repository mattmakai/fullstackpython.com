title: Docker
category: page
slug: docker
sort-order: 0717
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


## Docker resources
* [What is Docker and When to Use It](http://www.centurylinklabs.com/what-is-docker-and-when-to-use-it/)
  clearly delineates what Docker is and what it isn't. This is a good article
  for when you're first wrapping your head around Docker conceptually.

* [Andrew Baker](https://github.com/atbaker) presented a fantastic tutorial 
  at [PyOhio](http://andrewtorkbaker.com/pyohio-docker-101-tutorial) on 
  [beginner and advanced Docker usage](https://github.com/atbaker/docker-tutorial). Andrew also created 
  [O'Reilly Introduction to Docker video](http://shop.oreilly.com/product/0636920035732.do) that's
  well worth buying.

* [Docker Jumpstart](https://github.com/odewahn/docker-jumpstart/) is a 
  comprehensive introduction to what Docker is and how to get started with
  using the tool.

* [What the Bleep is Docker?](http://pythonforengineers.com/what-the-bleep-is-docker/)
  is a plain English explanation with examples of what Docker provides and
  what it can be used for in your environment.

* [Docker in Practice - A Guide for Engineers](https://zwischenzugs.wordpress.com/2015/03/14/docker-in-practice-a-guide-for-engineers/)
  is an explanation of the concepts and philosophy by the authors of the 
  new Manning Docker book in early access format.

* [Eight Docker Development Patterns](http://www.hokstad.com/docker/patterns)
  shares lessons learned and explains how to work with the containers so you 
  get more use out of them during development.

* [The marriage of Ansible and Docker](https://bildung.xarif.de/xwiki/bin/Articles/The+Marriage+of+Ansible+and+Docker)
  is a detailed look at how Docker and Ansible complement each other as
  deployment tools.


## Python-specific Docker resources
* [Hosting Python WSGI applications using Docker](http://blog.dscpl.com.au/2014/12/hosting-python-wsgi-applications-using.html)
  shows how to use Docker in WSGI application deployments specifically using
  mod\_wsgi.

* [How to Containerize Python Web Applications](https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications)
  is an extensive tutorial that uses a Flask application and deploys it
  using a Docker container.

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

