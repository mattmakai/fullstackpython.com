title: Servers
category: page
slug: servers
sortorder: 0502
toc: False
sidebartitle: Servers
meta: Servers are required to run web applications. Learn more about setting up servers on Full Stack Python.


Servers are the physical infrastructure to run all the layers of software
so your web application can respond to requests from clients such as web 
browsers.


## Why are servers necessary?
Your web application must live somewhere other than your own desktop or 
laptop. Servers should ideally be accessible 24 hours a day, 7 days a week, 
with no unplanned downtime. The servers that host your web application for
actual users (as opposed to test users) are known as *production* servers.
Production servers hold real data (again as opposed to test data) and must be 
secure against unauthorized access.


## Bare metal servers
The term *bare metal* refers to purchasing the actual hardware and hooking 
it up to the Internet either through a business-class internet service 
provider (ISP) or 
[co-locating the server](http://webdesign.about.com/od/colocation/a/what_colocation.htm)
with other servers. A "business-class" ISP is necessary because
most residential Internet service agreements explicitly prohibit running
web servers on their networks. You may be able to get away with low traffic
volume but if your site serves a lot of traffic it will alert an ISP's
filters.

The bare metal option offers the most control over the server configuration,
usually has the highest performance for the price, but also is the most
expensive upfront option and the highest ongoing maintenance. With bare
metal servers the ongoing operating cost is the electricity the server(s)
use as well as handling repairs when server components malfunction. You're
taking on manual labor working with hardware as well as the rest of the
software stack.

Buy actual hardware from a vendor either pre-built or as a collection of 
components that you assemble yourself. You can also buy 
pre-configured servers from Dell or HP. Those servers tend to be in
smaller case form factors (called "blades") but are correspondingly more 
expensive than putting off-the-shelf components together yourself in a 
standard computer case.


## Virtualized servers
Virtual private servers (VPSs) are slices of hardware on top of a larger
bare metal server. Virtualization software such as 
[Xen](http://www.xen.org/) and
[VMWare](http://www.vmware.com/virtualization/what-is-virtualization.html)
allow providers such as [Linode](http://www.linode.com/) and
[prgmr](http://prgmr.com/xen/) (as well as a many others) to provide
fractions of a full server that appear as their own instances. For example,
a server with an 8-core Xeon processor and 16 gigabytes of memory can be
sliced into 8 pieces with the equivalent of 1-core and 2 gigabytes of
memory.

The primary disadvantage of virtualized servers is that there is resource
overhead in the virtualization process. In addition, physical constraints
such as heavy I/O operations by a single virtualized instance on persistent 
storage can cause performance bottlenecks for other virtualized instances on
the shared server. Choosing virtualized server hosting should be based on
your needs for urgency of service ticket requests and the frequency you
require for ongoing maintenance such as persistent storage backups.


### Virtualized servers resources
* [Choosing a low cost VPS](http://blog.redfern.me/choosing-a-low-cost-vps/)
  reviews the factors that you should weigh when deciding on hosting 
  providers.

* [How to set up your Linode for maximum awesomeness](http://feross.org/how-to-setup-your-linode/)
  shows how to work with a VPS once you've got the server up and running.

* [CPU Load Averages](http://jvns.ca/blog/2016/02/07/cpu-load-averages/)
  explains how to measure CPU load and what to do about it.

* [Which cloud hosting company to choose in 2017?](https://www.webstack.de/blog/e/cloud-hosting-provider-comparison-2017/)
  compares DigitalOcean, Linode, Vultr, OVH and Scaleway in various 
  benchmarks such as CPUs, memory, disk space, network performance, traffic 
  capacity and cost. At the end of the article the author also provides some
  qualitative feedback on the strengths and weaknesses of each services'
  offerings.


## Infrastructure-as-a-service
Infrastructure-as-a-service (IaaS) overlaps with virtualized servers 
because the resources are often presented in the same way. The 
difference between virtualized servers and IaaS is the granularity of the
billing cycle. IaaS generally encourages a finer granularity based on minutes
or hours of server usage instead of on monthly billing cycles.

IaaS can be used in combination with virtualized servers to provide 
dynamic upscaling for heavy traffic. When traffic is low then virtualized
servers can solely be used. This combination of resources reduces cost at
the expense of greater complexity in the dynamically scaled infrastructure. 

The most common IaaS platforms are 
[Amazon Web Services](http://aws.amazon.com/) and 
[Rackspace Cloud](http://www.rackspace.com/cloud/).

The disadvantage to IaaS platforms is the lock-in if you have to write
custom code to deploy, dynamically scale, and generally understand your
infrastructure. Every platform has its quirks. For example, 
Amazon's standard [Elastic Block Store](http://aws.amazon.com/ebs/) storage
infrastructure has at least an order of magnitude worse I/O throughput 
than working with your local disk. Your application's database queries may 
work great locally but then when you deploy the performance is inadequate.
Amazon has [higher throughput EBS instances](http://aws.amazon.com/about-aws/whats-new/2012/07/31/announcing-provisioned-iops-for-amazon-ebs/)
but you will pay correspondingly more for them. EBS throughput is just 
one of many quirks you need to understand before committing to an 
IaaS platform.


### Infrastructure-as-a-service resources
* [The cloud versus dedicated servers](http://www.screamingatmyscreen.com/2012/12/the-cloud-vs-dedicated-servers/)

* [5 common server setups for your web application](https://www.digitalocean.com/community/articles/5-common-server-setups-for-your-web-application)
  is a great introduction to how hosting can be arranged.

* [Apache Libcloud](http://libcloud.apache.org/) is a Python library that
provides a unified API for many cloud service providers.

* [Amazon Web Services has official documentation](http://aws.amazon.com/python/) for running Python web applications.

* [boto](https://github.com/boto/boto) is an extensive and well-tested 
Python library for working with Amazon Web Services.

* [Poseidon](https://github.com/changhiskhan/poseidon) is a Python commandline
  interface for managing Digital Ocean droplets (servers).


## Servers learning checklist
1. Sign up for a hosting provider. I recommend getting a 
   [Linode VPS](https://www.linode.com/?r=bfeecaf55a83cd3dd224a5f2a3a001fdf95d4c3d) 
   to set up your initial infrastructure and deploy your web application 
   there. [Digital Ocean](https://www.digitalocean.com/) and 
   [prgrmr](http://prgmr.com/xen/) are other VPS options. You can change
   hosting providers later after the deployment process is automated.

1. Provision your first server. It will be ready but in a shutdown state 
   while awaiting your instructions.

1. Move to the [operating systems](/operating-systems.html) section to learn
   how to load Ubuntu 14.04 LTS as a base OS for Python web applications.

