title: Docker
category: page
slug: docker
sort-order: 1202
choice1url: /deployment.html
choice1icon: fa-share
choice1text: How do I deploy a Python application without a container?
choice2url: /continuous-integration.html
choice2icon: fa-refresh
choice2text: How do I regularly integrate my project's codebase?
choice3url: /development-environments.html
choice3icon: fa-desktop
choice3text: What should I use to code my Python application?
choice4url: 
choice4icon: 
choice4text: 


# Docker
Docker is an [open source](https://github.com/docker/docker) 
infrastructure management platform that manages disk images.


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


## Python-specific Docker resources
* [Hosting Python WSGI applications using Docker](http://blog.dscpl.com.au/2014/12/hosting-python-wsgi-applications-using.html)
  shows how to use Docker in WSGI application deployments specifically using
  mod\_wsgi.

* [How to Containerize Python Web Applications](https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications)
  is an extensive tutorial that uses a Flask application and deploys it
  using a Docker container.

* [Deploying Django Applications in Docker](http://handlebarcreative.tumblr.com/post/104881545637/deploying-django-applications-in-docker)
  explains some of the concepts behind using Docker for Python deployments and
  shows how to specifically use it for deploying Django. 



### What do you want to learn next about deployment?
