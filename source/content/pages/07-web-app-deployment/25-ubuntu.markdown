title: Ubuntu
category: page
slug: ubuntu
sortorder: 0725
toc: False
sidebartitle: Ubuntu
meta: Ubuntu is a Debian Linux-based operating system distribution often used for Python development and deployment.


# Ubuntu
Ubuntu is a Debian Linux-based operating system distribution often used for 
Python development and application deployment.


## Why is Ubuntu important for Python?
Ubuntu is one of the most commonly used Linux distributions for both local
development and server deployments. Some 
[platforms-as-a-service](/platform-as-a-service.html) such as Heroku run 
Ubuntu as the base operating system, so as a Python developer you'll often
have to work with Ubuntu or a similar Debian-based Linux operating system.

<div class="well see-also">Ubuntu is an implementation of the <a href="/operating-systems.html">operating systems</a> concept. Learn more in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## What does "LTS" mean for Ubuntu?
Every two years Ubuntu releases a Long-Term Support (LTS) version that
receives five years of updates instead of only two years for non-LTS
releases. However, there are some issues with the current LTS model,
in that you 
[must only use packages from the main repository](http://www.wilderssecurity.com/threads/ubuntu-lts-many-vulnerabilities-despite-long-term-support.385386/) 
unless you're going to manually handle security updates for non-main
repository system packages.


## Additional Ubuntu resources
* Get your Python [development environment](/development-environments.html)
  set up with one of these quick tutorials for Ubuntu 16.04 LTS:
    * [How to set up Python 3, Flask and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
    * [Configuring Python 3, Bottle and Gunicorn for Development on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html)
    * [Setting up Python 3, Django and Gunicorn on Ubuntu 16.04 LTS](/blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html)

* There are also walkthroughs for configuring relational databases and Redis 
  on Ubuntu:
    * [Setting up PostgreSQL with Python 3 and psycopg on Ubuntu 16.04](/blog/postgresql-python-3-psycopg2-ubuntu-1604.html)
    * [How to Install and Use MySQL on Ubuntu 16.04](/blog/install-mysql-ubuntu-1604.html)
    * [How to Use Redis with Python 3 and redis-py on Ubuntu 16.04](/blog/install-redis-use-python-3-ubuntu-1604.html)

* Canonical, the organization that produces Ubuntu, typically pushes the 
  boundaries on non-LTS releases, but occasionally rocks the boat with
  major changes for an LTS release. 16.04 LTS was one such version, which
  is described in this article about how 
  [Ubuntu 16.04 proves even an LTS release can live at Linux's bleeding edge](http://arstechnica.com/information-technology/2016/05/ubuntu-16-04-proves-even-an-lts-release-can-live-at-linuxs-bleeding-edge/).

* Ubuntu has been a target operating system for Docker since the beginning of
  the project. Here's a guide for 
  [how to install Docker on Ubuntu 14.04 LTS](http://www.liquidweb.com/kb/how-to-install-docker-on-ubuntu-14-04-lts/),
  one of the older operating system releases that supports containers.

* [What I learned while securing Ubuntu](https://major.io/2015/10/14/what-i-learned-while-securing-ubuntu/)
  explains how difficult it can be just to find correct information
  on how to secure an operating system. In this case, the author goes over
  how he went about securing package management, security standards and 
  file integrity on Ubuntu 14.04 LTS.

