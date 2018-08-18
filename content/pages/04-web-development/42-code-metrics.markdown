title: Code Metrics
category: page
slug: code-metrics
sortorder: 0442
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

* [Pylint](https://pypi.org/project/pylint/) contains checkers for PEP8 code 
  style compliance, design, exceptions and many other source code analysis
  tools.

* [PyFlakes](https://pypi.org/project/pyflakes/) parses source files for
  errors and reports on them.

* [Pyntch](http://www.unixuser.org/~euske/python/pyntch/index.html) is a
  static code analyzer that attempts to detect runtime errors. It does not
  perform code style checking.

* [Prospector](https://github.com/PyCQA/prospector) inspects Python source 
  code files to give data on type and location of classes, methods and 
  other related source information.

* [Flake8](http://flake8.pycqa.org/en/latest/) is a code format style
  guideline enforcer. Its goal is not to gather metrics but ensure 
  a consistent style in all of your Python programs for maximum readability.
  The rules for Flask8 are all defined in 
  [this list](https://lintlyci.github.io/Flake8Rules/), which rolls up
  the Flake8 dependencies of pycodestyle, pyflakes and McCabe.

* [Black](https://github.com/ambv/black) is a Python code formatter with
  strong, uncompromising assumptions about how your code must be formatted.

* [pylintdb](https://github.com/nedbat/pylintdb) puts pylint results into
  a [SQLite](/sqlite.html) database for programmatic access and searching.
  Ned Batchelder coded it and wrote about how he uses the program in this 
  [bite-sized command line tools: pylintdb](https://nedbatchelder.com//blog/201712/bitesized_command_line_tools_pylintdb.html)
  post.


## Hosted code metrics services
The following tools are ready to use by going to the service, punching in
the URL to your site, letting them perform their analysis and then reading
the results.

* [Coveralls](https://coveralls.io) shows code coverage from test suites 
  and other metrics to help developers improve the quality of their code.

* [webhint](https://webhint.io/), formerly 
  [Sonarwhal](https://24ways.org/2017/lint-the-web-forward-with-sonarwhal/)
  scans your website for accessibility, speed and security. There is both
  an online version that you can point at an arbitrary URL as well as
  a command-line version for running yourself.

* [Codecov](https://codecov.io/) hooks into GitHub, BitBucket or GitLab
  and reports code coverage on your code repositories.


## Code metrics resources
Code metrics are really useful when you have a team working on a project
for awhile and want to keep the code quality from degrading. However, you 
can easily go overboard instrumenting everything and overanalyzing the
results. The following resources will introduce code metrics topics to
you as well as give perspective when metrics are useful to the point of
diminishing returns.

* [How do Ruby & Python profilers work?](https://jvns.ca/blog/2017/12/17/how-do-ruby---python-profilers-work-/)
  explains the difference between sampling and tracing profilers then
  digs into how they work and their advantages and disadvantages.

* [Moving Fast With High Code Quality](https://engineering.quora.com/Moving-Fast-With-High-Code-Quality)
  provides Quora's code quality goals and how they handle code reviews
  with their internal tools.

* [Lessons from Building Static Analysis Tools at Google](https://cacm.acm.org/magazines/2018/4/226371-lessons-from-building-static-analysis-tools-at-google/fulltext)
  is a fantastic in-depth read that explains why workflow integration
  and adapting to developer feedback are critical for static analysis
  tools adoption in development environments.

* [Static Code Analizers for Python](http://doughellmann.com/2008/03/01/static-code-analizers-for-python.html)
  is an older article but goes over the basics of what Python static code
  analyzers do.

* [Getting Started with Pylint](http://jbisbee.blogspot.ca/2014/04/getting-started-with-pylint.html)
  goes over setting up Pylint, generating the .pylintrc file and what's
  in the configuration.

* [Linting as Lightweight Defect Detection for Python](https://dev.to/sethmichaellarson/linting-as-lightweight-defect-detection-for-python)
  presents a straightforward code example of how linters can detect certain
  classes of errors in code that especially in dynamically-typed languages
  are not caught at compile time. The post then shows how to use Flake8 in
  your own code reviews.

* This /r/Python 
  [poll on what linters the community uses](https://www.reddit.com/r/Python/comments/3oyjva/what_python_linter_do_you_use_poll/)
  provides some input on using PyCharm just for its linting features as
  well as some other approaches.

* [Automatically PEP8 & Format Your Python Code](https://avilpage.com/2015/05/automatically-pep8-your-python-code.html)
  shows how to use the `autopep8` library, including an [Emacs](/emacs.html)
  plugin that lints your code for PEP8 compliance as you work.

* [How to use Flask8](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html)
  explains what Flask8 is, its usage and expected output.

* [What is Flake8 and why we should use it?](https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2)
  covers why using a linting tool like Flake8 can improve the quality of 
  your Python code and how to install and configure it for your
  environment.

* [Which Python static analysis tools should I use?](https://www.codacy.com/blog/which-python-static-analysis-tools-should-i-use/)
  covers Pylint, PyFlakes and mypy with a short description of the 
  advantages and disadvantage for each one.

* [Dynamic tracing a Pony + Python program with DTrace](https://blog.wallaroolabs.com/2017/12/dynamic-tracing-a-pony---python-program-with-dtrace/)
  shows how to use dynamic tracing programs to analyze code
  at runtime.

* This [Stack Overflow question on Python static code analysis tools](http://stackoverflow.com/questions/1428872/pylint-pychecker-or-pyflakes)
  contains comparison discussions of PyLint, PyChecker and PyFlakes.

