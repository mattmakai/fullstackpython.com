title: How to Monitor Python Web Applications
slug: monitor-python-web-applications
meta: Learn how to add monitoring to a Python web application using a hosted monitoring service such as Rollbar.
category: post
date: 2017-09-26
modified: 2017-09-29
newsletter: False
headerimage: /img/170926-monitor-python-web-apps/header.jpg
headeralt: Python, Rollbar and Bottle logos, copyright their respective owners.


A quick way to check for errors and issues in your operational 
[Python web application](/web-development.html) is to drop-in one of many
awesome hosted [monitoring](/monitoring.html) tools.

Let's learn to quickly add [Rollbar monitoring](https://rollbar.com)
to a web app to visualize when our application is running properly and
when it has issues. This tutorial will use [Bottle](/bottle.html) as the 
example [web framework](/web-frameworks.html) along with Rollbar as the 
monitoring service but you can also check out the list of other tools 
on the [monitoring page](/monitoring.html).


## Our Tools 
We can use either [Python 2 or 3](/python-2-or-3.html) to build this
tutorial, but Python 3 is *strongly* recommended for all new applications. 
[Python 3.6.2](https://www.python.org/downloads/release/python-362/) 
was used to build this tutorial. We will also use the following 
[application dependencies](/application-dependencies.html) throughout
the post: 

* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/), which come installed 
  with Python 3, to install and isolate the Bottle and Rollbar libraries 
  from your other projects
