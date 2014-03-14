title: Platform-as-a-service
category: page
slug: platform-as-a-service
sort-order: 05


# Platform-as-a-service
A platform-as-a-service (PaaS) provides infrastructure and a software layer
on which a web application is deployed. Running your web application from
a PaaS removes the need to know as much about the underlying servers, 
operating system, web server, and often the WSGI server. 

*Note*: If you are not interested in deploying to a PaaS you can move 
ahead to the [WSGI servers](../wsgi-servers.html) section.

The PaaS layer defines how the application accesses resources such as 
computing time, files, and external services. The PaaS provides a 
higher-level abstraction for working with computing resources than deploying 
an application to a server or IaaS.

A PaaS makes deployment and operations easier because it forces the developer
to conform applications to the PaaS architecture. For example, Heroku looks for
Python's requirements.txt file in the base directory of the repository during
deployment because that is the de facto community standard.

[Heroku](http://www.heroku.com/)
[Google App Engine](https://developers.google.com/appengine/)
[Gondor](https://gondor.io/), and
[OpenShift](https://openshift.redhat.com/community/get-started/python>) are
PaaS that support Python web applications. Each one requires varying tradeoffs 
to deploy to their respective platforms.

<img src="theme/img/servers-versus-paas.png" width="100%" alt="Traditional LAMP server stack versus a Platform-as-a-Service stack" class="technical-diagram" />

If you go the PaaS route, you can skip over the operating system and web
server sections because they are baked into PaaS offerings. PaaS offerings
generally start at the WSGI server layer. 


## Platform-as-a-service responsibilities
Although PaaS offerings simplify setting up and maintaining the servers,
operating system, and web server, developers still have responsibilities for other
layers of their web stack.

While it's useful to know the operating system that underpins your PaaS, for 
example Heroku uses Ubuntu 10.04, you will not have to know as much about 
securing the operating system and server level. However, web applications deployed
to a PaaS are just as vulnerable to security breaches at the application level
as a standard LAMP stack. It's still your responsibility to ensure the web
application framework and your app itself is up to date and secured. See the
[security section](../web-application-security.html) for further information.



## Platform-as-a-service resources
* [PaaS bakeoff: Comparing Stackato, OpenShift, Dotcloud and Heroku for Django hosting and deployment](http://appsembler.com/blog/paas-bakeoff-comparing-stackato-openshift-dotcloud-and-heroku-for-django-hosting-and-deployment/) by [Nate Aune](https://twitter.com/natea).

* [Deploying Django](http://www.deploydjango.com/) by Randall Degges is 
  another great free resource about Heroku.

* Heroku's 
  [Python deployment documentation](https://devcenter.heroku.com/articles/getting-started-with-python)
  provides clear examples for how to work with virtualenv, pip and 
  requirementst.txt to get a applications deployed to their platform.

* Miguel Grinberg's Flask tutorial contains an entire post on deploying 
  [Flask applications to Heroku](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud).

* This series on DevOps Django by 
  [Randall Degges](https://twitter.com/rdegges) is great reading for 
  using the Heroku service:

    * [Part One: Goals](http://www.rdegges.com/devops-django-part-1-goals/)
    * [Part Two: The Pain of Deployment](http://www.rdegges.com/devops-django-part-2-the-pain-of-deployment/)
    * [Part Three: The Heroku Way](http://www.rdegges.com/devops-django-part-3-the-heroku-way/)
    * [Part Four: Choosing Heroku](http://rdegges.com/devops-django-part-4-choosing-heroku)


