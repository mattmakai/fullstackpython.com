title: How to Send SMS Text Messages with Python
slug: send-sms-text-messages-python
meta: A how-to guide for sending SMS (text messages) using the Python programming language.
category: post
date: 2016-05-11
modified: 2020-08-05
newsletter: False
headerimage: /img/160511-send-sms-python/header.jpg
headeralt: Twilio and Python logos. Copyright their respective owners.


Short Message Service (SMS) text messages are ubiquitous for communication
all over the world. It is easy to send SMS text messages from a 
[Python](/why-use-python.html) application using a 
[web application programming interface (API)](/application-programming-interfaces.html). 
Let's take a look at the tools we need to quickly add SMS capability to our
Python apps.


## Tools We Need
This guide works with both Python 2 and 3, so make sure you have one of 
those two versions installed.

* Either [Python 2 or 3](/python-2-or-3.html)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle
  [application dependencies](/application-dependencies.html)
* A free [Twilio account](www.twilio.com/referral/w9pugq) to use their 
  [SMS web API](https://www.twilio.com/docs/api/rest/sending-messages)
* Open source 
  [Twilio Python helper library](https://pypi.org/project/twilio),
  [version 6.0.0](https://github.com/twilio/twilio-python/tree/6.0.0) 
  or later

If you need assistance getting pip and virtualenv installed, check out the
first few steps of the 
[how to set up Python 3, Flask and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
guide that'll show how to install system packages for those tools.


## Using a Web API
We're going to use a web API to make sending SMS easier and more reliable.
Head to the 
[Twilio website and sign up for a free trial account](www.twilio.com/referral/w9pugq)
awesome for more than just sending text messages!) then sign into your 
existing account.

<img src="/img/160511-send-sms-python/try-twilio.png" width="100%" class="technical-diagram img-rounded">

The Twilio trial account allows you to send text messages to your own 
validated phone number.  When you want to send SMS to any phone number in 
your country or other countries then you can upgrade your account to send 
messages for fractions of a cent.

After signing up, you will get a free phone number in your country. We can
use that phone number without any configuration to send outbound text 
messsages. You can also receive text messages but that requires changing
the Request URL webhook in the phone number configuration screen - we'll
cover that in a future blog post.


## Installing Our Dependency
Our code will use a helper library to make it easier to send text messages
from Python. We are going to install the helper library from 
[PyPI](https://pypi.python.org/pypi) into a virtualenv. First we need to
create the virtualenv. In your terminal use the following command to create
a new virtualenv. If you need to install virtualenv take a look at the
[how to set up Python 3, Flask and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
guide.

    virtualenv sendsms


Activate the virtualenv.

    source sendsms/bin/activate


The command prompt will change after we properly activate the virtualenv
to something like this:

<img src="/img/160511-send-sms-python/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded">


Now install the Twilio Python helper library. We are using the 6.0.0
or above library version, which is important because the syntax in
this post is backwards-incompatible with 5.x and previous Twilio helper
library versions.

    pip install twilio>=6.0.0


The helper library is now installed and we can use it with the Python code 
we create and execute.


## Sending SMS From Python
Fire up the Python interpreter in the terminal using the `python` command,
or create a new file named `send_sms.py`. 

We need to grab our account credentials from the Twilio Console to connect 
our Python code to our Twilio account. Go to the 
[Twilio Console](https://www.twilio.com/console) and copy the Account SID
and Authentication Token into your Python code.

<img src="/img/160511-send-sms-python/console-tokens.png" width="100%" class="technical-diagram img-rounded">

Enter the following code into the interpreter or into the new Python file.
You can also copy and paste the code from the 
[blog-code-examples Git repository](https://github.com/fullstackpython/blog-code-examples/blob/master/send-sms-text-messages-python/send_sms.py)
in the 
[Full Stack Python GitHub organization](https://github.com/fullstackpython).


    # we import the Twilio client from the dependency we just installed
    from twilio.rest import Client

    # the following line needs your Twilio Account SID and Auth Token
    client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to="+19732644152", 
                           from_="+12023351278", 
                           body="Hello from Python!")


All the lines above that start with `#` are comments. Once you enter that 
code into the interpreter or run the Python script using 
`python send_sms.py` the SMS will be sent.

In a few seconds you should see a message appear on your phone. I'm on
iOS so here's how the text message I received looked.

<img src="/img/160511-send-sms-python/hello-from-python.png" width="100%" class="technical-diagram img-rounded">

That's it! You can add this code to any Python code to send text messages.
Just keep your Auth Token secret as it'll allow anyone that has it to use
your account to send and receive messages.

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160511-send-sms-text-message-python.markdown)
and submit a pull request.
