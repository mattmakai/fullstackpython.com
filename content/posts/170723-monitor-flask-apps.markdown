title: How to Add Hosted Monitoring to Flask Web Applications
slug: hosted-monitoring-flask-web-apps
meta: Learn to add hosted monitoring to Flask web applications using Rollbar.
category: post
date: 2017-07-23
modified: 2017-07-23
newsletter: False
headerimage: /img/170723-monitor-flask-apps/header.jpg
headeralt: Flask, Python and Rollbar logos, copyright their respective owners.


How do you know whether your application is running properly with minimal 
errors after [building](/web-development.html) and 
[deploying](/deployment.html) it? The fastest and easiest way
to monitor your operational [Flask web application](/flask.html) is to 
integrate one of the many available fantastic hosted 
[monitoring](/monitoring.html) tools.

In this post we will quickly add [Rollbar monitoring](https://rollbar.com)
to catch errors and visualize our application is running properly. There
are also many other great hosted monitoring tools, which you can check
out on the [monitoring](/monitoring.html) page.


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
* [blinker](https://pypi.org/project/blinker) for signaling support
  in Flask applications so pyrollbar can report on all errors
* A [free Rollbar account](https://rollbar.com/) where we will send error
  data and view it when it is captured
* [pip](https://pip.pypa.io/en/stable/) and the 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) virtual environment
  library, which come packaged with Python 3, to install and isolate the 
  Flask and Rollbar libraries from other Python projects you are working on

If you need help getting your 
[development environment](/development-environments.html) configured
before running this code, take a look at
[this guide for setting up Python 3 and Flask on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html).

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

<img src="/img/170723-monitor-flask-apps/activate-virtualenv.png" width="100%" class="shot rnd outl" alt="Activating our Python virtual environment on the command line.">

Remember that you need to activate the virtualenv in every new terminal 
window where you want to use the virtualenv to run the project.

Flask, Rollbar and Blinker can now be installed into the now-activated 
virtualenv.

```
pip install flask==0.12.2 rollbar==0.13.12 blinker==1.4
```

Our required dependencies should be installed within our virtualenv 
after a short installation period. Look for output like the following to 
confirm everything worked.

```
Installing collected packages: blinker, itsdangerous, click, MarkupSafe, Jinja2, Werkzeug, Flask, idna, urllib3, chardet, certifi, requests, six, rollbar
  Running setup.py install for blinker ... done
  Running setup.py install for itsdangerous ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for rollbar ... done
Successfully installed Flask-0.12.2 Jinja2-2.9.6 MarkupSafe-1.0 Werkzeug-0.12.2 blinker-1.4 certifi-2017.4.17 chardet-3.0.4 click-6.7 idna-2.5 itsdangerous-0.24 requests-2.18.1 rollbar-0.13.12 six-1.10.0 urllib3-1.21.1
```

Now that we have our Python dependencies installed into our virtualenv
we can create the initial version of our application.


## Building Our Flask App
Create a folder for your project named `monitor-flask-apps`. Change into
the folder and then create a file named `app.py` with the following
code.

```python
import re
from flask import Flask, render_template, Response
from werkzeug.exceptions import NotFound


app = Flask(__name__)
MIN_PAGE_NAME_LENGTH = 2


@app.route("/<string:page>/")
def show_page(page):
    try:
        valid_length = len(page) >= MIN_PAGE_NAME_LENGTH
        valid_name = re.match('^[a-z]+$', page.lower()) is not None
        if valid_length and valid_name:
            return render_template("{}.html".format(page))
        else:
            msg = "Sorry, couldn't find page with name {}".format(page)
            raise NotFound(msg)
    except:
        return Response("404 Not Found")


if __name__ == "__main__":
    app.run(debug=True)
```

The above application code has some standard Flask imports so we can
create a Flask web app and render template files. We have a single
function named `show_page` to serve a single Flask route. `show_page`
checks if the URL path contains only lowercase alpha characters for a
potential page name. If the page name can be found in the `templates`
folder then the page is rendered, otherwise an exception is thrown
that the page could not be found. We need to create at least one template
file if our function is ever going to return a non-error reponse.

Save `app.py` and make a new subdirectory named `templates` under your
project directory. Create a new file named `battlegrounds.html` and put
the following [Jinja2](/jinja2.html) template markup into it.

```jinja2
<!DOCTYPE html>
<html>
  <head>
    <title>You found the Battlegrounds GIF!</title>
  </head>
  <body>
    <h1>PUBG so good.</h1>
    <img src="https://media.giphy.com/media/3ohzdLMlhId2rJuLUQ/giphy.gif">
  </body>
</html>
```

The above [Jinja2](/jinja2.html) template is basic HTML without any
[embedded template tags](http://jinja.pocoo.org/docs/latest/templates/). 
The template creates a very plain page with a header description of
"PUBG so good" and a GIF from this
[excellent computer game](http://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/).

Time to run and test our code. Change into the base directory of your
project where `app.py` file is located. Execute `app.py` using the `python`
command as follows (make sure your virtualenv is still activated in the
terminal where you are running this command):

```bash
python app.py
```

The Flask development server should start up and display a few lines
of output.

<img src="/img/170723-monitor-flask-apps/python-app-py.png" width="100%" class="shot rnd outl" alt="Run the Flask development server locally.">

What happens when we access the application running on 
[localhost port 5000](http://localhost:5000)?

<img src="/img/170723-monitor-flask-apps/localhost-base-url.png" width="100%" class="shot rnd outl" alt="Testing our Flask application at the base URL receives an HTTP 404 error.">

HTTP status 404 page not found, which is what we expected because we only
defined a single route and it did not live at the base path.

We created a template named `battlegrounds.html` that should be accessible
when we go to 
[localhost:5000/battlegrounds/](http://localhost:5000/battlegrounds/).

<img src="/img/170723-monitor-flask-apps/localhost-pubg-gif.jpg" width="100%" class="shot rnd outl" alt="Testing our Flask application at /battlegrounds/ gets the proper template with a GIF.">

The application successfully found the `battlegrounds.html` template but
that is the only one available. What if we try 
[localhost:5000/fullstackpython/](http://localhost:5000/fullstackpython/)?

<img src="/img/170723-monitor-flask-apps/localhost-no-template.jpg" width="100%" class="shot rnd outl" alt="If no template is found we receive a 500 error.">

HTTP 500 error. That's no good.

The 404 and 500 errors are obvious to us right now because we are 
testing the application locally. However, what happens when the app is 
deployed and a user gets the error in their own web browser? They will 
typically quit out of frustration and you will never know what happened 
unless you add some error tracking and application monitoring.

We will now modify our code to add Rollbar to catch and report those
errors that occur for our users.


## Handling Errors
Head to [Rollbar's homepage](https://rollbar.com/) so we can add their
hosted monitoring tools to our oft-erroring Flask app.

<img src="/img/170723-monitor-flask-apps/rollbar-homepage.jpg" width="100%" class="shot rnd outl" alt="Rollbar homepage in the web browser.">

Click the "Sign Up" button in the upper right-hand corner. Enter your 
email address, a username and the password you want on the sign up page.

<img src="/img/170723-monitor-flask-apps/sign-up.jpg" width="100%" class="shot rnd outl" alt="Enter your basic account information on the sign up page.">

After the sign up page you will see the onboarding flow where you can
enter a project name and select a programming language. For project
name enter "Battlegrounds" and select that you are monitoring a Python app.

<img src="/img/170723-monitor-flask-apps/create-new-project.jpg" width="100%" class="shot rnd outl" alt="Create a new project named 'Battlegrounds' and select Python as the programming language.">

Press the "Continue" button at the bottom to move along. The next
screen shows us a few quick instructions to add monitoring to our Flask
application.

<img src="/img/170723-monitor-flask-apps/project-setup.jpg" width="100%" class="shot rnd outl" alt="Set up your project using your server-side access token.">

Let's modify our Flask application to test whether we can properly connect
to Rollbar's service. Change `app.py` to include the following highlighted
lines. 

```python
~~import os
import re
~~import rollbar
from flask import Flask, render_template, Response
from werkzeug.exceptions import NotFound


app = Flask(__name__)
MIN_PAGE_NAME_LENGTH = 2


~~@app.before_first_request
~~def add_monitoring():
~~    rollbar.init(os.environ.get('ROLLBAR_SECRET'))
~~    rollbar.report_message('Rollbar is configured correctly')


@app.route("/<string:page>/")
def show_page(page):
    try:
        valid_length = len(page) >= MIN_PAGE_NAME_LENGTH
        valid_name = re.match('^[a-z]+$', page.lower()) is not None
        if valid_length and valid_name:
            return render_template("{}.html".format(page))
        else:
            msg = "Sorry, couldn't find page with name {}".format(page)
            raise NotFound(msg)
    except:
        return Response("404 Not Found")


if __name__ == "__main__":
    app.run(debug=True)
```

We added a couple of new imports, `os` and `rollbar`. `os` allows us to
grab environment variable values, such as our Rollbar secret key. `rollbar`
is the library we installed earlier. The two lines below the Flask app
instantiation are to initialize Rollbar using the Rollbar secret token and
send a message to the service that it started correctly.

The `ROLLBAR_SECRET` token needs to be set in an environment variable.
Save an quit the `app.py`. Run `export ROLLBAR_SECRET='token here'` on the
command line where your virtualenv is activated. This token can be found
on the Rollbar onboarding screen. 

I typically store all my environment variables in a file like 
[template.env](https://github.com/fullstackpython/blog-code-examples/blob/master/monitor-flask-apps/template.env) and invoke it from the terminal using
the `. ./template.env` command. Make sure to avoid committing your secret
tokens to a source control repository, especially if the repository is 
public!

After exporting your `ROLLBAR_SECRET` key as an environment variable
we can test that Rollbar is working as we run our application. Run it
now using `python`:

```bash
python app.py
```

Back in your web browser press the "Done! Go to Dashboard" button. Don't 
worry about the "Report an Error" section code, we can get back to that in a 
moment.

If the event hasn't been reported yet we'll see a waiting screen like this
one:

<img src="/img/170723-monitor-flask-apps/waiting.jpg" width="100%" class="shot rnd outl" alt="Waiting for data on the dashboard.">

Once Flask starts up though, the first event will be populated on the 
dashboard.

<img src="/img/170723-monitor-flask-apps/first-event.jpg" width="100%" class="shot rnd outl" alt="First event populated on our dashboard for this project.">

Okay, our first test event has been populated, but we really want to see
all the errors from our application, not a test event.


## Testing Error Handling
How do we make sure real errors are reported rather than just a simple
test event? We just need to add a few more lines of code to our app.

```python
import os
import re
import rollbar
~~import rollbar.contrib.flask
from flask import Flask, render_template, Response
~~from flask import got_request_exception
from werkzeug.exceptions import NotFound


app = Flask(__name__)
MIN_PAGE_NAME_LENGTH = 2


@app.before_first_request
def add_monitoring():
    rollbar.init(os.environ.get('ROLLBAR_SECRET'))
~~	  ## delete the next line if you dont want this event anymore
    rollbar.report_message('Rollbar is configured correctly')
~~    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


@app.route("/<string:page>/")
def show_page(page):
    try:
        valid_length = len(page) >= MIN_PAGE_NAME_LENGTH
        valid_name = re.match('^[a-z]+$', page.lower()) is not None
        if valid_length and valid_name:
            return render_template("{}.html".format(page))
        else:
            msg = "Sorry, couldn't find page with name {}".format(page)
            raise NotFound(msg)
    except:
~~        rollbar.report_exc_info()
        return Response("404 Not Found")


if __name__ == "__main__":
    app.run(debug=True)
``` 

The above highlighted code modifies the application so it reports all Flask
errors as well as our HTTP 404 not found issues that happen within the
`show_page` function. 

Make sure your Flask development server is running and try to go to 
[localhost:5000/b/](http://localhost:5000/b/). You will receive an HTTP
404 exception and it will be reported to Rollbar. Next go to 
[localhost:5000/fullstackpython/](http://localhost:5000/fullstackpython/) and 
an HTTP 500 error will occur.

You should see an aggregation of errors as you test out these errors:

<img src="/img/170723-monitor-flask-apps/error-aggregation.jpg" width="100%" class="shot rnd outl" alt="Rollbar dashboard showing aggregations of errors.">

Woohoo, we finally have our Flask app reporting all errors that occur
for any user back to the hosted Rollbar monitoring service!


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
[Sanic](/sanic.html). You can also learn more about integrating Rollbar
with Python applications via 
[their Python documentation](https://rollbar.com/docs/notifier/pyrollbar/).

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

See something wrong in this blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170723-monitor-flask-apps.markdown)
and submit a pull request with a fix.
