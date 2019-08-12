title: Configuration Management
category: page
slug: configuration-management
sortorder: 0532
toc: False
sidebartitle: Configuration Management
meta: Configuration management tools automate application deployments and environment settings.


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


## Configuration management tool comparisons
* [Moving away from Puppet: SaltStack or Ansible?](http://ryandlane.com/blog/2014/08/04/moving-away-from-puppet-saltstack-or-ansible/)
  is an openly biased but detailed post on why to choose SaltStack over 
  Ansible in certain situations.

* [Ansible vs. Shell Scripts](https://valdhaus.co/writings/ansible-vs-shell-scripts/)
  provides some perspective on why using a configuration management tool is a 
  better choice than venerable but brittle shell scripts.

* [Ansible vs. Chef](http://tjheeta.github.io/2015/04/15/ansible-vs-chef/)
  is a comparsion of Ansible with the Chef configuration management tool.

* This post on [Ansible and Salt: A Detailed Comparison](http://missingm.co/2013/06/ansible-and-salt-a-detailed-comparison/)
  shows the differences between these two Python-powered tools.


### Configuration management resources
* [A quick guide to choosing infrastructure tools](https://www.oreilly.com/learning/a-quick-guide-to-choosing-infrastructure-tools)
  presents a high-level overview of the categories of tools you will need
  to perform infrastructure-as-code in an organization.


## Ansible configuration management
[Ansible](http://www.ansible.com/) is an open source configuration
management and application deployment tool built in Python.


### Ansible Resources
* [An Ansible Tutorial](https://serversforhackers.com/c/an-ansible2-tutorial)
  is a fantastically detailed introduction on using Ansible to set up
  servers.

* [Ansible Text Message Notifications with Twilio SMS](https://www.twilio.com/blog/2014/05/ansible-text-messages-notifications-with-twilio-sms.html)
  is my blog post with a detailed example for using the Twilio module in
  core Ansible 1.6+.

* [Python for Configuration Management with Ansible slides](http://www.insom.me.uk/post/pycon-talk.html) 
from PyCon UK 2013

* [First Steps with Ansible](http://labs.qandidate.com/blog/2013/11/15/first-steps-with-ansible/)

* [Red Badger on Ansible](http://red-badger.com/blog/2013/06/29/ansible/)

* [Getting Started with Ansible](http://lowendbox.com/blog/getting-started-with-ansible/)

* [An introduction to Ansible](https://davidwinter.me/introduction-to-ansible/)
  is a tutorial on the basics of getting started with the tool.

* [Ansible and Linode](http://softwareas.com/ansible-and-linode-what-i-learned-about-controlling-linodes-from-ansible)

* [Multi-factor SSH authentication with Ansible and Duo Security](http://jlafon.io/ansible-duo-security.html)

* [Introducing Ansible into Legacy Projects](http://benlopatin.com/getting-started-with-ansible/)

* [Post-install steps with Ansible](https://hvops.com/articles/ansible-post-install/)

* [6 practices for super smooth Ansible experience](http://hakunin.com/six-ansible-practices)

* [Create a Couchbase Cluster with Ansible](http://blog.couchbase.com/create-couchbase-cluster-with-ansible)

* [Idempotence, convergence, and other silly fancy words we often use](https://groups.google.com/forum/#!msg/Ansible-project/WpRblldA2PQ/lYDpFjBXDlsJ)

* [Testing with Jenkins, Docker and Ansible](http://blog.mist.io/post/82383668190/move-fast-and-dont-break-things-testing-with)


## Application dependencies learning checklist
1. Learn about configuration management in the context of deployment 
   automation and infrastructure-as-code.

1. Pick a configuration management tool and stick with it. My recommendation 
   is Ansible because it is by far the easiest tool to learn and use.

1. Read your configuration management tool's documentation and, when 
   necessary, the source code.

1. Automate the configuration management and deployment for your project. 
   Note that this is by far the most time consuming step in this 
   checklist but will pay dividends every time you deploy your project.

1. Hook the automated deployment tool into your existing deployment process.

