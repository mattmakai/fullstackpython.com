title: Code Metrics
category: page
slug: code-metrics
sort-order: 0603
choice1url: /continuous-integration.html
choice1icon: fa-refresh
choice1text: How can I continuously evaluate my code with these metrics?
choice2url: /task-queues.html
choice2icon: fa-tasks
choice2text: How can I call functions outside the HTTP requests?
choice3url: /web-application-security.html
choice3icon: fa-lock fa-inverse
choice3text: What should I do to secure my web application?
choice4url:
choice4icon:
choice4text:


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
* [Landscape](https://landscape.io/) provides free code metrics for open 
  source Python projects. Pricing is available for analyzing private 
  repositories as well.


## Code metrics resources
* [Static Code Analizers for Python](http://doughellmann.com/2008/03/01/static-code-analizers-for-python.html)
  is an older article but goes over the basics of what Python static code
  analyzers do.

* This [Stack Overflow question on Python static code analysis tools](http://stackoverflow.com/questions/1428872/pylint-pychecker-or-pyflakes)
  contains comparison discussions of PyLint, PyChecker and PyFlakes.


### What's next after obtaining code metrics?
