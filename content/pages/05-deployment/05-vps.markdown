title: Virtual Private Servers (VPS)
category: page
slug: virtual-private-servers-vps
sortorder: 0505
toc: False
sidebartitle: Virtual Private Servers
meta: A virtual private server is a software-isolated portion of hardware run with a hypervisor on a physical server.


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


### VPS providers
There are many VPS providers and their cost ranges dramatically based on
reliability, support, security and uptime. Make sure to choose a provider
that has a solid reputation unless you are willing to rebuild your server
on another provider whenever issues hit your service. 

A few providers I currently use to host my Python web applications:

* [Linode](https://www.linode.com/)

* [Digital Ocean](https://www.digitalocean.com/)

* [Amazon Web Services' Lightsail](https://amazonlightsail.com/)


### VPS comparisons
* [Ready. Steady. Go! The speed of VM creation and SSH access on AWS, DigitalOcean, Linode, Vexxhost, Google Cloud, Rackspace and Microsoft Azure](https://blog.cloud66.com/ready-steady-go-the-speed-of-vm-creation-and-ssh-key-access-on-aws-digitalocean-linode-vexxhost-google-cloud-rackspace-and-microsoft-azure/)
  and
  [Comparing the speed of VM creation and SSH access of cloud providers](https://blog.cloud66.com/part-2-comparing-the-speed-of-vm-creation-and-ssh-access-on-aws-digitalocean-linode-vexxhost-google-cloud-rackspace-packet-cloud-a-and-microsoft-azure/)
  are one way to measure some of the infrastructure speed provided by several
  cloud vendors. The virtual machine and SSH access data points are taken in 
  multiple regions. It's unclear how these metrics would change over time based
  on backend tweaks made by each provider.

* The [State of Cloud Instance Provisioning](https://ahmet.im/blog/cloud-instance-provisioning/)
  explains the tools and operations behind how AWS, 
  [DigitalOcean](/digitalocean.html), Google Cloud and Microsoft Azure stand up
  virtual machine instances for you to use.

* [VPS $5 Showdown - October 2018 - DigitalOcean vs. Lightsail vs. Linode vs. Vultr](https://joshtronic.com/2018/10/15/vps-showdown-october-2018/)
  compares and contrasts the cheapest options for four popular virtual 
  private server providers.

* [VPS comparisons](https://github.com/joedicastro/vps-comparison) uses
  [Ansible](/ansible.html) to get some data around provisioning speed
  and system performance. The whole 
  [README](https://github.com/joedicastro/vps-comparison/blob/master/README.org)
  file in that repository has a ton of useful information and summaries
  of the tested providers.
