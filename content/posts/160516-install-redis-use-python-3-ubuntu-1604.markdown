title: How to Use Redis with Python 3 and redis-py on Ubuntu 16.04
slug: install-redis-use-python-3-ubuntu-1604 
meta: Step-by-step instructions to install Redis and use it with Python 3 and redis-py on Ubuntu 16.04 Xenial Xerus.
category: post
date: 2016-05-16
modified: 2017-04-28
newsletter: False
headerimage: /img/160516-redis-ubuntu-1604/header.jpg
headeralt: Redis and Ubuntu logos. Copyright their respective owners.


[Redis](/redis.html) is an in-memory key-value pair 
[NoSQL data store](/no-sql-datastore.html) often used 
for [web application](/web-frameworks.html) sessions,
transient [data](/data.html) and as a broker for 
[task queues](/task-queues.html). redis-py is a common Python code 
library for interacting with Redis. Let's learn how to get Redis up
and running on [Ubuntu](/ubuntu.html) and then start using it in a simple 
Python application.


## Tools We Need
This tutorial is tested with Python 3.5 but either 
[Python 2 or 3](/python-2-or-3.html) should work for everything written 
here. Just make sure one version is installed on your system by going to 
the terminal and typing `python --version`. Other than Python itself,
here is the software we are going to use throughout the rest of this post:

* [Ubuntu 16.04](http://releases.ubuntu.com/16.04/) (these 
  instructions should work fine with earlier Ubuntu versions as well)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle the
  redis-py [application dependency](/application-dependencies.html)
* [Redis](http://redis.io)
* [redis-py](https://redis-py.readthedocs.io/en/latest/)

If you aren't sure how how to install pip and virtualenv, review the 
first few steps of the 
[how to set up Python 3, Flask and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
guide.


## Install Redis
There are a few ways to install Redis, such as 
[downloading and compiling from source](http://redis.io/topics/quickstart).
However, on Ubuntu we can install a system package through `apt`. The
advantage of this method is that the `apt` process will take care of 
installing `redis-server` as a system service. Open the terminal and run 
the following command:

    sudo apt-get install redis-server

Enter your `sudo` password and when you are prompted whether you want 
to install the new package enter 'yes'.

<img src="/img/160516-redis-ubuntu-1604/apt-get-redis.png" width="100%" class="technical-diagram img-rounded">

After a few moments the downloading and processing should be complete
and you will be back at the prompt.

<img src="/img/160516-redis-ubuntu-1604/apt-get-redis-done.png" width="100%" class="technical-diagram img-rounded">

Redis is now installed and the Redis server is running in the background 
as a system service. Even though we installed the `redis-server` package,
the installation also comes with the Redis command line client. The client
is useful for connecting directly to the Redis server without any Python
code. Give `redis-cli` a try by typing this into the command prompt:

    redis-cli

The Redis client connects to the localhost server and gives a new prompt
to show it's ready for commands:

<img src="/img/160516-redis-ubuntu-1604/redis-cli.png" width="100%" class="technical-diagram img-rounded">

Give the prompt a try by using Redis commands such as `keys *` or `set a 1`.
The full list of Redis commands is provided in the 
[project documentation](http://redis.io/commands).


## Virtualenv and Install redis-py
We need to figure out our `python3` location, then create a virtualenv,
activate the virtualenv and then install redis-py with `pip`.
Determine your `python3` executable location with the `which` command.
 
    which python3

You'll see some output like the following screenshot.

<img src="/img/160516-redis-ubuntu-1604/which-python-3.png" width="100%" class="technical-diagram img-rounded">

Create a new virtualenv either in your home directory or wherever you
store your project virtualenvs. Specify the full path to your `python3`
installation. 


    # specify the system python3 installation
    virtualenv --python=/usr/bin/python3 venvs/redistest

Activate the virtualenv.

    source ~/venvs/redistest/bin/activate

Next we can install the redis-py Python package from 
[PyPI](https://pypi.python.org/pypi) using the `pip` command.

    pip install redis

<img src="/img/160516-redis-ubuntu-1604/pip-install-redis.png" width="100%" class="technical-diagram img-rounded">

Alright, now it is installed in our virtualenv. Let's write some simple 
Python code to try out give redis-py!


## Working with Redis from Python
Fire up the Python REPL with the `python` or `python3` command. You can also 
write the following code in a Python file such as "testredis.py" then
execute it with `python testredis.py`.

    import redis
    # create a connection to the localhost Redis server instance, by
    # default it runs on port 6379
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
    # see what keys are in Redis
    redis_db.keys()
    # output for keys() should be an empty list "[]"
    redis_db.set('full stack', 'python')
    # output should be "True"
    redis_db.keys()
    # now we have one key so the output will be "[b'full stack']"
    redis_db.get('full stack')
    # output is "b'python'", the key and value still exist in Redis
    redis_db.incr('twilio')
    # output is "1", we just incremented even though the key did not
    # previously exist
    redis_db.get('twilio')
    # output is "b'1'" again, since we just obtained the value from
    # the existing key
    redis_db.delete('twilio')
    # output is "1" because the command was successful
    redis_db.get('twilio')
    # nothing is returned because the key and value no longer exist

That is a quick introduction to some commonly-used Redis commands
invoked by their Python bindings through the redis-py library. Take a look 
at the 
[redis-py official documentation](https://redis-py.readthedocs.io/en/latest/)
to learn more about the extensive command list you can use to create,
read, modify and delete keys and values in Redis.

Questions? Tweet [@fullstackpython](https://twitter.com/fullstackpython)
or post a message on the 
[Full Stack Python Facebook page](https://www.facebook.com/fullstackpython). 
See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160516-install-redis-use-python-3-ubuntu-1604.markdown)
and submit a pull request.
