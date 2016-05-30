title: Continuous Integration
category: page
slug: continuous-integration
sortorder: 0713
toc: False
sidebartitle: Continuous Integration
meta: Continuous integration (CI) automatically rebuilds, tests and deploys applications as developers commit code.


# Continuous Integration
Continuous integration automates the building, testing and deploying of 
applications. Software projects, whether created by a single individual or 
entire teams, typically use continuous integration as a hub to ensure 
important steps such as unit testing are automated rather than manual 
processes.


## Why is continuous integration important?
When continuous integration (CI) is established as a step in a software 
project's development process it can dramatically reduce deployment times 
by minimizing steps that require human intervention. The only minor downside 
to using CI is that it takes some initial time by a developer to set up and 
then there is some ongoing maintainence if a project is broken into multiple 
parts, such as going from a monolith architecture to 
[microservices](/microservices.html).


## Automated testing
Another major advantage with CI is that testing can be an automated step in 
the deployment process. Broken deployments can be prevented by running a 
comprehensive test suite of [unit](/unit-testing.html) and 
[integration tests](/integration-testing.html) when developers check in code 
to a source code repository. Any bugs accidentally introduced during a 
check-in that are caught by the test suite are reported and prevent the 
deployment from proceeding.

The automated testing on checked in source code can be thought of like the 
bumper guards in bowling that prevent code quality from going too far off 
track. CI combined with unit and integration tests check that any code 
modifications do not break existing tests to ensure the software works as 
intended.


## Continuous integration example
The following picture represents a high level perspective on how continuous
integration and deployment can work. 

<img src="/img/continuous-integration.png" width="100%" class="technical-diagram" alt="One potential way for continuous integration to work with source control and a deployment environment." />

In the above diagram, when new code is committed to a source repository 
there is a hook that notifies the continuous integration server that new 
code needs to be built (the continuous integration server could also
poll the source code repository if a notification is not possible).

The continuous integration server pulls the code to build and test it. If
all tests pass, the continuous integration server begins the deployment
process. The new code is pulled down to the server where the deployment is
taking place. Finally the deployment process is completed via restarting 
services and related deployment activities.

There are many other ways a continuous integration server and its 
deployments can be structured. The above was just one example of a 
relatively simple set up.


## Open source CI projects
There are a variety of free and open source continuous integration servers 
that are configurable based on a project's needs. 

Note that many of these servers are not written in Python but work 
just fine for Python applications. Polyglot organizations (ones that 
use more than a single language and ecosystem) often use a single CI 
server for all of their  projects regardless of the programming language 
the application was written in.

* [Jenkins](http://jenkins-ci.org/) is a common CI server for building and
  deploying to test and production servers. 
  [Jenkins source code is on GitHub](https://github.com/jenkinsci/jenkins).

* [Go CD](http://www.go.cd/) is a CI server by 
  [ThoughtWorks](http://www.thoughtworks.com/) that was designed with best 
  practices for the build and test & release cycles in mind. 
  [Go CD source code is on GitHub](https://github.com/gocd/gocd).

* [Strider](http://stridercd.com/) is a CI server written in node.js. 
  [Strider source code is on GitHub](https://github.com/Strider-CD/strider).

* [BuildBot](http://buildbot.net/) is a continuous integration **framework** 
  with a set of components for creating your own CI server. It's written in
  Python and intended for development teams that want more control over
  their build and deployment pipeline.
  [BuildBot source code is on GitHub](https://github.com/buildbot/buildbot).

* [TeamCity](https://www.jetbrains.com/teamcity/) is JetBrains' closed source
  CI server that requires a license to use.


## Jenkins CI resources
* [Assembling a continuous integration service for a Django project on Jenkins](https://medium.com/@mondaini/assembling-a-continuous-integration-service-for-a-django-project-on-jenkins-5f979d4c4184)
  shows how to set up a Ubuntu instance with a Jenkins server that'll build a 
  [Django](/django.html) project.

* My book on [deploying Python web applications](http://www.deploypython.com/)
  walks through every step of setting up a Jenkins project with a WSGI 
  application to enable continuous delivery. Take a look if you're not 
  grokking all of the steps provided in these other blog posts.

* [Setting up Jenkins as a continuous integration server for Django](http://michal.karzynski.pl/blog/2014/04/19/continuous-integration-server-for-django-using-jenkins/)
  is another solid tutorial that also shows how to send email notifications 
  as part of the build process.

* If you're running into difficulty adding an SSH key to your Jenkins system 
  account so you can connect to another server or Git repository
  [this blog post on connecting Jenkins with Git](http://dcycleproject.org/blog/51/connecting-jenkins-and-git)
  to get the steps to solve that problem.

* [Automated Servers and Deployments with Ansible & Jenkins](http://chromaticsites.com/blog/automated-servers-and-deployments-ansible-jenkins)
  
* [Running Jenkins in Docker Containers](http://www.catosplace.net/blog/2015/02/11/running-jenkins-in-docker-containers/)
  is a short tutorial showing how to use the official 
  [Jenkins container](https://registry.hub.docker.com/_/jenkins/) on the
  Docker hub.

* [Securing Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Securing+Jenkins)
  is the landing page for Jenkins security. If you're deploying your own
  instance, you'll need to lock it down against unauthorized users.

* [Can we use Jenkins for that?](http://engineering.simondata.com/can-we-use-jenkins-for-that)
  looks at how one team uses Jenkins for more than typical continuous 
  integration situations - they also use it as an administrative interface, 
  cron jobs, data analytics pipelines and long-running scripts.


## General continuous integration resources
* [What is continuous integration?](http://martinfowler.com/articles/continuousIntegration.html)
  is a classic detailed article by Martin Fowler on the concepts behind CI
  and how to implement it.

* [Continuous Deployment For Practical People](http://www.airpair.com/continuous-deployment/posts/continuous-deployment-for-practical-people)
  is not specific to Python but a great read on what it entails.

* [Continuous Integration & Delivery - Illustrated](http://bitcubby.com/continuous-integration-delivery-illustrated/)
  uses well done drawings to show how continuous integration and delivery 
  works for testing and managing data.

* [Diving into continuous integration as a newbie](http://www.rackspace.com/blog/diving-into-continuous-integration-as-a-newbie/)
  is a retrospective on learning CI from a Rackspace intern on how she learned
  the subject.

* [StackShare's Continuous Integration tag](http://stackshare.io/continuous-integration) 
  lists a slew of hosted CI services roughly ranked by user upvotes.

* [Good practices for continuous integration](http://buildoutcoredev.readthedocs.org/en/latest/continous-integration.html)
  includes advice on checking in code, commit tests and reverting to
  previous revisions.

* [Deploying to AWS using Ansible, Docker and Teamcity](http://blog.bwhaley.com/deploying-to-aws-using-ansible-docker-and-teamcity)
  is an example walking through one potential way to use the Teamcity CI
  server for automated deployments.

* [Why Continuous Integration Is Important](https://blog.codeship.com/continuous-integration-important/)
  is a high-level overview of how CI can build trust both among developers
  and between developers and non-technical people in an organization. The
  post also discusses tasks related to setting up reliable CI such as test 
  environments, [integration testing](/integration-testing.html) and 
  visibility into the CI results.

