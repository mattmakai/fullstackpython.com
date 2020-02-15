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


### Bash resources
* [Bash Guide for beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html)
  is an entire book for those new to working with commandlines. It covers
  commands, paths, Bash shell scripting, variables and many other critical
  topics that are necessary to move from beginner to advanced Bash user. 

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

* Google's [Shell Style Guide](https://google.github.io/styleguide/shell.xml)
  covers how to write consistent, maintainable shell scripts, which is 
  particularly important if you have ever tried to debug a hacky shell 
  script that was never meant to be used by anyone other than the original
  author.

* [101 Bash Commands and Tips for Beginners to Experts](https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je)
  is a well-done laundry list of tricks to explore.

* [Bash scripting quirks & safety tips](https://jvns.ca/blog/2017/03/26/bash-quirks/)
  explains Bash basic programming constructs like `for` loops and variable 
  assignment then goes into ways to avoid weird issues in your code.

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

* [Replacing Bash scripts with Python](https://github.com/ninjaaron/replacing-bash-scripting-with-python)
  is a guide on using using Python for administrative scripting, including
  what to do about replacing invaluable command line tools such as `awk`, 
  `sed` and `grep`.

* [Using Aliases to Speed Up Your Git Workflow](https://dev.to/robertcoopercode/using-aliases-to-speed-up-your-git-workflow-2f5a)
  has a bunch of shell aliases that make it easier for you to execute
  complicated or uncommon [Git](/git.html) commands.

* [Creating a bash completion script](https://iridakos.com/tutorials/2018/03/01/bash-programmable-completion-tutorial.html)
  is a great tutorial that walks you through a reasonably complex Bash
  script for completing syntax in other Bash shell scripts.

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

* [Bash Quick References](https://shellmagic.xyz/) is a cheat sheet for
  common operators and signals that come up when working with scripts.

* [Anybody can write good bash (with a little effort)](https://blog.yossarian.net/2020/01/23/Anybody-can-write-good-bash-with-a-little-effort)
  covers the basics of shell scripting and provides some recommendations
  for creating more maintainable scripts such as using linters and
  formatters.
