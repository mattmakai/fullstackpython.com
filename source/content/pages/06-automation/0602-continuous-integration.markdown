title: Continuous Integration
category: page
slug: continuous-integration
sort-order: 0602
choice1url: /logging.html
choice1icon: fa-align-left fa-inverse
choice1text: How do I log events that happen in my app while it is running?
choice2url: /web-application-security.html
choice2icon: fa-lock fa-inverse
choice2text: What should I do to secure my web application?
choice3url: /api-integration.html
choice3icon: fa-link fa-inverse
choice3text: How do I integrate external APIs into my application?
choice4url:
choice4icon:
choice4text:

# Continuous Integration
Continuous integration (CI) automates building, testing and deploying 
applications.

## Why is continuous integration important?
When CI is set up well it can dramatically reduce deployment times by 
eliminating manual steps and ensure code does not have bugs that are being
checked by automated tests. Source code changes as a project evolves.
CI combined with unit and integration tests check that code modifications 
do not break existing tests ensure the software works as intended.


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


## Continuous integration resources
* [What is continuous integration](http://martinfowler.com/articles/continuousIntegration.html)
  is a classic detailed article by Martin Fowler on the concepts behind CI
  and how to implement it.

* "[Diving into continuous integration as a newbie](http://www.rackspace.com/blog/diving-into-continuous-integration-as-a-newbie/)"
  is a retrospective on learning CI from a Rackspace intern on how she learned
  the subject.


### What do you want to add to your application next?
