title: Kubernetes
category: page
slug: kubernetes
sortorder: 0537
toc: False
sidebartitle: Kubernetes
meta: Kubernetes is a container orchestration system for deploying, scaling and managing applications.


[Kubernetes](https://kubernetes.io/) 
([source code](https://github.com/kubernetes/kubernetes)) is a 
[container](/containers.html) orchestration system for 
[deploying](/deployment.html), scaling and [operating](/devops.html) 
applications.

<a href="https://kubernetes.io/" style="border: none;"><img src="/img/logos/kubernetes.png" width="100%" alt="Official Kubernetes logo." class="shot" style="padding: 6px 0 6px 0"></a>


### Kubernetes tools
* [Helm](https://helm.sh/) ([source code](https://github.com/helm/helm))
  is a package manager for Kubernetes charts, which are the way to define
  common types of Kubernetes cluster arrangements, like [MySQL](/mysql.html),
  [Cassandra](/apache-cassandra.html) or [Jenkins](/jenkins.html).

* [Gitkube](https://gitkube.sh/) 
  ([source code](https://github.com/hasura/gitkube)) makes it possible to
  deploy an application to Kubernetes using `git push`, similar to how
  Heroku popularized making 
  [platform-as-a-service](/platform-as-a-service.html) deployments easy.

* [Kompose](http://kompose.io/index) 
  ([source code](https://github.com/kubernetes/kompose))
  translate Docker Compose files into Kubernetes configuration resources.

* [skaffold](https://skaffold.dev/). [Using Kubernetes for local development](https://nemethgergely.com/using-kubernetes-for-local-development/index.html)
  is a good starting place for more information on getting started with
  Skaffold.

* [kubethanos](https://github.com/berkay-dincer/kubethanos) is a tool to kill 
  half of your Kubernetes pods at random, to test the resilience of your
  infrastructure under highly chaotic scenarios.


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

* [How we designed our Kubernetes infrastructure on AWS](https://developer.atlassian.com/blog/2017/07/kubernetes-infra-on-aws/)
  explains how the Kubernetes Infrastructure Technology Team (yes, that
  abbreviates to KITT in honor of the 
  [1980s Knight Rider TV show](https://www.imdb.com/title/tt0083437/))
  at Atlassian starting using the tool and how they have built infrastructure
  around it for the company to operate their container-ized applications.

* [10 Most Common Reasons Kubernetes Deployments Fail](https://kukulinski.com/10-most-common-reasons-kubernetes-deployments-fail-part-1/)
  goes over many of the top technical reasons why issues come up with
  Kubernetes and what you need to do to avoid or work through them.

* [Draft vs Gitkube vs Helm vs Ksonnet vs Metaparticle vs Skaffold](https://blog.hasura.io/draft-vs-gitkube-vs-helm-vs-ksonnet-vs-metaparticle-vs-skaffold-f5aa9561f948/)
  gives a great overview of the most popular tools that make it easier to
  use Kubernetes.

* [Architecting applications for Kubernetes](https://www.digitalocean.com/community/tutorials/architecting-applications-for-kubernetes)
  is stuffed full of great design advice that is now available as people
  having been using Kubernetes for a couple of years.

* ["Let’s use Kubernetes!" Now you have 8 problems](https://pythonspeed.com/articles/dont-need-kubernetes/)
  is a counter-argument for why you should be cautious about introducing
  the significant complexity overhead of Kubernetes (or any related tools)
  into your environment unless you really need the advantages that they can
  provide. Each developer, team and organization should perform an explicit
  cost-benefit analysis to make sure the tool's scability, reliability
  and related functionality will outweigh the downsides.

* [How Zolando manages 140+ Kubernetes clusters](https://srcco.de/posts/how-zalando-manages-140-kubernetes-clusters.html)
  covers the architecture, monitoring and workflow of a team that has 
  to run a decent number of clusters for their development teams.


### Kubernetes tutorials
* [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
  is a tutorial that walks you through manually setting up a Kubernetes
  cluster. The purpose is to teach you what is happening at each step instead 
  of performing everything through automation like you normally would after
  you understand how to use the tool.

* [Kubernetes Any% Speedrun](https://elliot.pro/blog/kubernetes-any-percent-speedrun.html)
  hilariously presents the pain of using Kubernetes and gives the basic
  steps for getting a deployment up and running.

* [A Gentle introduction to Kubernetes with more than just the basics](https://github.com/eon01/kubernetes-workshop)
  is a Git README tutorial with clear steps for how to get started running
  a Kubernetes cluster.

* [Anatomy of my Kubernetes Cluster](https://ttt.io/anatomy-of-my-kubernetes-cluster)
  shows how one developer created their own Raspberry Pi cluster that could
  run Kubernetes to learn more about how it works.

* [The cult of Kubernetes](https://christine.website/blog/the-cult-of-kubernetes-2019-09-07)
  is a hilarious rant that also manages to teach the reader a lot about how to
  avoid some big issues the author ran into while working with Kubernetes for
  simple starter projects.

* [Kubernetes by Example](http://kubernetesbyexample.com/) provides the 
  commands and code for you to get started with the core Kubernetes concepts.

* [Your instant Kubernetes cluster](https://blog.alexellis.io/your-instant-kubernetes-cluster/)
  provide a concise set of instructions for setting up a cluster.

* [A tutorial introduction to Kubernetes](http://okigiveup.net/a-tutorial-introduction-to-kubernetes/)
  covers a bunch of introductory steps using an example Python application.

* [An Example Of Real Kubernetes: Bitnami](https://engineering.bitnami.com/articles/an-example-of-real-kubernetes-bitnami.html)
  gives instructions for what to do after you have finished creating
  a Kubernetes cluster and learned the "Hello, World!"-style example.

* [Kubernetes Production Patterns](https://github.com/gravitational/workshop/blob/master/k8sprod.md)
  is a tutorial with good and bad practices so you can learn what to do
  and what to avoid in your Kubernetes infrastructure.

* [Django Production Deployment on GCP with Kubernetes](https://www.agiliq.com/blog/2018/07/django-on-kubernetes/)
  uses Helm to make it easier to deploy the example [Django](/django.html)
  web app with a [PostgreSQL](/postgresql.html) backend.

* [K8s YAML Alternative: Python](https://www.phillipsj.net/posts/k8s-yaml-alternative-python/)
  shows how you can use Python scripts instead of YAML to configure
  your Kubernetes clusters.
