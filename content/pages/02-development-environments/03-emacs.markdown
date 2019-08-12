title: Emacs
category: page
slug: emacs
sortorder: 0203
toc: False
sidebartitle: Emacs
meta: Emacs is an extensible, customizable text editor often used for coding. Read more about Emacs on Full Stack Python.


[Emacs](https://www.gnu.org/software/emacs/) 
([source code](https://savannah.gnu.org/git/?group=emacs))
is an extensible text editor 
that can be customized by writing Emacs Lisp (Elisp) code.

<a href="https://www.gnu.org/software/emacs/"><img src="/img/logos/emacs-wide.png" width="100%" alt="Emacs community logo." class="shot"></a>


### Why is Emacs a good choice for coding Python?
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
`kill-emacs-hook` runs before exiting Emacs so functions can be loaded
into that hook to perform necessary actions before the exiting completes.

<div class="well see-also">Emacs is an implementation of the <a href="/text-editors-ides.html">text editors and IDEs</a> concept. Learn how these parts fit together in the <a href="/development-environments.html">development environments</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


### Python plus Emacs resources
Emacs is programming language agnostic by design so it takes some effort
to customize the editor as a Python-specific 
[development environment](/development-environments.html). The following
resources will walk you through the setups that other developers have 
created for working with Python.

* [Emacs - the Best Python Editor?](https://realpython.com/blog/python/emacs-the-best-python-editor/)
  continues the excellent Real Python series showing how to get started
  with editors. In addition to this Emacs post, there are also posts on 
  [Vim](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) 
  and 
  [Sublime Text 3](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)
  specifically for Python development.

* Python developers often use reStructuredText (RST) to document their 
  projects. This guide on 
  [Emacs Support for ReStructuredText](http://docutils.sourceforge.net/docs/user/emacs.html)
  is handy for properly configuring your environment to work with RST files.

* [Emacs as a Python IDE](https://robots.thoughtbot.com/emacs-as-a-python-ide)
  is a video of a technical talk where the speaker sets up code completion, 
  documentation lookup and the 
  [jedi-starter](https://github.com/wernerandrew/jedi-starter) kit on his
  Emacs environment.

* [How do you create a robust Python IDE with Emacs (as the Text editor)](https://emacs.stackexchange.com/questions/9696/how-do-you-create-a-robust-python-ide-with-emacs-as-the-text-editor)
  is a quality Stack Exchange thread that offers opinions about how to best
  go about setting up Emacs for efficient Python development.

* [Tricked out emacs for python coding](http://nipy.org/nipy/devel/tools/tricked_out_emacs.html)
  is a short guide for handling ReStructuredText documents and adding 
  [Python code metrics](/code-metrics.html) tools to your Emacs environment.


### General Emacs resources
Emacs, like any powerful tool, takes significant intentional practice to
use properly. These resources provide instructions for becoming comfortable
with the editor itself rather than specific Python environment configuration
advice.

* [GNU Emacs Manual](http://www.gnu.org/software/emacs/manual/html_node/emacs/index.html)
  provides an official in-depth review for how to use Emacs.

* [Emacs is sexy!](http://emacs.sexy/) provides a whole site with installation
  instructions, cheat sheets and other materials for learning Emacs.

* [Emacs Redux](http://emacsredux.com/) is a blog with tips and tricks for
  how to use Emacs effectively.

* [Emacs Rocks](http://emacsrocks.com/) is a video tutorial series for Emacs.

* The [Absolute Beginner's Guide to Emacs](http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/)
  and
  [Emacs as a Python IDE](http://www.jesshamrick.com/2012/09/18/emacs-as-a-python-ide/)
  are a couple of awesome detailed walkthroughs by 
  [Jessica Hamrick](https://github.com/jhamrick) for setting up Emacs for 
  general development as well as Python coding.

* [Compiling and running scripts in Emacs](https://www.masteringemacs.org/article/compiling-running-scripts-emacs)
  explains one workflow option you can use with Emacs to run code from 
  within the editor rather than bouncing out to a shell.

* [What the .emacs.d?!](http://whattheemacsd.com/) provides a bunch of tiny
  optimizations for Emacs' workflow.

* The [Using Emacs Series](https://cestlaz.github.io/stories/emacs/) is
  a set of videos along with an open source
  [Git repository of the configuration](https://github.com/zamansky/using-emacs)
  for using and gaining experience with Emacs.


### Programming Emacs with Elisp
Emacs can be completely customized and rewritten by using the Emacs-specific
Lisp programming language named Emacs Lisp (Elisp). The ability to completely
modify the editor is part of what led to the old joke "a great operating 
system, lacking only a decent editor". Nevertheless, Elisp is what gives 
Emacs its text editing power despite the perception that the editor is 
overkill for working with text.

These tutorials will help you learn the Elisp language and use it to modify
Emacs for your own purposes.

* [An Introduction to Programming in Emacs Lisp](https://www.gnu.org/software/emacs/manual/html_node/eintr/index.html)
  is the "official" introduction intended for a beginner programming
  audience.

* [Emacs Lisp Guide](https://github.com/chrisdone/elisp-guide) is for 
  developers that have been using Emacs for a while and want to start
  making extensions to get more out of the editor.

* The [Emacs Wiki](https://www.emacswiki.org/emacs/LearnEmacsLisp) contains
  advice and resources for getting oriented.

* [Practical Emacs Lisp](http://ergoemacs.org/emacs/elisp.html) contains
  a bunch of useful code and focuses on examples throughout the tutorial.


### Notable Elisp Packages
[Elisp](https://www.gnu.org/software/emacs/manual/eintr.html) is the 
[LISP](https://common-lisp.net/) programming language dialect that Emacs
using for adding and customizing functionality in the editor. The following
Elisp packages are existing Elisp libraries that many developers using Emacs 
incorporate into their environment.

* [Magit](https://magit.vc/) allows the user to inspect and modify
  Git repositories from within Emacs.

* [company-mode](http://company-mode.github.io/) creates a modular in-buffer
  completion framework.

* [Flycheck](http://www.flycheck.org/en/latest/) provides syntax checking.

* [anaconda-mode](https://github.com/proofit404/anaconda-mode/) is specific
  to Python development and allows code navigation, documentation lookup 
  and code completion.

* [web-mode.el](http://web-mode.org/) is a package for editing web templates
  like [Jinja](/jinja2.html). Many 
  [Python template engines](/template-engines.html) are supported 
  including [Django templates](/django-templates.html), [Mako](/mako.html)
  and [Cheetah](https://pythonhosted.org/Cheetah/) as well as 
  [JavaScript](/javascript.html) front-end frameworks.


### Popular user configurations
Numerous custom Emacs user configurations exist that bundle together custom
Elisp packages and libraries to handle creating a powerful integrated 
development environment. I recommend trying to configure Emacs yourself 
before you dive into any of these configurations so it is easier to
learn base Emacs rather than get distracted by the customizations.

* [Prelude](https://github.com/bbatsov/prelude) is an enhanced Emacs
  version 24 distribution.

* [A reasonable Emacs config](https://github.com/purcell/emacs.d) shows
  a batteries-includes Emacs configuration bundle.

* [Emacs settings](https://github.com/magnars/.emacs.d) is a repository of
  configurations used in the Emacs Rocks screencasts.

* [Spacemacs](https://github.com/syl20bnr/spacemacs) mashes together Emacs'
  extensibility and Vim's ergonomic text editing features.

