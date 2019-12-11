title: Continuous Integration
category: page
slug: continuous-integration
sortorder: 0527
toc: False
sidebartitle: Continuous Integration
meta: Continuous integration (CI) automatically rebuilds, tests and deploys applications as developers commit code.


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

<img src="/img/visuals/continuous-integration.png" width="100%" class="shot" alt="One potential way for continuous integration to work with source control and a deployment environment." />

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
relatively simple setup.


## Open source CI projects
There are a variety of free and open source continuous integration servers 
that are configurable based on a project's needs. 

Note that many of these servers are not written in Python but work 
just fine for Python applications. Polyglot organizations (ones that 
use more than a single language and ecosystem) often use a single CI 
server for all of their  projects regardless of the programming language 
the application was written in.

* [Jenkins](/jenkins.html) is a common CI server for building and
  deploying to test and production servers. 
  [Jenkins source code is on GitHub](https://github.com/jenkinsci/jenkins).

* [Go CD](http://www.go.cd/) is a CI server by 
  [ThoughtWorks](http://www.thoughtworks.com/) that was designed with best 
  practices for the build and test & release cycles in mind. 
  [Go CD source code is on GitHub](https://github.com/gocd/gocd).

* [Bazel](https://bazel.build/) is a build tool that works with CI tools
  to organize large code bases and provide consistency with a well-defined,
  automated build process.

* [BuildBot](http://buildbot.net/) is a continuous integration **framework** 
  with a set of components for creating your own CI server. It's written in
  Python and intended for development teams that want more control over
  their build and deployment pipeline.
  [BuildBot source code is on GitHub](https://github.com/buildbot/buildbot).

* [TeamCity](https://www.jetbrains.com/teamcity/) is JetBrains' closed source
  CI server that requires a license to use.


## Jenkins CI resources
[Jenkins](/jenkins.html) is commonly used as a continuous integration 
server implementation for Python projects because it is open source and 
programming language agnostic. Learn more via the following resources or on 
[the dedicated Jenkins page](/jenkins.html).

* My book on [deploying Python web applications](http://www.deploypython.com/)
  walks through every step of setting up a Jenkins project with a WSGI 
  application to enable continuous delivery. Take a look if you're not 
  grokking all of the steps provided in these other blog posts.

* [Assembling a continuous integration service for a Django project on Jenkins](https://medium.com/@mondaini/assembling-a-continuous-integration-service-for-a-django-project-on-jenkins-5f979d4c4184)
  shows how to set up a Ubuntu instance with a Jenkins server that'll build a 
  [Django](/django.html) project.

* [Setting up Jenkins as a continuous integration server for Django](http://michal.karzynski.pl/blog/2014/04/19/continuous-integration-server-for-django-using-jenkins/)
  is another solid tutorial that also shows how to send email notifications 
  as part of the build process.


## General continuous integration resources
* [What is continuous integration?](http://martinfowler.com/articles/continuousIntegration.html)
  is a classic detailed article by Martin Fowler on the concepts behind CI
  and how to implement it.

* [Continuous Deployment For Practical People](http://www.airpair.com/continuous-deployment/posts/continuous-deployment-for-practical-people)
  is not specific to Python but a great read on what it entails.

* [Continuous Integration & Delivery - Illustrated](http://bitcubby.com/continuous-integration-delivery-illustrated/)
  uses well done drawings to show how continuous integration and delivery 
  works for testing and managing data.

* [The real difference between CI and CD](https://fire.ci/blog/the-difference-between-ci-and-cd/)
  explains what advantages CI provides, what constraints it operates under
  (such as total build time) to work well, and how that is different from
  the related but distinct concept of continuous delivery.

* [6 top continuous integration tools](https://opensource.com/business/15/7/six-continuous-integration-tools)
  gives a high level overview of six CI tools from a programming language
  agnostic perspective.

* [Updating the GOV.UK Continuous Integration environment](https://gdstechnology.blog.gov.uk/2017/02/10/updating-the-gov-uk-continuous-integration-environment/)
  explains the UK's Government Digital Service continuous integration
  configuration that relies on [Jenkins](/jenkins.html).

* [StackShare's Continuous Integration tag](http://stackshare.io/continuous-integration) 
  lists a slew of hosted CI services roughly ranked by user upvotes.

* [Good practices for continuous integration](http://buildoutcoredev.readthedocs.org/en/latest/continous-integration.html)
  includes advice on checking in code, commit tests and reverting to
  previous revisions.

* [Scoring Continuous Integration](https://paulhammant.com/2017/05/01/scoring-continuous-integration/)
  gives an interesting perspective on ways to rank the effectiveness
  of how teams use their CI tooling.

* [Why Continuous Integration Is Important](https://blog.codeship.com/continuous-integration-important/)
  is a high-level overview of how CI can build trust both among developers
  and between developers and non-technical people in an organization. The
  post also discusses tasks related to setting up reliable CI such as test 
  environments, [integration testing](/integration-testing.html) and 
  visibility into the CI results.

* [Continuous Intrusion: Why CI tools are a hacker's best friend](https://www.blackhat.com/docs/eu-15/materials/eu-15-Mittal-Continuous-Intrusion-Why-CI-Tools-Are-An-Attackers-Best-Friend.pdf) (PDF)
  strongly advises securing your continuous integration server just as you
  would every other part of your production application, unless you want
  your environment to be vulnerable to malicious actors.

* [Measuring and Improving your CI/CD Pipelines](https://blog.petegoo.com/2018/11/09/optimizing-ci-cd-pipelines/)
  provides metrics for what you should measure with your CI/CD setup to 
  improve the process for helping your development teams ship code.

* [Six rules for setting up continuous integration systems](https://rhonabwy.com/2016/01/31/six-rules-for-setting-up-continuous-integration-systems/)
  has some solid general advice for culling problematic tests, ensuring
  the integration speed supports the development culture you are building
  and keeping all code in source control instead of having complicated
  logic configured within the CI server.

* [How to Identify Major Blockers in a CI/CD Pipeline](https://blog.codeship.com/how-to-identify-major-blockers-in-a-cicd-pipeline/)
  gives a high level overview of concepts such as shipping velocity, test
  execution and environment provisioning with regards to CI configurations.
