title: Sublime Text
category: page
slug: sublime-text
sortorder: 0204
toc: False
sidebartitle: Sublime Text
meta: Sublime Text is a commonly-used text editor with development extensions for the Python programming language.


[Sublime Text](https://www.sublimetext.com/) is a commonly-used text editor 
used to write Python code. Sublime Text's slick user interface along with its 
numerous extensions for syntax highlighting, source file finding and analyzing 
[code metrics](/code-metrics.html) make the editor more accessible to new
programmers than some other applications like [Vim](/vim.html) and 
[Emacs](/emacs.html).

<a href="https://www.sublimetext.com/" style="border:none"><img src="/img/logos/sublime-text.jpg" width="100%" alt="Sublime Text logo." class="shot outl rnd"></a>

<div class="well see-also">Sublime Text is an implementation of the <a href="/text-editors-ides.html">text editors and IDEs</a> concept. Learn how these parts fit together in the <a href="/development-environments.html">development environments</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


## What makes Sublime Text awesome?
Sublime Text is often the first editor that newer programmers pick up because
it works on all operating systems and it is far more approachable than 
[Emacs](/emacs.html), [Vim](/vim.html) or even [PyCharm](/pycharm.html).

It is easy to get started in Sublime because the menus and options are 
accessible by using a mouse. There are no different modes to learn like 
Vim's normal and insert modes. The keyboard shortcuts can be learned over
time rather than all at once in the case of Vim or Emacs. 

Sublime Text works well for beginners as soon as they install it and then
can be extended with many of the features provided by an IDE like 
[PyCharm](/pycharm.html) as a developer's skill level ramps up.

An additional bonus of using Sublime Text as a Python developer is that
[plugins are written in Python](http://www.sublimetext.com/docs/plugin-basics).
Python developers can extend Sublime Text with their own programming language
rather than learn a new language like Emacs' Elisp or Vim's Vimscript.


## Why use any other editor if Sublime is so great?
Picking a [text editor or IDE](/text-editors-ides.html) to use tends to 
be a weirdly personal decision for each developer. Yet it makes sense when
you realize that you are going to spend hours upon hours every day in your
chosen environment so why not make sure it is one that is enjoyable and
highly productive? 

For some folks they prefer [Vim](/vim.html)'s keyboard-driven style, 
[PyCharm](/pycharm.html)'s Swiss Army Knife set of Python tools or one of 
the many other editors with its own strengths and weaknesses.

The only "best" editor choice is to pick one that works really well for you
and stick to it. Master your tool so it gets out of your way and enables
as much time in 
[programming flow](https://en.wikipedia.org/wiki/Flow_(psychology)) as 
possible.


### Python-specific Sublime Text resources
There are many Python-specific Sublime Text tutorials and resources because
the editor is so frequently used to create Python applications. The following
links should get your editor customized with linters, 
[code metrics](/code-metrics.html), syntax checking and many other 
[integrated development environment](/text-editors-ides.html) features.

* [Setting Up Sublime Text 3 for Full Stack Python Development](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)
  is a spectacular tutorial that covers installing Sublime Text and 
  configuring a multitude of helpful Python programming plugins.

* [Sublime Text 3 Heaven](https://www.kennethreitz.org/essays/sublime-text-3-heaven)
  is a quick overview of the extensions, packages and bonus toys that
  one developer uses for his own Sublime Text development setup.

* [Sublime Tutor](https://sublimetutor.com/) is an interactive in-editor 
  keyboard shortcuts tutorial that plugs into Sublime so you can learn and
  become more productive as you use the editor.

* [Using Generators for Fun and Profit - Utility for developers](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=17671)
  is not about setting up your Sublime Text environment but instead how to
  create your own plugins using Python. The tutorial is written by the
  author of a Sublime Text plugin who uses generators
  to implement features with Sublime's API.

* [Turning Sublime Text Into a Lightweight Python IDE](https://cewing.github.io/training.codefellows/assignments/day01/sublime_as_ide.html)
  shows the basic settings and configuration specific to using Sublime with
  Python as more than just a text editor.

* [Setting up Sublime Text 3 for Python Type Checking](https://medium.com/@erika_dike/setting-up-sublime-text-3-for-python-type-checking-85af5ce1a1ee)
  shows one way of setting up support for Python 3.6 static type checking in 
  Sublime.

* [Three steps to lint Python 3.6 in Sublime Text](https://janikarhunen.fi/three-steps-to-lint-python-3-6-in-sublime-text.html)
  walks through setting up [Flake8](http://flake8.pycqa.org/en/latest/) to
  enforce code style guidelines and show you the errors and warnings in 
  Sublime as you are working.

* [Text editing techniques every front-end developer should know](https://benfrain.com/text-editing-techniques-every-front-end-developer-should-know/)
  gives examples in Sublime Text of time-saving text manipulation you may 
  not have known existed such as line bubbling, ragged line selection, 
  AceJump and transpose. While the techniques can be used in most editors
  the provided video clips show how to perform each of these shortcuts in
  Sublime.


### General Sublime Text resources
Sublime Text can be used for much more than Python development and there are
many useful tutorials that are not targeted at a specific programming language
which are still useful.

* [Super charge your Sublime Text 3 to increase your productivity](https://hackernoon.com/super-charge-your-sublime-text-3-to-increase-your-productivity-5d02c2c1b356)
  provides many shortcuts and tricks for using the editor.

* [Disassembling Sublime Text](http://thume.ca/2016/12/03/disassembling-sublime-text/) uses a binary disassembler to dive into the reverse engineered 
  source code of Sublime Text because it is not open source software.

* [Sync your sublime text 3 configurations safely and easy](https://medium.com/@arshamshirvani/sync-your-sublime-text-3-configurations-safely-and-easy-b493021c80da)
  explains how to mitigate configuration conflicts that can arise when trying
  to use copied files from one computer to another.

* [7 shortcuts of a highly effective Sublime Text user](https://kirankoduru.github.io/python/sublime-text-ninja.html)
  shows keyboard shortcuts for opening any file, going to any specific
  block of text, handling multiple cursors and more.


### Sublime Plugin resources
Sublime Text plugins are written in Python which makes it convenient for 
our ecosystem to customize the editor. The following resources provide
information on writing your own plugins as well as great community plugins
you will want to take a look at adding to your installation.

* Sublime's documentation covers 
  [plugin basics](http://www.sublimetext.com/docs/plugin-basics), the
  [API for plugins](http://www.sublimetext.com/docs/api-reference) and
  gives a 
  ["Hello, world!"-level example](http://www.sublimetext.com/docs/plugin-examples)
  that you can extend.

* [Sublime Text plugin development basics](http://engineering.vinted.com/2016/06/27/how-to-write-sublime-plugin/)
  has some good advice and further resources.

* [The 25 Best Sublime Text Plugins for Front End Developers](https://www.shopify.com/partners/blog/sublime-text-plugins-2018)
  is not specific to Python development but there is a bunch of overlap
  between plugins useful for general front-end development and any Python
  [web development](/web-development.html) project.

* [5 Awesome Sublime Plugins you Won’t Find in Top Plugin Posts](https://css-tricks.com/5-awesome-sublime-plugins-wont-find-top-plugin-posts/)
  covers some lesser-known plugins and how you can find your own via 
  [Package Control's trending plugins section](https://packagecontrol.io/browse/trending).

