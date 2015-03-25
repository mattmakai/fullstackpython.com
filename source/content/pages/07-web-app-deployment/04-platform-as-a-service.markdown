title: Platform-as-a-service
category: page
slug: platform-as-a-service
sort-order: 0704
meta: A platform-as-a-service simplifies the deployment of application code while risking other tradeoffs. Learn more on Full Stack Python.
choice1url: /wsgi-servers.html
choice1icon: fa-play fa-inverse
choice1text: What WSGI server should I use to run Python code?
choice2url: /databases.html
choice2icon: fa-hdd-o
choice2text: How do I set up a database for use with my app?
choice3url: /application-dependencies.html
choice3icon: fa-archive fa-inverse
choice3text: How can I install the libraries my app depends upon?


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
to conform applications to the PaaS architecture. For example, Heroku looks 
for Python's requirements.txt file in the base directory of the repository 
during deployment because that is the file's de facto community standard
location.

<img src="theme/img/servers-versus-paas.png" width="100%" alt="Traditional LAMP server stack versus a Platform-as-a-Service stack" class="technical-diagram" />

If you go the PaaS route, you can skip configuring an operating system
and web server prebaked into PaaS offerings. PaaS offerings generally start 
at the WSGI server layer. 


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


## Platforms-as-a-service that support Python
* [Heroku](http://www.heroku.com/)

* [Google App Engine](https://developers.google.com/appengine/)

* [Gondor](https://gondor.io/)

* [PythonAnywhere](https://www.pythonanywhere.com/)

* [OpenShift](https://openshift.redhat.com/community/get-started/python>)

* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)


## Platform-as-a-service resources
* [PaaS bakeoff: Comparing Stackato, OpenShift, Dotcloud and Heroku for Django hosting and deployment](http://appsembler.com/blog/paas-bakeoff-comparing-stackato-openshift-dotcloud-and-heroku-for-django-hosting-and-deployment/) by [Nate Aune](https://twitter.com/natea).

* [Deploying Django](http://www.rdegges.com/deploying-django/) by 
  Randall Degges is another great free resource about Heroku.

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

* [Deploying a Django App to AWS Elastic Beanstalk](https://realpython.com/blog/python/deploying-a-django-app-to-aws-elastic-beanstalk/)
  is a fantastic post that shows how to deploy to Amazon Web Service's own
  PaaS.

* [Deploy your hack in 3 steps: Intro to AWS and Elastic Beanstalk](https://news.mlh.io/deploy-your-hack-in-3-steps-intro-to-aws-and-elastic-beanstalk-02-20-2015)
  shows how to deploy a simple Ruby Sinatra app, but the steps are generally
  applicable to Python web apps as well. 


## Platform-as-a-service learning checklist
<i class="fa fa-check-square-o"></i>
Review the potential Python platform-as-a-service options above and on their
websites.

<i class="fa fa-check-square-o"></i>
Sign up for a PaaS account at the provider that appears to best fit your
application needs. Heroku is the PaaS option recommended for starters due to
their detailed documentation and walkthroughs available on the web. However,
the other options are perfectly viable since their purpose is to make deploying
applications as easy as possible.

<i class="fa fa-check-square-o"></i>
Check if there are any PaaS-specific configuration files needed for your app
to run properly on the PaaS after it is deployed.

<i class="fa fa-check-square-o"></i>
Deploy your app to the PaaS. 

<i class="fa fa-check-square-o"></i>
Sync your application's configuration with the database.

<i class="fa fa-check-square-o"></i>
Set up a content delivery network for your application's 
[static content](/static-content.html) unless your PaaS provider already
handles this deployment step for you.

<i class="fa fa-check-square-o"></i>
Check if the application's functionality is working and tweak as necessary.


### Do you want to use a PaaS or deploy to a traditional server?
