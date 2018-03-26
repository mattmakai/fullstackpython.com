title: Ansible
category: page
slug: ansible
sortorder: 0533
toc: False
sidebartitle: Ansible
meta: Ansible is configuration management tool used for application deployment and environment setup.


# Ansible
[Ansible](http://docs.ansible.com/ansible/latest/index.html) is 
[configuration management tool](/configuration-management.html) used for 
[application deployment](/deployment.html) and 
[environment setup](/development-environments.html).

<a href="http://docs.ansible.com/ansible/latest/index.html"><img src="/img/logos/ansible-wide.png" width="100%" alt="Official Ansible logo. Copyright Redhat." class="technical-diagram"></a>


### Example Ansible playbooks
Ansible is far easier to learn when you can read how more full-featured 
playbooks are built using many tasks. An interesting note from my own 
experience is that when you get more experienced using Ansible there are
many shortcuts in the task syntax so you can often make playbooks that have
fewer lines of code than when you were less experienced yet the readability
does not suffer. 

Check out some of these example playbooks to learn more about how you may
be able to structure your playbooks:

* The 
  [prod directory](https://github.com/mattmakai/fsp-deployment-guide/tree/master/prod) 
  under the 
  [Full Stack Python Deployment Guide open source project code](https://github.com/mattmakai/fsp-deployment-guide)
  contains a full playbook for deploying a standard [Nginx](/nginx.html),
  [Gunicorn](/green-unicorn-gunicorn.html) and [PostgreSQL](/postgresql.html)
  stack.

* [mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook)
  configures macOS with various applications and developer tools such as
  [Docker](/docker.html), Homebrew and [Sublime Text](/sublime-text.html).
  
* [ansible-nginx-haproxy-elasticsearch](https://github.com/gp187/ansible-nginx-haproxy-elasticsearch)
  sets up a server with [Nginx](/nginx.html), HAProxy and ElasticSearch.


### Specific Ansible topics
* [Using Ansible for deploying serverless applications](https://opensource.com/article/17/8/ansible-serverless-applications)
  provides a short overview with an example playbook how Ansible can also
  be useful for configuring [serverless](/serverless.html) applications.

* [DevOps from Scratch, Part 1: Vagrant & Ansible](https://www.kevinlondon.com/2016/09/19/devops-from-scratch-pt-1.html)

* [Ansible: Post-Install Setup](https://valdhaus.co/writings/ansible-post-install/)

* [Managing Docker containers with Ansible](https://linuxacademy.com/howtoguides/posts/show/topic/13750-managing-docker-containers-with-ansible)

* [How To Use Vault to Protect Sensitive Ansible Data on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-use-vault-to-protect-sensitive-ansible-data-on-ubuntu-16-04)

* [How to use Ansible Variables and Vaults](https://www.expressvpn.com/blog/ansible-variables-vaults/)

* [CI for Ansible playbooks which require Ansible Vault protected variables](https://www.jeffgeerling.com/blog/2017/ci-ansible-playbooks-which-require-ansible-vault-protected-variables)

* [How to use Ansible to manage PostgreSQL](https://opensource.com/article/17/6/ansible-postgresql-operations)

* [Deploy A Replicated MongoDB instance on AWS with Terraform and Ansible](https://blog.eleven-labs.com/en/deploy-a-replicated-mongodb-on-aws-with-terraform-and-ansible/)

