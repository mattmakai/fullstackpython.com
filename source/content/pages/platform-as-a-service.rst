=====================
Platform-as-a-service
=====================

:category: page
:slug: platform-as-a-service
:sort-order: 05


A platform-as-a-service (PaaS) provides infrastructure and a software layer
on which a web application is deployed. Running your web application from
a PaaS removes the need to know as much about the underlying servers, 
operating system, web server, and often the WSGI server. 

*Note*: If you are not interested in deploying to a PaaS you can move 
ahead to the `WSGI servers <../wsgi-servers.html>`_ section.

The PaaS layer defines how the 
application accesses resources such as computing time, files, and 
external services. The PaaS provides a higher-level abstraction for working
with computing resources than deploying an application to a server or IaaS.

A PaaS makes deployment and operations easier because it forces the developer
to conform applications to the PaaS architecture.

`Heroku <http://www.heroku.com/>`_, 
`Google App Engine <https://developers.google.com/appengine/>`_,
`Gondor <https://gondor.io/>`_, and
`OpenShift <https://openshift.redhat.com/community/get-started/python>`_ are
platform-as-services that support Python web applications. Each one requires
varying tradeoffs to deploy to their respective platforms.


.. image:: theme/img/servers-versus-paas.png
  :alt: Traditional LAMP server stack versus a Platform-as-a-Service stack
  :class: technical-diagram


If you go the PaaS route, you can skip over the operating system and web
server sections because they are baked into PaaS offerings. PaaS offerings
generally start at the WSGI server layer.

Platform-as-a-service resources
===============================
DevOps Django and Heroku Series by `Randall Degges <https://twitter.com/rdegges>`_:

* `Part One: Goals <http://www.rdegges.com/devops-django-part-1-goals/>`_

* `Part Two: The Pain of Deployment <http://www.rdegges.com/devops-django-part-2-the-pain-of-deployment/>`_

* `Part Three: The Heroku Way <http://www.rdegges.com/devops-django-part-3-the-heroku-way/>`_

* `Part Four: Choosing Heroku <http://rdegges.com/devops-django-part-4-choosing-heroku>`_

`PaaS bakeoff: Comparing Stackato, OpenShift, Dotcloud and Heroku for Django hosting and deployment <http://appsembler.com/blog/paas-bakeoff-comparing-stackato-openshift-dotcloud-and-heroku-for-django-hosting-and-deployment/>`_ by `Nate Aune <https://twitter.com/natea>`_

