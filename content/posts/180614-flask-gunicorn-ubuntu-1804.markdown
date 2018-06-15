title: Configure Python 3, Flask and Gunicorn on Ubuntu 18.04 LTS
slug: python-3-flask-gunicorn-ubuntu-1804-bionic-beaver
meta: Instructions for configuring Ubuntu 18.04 Bionic Beaver with Python 3, Flask and Green Unicorn (Gunicorn).
category: post
date: 2018-06-14
modified: 2018-06-15
newsletter: False
headerimage: /img/180614-ubuntu-flask-gunicorn/header.jpg
headeralt: Flask, Green Unicorn and Ubuntu logos. Copyright their respective owners.


[Ubuntu Linux's](/ubuntu.html) latest Long Term Support (LTS)
[operating system](/operating-systems.html) version is 
[18.04](http://releases.ubuntu.com/18.04/) and was released in April 2018.
The 18.04 update is code named "Bionic Beaver" and it includes
[Python 3](/python-2-or-3.html) by default. However, there are bunch of
dependencies you will need to install to get this release set up as a 
[development environment](/development-environments.html).

In this tutorial we will get Python 3.6 configured with development system
packages to start a new [Flask](/flask.html) web application project and 
run it with [Green Unicorn (Gunicorn)](/green-unicorn-gunicorn.html).


## Our Tools
Our project will use the Ubuntu 18.04 release along with a few other 
libraries. Note that if you are using the older 16.04 LTS release, there
is also 
[a guide that will walk you through setting up that version](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
as your development environment.

We will install the following tools as we step through the rest of 
the sections in this tutorial:

* [Ubuntu 18.04 LTS (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
* [Python](/why-use-python.html) version 
  [3.6.5](https://docs.python.org/3/whatsnew/3.6.html) 
  (default in Ubuntu 18.04)
* [Flask](/flask.html) web framework version 
  [1.0.2](http://flask.pocoo.org/docs/1.0/changelog/#version-1-0-2)
* [Green Unicorn (Gunicorn)](/green-unicorn-gunicorn.html) version 
  [19.8.1](http://docs.gunicorn.org/en/stable/news.html)

If you're running on Mac OS X or Windows, use virtualization software such
as [Parallels](https://www.parallels.com/products/desktop/) or
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) with the 
[Ubuntu .iso file](http://releases.ubuntu.com/18.04/). Either the amd64 or
i386 version for 18.04 will work. I am using amd64 for development and testing
in this tutorial.

When you boot up to the Ubuntu desktop you should see a screen like this one.

<img src="/img/180614-ubuntu-flask-gunicorn/ubuntu-desktop.jpg" width="100%" class="shot rnd outl">

We're ready to get our development environment configured.


## System Packages
Open up a terminal window to proceed with the setup.

Use the following two commands to check which version of Python 3 is installed

```bash
python3 --version
which python3
```

The Python version should be 3.6.5 and the location `/usr/bin/python3`.

Our Ubuntu installation requires a few system packages to do development
rather than just run Python scripts. Run the following `apt-get` command
and enter your `sudo` password to allow restricted system access.

```bash
sudo apt-get install python3-dev python3-pip python3-virtualenv
```

We should see the following prompt requesting `sudo` access. Enter `y` to 
let the system package manager complete the installation.

```bash
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-4.15.0-20 linux-headers-4.15.0-20-generic
  linux-image-4.15.0-20-generic linux-modules-4.15.0-20-generic
  linux-modules-extra-4.15.0-20-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  dh-python libexpat1-dev libpython3-dev libpython3.6-dev python3-setuptools
  python3-wheel python3.6-dev
Suggested packages:
  python-setuptools-doc
The following NEW packages will be installed:
  dh-python libexpat1-dev libpython3-dev libpython3.6-dev python3-dev
  python3-pip python3-setuptools python3-virtualenv python3-wheel
  python3.6-dev
0 upgraded, 10 newly installed, 0 to remove and 11 not upgraded.
Need to get 3,617 kB/3,661 kB of archives.
After this operation, 20.2 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
```

The package manager will do the dirty work and should report when the
installation finishes successfully.

```bash
(...clipped a bunch of installation lines for brevity...)
Unpacking python3-wheel (0.30.0-0.2) ...
Setting up python3-wheel (0.30.0-0.2) ...
Setting up python3-virtualenv (15.1.0+ds-1.1) ...
Setting up python3-pip (9.0.1-2.3~ubuntu1) ...
Setting up libexpat1-dev:amd64 (2.2.5-3) ...
Processing triggers for man-db (2.8.3-2) ...
Setting up python3-setuptools (39.0.1-2) ...
Setting up dh-python (3.20180325ubuntu2) ...
Setting up libpython3.6-dev:amd64 (3.6.5-3) ...
Setting up python3.6-dev (3.6.5-3) ...
Setting up libpython3-dev:amd64 (3.6.5-3) ...
Setting up python3-dev (3.6.5-3) ...
```

The packages we need are now installed. We can continue on to install our 
Python-specific dependencies.


## Virtual environment
We installed [virtualenv](https://virtualenv.pypa.io/en/latest/) 
and [pip](https://pypi.org/project/pip) to handle our 
[application dependencies](/application-dependencies.html).
We can now use them to download and install Flask and Gunicorn.


Create a directory to store your virtualenvs. Then create a new virtualenv
within that directory.

```bash
# make sure pip and setuptools are the latest version
pip3 install --upgrade pip setuptools
# the tilde ("~") specifies the user's home directory, such as "/home/matt"
cd ~
mkdir venvs
# specify the system python3 installation
python3 -m venv venvs/flask1804
```

Activate the virtualenv.

```bash
source ~/venvs/flask1804/bin/activate
```

Our prompt will change when the virutalenv is activated.

<img src="/img/180614-ubuntu-flask-gunicorn/venv-activated.jpg" width="100%" class="shot rnd outl">

Our virtualenv is now activated with Python 3. We can install any
dependencies we need such as Flask and Gunicorn.


## Flask and Gunicorn
We're going to use `pip` within our new virtualenv but it's a good
idea to update it to the latest version. We should also install the
`wheel` package to remove installation warnings when `pip` tries to
use [Python wheels](https://pythonwheels.com/), which are the newest 
standard in an admittedly long line of Python distribution package
models.

```bash
pip install --upgrade pip
pip install wheel
```

We can now install Flask and Green Unicorn via the `pip` command.

```bash
pip install flask gunicorn
```

Look for output similar to the following to ensure the libraries installed
without an issue.

```bash
(flask1804) matt@ubuntu:~$ pip install flask gunicorn
Collecting flask
  Using cached https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl
Collecting gunicorn
  Using cached https://files.pythonhosted.org/packages/55/cb/09fe80bddf30be86abfc06ccb1154f97d6c64bb87111de066a5fc9ccb937/gunicorn-19.8.1-py2.py3-none-any.whl
Collecting click>=5.1 (from flask)
  Using cached https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl
Collecting Werkzeug>=0.14 (from flask)
  Using cached https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl
Collecting itsdangerous>=0.24 (from flask)
  Using cached https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz
Collecting Jinja2>=2.10 (from flask)
  Using cached https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10->flask)
  Using cached https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
Building wheels for collected packages: itsdangerous, MarkupSafe
  Running setup.py bdist_wheel for itsdangerous ... done
  Stored in directory: /home/matt/.cache/pip/wheels/2c/4a/61/5599631c1554768c6290b08c02c72d7317910374ca602ff1e5
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: /home/matt/.cache/pip/wheels/33/56/20/ebe49a5c612fffe1c5a632146b16596f9e64676768661e4e46
Successfully built itsdangerous MarkupSafe
Installing collected packages: click, Werkzeug, itsdangerous, MarkupSafe, Jinja2, flask, gunicorn
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-1.0.2 gunicorn-19.8.1 itsdangerous-0.24
```

Create a new directory named `flask1804` under your home directory (not
within the `venvs` subdirectory) that will store our Flask test project. 
Change directory into the new folder.

```bash
mkdir ~/flask1804
cd ~/flask1804
```

Create a new file named `__init__.py` within our `flaskproj` directory so
we can test to make sure Flask is working properly. I usually use
[Vim](/vim.html) but [Emacs](/emacs.html) and other 
[development environments](/development-environments.html) work great as
well.

Within `__init__.py` write the following code.

```python
from flask import Flask, Response


app = Flask(__name__)

@app.route("/")
def index():
	return Response("It works!"), 200

if __name__ == "__main__":
	app.run(debug=True)
```


We could run our app with the Flask development server using the 
`python __init__.py` command. Instead run the Flask app with
Gunicorn. Go to the directory above the `flask1804` folder, in our
case we can enter `cd ~` then use the `gunicorn` command:

```bash
gunicorn flask1804.app:app
```

We should see:

```bash
[2018-06-15 15:54:31 -0400] [5174] [INFO] Starting gunicorn 19.8.1
[2018-06-15 15:54:31 -0400] [5174] [INFO] Listening at: http://127.0.0.1:8000 (5174)
[2018-06-15 15:54:31 -0400] [5174] [INFO] Using worker: sync
[2018-06-15 15:54:31 -0400] [5177] [INFO] Booting worker with pid: 5177
```

Great now we can bring up our shell Flask app in the web browser at
the `localhost:8000` or `127.0.0.1:8000` address.

<img src="/img/180614-ubuntu-flask-gunicorn/it-works.jpg" width="100%" class="shot rnd outl">

Now you're ready for some real [Flask](/flask.html) development!


## Ready to Code
That provides a quick configuration for getting started on 18.04 LTS 
developing [Flask](/flask.html) applications with the 
[Gunicorn](/green-unicorn-gunicorn.html) [WSGI server](/wsgi-servers.html).

Next up you should check out the following tutorials that use this 
Flask configuration:

* [Responding to SMS Text Messages with Python & Flask](/blog/respond-sms-text-messages-python-flask.html)
* [How to Add Hosted Monitoring to Flask Web Applications](/blog/hosted-monitoring-flask-web-apps.html))

Alternatively you can also determine what to code next in your Python 
project by reading the 
[Full Stack Python table of contents page](/table-of-contents.html).

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/180614-flask-gunicorn-ubuntu-1804.markdown)
and submit a pull request.
