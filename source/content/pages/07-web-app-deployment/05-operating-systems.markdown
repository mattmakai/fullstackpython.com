title: Operating Systems
category: page
slug: operating-systems
sortorder: 0705
toc: False
sidebartitle: Operating Systems
meta: Learn what operating system you should be using for you web application and resources to configure the OS on Full Stack Python.


# Operating Systems
An operating system runs on the server or virtual server and controls access 
to computing resources. The operating system also includes a way to install
programs necessary for running your Python web application.


## Why are operating systems necessary?
An operating system makes many of the computing tasks we take for granted 
easy. For example, the operating system enables writing to files, 
communicating over a network and running multiple programs at once. 
Otherwise you'd need to control the CPU, memory, network, graphics card, 
and many other components with your own low-level implementation.

Without using an existing operating system like Linux, Mac OS X or Windows,
you'd be forced to write a new operating system as part of your web 
application.  It would be impossible to write features for your Python 
web application because you'd be too busy hunting down a memory leak in 
your assembly code, if you even were able to get that far.

Fortunately, the open source community provides Linux to the Python world 
as a rock solid free operating system for running our applications.


## Recommended operating systems
The only recommended operating system for production Python web stack 
deployments is Linux. There are several Linux distributions commonly used 
for running production servers. Ubuntu Long Term Support (LTS) releases, 
Red Hat Enterprise Linux, and CentOS are all viable options. 

Mac OS X is fine for development activities. Windows and Mac 
OS X are not appropriate for production deployments unless there is a 
major reason why you must use them in lieu of Linux.

### Ubuntu
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
April 2016, 
[16.04 Xenial Xerus](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes)
is the latest Ubuntu LTS release. Xenial Xerus includes 
[Python 3.5](/python-2-or-3.html) as its default Python version, which is
a major update compared with 2.7 in Ubuntu 14.04 LTS.


#### Ubuntu Python Packages
There are several 
[Aptitude](https://help.ubuntu.com/12.04/serverguide/aptitude.html)
packages found on Linux servers running a Python stack. These packages are: 

* [python-dev](http://packages.ubuntu.com/precise/python-dev) for header
  files and static library for Python

* [python-virtualenv](http://packages.ubuntu.com/precise/python-virtualenv)
  for creating and managing Python 
  [virtualenvs](https://virtualenv.pypa.io/en/latest/) to isolate library
  dependencies


### Red Hat and CentOS
[Red Hat Enterprise Linux](http://www.redhat.com/products/enterprise-linux/)
(RHEL) and [Community ENTerprise Operating System](http://www.centos.org/)
(CentOS) are the same distribution. The primary difference between the two 
is that CentOS is an open source, liberally licensed free derivative of RHEL.

RHEL and CentOS use a different package manager and command-line interface 
from Debian-based Linux distributions: RPM Package Manager (RPM) and the 
Yellowdog Updater, Modified (YUM). RPM has a specific .rpm file format
to handle the packaging and installation of libraries and applications. YUM
provides a command-line interface for interacting with the RPM system.


## Operating system resources
* [What is a Linux distribution and how do I choose the right one?](http://www.linux.org/threads/selecting-a-linux-distribution.4087/)

* Lifehacker's [guide to choosing a Linux distro](http://lifehacker.com/5889950/how-to-find-the-perfect-linux-distribution-for-you).

* The [Ops School curriculum](http://www.opsschool.org/en/latest/) is a
  comprehensive resource for learning about Linux fundamentals and how to
  perform the work that system administrators typically handle.

* Since Linux is your go-to production operating system, it's important to
  get comfortable with the Unix/Linux commands and philosophy. Study up on
  [this introduction to Unix tutorial](http://www.oliverelliott.org/article/computing/tut_unix/)
  to become more familiar with the operating system.

* [First 5 Minutes on a Server](http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers)
  shows the first several [security steps](/web-application-security.html)
  that should be done manually or automatically on any server you stand up.

* Digital Ocean has a detailed 
  [walkthrough for setting up Python web applications on Ubuntu](https://www.digitalocean.com/community/articles/how-to-set-up-ubuntu-cloud-servers-for-python-web-applications).

* [linux-internals](http://0xax.gitbooks.io/linux-insides/content/index.html) is
  a series of posts about how Linux works under the covers, starting from the
  low level booting process.


## Operating system learning checklist
1. Choose either a Debian-based Linux distribution such as Ubuntu or a 
   Fedora-based distribution like CentOS.

1. Harden the security through a few basic steps. Install basic security 
   packages such as 
   [fail2ban](http://www.fail2ban.org/wiki/index.php/Main_Page) and
   [unattended-upgrades](https://help.ubuntu.com/community/AutomaticSecurityUpdates).
   Create a new user account with sudo privileges and disable
   root logins. Disable password-only logins and use a public-private keypair 
   instead. Read more about hardening systems in the resources listed below.

1. Install Python-specific packages to prepare the environment for running a
   Python application. Which packages you'll need to install depends on the 
   distribution you've selected.

1. Read up on [web servers](/web-servers.html) as installing one will be the 
   next step in the deployment process.

