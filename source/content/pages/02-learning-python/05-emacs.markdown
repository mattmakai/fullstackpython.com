title: Emacs
category: page
slug: emacs
sort-order: 0205
meta: GNU Emacs is an extensible, customizable text editor—and more.

# Emacs
Emacs is the extensible, customizable, self-documenting real-time
display editor.

## Why is Emacs matters?
Emacs is powerful text editor with unlimited flexibility.  Emacs
customized and mostly written in Emacs Lisp.  Your configuration is
the code as any other emacs package.  There are builtin Emacs Lisp
package manager named package.el with interactive menu for managing
your package installation.  [Melpa](http://melpa.org) is the biggest
Emacs Lisp Package Archive with automatic updates from upstream
source.

Emacs support interactive customization interface.  Call customize
command to see section hierarchy with options grouped by packages.
All customizations saved in your config file with proper comments.

When you need to do a lot of repeated actions you has an option to
capture a macro, repeat it any times and even save it directly to your
configuration file.  You can automate Emacs without writing Emacs Lisp
code at all!

The last by not least thing I want to mention here is a hooks.  Hooks
are events lives in Emacs all time you do something.  You can add
custom handlers for each event in different manners.  You can pretty
print you sources before you save a file.  You can turn on spell
checking when open text file.  You can pop up tray notification when
you get incoming jabber message :)

I hope this information is sufficient to interest you to try this
great text editor.  Links bellow contains manuals to start with Emacs,
advanced configurations with valuable effort to make you more
productive and list of packages most interested for python developers.

## General Emacs resources

* [GNU Emacs Manual](http://www.gnu.org/software/emacs/manual/html_node/emacs/index.html)

* [Emacs Redux](http://emacsredux.com/) Return to the Essence of Text
  Editing

* [Emacs Rocks](http://emacsrocks.com/) Video series

* [What The Emacs.d](http://whattheemacsd.com/) Tons of tiny
  optimizations for your workflow.

## Notable Elisp Packages
* With [Magit](http://magit.github.io/), you can inspect and modify
  your Git repositories with Emacs.

* [company-mode](http://company-mode.github.io/) Modular in-buffer
  completion framework for Emacs.

* [Flycheck](http://flycheck.github.io/) Syntax checking for GNU Emacs

* [anaconda-mode](https://github.com/proofit404/anaconda-mode/) Code
  navigation, documentation lookup and completion for Python.  It use
  awesome [jedi](http://jedi.jedidjah.ch/en/latest/) library under the
  hood.

* [Tern](http://ternjs.net/)is a stand-alone code-analysis engine for
  JavaScript. It can be simple integrated within your django project
  via [tern-django](https://github.com/proofit404/tern-django) package.

## Popular user configurations
* [Prelude](https://github.com/bbatsov/prelude) is an enhanced Emacs
  24 distribution that should make your experience with Emacs both
  more pleasant and more powerful.

* [A reasonable Emacs config](https://github.com/purcell/emacs.d) An
  Emacs configuration bundle with batteries included

* [Emacs settings](https://github.com/magnars/.emacs.d) used in the
  Emacs Rocks screencasts.

* [Spacemacs](https://github.com/syl20bnr/spacemacs) Emacs advanced
  Kit focused on Evil: The best editor is neither Emacs nor Vim, it's
  Emacs *and* Vim!
