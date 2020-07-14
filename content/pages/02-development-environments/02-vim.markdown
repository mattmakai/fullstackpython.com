title: Vim
category: page
slug: vim
sortorder: 0202
toc: False
sidebartitle: Vim
meta: Vim is a text editor with powerful string manipulation capabilities. Find out more about Vim on Full Stack Python.


[Vim](https://www.vim.org/) ([source code](https://github.com/vim/vim)), 
short for Vi IMproved, is a configurable text editor often used as
a Python development environment. Vim proponents commonly cite the numerous
plugins, Vimscript and logical command language as major Vim strengths.

<a href="https://www.vim.org/" style="border:none"><img src="/img/logos/vim-the-editor.jpg" width="100%" alt="Vim logo." class="shot rnd outl"></a>


## Why is Vim a good Python development environment?
Vim's philosophy is that developers are more productive when they avoid
taking their hands off the keyboard. Code should flow naturally from the
developer's thoughts through the keyboard and onto the screen. Using a mouse
or other peripheral is a detriment to the rate at which a developer's
thoughts become code. This "efficiency by keyboard" 
[keeps Vim as one of the most popular text editors](https://pragmaticpineapple.com/how-did-vim-become-so-popular/)
despite having been around for decades. Few programming tools have that kind 
of staying power.

Vim has a logical, structured command language. When a beginner is learning
the editor she may feel like it is impossible to understand all the key
commands. However, the commands stack together in a logical way so that over
time the editor becomes predictable.

<div class="well see-also">Vim is an implementation of the <a href="/text-editors-ides.html">text editors and IDEs</a> concept. Learn how these parts fit together in the <a href="/development-environments.html">development environments</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


## Configuring Vim with a Vimrc file
The Vimrc file is used to configure the Vim editor. A Vimrc file can range
from nothing in it to very complicated with hundreds or thousands of lines
of configuration commands.

Here's a short, commented example .vimrc file I use for Python development
to get a feel for some of the configuration statements:

```
" enable syntax highlighting
syntax enable

" show line numbers
set number

" set tabs to have 4 spaces
set ts=4

" indent when moving to the next line while writing code
set autoindent

" expand tabs into spaces
set expandtab

" when using the >> or << commands, shift lines by 4 spaces
set shiftwidth=4

" show a visual line under the cursor's current line
set cursorline

" show the matching part of the pair for [] {} and ()
set showmatch

" enable all Python syntax highlighting features
let python_highlight_all = 1
```

Here is how these configuration options look with a dark background on
Mac OS X while editing the markdown for this webpage (how meta!).

<img src="/img/visuals/vim-dark-bg.jpg" width="100%" alt="Vim with basic configuration options on a dark background." class="shot rnd outl">

Take a look at another example using these configuration options, this time
with a light background and editing Python code from my
[Choose Your Own Adventures Presentations](https://github.com/mattmakai/choose-your-own-adventure-presentations)
project.

<img src="/img/visuals/vim-white-bg.png" width="100%" alt="Vim with basic configuration options on a white background." class="shot rnd outl">

The Vimrc file lives under the home directory of the user account running
Vim. For example, when my user account is 'matt', on Mac OS X my Vimrc
file is found at ``/Users/matt/.vimrc``. On Ubuntu Linux my .vimrc file
can be found within the ``/home/matt/`` directory.

If a Vimrc file does not already exist, just create it within the user's
home directory and it will be picked up by Vim the next time you open the
editor.


### Vim tutorials
Vim has a reputation for a difficult learning curve, but it's much easier
to get started with these tutorials.

* [Learn Vim Progressively](http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)
  is a wonderful tutorial that follows the path I took when learning Vim:
  learn just enough to survive with it as your day-to-day editor then begin
  adding more advanced commands on top.

* [A vim Tutorial and Primer](https://danielmiessler.com/study/vim/) is an
  incredibly deep study in how to go from beginner to knowledgeable in Vim.

* [Why Atom Can't Replace Vim](https://medium.com/@mkozlows/why-atom-cant-replace-vim-433852f4b4d1)
  discusses one of Vim's core principles: command composability. Vim has 
  a language where simple commands are combined to execute more advanced 
  operations. For example, in command mode,`$` moves to the end of a line.
  When `$` is preceded by `d` then everything to the end of the line is
  deleted. Over time the simple commands become intuitive and the 
  combinations become more powerful than having distinct commands such as
  a drop-down menu with a specific option to delete all text until the end
  of the line.

* [Vim as a Language](http://benmccormick.org/2014/07/02/learning-vim-in-2014-vim-as-language/)
  explains the language syntax and how you can build up over time to master
  the editor.

* [How to install and use Vim on a cloud server](https://www.digitalocean.com/community/tutorials/installing-and-using-the-vim-text-editor-on-a-cloud-server)
  along with [How to use Vim for advanced editing of code on a VPS](https://www.digitalocean.com/community/tutorials/how-to-use-vim-for-advanced-editing-of-plain-text-or-code-on-a-vps--2)
  are two detailed Digital Ocean guides for getting up and running with Vim,
  regardless of whether you're using it locally or on a cloud server.

* [PacVim: a commandline game to learn Vim commands](https://www.ostechnix.com/pacvim-a-cli-game-to-learn-vim-commands/)
  takes the PacMan theme and teaches you how to use Vim by forcing you
  to move around and use Vim commands while gaming.

* [Ten years of Vim](https://matthias-endler.de/2018/ten-years-of-vim/)
  provides an insightful retrospective on one experienced developer's
  journey with using Vim as a primary text editor and development
  environment. I found the part about going overboard with plugins before
  switching back to a simpler configuration fascinating because it is
  the same path I've found myself taking as I approach my own ten year
  mark with Vim.

* [At least one Vim trick you might not know about](https://www.hillelwayne.com/post/intermediate-vim/)
  is a collection of non-obvious keyboard shortcuts, many of which are 
  infrequently used but still useful.

* [Vim Adventures](http://vim-adventures.com/) is a cute, fun browser-based
  game that helps you learn Vim commands by playing through the adventure.

* [Things About Vim I Wish I Knew Earlier](https://blog.petrzemek.net/2016/04/06/things-about-vim-i-wish-i-knew-earlier/)
  explores the lessons one developer learned while exclusively using Vim
  for several years. The author includes using relative instead of absolute
  line numbering, setting numerous configuration options and fuzzy finding
  to quickly open files in other directories rather than expanding the 
  whole path.

* [Seven habits of effective text editing](http://moolenaar.net/habits.html)
  explains moving around efficiently, fixing errors quickly and forming good
  habits.


### Vimrc resources
These are a few resources for learning how to structure a `.vimrc` file. I
recommend adding configuration options one at a time to test them
individually instead of going whole hog with a Vimrc you are unfamiliar with.

* [Vim and Python](https://justin.abrah.ms/vim/vim_and_python.html) shows
  and explains many Python-specific .vimrc options.

* [Vim as a Python IDE](http://liuchengxu.org/posts/use-vim-as-a-python-ide/)
  shows a slew of plugins and configuration options for coding with Python
  in Vim.

* This
  [repository's folder with Vimrc files](https://github.com/amix/vimrc/tree/master/vimrcs)
  has example configurations that are well commented and easy to learn from.

* For people who are having trouble getting started with Vim, check out this
  blog post on the
  [two simple steps that helped this author learn Vim](http://adamdelong.com/two-simple-steps-helped-me-learn-vim/).


### Vim installation guides
These installation guides will help you get Vim up and running on Mac OS X,
Linux and Windows.

* [Upgrading Vim on OS X](http://www.prioritized.net/blog/upgrading-vim-on-os-x)
  explains why to upgrade from Vim 7.2 to 7.3+ and how to do it using
  [Homebrew](http://brew.sh/).

* The easiest way to install Vim on Windows 7+ is to download and run the
  [gvim74.exe](http://www.vim.org/download.php#pc) file.

* On Linux make sure to install the
  [vim package](https://launchpad.net/ubuntu/+source/vim) with
  ``sudo apt-get install vim``.

* If you're using PyCharm as your IDE you won't need to install Vim as a
  separate text editor - instead use the
  [IdeaVim](https://plugins.jetbrains.com/plugin/164) PyCharm plugin to get
  Vim keybindings, visual/insert mode, configuration with ~/.ideavimrc and
  other Vim emulation features.


### Using Vim as a Python IDE
Once you get comfortable with Vim as an editor, there are several
configuration options and plugins you can use to enhance your Python
productivity. These are the resources and tutorials to read when you're
ready to take that step.

* [VIM and Python - a Match Made in Heaven](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) details how to set up a powerful VIM environment geared towards wrangling Python day in and day out.

* The [python-mode](https://github.com/klen/python-mode) project is a Vim
  plugin with syntax highlighting, breakpoints, PEP8 linting, code completion
  and many other features you'd expect from an integrated development
  environment.

* [Vim as Your IDE](http://haridas.in/vim-as-your-ide.html) discusses how to
  set up Vim for greater productivity once you learn the initial Vim language
  for using the editor.

* [Setting up Vim for Python](http://stackoverflow.com/questions/9172802/setting-up-vim-for-python)
  has a well written answer on Stack Overflow for getting started with Vim.

* If you're writing your documentation in Markdown using Vim, be sure to
  read this
  [insightful post on a Vim setup for Markdown](http://www.swamphogg.com/2015/vim-setup/).


### Vim Plugin resources
* [5 Essential VIM Plugins That Greatly Increase my Productivity](http://joelhooks.com/blog/2013/04/23/5-essential-vim-plugins/)
  covers the author's experience with the Vundle, NERDTree, ctrlp, Syntastic
  and EasyMotion Vim plugins.

* [Getting more from Vim with plugins](http://benmccormick.org/2014/07/21/learning-vim-in-2014-getting-more-from-vim-with-plugins/)
  provides a list of plugins with a description for each one on its
  usefulness. The comments at the bottom are also interesting as people have
  suggested alternatives to some of the plugins mentioned in the post.

* [Powerline](https://github.com/powerline/powerline) is a popular statusline
  plugin for Vim that works with both Python 2 and 3.

* [VimAwesome](https://vimawesome.com/) is a directory of Vim plugins sourced 
  from Vim.org, GitHub and user submissions.

* [Command-T](https://github.com/wincent/command-t) is a Vim plugin for
  fast fuzzy searching files.

* [YouCompleteMe](http://ycm-core.github.io/YouCompleteMe/)
  ([source code](https://github.com/ycm-core/YouCompleteMe)) is a
  code-completion engine and plugin that works for Python.


### Vim Plugin Managers
If you use many Vim plugins together it is really handy to have a plugin
managers to sort out all of the dependencies. The following plugin managers
are the most commonly-used ones in the Vim ecosystem.

* [Vundle](https://github.com/gmarik/Vundle.vim) comes highly recommended
  as a plugin manager for Vim.

* [Pathogen](https://github.com/tpope/vim-pathogen) is a widely used
  plugin manager.

* [Vim-plug](https://github.com/junegunn/vim-plug) bills itself as a
  minimalistic Vim plugin manager.


### Niche tutorials
After you have been using Vim for awhile there will be features you bump
into without realizing they were ever there. The following tutorials show
how to use some specific niche features. You may already know about these
if you have been using Vim for awhile but everyone's learning path is 
different so it's useful to do a quick scan to make sure you are not missing
anything.

* [Vim’s absolute, relative and hybrid line numbers](https://jeffkreeftmeijer.com/vim-number/)
  shows how to change the line numbering scheme. There was a period of 
  time I used relative line numbers although I eventually switched back
  to absolute numbers. The usefulness of these schemes is often dependent
  on what language you are working in.

* [A simpler Vim statusline](https://www.blaenkdenum.com/posts/a-simpler-vim-statusline/)
  explains how to customize your bottom screen statusline *without* using
  plugins such as [vim-powerline](https://github.com/powerline/powerline) 
  or [vim-airline](https://github.com/vim-airline/vim-airline).

* The [vim-clutch](https://github.com/alevchuk/vim-clutch) is a really cool
  project and walkthrough that shows how you can create a foot pedal to
  switch between Normal and Insert modes instead of using the typical ESC
  key (or a remapped key).

* [How I'm able to take notes in mathematics lectures using LaTeX and Vim](https://castel.dev/post/lecture-notes-1/)
  explains how the author is able to keep up with mathematics
  lectures by using Vim and LaTeX which produces gorgeous notes
  that can be used to study.
