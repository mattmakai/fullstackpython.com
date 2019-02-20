title: Kubernetes
category: page
slug: kubernetes
sortorder: 0537
toc: False
sidebartitle: Kubernetes
meta: Kubernetes is a container orchestration system for deploying, scaling and managing applications.


# Kubernetes
[Kubernetes](https://kubernetes.io/) 
([source code](https://github.com/kubernetes/kubernetes)) is a 
[container](/containers.html) orchestration system for 
[deploying](/deployment.html), scaling and [operating](/devops.html) 
applications.

<a href="https://kubernetes.io/" style="border: none;"><img src="/img/logos/kubernetes.png" width="100%" alt="Official Kubernetes logo." class="shot" style="padding: 6px 0 6px 0"></a>


### Kubernetes background and retrospectives
* [Borg, Omega and Kubernetes](https://queue.acm.org/detail.cfm?id=2898444)
  goes into the history of Borg and Omega, projects that preceded 
  Kubernetes' creation. There are a ton of great notes on why they developed
  the project in certain ways and what they knew to avoid based on the
  prior work on Borg and Omega.

* [Kubernetes at GitHub](https://githubengineering.com/kubernetes-at-github/)
  provides a retrospective on transitioning GitHub's infrastructure from
  a traditional Ruby on Rails deployment architecture to a more scalable
  container-based Kubernetes system. There are some great details on the
  steps in the transition and ramping up capacity until it was the full
  system for github.com and other critical services.

* [Reasons Kubernetes is cool](https://jvns.ca/blog/2017/10/05/reasons-kubernetes-is-cool/)
  breaks past the "why would I ever need this?" initial developer reaction
  and gives solid reasons such as better visibility into all of the services
  running on your Kubernetes cluster and potentially much faster deployment 
  after appropriate configuration.


### Kubernetes tutorials
* [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
  is a tutorial that walks you through manually setting up a Kubernetes
  cluster. The purpose is to teach you what is happening at each step instead 
  of performing everything through automation like you normally would after
  you understand how to use the tool.

* [Kubernetes by Example](http://kubernetesbyexample.com/) provides the 
  commands and code for you to get started with the core Kubernetes concepts.

* [Kubernetes Production Patterns](https://github.com/gravitational/workshop/blob/master/k8sprod.md)
  is a tutorial with good and bad practices so you can learn what to do
  and what to avoid in your Kubernetes infrastructure.


