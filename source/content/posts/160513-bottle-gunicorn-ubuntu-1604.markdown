title: Configuring Python 3, Bottle and Gunicorn for Development on Ubuntu 16.04 LTS
slug: python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus
meta: Instructions for developing Bottle web apps on Ubuntu 16.04 with Python 3 and Green Unicorn (Gunicorn).
category: post
date: 2016-05-13
headerimage: /source/static/img/160513-ubuntu-bottle-gunicorn/header.jpg
headeralt: Bottle, Green Unicorn and Ubuntu logos. Copyright their respective owners.


The [Ubuntu 16.04 Long Term Support (LTS)](/ubuntu.html) Linux
[operating system](/operating-systems.html) was released in April 2016.
This latest Ubuntu release is named "Xenial Xerus" and
it is the first Ubuntu release to include [Python 3](/python-2-or-3.html),
instead of Python 2.x, as the default Python installation.

We can quickly start a new [Bottle](/bottle.html) web application project 
and run it with [Green Unicorn (Gunicorn)](/green-unicorn-gunicorn.html) on
Ubuntu 16.04.


## Tools We Need
Our setup requires the Ubuntu 16.04 release along with a few other code 
libraries. Don't install these tools just yet since we'll get to them as 
we go through the walkthrough. Our requirements and their current versions 
as of May 13, 2016 are:

* [Ubuntu 16.04 LTS (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
* [Python](/why-use-python.html) version 
  [3.5](https://docs.python.org/3/whatsnew/3.5.html) 
  (default in Ubuntu 16.04)
* [Botle](/bottle.html) web framework version 
  [0.12](http://bottlepy.org/docs/0.12/)
* [Green Unicorn (Gunicorn)](/green-unicorn-gunicorn.html) version 
  [19.5](http://docs.gunicorn.org/en/stable/news.html)

If you are developing on Mac OS X or Windows, make sure to use 
virtualization software such
as [Parallels](https://www.parallels.com/products/desktop/) or
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) with the 
[Ubuntu .iso file](http://releases.ubuntu.com/16.04/). Either the amd64 or
i386 version of 16.04 is fine. I use the amd64 version for my own local 
development.

A desktop screen like this one appears when you boot up Ubuntu.

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/ubuntu-desktop.jpg" width="100%" class="technical-diagram img-rounded">

Open a terminal window to install the system packages.


## System Packages
We can see the python3 system version Ubuntu comes with and where its
executable is stored using these commands.

    python3 --version
    which python3

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/which-python.png" width="100%" class="technical-diagram img-rounded">

Our Ubuntu installation requires a few system packages. We will get prompted 
for the superuser password because restricted system access is needed 
to install packages through 
[apt](https://en.wikipedia.org/wiki/Advanced_Packaging_Tool).

    sudo apt-get install virtualenv python-pip python3-dev

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/install-packages.png" width="100%" class="technical-diagram img-rounded">

Enter `y` to let the system package installation process do its job.

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/packages-installed.png" width="100%" class="technical-diagram img-rounded">

The packages we need are now installed. We can continue on to install our 
Python-specific dependencies.


## Virtualenv
In the previous section, [virtualenv](https://virtualenv.pypa.io/en/latest/) 
and [pip](https://pypi.python.org/pypi/pip) were installed to handle our 
[application dependencies](/application-dependencies.html).
We can now use them to download and install Bottle and Gunicorn.


Create a directory for the virtualenvs. Then create a new virtualenv.

    # the tilde "~" specifies the user's home directory, like /home/matt
    cd ~
    mkdir venvs
    # specify the system python3 installation
    virtualenv --python=/usr/bin/python3 venvs/bottleproj

Activate the virtualenv.

    source ~/venvs/bottleproj/bin/activate

Our prompt will change after we properly activate the virtualenv.

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/venv-activated.png" width="100%" class="technical-diagram img-rounded">

Our virtualenv is now activated with Python 3. We can install whatever
dependencies we want, in our case Bottle and Gunicorn. 


## Bottle and Gunicorn
We can now install Bottle and Green Unicorn via the `pip` command.

    pip install bottle gunicorn


No errors like we see in the following screenshot is a good sign.

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/good-sign.png" width="100%" class="technical-diagram img-rounded">


Use the `mkdir` command to create a new directory to keep our Bottle 
project then use the `cd` (change directory) command to move into the
new folder.

    mkdir ~/bottleproj
    cd ~/bottleproj


Create a new file named `app.py` within our `bottleproj` directory so
we can test to make sure Bottle is working properly. I prefer to use
[Vim](/vim.html) but [Emacs](/emacs.html) and other 
[development environments](/development-environments.html) work great as
well.

Within the new `app.py` file write the following code.

    import bottle
    from bottle import route, run, Response

    # a basic URL route to test whether Bottle is responding properly
    @route('/')
    def index():
        return Response("It works!")

    # these two lines are only used for python app.py
    if __name__ == '__main__':
        run(host='0.0.0.0', port=8000, debug=True, reloader=True)

    # this is the hook for Gunicorn to run Bottle
    app = bottle.default_app()

We could run our app with the Bottle development server using the 
`python app.py` command. Let's instead run our Bottle app with
Gunicorn.

    gunicorn -w 2 app:app 

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/gunicorn-run.png" width="100%" class="technical-diagram img-rounded">

Sweet, we can bring up our shell Bottle app in the web browser at
the `localhost:8000` or `127.0.0.1:8000` address.

<img src="/source/static/img/160513-ubuntu-bottle-gunicorn/it-works.jpg" width="100%" class="technical-diagram img-rounded">

Time to develop a full-fledged web application with [Bottle](/bottle.html)!


## Ready for Development
Now you have a simple setup to develop Bottle web apps using Gunicorn as
the [WSGI server](/wsgi-servers.html) on Ubuntu 16.04. If you need a
full step-by-step tutorial to deploy your Python web application to a
production environment, check out the 
[Full Stack Python Guide to Deployments book](http://www.deploypython.com/).

To decide what to do next with your Python project, check out the
[Full Stack Python table of contents](/table-of-contents.html) page.

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/makaimc/fullstackpython.com/blob/gh-pages/source/content/posts/160513-bottle-gunicorn-ubuntu-1604.markdown)
and submit a pull request.

