title: Using Sentry to Handle Python Exceptions in Django Projects
slug: sentry-handle-exceptions-django-projects
meta: Learn to handle Python exceptions in your Django projects with the hosted Sentry service.
category: post
date: 2020-08-23
modified: 2020-08-23
newsletter: False
headerimage: /img/headers/django-sentry.jpg
headeralt: Logos for the implementations used in this blog post. Copyright their respective owners.


Web applications built in [Django](/django.html) can become sprawlingly complex over time, which is one reason why centralized error handling is important. This tutorial will guide you through adding a free, basic Sentry configuration to a new Django project.

When we're done, you will be able to view centralized error reports in the Sentry dashboard like you see in this screenshot:

<img src='/img/200823-django-sentry/sentry-dashboard.jpg' width='100%' alt='Sentry dashboard with caught Django exceptions.' class='shot rnd outl'>



## Tutorial Requirements
Throughout this tutorial we are going to use the following dependencies,
which we will install in just a moment. Make sure you also have Python 3,
[preferrably 3.7 or newer installed](https://www.python.org/downloads/),
in your environment:

We will use the following dependencies to complete this
tutorial:

* [Django](/django.html) [web framework](/web-frameworks.html),
  [version 3.1](https://www.djangoproject.com/download/)
* [sentry-sdk](https://sentry.io/for/python/),
  [version 0.16.5](https://pypi.org/project/sentry-sdk/)

All code in this blog post is available open source under the MIT license
on GitHub under the
[sentry-handle-exceptions-django-projects directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples).
Use the source code as you desire for your own projects.


## Development environment configuration
Change into the directory where you keep your Python
[virtual environments](/virtual-environments-virtualenvs-venvs.html).
Create a new virtualenv for this project using the following
command.

Start the Django project by creating a new
[virtual environment](/virtual-environments-virtualenvs-venvs.html)
using the following command. I recommend using a separate directory
such as `~/venvs/` (the tilde is a shortcut for your user's `home`
directory) so that you always know where all your virtualenvs are
located.

```bash
python3 -m venv ~/venvs/djsentry
```

Activate the virtualenv with the `activate` shell script:

```bash
source ~/venvs/djsentry/bin/activate
```

After the above command is executed, the command prompt will
change so that the name of the virtualenv is prepended to the
original command prompt format, so if your prompt is simply
`$`, it will now look like the following:

```bash
(djsentry) $
```

Remember, you have to activate your virtualenv in every new terminal
window where you want to use dependencies in the virtualenv.

We can now install the [Django](https://pypi.org/project/Django/)
package into the activated but otherwise empty virtualenv.

```
pip install django==3.1 sentry-sdk==0.16.5
```

Look for output similar to the following to confirm the appropriate
packages were installed correctly from PyPI.

```
(djsentry) $ pip install django==3.1 sentry-sdk==0.16.5
Collecting django
  Downloading https://files.pythonhosted.org/packages/2b/5a/4bd5624546912082a1bd2709d0edc0685f5c7827a278d806a20cf6adea28/Django-3.1-py3-none-any.whl (7.8MB)
    100% |████████████████████████████████| 7.8MB 6.3MB/s 
Collecting sentry-sdk
  Downloading https://files.pythonhosted.org/packages/f4/4c/49f899856e3a83e02bc88f2c4945aa0bda4f56b804baa9f71e6664a574a2/sentry_sdk-0.16.5-py2.py3-none-any.whl (113kB)
    100% |████████████████████████████████| 122kB 33.7MB/s 
Collecting asgiref~=3.2.10 (from django)
  Using cached https://files.pythonhosted.org/packages/d5/eb/64725b25f991010307fd18a9e0c1f0e6dff2f03622fc4bcbcdb2244f60d6/asgiref-3.2.10-py3-none-any.whl
Collecting sqlparse>=0.2.2 (from django)
  Using cached https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl
Collecting pytz (from django)
  Using cached https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl
Collecting urllib3>=1.10.0 (from sentry-sdk)
  Using cached https://files.pythonhosted.org/packages/9f/f0/a391d1463ebb1b233795cabfc0ef38d3db4442339de68f847026199e69d7/urllib3-1.25.10-py2.py3-none-any.whl
Collecting certifi (from sentry-sdk)
  Using cached https://files.pythonhosted.org/packages/5e/c4/6c4fe722df5343c33226f0b4e0bb042e4dc13483228b4718baf286f86d87/certifi-2020.6.20-py2.py3-none-any.whl
Installing collected packages: asgiref, sqlparse, pytz, django, urllib3, certifi, sentry-sdk
Successfully installed asgiref-3.2.10 certifi-2020.6.20 django-3.1 pytz-2020.1 sentry-sdk-0.16.5 sqlparse-0.3.1 urllib3-1.25.10

```

We can get started coding the application now that we have all of our
required dependencies installed.


## Coding the initial application
We have everything we need to start building our application.

We can use the [Django](/django.html) `django-admin` tool to create
the boilerplate code structure to get our project started.
Change into the directory where you develop your applications. For
example, I typically use `/Users/matt/devel/py/` for all of my
Python projects. Then run the following command to start a Django
project named `djsentry`:

```
django-admin.py startproject djsentry
```

Note that in this tutorial we are using the same name for both the
virtualenv and the Django project directory, but they can be
different names if you prefer that for organizing your own projects.

The `django-admin` command creates a directory named `djsentry`
along with several subdirectories that you should be familiar with
if you have previously worked with Django.

Change directories into the new project.

```
cd djsentry
```

Create a new Django app within `djsentry`.

```
python manage.py startapp errors
```

Django will generate a new folder named `errors` for the project.
We should update the URLs so the app is accessible before we write
our `views.py` code.

Open `djsentry/djsentry/urls.py`. Add the highlighted
lines so that URL resolver will check the `errors` app
for additional routes to match with URLs that are requested of
this Django application.

```python
# djsentry/djsentry/urls.py
~~from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
~~    path('', include('errors.urls')),
    path('admin/', admin.site.urls),
]
```

Save `djsentry/djsentry/urls.py` and open
`djsentry/djsentry/settings.py`.
Add the `errors` app to `settings.py` by inserting
the highlighted line:

```python
# djsentry/djsentry/settings.py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
~~    'errors',
]
```

Make sure you change the default `DEBUG` and `SECRET_KEY`
values in `settings.py` before you deploy any code to production. Secure
your app properly with the information from the Django
[production deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
so that you do not add your project to the list of hacked applications
on the web.

Save and close `settings.py`.

Next change into the `djsentry/errors` directory. Create
a new file named `urls.py` to contain routes for the `errors` app.

Add all of these lines to the empty `djsentry/errors/urls.py`
file.

```python
# djsentry/errors/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.errors_index, name="index"),
]
```

Save `djsentry/errors/urls.py`. Open
`djsentry/errors/views.py` to add the
following two highlighted lines. You can keep the boilerplate comment
"# Create your views here." or delete like I usually do.

```
# djsentry/errors/views.py
from django.shortcuts import render


~~def errors_index(request):
~~    return render(request, 'index.html', {})
```


Next, create a directory for your template files named `templates` under
the `djmaps/maps` app directory.

```
mkdir templates
```

Create a new file named `index.html` within
`djsentry/errors/templates` that contains the
following [Django template language](/django-templates.html) markup.

```
<!DOCTYPE html>
<html>
  <head>
    <title>First step for errors</title>
  </head>
  <body>
   <h1>Hello, world!</h1>
  </body>
</html>
```

We can test out this static page to make sure all of our code is
correct before we start adding the meat of the functionality to
the project. Change into the base directory of your Django project
where the `manage.py` file is located. Execute the development
server with the following command:

```bash
python manage.py runserver
```

The Django development server should start up with no issues other than
an unapplied migrations warning.

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 15, 2020 - 17:26:57
Django version 3.1, using settings 'djsentry.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

Open a web browser and go to `localhost:8000`.

<img src="/img/visuals/first-step.jpg" width="100%" class="shot rnd outl" alt="Plain old HTML page saying 'Hello, world!'.">

Our code works, but it sure does not do much yet. Let's add
sentry-sdk so we can understand how it works.


## Adding Sentry and the sentry-sdk library
We can now add Sentry and test it with a bunch of errors to make sure it
is working properly.

Sentry can either be [self-hosted](https://github.com/getsentry/onpremise) or
used as a cloud service through [Sentry.io](https://sentry.io). In this 
tutorial we will use the cloud hosted version because it's faster than
setting up your own server as well as free for smaller projects.

Go to [Sentry.io's homepage](https://sentry.io).

<img src="/img/200525-sentry/sentry-homepage.jpg" width="100%" class="shot rnd outl" alt="Sentry.io homepage where you can sign up for a free account.">

Sign into your account or sign up for a new free account. You will be at
the main account dashboard after logging in or completing the Sentry sign
up process.

There are no errors logged on our account dashboard yet, which is as 
expected because we have not yet connected our account to our Django
project.

<img src="/img/200525-sentry/sentry-empty-dashboard.jpg" width="100%" class="shot rnd outl" alt="Blank Sentry account dashboard.">

Create a new Sentry Project just for this application by clicking
"Projects" in the left sidebar to go to the Projects page.

<img src="/img/200525-sentry/create-project.jpg" width="100%" class="shot rnd outl" alt="Button to create a new Sentry project.">

On the Projects page, click the "Create Project" button in the top right
corner of the page.

<img src="/img/200525-sentry/create-new-project-screen.jpg" width="100%" class="shot rnd outl" alt="Create a new Sentry project.">

You can either choose "Django" or select "Python". I usually just choose 
"Python" if I do not yet know what framework I'll be using to build my 
application. Next, give your new Project a name and then press the "Create 
Project" button. Our new project is ready to integrate with our Python code.

We need the unique identifier for our account and project to authorize our
Python code to send errors to this Sentry instance. The easiest way to get
what we need is to go to the 
[Python+Django documentation page](https://docs.sentry.io/platforms/python/django/)
and read how to configure the SDK.

<img src="/img/200525-sentry/python-sentry-quickstart.jpg" width="100%" class="shot rnd outl" alt="The Sentry docs show you exactly what you need to export to connect to your account."> 

Copy the string parameter for the `init` method and set it
[as an environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
rather than having it exposed in your project's code.

```bash
export SENTRY_DSN='https://yourkeygoeshere.ingest.sentry.io/project-number'
```

**Make sure to replace "yourkeygoeshere" with your own unique identifier
and "project-number" with the ID that matches the project you just
created.**

Check that the `SENTRY_DSN` is set properly in your shell using the `echo`
command:

```bash
echo $SENTRY_DSN
```

Next, update `settings.py` with the following highlighted new lines:

```python
# settings.py
~~import os
~~import sentry_sdk

from pathlib import Path
~~from sentry_sdk.integrations.django import DjangoIntegration

                                                                                                                                                                                 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
```

At the bottom of the file after the line with `STATIC_URL`, add the
Sentry configuration:

```python
STATIC_URL = '/static/'

~~sentry_sdk.init(
~~    dsn=os.getenv('SENTRY_DSN'),
~~    integrations=[DjangoIntegration()],

~~    # If you wish to associate users to errors (assuming you are using
~~    # django.contrib.auth) you may enable sending PII data.
~~    send_default_pii=True
~~)
```

Now that we have the configuration in place we can deliberately make some
errors happen to test the connection to Sentry's service.


## Testing Sentry's error catching
We'll change some of the existing code to deliberately throw exceptions
to make sure everything is working properly.

Start by opening `errors/views.py` and updating it with one new
highlighted line that will automatically throw a generic Exception
when this function is called.

```python
# djsentry/errors/views.py
from django.shortcuts import render


def errors_index(request):
~~    raise Exception('testing exception')
    return render(request, 'index.html', {})
```

Go to `localhost:8000` in your browser and you will immediately get this
exception page when running the development server:

<img src='/img/200823-django-sentry/exception-thrown-debug-page.jpg' width='100%' alt='Django development mode debug page when the Exception is raised.' class='shot rnd outl'>

We can also try out code that does not simply raise an exception but instead
will definitely create one when executed, like this division by zero 
operation:

```python
# djsentry/errors/views.py
from django.shortcuts import render


def errors_index(request):
~~    division_by_zero = 1 / 0
    return render(request, 'index.html', {})
```

<img src='/img/200823-django-sentry/division-by-zero-exception.jpg' width='100%' alt='Django development mode debug page when the Exception occurs.' class='shot rnd outl'>

If those exceptions both appear in the Sentry dashboard like this, you're all
set:

<img src='/img/200823-django-sentry/sentry-dashboard.jpg' width='100%' alt='Sentry dashboard with the exceptions that just occurred..' class='shot rnd outl'>

The above exceptions were just a couple of generic ways to test that everything
is working to send error information to Sentry. This configuration will
also handle the 
[many other Django exceptions](https://docs.djangoproject.com/en/stable/ref/exceptions/)
you are likely to see when building the rest of your Django project.


## Additional resources
We just finished building a Django project that uses Sentry for 
centralized error handling.

Next, try out some of these other related [Django](/django.html) tutorials:

* [Tracking Daily User Data in Django with django-user-visit](/blog/track-daily-user-data-django-user-visit.html)
* [Quickly Use Bootstrap 4 in a Django Template with a CDN](/blog/bootstrap-4-django-template.html)
* [How to Add Maps to Django Web App Projects with Mapbox](/blog/maps-django-web-applications-projects-mapbox.html)

If you have questions or comments about this tutorial, please contact me
via Twitter [@fullstackpython](https://twitter.com/fullstackpython), or
on GitHub [@mattmakai](https://github.com/mattmakai).
See something wrong with this post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/200823-sentry-handle-exceptions-django-projects.markdown)
and submit a pull request.

