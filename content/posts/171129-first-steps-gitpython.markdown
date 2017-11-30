title: First Steps with GitPython
slug: first-steps-gitpython
meta: Learn to use the GitPython library to programmatically interact with Git repositories.
category: post
date: 2017-11-29
modified: 2017-11-29
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

<img src="/img/171129-gitpython/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Create and activate the Python virtual environment.">

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
