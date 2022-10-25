title: Microservices
category: page
slug: microservices
sortorder: 0445
toc: False
sidebartitle: Microservices
meta: Microservices are an architecture where independent, functionality-contained programs communicate via network calls.


Microservices are an application architecture style where independent,
self-contained programs with a single purpose each can communicate with
each other over a network. Typically, these microservices are able to be
deployed independently because they have strong separation of 
responsibilities via a well-defined specification with significant 
backwards compatibility to avoid sudden dependency breakage.


## Why are microservices getting so much buzz?
Microservices follow in a long trend of software architecture patterns
that become all the rage. Previously, 
[CORBA](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture) 
and (mostly XML-based) service-oriented architectures (SOA) were the
hip buzzword among ivory tower architects.

However, microservices have more substance because they are typically based
on [RESTful APIs](/application-programming-interfaces.html) that are far
easier for actual software developers to use compared with the previous 
complicated XML-based schemas thrown around by enterprise software companies.
In addition, successful applications begin with a monolith-first approach using
a single, shared application codebase and deployment. Only after the application
proves its usefulness is it then broken down into microservice components to
ease further development and deployment. This approach is called the 
"monolith-first" or 
"[MonolithFirst](http://martinfowler.com/bliki/MonolithFirst.html)" pattern.


### Microservice resources
* James Lewis's 
  [microservices](http://martinfowler.com/articles/microservices.html)
  article is one of the best in-depth explanations for what microservices are
  and why to consider them as an architectural pattern.

* [Developing a RESTful microservice in Python](http://www.skybert.net/python/developing-a-restful-micro-service-in-python/)
  is a good story of how an aging Java project was replaced with a
  microservice built with Python and Flask.

* [Microservices: The essential practices](http://technologyconversations.com/2015/11/10/microservices-the-essential-practices/)
  first goes over what a monolith application looks like then dives into what 
  operations you need to support potential microservices. For example, you really 
  need to have continuous integration and deployment already set up. This is a
  good high-level overview of the topics many developers aren't aware of when they
  embark on converting a monolith to microservices.

* [Using Nginx to Load Balance Microservices](https://hagbarddenstore.se/posts/2016-03-11/using-nginx-to-load-balance-microservices/)
  explains how an Nginx instance can use configuration values from etcd
  updated by confd as the values are modified. This setup can be useful for
  load balancing microservices as the backend services are brought up
  and taken down.

* [How Microservices have changed and why they matter](http://thenewstack.io/microservices-changed-matter/)
  is a high level overview of the topic with some quotes from
  various developers around the industry.

* [The State of Microservices Today](http://blog.codeship.com/the-state-of-microservices-today/)
  provides some general trends and broad data showing the increasing 
  popularity of microservices heading into 2016. This is more of an
  overview of the term than a tutorial but useful context for both
  developers and non-developers.

* [bla bla microservices bla bla](http://jonasboner.com/bla-bla-microservices-bla-bla/) 
  is a transcript for a killer talk on microservices that breaks down the
  important first principles of distributed systems, including asynchronous 
  communication, isolation, autonomicity, single responsibility, 
  exclusive state, and mobility. The slides along with the accompanying
  text go into how reality gets messy and how to embrace the constraints
  inherent in distributed systems.

* In the 
  [Microservices with Docker, Flask, and React](https://testdriven.io/bundle/microservices-with-docker-flask-and-react/?utm_source=fsp)
  course bundle, you will learn how to quickly spin up a reproducible 
  development environment with Docker to manage a number of microservices. 
  Once the app is up and running locally, you'll learn how to deploy it to 
  an Amazon EC2 instance. Finally, we'll look at scaling the services on 
  Amazon EC2 Container Service (ECS).

* [Should I use microservices?](https://www.oreilly.com/ideas/should-i-use-microservices)
  contains a high-level perspective on why or why not use microservices
  as an architectural choice.

* [Zuul](https://github.com/Netflix/zuul) is an open source proxy for combining multiple microservices into a 
  unified API call. Check out this post on 
  [Using Netflix Zuul to Proxy your Microservices](https://blog.heroku.com/using_netflix_zuul_to_proxy_your_microservices)
  to learn more and get started using it.

* [The Majestic Monolith](https://m.signalvnoise.com/the-majestic-monolith/)
  explains the advantages of a monolithic architecture and how it's worked
  amazingly well for the Basecamp small development team.

* [Developing a RESTful micro service in Python](http://skybert.net/python/developing-a-restful-micro-service-in-python/)
  goes into detail on how one development team rebuilt an existing Java
  application as a microservice in Python with [Flask](/flask.html).

* [Documenting microservices](https://blog.codeship.com/documenting-microservices/)
  has some good thoughts on how to explain your microservice API to
  other developers such as clearly showing all of the endpoints as well as
  the intersection of multiple endpoints.

* [Best practices for building a microservice](https://www.vinaysahni.com/best-practices-for-building-a-microservice-architecture)
  is an exhaustive (and somewhat exhausting to read!) list with what you
  should think about as you build your microservice.

* [The Hardest Part About Microservices: Your Data](http://blog.christianposta.com/microservices/the-hardest-part-about-microservices-data/)
  presents a data-centric view on how to structure and transport data
  in a microservices architecture.

* [Deleting data distributed throughout your microservices architecture](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2020/deleting-data-distributed-throughout-your-microservices-architecture.html)
  examines how Twitter handles issues with discoverability, access and erasure
  in their microservices-heavy production environment.
