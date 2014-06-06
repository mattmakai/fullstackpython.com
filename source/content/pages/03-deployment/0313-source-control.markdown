title: Source Control
category: page
slug: source-control
sort-order: 037
choice1url: /deployment.html
choice1icon: fa-share
choice1text: How do I deploy the code I've created for my web app?
choice2url: /web-analytics.html
choice2icon: fa-dashboard
choice2text: I want to learn more about the users of my application.
choice3url: /api-integration.html
choice3icon: fa-link
choice3text: How do I integrate external APIs into my web application?
choice4url:
choice4icon:
choice4text:


# Source control
Source control systems, also known as version control systems, store code
and other static files, such as images, with a history of the changes made to
those files.

## Why is source control necessary?
Version control systems allow developers to modify code without worrying 
about permanently screwing something up. Unwanted changes can be easily rolled
back. Developers can merge changes with other developer's code through 
[diff](http://en.wikipedia.org/wiki/Diff) views. 

These benefits exist on all software projects. Therefore version control is 
a necessity regardless of time size or the programming ecosystem used. Every
project should immediately begin by using a version control system such
as Git or Mercurial.

<img src="theme/img/app-source-control.png" width="100%" class="technical-diagram" alt="App deployment uses a server to pull from the source control system.">

Pulling code during a deployment is One way source control systems can fit 
into the deployment process. 

Note that some developers recommend deployment pipelines package the source 
code to deploy it and never have a production environment touch a source 
control system directly. However, for small scale deployments it's often
easiest to pull from source code when you're getting started instead of 
figuring out how to wrap the Python code in a system installation package.


## Source control systems
* [Git](http://git-scm.com/) is a free and open source distributed version
  control system.

* [Mercurial](http://mercurial.selenic.com/) is similar to Git, also a free
  and open source distributed version control system.


## Source control hosted services
* [GitHub](https://github.com/) is currently the most commonly used source
  control platform for using Git.

* [BitBucket](https://bitbucket.org/) provides free Git and Mercurial 
  repositories for open projects and private repositories for up to five
  users. Users pay for hosting private repositories with more than five users.


## Source control resources
* [Staging Servers, Source Control & Deploy Workflows, And Other Stuff Nobody Teaches You](http://www.kalzumeus.com/2010/12/12/staging-servers-source-control-deploy-workflows-and-other-stuff-nobody-teaches-you/) 
  is a comprehensive overview by Patrick McKenzie of why you need source 
  control.

* [Version control best practices](https://blog.rainforestqa.com/2014-05-28-version-control-best-practices/)
  is a good write up of how to work with version control systems. The post is 
  part of an ongoing deployment guide written by the folks at 
  [Rainforest](https://www.rainforestqa.com/).

* This lighthearted guide to the 
  [ten astonishments in version control history](http://www.flourish.org/blog/?p=397) 
  is a fun way to learn how systems developed over the past several decades.

* [A visual guide to version control](http://betterexplained.com/articles/a-visual-guide-to-version-control/) 
  is a detailed article with real-life examples for why version control is
  necessary in software development.

* [An introduction to version control](http://guides.beanstalkapp.com/version-control/intro-to-version-control.html) 
  shows the basic concepts behind version control systems.

* [What Is Version Control? Why Is It Important For Due Diligence?](http://oss-watch.ac.uk/resources/versioncontrol) 
  explains the benefits and necessity of version control systems.

* [About version control](http://git-scm.com/book/en/Getting-Started-About-Version-Control) 
reviews the basics of distributed version control systems.


## Git resources
* [Pro Git](http://git-scm.com/book) is a free open source book that walks 
  through all aspects of using the version control system.

* [A Hacker's Guide to Git](http://wildlyinaccurate.com/a-hackers-guide-to-git)
  covers the basics as well as more advanced Git commands while explaining each
  step along the way.

* [git ready](http://gitready.com/) has a nice collection of blog posts based on
  beginner, intermediate and advanced Git use cases.

* [git-flow](http://nvie.com/posts/a-successful-git-branching-model/) details
  a Git branching model for small teams.

* [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html) builds on
  git-flow, goes over some of the issues that arise with it and presents a
  few solutions to those problems.

* [Git Workflows That Work](http://blog.endpoint.com/2014/05/git-workflows-that-work.html)
  is a helpful post with diagrams to show how teams can create a Git workflow
  that will help their development process.

* "[Our Git Workflow](http://www.braintreepaymentsolutions.com/devblog/our-git-workflow)"
  by Braintree goes over how this payments company uses Git for development
  and merging source code.


## Source control learning checklist
<i class="fa fa-check-square-o"></i>
Pick a version control system. Git is recommended because on the web there 
are a significant number of tutorials to help both new and advanced users.

<i class="fa fa-check-square-o"></i>
Learn basic use cases for version control such as committing changes, rolling 
back to earlier file versions and searching for when lines of code were 
modified during development history.

<i class="fa fa-check-square-o"></i>
Ensure your source code is backed up in a central repository. A central
repository is critical not only if your local development version is corrupted
but also for the deployment process.

<i class="fa fa-check-square-o"></i>
Integrate source control into your deployment process in three ways. First,
pull the project source code from version control during deployments. Second, 
kick off deployments when code is modified by using webhooks or polling on 
the repository. Third, ensure you can roll back to a previous version if a 
code deployment goes wrong.


### Now that your source code is versioned, what's next?
