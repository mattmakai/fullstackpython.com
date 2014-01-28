Operating Systems
=================

:category: page
:slug: operating-systems
:sort-order: 03

The operating system runs on the server or virtual server and controls access 
to computing resources. The only recommeneded operating system for 
production Python web stack deployments is Linux. There are several 
Linux distributions commonly used for running production servers. Ubuntu 
Long Term Support (LTS) releases, Red Hat Enterprise Linux, and CentOS are 
all viable options. 

*Side note*: Mac OS X is fine for development activities. Windows and Mac 
OS X are not appropriate for most test and production deployments unless
there is a specific reason why you must use them in lieu of Linux.

Ubuntu
------
Ubuntu is a Linux distribution packaged by the 
`Canonical Ltd <http://www.canonical.com/>`_ company. Ubuntu uses the
Debian distribution as a base for packages, including the `aptitude package
manager <http://wiki.debian.org/Apt>`_. For desktop versions of Ubuntu, 
GNOME (until the 11.04 release) or Unity (11.10 through current)
is added to the distribution to provide a user interface.

Ubuntu `Long Term Support (LTS) <https://wiki.ubuntu.com/LTS>`_ releases
are the recommended versions to use for deployments. LTS versions receive
five years of post-release updates from Canonical. Every two years, Canonical 
creates a new LTS release, which allows for an easy upgrade path as well 
as flexibility in skipping every other LTS release if necessary.


Red Hat and CentOS
------------------
`Red Hat Enterprise Linux <http://www.redhat.com/products/enterprise-linux/>`_ 
(RHEL) and `Community ENTerprise Operating System <http://www.centos.org/>`_ 
(CentOS) are the same distribution. The only difference between the two 
(other than the name) is that CentOS is an open source, liberally 
licensed free derivative of RHEL.

RHEL and CentOS use a different package manager and command-line interface 
from Debian-based Linux distributions: RPM Package Manager (RPM) and the 
Yellowdog Updater, Modified (YUM). RPM has a specific .rpm file format
to handle the packaging and installation of libraries and applications. YUM
provides a command-line interface for interacting with the RPM system.


Operating System Resources
--------------------------
`Choosing a Linux Distribution <http://www.rackspace.com/knowledge_center/article/choosing-a-linux-distribution>`_

`First 5 Minutes on a Server <http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers>`_

`Securing an Ubuntu Server <http://www.andrewault.net/2010/05/17/securing-an-ubuntu-server/>`_
`Securing Ubuntu <http://joshrendek.com/2013/01/securing-ubuntu/>`_

`Securing a Linux Server <http://spenserj.com/blog/2013/07/15/securing-a-linux-server/>`_

`quick-secure scripts <https://github.com/marshyski/quick-secure>`_ for
securing RedHat Linux distributions on boot.

