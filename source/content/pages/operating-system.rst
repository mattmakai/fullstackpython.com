Operating System
================

:category: page
:slug: operating-system
:sort-order: 03

The operating system runs on top of the server or virtual server
and controls access to computing resources. The only operating
system I can recommend for production Python web stack deployments is
a flavor of Linux. Ubuntu Long Term Support (LTS) releases, Red Hat 
Enterprise Linux, and CentOS are all viable options. 

*Side note*: Mac OS X is fine for development activities but not for 
test/production deployments.

Ubuntu
------
Ubuntu is a Linux distribution packaged by the 
`Canonical Ltd <http://www.canonical.com/>`_ company. Ubuntu uses the
Debian distribution as a base for packages, including the `aptitude package
manager <http://wiki.debian.org/Apt>`_. For desktop versions of Ubuntu, 
GNOME (until the 11.04 release) or Unity (11.10 through current)
is added to the distribution to provide a user interface.


Red Hat and CentOS
------------------
`Red Hat Enterprise Linux <http://www.redhat.com/products/enterprise-linux/>`_ 
(RHEL) and Community enterprise Operating 
System (CentOS) are essentially the same distribution. The key 
difference is that CentOS is an open source free derivative of RHEL.

RHEL and CentOS use a different package manager and command-line interface 
from Debian-based Linux distributions: RPM Package Manager (RPM) and the 
Yellowdog Updater, Modified (YUM). RPM has a specific .rpm file format
to handle the packaging and installation of libraries and applications. YUM
provides a command-line interface for interacting with the RPM system.

Monitoring
----------
There are several important resources to monitor on the operating system 
and network level of a web stack.

1. CPU utilization
2. Memory utilization
3. Persistence storage consumed versus free
4. Network bandwidth and latency

