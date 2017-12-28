title: How to Install and Use MySQL on Ubuntu 16.04
slug: install-mysql-ubuntu-1604 
meta: A quick tutorial to install and use MySQL on Ubuntu 16.04 Xenial Xerus.
category: post
date: 2016-05-28
modified: 2017-12-22
newsletter: False
headerimage: /img/160528-mysql-ubuntu-1604/header.jpg
headeralt: MySQL and Ubuntu logos. Copyright their respective owners.


[MySQL](/mysql.html) is a common open source 
[relational database](/databases.html) for creating, reading, updating 
and deleting data in [Python web applications](/web-frameworks.html).
Let's learn how to install MySQL on [Ubuntu 16.04](/ubuntu.html) and then 
run a few SQL queries within the command line client.

We will not go over connecting via Python applications using
[object-relational mappers (ORMs)](/object-relational-mappers-orms.html) 
but these steps can be used as a prerequisite to working with an ORM such 
as SQLAlchemy or Peewee.


## Tools We Need
In this tutorial we'll use the following components:

* [Ubuntu 16.04.2](http://releases.ubuntu.com/16.04/) (this tutorial 
  should also work on other Ubuntu versions)
* [MySQL](http://dev.mysql.com/doc/)


## Install MySQL
We can install MySQL by using the `apt` package manager. First make sure
your packages list are up to date. Open the terminal and run this `apt`
command.

    sudo apt-get update

We need to install the `mysql-server` package, which downloads the required
files, configures the initial database set up and handles running MySQL
as a system service. Run this `apt` command to get the process started.

    sudo apt-get install mysql-server

Enter 'y' when prompted with whether or not you want to install the
new package.

<img src="/img/160528-mysql-ubuntu-1604/apt-install-prompt.png" width="100%" class="technical-diagram img-rounded">

An administrative screen asking for a new root password will appear in the 
middle of the package installation process. Enter your chosen new password 
twice and the installation will continue.

<img src="/img/160528-mysql-ubuntu-1604/new-root-password.png" width="100%" class="technical-diagram img-rounded">

In a moment the installation will finish and you'll be back at the command
prompt.

<img src="/img/160528-mysql-ubuntu-1604/apt-finished.png" width="100%" class="technical-diagram img-rounded">

MySQL is now installed with a root user. However, we do not want to have our
applications connect to the database with that user, so next we will 
create a new non-root user.


## Securing MySQL
MySQL is installed with a basic configuration meant for development and testing
purposes. However, the configuration is not secure for production enviroments,
therefore it comes with a utility to handle basic security. Run the
following command and answer the questions based on your environment 
requirements.

    sudo mysql_secure_installation

When you finish running the script you should see the following output and
be back at the command prompt.

<img src="/img/160528-mysql-ubuntu-1604/mysql-secure-installation.png" width="100%" class="technical-diagram img-rounded">

Our MySQL instance has basic security in place but we need to create a 
non-root user for applications to interact with the database.


## Creating MySQL Users
To create a non-root user, connect to the MySQL instance with the 
`mysql` command line client.

    mysql -u root -p

Now use the `CREATE USER` command to generate a new user. Make sure to
change "mynewuser" and "goodPassword" with your own values.

    CREATE USER 'mynewuser'@'localhost' IDENTIFIED BY 'goodPassword';

No output after the command is good - that means the command succeeded.

<img src="/img/160528-mysql-ubuntu-1604/create-user.png" width="100%" class="technical-diagram img-rounded">

We need to apply privileges to the new user so it can handle basic database
operations. Again, make sure to replace the default username in this command
with your new username.

    GRANT ALL PRIVILEGES ON * . * TO 'mynewuser'@'localhost';

<img src="/img/160528-mysql-ubuntu-1604/grant-all.png" width="100%" class="technical-diagram img-rounded">

It's a good idea to reload the privileges to make sure our new user's
permissions are in place.

    FLUSH PRIVILEGES;

Now that our permissions are reloaded we can connect with the new user.


## New User Connection
We're set to connect to the database with our new user. Exit the MySQL
client with "Ctrl-d". Reconnect using a slightly different command than
we used earlier.
    
    mysql -u mynewuser -p

<img src="/img/160528-mysql-ubuntu-1604/mysql-new-user.png" width="100%" class="technical-diagram img-rounded" alt="Connect to MySQL as the new user we just created.">

Create a new database with the `CREATE DATABASE` command.

    CREATE DATABASE fullstackpython;


<img src="/img/160528-mysql-ubuntu-1604/create-database.png" width="100%" class="technical-diagram img-rounded" alt="Create a new MySQL database with our new user.">

Connect to the new database with the `USE` command.

    use fullstackpython;


<img src="/img/160528-mysql-ubuntu-1604/use-command.png" width="100%" class="technical-diagram img-rounded" alt="Connect to the newly-created database with the USE command.">

Create a simple new table with the `CREATE TABLE` command.

    CREATE TABLE pages (name VARCHAR(50), url VARCHAR(1024));


Our table is ready to go - we can interact with it using the 
`SELECT`, `INSERT`, `UPDATE` and `DELETE` SQL commands.


## What's next?
We now have our MySQL instance installed and ready for interaction.
Take a look at the [MySQL](/mysql.html), 
[relational databases](/databases.html) and 
[object-relational mappers (ORMs)](/object-relational-mappers-orms.html)
pages for more tutorials.

Questions? Tweet [@fullstackpython](https://twitter.com/fullstackpython)
or post a message on the 
[Full Stack Python Facebook page](https://www.facebook.com/fullstackpython). 

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160528-install-mysql-ubuntu-1604.markdown)
and submit a pull request.
