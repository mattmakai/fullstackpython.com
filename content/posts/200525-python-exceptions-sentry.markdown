title: Reporting Exceptions in Python Scripts with Sentry
slug: report-exceptions-python-scripts-sentry
meta: Learn how to catch exceptions in Python scripts and then use Sentry to store and analyze the errors.
category: post
date: 2020-05-25
modified: 2020-05-25
newsletter: False
headerimage: /img/200525-sentry/header.jpg
headeralt: Python and Sentry logos. Copyright their respective owners.


Python scripts are the glue that keep many applications and their 
infrastructure running, but when one of your scripts throws an exception 
you may not know about it immediately unless you have a central place to 
aggregate the errors. That's where adding [Sentry](https://sentry.io/)
can solved this distributed error logging problem. 

In this tutorial, we'll see how to quickly add Sentry to a new or existing 
Python script to report errors into a centralized location for further 
[debugging](/debugging.html).


## Development environment setup
Make sure you have Python 3 installed. As of right now, 
[Python 3.8.3](https://www.python.org/downloads/) is the latest
version of Python.

During this tutorial we're also going to use: 

* a hosted Sentry instance on [sentry.io](https://sentry.io), which we'll
  need an account to access
* the [Sentry Python helper library](https://pypi.org/project/sentry-sdk/) to
  send exception data to our Sentry instance


Install the above code libraries into a new 
[Python virtual environment](/virtual-environments-virtualenvs-venvs.html)
using the following commands:

```bash
python -m venv sentryscript
source sentryscript/bin/activate

pip install sentry-sdk>=0.14.4
```

Our [development environment](/development-environments.html) is now 
ready and we can write some code that will throw exceptions to demonstrate
how to use Sentry.

Note that all of the code for this tutorial can be found within the
[blog-code-examples](https://github.com/fullstackpython/blog-code-examples)
Git repository on GitHub under the 
[python-script-sentry](https://github.com/fullstackpython/blog-code-examples/tree/master/python-script-sentry)
directory.


## An Example Script for Loading Python Modules
We'll start by writing a small but useful script that prints out the
names of all modules within a Python package, then add Sentry to it
when it becomes apparent that capturing exceptions would be a
useful addition.

Create a new file named `module_loader.py` and write the
following lines of code in it to allow us to easily execute it
on the command line.

```python
import argparse

def import_submodules(package):
    return {}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("package")
    args = parser.parse_args()

    package_to_load = args.package
    results = import_submodules(package_to_load)
    for r in results:
        print(str(r))
```

The above code takes an argument when the script is invoked from the
command line and uses the value as an input into the stub
`import_submodules` function that will contain code to walk the
tree of modules within the package.

Nextt, add the following highlighted lines of code to use `importlib` and
`pkgutil` to recursively import modules from the package if one is
found that matches the name sent in as the `package` argument.

```python
import argparse
~~import importlib
~~import pkgutil


def import_submodules(package):
~~    """Import all submodules of a module, recursively, including subpackages.

~~    :param package: package (name or actual module)
~~    :type package: str | module
~~    :rtype: dict[str, types.ModuleType]
~~    """
~~    if isinstance(package, str):
~~        package = importlib.import_module(package)
~~    results = {}
~~    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
~~        full_name = package.__name__ + '.' + name
~~        try:
~~            results[full_name] = importlib.import_module(full_name)
~~            if is_pkg:
~~                results.update(import_submodules(full_name))
~~        except ModuleNotFoundError as mnfe:
~~            print("module not found: {}".format(full_name))
~~        except Exception as general_exception:
~~            print(general_exception)
~~    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("package")
    args = parser.parse_args()

    package_to_load = args.package
    results = import_submodules(package_to_load)
    for r in results:
        print(str(r))
```

The new code above loops through all packages with the
`walk_package` function in the `pkgutil` standard library
module and tries to import it using the `import_module` on
the package name plus package as a string. If the
result is successful, the function will recursively call
itself to import submodules within the imported package.
If a module is not found, or some other issue occurs, exceptions
are caught so that the script does not fail but instead can
continue processing potential modules.

Test the full script to see what it prints out with an arbitrary
package on the command line:

```bash
python module_loader.py importlib
```

The above example generates the output:

```bash
importlib._bootstrap
importlib._bootstrap_external
importlib.abc
importlib.machinery
importlib.resources
importlib.util
```

Trying to inspect a package that is not installed will give an error. Use
the script with a package that is not installed in your current environment.

```bash
python module_loader.py flask
```

The above command produces the following traceback due to an expected 
`ModuleNotFoundError`.

```
Traceback (most recent call last):
  File "module_loader.py", line 35, in <module>
    results = import_submodules(package_to_load)
  File "module_loader.py", line 14, in import_submodules
    package = importlib.import_module(package)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 965, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'flask'
```

If you install Flask into your current environment the module is found and
the application will go through the list of modules and submodules.

Our example script is usable but what if we run this code or something similar
on one or more servers that we don't check that often? That's where it would
be helpful to have a way to aggregate one or more scripts' exception output
in a single place. Sentry can help us to accomplish that goal.


## Adding Exception Reporting with Sentry
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
expected because we have not yet connected our account to the Python 
script.

<img src="/img/200525-sentry/sentry-empty-dashboard.jpg" width="100%" class="shot rnd outl" alt="Blank Sentry account dashboard.">

You'll want to create a new Sentry Project just for this application so
click "Projects" in the left sidebar to go to the Projects page.

<img src="/img/200525-sentry/create-project.jpg" width="100%" class="shot rnd outl" alt="Button to create a new Sentry project.">

On the Projects page, click the "Create Project" button in the top right
corner of the page.

<img src="/img/200525-sentry/create-new-project-screen.jpg" width="100%" class="shot rnd outl" alt="Create a new Sentry project.">

Select Python, give your new Project a name and then press the "Create Project"
button. Our new project is ready to integrate with our Python script.

We need the unique identifier for our account and project to authorize our
Python code to send errors to this Sentry instance. The easiest way to get
what we need is to go to the 
[Python getting started documentation page](https://docs.sentry.io/error-reporting/quickstart/?platform=python)
and scroll down to the "Configure the SDK" section.

<img src="/img/200525-sentry/python-sentry-quickstart.jpg" width="100%" class="shot rnd outl" alt="The Sentry docs show you exactly what you need to export to connect to your account.">

Copy the string parameter for the `init` method and 
[set it as an environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) 
rather than exposing it directly in your application code.

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

Modify the application to send exception information to Sentry now 
that we have our unique identifier. Open `module_loader.py` again and
update the following highlighted lines of code.

```python
import argparse
import importlib
~~import os
import pkgutil
~~import sentry_sdk
~~from sentry_sdk import capture_exception

~~# find on https://docs.sentry.io/error-reporting/quickstart/?platform=python
~~sentry_sdk.init(dsn=os.getenv('SENTRY_DSN'))


def import_submodules(package):
    """Import all submodules of a module, recursively, including subpackages.

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        try:
            results[full_name] = importlib.import_module(full_name)
            if is_pkg:
                results.update(import_submodules(full_name))
        except ModuleNotFoundError as mnfe:
            print("module not found: {}".format(full_name))
~~            capture_exception(mnfe)
        except Exception as general_exception:
            print(general_exception)
~~            capture_exception(general_exception)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("package")
    args = parser.parse_args()

    package_to_load = args.package
    results = import_submodules(package_to_load)
    for r in results:
        print(str(r))
```

These new lines of code import the 
[Sentry Python SDK](https://github.com/getsentry/sentry-python) and `os`
library (to read system environment variables). The application then
initializes the Sentry SDK with the string found in the `SENTRY_DSN`
environment variable. Down in the `import_submodules` function we
then call the `capture_exception` SDK function whenever a
`ModuleNotFoundException` is thrown or another exception which would
be caught within the broader `Exception` bucket.

Now that our code is in place, let's test out the new Sentry integration.


## Testing the Script and Viewing Exceptions
The easiest way to test out whether the Sentry code is working or not is
to try to import a module that does not exist. Let's say you make a
typo in your command and try to run the script on `importliba` instead
of `importlib` (maybe because you are using an awful Macbook Pro "butterfly"
keyboard instead of a durable keyboard). Try it out and see what happens:

```bash
python module_loader.py importliba
```

The script will run and finish but there will be errors because that
module does not exist. Thanks to our new code, we can view the
errors in Sentry.

Check the Sentry dashboard to see the error.

<img src="/img/200525-sentry/exception-in-dashboard.jpg" width="100%" class="shot rnd outl" alt="Viewing the first exception in the Sentry dashboard.">

We can also click into the error to learn more about what happened.

<img src="/img/200525-sentry/detailed-error-report.jpg" width="100%" class="shot rnd outl" alt="The exception details in the Sentry dashboard.">

You can also receive email reports on the errors that occur so that
you do not have to always stay logged into the dashboard.

<img src="/img/200525-sentry/sentry-email.jpg" width="100%" class="shot rnd outl" alt="The exception via email.">

With that all configured, we've now got a great base to expand the script 
and build better error handling with Sentry as our Python application 
becomes more complex.


## What's Next?
We just created an example script that outputs all of the modules and 
submodules in a package, then added Sentry to it so that it would report 
any exceptions back to our central hosted instance.

That's just a simple introduction to Sentry, so next you'll want to
read one of the following articles to do more with it:

* [Python Sentry docs](https://docs.sentry.io/platforms/python/)
* [How to use Sentry with Flask](https://docs.sentry.io/platforms/python/flask/)
* [Integrating Sentry into Celery task queues](https://docs.sentry.io/platforms/python/celery/)

You can also get an idea of what to code next in your Python project by 
reading the 
[Full Stack Python table of contents page](/table-of-contents.html).

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/200525-python-exceptions-sentry.markdown)
and submit a pull request.