* [Bottle](/bottle.html) web framework, 
  [version 0.12.13](https://bottlepy.org/docs/0.12/)
* [pyrollbar](https://rollbar.com/docs/notifier/pyrollbar/) monitoring 
  instrumentation library,
  [version 0.13.13](https://github.com/rollbar/pyrollbar/tree/v0.13.13)
  in Bottle applications so pyrollbar can report on all errors
* A [free Rollbar account](https://rollbar.com/) where we will send error
  data and view it when it is captured

If you need help getting your 
[development environment](/development-environments.html) configured
before running this code, take a look at
[this guide for setting up Python 3 and Bottle on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html).

All code in this blog post is available open source under the MIT license 
on GitHub under the 
[monitor-python-bottle-apps directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples). 
Use and abuse the source code as you desire for your own applications.


## Installing Dependencies
Create a new virtual environment for this project using the following
command. I recommend keeping a separate directory for virtualenvs under 
`~/Envs/` so you will know where all your project virtualenvs are located.

```bash
python3 -m venv monitorpython
```

Activate the virtualenv with the `activate` shell script:

```bash
source monitorpython/bin/activate
```

The command prompt will change after activating the virtualenv:

<img src="/img/170926-monitor-python-web-apps/activate-python-virtualenv.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Activating our Python virtual environment on the command line.">

Remember that you need to activate your virtualenv in every new terminal 
window where you want to use the virtualenv to run the project.

We can now install Bottle and Rollbar into the activated
virtualenv.

```
pip install bottle==0.12.13 rollbar==0.13.13
```

Look for output like the following to confirm the 
dependencies installed correctly.

```
Installing collected packages: bottle, urllib3, certifi, idna, chardet, requests, six, rollbar
  Running setup.py install for bottle ... done
    Running setup.py install for rollbar ... done
    Successfully installed bottle-0.12.13 certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 rollbar-0.13.13 six-1.11.0 urllib3-1.22
```

We have our dependencies ready to go so now we can build
our Python web application.


## Our Python Web App
Create a folder for your project named `monitor-python-apps`. `cd` into
the folder and then create a file named `app.py` with the following
code.

```python
import bottle
import os
import re
from bottle import route, template


TEMPLATE_STRING = """
<html>
 <head>
  <title>Full Stack Python Web App</title>
 </head>
 <body>
  <h1>{{ h1 }}</h1>
 </body>
</html>
"""

MIN_MSG_LENGTH = 2


@route("/<msg>/")
def show_message(msg):
    """Display a message if the msg value is greater than 2 characters
    in the path.
    """
    valid_length = len(msg) >= MIN_MSG_LENGTH
    valid_name = re.match('^[a-z\-]+$', msg.lower()) is not None
    if valid_length and valid_name:
        return template(TEMPLATE_STRING, h1=msg)
    else:
        error_msg = "Sorry, only alpha characters and hyphens allowed."
        raise Exception(error_msg)


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)
```

The above application code has a few standard Bottle imports so we can
create a Bottle web app and handle URL routes. 

We have a single function, `show_message`, that handles a single Bottle 
URL route. `show_message` checks if the URL path contains only alphabetic 
characters and hyphens for a message to display. If the message passes 
the conditions then a page is rendered with that message
in an `h1` element. If `msg` does not pass the condition test then an 
exception is thrown that only alpha characters and hyphens are allowed.

Save `app.py` and we can run our code. Execute `app.py` using the `python`
command as follows (make sure your virtualenv is still activated in the
terminal where you are running this command):

```bash
python app.py
```

The Bottle development server should start up and display a few lines
of output.

<img src="/img/170926-monitor-python-web-apps/run-bottle-app.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Run the local Bottle development server.">

Try to access a URL with a path that contains only alphabetic characters and 
hyphens, such as 
[localhost:8080/hello-world/](http://localhost:8080/hello-world/).

<img src="/img/170926-monitor-python-web-apps/localhost-hello-world.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Testing at /hello-world/ returns an HTTP 200 response.">

The application was successful in displaying "hello-world" but what if we
try a URL that contains numbers in addition to the alphabetic characters,
such as
[localhost:8080/fullstackpython123/](http://localhost:8080/fullstackpython/)?

<img src="/img/170926-monitor-python-web-apps/localhost-500.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="We receive a 500 error when numbers are added to the URL.">

An HTTP 500 error. That is surely not a good user experience.

The 500 error is obvious to us right now because we are 
testing the application locally during development. However, what happens 
when the app is deployed and a user gets the error in their own web 
browser? They will likely quit out of frustration and you will never 
know what happened unless you add some error tracking and application 
monitoring.

Time to modify our code to add Rollbar to report errors that occur.


## Monitoring for Errors with Rollbar
Go to the [Rollbar homepage in your browser](https://rollbar.com/) 
to add their tool to our Bottle app.

<img src="/img/170926-monitor-python-web-apps/rollbar-homepage.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="The Rollbar homepage in the Chrome web browser.">

Click the "Sign Up" button in the upper right-hand corner. Enter your 
email address, a username and the password you want on the sign up page.

<img src="/img/170926-monitor-python-web-apps/sign-up-page.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Enter your account information on the sign up page.">

After the sign up page you will see the onboarding flow where you can
enter a project name and select a programming language. For the project
name type in "Full Stack Python" then select that you are monitoring a 
Python app.

<img src="/img/170926-monitor-python-web-apps/create-new-project.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Create a new project named 'Battlegrounds' and select Python as the programming language.">

Press the "Continue" button at the bottom to move along. The next
screen shows us a few instructions to add monitoring to a Python
application.

<img src="/img/170723-monitor-flask-apps/project-setup.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Set up your project using your server-side access token.">

Let's change our Bottle code to let Rollbar collect and aggregate the
errors that pop up in our application. Modify `app.py` to include the 
following highlighted lines. 

```python
import bottle
import os
import re
from bottle import route, template
~~from rollbar.contrib.bottle import RollbarBottleReporter


TEMPLATE_STRING = """
<html>
 <head>
  <title>Full Stack Python Web App</title>
 </head>
 <body>
  <h1>{{ h1 }}</h1>
 </body>
</html>
"""

MIN_MSG_LENGTH = 2
~~ROLLBAR_SECRET = os.environ.get("ROLLBAR_SECRET")
~~
~~rb_monitor = RollbarBottleReporter(access_token=ROLLBAR_SECRET,
~~                                   environment='production')
~~bottle.install(rb_monitor)


@route("/<msg>/")
def show_message(msg):
    """Display a message if the msg value is greater than 2 characters
    in the path.
    """
    valid_length = len(msg) >= MIN_MSG_LENGTH
    valid_name = re.match('^[a-z\-]+$', msg.lower()) is not None
    if valid_length and valid_name:
        return template(TEMPLATE_STRING, h1=msg)
    else:
        error_msg = "Sorry, only alpha characters and hyphens allowed."
        raise Exception(error_msg)


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)
```

A new import `from rollbar.contrib.bottle import RollbarBottleReporter`
is our conduit between the application and the Rollbar server. `rollbar`
is the library we installed earlier. 

The `ROLLBAR_SECRET` token needs to be set in an environment variable.
Save and quit `app.py`. Run the following command in the terminal where your
virtualenv is activated:

```bash
export ROLLBAR_SECRET='token here'
``` 

If you are uncertain about what your secret token is, it can be found on 
the Rollbar onboarding screen. 

Note that I typically store all my environment variables in a `.env` 
file and use a 
[template.env](https://github.com/fullstackpython/blog-code-examples/blob/master/monitor-flask-apps/template.env) 
as a template for what I should fill into `.env`. `.env` can be invoked
from the terminal using the `. .env` command. Make sure to *never* commit 
your secret tokens to a source control repository though, especially if 
the repository is public!

After exporting your `ROLLBAR_SECRET` key as an environment variable
we can test that Rollbar is working as we run our application. Run it
now using `python`:

```bash
python app.py
```

Back in your web browser press the "Done! Go to Dashboard" button.

If an event hasn't been reported yet we'll see a waiting screen like this
one:

<img src="/img/170926-monitor-python-web-apps/waiting.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Waiting for data on the Rollbar dashboard.">

Make sure your Bottle development server is running and try to go to 
[localhost:8080/fullstackpython123/](http://localhost:8080/fullstackpython123/).
A 500 server error is immediately reported on the dashboard:

<img src="/img/170926-monitor-python-web-apps/exception-reported.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Viewing the 500 errors reported in the Rollbar dashboard.">

We even get an email with the error (which can also be turned off if you
don't want emails for every error):

<img src="/img/170926-monitor-python-web-apps/email-error-report.jpg" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Email with the Rollbar error report.">

Nice, with just a few lines of code we now have our Bottle app reporting
errors for any user that's working with our application.


## What now?
We just learned how to catch and handle errors with Rollbar as a hosted
monitoring platform in a simple example 
[Bottle application](/bottle.html). Next you will want to 
add [monitoring](/monitoring.html) to more complicated web apps, including
ones that use [Django](/django.html) or [Flask](/flask.html). You can also 
try Rollbar's more advanced features to:

* [set up rules to group errors](https://rollbar.com/docs/custom-grouping/)
* [debug and track deployment issues](https://rollbar.com/docs/deploy-tracking/)
* [sort and view errors by user](https://rollbar.com/docs/person-tracking/)

There is plenty more to learn about in the areas of 
[web development](/web-development.html) and 
[deployments](/deployments.html) so keep learning by reading 
about [web frameworks](/web-frameworks.html). You can also learn more 
about integrating Rollbar with Python applications via 
[their Python documentation](https://rollbar.com/docs/notifier/pyrollbar/).

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

Do you see a typo, syntax issue or just something that's confusing in this 
blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170926-monitor-python-web-apps.markdown)
and submit a pull request with a fix or 
[file an issue ticket on GitHub](https://github.com/mattmakai/fullstackpython.com/issues).
