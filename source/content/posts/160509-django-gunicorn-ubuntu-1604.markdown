title: Setting up Python 3, Django and Gunicorn on Ubuntu 16.04 LTS
slug: python-3-django-gunicorn-ubuntu-1604-xenial-xerus
meta: Step-by-step instructions for developing on Ubuntu 16.04 with Python 3, Django and Green Unicorn (Gunicorn).
category: post
date: 2016-05-09
headerimage: /source/static/img/160509-ubuntu-django-gunicorn/header.jpg
headeralt: Django, Green Unicorn and Ubuntu logos. Copyright their respective owners.


[Ubuntu](/ubuntu.html) released the newest Long Term Support (LTS) 
version of its [operating system](/operating-systems.html) in April 2016. 
The update brings Ubuntu to version 16.04 and its latest code name is 
"Xenial Xerus". 16.04 is the first Ubuntu release to include 
[Python 3](/python-2-or-3.html) as the default Python installation.

Let's use this newest Ubuntu release along with Python version 3.5 to 
start a new [Django](/django.html) web application project and run it with 
[Green Unicorn (Gunicorn)](/green-unicorn-gunicorn.html).


## Tools We'll Need
We will need a few tools to complete our project. Don't worry about 
installing these just yet as we'll get to them as we progress through the
tutorial. The tools and their current versions as of May 9, 2016 are:

* [Ubuntu 16.04 LTS (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
* [Python](/why-use-python.html) version 
  [3.5](https://docs.python.org/3/whatsnew/3.5.html) 
  (default in Ubuntu 16.04)
* [Django](/django.html) web framework version 
  [1.9.6](https://docs.djangoproject.com/en/1.9/releases/1.9/)
* [Green Unicorn (Gunicorn)](/green-unicorn-gunicorn.html) version 
  [19.4](http://docs.gunicorn.org/en/stable/news.html)

If you're running on Mac OS X or Windows, use virtualization software such
as [Parallels](https://www.parallels.com/products/desktop/) 
(this is what I use, but it's Mac OS X-only) or 
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) with the 
[Ubuntu .iso file](http://releases.ubuntu.com/16.04/). Either the amd64 or
i386 version of 16.04 is fine, but I use amd64 for development and testing
in this blog post.

When we boot up for the first time, we should see a desktop screen like this 
one.

<img src="/source/static/img/160509-ubuntu-django-gunicorn/ubuntu-desktop.jpg" width="100%" class="technical-diagram img-rounded">

Open up terminal to proceed with the setup.


## System Packages
We can see the python3 version Ubuntu comes with, as well as where its
executable is stored.

    python3 --version
    which python3

<img src="/source/static/img/160509-ubuntu-django-gunicorn/which-python.png" width="100%" class="technical-diagram img-rounded">

Our Ubuntu installation first needs system packages for Python development.
You'll be prompted for your superuser password because restricted system
access is required to install packages through apt.

    sudo apt-get install virtualenv python-pip python3-dev

<img src="/source/static/img/160509-ubuntu-django-gunicorn/install-packages.png" width="100%" class="technical-diagram img-rounded">

Enter `y` and let the system package installation process run.

<img src="/source/static/img/160509-ubuntu-django-gunicorn/packages-installed.png" width="100%" class="technical-diagram img-rounded">

The basic system packages we need are now installed so we can proceed to
our Python-specific dependencies.


## Virtualenv
Virtualenv and pip for isolating and handling 
[application dependencies](/application-dependencies.html) were just 
installed via system packages so we can now use them to obtain Django and 
Gunicorn.


Create a directory to store virtualenvs then put a new virtualenv in it.

    # the tilde "~" specifies the user's home directory, like /home/matt
    cd ~
    mkdir venvs
    # specify the system python3 installation
    virtualenv --python=/usr/bin/python3 venvs/djproject

Activate the virtualenv.

    source ~/venvs/djproject/bin/activate

We should see our prompt change so that we know the virtualenv is properly 
activated.

<img src="/source/static/img/160509-ubuntu-django-gunicorn/venv-activated.png" width="100%" class="technical-diagram img-rounded">

Our virtualenv with Python 3 is activated so we can install whatever
dependencies we want, such as Django and Gunicorn. 


## Django and Gunicorn
Time to install Django and Green Unicorn into our virtualenv.

    pip install django gunicorn    


No errors is a good sign everything worked for us.

<img src="/source/static/img/160509-ubuntu-django-gunicorn/good-sign.png" width="100%" class="technical-diagram img-rounded">


Create a new Django project named `djproject`, or whatever you want to name
your project. Then change into the directory for the new project.

    django-admin startproject djproject
    cd djproject


We could run Django with the development server using the 
`python manage.py runserver` command. However, start Django up with
Gunicorn instead.

    gunicorn djproject.wsgi

<img src="/source/static/img/160509-ubuntu-django-gunicorn/gunicorn-run.png" width="100%" class="technical-diagram img-rounded">

Awesome, now we can bring up our shell project in the web browser at
the `localhost:8000` or `127.0.0.1:8000` address.

<img src="/source/static/img/160509-ubuntu-django-gunicorn/it-worked.jpg" width="100%" class="technical-diagram img-rounded">

Ready for development!


## Ready for Development
Those are the basics for starting development with Django and Gunicorn on 
Ubuntu 16.04. If you need an even more in-depth step-by-step tutorial to 
deploy your Python web application to a production environment, check out the 
[Full Stack Python Guide to Deployments book](http://www.deploypython.com/).

To figure out what to do next for your Python project, read the topics 
found on the [table of contents](/table-of-contents.html) page.

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [makaimc](https://github.com/makaimc).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/makaimc/fullstackpython.com/blob/gh-pages/source/content/posts/160509-django-gunicorn-ubuntu-1604.markdown)
and submit a pull request.

