title: Containers
category: page
slug: containers
sortorder: 0535
toc: False
sidebartitle: Containers
meta: Containers are a concept where processes are run isolated on a operating system.


# Containers
Containers are an [operating system](/operating-systems.html)-level 
isolation mechanism for running processes and other system resources from
other containers and the base system.


## Are containers new?
Containers are not conceptually new, dating back to around the 1970s, but
they gained rapid adoption starting in 2012 when several Linux distributions
began integrating containers tools generally made it more practical to
use them. Previously, to use containers a developer would need to use a
less common operating system or distribution customized with some sort of
virtual machine feature. Using containers was basically not supported in typical
deployment scenarios.


### Containers history and introduction
The following resources do a great job of explaining where the containers
concept came from, how they differ from virtual machines and why they are
useful.

* [A brief history of containers](https://mesosphere.com/blog/brief-history-containers/)
  has some solid context for why containers have taken off in the last
  several years, including the integration of operating system container
  virtualization in most distributions as well as the creation of management 
  tools such as [Docker](/docker.html), Kubernetes, Docker Swarm and 
  Mesosphere.

* [Setting the Record Straight: containers vs. Zones vs. Jails vs. VMs](https://blog.jessfraz.com/post/containers-zones-jails-vms/)
  compares and contrasts the designs of Linux containers, zones, jails
  and virtual machines. Containers typically take advantage of primitives
  but are more complicated because they have more individual parts put
  together while zones and jails are designed as top-level operating
  system components. There are advantages and disadvantages of these
  approaches that you should understand as you use each one.

* [Containers and Distributed Systems: Where They Came From and Where They’re Going](https://mesosphere.com/blog/containers-distributed-systems/)
  is an interview that digs into the past, present and future of
  containers based on the experience of Chuck McManis who has worked
  on building jails and other process isolation abstractions into
  operating systems.

* [A Practical Introduction to Container Terminology](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction/)
  has both some solid introductory information on containers as well as
  a good description of terms such as container host, registry server,
  image layer, orchestration and many others that come up frequently
  when using containers.

* [Containers from scratch](https://ericchiang.github.io/post/containers-from-scratch/)
  explains how Linux features such as `cgroups`, `chroot` and namespaces
  are used by container implementations.

* [Running containers without Docker](https://jvns.ca/blog/2016/10/26/running-container-without-docker/)
  reviews a migration path for an organization that already has a bunch of
  infrastructure but sees advantages in using containers. However, the 
  author explains why you can use containers without Docker even if you
  eventually plan to use Docker, Kubernetes or other container tools and
  orchestration layer.

* [mocker](https://github.com/tonybaloney/mocker) is a Docker imitation
  open source project written in all Python which is intended for learning
  purposes.


### Working with containers
You can get started using containers once you understand some of the 
terminology and work through a couple of introductory tutorials like the ones
listed above. Check out the below resources when you want to do more advanced 
configurations and dig deeper into how containers work.

* [Linux containers in 500 lines of code](https://blog.lizzie.io/linux-containers-in-500-loc.html)
  is a bonkers in-depth post about building your own simplified, but not 
  simple version of Docker to learn how it works.


### Container security resources
Container security is a hot topic because there are so many ways of screwing
it up, just like any infrastructure that runs your applications. These
resources explain security considerations specific to containers.

* [Building Container Images Securely on Kubernetes](https://blog.jessfraz.com/post/building-container-images-securely-on-kubernetes/)
  discusses some of the issues with building containers and why the
  author created [img](https://github.com/genuinetools/img) as a tool
  to help solve the problems she was seeing.
 


