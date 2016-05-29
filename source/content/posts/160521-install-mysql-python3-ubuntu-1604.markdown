title: How to Install and Use MySQL with Python 3 on Ubuntu 16.04
slug: mysql-python-3-psycopg2-ubuntu-1604 
meta: A tutorial to install and use MySQL with Python 3 and mysqlclient on Ubuntu 16.04 Xenial Xerus.
category: post
date: 2016-05-21


[MySQL](/mysql.html) is a common open source 
[relational database](/databases.html) for creating, reading, updating 
and deleting data in [Python web applications](/web-frameworks.html).
[mysqlclient](https://pypi.python.org/pypi/mysqlclient) is a MySQL database 
driver that serves as a Python client for access to the MySQL server. 
Let's learn how to install MySQL on Ubuntu 16.04 and then run a few 
SQL queries within a Python program.

We will not go over
[object-relational mappers (ORMs)](/object-relational-mappers-orms.html) 
but these steps can be used as a prerequisite to working with an ORM such 
as SQLAlchemy or Peewee.


## Tools We Need
Our walkthrough should work with either [Python 2 or 3](/python-2-or-3.html) 
because mysqlclient is a Python 3-enhanced fork of the Python 2-only 
[MySQLdb](https://pypi.python.org/pypi/MySQL-python) driver. Other than 
the Python interpreter, we will also use these components:

* [Ubuntu 16.04](http://releases.ubuntu.com/16.04/) (this tutorial 
  should also work on other Ubuntu versions)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle the
  [mysqlclient](https://mysqlclient.readthedocs.io/en/latest/) 
  [application dependency](/application-dependencies.html)
* [MySQL](http://dev.mysql.com/doc/)

If you aren't sure how how to install pip and virtualenv, review the 
first few steps of the 
[how to set up Python 3, Django and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html)
guide.


## Install MySQL
We can install MySQL by using the `apt` package manager. First make sure
your packages list are up to date. Open the terminal and run this `apt`
command.

    sudo apt-get update

We need to install the `mysql-server` package, which downloads the required
files, configures the initial database set up and handles running MySQL
as a system service. Run this `apt` command to get the process started.

    sudo apt-get install mysql

Enter 'y' when prompted with whether or not you want to install the
new package.

<img src="/source/static/img/160528-mysql-ubuntu-1604/apt-install-prompt.png" width="100%" class="technical-diagram img-rounded">

An administrative screen asking for a new root password will appear in the 
middle of the package installation process. Enter your chosen new password 
twice and the installation will continue.

<img src="/source/static/img/160528-mysql-ubuntu-1604/new-root-password.png" width="100%" class="technical-diagram img-rounded">

In a moment the installation will finish and you'll be back at the command
prompt.

<img src="/source/static/img/160528-mysql-ubuntu-1604/apt-finished.png" width="100%" class="technical-diagram img-rounded">

MySQL is now installed with a root user. However, default settings for a 
MySQL installation are configured for development and leave open many
security holes in production environments. Run the `mysql_secure_installation` 
command to plug some of the most glaring security concerns.
    
    sudo mysql_secure_installation

When you run the command you'll be asked several questions. If you're working
on a development or test server you may want to leave one or more settings
in their default values. In a production environment though you should most
likely specify yes to every question.

After you run through the `mysql_secure_installation` program you can have
it immediately reload the MySQL privilege tables and then you'll be back
at the command prompt.

<img src="/source/static/img/160528-mysql-ubuntu-1604/mysql-secure-installation.png" width="100%" class="technical-diagram img-rounded">

We do not yet have any non-root MySQL accounts for our applications to use
to connect to our databases.


## Creating MySQL Users


    mysql -u root -p

## Installing mysqlclient


## What's next?



## Using MySQL from Python
Start the Python REPL with the `python` or `python3` command. You can also 
write the following code in a Python file such as "test\_mysql.py" then
execute it with `python test_mysql.py`. Make sure to replace the "user"
and "password" strings with your own values.

    import psycopg2

    try:
        connect_str = "dbname='testpython' user='matt' host='localhost' " + \
                      "password='myOwnPassword'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # create a new table with a single column called "name"
        cursor.execute("""CREATE TABLE tutorials (name char(40));""")
        # run a SELECT statement - no data in there, but we can try it
        cursor.execute("""SELECT * from tutorials""")
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

When we run the above code we won't get anything fancy, just an empty
list printed out. However, in those few lines of code we've ensured our 
connection to our new database works and we can create new tables in it as 
well as query them.

<img src="/source/static/img/160518-postgresql-ubuntu-1604/output.png" width="100%" class="technical-diagram img-rounded">

That's just enough of a hook to get started writing more complicated SQL 
queries using psycopg2 and PostgreSQL. Make sure to check out the 
[PostgreSQL](/postgresql.html),
[relational databases](/databases.html) and 
[object-relational mappers (ORMs)](/object-relational-mappers-orms.html)
pages for more tutorials.

Questions? Tweet [@fullstackpython](https://twitter.com/fullstackpython)
or post a message on the 
[Full Stack Python Facebook page](https://www.facebook.com/fullstackpython). 
Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/makaimc/fullstackpython.com/blob/gh-pages/source/content/posts/160518-install-postgresql-python-3-ubuntu-1604.markdown).

