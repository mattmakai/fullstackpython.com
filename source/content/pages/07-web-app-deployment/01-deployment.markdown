title: Deployment
category: page
slug: deployment
sortorder: 0701
toc: True
sidebartitle: 7. Deployment
meta: Web application deployment involves packaging and running your app on a server. Learn more about deployments on Full Stack Python.


# Deployment
Deployment involves packaging up your web application and putting it in a 
production environment that can run the app.


## Why is deployment necessary?
Your web application must live somewhere other than your own desktop or 
laptop. A production environment is the canonical version of your current 
application and its associated data.


## Deployment topics map
Python web application deployments are comprised of many pieces that need to
be individually configured. Here is a map that visually depicts how each
deployment topic relates to each other. Click the image to pull up a PDF 
version.

<a href="/full-stack-python-map.pdf" target="_blank" style="border: none;"><img src="/img/full-stack-python-map.png" width="100%" alt="Full Stack Python site map." class="technical-diagram" /></a>


## Deployment hosting options
There are four options for deploying and hosting a web application:

1. ["Bare metal" servers](/servers.html)

2. [Virtualized servers](/servers.html)

3. [Infrastructure-as-a-service](/servers.html)

4. [Platform-as-a-service](/platform-as-a-service.html)

The first three options are similar. The deployer needs to provision one or
more servers with a Linux distribution. System packages, a web server, 
WSGI server, database and the Python environment are then installed. Finally
the application can be pulled from source and installed in the environment.

Note that there are other ways of installing a Python web application through
system-specific package management systems. We won't cover those in this
guide as they are considered advanced deployment techniques.


## Deployment resources
* If you need a step-by-step guide to deploying a Python web application,
  I wrote [a whole book](http://www.deploypython.com/) on exactly this topic 
  called 
  [The Full Stack Python Guide to Deployments](https://gumroad.com/l/WOvyt)
  that you'll find super helpful.

* [Deploying Python web applications](http://talkpython.fm/episodes/show/26/deploying-python-web-applications-updated)
  is an episode of the great Talk Python to Me podcast series where I
  discuss deploying web applications based on a fairly traditional virtual 
  private server, Nginx and Green Unicorn stack.

* [Thoughts on web application deployment](http://omniti.com/seeds/thoughts-on-web-application-deployment)
  walks through stages of deployment with source control, planning, 
  continuous deployment and monitoring the results.

* [Deploying Software](https://zachholman.com/posts/deploying-software)
  is a long must-read for understanding how to deploy software properly.

* [Practical continuous deployment](http://blogs.atlassian.com/2014/04/practical-continuous-deployment/)
  defines delivery versus deployment and walks through a continuous deployment
  workflow.

* In [this free video by Neal Ford](http://player.oreilly.com/videos/9781491908181?toc_id=210188),
  he talks about engineering practices for continuous delivery. He explains
  the difference between 
  [continuous integration](/continuous-integration.html),
  continuous deployment and continuous delivery. Highly recommended for an
  overview of deployment concepts and as an introduction to the other videos
  on those subjects in that series.

* [Continuous deployment at Instagram](http://engineering.instagram.com/posts/1125308487520335/continuous-deployment-at-instagram/)
  is the story of how their deployment process evolved over time from a 
  large Fabric script to continous deployments. Along the way they 
  encountered issues with code reviews, test failures, canary builds and
  rollbacks. It's a great read that sheds some light on how Python 
  deployments can be done well at large scale.

* Stack Overflow's guide on 
  [how they do deployment](http://nickcraver.com/blog/2016/05/03/stack-overflow-how-we-do-deployment-2016-edition/)
  is an awesome in-depth read covering topics ranging from git branching
  to database migrations.

* If you're using Flask this 
  [detailed post on deploying it to Ubuntu](https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/)
  is a great way to familiarize yourself with the deployment process.


## Deployment learning checklist
1. If you're tight on time look at the 
   [platform-as-a-service (PaaS)](/platform-as-a-service.html) options. You 
   can deploy a low traffic project web app for free or low cost. You won't 
   have to worry about setting up the operating system and web server 
   compared to going the traditional server route. In theory you should be 
   able to get your application live on the web sooner with PaaS hosting.

1. [Traditional server options](/servers.html) are your best bet for learning
   how the entire Python web stack works. You'll often save money with a 
   virtual private server instead of a platform-as-a-service as you scale up.

1. Read about servers, [operating systems](/operating-systems.html), 
   [web servers](/web-servers.html) and [WSGI servers](/wsgi-servers.html) 
   to get a broad picture of what components need to be set up to run a 
   Python web application.

