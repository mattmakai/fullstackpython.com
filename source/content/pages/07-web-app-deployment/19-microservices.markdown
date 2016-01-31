title: Microservices
category: page
slug: microservices
sort-order: 0719
meta: Microservices are an architecture where independent, functionality-contained programs communicate via network calls.


# Microservices
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
hip buzzword among 
[ivory tower architects](http://www.igloocoder.com/2271/ivory-tower-architect).

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
* Martin Fowler's 
  [microservices](http://martinfowler.com/articles/microservices.html)
  article is one of the best in-depth explanations for what microservices are
  and why to consider them as an architectural pattern.

* [On monoliths and microservices](http://dev.otto.de/2015/09/30/on-monoliths-and-microservices/)
  provides some advice on using microservices in a fairly early stage of
  a software project's lifecycle.

* [Developing a RESTful microservice in Python](http://www.skybert.net/python/developing-a-restful-micro-service-in-python/)
  is a good story of how an aging Java project was replaced with a
  microservice built with Python and Flask.

* [Microservices: The essential practices](http://technologyconversations.com/2015/11/10/microservices-the-essential-practices/)
  first goes over what a monolith application looks like then dives into what 
  operations you need to support potential microservices. For example, you really 
  need to have continuous integration and deployment already set up. This is a
  good high-level overview of the topics many developers aren't aware of when they
  embark on converting a monolith to microservices.

* [The State of Microservices Today](http://blog.codeship.com/the-state-of-microservices-today/)
  provides some general trends and broad data showing the increasing 
  popularity of microservices heading into 2016. This is more of an
  overview of the term than a tutorial but useful context for both
  developers and non-developers.

