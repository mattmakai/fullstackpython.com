title: Source Control
category: page
slug: source-control
sortorder: 0218
toc: False
sidebartitle: Source Control
meta: Source control versions and backs up code for when programming problems occur. Learn more about source control on Full Stack Python.


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


## Monorepo vs Multirepo
There is a spectrum of philosophies for how to store projects within
source code repositories. 

On one extreme end of the spectrum, every line of code for every project 
within an organization is stored **in a single repository**. That approach 
is called *monorepo* and it is used by companies like Google. On the other 
end of the spectrum, there are potentially tens of thousands or more 
repositories that store parts of projects. That approach is known as
*multirepo* or *manyrepo*. 

For example, in a [microservices](/microservices.html) architecture, there
could be thousands of microservices and each one is stored within its own
repository. No one repository contains the code for the entire application
created by the interaction of the microservices.

There are many hybrid strategies for how to store source code that fall
between these opposite approaches. What to choose will depend on your
organization's needs, resources and culture.


## Source control during deployment
Pulling code during a deployment is a potential way source control systems fit
into the deployment process. 

<img src="/img/visuals/app-source-control.png" width="100%" class="shot" alt="App deployment uses a server to pull from the source control system.">

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
today's Python development world. The three primary choices are:

* [Git](/git.html) is a free and open source distributed version
  control system.

* [Mercurial](/mercurial.html) is similar to Git, also a free
  and open source distributed version control system.

* [Subversion](https://subversion.apache.org/) is a centralized system where
  developers must check files in and out of the hosted repository to minimize
  merge conflicts.


## Hosted version control services
Git and Mercurial can be downloaded and run on your own server. However,
it's easy and cheap to get started with a hosted version control service.
You can transition away from the service at a later time by moving your 
repositories if your needs change. A couple of recommended hosted version
control services are:

* [GitLab](https://about.gitlab.com/) has both a self-hosted version of its
  open source software as well as their hosted version with 
  [pricing](https://about.gitlab.com/pricing/) for businesses that need
  additional hosting support.

* [GitHub](https://github.com) is a software-as-a-service platform that 
  provides a user interface, tools and backup for developers to use with their 
  [Git](/git.html) repositories. Accounts are free for public open source 
  development and private Git repositories can also be hosted for 
  [$7 per month](https://github.com/pricing).

* [BitBucket](https://bitbucket.org/) is 
  [Atlassian](https://www.atlassian.com/)'s software-as-a-service tool 
  with a user interface, comparison tools and backup for Git projects. There 
  are many features in BitBucket focused on making it easier for groups of 
  developers to work on projects together. BitBucket also has free private 
  repositories for up to five users. Users pay for hosting private 
  repositories with more than five users.


## General source control resources
* [Staging Servers, Source Control & Deploy Workflows, And Other Stuff Nobody Teaches You](https://www.kalzumeus.com/2010/12/12/staging-servers-source-control-deploy-workflows-and-other-stuff-nobody-teaches-you/) 
  is a comprehensive overview by Patrick McKenzie of why you need source 
  control.

* [Version control best practices](https://blog.rainforestqa.com/2014-05-28-version-control-best-practices/)
  is a good write up of how to work with version control systems. The post is 
  part of an ongoing deployment guide written by the folks at 
  [Rainforest](https://www.rainforestqa.com/).

* [A visual guide to version control](https://betterexplained.com/articles/a-visual-guide-to-version-control/) 
  is a detailed article with real-life examples for why version control is
  necessary in software development.

* [An introduction to version control](http://guides.beanstalkapp.com/version-control/intro-to-version-control.html) 
  shows the basic concepts behind version control systems.

* [What Is Version Control? Why Is It Important For Due Diligence?](http://oss-watch.ac.uk/resources/versioncontrol) 
  explains the benefits and necessity of version control systems.

* [Version control before Git with CVS](https://twobithistory.org/2018/07/07/cvs.html)
  goes into the history of version control systems and defines three 
  generations, of which CVS and SVN were part of the second generation
  while Git and Mercurial are third-generation version control systems.

* [About version control](https://git-scm.com/book/en/Getting-Started-About-Version-Control) 
reviews the basics of distributed version control systems.

* [Why not Git?](https://sqlite.org/whynotgit.html) covers 
  [SQLite](/sqlite.html)'s development workflow and why they do not
  use [Git](/git.html) as their version control system.


### Monorepo vs multirepo resources
Monorepo versus multirepo version control strategies are a weirdly 
contentious topic in software development, likely because once a policy
is set for an organization it is exceptionally difficult to change
your approach. The following resources give more insight into the debate
on how to structure your repositories.

* [Monorepo, Manyrepo, Metarepo](https://notes.burke.libbey.me/metarepo/)
  is an awesome guide to varying ways of structuring your source repositories
  that contain more than one project. The guide covers advantages and
  disadvantages of common approaches used in both small and large 
  organizations.

* [Repo Style Wars: Mono vs Multi](http://www.gigamonkeys.com/mono-vs-multi/)
  goes into the implications of using one side or the other and why it is
  unlikely you can create a combination solution that will give you the
  advantages of both without the disadvantages.

* [Why Google Stores Billions of Lines of Code in a Single Repository](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext)
  covers the history and background of Google's source control monorepo, 
  which is one of if not the largest monorepo for an organization in the
  world.

* [Advantages of monorepos](https://danluu.com/monorepo/) goes into the
  advantages of using a monorepo and does not discuss the downsides but
  admits there are many so the decision is not clear-cut on using either
  strategy.

* [Monorepos and the Fallacy of Scale](https://presumably.de/monorepos-and-the-fallacy-of-scale.html)
  argues that having all of an organization's code in a single repository
  encourages code sharing. The author considers the concerns often raised 
  about tight coupling between components in a monorepo code base but says
  that the advantages outweigh the disadvantages overall.


### Git distributed source control system
[Git](/git.html) is the most widely-used source control system currently
in use. Its distributed design eliminates the need to check files in
and out of a centralized repository, which is a problem when using
[Subversion](https://subversion.apache.org/) without a network connection. There is
[a full page on Git](/git.html) with further details and resources.


### Subversion resources
[Apache Subversion](https://subversion.apache.org/)
([source code](https://subversion.apache.org/source-code.html)), 
often just called "Subversion" or "SVN", is a source control system 
implementation.

* The [SVN book](http://svnbook.red-bean.com/en/1.7/index.html) is the
  free online version of the O'Reilly 
  [Version Control with Subversion](https://www.amazon.com/dp/B002SR2QIW/) book.

* [How to Host SVN Repositories](https://www.perforce.com/blog/vcs/how-host-subversion-svn) 
  lays out the basic concepts and provides the first few steps for getting 
  started tracking files.

* [10 Most Used SVN Commands with Examples](http://www.thegeekstuff.com/2011/04/svn-command-examples/)
  is a good refresher list if you've used SVN in the past but it has been 
  awhile since you worked with all the commands.


### Source control learning checklist
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

