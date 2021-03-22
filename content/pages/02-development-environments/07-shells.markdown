title: Shells
category: page
slug: shells
sortorder: 0207
toc: False
sidebartitle: Shells
meta: A shell is a computer user interface and often refers to a text-only or primarily text command line terminal.


Shells are computer user interfaces that typically refer to a text-only or 
primarily text-based command prompt.

<img src="/img/visuals/terminal-shell.png" width="100%" alt="My macOS terminal window showing the bash shell with an active virtualenv." class="shot outl">

The above screenshot shows the bash shell with an active Python virtual 
environment named `fullstackpython` within the macOS Terminal application.


### Shell resources
* [cmd](https://docs.python.org/3/library/cmd.html) is the Pythonic
  standard library module that can be used for building your own shells.
  The [Python CmdModule wiki page](https://wiki.python.org/moin/CmdModule)
  has a great overview of the module and its capabilities.

* [Give your Python program a shell with the cmd module](https://coderwall.com/p/w78iva/give-your-python-program-a-shell-with-the-cmd-module)
  shows a short code example of how to use cmd to build a simple shell.
 
* [Super Charge Your Shell For Python Development](http://avilpage.com/2017/03/super-charge-your-shell-for-python-development.html)
  covers aliases, environment variables via 
  [Autoenv](https://github.com/kennethreitz/autoenv) and some basic
  shell commands often used during development.

* [Terminal latency](https://danluu.com/term-latency/) quantifies the impact
  of lag in your keystrokes appearing on the screen. It's a fascinating look 
  at how a small difference of tens of milliseconds causes some shells and 
  editors to feel slow while others are snappy.

* [Why Create a New Unix Shell?](http://www.oilshell.org/blog/2021/01/why-a-new-shell.html)
  is a post by the creator of [Oil shell](http://www.oilshell.org/) that
  goes into the rationale for building a new shell even though so many others
  such as Bash, zsh, PowerShell and KornShell already exist.

* [explainshell](https://explainshell.com/) 
  ([source code](https://github.com/idank/explainshell)) is a wonderful
  little tool that shows how input and arguments in the shell break
  down and are interpreted by commands. The data is pulled from the 
  [Ubuntu](/ubuntu.html) `man` pages.

* [Shell productivity tips and tricks](https://blog.balthazar-rouberol.com/shell-productivity-tips-and-tricks.html)
  covers how to increase your effectiveness on the shell across topics such as
  navigating history, autocompletion, and pattern matching.
