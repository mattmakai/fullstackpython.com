title: Environment configuration
category: page
slug: environment-configuration
sortorder: 0215
toc: False
sidebartitle: Environment configuration
meta: Configuring a dev, test or production environment is important to successfully run a Python application.


# Environment configuration
Properly configuring a development, test or production environment is 
important for the successful execution of your Python application.

There are many de facto names for environments:

1. Local development
1. Development / integration
1. Test
1. Staging
1. Production

The above list provides the common environment names but there
can be a limitless number and each organization has their own 
configuration.


## Environment variables
Environment variables are modifiable system values that can be read 
by Python applications to affect a program's execution.

One answer I found very useful when learning about getting environment
variables in Python code is 
[knowing the difference between os.getenv and os.environ.get](https://stackoverflow.com/questions/16924471/difference-between-os-getenv-and-os-environ-get).
Either one can be used in your applications but there are slight differences 
that can make one better than the other in various situations.
 
Other useful environment variables resources:

* [Environment variables on Ubuntu Linux](https://help.ubuntu.com/community/EnvironmentVariables)

* [Why you shouldn't use ENV variables for secret data](https://diogomonica.com/2017/03/27/why-you-shouldnt-use-env-variables-for-secret-data/)

* [Environment variables in Windows](https://www.digitalcitizen.life/simple-questions-what-are-environment-variables)


### Environment configuration resources
* [Staging Servers, Source Control & Deploy Workflows, And Other Stuff Nobody Teaches You](https://www.kalzumeus.com/2010/12/12/staging-servers-source-control-deploy-workflows-and-other-stuff-nobody-teaches-you/)

* [Deployments best practices](http://guides.beanstalkapp.com/deployments/best-practices.html)
  explains the differences between various environments and why you
  need each one.

* [Best practices for staging environments](https://increment.com/development/center-stage-best-practices-for-staging-environments/)

* [Staging environment vs Production environment](https://softwareengineering.stackexchange.com/questions/117945/staging-environment-vs-production-environment)

* [A good QA team needs a proper software staging environment for testing](https://searchsoftwarequality.techtarget.com/tip/A-good-QA-team-needs-a-proper-software-staging-environment-for-testing)

