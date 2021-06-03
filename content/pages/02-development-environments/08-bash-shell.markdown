title: Bash shell
category: page
slug: bourne-again-shell-bash
sortorder: 0208
toc: False
sidebartitle: Bash shell
meta: The Bourne-Again Shell (Bash) is an implementation of the shell concept and is often used during Python software development.


The [Bourne-Again SHell](https://www.gnu.org/software/bash/) 
([source code](https://savannah.gnu.org/git/?group=bash)), almost 
always referred to simply as "*Bash*", interprets and executes input 
entered from a source such as the user or a program. Bash is an 
implementation of the [shell concept](/shells.html) and is often used 
during Python software development as part of a programmer's 
[development environment](/development-environments.html).

<a href="https://www.gnu.org/software/bash/" style="border:none"><img src="/img/logos/bash-wide.jpg" width="100%" alt="Bourne-again shell (Bash) logo."></a>

<div class="well see-also">Bash is an implementation of the <a href="/shells.html">shells</a> concept. Learn more in the <a href="/development-environments.html">development environments</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### How do Python developers use Bash?
If you are programming in the terminal on [macOS](/macos.html)
or [Linux](/ubuntu.html), or using the 
[Windows Subsystem for Linux on Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10),
you can easily gain access to Bash if it is not already
your default shell.

You can show what shell you are currently using by echoing the
`SHELL` environment variable, like so:

```
$ echo "$SHELL"
```

Which will then print the shell you are currently using. For example,
on macOS I am using Bash by default so the echo command prints:

```
/bin/bash
```

How much you use Bash or any shell will likely depend on your
[development environment](/development-environments.html), especially
if you are using an editor like [Vim](/vim.html) instead of an
IDE like [PyCharm](/pycharm.html), because it is often easier to do
certain tasks in the shell. For example, most developers I know who
use PyCharm will search for some instance of source code right in
their IDE, whereas I use a combination of Vim and [tmux](/tmux.html)
so I frequently flip between panes to use commands like `grep` to
do my source code searches. 

There is no right way to perform a task like source code searching, it's 
really just what works for your brain as a developer that will guide
how often you interact with the Bash shell.


### Getting started with Bash
Working with a shell, Bash or otherwise, is intimidating the first time
you try to get started. You are staring at the `$` prompt without a
whole lot of direction.

When you are completely new to using Bash, it is a good idea to at least
scan, if not take some additional time for in-depth reading of the
documentation for commands that every developer uses. The following 
commands are used so frequently in Bash that an experienced developer
probably does not even think about them anymore, they become just a
natural part of your workflow:

* `echo`: [print text to the command line](https://man7.org/linux/man-pages/man1/echo.1.html)
* `ls`: [list the contents of a directory](https://man7.org/linux/man-pages/man1/ls.1.html)
* `cd`: [change the working directory](https://man7.org/linux/man-pages/man1/cd.1p.html)
* `cp`: [copy a file or directory](https://man7.org/linux/man-pages/man1/cp.1.html)
* `mv`: [move one or more files](https://man7.org/linux/man-pages/man1/mv.1.html)
* `rm`: [delete one or more files or directories](https://man7.org/linux/man-pages/man1/rm.1.html)

If you know how to use the above commands then you will at least be able
to move around the file system, create, move and update files and know
what is on your storage device(s).

The following commands are somewhat more advanced but also frequently
used by developers:

* `su`: [run comamnds as different users or groups](https://man7.org/linux/man-pages/man1/su.1.html)
* `whoami`: [print which user you are currently logged in as](https://man7.org/linux/man-pages/man1/whoami.1.html)
* `grep`: [searches for patterns in files](https://man7.org/linux/man-pages/man1/grep.1.html)

The above lists are not even close to exhaustive for what commands
you need to know when working with Bash. Read some of the following
introductory tutorials to gain a better understanding of working
with this shell:

* [The Linux command line for beginner](https://ubuntu.com/tutorials/command-line-for-beginners)
  by [Ubuntu](/ubuntu.html) will provide you with context for how to
  use the command line, working with files and directories, and handling
  superuser commands.

* [Bash Guide for beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html)
  is an entire book for those new to working with command lines. It covers
  commands, paths, Bash shell scripting, variables and many other critical
  topics that are necessary to move from beginner to advanced Bash user. 

* [101 Bash Commands and Tips for Beginners to Experts](https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je)
  gives a well-done laundry list of tricks to explore.

* [Bash Quick References](https://shellmagic.xyz/) is a cheat sheet for
  common operators and signals that come up when working with scripts.


### Bash scripting
Bash is used not only as an interactive prompt but also for scripting, which
makes it possible to execute one or more Bash commands stored within a file.
These scripts can be short, with only a single command, or very complicated
with control-flow logic, for loops, and almost anything you want to automate
or compute because 
[Bash is a Turing-complete programming language](https://www.quora.com/Is-Bash-Turing-complete).

Complex Bash scripts sometimes get a negative reputation because they can be
difficult to read and understand if you are not the original author (or you
are reading your own script after a significant period of time has elapsed). 
There are many ways to accomplish the same tasks with Bash so the files are
often confusing to read unless the author of a script included clear 
documentation. This readability problem is typically less of an issue with
Python scripts because spacing is enforced and the standard library 
encapsulates common tasks.

It's a good idea to think about how you want to structure your Bash scripts
as they grow larger. The following resources provide insight into what you
should consider while coding Bash scripts.

* This [minimal safe Bash template](https://betterdev.blog/minimal-safe-bash-script-template/)
  contains an 86-line Bash script that the author claims once you 
  understand and use it as a base then it will make your scripts
  easier to maintain over time.

* [Creating a bash completion script](https://iridakos.com/tutorials/2018/03/01/bash-programmable-completion-tutorial.html)
  is a great tutorial that walks you through a reasonably complex Bash
  script for completing syntax in other Bash shell scripts.

* [Anybody can write good bash (with a little effort)](https://blog.yossarian.net/2020/01/23/Anybody-can-write-good-bash-with-a-little-effort)
  covers the basics of shell scripting and provides some recommendations
  for creating more maintainable scripts such as using linters and
  formatters.

* Google's [Shell Style Guide](https://google.github.io/styleguide/shell.xml)
  covers how to write consistent, maintainable shell scripts, which is 
  particularly important if you have ever tried to debug a hacky shell 
  script that was never meant to be used by anyone other than the original
  author.

* [Bash scripting quirks & safety tips](https://jvns.ca/blog/2017/03/26/bash-quirks/)
  explains Bash basic programming constructs like `for` loops and variable 
  assignment then goes into ways to avoid weird issues in your code.

* If all else fails when you're trying to use Bash scripts, this article
  on [replacing Bash scripts with Python](https://github.com/ninjaaron/replacing-bash-scripting-with-python)
  is a guide on swapping in Python for administrative scripting, including
  what to do about replacing invaluable command line tools such as `awk`, 
  `sed` and `grep`.


### Additional Bash resources
The following resources cover more advanced Bash use cases and what pitfalls
to try to avoid as you work with the shell or write scripts.

* [Advancing in the Bash shell](http://samrowe.com/wordpress/advancing-in-the-bash-shell/)
  covers important concepts such as bang syntax, movement commands, 
  tab completion and aliases.

* [Mastering Bash and Terminal](https://www.blockloop.io/mastering-bash-and-terminal)
  shows methods for repeating commands, changing directories and
  handling background processes.

* [Ten Things I Wish I’d Known About Bash](https://zwischenzugs.com/2018/01/06/ten-things-i-wish-id-known-about-bash/)
  covers some edge cases that are very useful to know about such as
  proper exit code usage and configuration options through the `set`
  command. There is also a great follow up post called
  [Ten MORE Things I Wish I'd Known About Bash](https://zwischenzugs.com/2018/01/21/ten-more-things-i-wish-id-known-about-bash/) 
  that covers new topics such as on-the-fly command re-execution using the 
  carrot character. The 
  [Seven Surprising Bash Variables](https://zwischenzugs.com/2019/05/11/seven-surprising-bash-variables/)
  post continues the series by examining built-in variables such as
  `PROMPT_COMMAND`, `CDPATH` and `REPLY` which can simplify your
  scripts by using values that Bash already has stored for you.

* [Safe ways to do things in bash](https://github.com/anordal/shellharden/blob/master/how_to_do_things_safely_in_bash.md)
  shows you how to not shoot yourself in the foot by using safe coding
  practices with your shell scripts.

* The 
  [Bash Infinity Framework](https://invent.life/project/bash-infinity-framework)
  [source code](https://github.com/niieani/bash-oo-framework) provides 
  boilerplate and a standard library for Bash projects so they are easier 
  to read and maintain. If you have ever tried to read someone else's
  Bash scripts or even your own after setting them aside for a couple of 
  months, you know that anything which makes readability better is a major 
  step up from vanilla Bash.

* [Static status](https://github.com/Cyclenerd/static_status) is a Bash 
  application that generates a hostable, customizable status page for your 
  services.

* [Using Aliases to Speed Up Your Git Workflow](https://dev.to/robertcoopercode/using-aliases-to-speed-up-your-git-workflow-2f5a)
  has a bunch of shell aliases that make it easier for you to execute
  complicated or uncommon [Git](/git.html) commands.

* [6 Tips Before You Write Your Next Bash Cronjob](https://yasoob.me/posts/6-tips-before-you-write-your-next-bash-cronjob/)
  covers starting your scripts with shebang, redirecting output, timeouts
  and sudo privileges.

* [Better Bash history](https://sanctum.geek.nz/arabesque/better-bash-history/)
  shows how to make your Bash history more useful by having it store more
  previous commands (which takes up more persistent storage but is not
  a huge deal in 2019) and add timestamps to the `history` command.

* [9 Evil Bash Commands Explained](https://dev.to/devmount/9-evil-bash-commands-explained-4k5e)
  presents a list of commands *you should never run*, but can learn about
  their destructive abilities by reading through the descriptions provided
  by the author.

* [Faster bash startup](https://danpker.com/posts/faster-bash-startup/)
  and
  [Even faster bash startup](https://work.lisk.in/2020/11/20/even-faster-bash-startup.html)
  are two great tutorials that will save you a bunch of time if you frequently
  open new Bash shells. On many systems you can easily cut down the startup
  time for the shell which can be unnecessarily sluggish.

* [Bash HTTP monitoring dashboard](https://raymii.org/s/software/Bash_HTTP_Monitoring_Dashboard.html)
  ([source code](https://github.com/RaymiiOrg/bash-http-monitoring))
  is a useful application fully written in Bash shell scripts that
  monitors the health of one or more websites to make sure they are
  up and running.
