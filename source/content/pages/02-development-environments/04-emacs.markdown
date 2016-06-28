title: Emacs
category: page
slug: emacs
sortorder: 0204
toc: False
sidebartitle: Emacs
meta: Emacs is an extensible, customizable text editor often used for coding. Read more about Emacs on Full Stack Python.


# Emacs
Emacs is an extensible text editor that can be customized by writing Lisp
code.


## Why is Emacs a good choice for Python coding?
Emacs is designed to be customized via the built-in Lisp interpreter and
package manager. The package manager, named package.el, has menus for
handling installation. The largest Lisp Package Archive is 
[Melpa](http://melpa.org), which provides automatic updates from upstream
sources.

Macros are useful for performing repetitive actions in Emacs. A macro
is just a recording of a previous set of keystrokes that can be replayed
to perform future actions.

Hooks, which are Lisp variables that hold lists of functions to call,
provide an extension mechanism for Emacs. For example,
``kill-emacs-hook`` runs before exiting Emacs so functions can be loaded
into that hook to perform necessary actions before the exiting completes.

<div class="well see-also">While you're reading about coding Python in Emacs be sure to also learn about which <a href="/web-frameworks.html">web frameworks</a> to use as well as <a href="/deployment.html">how to deploy an application</a>.</div>


## General Emacs resources
* [GNU Emacs Manual](http://www.gnu.org/software/emacs/manual/html_node/emacs/index.html)
  provides an official in-depth review for how to use Emacs.

* [Emacs as a Python IDE](http://www.jesshamrick.com/2012/09/18/emacs-as-a-python-ide/)
  is a detailed walkthrough of setting up Emacs for Python development.

* [Emacs - the Best Python Editor?](https://realpython.com/blog/python/emacs-the-best-python-editor/)
  continues the excellent Real Python series showing how to get started
  with editors. In addition to this Emacs post, there are also posts on 
  [Vim](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) 
  and 
  [Sublime Text 3](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)
  specifically for Python development.

* [Emacs Redux](http://emacsredux.com/) is a blog with tips and tricks for
  how to use Emacs effectively.

* [Emacs Rocks](http://emacsrocks.com/) is a video tutorial series for Emacs.

* [What the .emacs.d?!](http://whattheemacsd.com/) provides a bunch of tiny
  optimizations for Emacs' workflow.


## Notable Elisp Packages
* [Magit](https://magit.vc/) allows the user to inspect and modify
  Git repositories from within Emacs.

* [company-mode](http://company-mode.github.io/) creates a modular in-buffer
  completion framework.

* [Flycheck](http://flycheck.github.io/) provides syntax checking.

* [anaconda-mode](https://github.com/proofit404/anaconda-mode/) is specific
  to Python development and allows code navigation, documentation lookup 
  and code completion. The [jedi](http://jedi.jedidjah.ch/en/latest/) library 
  is used under the hood.

* [Tern](http://ternjs.net/) is a stand-alone code-analysis engine for
  JavaScript. It can be integrated within a Django project
  via the [tern-django](https://github.com/proofit404/tern-django) package.


## Popular user configurations
* [Prelude](https://github.com/bbatsov/prelude) is an enhanced Emacs
  version 24 distribution.

* [A reasonable Emacs config](https://github.com/purcell/emacs.d) shows
  a batteries-includes Emacs configuration bundle.

* [Emacs settings](https://github.com/magnars/.emacs.d) is a repository of
  configurations used in the Emacs Rocks screencasts.

* [Spacemacs](https://github.com/syl20bnr/spacemacs) mashes together Emacs'
  extensibility and Vim's ergonomic text editing features.

