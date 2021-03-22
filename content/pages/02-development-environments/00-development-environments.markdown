title: Development Environments
category: page
slug: development-environments
sortorder: 0200
toc: True
sidebartitle: 2. Development Environments
meta: Development environments allow programmers to read, write and work with code.


A development environment is a combination of a 
[text editor](/text-editors-ides.html) and a Python runtime implementation.
The text editor allows you to write code for your applications. The runtime
implementation, such as [CPython](https://github.com/python/cpython) 
or [PyPy](https://pypy.org/), provides the method for executing your code.

<img src="/img/visuals/tmux-vim-editor.jpg" width="100%" alt="tmux plus Vim editor on a dark background." class="shot rnd outl">

A text editor can be as simple as Notepad running on Windows or a more 
complicated 
[integrated development environment (IDE)](/text-editors-ides.html) with
syntax checking, integrated [test runner](/testing.html) and code highlighting. 
A couple of common IDEs for Python development are 
[PyCharm](https://www.jetbrains.com/pycharm/) and 
[VSCode](https://code.visualstudio.com/), both of which runs on any major 
[operating system](/operating-systems.html).


## Why is a development environment necessary?
Python code needs to be written, executed and tested to build
applications. The text editor provides a way to write the code. The 
interpreter allows it to be executed. Testing to see if the code does what
you want can either be done manually or by unit and functional tests. 

<div class="well see-also">While you're learning about development environments be sure to check out information on <a href="/vim.html">Vim</a> and <a href="/emacs.html">Emacs</a>.</div>


## An example development environment
Here's what I (the author of Full Stack Python, 
[Matt Makai](/about-author.html)) use to develop most of my Python 
applications. I have a Macbook Pro with Mac OS X as its base operating 
system. [Ubuntu 18.04 LTS](/operating-systems.html) is virtualized on top 
with [Parallels](https://www.parallels.com/). My code is written in 
[vim](http://www.vim.org/) and executed with the 
[Python 3.6](https://www.python.org/downloads/release/python-365/) release
via the command line. I use [virtualenv](https://virtualenv.pypa.io/en/latest/) 
to create separate Python interpreters with their own isolated
[application dependencies](/application-dependencies.html) and
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
to quickly switch between the interpreters created by virtualenv.

That's a common set up but you can certainly write great code with a much
less expensive set up or a cloud-based development environment.


## Other developers' environments
Often the best way to figure out how to get comfortable in your own
development environment is to see examples of how other experienced 
developers have set up their configurations. The following posts contain
the tools, editors and workflows that developers have taken the time to 
publicly document.

* [My Python development environment](https://gist.github.com/awesomebytes/c932b2502fab32d0c8bb)
  has a setup with [Sublime Text](/sublime-text.html), Anaconda, 
  [PyCharm](/pycharm.html) and the author's workflow for how to use
  the different editors for different purposes.

* [My Python Development Environment, 2020 Edition](https://jacobian.org/2019/nov/11/python-environment-2020/)
  explains Jacob Kaplan-Moss' (one of the original creators of the
  [Django](/django.html) web framework) local setup.

* [The definitive guide to setup my Python workspace](https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14)
  is geared towards using Python for data science but the guide remains
  useful for configuring your system for any type of Python work. There is
  some solid advice in the post about not adulterating your global Python
  installation as well as how to split out many virtual environments for
  Python 2 & 3.


## Cloud hosted dev environments
Several cloud-based development environments have popped up over the past
several years. These hosted environments can work well when you are learning
or stuck on a machine with a web browser but otherwise no administrative 
privileges to install your own software. Most of these have free tiers for 
getting started and then require payment as you scale up your application.

* [CodeAnywhere](https://codeanywhere.com/) is a cloud IDE that can be used
  in the web browser or on an iOS or Android device.

* [Cloud9](https://c9.io/) began as an independent company and is now owned 
  by Amazon as part of Amazon Web Services.

* [code.xyz](https://code.xyz/) is an online text editor built by
  [Stdlib](https://stdlib.com/) that can integrate with external 
  [web APIs](/application-programming-interfaces.html).

* [GitLab Web IDE](https://docs.gitlab.com/ee/user/project/web_ide/)
  is integrated into the GitLab web application for modifying your
  [Git](/git.html) repository files directly in your browser.


### General dev environment resources
Development environments are unique to each programmer because Python is
used for many different purposes. The following guides range from 
[web development](/web-development.html) to 
[DevOps](/devops.html) and from 
[getting started](/learning-programming.html) to [data science](/data.html).
Even though your environment requirements are unique, you should be able to 
find someone who has set up something similar to what you need. Use that
configuration as a starting point and customize it from there.

* The Python subreddit had a nice thread with developers giving the
  specifications to their Python development environments in this post on
  [What is in your Python Development Environment?](https://www.reddit.com/r/Python/comments/8n6cep/what_is_in_your_python_development_environment/).

* Real Python has an awesome, detailed post on 
  [setting up your Sublime Text 3 environment](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)
  as a full-fledged IDE.

* [How to bootstrap a Python project](https://blog.emacsos.com/bootstrap-a-python-project.html)
  covers using a virtualenv, where to store your files, 
  [which version of Python to use](/python-2-or-3.html) and adding
  [code metrics](/code-metrics.html) libraries for checking syntax.

* [Three Ways to Install Python on your Windows Computer](http://blog.yhat.com/posts/installing-python-on-windows.html)
  provides multiple avenues for Windows users to get Python on their machine
  before setting up the rest of their development environment. Unlike
  macOS and Linux, the Windows [operating system](/operating-systems.html) 
  does not include Python with its default installation.

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

* [Setting up a Python Development Environment with and without Docker](https://nickjanetakis.com/blog/setting-up-a-python-development-environment-with-and-without-docker)
  explains the reasoning behind why and when to use various tools in
  your local environment.

* [Epic Development Environment using Windows Subsystem for Linux](https://dev.to/johnwoodruff91/epic-development-environment-using-windows-subsystem-forlinux-5f0n)
  is geared towards [JavaScript](/javascript.html) developers but contains a
  slew of good advice for developers trying to configure Windows.

