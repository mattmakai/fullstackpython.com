title: Virtual Private Servers (VPS)
category: page
slug: virtual-private-servers-vps
sortorder: 0806
toc: False
sidebartitle: Virtual Private Servers
meta: A virtual private server is a software-isolated portion of hardware run with a hypervisor on a physical server.


# Virtual private servers (VPS)
Virtual private servers (VPSs) are sandboxed slices of hardware run with a
hypervisor running on top of a physical server. Virtualization software 
such as [Xen](http://www.xenproject.org/) and 
[VMWare](http://www.vmware.com/virtualization) allow a providers' 
customers to use fractions of a full server that appear as their own 
independent instances. For example, a server with an 8-core processor 
and 16 gigabytes of memory can be roughly virtualized into 8 pieces with 
the equivalent of 1-core and 2 gigabytes of memory.

The primary disadvantage of virtualized servers is that there is resource 
overhead in the virtualization process. But for our web application 
deployment, a single well-configured virtual private server provides 
more than enough performance and represents a huge cost savings over 
purchasing dedicated hardware. 
