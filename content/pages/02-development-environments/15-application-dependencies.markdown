title: Application Dependencies
category: page
slug: application-dependencies
sortorder: 0215
toc: False
sidebartitle: Application Dependencies
meta: Python web applications depend on many code libraries. Learn more about application dependencies on Full Stack Python.


Application dependencies are the libraries other than your project code
that are required to create and run your application. 


## Why are application dependencies important?
Python web applications are built upon the work done by thousands of open
source programmers. Application dependencies include not only web frameworks but
also libraries for scraping, parsing, processing, analyzing, visualizing, 
and many other tasks. Python's ecosystem facilitates discovery, retrieval and 
installation so applications are easier for developers to create.


## Finding libraries
Python libraries are stored in a central location known as the 
[Python Package Index](https://pypi.org/). PyPi contains
search functionality with results weighted by usage and relevance based on
keyword terms.

Besides PyPi there are numerous resources that list common or "must-have" 
libraries. Ultimately the decision for which application dependencies are
necessary for your project is up to you and the functionality you're looking
to build. However, it's useful to browse through these lists in case you come 
across a library to solve a problem by reusing the code instead of writing it
all yourself. A few of the best collections of Python libraries are

* [Python.org's useful modules](https://wiki.python.org/moin/UsefulModules)
  which groups modules into categories.

* [GitHub Explore Trending repositories](https://github.com/trending?l=python)
  shows the open source Python projects trending today, this week, and this 
  month.

* Wikipedia actually has an extensive 
  [page dedicated to Python libraries](http://en.wikipedia.org/wiki/List_of_Python_software) 
  grouped by categories.
  

## Isolating dependencies
Dependencies are installed separately from system-level packages to prevent 
library version conflicts. The most common isolation method is 
[virtualenv](https://virtualenv.pypa.io/en/latest/). Each virtualenv is its
own copy of the Python interpreter and dependencies in the site-packages
directory. To use a virtualenv it must first be created with the virtualenv
command and then activated.

The virtualenv stores dependencies in an isolated environment. The web 
application then relies only on that virtualenv instance which has a separate
copy of the Python interpreter and site-packages directory. A high level of
how a server configured with virtualenv can look is shown in the picture below.

<img src="/img/visuals/server-setup.png" alt="How the virtualenv separates dependencies on the server." width="100%" class="shot" />


## Installing Python dependencies
The recommended way to install Python library dependencies is with the 
[pip](http://www.pip-installer.org/en/latest/) command when a virtualenv
is activated.

Pip and virtualenv work together and have complementary responsibilities.
Pip downloads and installs application dependencies from the central
[PyPi](https://pypi.python.org/pypi) repository. 


## requirements.txt
The pip convention for specifying application dependencies is with a 
`requirements.txt` file. When you build a Python web application you 
should include `requirements.txt` in the base directory of your project.

Python projects' dependencies for a web application should be specified 
with pegged dependencies like the following:

```
django==1.11.0
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
```

Pegged dependencies with precise version numbers or Git tags are important 
because otherwise the latest version of a dependency will be used. While
it may sound good to stay up to date, there's no telling if your application
actually works with the latest versions of all dependencies. Developers should 
deliberately upgrade and test to make sure there were no backwards-incompatible
modifications in newer dependency library versions.


## setup.py
There is another type of dependency specification for Python libraries
known as 
[setup.py](http://stackoverflow.com/questions/1471994/what-is-setup-py).
Setup.py is a standard for distributing and installing Python libraries.
If you're building a Python library, such as 
[twilio](https://github.com/twilio/twilio-python) or
[underwear](https://github.com/mattmakai/underwear) you must include setup.py
so a dependency manager can correctly install both the library as well as
additional dependencies for the library. There's still quite a bit of 
confusion in the Python community over the difference between 
requirements.txt and setup.py, so read this 
[well written post](https://caremad.io/2013/07/setup-vs-requirement/) for
further clarification.


### Open source app dependency projects
[pip and venv](https://docs.python.org/3/library/venv.html) are part of 
Python 3's standard library as of version 3.3. However, there are numerous
other open source libraries that can be helpful when managing application
dependencies in your projects, as listed below.

* [Autoenv](https://github.com/kennethreitz/autoenv) is a tool for activating
  environment variables stored in a `.env` file in your projects' home
  directories. Environment variables aren't managed by virtualenv and although
  virtualenvwrapper has some hooks for handling them, it's often easiest to
  use a shell script or `.env` file to set them in a development environment.

* [Pipenv](https://pipenv.readthedocs.io/en/latest/) is a newer Python 
  packaging and dependency management library that has seen some adoption
  in place of the standard `pip` library.

* [Pipreqs](https://github.com/bndr/pipreqs) searches through a project for
  dependencies based on imports. It then generates a `requirements.txt` file
  based on the libraries necessary to run those dependencies. Note though that
  while this could come in handy with a legacy project, the version numbers
  for those libraries will not be generated with the output.

* [pip-check](https://github.com/bartTC/pip-check) presents a nicely-formatted
  list of all your installed dependencies and the status of whether or not
  updates are available for each of them.

* [pip-name](https://github.com/prakashdanish/pip-name) is a straightforward
  library that looks up package names on PyPI and tells you whether or not
  the library name is already taken.


### Code library packaging guides
There are many steps in creating and distributing packages on PyPI and 
your own hosted application dependency servers. Many of these steps involve
writing configuration files that are not as well documented as some other
areas of Python development. These resources are the best ones I have found
so far to get up to speed on building and releasing your own packages.

* [Python Packaging User Guide](https://packaging.python.org/)
  provides a collection of resources to understand how to package and 
  distribute Python code libraries.

* [Alice in Python projectland](https://veekaybee.github.io/2017/09/26/python-packaging/)
  is an amazing post that takes the reader from simple Python script
  into a complete Python package.

* [How to Publish Your Package on PyPI](https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/)
  is for developers who have created a code library they would like to
  share and make installable for other developers.


### Application dependency resources
The following links provide advice on how to use Python packages as well
as package your own dependencies for projects or consumption by other
developers.

* [Python's New Package Landscape](http://andrewsforge.com/article/python-new-package-landscape/)
  covers the history of Python packaging tools and examines the
  problems with dependency isolation and the dependency graphs that 
  newer tools such as 
  [Pipenv](https://pipenv.readthedocs.io/en/latest/), 
  [Poetry](https://poetry.eustace.io/), 
  [Hatch](https://github.com/ofek/hatch) and 
  [pipsi](https://github.com/mitsuhiko/pipsi) 
  aim to solve.

* [Python Packaging Is Good Now](https://glyph.twistedmatrix.com/2016/08/python-packaging.html)
  is a wonderfully written blog post. It provides historical context on why
  Python's code library packaging was painful for a long time, and what's 
  been fixed to make building and installing application dependencies so
  much better.

* [A non-magical introduction to virtualenv and pip](http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/) 
  breaks down what problems these tools solve and how to use them.

* [There’s no magic: virtualenv edition](https://www.recurse.com/blog/14-there-is-no-magic-virtualenv-edition)
  breaks open the virtual environment "black box" to show you what the
  tool is doing when you use its commands.

* [Using pyenv to manage your Python interpreters](https://www.marc-richter.info/using-pyenv-to-manage-your-python-interpreters/)
  explains how the pyenv tool can make it easier to switch between different
  versions of Python for each project and gives a brief review of the
  important things to know when using the tool such as local versus global
  scope.

* [Testing & Packaging](https://hynek.me/articles/testing-packaging/) examines
  a configuration for ensuring tests run against your code and how to
  properly package your project.

* [12 Alternatives for Distributing Python Applications in 2020](https://tryexceptpass.org/article/distributing-python-applications/)
  covers packaging with [Docker](/docker.html), Vagrant, PyInstaller, 
  Briefcase, virtual environments, Pipx and several more options for
  bundling and running Python code.

* [Python Application Dependency Management in 2018](https://hynek.me/articles/python-app-deps-2018/)
  presents some critical analysis and critique of the existing Python
  dependency management tools including newer ones such as pipenv and
  Poetry.

* [Open source trust scaling](http://lucumr.pocoo.org/2016/3/24/open-source-trust-scaling/)
  is a good piece for the [Python community](/python-community.html) 
  (and other programming communities) that is based on the 
  [left-pad NPM situation](https://kodfabrik.com/journal/i-ve-just-liberated-my-modules)
  that broke many dependent packages in the Node.js community.

* Major speed improvements were made in pip 7 over previous versions. Read 
  [this article about the differences](https://lincolnloop.com/blog/fast-immutable-python-deployments/)
  and be sure to upgrade.

* [Typosquatting programming language package managers](https://incolumitas.com/2016/06/08/typosquatting-package-managers/)
  shows how many packages on centralized dependency servers for Python, 
  Node.js and Ruby can be vulnerable to "typosquatting" where a developer
  either confuses a fake package for the correct one or simply makes a
  typo when specifying her dependency list.

* [The Many Layers of Packaging](https://sedimental.org/the_packaging_gradient.html)
  goes up and down the packaging stack and even covers bits about virtual
  environments and security. It's well worth investing some time to read
  this post to get an overview of the many layers involved in dependency
  packaging.


### Application dependencies learning checklist
1. Ensure the libraries your web application depends on are all captured in 
   a `requirement.txt` file with pegged versions. 

1. An easy way to capture currently installed dependencies is with the 
   `pip freeze` command.

1. Create a fresh virtualenv and install the dependencies from your 
   `requirements.txt` file by using the `pip install -r requirements.txt` 
   command.

1. Check that your application runs properly with the fresh virtualenv and 
   only the installed dependencies from the `requirements.txt` file.

