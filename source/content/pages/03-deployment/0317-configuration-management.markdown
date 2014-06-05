title: Configuration Management
category: page
slug: configuration-management
sort-order: 039
choice1url: /logging.html
choice1icon: fa-align-left fa-inverse
choice1text: How do I log events that happen in my app while it is running?
choice2url: /web-analytics.html
choice2icon: fa-dashboard
choice2text: I want to learn more about the users of my app with web analytics.
choice3url: /api-integration.html
choice3icon: fa-link fa-inverse
choice3text: How do I integrate external APIs into my application?
choice4url: /web-application-security.html
choice4icon: fa-lock fa-inverse
choice4text: What should I do to secure my web application?


# Configuration Management
Configuration management involves modifying servers from an existing state to 
a desired state and automating how an application is deployed.


## Configuration management tools
Numerous tools exist to modify server state in a controlled 
way, including [Puppet](http://puppetlabs.com/puppet/what-is-puppet), 
[Chef](http://www.getchef.com/chef/), 
[SaltStack](http://www.saltstack.com/), and Ansible. Puppet and Chef are
written in Ruby, while SaltStack and Ansible are written in Python.


## Ad hoc tasks
Configuration management tools such as Chef, Puppet, Ansible, and SaltStack
are not useful for performing ad hoc tasks that require interactive responses.
[Fabric](http://docs.fabfile.org/en/1.8/) and 
[Invoke](http://docs.pyinvoke.org/en/latest/) are used for interactive 
operations, such as querying the database from the Django manage.py shell.


## Ansible
[Ansible](http://www.ansibleworks.com/) is an open source configuration
management and application deployment tool built in Python.


### Ansible Resources
* [Official Ansible documentation](http://docs.ansible.com/index.html)

* [Python for Configuration Management with Ansible slides](http://www.insom.me.uk/post/pycon-talk.html) 
from PyCon UK 2013

* [Ansible Weekly Newsletter](http://devopsu.com/newsletters/ansible-weekly-newsletter.html)

* [First Steps with Ansible](http://labs.qandidate.com/blog/2013/11/15/first-steps-with-ansible/)

* [Red Badger on Ansible](http://red-badger.com/blog/2013/06/29/ansible/)

* [Getting Started with Ansible](http://lowendbox.com/blog/getting-started-with-ansible/)

* [Ansible Text Message Notifications with Twilio SMS](https://www.twilio.com/blog/2014/05/ansible-text-messages-notifications-with-twilio-sms.html)
  is my blog post with a detailed example for using the Twilio module in
  core Ansible 1.6+.

* [Ansible and Linode](http://softwareas.com/ansible-and-linode-what-i-learned-about-controlling-linodes-from-ansible)

* [Multi-factor SSH authentication with Ansible and Duo Security](http://jlafon.io/ansible-duo-security.html)

* [Ansible vs. Shell Scripts](http://devopsu.com/blog/ansible-vs-shell-scripts/)

* [Ansible and Salt: A Detailed Comparison](http://missingm.co/2013/06/ansible-and-salt-a-detailed-comparison/)

* [Automating your development environment with Ansible](http://www.nickhammond.com/automating-development-environment-ansible/)

* [Post-install steps with Ansible](http://devopsu.com/guides/ansible-post-install.html) 

* [First Five (and a half) Minutes on a Server with Ansible](http://lattejed.com/first-five-and-a-half-minutes-on-a-server-with-ansible) 

* [(Detailed) Introduction to Ansible](http://davidwinter.me/articles/2013/11/23/introduction-to-ansible/)

* [Shippable + Ansible + Docker + Loggly for awesome deployments](http://www.hiddentao.com/archives/2014/06/03/shippable-ansible-docker-loggly-for-awesome-deployments/)
  is a well written detailed post about using Docker and Ansible together with
  a few other pieces.

* [Create a Couchbase Cluster with Ansible](http://blog.couchbase.com/create-couchbase-cluster-with-ansible)

* [Idempotence, convergence, and other silly fancy words we often use](https://groups.google.com/forum/#!msg/Ansible-project/WpRblldA2PQ/lYDpFjBXDlsJ)

* [How to Write an Ansible Role for Ansible Galaxy](http://probablyfine.co.uk/2014/03/27/how-to-write-an-ansible-role-for-ansible-galaxy/)

* [Testing with Jenkins, Docker and Ansible](http://blog.mist.io/post/82383668190/move-fast-and-dont-break-things-testing-with)


## Application dependencies learning checklist
<i class="fa fa-check-square-o"></i>
Learn about configuration management in the context of deployment automation
and infrastructure-as-code.

<i class="fa fa-check-square-o"></i>
Pick a configuration management tool and stick with it. My recommendation is
Ansible because it is by far the easiest tool to learn and be productive with.

<i class="fa fa-check-square-o"></i>
Read your configuration management tool's documentation and, when necessary,
the source code.

<i class="fa fa-check-square-o"></i>
Automate the configuration management and deployment for your project. Note
that this is by far the most time consuming step in this checklist but will
pay dividends every time you deploy your project.

<i class="fa fa-check-square-o"></i>
Hook the automated deployment tool into your existing deployment process.


### What's next after automating your app configuration?
