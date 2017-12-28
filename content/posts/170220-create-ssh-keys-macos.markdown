title: Creating SSH Keys on macOS Sierra
slug: ssh-keys-macos-sierra
meta: Learn how to quickly create new SSH keys on macOS Sierra.
category: post
date: 2017-02-20
modified: 2017-04-28
newsletter: False
headerimage: /img/170220-ssh-keys-macos/header.jpg
headeralt: Apple logo, copyright Apple.


[Deploying](/deployment.html) Python applications typically requires
SSH keys. An SSH key has both a public and a private key file. You can 
use the private key to authenticate when syncing remote [Git](/git.html) 
repositories, connect to remote [servers](/servers.html) and automate 
your application's deployments via 
[configuration management](/configuration-management.html) tools like 
Ansible. Let's learn how to generate SSH key pairs on 
[macOS Sierra](http://www.apple.com/macos/sierra/).


## Generating New Keys
Bring up a new terminal window on macOS by going into Applications/Utilities
and opening "Terminal".

<img src="/img/170220-ssh-keys-macos/new-terminal.jpg" width="100%" class="technical-diagram img-rounded" alt="New macOS terminal window.">

The `ssh-keygen` command provides an interactive command line interface for
generating both the public and private keys. Invoke `ssh-keygen` with the
following `-t` and `-b` arguments to ensure we get a 4096 bit RSA key. Note 
that you *must* use a key with 2048 or more bits in macOS Sierra or the
system will not allow you to connect to servers with it.

Optionally, you can also specify your email address with `-C` (otherwise 
one will be generated off your current macOS account):

```bash
ssh-keygen -t rsa -b 4096 -C my.email.address@company.com
```

The first prompt you will see asks where to save the key. However, there are
actually two files that will be generated: the public key and the private 
key. 

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/matt/.ssh/id_rsa):
```

This prompt refers to the private key and whatever you enter will also
generate a second file for the public key that has the same name and `.pub` 
appended.

If you already have a key then specify a new filename. I use many
SSH keys so I oftne name them "test-deploy", "prod-deploy", "ci-server"
along with a unique project name. Naming is one of those hard computer 
science problems, so take some time to come up with a system that works for
you!

Next you will see a prompt for an optional passphrase:

```bash
Enter passphrase (empty for no passphrase):
```

Whether or not you want a passphrase depends on how you will use the key.
The system will ask you for the passphrase whenever you use the SSH key,
although 
[macOS can store the passphrase in your system Keychain](http://apple.stackexchange.com/questions/254468/macos-sierra-doesn-t-seem-to-remember-ssh-keys-between-reboots) 
after the first time you enter it. However, if you are automating deployments 
with a [continuous integration](/continuous-integration.html) server like
[Jenkins](/jenkins.html) then you will not want a passphrase.

Note that it is impossible to recover a passphrase if it is lost. Keep 
that passphrase safe and secure because otherwise a completely new key would 
have to be generated.

Enter the passphrase (or just press enter to not have a passphrase) twice.
You'll see some output like the following:

```bash
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/matt/.ssh/deploy_prod.
Your public key has been saved in /Users/matt/.ssh/deploy_prod.pub.
The key fingerprint is:
SHA256:UnRGH/nzYzxUFS9jjd0wOl1ScFGKgW3pU60sSxGnyHo matthew.makai@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|        ..+o++**@|
|       . +.o*O.@=|
|        . oo*=B.*|
|       . .  =o=+ |
|      . S E. +oo |
|       . .  .  =.|
|              . o|
|                 |
|                 |
+----[SHA256]-----+
```

Your SSH key is ready to use!


## What now?
Now that you have your public and private keys, I recommend building and
deploying some [Python web apps](/web-development.html) such as:

* [Building your first Slack bot](/blog/build-first-slack-bot-python.html)
* [Sending picture or video messages via a REST API](/blog/send-mms-picture-messages-python.html)
* [Dialing outbound phone calls](/blog/dial-outbound-phone-calls-python-bottle.html)
  with the [Bottle](/bottle.html) web framework

Additional `ssh-keygen` command resources:

* [SSH keys on macOS Sierra](https://testequals.com/2016/09/09/macos-sierra-10-12-ssh-keys/)
* [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)


Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170220-create-ssh-keys-macos.markdown)
and submit a pull request.
