Servers
=======

:category: page
:slug: servers
:sort-order: 2

There are several options for setting up infrastructure to serve your
web application:

1. "Bare metal" servers

2. Virtualized servers

3. Infrastructure-as-a-service

4. Platform-as-a-service

Bare metal
----------
The most control and also the highest maintenance. Buy actual hardware 
from a vendor either pre-built or as a collection of components that 
you assemble yourself.


Virtualized servers
-------------------
Virtual private servers (VPSs) are slices of hardware on top of a larger
bare metal server. Virtualization software such as 
`Xen <http://www.xen.org/>`_ and
`VMWare <http://www.vmware.com/virtualization/what-is-virtualization.html>`_
allow providers such as `Linode <http://www.linode.com/>`_ and
`prgmr <http://prgmr.com/xen/>`_ (as well as a many others) to provide
fractions of a full server that appear as their own instances. For example,
a server with an 8-core Xeon processor and 16 gigabytes of memory can be
sliced into 8 pieces with the equivalent of 1-core and 2 gigabytes of
memory.

The primary disadvantage of virtualized servers is that there is resource
overhead in the virtualization process. In addition, physical constraints
such as heavy I/O operations by a single virtualized instance on persistent 
storage can cause performance bottlenecks for other virtualized instances on
the shared server.

Server Monitoring
-----------------
There are several important resources to monitor the server level of a web 
stack:

1. Server uptime
2. CPU utilization
3. Memory utilization
4. Persistence storage consumed versus free
5. Network bandwidth and latency

Resources
---------

