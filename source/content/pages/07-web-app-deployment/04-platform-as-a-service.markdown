title: Platform-as-a-service
category: page
slug: platform-as-a-service
sortorder: 0704
toc: False
sidebartitle: Platform-as-a-Service
meta: A platform-as-a-service simplifies the deployment of application code while risking other tradeoffs. Learn more on Full Stack Python.


# Platform-as-a-service
A platform-as-a-service (PaaS) provides infrastructure and a software layer
on which a web application is deployed. Running your web application from
a PaaS removes the need to know as much about the underlying servers, 
operating system, web server, and often the WSGI server. 

*Note*: If you are not interested in deploying to a PaaS you can move 
ahead to the [WSGI servers](/wsgi-servers.html) section.

The PaaS layer defines how the application accesses resources such as 
computing time, files, and external services. The PaaS provides a 
higher-level abstraction for working with computing resources than deploying 
an application to a server or IaaS.

A PaaS makes deployment and operations easier because it forces the developer
to conform applications to the PaaS architecture. For example, Heroku looks 
for Python's `requirements.txt` file in the base directory of the repository 
during deployment because that is the file's de facto community standard
location.

<img src="/img/servers-versus-paas.png" width="100%" alt="Traditional LAMP server stack versus a Platform-as-a-Service stack" class="technical-diagram" />

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
[security section](/web-application-security.html) for further information.


## Platforms-as-a-service that support Python
* [Heroku](http://www.heroku.com/)

* [Google App Engine](https://developers.google.com/appengine/)

* [Gondor](https://gondor.io/)

* [PythonAnywhere](https://www.pythonanywhere.com/)

* [OpenShift](https://openshift.redhat.com/community/get-started/python)

* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)


## Platform-as-a-service resources
* [PaaS bakeoff: Comparing Stackato, OpenShift, Dotcloud and Heroku for Django hosting and deployment](http://appsembler.com/blog/paas-bakeoff-comparing-stackato-openshift-dotcloud-and-heroku-for-django-hosting-and-deployment/) by [Nate Aune](https://twitter.com/natea).

* [Deploying Django](http://www.rdegges.com/deploying-django/) by 
  Randall Degges is another great free resource about Heroku.

* [AWS in Plain English](https://www.expeditedssl.com/aws-in-plain-english)
  shows what current Amazon Web Services individual services are
  currently called and what they could've been called to be more 
  clear to users.

* [5 AWS mistakes you should avoid](https://cloudonaut.io/5-aws-mistakes-you-should-avoid/)
  explains how common beginner practices such as manually managing 
  infrastructure, not using scaling groups and underutilizing instances can 
  create problems you'd be better off avoiding altogether.

* Heroku's 
  [Python deployment documentation](https://devcenter.heroku.com/articles/getting-started-with-python)
  provides clear examples for how to work with virtualenv, pip and 
  `requirements.txt` to get a applications deployed to their platform.

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

* Are you wondering what it will cost to deploy a reasonable sized production 
  app on a platform-as-a-service like Heroku? Check out Cushion's 
  [transparent costs list](http://cushionapp.com/expenses/) where they
  include their expenses from using a PaaS as well as other services.

* The [beginner's guide to scaling to 11 million users on AWS](http://highscalability.com/blog/2016/1/11/a-beginners-guide-to-scaling-to-11-million-users-on-amazons.html)
  is a useful list of services you'll need to look at as you grow an
  application from 10 to 100 to 1000 to 500,000 and beyond to millions 
  of users.

* [How to Separate Your AWS Production and Development Accounts](http://blog.codeship.com/separate-aws-production-and-development-accounts/)
  is a basic post on keeping developer sandbox accounts separate from
  production AWS environments.

* [How much is Spotify Paying Google Cloud?](https://medium.com/@davidmytton/how-much-is-spotify-paying-google-cloud-ebb3bf180f15)
  provides some insight into how Spotify runs all of their infrastructure
  on Google Cloud and posits what they may be paying to run their
  service.


## Platform-as-a-service learning checklist
1. Review the potential Python platform-as-a-service options listed above.

1. Sign up for a PaaS account at the provider that appears to best fit your
   application needs. Heroku is the PaaS option recommended for starters due 
   to their detailed documentation and walkthroughs available on the web. 
   However, the other options are also viable since their purpose is to make 
   deploying applications as easy as possible.

1. Check if there are any PaaS-specific configuration files needed for your 
   app to run properly on the PaaS after it is deployed.

1. Deploy your app to the PaaS. 

1. Sync your application's configuration with the database.

1. Set up a content delivery network for your application's 
   [static content](/static-content.html) unless your PaaS provider already
   handles this deployment step for you.

1. Check if the application's functionality is working and tweak as necessary.

