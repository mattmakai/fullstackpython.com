title: Dialing Outbound Phone Calls with a Bottle Web App
slug: dial-outbound-phone-calls-python-bottle
meta: A tutorial that shows how to dial outbound phone calls with a Bottle web application built with Python 3.
category: post
date: 2016-08-30
modified: 2017-06-16
newsletter: False
headerimage: /img/160830-phone-calls-bottle/header.jpg
headeralt: Bottle, Python and Twilio logos. Copyright their respective owners.


Python web apps built with the [Bottle web framework](/bottle.html) can 
[send](/blog/send-sms-text-messages-python.html) and 
[receive SMS text messages](/blog/reply-sms-text-messages-python-bottle.html).
In this tutorial we will go beyond texting and learn how to dial outbound 
phone calls. The calls will read a snippet of text then play an MP3 file,
but they can then be easily modified to create conference lines and many
other voice features in your Python web apps.


## Tools We Need
You should have either [Python 2 or 3](/python-2-or-3.html) installed to
create your Bottle app, although Python 3 is recommended for new 
applications. We also need:

* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle
  [application dependencies](/application-dependencies.html)
* [Ngrok](https://ngrok.com/) for localhost tunneling to our Bottle
  application while it's running on our local development environment
* [Bottle](/bottle.html) web framework
* Free [Twilio account](https://www.twilio.com/try-twilio) to use their 
  [phone calling web API](https://www.twilio.com/docs/api/rest/making-calls)
* Twilio's 
  [Python helper library](https://www.twilio.com/docs/libraries/python),
  which is [open source on GitHub](https://github.com/twilio/twilio-python) 
  and [available for download from PyPI](https://pypi.org/project/twilio)

Take a look at 
[this guide on setting up Python 3, Bottle and Gunicorn on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html)
if you need help getting your 
[development environment](/development-environments.html) 
configured before continuing on through the remainder of this tutorial.

You can snag all the open source code for this tutorial in the 
[python-bottle-phone](https://github.com/mattmakai/python-bottle-phone)
GitHub repository under the 
[outbound directory](https://github.com/mattmakai/python-bottle-phone/tree/master/outbound-calls). 
Use and copy the code however you want - it's all open source under the 
MIT license.


## Installing Our Application Dependencies
Our Bottle app needs a helper code library to make it easy to dial outbound
phone calls. Bottle and the Twilio helper library are installable from 
[PyPI](https://pypi.python.org/pypi) into a virtualenv. Open your terminal 
and use the `virtualenv` command to create a new virtualenv:

```
virtualenv bottlephone
```

Use the `activate` script within the virtualenv, which makes this virtualenv
the active Python installation. Note that you need to do this in every 
terminal window that you want this virtualenv to be used.

```
source bottlephone/bin/activate
```

The command prompt will change after activating the virtualenv
to something like `(bottlephone) $`. Here is a screenshot of what my
environment looked like when I used the `activate` script.

<img src="/img/160830-phone-calls-bottle/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded">

Next use the `pip` command to install the [Bottle](/bottle.html) and 
[Twilio Python](https://www.twilio.com/docs/libraries/python) packages
into your virtualenv.

    pip install bottle twilio==5.7.0


After the installation script finishes, we will have the required 
dependencies to build our app. Time to write some Python code to dial 
outbound phone calls.


## Bottle and Twilio
Our simple Bottle web app will have three routes: 

* `/` - returns a text string to let us know our Bottle app is running
* `/twiml` - responds with [TwiML](https://www.twilio.com/docs/api/twiml) 
  (a simple subset of XML) that instructs Twilio what to do when someone
  picks up the call to them from our Bottle web app
* `/dial-phone/<outbound_phone_number>`, where "outbound_phone_number" is
  a phone number in the format "+12025551234" - this route uses the Twilio
  helper library to send a POST request to the Twilio Voice API to dial a
  phone  call

We can build the structure of our Bottle app and the first route right now.
Create a new file named `app.py` with the following contents to start our
app.

```python
import os
import bottle
from bottle import route, run, post, Response
from twilio import twiml
from twilio.rest import TwilioRestClient


app = bottle.default_app()
# plug in account SID and auth token here if they are not already exposed as
# environment variables
twilio_client = TwilioRestClient()

TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', '+12025551234')
NGROK_BASE_URL = os.environ.get('NGROK_BASE_URL', 'https://c6c6d4e8.ngrok.io')


@route('/')
def index():
    """
    Returns a standard text response to show the app is up and running.
    """
    return Response("Bottle app running!")


if __name__ == '__main__':
    run(host='127.0.0.1', port=8000, debug=False, reloader=True)
```

Make sure you are in the directory where you created the above `app.py`
file. Run the app via the Bottle development server with the following 
command. Make sure your virtualenv is still activated so our code can rely 
on the Bottle code library.

```
python app.py
```

We should see a successful development server start up like this:

```
(bottlephone) matt@ubuntu:~/bottlephone$ python app.py 
Bottle v0.12.9 server starting up (using WSGIRefServer())...
Listening on http://127.0.0.1:8000/
Hit Ctrl-C to quit.
```

Here is what the development server message looks like in my environment 
on Ubuntu:

<img src="/img/160830-phone-calls-bottle/bottle-app-running.png" width="100%" class="technical-diagram img-rounded" alt="Successfully starting the Bottle development server from the command line.">

Let's test out the app by going to "localhost:8000"
in the web browser. We should get a simple success message that the app
is running and responding to requests.

<img src="/img/160830-phone-calls-bottle/bottle-app-web-browser.png" width="100%" class="technical-diagram img-rounded" alt="Simple success message in the web browser that the Bottle app is running.">

Next we need to obtain a phone number that our Bottle app can use to 
call other phone numbers.


## Obtain a Phone Number
Our basic Bottle web app is running but what we really want to do is dial
outbound calls - which will be handled by [Twilio](https://www.twilio.com/).

In your web browser go to the
[Twilio website and sign up for a free account](https://www.twilio.com/try-twilio). 
You can also sign into your existing Twilio account if you already have one.

<img src="/img/160830-phone-calls-bottle/try-twilio.png" width="100%" class="technical-diagram img-rounded" alt="Twilio sign up screen.">

The Twilio trial account allows you to dial and receive phone calls to 
your own validated phone number. To dial and receive calls from any phone 
number then you need to upgrade your account (hit the upgrade button on the
top navigation bar to do that). Trial accounts are great for initial 
development before your application goes live but upgraded accounts are where
the real power comes in.

Once you are signed into your Twilio account, go to the 
[manage phone numbers screen](https://www.twilio.com/console/phone-numbers).
On this screen you can 
[buy one or more phone numbers](https://www.twilio.com/console/phone-numbers/search)
or click on an existing phone number in your account to configure it.

<img src="/img/160830-phone-calls-bottle/manage-phone-numbers.png" width="100%" class="technical-diagram img-rounded" alt="Manage phone numbers screen.">

There is nothing for us to configure right now on the phone number 
configuration page because we are making outbound phone calls for this 
tutorial. Now that we have a phone number in hand, let's add the final bit
of code to our Bottle app to get this app working.


## Making Phone Calls
We need to add two new routes to our Bottle app so it can dial outbound
phone calls. Modify your existing app.py file with the two new functions
below, `twiml_response` and `outbound_call`. None of the other code in
this file needs to change other than adding those two new functions to
what we wrote in the previous section.

```python
import os
import bottle
from bottle import route, run, post, Response
from twilio import twiml
from twilio.rest import TwilioRestClient


app = bottle.default_app()
# plug in account SID and auth token here if they are not already exposed as
# environment variables
twilio_client = TwilioRestClient()

# add your Twilio phone number here
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', '+16093002984')
# plug in your Ngrok Forwarding URL - we'll set it up in a minute
NGROK_BASE_URL = os.environ.get('NGROK_BASE_URL', 'https://c6c6d4e8.ngrok.io')


@route('/')
def index():
    """
    Returns a standard text response to show the app is up and running.
    """
    return Response("Bottle app running!")


@post('/twiml')
def twiml_response():
    """
    Provides TwiML instructions in response to a Twilio POST webhook
    event so that Twilio knows how to handle the outbound phone call
    when someone picks up the phone.
    """
    response = twiml.Response()
    response.say("Sweet, this phone call is answered by your Bottle app!")
    response.play("https://api.twilio.com/cowbell.mp3", loop=10)
    return Response(str(response))


@route('/dial-phone/<outbound_phone_number>')
def outbound_call(outbound_phone_number):
    """
    Uses the Twilio Python helper library to send a POST request to
    Twilio telling it to dial an outbound phone call from our specific
    Twilio phone number (that phone number must be owned by our Twilio 
    account).
    """
    # the url must match the Ngrok Forwarding URL plus the route defined in
    # the previous function that responds with TwiML instructions
    twilio_client.calls.create(to=outbound_phone_number, 
                               from_=BLOG_POST_NUMBER,
                               url=NGROK_BASE_URL + '/twiml')
    return Response('phone call placed to ' + outbound_phone_number + '!')


if __name__ == '__main__':
    run(host='127.0.0.1', port=8000, debug=False, reloader=True)
```

There is just one problem with our current setup if you're developing on
a local environment: Twilio won't be able to reach that `/twiml` route. 
We need to deploy our app to a reachable server, or just use a localhost 
tunneling tool like [Ngrok](https://ngrok.com). Ngrok provides an external
URL that connects to a port running on your machine. 
[Download and install the Ngrok application](https://ngrok.com/download) 
that is appropriate for your operating system.

We run Ngrok locally and expose our Bottle app that is running on 
port 8000. Run this command within the directory where the Ngrok executable is
located.

    ./ngrok http 8000 

Ngrok will start up and provide us with a Forwarding URL, with both HTTP
and HTTPS versions.

<img src="/img/160830-phone-calls-bottle/start-ngrok.png" width="100%" class="technical-diagram img-rounded" alt="Ngrok started and running to serve as a localhost tunnel.">

We can use the Forwarding URL to instruct Twilio how to handle the outbound
phone call when someone picks up. Insert the Ngrok forwarding URL into the
`app.py` file where `NGROK_BASE_URL` is specified.

<img src="/img/160830-phone-calls-bottle/access-ngrok.png" width="100%" class="technical-diagram img-rounded" alt="Paste the ngrok Forwarding URL into the Twilio webhook configuration text box.">

If Ngrok is useful to you, make sure to read this 
[6 awesome reasons to use Ngrok when testing webhooks post](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html) 
to learn even more about the tool.

Time to test out our app, let's give it a quick spin.


## Making Phone Calls
Make sure your Bottle development server is still running or re-run it with
the `python app.py` command in a shell where your virtualenv is still
activated.

Bring up the application in a browser, this time test out the phone calling
capabilities. Go to "localhost:8000/dial-phone/my-phone-number", where 
"my-phone-number" is a number in the "+12025551234" format. For example,
here is what happens when I dialed +12023351278:

<img src="/img/160830-phone-calls-bottle/phone-call-placed.png" width="100%" class="technical-diagram img-rounded" alt="Dialing an outbound phone call with Bottle.">

And here is the inbound phone call!

<img src="/img/160830-phone-calls-bottle/inbound-call.png" width="100%" class="technical-diagram img-rounded" alt="Receiving an incoming phone call on the iPhone.">

When we pick up the phone call we also see the `/twiml` route get called via
Ngrok.

<img src="/img/160830-phone-calls-bottle/ngrok-twiml.png" width="100%" class="technical-diagram img-rounded" alt="/twiml route being called via Ngrok.">

With just two routes in our Bottle app and Twilio we were able to make
outbound phone calls. Not bad!


## What's next?
Sweet, we can now dial outbound phone calls to *any* phone number from
our Bottle web application. Next you may want to try one of these tutorials 
to add even more features to your app:

* Upgrade your [Bottle app to also send and respond to text messages](/blog/reply-sms-text-messages-python-bottle.html)
* Create a [phone-calling Slack bot](https://www.twilio.com/blog/2016/05/add-phone-calling-slack-python.html)
* Implement [call tracking](https://www.twilio.com/docs/tutorials/walkthrough/call-tracking/python/django)
  for both inbound and outbound phone calls made through your app

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub as
[mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160830-phone-calls-bottle.markdown)
and submit a pull request.
