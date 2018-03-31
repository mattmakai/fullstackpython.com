title: Development Environments
category: page
slug: development-environments
sortorder: 0200
toc: True
sidebartitle: 2. Development Environments
meta: Development environments allow programmers to read, write and work with code.


# Development Environments
A development environment is a combination of a text editor and the Python
interpreter. The text editor allows you to write the code. The interpreter
provides a way to execute the code you've written. A text editor can be
as simple as Notepad on Windows or more complicated as a complete integrated
development environment (IDE) such as 
[PyCharm](https://www.jetbrains.com/pycharm/) which runs on any major 
operating system.


## Why is a development environment necessary?
Python code needs to be written, executed and tested to build
applications. The text editor provides a way to write the code. The 
interpreter allows it to be executed. Testing to see if the code does what
you want can either be done manually or by unit and functional tests. 

<div class="well see-also">While you're learning about development environments be sure to check out information on <a href="/vim.html">Vim</a> and <a href="/emacs.html">Emacs</a>.</div>


## A development environment example
Here's what I (the author of Full Stack Python, 
[Matt Makai](/about-author.html)) use to develop most of my Python 
applications. I have a Macbook Pro with Mac OS X as its base operating 
system. [Ubuntu 14.04 LTS](/operating-systems.html) is virtualized on top 
with [Parallels](https://www.parallels.com/). My code is written in 
[vim](http://www.vim.org/) and executed with the 
[Python 2.7.x](https://www.python.org/download/releases/2.7.8/) interpreter
via the command line. I use [virtualenv](https://virtualenv.pypa.io/en/latest/) to create separate Python interpreters
with their own isolated
[application dependencies](/application-dependencies.html) and
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
to quickly switch between the interpreters created by virtualenv.

That's a common set up but you can certainly write great code with a much
less expensive set up or a cloud-based development environment.


## Open source text editors
* [vim](http://www.vim.org/) is my editor of choice and installed by default
  on most \*nix systems.

* [emacs](http://www.gnu.org/software/emacs/) is another editor often used
  on \*nix.

* [Atom](https://atom.io/) is an open source editor built by the 
  [GitHub](https://github.com) team.


## Python-specific IDEs
* [PyCharm](https://www.jetbrains.com/pycharm/) is a Python-specific IDE
  built on [JetBrains](https://www.jetbrains.com/)' platform. There are
  free editions for students and open source projects.

* [Thonny](http://thonny.org/) is an 
  [open source](https://bitbucket.org/plas/thonny/src) Python IDE for new 
  programmers. The tool bakes in syntax highlighting, code completion, a 
  simple debugger, a beginner-friendly shell and in situ documentation to
  assist new developers who are just starting to code.

* [Wing IDE](https://wingware.com/) is a paid development environment with
  integrated debugging and code completion.

* [PyDev](http://pydev.org/) is a Python IDE plug in for 
  [Eclipse](https://eclipse.org/).


## Proprietary (closed source) editors
* [Sublime Text](http://www.sublimetext.com/) versions 2 and 3 (currently
  in beta) are popular text editors that can be extended with code completion,
  linting, syntax highlighting and other features using plugins. If you
  are considering using Sublime Text for Python development, check out this
  [2016 in review - likes and dislikes about Sublime Text](https://dbader.org/blog/sublime-text-for-python-development-2016-review)
  post that summarizes many of the positives and negatives of using the
  editor.

* [Komodo](http://komodoide.com/) is a cross-platform text editor and IDE
  for major languages including Python, Ruby, JavaScript, Go and more.


## Hosted development environments
Several cloud-based development environments have popped up over the past
several years. These hosted environments can work well when you are learning
or stuck on a machine with a web browser but otherwise no administrative 
privileges to install your own software. Most of these have free tiers for 
getting started and then require payment as you scale up your application.

* [CodeAnywhere](https://codeanywhere.com/) is a cloud IDE that can be used
  in the web browser or on an iOS or Android device.

* [Cloud9](https://c9.io/) began as an independent company and is now owned 
  by Amazon as part of Amazon Web Services.


## Development environment resources
Development environments are unique to each programmer because Python is
used for many different purposes. The following guides range from 
[web development](/web-development.html) to 
[DevOps](/devops.html) and from 
[getting started](/learning-programming.html) to [data science](/data.html).
Even though your environment requirements are unique, you should be able to 
find someone who has set up something similar to what you need. Use that
configuration as a starting point and customize it from there.

* [The definitive guide to setup my Python workspace](https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14)
  is geared towards using Python for data science but the guide remains
  useful for configuring your system for any type of Python work. There is
  some solid advice in the post about not adulterating your global Python
  installation as well as how to split out many virtual environments for
  Python 2 & 3.

* Real Python has an awesome, detailed post on 
  [setting up your Sublime Text 3 environment](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)
  as a full-fledged IDE.

* [Three Ways to Install Python on your Windows Computer](http://blog.yhat.com/posts/installing-python-on-windows.html)
  provides multiple avenues for Windows users to get Python on their machine
  before setting up the rest of their development environment. Unlike
  macOS and Linux, the Windows [operating system](/operating-systems.html) 
  does not include Python with its default installation.

* [PyCharm vs Sublime Text](https://opensourcehacker.com/2015/05/02/pycharm-vs-sublime-text/)
  has a comparison of several features between the two editors.

* [PyCharm: The Good Parts](http://nafiulis.me/pycharm-the-good-parts-i.html)
  shows you how to be more efficient and productive with that IDE if it's
  your choice for writing Python code.

* JetBrains' [PyCharm Blog](http://blog.jetbrains.com/pycharm/) is required
  reading if you're using the IDE or considering trying it. One of the
  core developers also has an interview on the 
  [Talk Python to Me podcast](http://talkpython.fm/episodes/show/36/python-ides-with-the-pycharm-teama) 
  that's worth listening to.

* [The Joy of Linux Desktop Environments](https://hackernoon.com/the-joy-of-linux-desktop-environments-365d6cc8de72)
  talks about *desktop* environments, not specifically development 
  environments, but provides an explanation for why the core Linux operating
  system is awesome for being unbundled from the desktop environment itself.
  You can change your desktop environment from just a command line without
  a windowing system to a full windowed system provided by Gnome, KDE or 
  Unity for using the system and getting your programming work done.

* The [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/dev/env/)
  has a page dedicated to development environments.

* If you're considering the cloud-based development environment route, check
  out this 
  [great article comparing Cloud9, Koding and Nitrous.io](http://readwrite.com/2014/08/14/cloud9-koding-nitrousio-integrated-development-environment-ide-coding)
  by Lauren Orsini. She also explains more about what a cloud IDE is and is
  not.

