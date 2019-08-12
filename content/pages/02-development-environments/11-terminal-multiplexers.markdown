title: Terminal Multiplexers
category: page
slug: terminal-multiplexers
sortorder: 0211
toc: False
sidebartitle: Terminal Multiplexers
meta: Terminal multiplexers can run several shells in a single terminal as well as attach, detach and move sessions from one computer to another.


A terminal multiplexer provides separation between where a [shell](/shells.html)
is running and where the shell is accessed. Each shell can be running on a 
different computer, but to the developer it does not matter where each 
shell is being executed.

For example, a developer could have many shells running within a 
terminal, like the following screenshot. 

<img src="/img/visuals/terminal-multiplexer-tmux.jpg" width="100%" alt="tmux terminal multiplexer with many panes." class="shot"></a>

The above terminal window is using the tmux terminal multiplexer implementation
with two windows and three panes. 


## Why are terminal multiplexers awesome?
Developers gain greater control over the usage of their shells by working
with a terminal multiplexer.

Shells are typically executed locally on a computer but terminal multiplexers 
allow one or more virtual shells to be run within a single terminal. Shells 
can also be left running within the multiplexer and attached to again from a 
different machine.

Terminal multiplexers are used by developers to run many virtual shells 
within a single terminal. These shells can be run via a mix of local, 
remote, containerized and virtualized resources. The shells can also
be persisted and moved while running from one computer to another.


### Terminal multiplexer implementations
Many terminal multiplexer implementations exist, including:

* [tmux](/tmux.html)

* [screen](/screen.html)

* byobu

* [Pymux](https://pypi.org/project/pymux)
  ([source code](https://github.com/jonathanslenders/pymux)) is a
  terminal multiplexer implementation 
  written in Python that clones the functionality of [tmux](/tmux.html).
  Like tmux and [Screen](/screen.html), Pymux makes it easier for
  programmers to use many shells within a single terminal window during
  development.


### Terminal multiplexer resources
* [Terminal multiplexers](http://linuxcommand.org/lc3_adv_termmux.php)
  provides a wonderful overview of the subject, including the history
  of various implementations and why you would want to use one for
  development.

* [Terminal multiplexer commands](http://hyperpolyglot.org/multiplexers)
  is a comparison of equivalent key command in the two most popular 
  implementations, tmux and screen.

* [Byobu vs. GNU Screen vs. tmux — usefulness and transferability of skills](https://superuser.com/questions/423310/byobu-vs-gnu-screen-vs-tmux-usefulness-and-transferability-of-skills)
  gives solid answers on this (now closed) question of the usefulness of
  the major terminal multiplexer implementations.

* [Pymux discussion on Hacker News](https://news.ycombinator.com/item?id=10831149)

