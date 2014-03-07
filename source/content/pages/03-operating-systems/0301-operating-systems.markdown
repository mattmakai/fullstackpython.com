title: Operating Systems
category: page
slug: operating-systems
sort-order: 03


# Operating Systems
An operating system runs on the server or virtual server and controls access 
to computing resources. The only recommended operating system for 
production Python web stack deployments is Linux. There are several 
Linux distributions commonly used for running production servers. Ubuntu 
Long Term Support (LTS) releases, Red Hat Enterprise Linux, and CentOS are 
all viable options. 

*Side note*: Mac OS X is fine for development activities. Windows and Mac 
OS X are not appropriate for most test and production deployments unless
there is a specific reason why you must use them in lieu of Linux.

## Ubuntu
Ubuntu is a Linux distribution packaged by the 
[Canonical Ltd](http://www.canonical.com/) company. Ubuntu uses the
Debian distribution as a base for packages, including the 
[aptitude package manager](http://wiki.debian.org/Apt). For desktop versions 
of Ubuntu, GNOME (until the 11.04 release) or Unity (11.10 through current)
is bundled with the distribution to provide a user interface.

Ubuntu [Long Term Support](https://wiki.ubuntu.com/LTS) (LTS) releases
are the recommended versions to use for deployments. LTS versions receive
five years of post-release updates from Canonical. Every two years, Canonical 
creates a new LTS release, which allows for an easy upgrade path as well 
as flexibility in skipping every other LTS release if necessary. As of
February 2014, 
[12.04 Precise Pangolin](http://releases.ubuntu.com/precise/)
is the latest Ubuntu LTS release.


### Ubuntu Python Packages
There are several 
[Aptitude](https://help.ubuntu.com/12.04/serverguide/aptitude.html)
packages found on Linux servers running a Python stack. These packages are: 

* [python-dev](http://packages.ubuntu.com/precise/python-dev) for header
  files and static library for Python

* [python-virtualenv](http://packages.ubuntu.com/precise/python-virtualenv)
  for creating and managing Python 
  [virtualenvs](http://www.virtualenv.org/en/latest/) to isolate library
  dependencies


## Red Hat and CentOS
[Red Hat Enterprise Linux](http://www.redhat.com/products/enterprise-linux/)
(RHEL) and [Community ENTerprise Operating System](http://www.centos.org/)
(CentOS) are the same distribution. The primary difference between the two 
is that CentOS is an open source, liberally licensed free derivative of RHEL.

RHEL and CentOS use a different package manager and command-line interface 
from Debian-based Linux distributions: RPM Package Manager (RPM) and the 
Yellowdog Updater, Modified (YUM). RPM has a specific .rpm file format
to handle the packaging and installation of libraries and applications. YUM
provides a command-line interface for interacting with the RPM system.


## Operating System Resources
* [Choosing a Linux Distribution](http://www.rackspace.com/knowledge_center/article/choosing-a-linux-distribution)

* [First 5 Minutes on a Server](http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers)

* [Securing an Ubuntu Server](http://www.andrewault.net/2010/05/17/securing-an-ubuntu-server/)

* [Securing Ubuntu](http://joshrendek.com/2013/01/securing-ubuntu/)

* [Securing a Linux Server](http://spenserj.com/blog/2013/07/15/securing-a-linux-server/)

* [quick NIX secure script](https://github.com/marshyski/quick-secure) for
securing Linux distributions.

