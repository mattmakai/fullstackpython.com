title: Virtual environments (virtualenvs)
category: page
slug: virtual-environments-virtualenvs-venvs
sortorder: 0216
toc: False
sidebartitle: Virtualenvs
meta: Virtual environments (virtualenvs) provide dependency isolation for your projects from external libraries.


Virtual environments, implemented by the library virtualenv and venv 
(added to Python standard library in Python 3.3 via 
[PEP 405](https://www.python.org/dev/peps/pep-0405/)), separate project
dependencies, such as the [Django](/django.html) library code, 
from your code projects. For example, if you have three projects,
one that uses Django 1.7, another that uses Django 2.0 and another project
that does not use Django at all, you will have three virtualenvs that
each contain those dependencies separated from each other.


## How do virtualenvs work?
Virtualenv provides dependency isolation for Python projects. A
virtualenv creates a separate copy of the Python installation that is
clean of existing code libraries and provides a directory for new
[application dependencies](/application-dependencies.html) on a 
per-project basis. A programmer can technically use a virtualenv for many 
projects at once but that is not consider to be a good practice.


### Virtual environment resources
* [Package management in Python 2 or 3 (Linux and Mac) with virtualenv or venv](http://aaronsnitzer.com/writing/2016/04/27/virtualenv-and-pyvenv-beginner-tutorial.html)

* [There’s no magic: virtualenv edition](https://www.recurse.com/blog/14-there-is-no-magic-virtualenv-edition)

* [Virtual environments dymystified](https://meribold.github.io/python/2018/02/13/virtual-environments-9487/)

* [What is the relationship between virtualenv and pyenv?](https://stackoverflow.com/questions/29950300/what-is-the-relationship-between-virtualenv-and-pyenv)

* [Setting up Python on a Unix machine (with pyenv and direnv)](https://mike.place/2017/python-pyenv/)

* [venv — Create Virtual Environments](https://pymotw.com/3/venv/)

* [Python development environment, 2020 edition](https://jacobian.org/2019/nov/11/python-environment-2020/)

