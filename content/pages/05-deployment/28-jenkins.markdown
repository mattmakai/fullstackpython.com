title: Jenkins
category: page
slug: jenkins
sortorder: 0528
toc: False
sidebartitle: Jenkins
meta: Jenkins is a continuous integration (CI) server often used to automatically build and test Python applications.


# Jenkins
[Jenkins](https://jenkins.io/) is a 
[continuous integration](/continuous-integration.html) (CI) server often 
used to automate building, [testing](/testing.html) and 
[deploying](/deployment.html) Python applications.

<a href="https://jenkins.io/" style="border: none;"><img src="/img/logos/jenkins.png" width="100%" alt="Official Jenkins CI logo. Licensed under Creative Commons Attribution-ShareAlike 3.0 Unported License." class="technical-diagram"></a>

<div class="well see-also">Jenkins is an implementation of the <a href="/continuous-integration.html">continuous integration</a> concept. Learn more in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


### Jenkins resources
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
  covers the benefits of using the 
  [configuration management tool](/configuration-management.html) Ansible in
  combination with Jenkins.
  
* [Running Jenkins in Docker Containers](http://www.catosplace.net/blog/2015/02/11/running-jenkins-in-docker-containers/)
  is a short tutorial showing how to use the official 
  [Jenkins container](https://registry.hub.docker.com/_/jenkins/) on the
  Docker hub.

* [Securing Jenkins](https://wiki.jenkins.io/display/JENKINS/Securing+Jenkins)
  is the landing page for Jenkins security. If you're deploying your own
  instance, you'll need to lock it down against unauthorized users.

* [Can we use Jenkins for that?](http://engineering.simondata.com/can-we-use-jenkins-for-that)
  looks at how one team uses Jenkins for more than typical continuous 
  integration situations - they also use it as an administrative interface, 
  cron jobs, data analytics pipelines and long-running scripts.

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
