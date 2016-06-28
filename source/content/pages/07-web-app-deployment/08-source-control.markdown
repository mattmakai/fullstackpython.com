title: Source Control
category: page
slug: source-control
sortorder: 0708
toc: False
sidebartitle: Source Control
meta: Source control versions and backs up code for when programming problems occur. Learn more about source control on Full Stack Python.


# Source control
Source control, also known as *version control*, stores software code files
with a detailed history of every modification made to those files.

## Why is source control necessary?
Version control systems allow developers to modify code without worrying 
about permanently screwing something up. Unwanted changes can be easily rolled
back to previous working versions of the code. 

Source control also makes team software development easier. One developer 
can combine her code modifications with other developers' code through 
[diff](http://en.wikipedia.org/wiki/Diff) views that show line-by-line 
changes then merge the appropriate code into the main code branch.

Version control is a necessity on all software projects regardless of 
development time, codebase size or the programming language used. Every
project should immediately begin by using a version control system such
as Git or Mercurial.

## Source control during deployment
Pulling code during a deployment is a potential way source control systems fit
into the deployment process. 

<img src="/img/app-source-control.png" width="100%" class="technical-diagram" alt="App deployment uses a server to pull from the source control system.">

Note that some developers recommend deployment pipelines package the source 
code to deploy it and never have a production environment touch a source 
control system directly. However, for small scale deployments it's often
easiest to pull from source code when you're getting started instead of 
figuring out how to wrap the Python code in a system installation package.


## Source control projects
Numerous source control systems have been created over the past several
decades. In the past, proprietary source control software offered features
tailored to large development teams and specific project workflows. However,
open source systems are now used for version control on the largest and most
complicated software projects in existence. There's no reason why your project
should use anything other than an open source version control system in
today's Python development world. The two primary choices are:

* [Git](http://git-scm.com/) is a free and open source distributed version
  control system.

* [Mercurial](http://mercurial.selenic.com/) is similar to Git, also a free
  and open source distributed version control system.


## Hosted source control services
Git and Mercurial can be downloaded and run on your own server. However,
it's easy and cheap to get started with a hosted version control service.
You can transition away from the service at a later time by moving your 
repositories if your needs change. A couple of recommended hosted version
control services are:

* [GitLab](https://about.gitlab.com/) has both a self-hosted version of its
  open source software as well as their hosted version with 
  [pricing](https://about.gitlab.com/pricing/) for businesses that need
  additional hosting support.

* [GitHub](https://github.com/) provides free open source repositories 
  and paid private repositories for Git.

* [BitBucket](https://bitbucket.org/) also has free Git and Mercurial 
  repositories for open projects, but adds private repositories for up to 
  five users. Users pay for hosting private repositories with more than 
  five users.


## General source control resources
* [Staging Servers, Source Control & Deploy Workflows, And Other Stuff Nobody Teaches You](http://www.kalzumeus.com/2010/12/12/staging-servers-source-control-deploy-workflows-and-other-stuff-nobody-teaches-you/) 
  is a comprehensive overview by Patrick McKenzie of why you need source 
  control.

* [Version control best practices](https://blog.rainforestqa.com/2014-05-28-version-control-best-practices/)
  is a good write up of how to work with version control systems. The post is 
  part of an ongoing deployment guide written by the folks at 
  [Rainforest](https://www.rainforestqa.com/).

* This lighthearted guide to the 
  [ten astonishments in version control history](http://www.flourish.org/2011/12/astonishments-ten-in-the-history-of-version-control/) 
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

* [Git in Six Hundred Words](http://maryrosecook.com/blog/post/git-in-six-hundred-words)
  is a clear and concise essay explaining the fundamental concepts of
  Git.

* [A Hacker's Guide to Git](http://wildlyinaccurate.com/a-hackers-guide-to-git)
  covers the basics as well as more advanced Git commands while explaining each
  step along the way.

* [Think like a Git](http://think-like-a-git.net/) is another introduction
  that focuses more on the graph theory and conceptual ideas behind Git
  to help the reader understand what's happening as they use Git commands.

* [A practical git introduction](http://mrchlblng.me/2014/09/practical-git-introduction/)
  is exactly what the title says it is. This is a well written guide with 
  plenty of code snippets to get you up to speed with Git.

* [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out)
  demonstrates how Git's graph-based data structure produces certain behavior 
  through example Git commands. This is a highly recommended read after you've
  grasped the basics and are looking to go deeper with Git.

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

* [Code Sleuthing with Git](https://robots.thoughtbot.com/code-sleuthing-with-git)
  shows how to review past changes when a deployment goes wrong to figure
  out what the heck happened.


## Source control learning checklist
1. Pick a version control system. Git is recommended because on the web there
   are a significant number of tutorials to help both new and advanced users.

1. Learn basic use cases for version control such as committing changes, 
   rolling back to earlier file versions and searching for when lines of code 
   were modified during development history.

1. Ensure your source code is backed up in a central repository. A central
   repository is critical not only if your local development version is 
   corrupted but also for the deployment process.

1. Integrate source control into your deployment process in three ways. First,
   pull the project source code from version control during deployments. 
   Second, kick off deployments when code is modified by using webhooks or 
   polling on the repository. Third, ensure you can roll back to a previous 
   version if a code deployment goes wrong.

