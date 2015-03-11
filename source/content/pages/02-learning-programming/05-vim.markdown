title: Vim
category: page
slug: vim
sort-order: 0205
meta: Vim is a text editor with powerful string manipulation capabilities. Learn more about Vim on Full Stack Python.
choice1url: /development-environments.html
choice1icon: fa-desktop
choice1text: What other editors and development environments exist?
choice2url: /best-python-resources.html
choice2icon: fa-book fa-inverse
choice2text: Show me a list of the best Python learning resources.
choice3url: /web-frameworks.html
choice3icon: fa-code fa-inverse
choice3text: I want to get started coding a Python web app.
choice4url:
choice4icon:
choice4text:


# Vim
Vim, shorthand for Vi IMproved, is a text editor with numerous configuration 
options and wide-ranging extensions that can be used to write Python code.


## Why is Vim a good Python development environment?
Vim's philosophy is that developers are fastest when they never take their 
hands off the keys. Even using the mouse is a detriment to the rate at which
your thoughts can flow into code. 

Vim has a language behind its commands. When a beginner is learning the
editor she may feel like it is impossible to understand all the key commands.
However, the commands stack together in a logical way so that over time
the editor becomes predictable.


## Configuring Vim with a Vimrc
The Vimrc file is used to configure the Vim editor. A Vimrc file can range
from nothing in it to very complicated with hundreds or thousands of lines
of configuration commands.

Here's a simple example .vimrc file I use for Python development to get a feel
for some of the configuration statements:

    # enable syntax highlighting
    syntax on

    # the next 4 lines set tabs to have 4 spaces, autoindent when already
    # working with indented lines, expand tabs key presses to spaces and
    # move lines 4 spaces each time the >> or << commands are used
    set ts=4
    set autoindent
    set expandtab
    set shiftwidth=4

    # enable all Python syntax highlighting features
    let python_highlight_all = 1


The Vimrc file lives under the home directory of the user account running
Vim. For example, when my user account is 'matt', on Mac OS X my Vimrc
file is found at ``/Users/matt/.vimrc``. On Ubuntu Linux my Vimrc file
can be found within ``/home/matt/.vimrc``. 

If the Vimrc file does not already exist, just create it within the user's
home directory and it will be picked up by Vim the next time you start the
program.


## General Vim resources
* [Vim Adventures](http://vim-adventures.com/) is a cute, fun browser-based
  game that helps you learn Vim commands by playing through the adventure.

* [Learn Vim Progressively](http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)
  is a wonderful tutorial that follows the path I took when learning Vim:
  learn just enough to survive with it as your day-to-day editor then begin 
  adding more advanced commands on top.

* [A vim Tutorial and Primer](https://danielmiessler.com/study/vim/) is an
  incredibly deep study in how to go from beginner to knowledgeable in Vim.

* [Vim as Your IDE](http://haridas.in/vim-as-your-ide.html) discusses how to
  set up Vim for greater productivity once you learn the initial Vim language 
  for using the editor.

* [Setting up Vim for Python](http://stackoverflow.com/questions/9172802/setting-up-vim-for-python)
  has a well written answer on Stack Overflow for getting started with Vim.

* [Vim as a Language](http://benmccormick.org/2014/07/02/learning-vim-in-2014-vim-as-language/)
  explains the language syntax and how you can build up over time to master
  the editor.

* In [Vim: revisited](http://mislav.uniqpath.com/2011/12/vim-revisited/) the
  author explains his on-again off-again relationship with using Vim. He then
  shows how he configures and uses the editor so it sticks as his primary
  code editting tool.


## Vim installation guides
* [Upgrading Vim on OS X](http://prioritized.net/blog/upgrading-vim-on-os-x/)
  explains why to upgrade from Vim 7.2 to 7.3+ and how to do it using 
  [Homebrew](http://brew.sh/).

* The easiest way to install Vim on Windows 7+ is to download and run the 
  [gvim74.exe](http://www.vim.org/download.php#pc) file.

* On Linux make sure to install the 
  [vim package](https://launchpad.net/ubuntu/+source/vim) with
  ``sudo apt-get install vim``.


## Vimrc resources
* [A Good Vimrc](http://dougblack.io/words/a-good-vimrc.html) is a fantastic,
  detailed overview and opinionated guide to configuring Vim. Highly 
  recommended for new and experienced Vim users.

* [Vim and Python](https://justin.abrah.ms/vim/vim_and_python.html) shows
  and explains many Python-specific .vimrc options.


### What do you want to learn about Python development?
