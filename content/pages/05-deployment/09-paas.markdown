title: Platform-as-a-service
category: page
slug: platform-as-a-service
sortorder: 0509
toc: False
sidebartitle: Platform-as-a-Service
meta: A platform-as-a-service simplifies the deployment of application code while risking other tradeoffs. Learn more on Full Stack Python.


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

<img src="/img/visuals/servers-versus-paas.png" width="100%" alt="Traditional LAMP server stack versus a Platform-as-a-Service stack" class="technical-diagram" />

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

* [PythonAnywhere](https://www.pythonanywhere.com/)

* [OpenShift](https://openshift.redhat.com/community/get-started/python)

* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) and
  [AWS CodeStar](https://aws.amazon.com/codestar/) are Amazon Web Services'
  PaaS offerings. CodeStar is the newer service and recommended for new
  projects.


## Platform-as-a-service open source projects
The following open source projects allow you to host your own version
of a platform-as-a-service. Running one of these gives you the advantage
of controlling and modifying the project for your own applications,
but prevents you from offloading the responsibility of keeping servers
running to someone else.

* [Kel](http://www.kelproject.com/) uses Kubernetes as a foundation
  for a custom self-hosted PaaS. Note that it was created by Eldarion,
  which had one of the first Python-specific PaaS offerings on the
  market around the time that Heroku was launched.

* [Dokku](http://dokku.viewdocs.io/dokku/) builds on Docker and has
  hooks for plugins to extend the small core of the project and customize 
  deployments for your applications.

* [Convox Rack](https://github.com/convox/rack) is open source PaaS
  designed to run on top of AWS services.



## Platform-as-a-service resources
* [The differences between IaaS, PaaS and SaaS](https://www.engineyard.com/blog/the-differences-between-iaas-paas-and-saas-and-when-to-use-each)
  explains the abstract layer differences among "X-as-a-service" offering
  types and when to consider using each one.

* [PaaS bakeoff: Comparing Stackato, OpenShift, Dotcloud and Heroku for Django hosting and deployment](http://appsembler.com/blog/paas-bakeoff-comparing-stackato-openshift-dotcloud-and-heroku-for-django-hosting-and-deployment/) 
  by [Nate Aune](https://twitter.com/natea).

* [Deploying Django](http://www.rdegges.com/deploying-django/) by 
  Randall Degges is another great free resource about Heroku.

* [AWS in Plain English](https://www.expeditedssl.com/aws-in-plain-english)
  shows what current Amazon Web Services individual services are
  currently called and what they could've been called to be more 
  clear to users.

* [PAAS comparison - Dokku vs Flynn vs Deis vs Kubernetes vs Docker Swarm in 2017](http://www.jancarloviray.com/blog/paas-comparison-2017-dokku-flynn-deis-kubernetes-docker-swarm/)
  covers high-level advantages and disadvantages of several self-hosted PaaS 
  projects.

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

* [Deploying a Django app on Amazon EC2 instance](http://agiliq.com/blog/2014/08/deploying-a-django-app-on-amazon-ec2-instance/)
  is a detailed walkthrough for deploying an example Django app to Amazon
  Web Services.

* [How much is Spotify Paying Google Cloud?](https://medium.com/@davidmytton/how-much-is-spotify-paying-google-cloud-ebb3bf180f15)
  provides some insight into how Spotify runs all of their infrastructure
  on Google Cloud and posits what they may be paying to run their
  service.

* Two blog posts on using AWS Autoscaling in [Automatic replacement of Autoscaling nodes with equivalent spot instances](https://mcristi.wordpress.com/2016/04/21/my-approach-at-making-aws-ec2-affordable-automatic-replacement-of-autoscaling-nodes-with-equivalent-spot-instances/)
  and
  [Autoscaling nodes: seeing it in action](https://mcristi.wordpress.com/2016/04/27/automatic-replacement-of-autoscaling-nodes-with-equivalent-spot-instances-seeing-it-in-action/)
  provide a potential approach for making AWS cheaper via autoscaling. While
  these posts may look a bit more dfifficult than the Heroku dyno slider
  bar, if you're already using AWS this should prove fairly easy to configure.


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

