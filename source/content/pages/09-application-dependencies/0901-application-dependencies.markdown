title: Application Dependencies
category: page
slug: application-dependencies
sort-order: 09


# Application Dependencies
Application dependencies are the Python libraries and their versions
required for an application to work properly. These dependencies are 
installed separately from system-level packages to prevent library version
conflicts.

The most common way to install Python library dependencies is with 
the [pip](http://www.pip-installer.org/en/latest/)
command combined with 
[virtualenv](http://www.virtualenv.org/en/latest/) to isolate the
dependencies of individual applications from each other.

Pip and virtualenv work together and have complementary responsibilities.
Pip downloads and installs application dependencies from the central
[PyPi](https://pypi.python.org/pypi) repository. Virtualenv creates an 
isolated Python installation is where those dependencies are installed into.


## requirements.txt
The pip convention for specifying application dependencies is with a 
[requirements.txt](http://www.pip-installer.org/en/1.4.1/cookbook.html#requirements-files)
file. When you build a Python web application you should include a 
requirements.txt file with 
[pegged dependencies](https://devcenter.heroku.com/articles/python-pip).


## setup.py
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
