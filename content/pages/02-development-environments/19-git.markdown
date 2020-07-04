title: Git
category: page
slug: git
sortorder: 0219
toc: False
sidebartitle: Git
meta: Git is an implementation of the source (version) control concept. Learn more about Git and source control on Full Stack Python.


[Git](https://git-scm.com/) is a distributed open source 
[source control](/source-control.html) (also referred to as "version 
control") system commonly used to track and manage file changes. Git is 
frequently used as the version control system for Python projects.

<a href="https://git-scm.com/" style="border: none;"><img src="/img/logos/git.png" width="100%" alt="Official Git logo." class="technical-diagram"></a>

<div class="well see-also">Git is an implementation of the <a href="/source-control.html">source control</a> concept. Learn how these pieces fit together in the <a href="/development-environments.html">development environments</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Why is Git widely-used by developers?
Git is a *distributed* version control system (DVCS) compared to the 
centralized models previously provided by 
[Subversion](https://subversion.apache.org/) and [CVS](https://www.nongnu.org/cvs/).
Files would need to be "checked out" over the network by a single person at
a time while she was working. The network transfer speed as well as the 
blocking check out model became a significant bottleneck, especially for 
large development teams. 

Git clones a full repository and its entire history instead of just the 
current state of a file. Developers only require a network connection when
pulling updates and pushing changes to a backup repository. The commit log
and file histories are stored and transmitted far more efficiently than
prior version control systems to maximize the effectiveness of the 
distributed version control design.

Another issue with traditional VCS was that it was difficult to create 
branches. Take a look
[at this tutorial on managing a CVS repository](http://www.sci.utah.edu/~macleod/docs/cvs-tips.html)
as an example of the confusion the existing non-distributed models could
cause. Git simplified the branching process with simplified commands 
such as `git checkout -b` and faster branch merging and clean up. In contrast
to earlier version control systems, Git encourages developers to create local 
branches and experiment in them without impacting a stable `master` branch.

[GitHub](https://www.github.com/) also helped to drive Git as the overwhelming
version control favorite by providing the open source community with free open
remote Git repositories. GitHub's web application user interface, issue 
tracking and pull request features for maintainers and consumers also 
encouraged more collaboration than Git alone. Recently, 
[GitHub's third-party marketplace](https://github.com/marketplace) has
begun to add more features by integrating 
[continuous integration](/continuous-integration.html) servers like 
as [Jenkins](/jenkins.html) and [code metrics](/code-metrics.html) services.


## Beginner Git tutorials
Git can take awhile to wrap your head around, even for experienced software
developers. The following tutorials can quickly get you up to speed.

* The [official Pro Git](https://git-scm.com/book/en/v2) book is available
  online for free. It is awesome both as a step-by-step walkthrough and as
  a bookmarked reference on specific topics.

* [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out)
  provides a spectacular walkthrough for developers who have used Git before
  but want to go deeper in understanding what each command does under the 
  covers instead of simply using the tool as a black box.

* [Think like a Git](http://think-like-a-git.net/) is another introduction
  that focuses more on the graph theory and conceptual ideas behind Git
  to help the reader understand what's happening as they use Git commands.

* [Git and GitHub in plain English](https://red-badger.com/blog/2016/11/29/gitgithub-in-plain-english)
  is a high-level overview of both Git and GitHub. This guide is intended 
  for both non-programmers and junior developers who want to learn everything
  from terminology to workflow.

* [A Hacker's Guide to Git](http://wildlyinaccurate.com/a-hackers-guide-to-git)
  is a free ebook written for experienced developers that contains both
  the syntax and the conceptual ideas behind how Git works.

* [A Designer's Guide to Git](https://blog.marvelapp.com/designers-guide-git/)
  gives a beginner's Git overview for non-programmers. The tutorial also 
  covers using Git clients such as the GitHub desktop application.

* [Git in Six Hundred Words](http://maryrosecook.com/blog/post/git-in-six-hundred-words)
  is a concise essay explaining what happens when you add and commit files
  in a Git repository.

* [19 Tips For Everyday Git Use](http://www.alexkras.com/19-git-tips-for-everyday-use/)
  is a laundry list of helpful Git tips on commands such as `git bisect`,
  `git stash` and `git difftool`.

* [git ready](http://gitready.com/) presents beginner, intermediate and 
  advanced tips for how to use Git. The example commands and their results
  are great for learning Git piece-by-piece.


## Advanced Git tutorials and resources
You won't learn Git in an afternoon or even a few months of usage. After
six-plus years of working with Git I still get tripped up and have a lot to
learn. These tutorials have taught me some of the beyond-the-basics edge
cases.

* [Flight rules for git](https://github.com/k88hudson/git-flight-rules) 
  contains common commands that answer specific desired tasks such as 
  "I want to discard specific unstaged files" (`git checkout filename`) and
  "I want to rename a branch" (`git branch -m newname`).

* [Shadows Of The Past: Analysis Of Git Repositories](https://jqassistant.org/shadows-of-the-past-analysis-of-git-repositories/)
  explains how you can extract some surprising data from Git repositories'
  commit history, such as which developers are domain experts in certain
  tools, potential hot spots in the code and coupling between source code
  files. This is a great read once you get past the basics of using Git.

* [Write yourself a Git!](https://wyag.thb.lt/) is a tutorial for building 
  your own version of Git from scratch with 503 lines of Python code. The 
  result is obviously not as full-featured as the real Git implementation
  but this program is awesome for understanding how Git's internals work.

* [Phil Nash](https://philna.sh/) shows how to use the `git reflog` command 
  in [Git back to the future](https://philna.sh/blog/2017/01/04/git-back-to-the-future/).
  
* [On undoing, fixing, or removing commits in git](https://sethrobertson.github.io/GitFixUm/fixup.html)
  is a fantastic overview of how to unscrew a whole slew of bad situations
  you may find yourself in if you use Git for long enough.

* [High-level Problems with Git and How to Fix Them](https://gregoryszorc.com/blog/2017/12/11/high-level-problems-with-git-and-how-to-fix-them/)
  is a long-form article on how to fork properly (and how not to use them)
  and how to not go crazy using branches and remote repositories.


## Specific Git resources
Large tutorials are great for getting started with Git. However, sometimes
you need tactical support or want to learn new tricks to add to your 
workflow. These resources will come in handy for specific Git subjects.

* [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/)
  provides strong advice that will help you write consistent, concise and
  contextual messages on your commits. Commit messages are especially 
  important when working with others on a long-lasting project where you
  dive through the commit history via `git log` and related commands.

* [How to squash Git commits](https://gitbetter.substack.com/p/how-to-squash-git-commits)
  explains how to use the `git rebase` command in interactive mode to
  consolidated the number of commits in your history. This technique is
  useful when a group of commits are related and it's easier to understand
  them as a single commit rather than a collection of smaller commits.

* [Oh shit, Git!](http://ohshitgit.com/) is a profanity-filled description
  of tips to get you out of binds you may find yourself in when you get too 
  tricky with Git commands. 

* [Tips for a disciplined git workflow](https://drewdevault.com/2019/02/25/Using-git-with-discipline.html)
  is less about workflow and more about how to write self-explaining commit
  messages, self-containing each commit and modifying branch history
  when you muff up before it is merged into master.

* [Another Git catastrophe cleaned up](http://blog.plover.com/prog/git-tastrophe.html) 
  goes through a difficult merge scenario that required deep Git 
  understanding to properly fix.
 
* Erlang's source code provides a concise explanation on 
  [writing good commit messages](https://github.com/erlang/otp/wiki/Writing-good-commit-messages)
  that any programming ecosystem can learn from. 

* [Git internals](https://blog.isquaredsoftware.com/presentations/2019-03-git-internals-rewrite/)
  is a presentation that covers how Git stores data, how to work with
  the Git history, and good practices for using Git based on the
  knowledge of how it works internally.

* [Chasing a bad commit](https://vishaltelangre.com/chasing-a-bad-commit/) 
  examines the `git bisect` command and how it can be used in either
  interactive mode or on its own with `git bisect run` to find the
  problematic code commit that needs to be fixed.

* [How Microsoft uses Git](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/use-git-microsoft)
  gives a high-level overview of their repository structure and hosting 
  at the extremely large scale organization.

* [GitTips](https://git.wiki.kernel.org/index.php/GitTips) is a list of 
  pro tips to clean up common issues and how to dive through Git history
  to find specific text.

* Git allows command aliasing, which allowed one developer to create his 
  own list of [lesser known Git commands](https://hackernoon.com/lesser-known-git-commands-151a1918a60)
  that alias more complicated Git lines.

* [Little things I like to do with Git](https://csswizardry.com/2017/05/little-things-i-like-to-do-with-git/)
  has some nice tips such as easily viewing branches you recently worked
  on and generating a changelog from your commits.

* [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out)
  demonstrates how Git's graph-based data structure produces certain behavior 
  through example Git commands. This is a highly recommended read after you've
  grasped the basics and are looking to go deeper with Git.

* [How I configure my git in a new computer](https://medium.com/@Tiagojdferreira/how-i-set-up-my-git-in-a-new-computer-85bb461b089f)
  shows how to handle a `.gitconfig` file, with 
  [an example Gist](https://gist.github.com/Tiagojdferreira/115ecac229e176e48d520c59b022e4fb) 
  that the author uses for his own environment.

* [How to Quickly and Correctly Generate a Git Log in HTML](http://www.oilshell.org/blog/2017/09/19.html)
  is an interesting look at how string processing on \*nix systems works
  by generating an HTML page from a Git log. If you need to output your
  Git commits somewhere and are having trouble writing your own script
  you should check out some of the interesting solutions the author
  presents.

* [Better Git configuration](https://blog.scottnonnenberg.com/better-git-configuration/)
  explains global config options, revisions and merging along with several
  other commands that can be customized to your taste.

* [Why does Git use a cryptographic hash function?](https://stackoverflow.com/questions/28792784/why-does-git-use-a-cryptographic-hash-function)
  explains that the SHA-1 hash isn't used for security on Git, it's a
  consistency check. [SHA-1 has been broken](https://shattered.io/)
  in practice so Git needs to transition to a stronger hash without proven
  collisions but it's not quite as big of a concern compared to 
  security-related projects that use SHA-1.

* [The anatomy of a git commit](https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html)
  digs into the tree and commit objects that underpin the Git source control
  system. This is an awesome read to get a view on how Git works under the
  commands you're using to manipulate these objects.


## Git Workflows
Teams of developers can use Git in varying workflows because of Git's 
distributed model and lightweight branching. There is no "right way" to 
use Git, especially because development teams can range in size from a
single developer up to entire companies with thousands of developers in
a repository. The only correct answer is to let the developers decide on
a workflow that maximizes their ability to frequently commit code and
minimize merge conflicts.

* [git-flow](http://nvie.com/posts/a-successful-git-branching-model/) shows
  one possible way for small teams to use Git branches.
  [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html) explains
  why at GitHub they do not use the git-flow model and provides an 
  alternative that solves some of the issues they found with git-flow.
  
* [Git Workflows That Work](http://blog.endpoint.com/2014/05/git-workflows-that-work.html)
  is a helpful post with diagrams to show how teams can create a Git workflow
  that will help their development process.

* [Comparing workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
  provides a slew of examples for how developers on a team can handle merge
  conflicts and other situations that commonly arise when using Git.


### GitHub resources
GitHub is a software-as-a-service application 
[owned by Microsoft](https://blogs.microsoft.com/blog/2018/06/04/microsoft-github-empowering-developers/)
that makes it easier to collaborate with other developers on centralized
Git repositories. The site also provides a remote backup location for
repositories as well as secure, private repository storage. The following
tutorials show how to get started using Git on GitHub.

* [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/)
  covers basic usage for Git and working with repositories locally and on
  the GitHub service.

* [Hello World: GitHub edition](https://guides.github.com/activities/hello-world/) 
  and
  [Git and GitHub learning resources](https://help.github.com/articles/git-and-github-learning-resources/)
  are GitHub's official guide and learning resources.

* [A Beginner’s Git and GitHub Tutorial](https://blog.udacity.com/2015/06/a-beginners-git-github-tutorial.html)
  shows how to perform your first commit and back it up on GitHub.

