title: How to Add User Authentication to Flask Apps with Okta
slug: add-user-authentication-flask-apps-okta
meta: How to quickly add user authentication to Flask web applications using the Okta service.
category: post
date: 2018-10-08
modified: 2018-10-10
newsletter: False
headerimage: /img/181008-flask-okta/header.jpg
headeralt: Flask and Okta logos. Copyright their respective owners.


User authentication is a basic feature in 
[web applications](/web-development.html) so people can create and access 
their own accounts. Unfortunately, authentication is not always easy to
set up and there are many ways to incorrectly implement login and logout
features. 

This tutorial walks through how to use the 
[secure identity authentication service](https://developer.okta.com/use_cases/authentication/)
called [Okta](https://developer.okta.com/), which is free for up to 1,000
active user accounts, to easily handle user data in [Flask](/flask.html) 
applications.


## Our Tools
Python 3 is strongly recommended for building applications and this
tutorial was built with Python 3.7 although earlier versions of Python 3 
should also work fine. In addition to Python 3.x we will also use:

* [Flask](/flask.html) web framework [version 1.0.2](https://pypi.org/project/Flask/1.0.2/)
* [Flask-OIDC](https://flask-oidc.readthedocs.io/en/latest/) where
  OIDC stands for "OpenID Connect". It provides support to use OpenID 
  Connect in Flask applications.
* [Okta Python helper library](https://pypi.org/project/okta/)
* A free [Okta developer account](https://developer.okta.com)

All of the code in this blog post is provided as open source under the 
MIT license on GitHub under the 
[flask-auth-okta directory of the blog-code-examples](https://github.com/fullstackpython/blog-code-examples) 
repository. Use and abuse the source code for applications you want to 
build.


## Installing Dependencies
Create a new Python virtualenv for this project:

```bash
python3 -m venv flaskauth
```

Activate the virtual environment with the `activate` script:

```bash
. ./flaskauth/bin/activate
```

The command prompt should change after activation:

<img src="/img/181008-flask-okta/activate-virtualenv.jpg" width="100%" class="shot rnd outl" alt="Activating the flaskauth virtualenv.">

Remember that you will have to activate the virtualenv in every terminal 
window where you want to use the dependencies contained in this virtualenv.

Now we can install [Flask](/flask.html) and the Okta dependencies.

```
pip install flask>=1.0.2 flask-oidc>=1.4.0 okta==0.0.4
```

Look for output similar to the following to confirm that the dependencies
successfully installed:

```
...
Collecting idna<2.8,>=2.5 (from requests>=2.5.3->okta)
  Downloading https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 16.6MB/s 
Collecting urllib3<1.24,>=1.21.1 (from requests>=2.5.3->okta)
  Downloading https://files.pythonhosted.org/packages/bd/c9/6fdd990019071a4a32a5e7cb78a1d92c53851ef4f56f62a3486e6a7d8ffb/urllib3-1.23-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 143kB 14.0MB/s 
Installing collected packages: MarkupSafe, Jinja2, click, itsdangerous, Werkzeug, flask, pyasn1, pyasn1-modules, rsa, httplib2, six, oauth2client, flask-oidc, chardet, certifi, idna, urllib3, requests, python-dateutil, okta
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for itsdangerous ... done
  Running setup.py install for httplib2 ... done
  Running setup.py install for flask-oidc ... done
  Running setup.py install for okta ... done
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 certifi-2018.8.24 chardet-3.0.4 click-6.7 flask-1.0.2 flask-oidc-1.4.0 httplib2-0.11.3 idna-2.7 itsdangerous-0.24 oauth2client-4.1.3 okta-0.0.4 pyasn1-0.4.4 pyasn1-modules-0.2.2 python-dateutil-2.7.3 requests-2.19.1 rsa-4.0 six-1.11.0 urllib3-1.23
```

We installed our required Flask and the Okta dependencies so let's get to building
the Flask application.


## Creating A Basic Flask App
The first step before adding authentication to our Flask application is
to write some scaffolding functions. The authentication will hook into
these functions, such as `signin` and `signout`, to ensure the auth
process works properly.

Create a directory for your project named `thundercats`. Why `thundercats`?
Why *not* Thundercats?

Within the `thundercats` directly create a file named `app.py` with the 
following initial contents:

```python
# imports for Flask
from flask import Flask, Response


app = Flask(__name__)


@app.route("/lair")
def lair():
    return Response("Thundercats (supposed to be hidden) lair.")


@app.route("/")
def landing_page():
    return Response("Thundercats, Thundercats, hoooooooooooo!")
```

We can run our Flask app using the following command:


```
set FLASK_APP=app.py
flask run
```

Go to localhost:5000 in your web browser and you should see:

<img src="/img/181008-flask-okta/flask-app-running.png" width="100%" class="shot rnd outl" alt="Simple version of Flask application running.">

Now go to our "hidden lair" at localhost:5000/lair/. Eventually this
page should require authentication to access, but for now it appears
without any login challenge:

<img src="/img/181008-flask-okta/flask-app-lair.png" width="100%" class="shot rnd outl" alt="Part of Flask app that should be hidden behind a login page.">

Awesome, our basic app is up and running, let's get to the authentication
functionality.


## Auth-as-a-Service
Head to the [Okta developers sign up page](https://developer.okta.com/signup).

<img src="/img/181008-flask-okta/okta-sign-up.jpg" width="100%" class="shot rnd outl" alt="Okta developers landing page for signing up.">

Sign up for a new account or log into your existing account.

<img src="/img/181008-flask-okta/okta-dev.jpg" width="100%" class="shot rnd outl" alt="Okta developer sign up flow.">

The interesting bit about the Okta developer sign up flow is that now you 
should check your email to finish creating your account. Look for an email 
like this one:

<img src="/img/181008-flask-okta/okta-email.jpg" width="100%" class="shot rnd outl" alt="Okta sign up email.">

Click the "Sign In" button and log into developer account using 
the temporary password found in the email. Set a new password and challenge
question. Then pick an image to match your account login process.

<img src="/img/181008-flask-okta/okta-create-account.png" width="100%" class="shot rnd outl" alt="Okta finish creating an account.">

Click the "Create Account" button and you will be wisked away to the
Okta developer dashboard.

<img src="/img/181008-flask-okta/dev-dashboard.png" width="100%" class="shot rnd outl" alt="Okta developer dashboard.">

Find the "Org URL" as shown in the following image.

<img src="/img/181008-flask-okta/okta-dev-dashboard-url.jpg" width="100%" class="shot rnd outl" alt="Okta Org URL value.">

We are going to use that URL in our secret credentials file so that
our Flask web app can properly connect to the Okta service.

Create a new file in your project directory named 
`openidconnect_secrets.json` with the following contents:

```json
{
  "web": {
    "client_id": "{{ OKTA_CLIENT_ID }}",
    "client_secret": "{{ OKTA_CLIENT_SECRET }}",
    "auth_uri": "{{ OKTA_ORG_URL }}/oauth2/default/v1/authorize",
    "token_uri": "{{ OKTA_ORG_URL }}/oauth2/default/v1/token",
    "issuer": "{{ OKTA_ORG_URL }}/oauth2/default",
    "userinfo_uri": "{{ OKTA_ORG_URL }}/oauth2/default/userinfo",
    "redirect_uris": [
      "http://localhost:5000/oidc/callback"
    ]
  }
}
```

Replace the four `{{ OKTA_ORG_URL }}` placeholders with the Org URL value
found in your dashboard. We will fill in the rest of the placeholders with 
actual values as we proceed through the tutorial. My 
`openidconnect_secret.json` file would currently have the following
values based on my developer dashboard Org URL. 
**Remember that your URL values will be different!**

```json
{
  "web": {
    "client_id": "{{ OKTA_CLIENT_ID }}",
    "client_secret": "{{ OKTA_CLIENT_SECRET }}",
~~    "auth_uri": "https://dev-860408.oktapreview.com/oauth2/default/v1/authorize",
~~    "token_uri": "https://dev-860408.oktapreview.com/oauth2/default/v1/token",
~~    "issuer": "https://dev-860408.oktapreview.com/oauth2/default",
~~    "userinfo_uri": "https://dev-860408.oktapreview.com/oauth2/default/userinfo",
    "redirect_uris": [
      "http://localhost:5000/oidc/callback"
    ]
  }
}
```

Okay awesome, we have our Okta account set up so we can add the 
authentication code to our Flask application.


## Connecting Flask to Okta
We need to connect our Flask code to our new Okta account. The
recommended way of including variables such as account credentials
in a Flask application is through
[configuration handling](http://flask.pocoo.org/docs/1.0/config/) 
so we will use that in our account.

Update the Flask code with the following highlighted lines.

```python
# imports for both Flask and Okta connection
~~from os import environ
from flask import Flask, Response
~~from flask_oidc import OpenIDConnect
~~from okta import UsersClient


app = Flask(__name__)
~~# secret credentials for Okta connection
~~app.config["OIDC_CLIENT_SECRETS"] = "openidconnect_secrets.json"
~~app.config["OIDC_COOKIE_SECURE"] = False
~~app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
~~app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
~~app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
~~app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
~~# instantiate OpenID client to handle user session
~~oidc = OpenIDConnect(app)
~~# Okta client will determine if a user has an appropriate account
~~okta_client = UsersClient(environ.get("OKTA_ORG_URL"),
~~                          environ.get("OKTA_AUTH_TOKEN"))


@app.route("/lair")
def lair():
    return Response("Thundercats (supposed to be hidden) lair.")


@app.route("/")
def landing_page():
    return Response("Thundercats, Thundercats, hoooooooooooo!")
```

We first add three import lines, one to pull values from environment
variables, and the next two imports to make it possible to use OpenID
Connect and Okta in our application.

The rest of the new code sets Flask application configuration
values that can be used to instantiate the OpenID Connect and
Okta clients.

* `OIDC_CLIENT_SECRETS`: the location of the OpenID Connect secrets file
* `OIDC_COOKIE_SECURE`: allows development mode for testing user login and
  registration without SSL. Your application must set this to `True` in a
  production application.
* `OIDC_CALLBACK_ROUTE`: URL in the web app for handling user logins
* `OIDC_SCOPES`: what data to request about the user when they log in. Our
  application requests the basic email, name and profile information
* `SECRET_KEY`: this is a Flask setting to keep sessions secure. The key 
  must never be made public or your web application user sessions will be
  compromised. 

Where do we get those application configuration values though? We
need to obtain them from our Okta account so go back to the
dashboard to create a new OpenID Connect application.

<img src="/img/181008-flask-okta/select-applications.jpg" width="100%" class="shot rnd outl" alt="Select applications on the Okta developer dashboard.">

OpenID Connect applications use a client ID and client secret in
place of traditional usernames and passwords. The client ID and
client secret will tell your authorization server to recognize your 
application. Press the "Add Application" button.

<img src="/img/181008-flask-okta/add-application.jpg" width="100%" class="shot rnd outl" alt="Click the Add Application button.">

On the new application screen choose "Web" and then press "Next".

<img src="/img/181008-flask-okta/web-application.jpg" width="100%" class="shot rnd outl" alt="Choose a web application.">

On the next page there are numerous configuration options but only a 
few values we need to fill in before we can get our credentials. Set
the following values to the `Name`, `Base URIs` and `Login redirect URIs`
properties:

1. **ThunderFlaskCats** for `Name`
1. **http://localhost:5000** for `Base URIs`
1. **http://localhost:5000/oidc/callback** for `Login redirect URIs`

<img src="/img/181008-flask-okta/set-app-configuration.jpg" width="100%" class="shot rnd outl" alt="Set application configuration values.">

Those are the three values you need to fill in for now so save the 
application to create it.

On the next page scroll down to find your client and secret keys.

<img src="/img/181008-flask-okta/client-credentials.jpg" width="100%" class="shot rnd outl" alt="Save the client credentials for later use.">

Copy and paste the client ID and client secret into the following 
highlighted lines to replace the `{{ OKTA_CLIENT_ID }}` and 
`{{ OKTA_CLIENT_SECRET }}` placeholders.

```json
{
  "web": {
~~    "client_id": "{{ OKTA_CLIENT_ID }}",
~~    "client_secret": "{{ OKTA_CLIENT_SECRET }}",
    "auth_uri": "https://dev-860408.oktapreview.com/oauth2/default/v1/authorize",
    "token_uri": "https://dev-860408.oktapreview.com/oauth2/default/v1/token",
    "issuer": "https://dev-860408.oktapreview.com/oauth2/default",
    "userinfo_uri": "https://dev-860408.oktapreview.com/oauth2/default/userinfo",
    "redirect_uris": [
      "http://localhost:5000/oidc/callback"
    ]
  }
}
```

Save the file and make sure to keep it out of version control as those
secret values need to stay secret.

We have one more step in the Okta developer dashboard before we upgrade 
our Flask application with the authentication code: creating an 
[API authentication token](https://developer.okta.com/use_cases/api_access_management/).
Go to the API tab.

<img src="/img/181008-flask-okta/api-tab.jpg" width="100%" class="shot rnd outl" alt="Click the API tab in the dashboard.">

Click the "Create Token" button.

<img src="/img/181008-flask-okta/create-token.png" width="100%" class="shot rnd outl" alt="Create an authentication token to access Okta.">

Name the token `ThunderFlaskCatsToken` and copy it. Save the token somewhere
safe as we will not be able to access it through the dashboard again. We
are going to use this token when setting the `OKTA_AUTH_TOKEN` environment
variable in the next section of this tutorial.


Okay, we finally have all the Okta service configuration and tokens in
our `openidconnect_secret.json` file that we need to finish our application.


## Protecting the Lair
Our configuration is set so update the `app.py` file with the following 
highlighted lines:

```python
# imports for both Flask and Okta connection
from os import environ
~~from flask import Flask, Response, redirect, g, url_for
from flask_oidc import OpenIDConnect
from okta import UsersClient


app = Flask(__name__)
# secret credentials for Okta connection
app.config["OIDC_CLIENT_SECRETS"] = "openidconnect_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
# instantiate OpenID client to handle user session
oidc = OpenIDConnect(app)
# Okta client will determine if a user has an appropriate account
okta_client = UsersClient(environ.get("OKTA_ORG_URL"),
                          environ.get("OKTA_AUTH_TOKEN"))


~~@app.before_request
~~def before_request():
~~    if oidc.user_loggedin:
~~        g.user = okta_client.get_user(oidc.user_getfield("sub"))
~~    else:
~~        g.user = None


@app.route("/lair")
~~@oidc.require_login
def lair():
    return Response("Thundercats (supposed to be hidden) lair.")


@app.route("/")
def landing_page():
    return Response("Thundercats, Thundercats, hoooooooooooo!")


~~@app.route("/login")
~~@oidc.require_login
~~def login():
~~    return redirect(url_for(".lair"))
~~
~~
~~@app.route("/logout")
~~def logout():
~~    oidc.logout()
~~    return redirect(url_for(".landing_page"))
```

The above new highlighted lines check whether or not a user is logged in
before each request. If a route requires a logged in user due to the 
`@oidc.require_login` decorator then the user will be redirect to the
sign in page. We also added routes under `/login` and `/logout` to make
it possible to log in and out of the application.

Set three environment variables so our application can use them when we
run it. Make sure the placeholders `ORG_URL` and `AUTH_TOKEN` are set with 
your actual Org URL value and auth token from the Okta developer dashboard.

On the command line run the following commands, making sure to replace
any placeholder values with your own tokens and URLs:

```
# this tells Flask we want to run the built-in server in dev mode
export FLASK_ENV=development
# make sure to use a very long random string here that cannot be guessed
export SECRET_KEY='a very long string with lots of numbers and letters'
# this is the same Org URL found on your developer dashboard
# for example, https://dev-860408.oktapreview.com
export OKTA_ORG_URL='ORG_URL'
# this is the API authentication token we created
export OKTA_AUTH_TOKEN='AUTH_TOKEN'
```

Now re-run the Flask application:

```
set FLASK_APP=app.py
flask run
```

You should be in good shape if the development server starts up with output
like this:

```
(flaskauth)$ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 415-920-546
```

Head to localhost:5000 in a browser where you are not already logged into
your Okta account (an incognito window of your web browser works great).

<img src="/img/181008-flask-okta/landing-page-incognito.png" width="100%" class="shot rnd outl" alt="Landing page while in incognito mode.">


Let's test the redirect functionality when we try to go to the `/lair`
route by going to localhost:5000/lair. We get redirected to the Okta
login page.

<img src="/img/181008-flask-okta/lair-redirect.jpg" width="100%" class="shot rnd outl" alt="Getting redirected while in incognito mode.">

Enter your Okta developer username and password to log into your application.
For development purposes this will work fine for testing but obviously in a
production application you will create other accounts for users to log into.

<img src="/img/181008-flask-okta/enter-lair.jpg" width="100%" class="shot rnd outl" alt="Got into the lair URL after logging in.">

Let's tweak one more bit in our application to fix the glaring lack of
excitement in successfully completing the authentication code for this 
tutorial. Update the two highlighted lines to match what is in the code
block below:

```python
# imports for both Flask and Okta connection
from os import environ
from flask import Flask, Response, redirect, g, url_for
from flask_oidc import OpenIDConnect
from okta import UsersClient


app = Flask(__name__)
# secret credentials for Okta connection
app.config["OIDC_CLIENT_SECRETS"] = "openidconnect_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
# instantiate OpenID client to handle user session
oidc = OpenIDConnect(app)
# Okta client will determine if a user has an appropriate account
okta_client = UsersClient(environ.get("OKTA_ORG_URL"),
                          environ.get("OKTA_AUTH_TOKEN"))


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


@app.route("/lair")
@oidc.require_login
def lair():
~~    thundercats_lair = '<html><head><title>Thundercats, hoooo!</title></head><body><h1>Thundercats now hidden lair.</h1><iframe src="https://giphy.com/embed/ahXtBEbHiraxO" width="480" height="273" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/retro-cartoons-thundercats-ahXtBEbHiraxO">via GIPHY</a></p></body></html>'
~~    return Response(thundercats_lair)


@app.route("/")
def landing_page():
    return Response("Thundercats, Thundercats, hoooooooooooo!")


@app.route("/login")
@oidc.require_login
def login():
    """Force user to login and then redirect them to the lair.
    """
    return redirect(url_for(".lair"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".landing_page"))
```

Refresh the lair page.

<img src="/img/181008-flask-okta/refreshed-lair.jpg" width="100%" class="shot rnd outl" alt="Lair page with new GIF.">

Alright that's just a little bit better! Go to localhost:5000/logout to 
unauthenticate your user. When you go to localhost:5000/lair again you 
will now have to re-authenticate. 


## What Now?
We just built an example Flask application with user authentication via 
the [Okta API](https://developer.okta.com/use_cases/api_access_management/).

Next up try the following tutorials to add other features to your
Flask application:

* [Responding to SMS Text Messages with Python & Flask](/blog/respond-sms-text-messages-python-flask.html)
* [How to Add Hosted Monitoring to Flask Web Applications](/blog/hosted-monitoring-flask-web-apps.html)
* [Develop and Run Flask Apps within Docker Containers](/blog/develop-flask-web-apps-docker-containers-macos.html)

You can also determine what to code next in your Python project by reading 
the [Full Stack Python table of contents page](/table-of-contents.html).

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/181008-add-user-auth-flask-okta.markdown)
and submit a pull request.
