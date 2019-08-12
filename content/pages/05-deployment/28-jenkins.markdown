title: Jenkins
category: page
slug: jenkins
sortorder: 0528
toc: False
sidebartitle: Jenkins
meta: Jenkins is a continuous integration (CI) server often used to automatically build and test Python applications.


[Jenkins](https://jenkins.io/) is a 
[continuous integration](/continuous-integration.html) (CI) server often 
used to automate building, [testing](/testing.html) and 
[deploying](/deployment.html) Python applications.

<a href="https://jenkins.io/" style="border: none;"><img src="/img/logos/jenkins.png" width="100%" alt="Official Jenkins CI logo. Licensed under Creative Commons Attribution-ShareAlike 3.0 Unported License." class="shot"></a>

<div class="well see-also">Jenkins is an implementation of the <a href="/continuous-integration.html">continuous integration</a> concept. Learn more in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


### Jenkins resources
* [Assembling a continuous integration service for a Django project on Jenkins](https://medium.com/@mondaini/assembling-a-continuous-integration-service-for-a-django-project-on-jenkins-5f979d4c4184)
  shows how to set up a Ubuntu instance with a Jenkins server that'll build a 
  [Django](/django.html) project.

* My book on [deploying Python web applications](http://www.deploypython.com/)
  walks through every step of setting up a Jenkins project with a WSGI 
  application to enable continuous delivery. Take a look if you're not 
  grokking all of the steps provided in these other blog posts.

* [Revisiting Docker and Jenkins](https://engineering.riotgames.com/news/revisiting-docker-and-jenkins)
  is a fantastic series of posts that explains how Riot Games combines 
  Jenkins and Docker to test their back end services.

* [Setting up Jenkins as a continuous integration server for Django](http://michal.karzynski.pl/blog/2014/04/19/continuous-integration-server-for-django-using-jenkins/)
  is another solid tutorial that also shows how to send email notifications 
  as part of the build process.

* If you're running into difficulty adding an SSH key to your Jenkins system 
  account so you can connect to another server or Git repository
  [this blog post on connecting Jenkins with Git](http://dcycleproject.org/blog/51/connecting-jenkins-and-git)
  to get the steps to solve that problem.

* [Running Jenkins in Docker Containers](http://www.catosplace.net/blog/2015/02/11/running-jenkins-in-docker-containers/)
  is a short tutorial showing how to use the official 
  [Jenkins container](https://registry.hub.docker.com/_/jenkins/) on the
  Docker hub.

* [Securing Jenkins](https://wiki.jenkins.io/display/JENKINS/Securing+Jenkins)
  is the landing page for Jenkins security. If you're deploying your own
  instance, you'll need to lock it down against unauthorized users.

* [Updating the GOV.UK Continuous Integration environment](https://gdstechnology.blog.gov.uk/2017/02/10/updating-the-gov-uk-continuous-integration-environment/)
  describes the configuration improvements one infrastructure team made
  to Jenkins, where they enabled 
  [jenkinsfiles](https://jenkins.io/doc/book/pipeline/jenkinsfile/)
  to store CI data within project repositories instead of having to 
  handle the setup through the Jenkins user interface. The team also
  published 
  [their Puppet files for building](https://github.com/alphagov/govuk-puppet/tree/master/modules/govuk_jenkins/manifests)
  Jenkins infrastructure.

* [Jenkins configuration as code](https://www.praqma.com/stories/jenkins-configuration-as-code/)
  details the launch of a new Jenkins tool for programmatically configuring
  Jenkins so you can automate the setup of this part of your deployment
  infrastructure. The post goes into the motivations behind creating another
  tool for code configuration when other similar libraries already exist.

* [Automated servers and deployments with Ansible & Jenkins](https://chromatichq.com/blog/automated-servers-and-deployments-ansible-jenkins)
  covers using [Ansible](/ansible.html) for automating 
  [deployments](/deployment.html) and handling the coordination via
  Jenkins builds.

* [Building GitHub Pull Requests using Jenkins Pipelines](https://www.theguild.nl/building-github-pull-requests-using-jenkins-pipelines/)
  explains how to use Jenkins 2.0 with Pipelines to create builds that
  run in Docker containers off of new GitHub pull requests.

* [Automated API testing with Jenkins](https://assertible.com/blog/automated-api-testing-with-jenkins)
  walks through how to use Jenkins to tests your 
  [API](/application-programming-interfaces.html) upon each deployment.

* [Continuous Delivery with Jenkins and Rollbar](https://rollbar.com/blog/continuous-delivery-with-jenkins/)
  is a tutorial on using Jenkins for continuous integration paired with
  [Rollbar](/rollbar.html) for tracking deployments and errors.
