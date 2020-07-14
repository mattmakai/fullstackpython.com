title: Deployment
category: page
slug: deployment
sortorder: 0500
toc: True
sidebartitle: 5. Deployment
meta: Web application deployment involves packaging and running your app on a server. Learn more about deployments on Full Stack Python.


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

<a href="/full-stack-python-map.pdf" style="border:none"><img src="/img/visuals/full-stack-python-map.png" width="100%" alt="Full Stack Python deployments map." class="shot"></a>


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


## Deployment tools
* [teletraan](https://github.com/pinterest/teletraan) is the deploy system
  used by the development teams at Pinterest, a huge Python shop!

* [pants](https://www.pantsbuild.org/docs) is a build system originally
  created at Twitter and now split out as its own sustainable open source
  project.

* [Screwdriver](http://screwdriver.cd/) is an open source build system
  originally developed at Yahoo! that is now open source. Learn more about
  it in the 
  [introduction post](https://yahooeng.tumblr.com/post/155765242061/open-sourcing-screwdriver-yahoos-continuous)
  that contains the rationale for its creation.


### Deployment resources
* [Hello, production](https://blog.thepete.net/blog/2019/10/04/hello-production/)
  lays out the powerful philosophy of putting a project into production as
  soon as possible in a project's lifecycle to establish the pipeline,
  identify issues and bottlenecks, and build the foundation for continuous 
  delivery. The post also covers common objections and provides some 
  arguments to help you convince others that this strategy is the right
  way to go on all projects.

* [Automated Continuous Deployment at Heroku](https://blog.heroku.com/automated-continuous-deployment-at-heroku)
  explains [Heroku](/heroku.html)'s deployment system, the checks they 
  use to ensure code quality and what they have learned from building
  the pipeline and process.

* [Deploying Python web applications](http://talkpython.fm/episodes/show/26/deploying-python-web-applications-updated)
  is an episode of the great Talk Python to Me podcast series where I
  discuss deploying web applications based on a fairly traditional virtual 
  private server, Nginx and Green Unicorn stack.

* [Thoughts on web application deployment](http://omniti.com/seeds/thoughts-on-web-application-deployment)
  walks through stages of deployment with source control, planning, 
  continuous deployment and monitoring the results.

* [Deploying Software](https://zachholman.com/posts/deploying-software)
  is a long must-read for understanding how to deploy software properly.

* [The evolution of code deploys at Reddit](https://redditblog.com/2017/06/02/the-evolution-of-code-deploys-at-reddit/)
  teaches the history, including the mistakes, that Reddit's development
  teams learned as they scaled up the development team and the traffic
  on one of the most-visited websites in the world.

* [Deployment strategies defined](http://blog.itaysk.com/2017/11/20/deployment-strategies-defined)
  explains various ways that development teams deploy applications, 
  ranging from reckless to versioned.

* [How we release so frequently](https://engineering.skybettingandgaming.com/2016/02/02/how-we-release-so-frequently/)
  provides a high-level overview of tactics for how teams at large scale 
  can deploy changes several times per day or more with confidence the 
  systems will not completely fail. There will be bugs, but that does not
  mean the entire operation will stop.

* [Hands-off deployment with Canary](https://developers.soundcloud.com/blog/hands-off-deployment-with-canary)
  explains how SoundCloud automates their deployment process and uses
  canary builds to identify and roll back issues to mitigate reliability
  issues that can occur with shipping software at scale.

* [Practical continuous deployment](http://blogs.atlassian.com/2014/04/practical-continuous-deployment/)
  defines delivery versus deployment and walks through a continuous deployment
  workflow.

* [5 ways to deploy your Python application in 2017](https://www.youtube.com/watch?v=vGphzPLemZE)
  is a talk from 
  [PyCon US 2017](https://www.youtube.com/channel/UCrJhliKNQ8g0qoE_zvL8eVg/videos)
  where Andrew Baker deploys the getting started [Flask](/flask.html) 
  app using Ngrok, Heroku, Zappa on the [serverless](/serverless.html)
  [AWS Lambda](/aws-lambda.html) platform, a virtual machine on Google Cloud
  and [Docker](/docker.html).
  
* [Continuous deployment at Instagram](https://engineering.instagram.com/continuous-deployment-at-instagram-1e18548f01d1)
  is the story of how their deployment process evolved over time from a 
  large Fabric script to continuous deployments. Along the way they 
  encountered issues with code reviews, test failures, canary builds and
  rollbacks. It's a great read that sheds some light on how Python 
  deployments can be done well at large scale.

* Stack Overflow's guide on 
  [how they do deployment](http://nickcraver.com/blog/2016/05/03/stack-overflow-how-we-do-deployment-2016-edition/)
  is an awesome in-depth read covering topics ranging from git branching
  to database migrations.

* In [this free video by Neal Ford](https://www.youtube.com/watch?v=RyTqRi4rJbw),
  he talks about engineering practices for continuous delivery. He explains
  the difference between 
  [continuous integration](/continuous-integration.html),
  continuous deployment and continuous delivery. Highly recommended for an
  overview of deployment concepts and as an introduction to the other videos
  on those subjects in that series.

* [TestDriven.io](https://testdriven.io/) shows how to deploy a
  [microservices](/microservices.html) architecture that uses 
  [Docker](/docker.html), [Flask](/flask.html), and React with 
  container orchestration on Amazon ECS. 


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

