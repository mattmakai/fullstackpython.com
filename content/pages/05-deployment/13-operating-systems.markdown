title: Operating Systems
category: page
slug: operating-systems
sortorder: 0513
toc: False
sidebartitle: Operating Systems
meta: Learn what operating system you should be using for you web application and resources to configure the OS on Full Stack Python.


An operating system runs on the server or virtual server and controls access 
to computing resources. The operating system also includes a way to install
programs necessary for running your Python web application.

<img src="/img/logos/operating-systems.jpg" width="100%" alt="Windows, Linux and Apple logos, copyright their respective owners." class="shot rnd outl">


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
The only recommended operating systems for production Python web stack 
deployments are 
[Linux](https://github.com/torvalds/linux)
and 
[FreeBSD](https://www.freebsd.org/). 
There are several Linux distributions commonly used 
for running production servers. Ubuntu Long Term Support (LTS) releases, 
Red Hat Enterprise Linux, and CentOS are all viable options. 

Mac OS X is fine for development activities. Windows and Mac 
OS X are not appropriate for production deployments unless there is a 
major reason why you must use them in lieu of Linux.

### Canonical's Ubuntu Linux
Ubuntu is a Linux distribution packaged by the 
[Canonical Ltd](http://www.canonical.com/) company. Ubuntu uses the
Debian distribution as a base for packages, including the 
[aptitude package manager](http://wiki.debian.org/Apt). For desktop versions
of Ubuntu, GNOME (until the 11.04 release, then again in 18.04) or Unity 
(11.10 until 17.10) is bundled with the distribution to provide a user 
interface.

Ubuntu [Long Term Support](https://wiki.ubuntu.com/LTS) (LTS) releases
are the recommended versions to use for deployments. LTS versions receive
five years of post-release updates from Canonical. Every two years, Canonical 
creates a new LTS release, which allows for an easy upgrade path as well 
as flexibility in skipping every other LTS release if necessary. As of
May 2018, 
[18.04 Bionic Beaver](http://releases.ubuntu.com/18.04/)
is the latest Ubuntu LTS release. Xenial Xerus includes 
[Python 3.6](/python-2-or-3.html) as its default Python version, which is
a major update compared with 2.7 in Ubuntu 14.04 LTS and a solid
improvement over Python 3.5 included in Ubuntu 16.04 LTS.


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


## Learning how operating systems work
* [Linux Performance](http://www.brendangregg.com/linuxperf.html) is an
  incredible site that links to a number of performance-focused materials
  that are useful when developing on or deploying to any Linux distribution.

* [Linux Journey](https://linuxjourney.com/) is a really well designed
  curriculum for learning Linux basics such as the command line, package
  management, text handling. There are also courses for more advanced topics
  such as how the kernel works, setting up logging and device management.

* The [Ops School curriculum](http://www.opsschool.org/) is a
  comprehensive resource for learning about Linux fundamentals and how to
  perform the work that system administrators typically handle.

* Since Linux is your go-to production operating system, it's important to
  get comfortable with the Unix/Linux commands and philosophy. Study up on
  [this introduction to Unix tutorial](http://www.oliverelliott.org/article/computing/tut_unix/)
  to become more familiar with the operating system.

* [First 5 Minutes on a Server](http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers)
  shows the first several [security steps](/web-application-security.html)
  that should be done manually or automatically on any server you stand up.

* [How to Use the Command Line for Apple macOS and Linux](https://www.taniarascia.com/how-to-use-the-command-line-for-apple-macos-and-linux/)
  is useful for learning the shell and is even helpful for Windows now
  that the 
  [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
  allows you to work with Widnows as if it is a \*nix operating system.

* [Linux System Mining with Python](https://echorand.me/linux-system-mining-with-python.html)
  shows how to gather system information using the `platform` module and 
  some of your own Python code.

* Digital Ocean has a detailed 
  [walkthrough for setting up Python web applications on Ubuntu](https://www.digitalocean.com/community/articles/how-to-set-up-ubuntu-cloud-servers-for-python-web-applications).

* [linux-internals](http://0xax.gitbooks.io/linux-insides/content/index.html) is
  a series of posts about how Linux works under the covers, starting from the
  low level booting process.

* While not quite necessary to run your Python application, if you want to
  dig into how operating systems are built, check out this free book
  [How to Make a Computer Operating System](https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System),
  which was originally written by a high school student and later updated
  as he became a professional software developer.

* [ops-class.org](https://www.ops-class.org/) provides an online lecture
  videos, slides and sample exams for learning how operating systems are 
  built.

* [Operating Systems: Three Easy Pieces](http://pages.cs.wisc.edu/~remzi/OSTEP/)
  is a free book by University of Wisconsin Computer Science professors
  that teaches how operating systems are built. Although you do not know
  exactly how to build your own OS to use one, understanding the 
  foundation for how software works is incredibly helpful in unexpected
  ways while developing and operating your applications.

* [Operating systems: From 0 to 1](https://tuhdo.github.io/os01/) is a 
  self-learner resource for writing your own operating system from scratch.


### Choosing an OS resources
macOS and Linux are generally preferred by Python developers over Windows 
because many Python packages like [gevent](http://www.gevent.org/) simply do 
not work on Windows. Others such as [Ansible](/ansible.html) cannot be used 
as intended on Windows without major hacks.

The following operating system resources cover perspectives on why developers
chose one operating system over others.

* [Finding an alternative to Mac OS X: Part 1](http://bitcannon.net/post/finding-an-alternative-to-mac-os-x/),
  [part 2](http://bitcannon.net/post/finding-an-alternative-to-mac-os-x-part-2/)
  and [part 3: being productive on Linux](http://bitcannon.net/post/being-productive-on-linux/)
  explain what alternative applications are available for common functionality
  such as the Gnome windowing system, email and terminal. There are a ton
  of tips and tricks in there for getting comfortable with Linux as well as
  a lot of thought put into what and why the developer wants his environment
  set up in a particular way.

* [Why I switched from OS X to GNU/Linux](https://jeena.net/why-i-switchedfrom-osx-to-linux)
  explains the rationale for switching from the Apple-based operating system
  to Linux along with what applications the author now uses.

* [Ultimate Linux on the Desktop](https://blog.jessfraz.com/post/ultimate-linux-on-the-desktop/)
  explains one experienced developer's Linux desktop development environment
  for getting coding work done.

* Lifehacker's [guide to choosing a Linux distro](http://lifehacker.com/5889950/how-to-find-the-perfect-linux-distribution-for-you).

* [Distro chooser](https://distrochooser.de/?l=2) walks you through a set of
  sixteen questions to determine which Linux distribution could fit your
  personal needs.
  

### Operating system learning checklist
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

