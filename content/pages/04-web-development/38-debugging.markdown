title: Debugging
category: page
slug: debugging
sortorder: 0438
toc: False
sidebartitle: Debugging
meta: Debugging involves instrumenting, isolating and hunting defects in running code. Learn more about debugging on Full Stack Python.


# Debugging
Developers often find themselves in situations where the code they've written
is not working quite right. When that happens, a developer debugs their code
by instrumenting, executing and inspecting the code to determine what state
of the application does not match the assumptions of how the code should
be correctly running.


## Why is debugging important?
There are bugs in every modest sized or larger application. Every 
developer has to learn how to debug code in order to write programs that
work as correctly as time and budget allow.


### Debugging tools
There are many debugging tools, some of which are built into 
[IDEs](/text-editors-ides.html) like [PyCharm](/pycharm.html) and others
that are standalone applications. The following list contains mostly 
standalone tools that you can use in any 
[development environment](/development-environments.html).

* [pdb](https://docs.python.org/3/library/pdb.html) is a debugger built
  into the Python standard library and is the one most developers come across
  first when trying to debug their programs.

* [Web-PDB](https://github.com/romanvm/python-web-pdb) provides a
  web-based user interface for pdb to make it easier to understand what is
  happening while inspecting your running code.

* [wdb](https://github.com/Kozea/wdb) uses [WebSockets](/websockets.html)
  to allow you to debug running Python code from a web browser.

* [Pyflame](http://eng.uber.com/pyflame/) 
  ([source code](https://github.com/uber/pyflame)) is a profiling tool
  that generates [flame graphs](http://www.brendangregg.com/flamegraphs.html)
  for executing Python program code.

* [objgraph](https://mg.pov.lt/objgraph/)
  ([source code](https://github.com/mgedmin/objgraph)) uses 
  [graphviz](https://www.graphviz.org/) to draw the connections between 
  Python objects running in an application


### Python-specific debugging tutorials
The Python ecosystem has a range of tools to help with debugging your code.
These tutorials are specific to Python libraries like pdb and objgraph.

* [Debugging your Python code](http://howchoo.com/g/zgi2y2iwyze/debugging-your-python-code)
  walks through a scenario where 
  [pdb](https://docs.python.org/3/library/pdb.html) 
  can be used to find a defect in a block of Python code.

* [How to Use Pdb to Debug Your Code](https://pybit.es/pdb-debugger.html)
  is a wonderful code-first tutorial on getting started with pdb.

* [pdb - Interactive Debugger](https://pymotw.com/3/pdb/) is featured on
  the Python Module of the Week blog and has some great detail on using
  the program effectively.

* [Python debugging tools](http://blog.ionelmc.ro/2013/06/05/python-debugging-tools/)
  provides a list of tools such as pdb and its derivatives ipdb, pudb and
  pdb++ along with how they can be used in the hunt for defects.

* [Debugging in Python](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/)
  elaborates on what pdb does and how it can be used.

* [Profiling Python web applications with visual tools](https://mitjafelicijan.com/profiling-python-web-applications-with-visual-tools)
  details a configuration for visualizing code execution using 
  [KCachegrind](http://kcachegrind.sourceforge.net/html/Home.html).

* [pdb: Using the Python debugger in Django](https://mike.tig.as/blog/2010/09/14/pdb/)
  is a tutorial specific to working with pdb in [Django](/django.html)
  projects.

* [My Startling Encounter With Python Debuggers](https://benbernardblog.com/my-startling-encounter-with-python-debuggers/)
  along with 
  [the follow-up second post](https://benbernardblog.com/my-startling-encounter-with-python-debuggers-part-2/)
  are a fantastic couple of posts that walk through a specific scenario
  of how a well-tested distributed web crawler failed and how tools like
  gdb, top and Winpdb were used to debug a multithreaded application.


### General debugging resources
The following resources are not specific to Python development but
give solid programming language-agnostic debugging advice.

* [The art of debugging](https://remysharp.com/2015/10/14/the-art-of-debugging)
  provides a whirlwind overview for how to fix issues in your code.

* [How to debug JavaScript errors](https://rollbar.com/guides/how-to-debug-javascript/)
  introduces some key debugging tools such as source maps that make
  identifying errors on the client side much easier during development.

* [Linux debugging tools you'll love](https://jvns.ca/debugging-zine.pdf)
  is an awesome comic that covers the Linux ecosystem for debugging.
  
