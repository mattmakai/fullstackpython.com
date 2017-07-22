title: How to Add Hosted Monitoring to Flask Web Applications
slug: hosted-monitoring-flask-web-apps
meta: 
category: post
date: 2017-07-23
modified: 2017-07-23
headerimage: /img/170723-monitor-flask-apps/header.jpg
headeralt: Flask, Python and Rollbar logos, copyright their respective owners.


How do you know whether your application is running properly with minimal 
errors after [building](/web-development.html) and 
[deploying](/deployment.html) it? The fastest and easiest way
to monitor your operational [Flask web application](/flask.html) is to 
integrate one of the many available fantastic hosted 
[monitoring](/monitoring.html) tools.

In this post we will quickly add [Rollbar monitoring](https://rollbar.com)
to catch errors and visualize our application is running properly.


## Our Tools 
We can use either [Python 2 or 3](/python-2-or-3.html) to build this
tutorial, but Python 3 is *strongly* recommended for all new applications. 
I used 
[Python 3.6.2](https://www.python.org/downloads/release/python-362/) to 
execute my code. We will also use the following 
[application dependencies](/application-dependencies.html) throughout
the post: 

* [Flask](/flask.html) web framework, 
  [version 0.12.2](https://github.com/pallets/flask/releases/tag/0.12.2)
* [pyrollbar](https://rollbar.com/docs/notifier/pyrollbar/) monitoring 
  instrumentation library,
  [version 0.13.12](https://github.com/rollbar/pyrollbar/tree/v0.13.12)
* [pip](https://pip.pypa.io/en/stable/) and the 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) virtual environment
  library, which come packaged with Python 3, to install and isolate the 
  Flask and Rollbar libraries from other Python projects you are working on

If you need help getting your 
[development environment](/development-environments.html) configured
before running this code, take a look at
[this guide for setting up Python 3 and Flask on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)

All code in this blog post is available open source under the MIT license 
on GitHub under the 
[monitor-flask-apps directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples). 
Use and abuse the source code as you desire for your own applications.


## Installing Dependencies
Change into the directory where you keep your Python virtualenvs. 
Create a new virtual environment for this project using the following
command.

```bash
python3 -m venv monitorflask
```

Activate the virtualenv.

```bash
source monitorflask/bin/activate
```

The command prompt will change after activating the virtualenv:

<img src="/img/170723-monitor-flask-apps/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Activating our Python virtual environment on the command line.">

Remember that you need to activate the virtualenv in every new terminal 
window where you want to use the virtualenv to run the project.

Flask and Rollbar can now be installed into the now-activated virtualenv.

```
pip install flask==0.12.2 rollbar==0.13.12
```

Our required dependencies should be installed within our virtualenv 
after a short installation period. Look for output like the following to 
confirm everything worked.

```
Installing collected packages: MarkupSafe, Jinja2, itsdangerous, click, Werkzeug, flask, idna, urllib3, chardet, certifi, requests, six, rollbar
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for itsdangerous ... done
  Running setup.py install for rollbar ... done
Successfully installed Jinja2-2.9.6 MarkupSafe-1.0 Werkzeug-0.12.2 certifi-2017.4.17 chardet-3.0.4 click-6.7 flask-0.12.2 idna-2.5 itsdangerous-0.24 requests-2.18.1 rollbar-0.13.12 six-1.10.0 urllib3-1.21.1
```

Now that we have our Python dependencies installed into our virtualenv
we can create the initial version of our application.


## Building Our Flask App
Create a folder for your project named `monitor-flask-apps`. Change into
the folder and then create a file named `app.py` with the following
code.

```python

```


Test it out.

We can see the error because we are testing our application locally,
but what happens when our application is deployed and a user gets the
error? They will typically quit out of frustration and you will never
know what happened unless you add some error tracking and application
monitoring.

We'll now modify our code to add Rollbar to catch and report those
errors that occur for our users.


## Handling Errors
Head to [Rollbar's homepage](https://rollbar.com/) so we can add their
hosted monitoring tools to our oft-erroring Flask app.

<img src="/img/170723-monitor-flask-apps/rollbar-homepage.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Rollbar homepage in the web browser.">

Click the "Sign Up" button in the upper right-hand corner. Enter your 
email address, a username and the password you want on the sign up page.

<img src="/img/170723-monitor-flask-apps/sign-up.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Enter your basic account information on the sign up page.">

After the sign up page you'll get to the onboarding flow where you can
enter a project name and select a programming language. For project
name enter "Echo" and select that you are monitoring a Python app.

<img src="/img/170723-monitor-flask-apps/create-new-project.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Create a new project named 'echo' and select Python as the programming language.">


(links to Python docs)


## Testing Error Handling


## What's Next?
We just learned how to catch and handle errors with Rollbar as a hosted
monitoring platform in a simple Flask application. Next you will want to 
add monitoring to your more complicated web apps. You can also check out 
some of Rollbar's more advanced features such as:

* [tracking and debugging deployment issues](https://rollbar.com/docs/deploy-tracking/)
* [sorting and viewing errors by user](https://rollbar.com/docs/person-tracking/)
* [setting up custom rules to group errors](https://rollbar.com/docs/custom-grouping/)

There is a lot more to learn about [web development](/web-development.html)
and [deployments](/deployments.html) so keep learning by reading up on 
[Flask](/flask.html) and other [web frameworks](/web-frameworks.html) 
such as [Django](/django.html), [Pyramid](/pyramid.html) and 
[Sanic](/sanic.html).

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

See something wrong in this blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170723-monitor-flask-apps.markdown)
and submit a pull request with a fix.
