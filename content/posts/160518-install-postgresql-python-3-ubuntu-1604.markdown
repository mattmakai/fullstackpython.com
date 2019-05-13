title: Setting up PostgreSQL with Python 3 and psycopg on Ubuntu 16.04
slug: postgresql-python-3-psycopg2-ubuntu-1604 
meta: A guide for installing and using PostgreSQL with Python 3 and psycopg2 on Ubuntu 16.04 Xenial Xerus.
category: post
date: 2016-05-18
modified: 2017-12-25
newsletter: False
headerimage: /img/160518-postgresql-ubuntu-1604/header.jpg
headeralt: PostgreSQL and Ubuntu logos. Copyright their respective owners.


[PostgreSQL](/postgresql.html) is a powerful open source 
[relational database](/databases.html) frequently used to create, read,
update and delete [Python web application](/web-frameworks.html) data.
[Psycopg2](http://initd.org/psycopg/) is a PostgreSQL database 
driver that serves as a Python client for access to the PostgreSQL server. 
This post explains how to install PostgreSQL on [Ubuntu 16.04](/ubuntu.html) 
and run a few basic SQL queries within a Python program.

We won't cover 
[object-relational mappers (ORMs)](/object-relational-mappers-orms.html) 
in this tutorial but these steps can be used as a prerequisite to working 
with an ORM such as SQLAlchemy or Peewee.


## Tools We Need
Our walkthrough should work with either [Python 2 or 3](/python-2-or-3.html) 
although all the steps were tested specifically with Python 3.5. Besides 
the Python interpreter, here are the other components we'll use:

* [Ubuntu 16.04.2](http://releases.ubuntu.com/16.04/) (these 
  steps should also work fine with other Ubuntu versions)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle the
  [psycopg2](https://pypi.org/project/psycopg2/2.6.1) 
  [application dependency](/application-dependencies.html)
* [PostgreSQL](http://www.postgresql.org/)

If you aren't sure how to install pip and virtualenv, review the 
first few steps of the 
[how to set up Python 3, Bottle and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html)
guide.


## Install PostgreSQL
We'll install PostgreSQL via the `apt` package manager. There are a few
packages we need since we want to both run PostgreSQL and use the psycopg2
driver with our Python programs. PostgreSQL will also be installed as a
system service so we can start, stop and reload its configuration when
necessary with the `service` command. Open the terminal and run: 

    sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common

Enter your `sudo` password when prompted and enter 'yes' when `apt` asks
if you want to install the new packages.

<img src="/img/160518-postgresql-ubuntu-1604/apt-get-postgresql.png" width="100%" class="technical-diagram img-rounded">

After a few moments `apt` will finish downloading, installing and 
processing.

<img src="/img/160518-postgresql-ubuntu-1604/apt-get-postgresql-done.png" width="100%" class="technical-diagram img-rounded">

We now have PostgreSQL installed and the PostgreSQL service is running
in the background. However, we need to create a user and a database instance
to really start using it. Use the `sudo` command to switch to the new
"postgres" account.

    sudo -i -u postgres

Within the "postgres" account, create a user from the command line with the
`createuser` command. PostgreSQL will prompt you with several questions.
Answer "n" to superuser and "y" to the other questions.

    createuser matt -P --interactive
    
<img src="/img/160518-postgresql-ubuntu-1604/createuser.png" width="100%" class="technical-diagram img-rounded">

Awesome, now we have a PostgreSQL user that matches our Ubuntu login
account. Exit out of the postgres account by pressing the "Ctrl" key along
with "d" into the shell. We're back in our own user account.

Create a new database we can use for testing. You can name it "testpython"
or whatever you want for your application.

    createdb testpython

Now we can interact with "testpython" via the PostgreSQL command line tool.


## Interacting with PostgreSQL
The `psql` command line client is useful for connecting directly to our
PostgreSQL server without any Python code. Try out `psql` by using this
command at the prompt: 

    psql testpython

The PostgreSQL client will connect to the localhost server. The client is
now ready for input:

<img src="/img/160518-postgresql-ubuntu-1604/postgresql-cli.png" width="100%" class="technical-diagram img-rounded">

Try out PostgreSQL's command prompt a try with commands such as `\dt` and
`\dd`. We can also run SQL queries such as "SELECT * from testpython", 
although that won't give us back any data yet because we have not inserted
any into the database. A full list of PostgreSQL commands can be 
found in the
[psql documentation](http://www.postgresql.org/docs/9.6/static/app-psql.html).


## Installing psycopg2
Now that PostgreSQL is installed and we have a non-superuser account, we
can install the [psycopg2](http://initd.org/psycopg/) package. Let's
figure out where our `python3` executable is located, create a virtualenv
with `python3`, activate the virtualenv and then install the psycopg2 package
with `pip`. Find your `python3` executable using the `which` command.
 
    which python3

We will see output like what is in this screenshot.

<img src="/img/160518-postgresql-ubuntu-1604/which-python-3.png" width="100%" class="technical-diagram img-rounded">

Create a new virtualenv in either your home directory or wherever you
store your Python virtualenvs. Specify the full path to your `python3`
installation. 


    # specify the system python3 installation
    virtualenv --python=/usr/bin/python3 venvs/postgrestest

Activate the virtualenv.

    source ~/venvs/postgrestest/bin/activate

Next we can install the psycopg2 Python package from 
[PyPI](https://pypi.python.org/pypi) using the `pip` command.

    pip install psycopg2

<img src="/img/160518-postgresql-ubuntu-1604/pip-install-psycopg2.png" width="100%" class="technical-diagram img-rounded">

Sweet, we've got our PostgreSQL driver installed in our virtualenv! We can 
now test out the installation by writing a few lines of Python code.


## Using PostgreSQL from Python
Launch the Python REPL with the `python` or `python3` command. You can also 
write the following code in a Python file such as "testpostgres.py" then
execute it with `python testpostgres.py`. Make sure to replace the "user"
and "password" values with your own.

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
        conn.commit() # <--- makes sure the change is shown in the database
        rows = cursor.fetchall()
        print(rows)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

When we run the above code we won't get anything fancy, just an empty
list printed out. However, in those few lines of code we've ensured our 
connection to our new database works and we can create new tables in it as 
well as query them.

<img src="/img/160518-postgresql-ubuntu-1604/output.png" width="100%" class="technical-diagram img-rounded">

That's just enough of a hook to get started writing more complicated SQL 
queries using psycopg2 and PostgreSQL. Make sure to check out the 
[PostgreSQL](/postgresql.html),
[relational databases](/databases.html) and 
[object-relational mappers (ORMs)](/object-relational-mappers-orms.html)
pages for more tutorials.

Questions? Tweet [@fullstackpython](https://twitter.com/fullstackpython)
or post a message on the 
[Full Stack Python Facebook page](https://www.facebook.com/fullstackpython). 

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160518-install-postgresql-python-3-ubuntu-1604.markdown)
and submit a pull request.
