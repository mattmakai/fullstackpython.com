title: Continuous Integration
category: page
slug: continuous-integration
sort-order: 0713
meta: Continuous integration automatically rebuilds and deploys applications as developers commit code. Learn more on Full Stack Python.


# Continuous Integration
Continuous integration (CI) automates building, testing and deploying 
applications.

## Why is continuous integration important?
When CI is set up well it can dramatically reduce deployment times by 
eliminating manual steps and ensure code does not have bugs that are being
checked by automated tests. Source code changes as a project evolves.
CI combined with unit and integration tests check that code modifications 
do not break existing tests ensure the software works as intended.

## Continuous integration example
The following picture represents a high level perspective on how continuous
integration and deployment can work. 

<img src="theme/img/continuous-integration.png" width="100%" class="technical-diagram" alt="One potential way for continuous integration to work." />

In the above diagram, when new code is commited to a source repository 
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
  Python and intended for development teams that want more controller over
  their build and deployment pipeline.
  [BuildBot source code is on GitHub](https://github.com/buildbot/buildbot).

* [TeamCity](https://www.jetbrains.com/teamcity/) is JetBrains' closed source
  CI server that requires a license to use.


## Hosted CI services
* [Travis CI](https://travis-ci.org/) provides free CI for open source 
  projects and has a [commercial version](https://travis-ci.com/) for 
  private repositories.

* [Bamboo](https://www.atlassian.com/software/bamboo) is 
  [Atlassian](https://www.atlassian.com/)'s hosted continuous integration that
  is also free for open source projects.

* [Circle CI](https://circleci.com/) works with open or closed source projects
  on GitHub and can deploy them to Heroku if builds are successful.

* [Shippable](https://www.shippable.com/) uses Docker containers to speed 
  the build and integration process. It's free for public repositories.

* [Drone](https://drone.io/) is another CI service that also provides free
  builds for open source projects.

* [Codeship](https://www.codeship.io/) provides continuous integration for
  Python 2.7.

* [Snap](https://snap-ci.com/) is a CI server and build pipeline tool for
  both integrating and deploying code.


## Continuous integration resources
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

* [Running Jenkins in Docker Containers](http://www.catosplace.net/blog/2015/02/11/running-jenkins-in-docker-containers/)
  is a short tutorial showing how to use the official 
  [Jenkins container](https://registry.hub.docker.com/_/jenkins/) on the
  Docker hub.

* [Good practices for continuous integration](http://buildoutcoredev.readthedocs.org/en/latest/continous-integration.html)
  includes advice on checking in code, commit tests and reverting to
  previous revisions.

* [Deploying to AWS using Ansible, Docker and Teamcity](http://blog.bwhaley.com/deploying-to-aws-using-ansible-docker-and-teamcity)
  is an example walking through one potential way to use the Teamcity CI
  server for automated deployments.


### What do you want to add to your application next?
