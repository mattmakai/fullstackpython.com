title: Creating SSH Keys on Ubuntu Linux 16.04 LTS
slug: ssh-keys-ubuntu-linux
meta: Learn how to quickly generate new SSH keys on Ubuntu Linux 16.04 LTS.
category: post
date: 2017-02-14
modified: 2017-04-28
newsletter: False
headerimage: /img/170214-ssh-keys-ubuntu/header.jpg
headeralt: Ubuntu Linux logo, copyright Canonical Ltd.


SSH keys are a necessity for Python development when you are working with
[Git](/git.html), connecting to remote servers and automating your
[deployments](/deployment.html). Let's walk through how to generate SSH
key pairs, which contain both a public and a private key within a single 
pair, on Ubuntu Linux.


## Generating the Public and Private Keys
Open up a new terminal window in Ubuntu like we see in the following 
screenshot.

<img src="/img/170214-ssh-keys-ubuntu/new-ubuntu-terminal.jpg" width="100%" class="technical-diagram img-rounded">

The `ssh-keygen` command provides an interactive command line interface for
generating both the public and private keys. Invoke `ssh-keygen` with the
following `-t` and `-b` arguments to ensure we get a 4096 bit RSA key.
Optionally, you can also specify your email address with `-C` (otherwise 
one will be generated off your current Linux account):

```bash
ssh-keygen -o -t rsa -b 4096 -C my.email.address@company.com
```

(Note: the `-o` option was introduced in 2014; if this command fails for you, simply remove the `-o` option)

The first prompt you will see asks where to save the key. However, there are
actually two files that will be generated: the public key and the private 
key. 

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/matt/.ssh/id_rsa): 
```

This prompt refers to the private key and whatever you enter will also
generate a second file for the public key that has the same name and `.pub` 
appended.

If you already have a key, you should specify a new filename. I use many
SSH keys so I typically name them "test-deploy", "prod-deploy", "ci-server"
along with a unique project name. Naming is one of those hard computer 
science problems, so take some time to come up with a system that works for
you and the development team you work with!

Next you will see a prompt for an optional passphrase:

```bash
Enter passphrase (empty for no passphrase):
```

Whether or not you want a passphrase depends on how you will use the key.
The system will ask you for the passphrase whenever you use the SSH key
so it is more secure.
However, if you are automating deployments with a 
[continuous integration](/continuous-integration.html) server like
[Jenkins](/jenkins.html) then you will not want a passphrase.

Be aware that it is impossible to recover a passphrase if it is lost. Keep 
that passphrase safe and secure because otherwise a completely new key would 
have to be generated.

Enter the passphrase (or just press enter to not have a passphrase) twice.
You'll see some output like the following:

```bash
Your identification has been saved in /home/matt/.ssh/prod_deploy.
Your public key has been saved in /home/matt/.ssh/prod_deploy.pub.
The key fingerprint is:
SHA256:xoCWgk40XfM5mruZQNCVoBKXZ4d0gn09ivVENacb7xw matt@ubuntu
The key's randomart image is:
+---[RSA 2048]----+
|.oo*==oo..o .    |
|.+*.*** =  +     |
|o+.++=.B .o      |
|+ .o. +oo  +     |
| . . o  S . E    |
|  .   ..   o .   |
|   . .      o    |
|    . +          |
|     +           |
+----[SHA256]-----+
```

Your SSH key is now generated and ready to use!


## What now?
Now that you have your public and private keys, I recommend setting
up a [Python development environment](/development-environments.html) with 
one of the following tutorials so you can start coding:

* [Setting up Python 3, Django and Gunicorn on Ubuntu 16.04 LTS](/blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html)
* [How to Use Redis with Python 3 and redis-py on Ubuntu 16.04](/blog/install-redis-use-python-3-ubuntu-1604.html)
* [Setting up PostgreSQL with Python 3 and psycopg on Ubuntu 16.04](/blog/postgresql-python-3-psycopg2-ubuntu-1604.html)

Additional `ssh-keygen` command resources:

* [ubuntu manuals ssh-keygen](http://manpages.ubuntu.com/manpages/xenial/man1/ssh-keygen.1.html)
* [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)


Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170214-create-ssh-keys-ubuntu.markdown)
and submit a pull request.
