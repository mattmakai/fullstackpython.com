title: Replying to SMS Text Messages with Python and Bottle
slug: reply-sms-text-messages-python-bottle
meta: A short walkthrough for how to reply to SMS text messages in a Bottle web application built with Python.
category: post
date: 2016-06-05
modified: 2016-08-10
newsletter: False
headerimage: /img/160605-reply-sms-python-bottle/header.jpg
headeralt: Twilio, Python and Bottle logos. Copyright their respective owners.


Python applications can 
[easily send SMS](/blog/send-sms-text-messages-python.html) 
by using a [web API](/application-programming-interfaces.html). 
Web apps built with the [Bottle](/bottle.html) framework can also reply
to incoming text messages by handling inbound HTTP POST webhooks. In
this post we'll quickly walk through how to set up a Bottle web app to
handle SMS data in the form of HTTP POST requests.


## Tools We'll Need
This tutorial works with either [Python 2 or 3](/python-2-or-3.html), 
although Python 3 is recommended by the community for new applications. 
Install one of those two Python versions on your system to use for this
walkthrough. We also need:

* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle
  [application dependencies](/application-dependencies.html)
* [Bottle](/bottle.html) web framework
* [Ngrok](https://ngrok.com/) for localhost tunneling to our Bottle
  application while it's running on our local development environment
* Free [Twilio account](https://www.twilio.com/try-twilio) to use their 
  [SMS web API](https://www.twilio.com/docs/api/rest/sending-messages)
* Open source 
  [Twilio Python helper library](https://pypi.org/project/twilio),
  version 5.7.0 or earlier

Check out the guide on 
[how to set up Python 3, Bottle and Gunicorn on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html)
if you need help getting your 
[development environment](/development-environments.html) 
configured.


## Application Dependency Installation
Our application will use a helper code library to reply to inbound SMS.
Bottle and the helper library are installable from 
[PyPI](https://pypi.python.org/pypi) into a virtualenv. Open your terminal 
and use the `virtualenv` command to create a new virtualenv:

    virtualenv replysms


Invoke the virtualenv's `activate` script, which makes it the "active" 
Python installation. Note that you need to do this in every terminal window
that you want this virtualenv to be used.

    source replysms/bin/activate


The command prompt will change after activating the virtualenv:

<img src="/img/160605-reply-sms-python-bottle/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded">


Use the `pip` command to install the [Bottle](/bottle.html) and 
[Twilio Python](https://www.twilio.com/docs/libraries/python) packages
into your virtualenv.

    pip install bottle twilio==5.7.0


We have installed the required dependencies so now Python code that is run 
with the virtualenv activated will be able to use those packages. It's time 
to build our Bottle web app and reply to incoming text messages.


## Coding Our Bottle App
The Bottle web app will have two routes. One route will allow us to test
that the app is running. The other route will handle and respond to incoming
HTTP POST requests from Twilio. Create a new file named `app.py` in your 
in the directory where you want to store this Python project.

Write the following code in the new `app.py` file. There is also
[a GitHub Gist](https://gist.github.com/mattmakai/6ec3b46e40a1020a3ea9c772c601199a) 
with the code that you can copy and paste.

```python
from bottle import (post, request, response, route, run, )
from twilio import twiml


@route('/')
def check_app():
    # returns a simple string stating the app is working
    return "It works!"


@post('/twilio')
def inbound_sms():
    twiml_response = twiml.Response()
    # grab message from the request. could also get the "To" and 
    # "From" phone numbers as well from parameters with those names
    inbound_message = request.forms.get("Body")
    # we can now use the incoming message text in our Python application
    if inbound_message == "Hello":
        twiml_response.message("Hello from Bottle right back at you!")
    else:
        twiml_response.message("Hi! Not quite sure what you meant, but okay.")
    # we return back the mimetype because Twilio needs an XML response
    response.content_type = "application/xml"
    return str(twiml_response)


if __name__ == '__main__':
    run(host='127.0.0.1', port=5000, debug=True, reloader=True)
```

The lines starting with `#` are comments that give explanations for what
the code lines below them are doing. Bottle web apps define URL routes with 
the `@route` and `@post` decorators, depending on the type of HTTP request
the route should handle. 

Make sure your virtualenv is still active so that the application can use 
the Bottle and Twilio code libraries we installed earlier. Give the 
application a try by running it with `python app.py`. 

Open a web browser and go to localhost:5000 (or 127.0.0.1:5000). We should
see "It works!" on the screen.

<img src="/img/160605-reply-sms-python-bottle/bottle-app-local.jpg" width="100%" class="technical-diagram img-rounded" alt="Bottle application running locally on Ubuntu.">

However, there is an issue with our web app running on our local development
environment. Twilio cannot send a the HTTP POST request to the web app
server unless a localhost tunnel is created.


## Ngrok Localhost Tunneling
[Ngrok](https://ngrok.com) is a localhost tunneling tool that bridges
your local development environment to an external URL. 
[Download and install](https://ngrok.com/download) the Ngrok version that's
appropriate for your operating system.

We can run Ngrok locally and expose our Bottle app that is running on 
port 5000. Run this command within the directory where the Ngrok executable is
located.

    ./ngrok http 5000 
 
<img src="/img/160605-reply-sms-python-bottle/start-ngrok.jpg" width="100%" class="technical-diagram img-rounded" alt="Ngrok started and running to serve as a localhost tunnel.">

Cool, now we can use the Forwarding URL so Twilio can send POST requests
to our application when there is an inbound SMS. Replace the URL in the
text box with your own Forwarding URL, like I did in this screenshot.

<img src="/img/160605-reply-sms-python-bottle/access-ngrok.jpg" width="100%" class="technical-diagram img-rounded" alt="Paste the ngrok Forwarding URL into the Twilio webhook configuration text box.">

Now we just need a Twilio phone number that will send POST request to our
application when there is an inbound SMS.


## Obtain a Phone Number
Our Bottle web app's route can respond to incoming POST requests but we
need to use Twilio to have a phone number that will convert the inbound SMS
data into the POST request. In your web browser go to the
[Twilio website and sign up for a free account](https://www.twilio.com/try-twilio). 
You can also sign into your existing Twilio account if you already have one.

<img src="/img/160605-reply-sms-python-bottle/try-twilio.png" width="100%" class="technical-diagram img-rounded" alt="Twilio sign up screen.">

The Twilio trial account allows you to send and receive text messages to 
your own validated phone number. To send and reply to SMS to and from any 
phone number then you need to upgrade your account. Trial accounts are 
great for initial development before your application goes live.

When you sign up, you receive a free Twilio phone number. We can
configure that phone number to forward the SMS information to our web 
application by setting up the response webhook.

Go to the 
[manage phone numbers screen](https://www.twilio.com/console/phone-numbers) 
and click on the phone number you want to configure for replying to 
text messages.

Scroll down and look for the "Messaging" header. Change the 
"A Message Comes in" text box to input the ngrok Forwarding URL plus 
the "/twilio" route, as shown in the screenshot below.

<img src="/img/160605-reply-sms-python-bottle/webhook-ngrok.jpg" width="100%" class="technical-diagram img-rounded" alt="Paste the ngrok Forwarding URL into the Twilio webhook configuration text box.">

Click the "Save" button so that our changes take effect.

Our application is ready to go - time to give our phone number a try! 
Send "Hello" or whatever text you want to your phone number. Here is what 
the result looks like on my iPhone.

<img src="/img/160605-reply-sms-python-bottle/bottle-success.png" width="100%" class="technical-diagram img-rounded" alt="Example screenshot of what SMS replies look like on the iPhone.">

The concise Bottle web app is a good start to build more complicated
programs such as 
[Choose Your Own Adventure Presentations](https://www.twilio.com/blog/2014/11/choose-your-own-adventure-presentations-with-reveal-js-python-and-websockets.html)
or
[SMS Slack bots](https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html).


## What's next?
Awesome, our Bottle application now replies to inbound SMS text
messages! 

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160605-reply-sms-python-bottle.markdown)
and submit a pull request.
