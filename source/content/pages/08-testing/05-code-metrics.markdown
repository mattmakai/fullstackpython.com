title: Code Metrics
category: page
slug: code-metrics
sortorder: 0805
toc: False
sidebartitle: Code Metrics
meta: Code metrics provide insight into the quality of a code base via analysis tools. Learn more about code metrics on Full Stack Python.


# Code Metrics
Code metrics can be produced by static code analysis tools to determine 
complexity and non-standard practices.


## Why are code metrics important?
Code metrics allow developers to find problematic codebase areas that may
need refactoring. In addition, some metrics such as technical debt assist 
developers in communicating to non-technical audiences why issues with a
system are occurring.


## Open source code metrics projects
* [Radon](http://radon.readthedocs.org/en/latest/index.html) is a tool for
  obtaining raw metrics on line counts, Cyclomatic Complexity, Halstead
  metrics and maintainability metrics.

* [Pylint](http://www.pylint.org/) contains checkers for PEP8 code 
  style compliance, design, exceptions and many other source code analysis
  tools.

* [PyFlakes](https://pypi.python.org/pypi/pyflakes) parses source files for
  errors and reports on them.

* [Pyntch](http://www.unixuser.org/~euske/python/pyntch/index.html) is a
  static code analyzer that attempts to detect runtime errors. It does not
  perform code style checking.


## Hosted code metrics services
* [Coveralls](https://coveralls.io) shows code coverage from test suites 
  and other metrics to help developers improve the quality of their code.


## Code metrics resources
* [Static Code Analizers for Python](http://doughellmann.com/2008/03/01/static-code-analizers-for-python.html)
  is an older article but goes over the basics of what Python static code
  analyzers do.

* This [Stack Overflow question on Python static code analysis tools](http://stackoverflow.com/questions/1428872/pylint-pychecker-or-pyflakes)
  contains comparison discussions of PyLint, PyChecker and PyFlakes.

* [Getting Started with Pylint](http://jbisbee.blogspot.ca/2014/04/getting-started-with-pylint.html)
  goes over setting up Pylint, generating the .pylintrc file and what's
  in the configuration.

* This /r/Python 
  [poll on what linters the community uses](https://www.reddit.com/r/Python/comments/3oyjva/what_python_linter_do_you_use_poll/)
  provides some input on using PyCharm just for its linting features as
  well as some other approaches.

