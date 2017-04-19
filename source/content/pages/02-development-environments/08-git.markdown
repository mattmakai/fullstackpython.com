title: Git
category: page
slug: git
sortorder: 0208
toc: False
sidebartitle: Git
meta: Git is an implementation of the source (version) control concept. Learn more about Git and source control on Full Stack Python.


# Git
[Git](https://git-scm.com/) is a distributed open source 
[source control](/source-control.html) (also referred to as "version 
control") system commonly used to track and manage file changes. Git is 
frequently used as the version control system for Python projects.

<a href="https://git-scm.com/" style="border: none;"><img src="/img/git-logo.png" width="100%" alt="Official Git logo." class="technical-diagram"></a>

<div class="well see-also">Git is an implementation of the <a href="/source-control.html">source control</a> concept. Learn how these pieces fit together in the <a href="/development-environments.html">development environments</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Git tutorials
Git can take awhile to wrap your head around, even for experienced software
developers. The following tutorials can quickly get you up to speed.

* The [official Pro Git](https://git-scm.com/book/en/v2) book is available
  online for free. It is awesome both as a step-by-step walkthrough and as
  a bookmarked reference on specific topics.

* [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out)
  provides a spectacular walkthrough for developers who have used Git before
  but want to go deeper in understanding what each command does under the 
  covers instead of simply using the tool as a black box.

* [Git and GitHub in plain English](https://red-badger.com/blog/2016/11/29/gitgithub-in-plain-english)
  is a high-level overview of both Git and GitHub. This guide is intended 
  for both non-programmers and junior developers who want to learn everything
  from terminology to workflow.

* [A Designer's Guide to Git](https://blog.marvelapp.com/designers-guide-git/)
  gives a beginner's Git overview for non-programmers. The tutorial also 
  covers using Git clients such as the GitHub desktop application.

* [Git in Six Hundred Words](http://maryrosecook.com/blog/post/git-in-six-hundred-words)
  is a concise essay explaining what happens when you add and commit files
  in a Git repository.

* A 
  [practical git introduction](http://marc.helbling.fr/2014/09/practical-git-introduction)
  is rich with pragmatic examples for Git usage.


## Specific Git resources
Large tutorials are great for getting started with Git. However, sometimes
you need tactical support or want to learn new tricks to add to your 
workflow. These resources will come in handy for specific Git subjects.

* [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/)
  provides strong advice that will help you write consistent, concise and
  contextual messages on your commits. Commit messages are especially 
  important when working with others on a long-lasting project where you
  dive through the commit history via `git log` and related commands.

* [Oh shit, Git!](http://ohshitgit.com/) is a profanity-filled description
  of tips to get you out of binds you may find yourself in when you get too 
  tricky with Git commands. 

* [Phil Nash](https://philna.sh/) shows how to use the `git reflog` command 
  in [Git back to the future](https://philna.sh/blog/2017/01/04/git-back-to-the-future/).
  
 * [Another Git catastrophe cleaned up](http://blog.plover.com/prog/git-tastrophe.html) 
   goes through a difficult merge scenario that required deep Git 
   understanding to properly fix.
 
* Erlang's source code provides a concise explanation on 
  [writing good commit messages](https://github.com/erlang/otp/wiki/Writing-good-commit-messages)
  that any programming ecosystem can learn from. 

* [GitTips](https://git.wiki.kernel.org/index.php/GitTips) is a list of 
  pro tips to clean up common issues and how to dive through Git history
  to find specific text.

* [19 Tips For Everyday Git Use](http://www.alexkras.com/19-git-tips-for-everyday-use/)
  is a laundry list of helpful Git tips on commands such as `git bisect`,
  `git stash` and `git difftool`.

* Git allows command aliasing, which allowed one developer to create his 
  own list of [lesser known Git commands](https://hackernoon.com/lesser-known-git-commands-151a1918a60)
  that alias more complicated Git lines.

* [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out)
  demonstrates how Git's graph-based data structure produces certain behavior 
  through example Git commands. This is a highly recommended read after you've
  grasped the basics and are looking to go deeper with Git.

* [How To Host Your Own Private Git Repositories](https://eklitzke.org/how-to-how-your-own-private-git-repositories)
  provides the steps for handling private Git repositories on your own
  server. This setup is great for either mirroring GitHub repositories
  or just getting away from hosted services entirely.

* [How I configure my git in a new computer](https://medium.com/@Tiagojdferreira/how-i-set-up-my-git-in-a-new-computer-85bb461b089f)
  shows how to handle a `.gitconfig` file, with 
  [an example Gist](https://gist.github.com/Tiagojdferreira/115ecac229e176e48d520c59b022e4fb) 
  that the author uses for his own environment.


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

* "[Our Git Workflow](http://www.braintreepaymentsolutions.com/devblog/our-git-workflow)"
  by Braintree goes over how this payments company uses Git for development
  and merging source code.

