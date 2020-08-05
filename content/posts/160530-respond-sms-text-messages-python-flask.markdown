title: Responding to SMS Text Messages with Python & Flask
slug: respond-sms-text-messages-python-flask
meta: A quick tutorial on receiving and responding to SMS text messages in a Flask application built with Python.
category: post
date: 2016-05-30
modified: 2020-08-05
newsletter: False
headerimage: /img/160530-respond-sms-python-flask/header.jpg
headeralt: Twilio, Python and Flask logos. Copyright their respective owners.


Short Message Service (SMS) text messages are 
[easy to send from Python applications](/blog/send-sms-text-messages-python.html) 
with a
[web application programming interface (API)](/application-programming-interfaces.html). 
Flask applications can also receive incoming text messages and respond
back to the sender with just a few lines of Python code.


## Tools We Need
This tutorial is fine for both Python 2 and 3. Make sure you have one of 
those two versions installed on your system.

* Either [Python 2 or 3](/python-2-or-3.html)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle
  [application dependencies](/application-dependencies.html)
* The [Flask](/flask.html) micro web framework
* A free [Twilio account](www.twilio.com/referral/w9pugq) to use their 
  [SMS web API](https://www.twilio.com/docs/api/rest/sending-messages)
* Open source 
  [Twilio Python helper library](https://pypi.org/project/twilio)
* [Ngrok](https://ngrok.com/) for localhost tunneling to our Flask 
  application while it's running on our local development environment

If you need assistance getting pip and virtualenv installed, take a look at 
the first few steps in the 
[how to set up Python 3, Flask and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
guide, which shows how to install system packages for those tools.


## Installing Our Dependencies
Our code will use a helper library to make it easier to respond to text 
messages from Python. The helper library dependency along with the Flask
code library can be installed from [PyPI](https://pypi.python.org/pypi) into 
a virtualenv. In your terminal use the following command to generate a new 
virtualenv. 

    virtualenv respondsms


Activate the virtualenv.

    source respondsms/bin/activate


The command prompt will change after we properly activate the virtualenv
to something like this:

<img src="/img/160530-respond-sms-python-flask/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded">


Install Flask and the Twilio Python helper library into the virtualenv with
the `pip` command. 

    pip install flask twilio==5.7.0


The dependencies are installed so that we can use it with our Python code.
Now we can write our Python application.


## Building Our Flask Web App
Our Flask application will have two routes: one to make sure the web app
is running and another that handles incoming HTTP POST requests. Create
a new file named `app.py` in your home directory or where you choose to
store your Python project files.

Within `app.py` write the following code. You can also see 
[this code in a GitHub Gist](https://gist.github.com/mattmakai/8ab434ccb604d3ba5bde817a183e0bde) 
if that's easier to copy and paste.


    from flask import Flask, Response, request
    from twilio import twiml


    app = Flask(__name__)


    @app.route("/")
    def check_app():
        # returns a simple string stating the app is working
        return Response("It works!"), 200


    @app.route("/twilio", methods=["POST"])
    def inbound_sms():
        response = twiml.Response()
        # we get the SMS message from the request. we could also get the 
        # "To" and the "From" phone number as well
        inbound_message = request.form.get("Body")
        # we can now use the incoming message text in our Python application
        if inbound_message == "Hello":
            response.message("Hello back to you!")
        else:
            response.message("Hi! Not quite sure what you meant, but okay.")
        # we return back the mimetype because Twilio needs an XML response
        return Response(str(response), mimetype="application/xml"), 200


    if __name__ == "__main__":
        app.run(debug=True)


The inline comments on the lines starting with `#` explain what the lines
below them do. Flask applications define URL routes with the `@app.route`
decorator. Our application needs two routes therefore we have two of those
decorators defined.

Give the application a try by running it with `python app.py`. If you have
trouble running the program, make sure your virtualenv is still active so
that the application can use the Flask and Twilio code libraries we installed
earlier.

Open a web browser and go to localhost:5000 (or 127.0.0.1:5000). We should
see "It works!" on the screen.

<img src="/img/160530-respond-sms-python-flask/app-local.jpg" width="100%" class="technical-diagram img-rounded">

There is one problem with our application running on our local development
environment: there's no way for our server to receive HTTP POST requests 
unless we use a localhost tunnel.


## Localhost Tunneling with Ngrok
[Ngrok](https://ngrok.com) provides a localhost tunnel so that outside
services can connect to a server running in your local development 
environment. Download and install Ngrok.

We can now run Ngrok locally and connect our Flask app running on port 5000. 
Within the directory where you extracted Ngrok, run this command.

    ./ngrok http 5000 
 
<img src="/img/160530-respond-sms-python-flask/start-ngrok.jpg" width="100%" class="technical-diagram img-rounded">

Awesome, now we can use that Ngrok Forwarding URL to access our application
from any machine that has an internet connection. Replace the URL in the
web browser with your own Forwarding URL, like I did in this screenshot.

<img src="/img/160530-respond-sms-python-flask/access-ngrok.png" width="100%" class="technical-diagram img-rounded">

We just need a phone number that'll hit our application with a POST request
to respond to text messages.


## Obtaining Our Phone Number
We can use our Flask application's route to respond to incoming web API 
requests based on incoming SMS messages to a Twilio phone number. Go to the
[Twilio website and sign up for a free trial account](www.twilio.com/referral/w9pugq)
to use their API. If you already have a Twilio account then sign into your 
existing account.

<img src="/img/160530-respond-sms-python-flask/try-twilio.png" width="100%" class="technical-diagram img-rounded">

The Twilio trial account allows you to send and receive text messages to 
your own validated phone number. To send and respond to SMS to and from any 
phone number then you need to upgrade your account. Trial accounts are 
great for initial development before your application goes live.

When you sign up, you receive a free Twilio phone number. We can
configure that phone number to forward the SMS information to our web 
application by setting up the response webhook.

Go to the 
[manage phone numbers screen](https://www.twilio.com/console/phone-numbers) 
and click on the phone number you want to configure for responding to 
inbound text messages.

Scroll down to near the bottom of the page and look for the "Messaging"
header. Modify the "A Message Comes in" text box so that it has your
ngrok Forwarding URL plus the "/twilio" route, as shown in this screenshot.

<img src="/img/160530-respond-sms-python-flask/number-configuration.png" width="100%" class="technical-diagram img-rounded">

Now press the red "Save" button at the bottom to make our changes take
effect.

Our application is ready to go - time to give our phone number a try! 
Send "Hello" or whatever text you want to your phone number. Here is what 
the result looks like on my iPhone.

<img src="/img/160530-respond-sms-python-flask/success.jpg" width="100%" class="technical-diagram img-rounded">

This simple Flask application is a good start to build more complicated
responses such as
[adding natural language processing](https://www.twilio.com/blog/2014/06/using-natural-language-processing-for-better-sms-interfaces-using-twilio-and-pythons-textblob.html),
[building SMS Slack bots](https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html)
or 
[coding SMS-powered NES Game Genies](https://www.twilio.com/blog/2015/08/romram-hacking-building-an-sms-powered-game-genie-with-lua-and-python.html).


## What's next?
Sweet, now our Flask web app automatically responds to incoming SMS text
messages! It's pretty crazy to think that entire businesses such as 
[SuperPhone](http://techcrunch.com/2016/03/07/superphone/) and 
[Remind](https://www.remind.com/) are built off code that started out very
similar to the code we just wrote.

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160530-respond-sms-text-messages-python-flask.markdown)
and submit a pull request.
