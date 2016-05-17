title: Vim
category: page
slug: vim
sortorder: 0203
toc: False
sidebartitle: Vim
meta: Vim is a text editor with powerful string manipulation capabilities. Find out more about Vim on Full Stack Python.


# Vim
Vim, short for Vi IMproved, is a configurable text editor often used as
a Python development environment. Vim proponents commonly cite the numerous
plugins, Vimscript and logical command language as major Vim strengths.


## Why is Vim a good Python development environment?
Vim's philosophy is that developers are more productive when they avoid
taking their hands off the keyboard. Code should flow naturally from the
developer's thoughts through the keyboard and onto the screen. Using a mouse
or other peripheral is a detriment to the rate at which a developer's
thoughts become code.

Vim has a logical, structured command language. When a beginner is learning
the editor she may feel like it is impossible to understand all the key
commands. However, the commands stack together in a logical way so that over
time the editor becomes predictable.

<div class="well see-also">If you're interested in Vim you'll also want to read about <a href="/development-environments.html">development environments for coding</a> and learn <a href="/why-use-python.html">what makes Python a great programming language</a>.</div>


## Configuring Vim with a Vimrc file
The Vimrc file is used to configure the Vim editor. A Vimrc file can range
from nothing in it to very complicated with hundreds or thousands of lines
of configuration commands.

Here's a short, commented example .vimrc file I use for Python development
to get a feel for some of the configuration statements:

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


Here is how these configuration options look with a dark background on
Mac OS X while editing the markdown for this webpage (how meta!).

<img src="/img/vim-dark-bg.jpg" width="100%" alt="Vim with basic configuration options on a dark background." class="technical-diagram" style="border-radius: 5px;">

Take a look at another example using these configuration options, this time
with a light background and editing Python code from my
[Choose Your Own Adventures Presentations](https://github.com/makaimc/choose-your-own-adventure-presentations)
project.

<img src="/img/vim-white-bg.png" width="100%" alt="Vim with basic configuration options on a white background." class="technical-diagram" style="border-radius: 5px; border: 1px solid #999;">



The Vimrc file lives under the home directory of the user account running
Vim. For example, when my user account is 'matt', on Mac OS X my Vimrc
file is found at ``/Users/matt/.vimrc``. On Ubuntu Linux my .vimrc file
can be found within the ``/home/matt/`` directory.

If a Vimrc file does not already exist, just create it within the user's
home directory and it will be picked up by Vim the next time you open the
editor.


## Vim tutorials
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

* [Vim Adventures](http://vim-adventures.com/) is a cute, fun browser-based
  game that helps you learn Vim commands by playing through the adventure.

* In [Vim: revisited](http://mislav.uniqpath.com/2011/12/vim-revisited/) the
  author explains his on-again off-again relationship with using Vim. He then
  shows how he configures and uses the editor so it sticks as his primary
  code editing tool.


## Vimrc resources
These are a few resources for learning how to structure a `.vimrc` file. I
recommend adding configuration options one at a time to test them
individually instead of going whole hog with a Vimrc you are unfamiliar with.

* [A Good Vimrc](http://dougblack.io/words/a-good-vimrc.html) is a fantastic,
  detailed overview and opinionated guide to configuring Vim. Highly
  recommended for new and experienced Vim users.

* [Vim and Python](https://justin.abrah.ms/vim/vim_and_python.html) shows
  and explains many Python-specific .vimrc options.

* This
  [repository's folder with Vimrc files](https://github.com/amix/vimrc/tree/master/vimrcs)
  has example configurations that are well commented and easy to learn from.

* For people who are having trouble getting started with Vim, check out this
  blog post on the
  [two simple steps that helped this author learn Vim](http://adamdelong.com/two-simple-steps-helped-me-learn-vim/).


## Vim installation guides
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


## Using Vim as a Python IDE
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

* [Vim as a Python IDE](http://unlogic.co.uk/2013/02/08/vim-as-a-python-ide/)
  goes through the steps necessary to make Vim into a more comfortable
  environment for Python development.

* [Setting up Vim for Python](http://stackoverflow.com/questions/9172802/setting-up-vim-for-python)
  has a well written answer on Stack Overflow for getting started with Vim.

* If you're writing your documentation in Markdown using Vim, be sure to
  read this
  [insightful post on a Vim setup for Markdown](http://www.swamphogg.com/2015/vim-setup/).


## Vim Plugin Managers
* [Vundle](https://github.com/gmarik/Vundle.vim) comes highly recommended
  as a plugin manager for Vim.

* [Pathogen](https://github.com/tpope/vim-pathogen) is a widely used
  used plugin manager.

* [Vim-plug](https://github.com/junegunn/vim-plug) bills itself as a
  minimalistic Vim plugin manager.


## Vim Plugin resources
* [5 Essential VIM Plugins That Greatly Increase my Productivity](http://joelhooks.com/blog/2013/04/23/5-essential-vim-plugins/)
  covers the author's experience with the Vundle, NERDTree, ctrlp, Syntastic
  and EasyMotion Vim plugins.

* [Getting more from Vim with plugins](http://benmccormick.org/2014/07/21/learning-vim-in-2014-getting-more-from-vim-with-plugins/)
  provides a list of plugins with a description for each one on its
  usefulness. The comments at the bottom are also interesting as people have
  suggested alternatives to some of the plugins mentioned in the post.

* [Powerline](https://github.com/powerline/powerline) is a popular statusline
  plugin for Vim that works with both Python 2 and 3.

