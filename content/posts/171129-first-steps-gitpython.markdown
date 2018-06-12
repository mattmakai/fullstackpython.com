title: First Steps with GitPython
slug: first-steps-gitpython
meta: Learn to use the GitPython library to programmatically interact with Git repositories.
category: post
date: 2017-11-29
modified: 2017-11-30
newsletter: False
headerimage: /img/171129-gitpython/header.jpg
headeralt: Python and Git logos, copyright their respective owners.


[GitPython](http://gitpython.readthedocs.io/) is a Python code library
for programmatically reading from and writing to [Git](/git.html)
[source control](/source-control.html) repositories.

Let's learn how to use GitPython by quickly installing it and reading from
a local cloned Git repository.


## Our Tools 
This tutorial should work with either [Python 2.7 or 3](/python-2-or-3.html), 
but Python 3, especially 3.6+, is strongly recommended for all new 
applications. I used
[Python 3.6.3](https://www.python.org/downloads/release/python-363/) to 
write this post. In addition to Python, throughout this tutorial we 
will also use the following 
[application dependencies](/application-dependencies.html): 

* [Git](/git.html), 
  a [source (version) control](/static-site-generator.html) implementation, 
  [version 2.15.1](https://github.com/git/git/tree/v2.15.1)
* [GitPython](https://github.com/gitpython-developers/GitPython/tree/2.1.7)
  version [2.1.7](https://github.com/gitpython-developers/GitPython/tree/2.1.7)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/), which come
  packaged with Python 3, to install and isolate the GitPython library
  from any of your other Python projects

Take a look at
[this guide for setting up Python 3 and Flask on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
if you need specific instructions to get a base
[Python development environment](/development-environments.html) set up.

All code in this blog post is available open source under the MIT license 
on GitHub under the 
[first-steps-gitpython directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples/tree/master/first-steps-gitpython).
Use and abuse the source code as you like for your own applications.


## Install GitPython
Start by creating a new virtual environment for your project. My virtualenv
is named `testgit` but you can name yours whatever matches the project 
you are creating.

```bash
python3 -m venv gitpy
```

Activate the newly-created virtualenv.

```
source gitpy/bin/activate
```

The virtualenv's name will be prepended to the command prompt after 
activation.

<img src="/img/171129-gitpython/activate-virtualenv.png" width="100%" class="shot rnd outl" alt="Create and activate the Python virtual environment.">

Now that the virutalenv is activated we can use the `pip` command to install
GitPython.


```bash
pip install gitpython==2.1.7
```

Run the `pip` command and after everything is installed you should see output
similar to the following "Successfully installed" message.

```bash
(gitpy) $ pip install gitpython==2.1.7
Collecting gitpython==2.1.7
  Downloading GitPython-2.1.7-py2.py3-none-any.whl (446kB)
    100% |████████████████████████████████| 450kB 651kB/s 
Collecting gitdb2>=2.0.0 (from gitpython==2.1.7)
  Downloading gitdb2-2.0.3-py2.py3-none-any.whl (63kB)
    100% |████████████████████████████████| 71kB 947kB/s 
Collecting smmap2>=2.0.0 (from gitdb2>=2.0.0->gitpython==2.1.7)
  Downloading smmap2-2.0.3-py2.py3-none-any.whl
Installing collected packages: smmap2, gitdb2, gitpython
Successfully installed gitdb2-2.0.3 gitpython-2.1.7 smmap2-2.0.3
```

Next we can start programmatically interacting with Git repositories in our
Python applications with the GitPython installed.


## Clone Repository
GitPython can work with remote repositories but for simplicity in this 
tutorial we'll use a cloned repository on our local system.

Clone a repository you want to work with to your local system. If you don't
have a specific one in mind use the 
[open source Full Stack Python Git repository](https://github.com/mattmakai/fullstackpython.com)
that is hosted on GitHub.

```bash
git clone git@github.com:mattmakai/fullstackpython.com fsp
```

Take note of the location where you cloned the repository because we need
the path to tell GitPython what repository to handle. Change into the 
directory for the new Git repository with `cd` then run the `pwd` (present
working directory) command to get the full path.

```bash
cd fsp
pwd
```

You will see some output like `/Users/matt/devel/py/fsp`. This path is your
absolute path to the base of the Git repository.

Use the `export` command to set an environment variable for the absolute path
to the Git repository.

```bash
export GIT_REPO_PATH='/Users/matt/devel/py/fsp' # make sure this your own path
```

Our Git repository and path environment variable are all set so let's write
the Python code that uses GitPython.


## Read Repository and Commit Data
Create a new Python file named `read_repo.py` and open it so we can start
to code up a simple script.

Start with a couple of imports and a constant:

```python
import os
from git import Repo


COMMITS_TO_PRINT = 5

```

The `os` module makes it easy to read environment variables, such as our
`GIT_REPO_PATH` variable we set earlier. `from git import Repo` gives our
application access to the GitPython library when we create the `Repo` object.
`COMMITS_TO_PRINT` is a constant that limits the number of lines of output
based on the amount of commits we want our script to print information on.
Full Stack Python has over 2,250 commits so there'd be a whole lot of output
if we printed every commit.

Next within our `read_repo.py` file create a function to print individual
commit information:

```python
def print_commit(commit):
    print('----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary,
                                     commit.author.name,
                                     commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(),
                                              commit.size)))


```

The `print_commit` function takes in a GitPython commit object and
prints the 40-character SHA-1 hash for the commit followed by:

1. the commit summary
1. author name 
1. author email
1. commit date and time
1. count and update size

Below the `print_commit` function, create another function named 
`print_repository` to print details of the `Repo` object:

```python
def print_repository(repo):
    print('Repo description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


```

`print_repository` is similar to `print_commit` but instead prints the
repository description, active branch, all remote Git URLs configured
for this repository and the latest commit.

Finally, we need a "main" function for when we invoke the script from the
terminal using the `python` command. Round out our 

```python
if __name__ == "__main__":
    repo_path = os.getenv('GIT_REPO_PATH')
    # Repo object used to programmatically interact with Git repositories
    repo = Repo(repo_path)
    # check that the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print('Could not load repository at {} :('.format(repo_path))
```

The main function handles grabbing the `GIT_REPO_PATH` environment variable
and creates a Repo object based on the path if possible.

If the repository is not empty, which indicates a failure to find the 
repository, then the `print_repository` and `print_commit` functions are 
called to show the repository data.

If you want to copy and paste all of the code found above at once, take a
look at the 
[`read_repo.py` file on GitHub](https://github.com/fullstackpython/blog-code-examples/blob/master/first-steps-gitpython/read_repo.py).

Time to test our GitPython-using script. Invoke the `read_repo.py` file using
the following command.

```bash
(gitpy) $ python read_repo.py
```

If the virtualenv is activated and the `GIT_REPO_PATH` environment variable
is set properly, we should see output similar to the following.

```bash
Repo at ~/devel/py/fsp/ successfully loaded.
Repo description: Unnamed repository; edit this file 'description' to name the repository.
Repo active branch is master
Remote named "origin" with URL "git@github.com:mattmakai/fullstackpython.com"
Last commit for repo is 1fa2de70aeb2ea64315f69991ccada51afac1ced.
----
1fa2de70aeb2ea64315f69991ccada51afac1ced
"update latest blog post with code" by Matt Makai (matthew.makai@gmail.com)
2017-11-30 17:15:14-05:00
count: 2256 and size: 254
----
1b026e4268d3ee1bd55f1979e9c397ca99bb5864
"new blog post, just needs completed code section" by Matt Makai (matthew.makai@gmail.com)
2017-11-30 09:00:06-05:00
count: 2255 and size: 269
----
2136d845de6f332505c3df38efcfd4c7d84a45e2
"change previous email newsletters list style" by Matt Makai (matthew.makai@gmail.com)
2017-11-20 11:44:13-05:00
count: 2254 and size: 265
----
9df077a50027d9314edba7e4cbff6bb05c433257
"ensure picture sizes are reasonable" by Matt Makai (matthew.makai@gmail.com)
2017-11-14 13:29:39-05:00
count: 2253 and size: 256
----
3f6458c80b15f58a6e6c85a46d06ade72242c572
"add databases logos to relational databases pagem" by Matt Makai (matthew.makai@gmail.com)
2017-11-14 13:28:02-05:00
count: 2252 and size: 270
```

The specific commits you see will vary based on the last 5 commits I've
pushed to the GitHub repository, but if you see something like the output
above that is a good sign everything worked as expected.


## What's next?
We just cloned a [Git](/git.html) repository and used the GitPython 
library to read a slew of data about the repository and all of its commits.

GitPython can do more than just read data though - it can also create and 
write to Git repositories! Take a look at the 
[modifying references](http://gitpython.readthedocs.io/en/stable/tutorial.html#modifying-references)
documentation page in the official GitPython tutorial or check back here in
the future when I get a chance to write up a more advanced GitPython 
walkthrough.

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).  

See something wrong in this blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/171129-first-steps-gitpython.markdown)
and submit a pull request.
