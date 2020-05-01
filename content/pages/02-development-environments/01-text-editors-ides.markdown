title: Text Editors and IDEs
category: page
slug: text-editors-ides
sortorder: 0201
toc: False
sidebartitle: Text Editors & IDEs
meta: Text editors and integrated development environments (IDEs) are applications for writing Python code.


Text editors and integrated development environments (IDEs) are applications
for [writing code](/learning-programming.html). These applications are the
primary user interface for developers to create their own programs.

<img src="/img/visuals/vim-dark-bg.jpg" width="100%" alt="Vim with basic configuration options on a dark background." class="shot outl rnd">

[Vim](/vim.html) is an example of a text editor implementation that can be 
expanded into a full Python IDE using configuration files and plugins.

<div class="well see-also">Text editors and IDEs are a concept implemented by <a href="/vim.html">Vim</a>, <a href="/emacs.html">Emacs</a>, <a href="/sublime-text.html">Sublime Text</a>, <a href="/jupyter-notebook.html">Jupyter Notebook</a> and several other applications. Learn how the parts fit together in the <a href="/development-environments.html">development environments</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


## Why is a text editor or IDE necessary?
Where will you write your code if you do not have a text editor? Your
[development environment](/development-environments.html) must include
a text editor so you can enter, edit and delete characters to create
Python applications.

Preferrably your editor will have a monospace font. It will also get out
of your way, so no "smart" correction or automatic letter capitalization.
The more comfortable you become in your editor of choice the faster you
can figure out how to implement that next feature in your application or
squash that pesky bug that you just found.


## What's the difference between editors and IDEs?
IDEs contain text editors but many text editors, for example Notepad included
with Windows, do not include IDE features. Many text editors such as
Vim or Emacs have IDE features by default but then can be further customized
to add file trees, syntax highlighting, line numbers and syntax checking 
that is commonly found in full-featured IDEs.


## Open source text editors
Open source provides an embarrassment of riches when its come to stable, 
extendable text editors. Some version of these editors, such as the original
vi version of Vim, have been used for over 40 years! You can't go wrong with
using one of the editors as your development environment foundation.

The following text editor implementations can be upgraded with
configurations and plugins to become full-fledged IDEs when a developer
wants that kind of functionality.

* [Vim](/vim.html) is my editor of choice and installed by default
  on most \*nix systems.

* [Emacs](/emacs.html) is another editor often used
  on \*nix.

* [Mu](https://codewith.mu/en/) ([source code](https://codewith.mu/en/)) is an
  open source editor intended for Python beginners.

* [Atom](https://atom.io/) is an open source editor built by the 
  [GitHub](https://github.com) team.

* [Visual Studio Code](https://code.visualstudio.com/) by Microsoft provides
  [spectacular Python support](https://code.visualstudio.com/docs/python/editing).


## Python-specific IDEs
Editors built from the foundation up are not necessarily better than 
general-purpose text editors and IDEs like [Vim](/vim.html) and 
[Emacs](/emacs.html) but they are typically much easier to configure for 
gathering [code metrics](/code-metrics.html), running 
[unit tests](/unit-testing.html) and [debugging](/debugging.html).

* [PyCharm](https://www.jetbrains.com/pycharm/) is a Python-specific IDE
  built on [JetBrains](https://www.jetbrains.com/)' platform. There are
  free editions for students and open source projects.

* [Thonny](http://thonny.org/) is an 
  [open source](https://github.com/thonny/thonny) Python IDE for new 
  programmers. The tool bakes in syntax highlighting, code completion, a 
  simple debugger, a beginner-friendly shell and in situ documentation to
  assist new developers who are just starting to code.

* [Wing IDE](https://wingware.com/) is a paid development environment with
  integrated debugging and code completion.

* [PyDev](http://pydev.org/) is a Python IDE plug in for 
  [Eclipse](https://eclipse.org/).


## Proprietary (closed source) editors
There are some editors that are closed source that developers are very
happy using.

* [Sublime Text](http://www.sublimetext.com/) versions 2 and 3 (currently
  in beta) are popular text editors that can be extended with code completion,
  linting, syntax highlighting and other features using plugins. If you
  are considering using Sublime Text for Python development, check out this
  [2016 in review - likes and dislikes about Sublime Text](https://dbader.org/blog/sublime-text-for-python-development-2016-review)
  post that summarizes many of the positives and negatives of using the
  editor.

* [Komodo](http://komodoide.com/) is a cross-platform text editor and IDE
  for major languages including Python, Ruby, JavaScript, Go and more.


## Building your own text editor
One great way to learn more about how text editors work is by building your 
own, even if it turns out to be a hacked-together proof-of-concept. These
resources give walkthroughs on building an editor, or explain how existing 
editors work by digging into their source code.

* [Build your own text editor](https://viewsourcecode.org/snaptoken/kilo/)
  provides an awesome tutorial for creating a basic editor in the C
  programming language. This walkthrough is useful to break open the black
  box of how a tool you use every day as a programmer works under the covers.

* [A brief glance at how various text editors manage their textual data](https://ecc-comp.blogspot.com/2015/05/a-brief-glance-at-how-5-text-editors.html)
  is a fun dive into the source code of vi, GNU Moe, [Emacs](/emacs.html),
  Scintilla and GNOME GtkTextView/GtkTextBuffer.

* [Xi: an editor for the next 20 years](https://www.recurse.com/events/localhost-raph-levien)
  is an awesome technical talk about designing a text editor with the
  current (2018) set of tools available to a developer.

* [Building a Text Editor for a Digital-First Newsroom](https://open.nytimes.com/building-a-text-editor-for-a-digital-first-newsroom-f1cb8367fc21)
  gives some wonderful insight into the New York Times' homegrown legacy
  text editor and why they started building a new text editor named Oak
  that is customized to the newsroom's workflow.


### General text editor & IDE resources
These resources provide comparisons of various editors and give some
deeper insight into the IDE vs plain text editor debate.

* [EditorConfig](https://editorconfig.org/) 
  ([source code](https://github.com/editorconfig/)) is an open source
  tool for keeping many text editors and IDEs on the same code styles
  and configurations.

* [PyCharm vs Sublime Text](https://opensourcehacker.com/2015/05/02/pycharm-vs-sublime-text/)
  has a comparison of several features between the two editors.

* [What is the best IDE for Python](https://www.quora.com/What-is-the-best-IDE-for-Python)
  tries to answer a loaded question and gives some rationale behind
  choosing one application or another.

* [Why I Deleted My IDE; and How It Changed My Life For the Better](https://dev.to/overopshq/why-i-deleted-my-ide-and-how-it-changed-my-life-for-the-better-hli)
  contains some hyperbole but still has some solid reasoning why integrated
  environments are not necessarily for everyone depending on a developer's
  chosen workflow.

* [Text editing techniques every Front-End developer should know](https://benfrain.com/text-editing-techniques-every-front-end-developer-should-know/)
  contains tricks that experienced developers use in their editor of choice.
  The author uses [Sublime Text](/sublime-text.html) to demonstrate how
  the methods work but they can be used in just about any editor.
