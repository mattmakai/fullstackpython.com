title: Application Dependencies
category: page
slug: application-dependencies
sort-order: 09


# Application Dependencies
Application dependencies are the libraries other than your project code
that are required to create and run your application. 


## Why are application dependencies important?
Python web applications are built upon the work done by thousands of open
source programmers. Application dependencies include not only web frameworks but
also libraries for scraping, parsing, processing, analyzing, visualizing, 
and myriad other tasks. Python's ecosystem facilitates discovery, retrieval and 
installation so applications are easier for developers to create.

## Finding libraries
Python libraries are stored in a central location known as the 
[Python Package Index](https://pypi.python.org/pypi) (PyPi). PyPi contains
search functionality with results weighted by usage and relevance based on
keyword terms.


## Isolating application dependencies
Dependencies are installed separately from system-level packages to prevent 
library version conflicts. The most common isolation method is 
[virtualenv](http://www.virtualenv.org/en/latest/). Each virtualenv is its
own copy of the Python interpreter and depedencies in the site-packages
directory. To use a virtualenv it must first be created with the virtualenv
command and then activated.


## Downloading and installing Python dependencies
The recommended way to install Python library dependencies is with the 
[pip](http://www.pip-installer.org/en/latest/) command when a virtualenv
is activated.

Pip and virtualenv work together and have complementary responsibilities.
Pip downloads and installs application dependencies from the central
[PyPi](https://pypi.python.org/pypi) repository. 


## requirements.txt
The pip convention for specifying application dependencies is with a 
[requirements.txt](http://www.pip-installer.org/en/1.4.1/cookbook.html#requirements-files)
file. When you build a Python web application you should include a 
requirements.txt file. 


### requirementst.txt example with pegged dependencies
Python projects' dependencies for a web application should be specified in the
requirements.txt with 
[pegged dependencies](https://devcenter.heroku.com/articles/python-pip) like
the following:

    django==1.6
    bpython==0.12
    django-braces==0.2.1
    django-model-utils==1.1.0
    logutils==0.3.3
    South==0.7.6
    requests==1.2.0
    stripe==1.9.1
    dj-database-url==0.2.1
    django-oauth2-provider==0.2.4
    djangorestframework==2.3.1

Pegged dependencies with precise version numbers or Git tags are important 
because otherwise the latest version of a dependency will be used. While
it may sound good to stay up to date, there's no telling if your application
actually works with the latest versions of all dependencies. Developers should 
deliberately upgrade and test to make sure there were no backwards-incompatible
modifications in newer dependency library versions.


##setup.py
There is another type of dependency specification for Python libraries
known as 
[setup.py](http://stackoverflow.com/questions/1471994/what-is-setup-py).
Setup.py is a standard for distributing and installing Python libraries.
If you're building a Python library, such as 
[requests](http://www.python-requests.org/en/latest/) or
[underwear](https://github.com/makaimc/underwear) you must include setup.py
so a dependency manager can correctly install both the library as well as
additional dependencies for the library. There's still quite a bit of 
confusion in the Python community over the difference between 
requirements.txt and setup.py, so read this 
[well written post](https://caremad.io/blog/setup-vs-requirement/) for
further clarification.


## Application dependency resources
* [Jon Chu](https://twitter.com/jonathanchu) wrote a great introduction on 
  [virtualenv and pip basics](http://www.jontourage.com/2011/02/09/virtualenv-pip-basics/).

* "[A non-magical introduction to virtualenv and pip](http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/) 
  breaks down what problems these tools solve and how to use them.

* [Tools of the modern Python hacker](http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip/) 
  contains detailed explanations of virtualenv, Fabric, and pip.

* Occasionally arguments about using Python's dependency manager versus
  one of Linux's depenency managers comes up. This provides
  [one perspective on that debate](http://notes.pault.ag/debian-python/).
