title: How to Send MMS Picture Messages with Python
slug: send-mms-picture-messages-python
meta: A tutorial on how to send MMS (picture multimedia messages) using the Python programming language.
category: post
date: 2016-05-15
modified: 2018-03-28
newsletter: False
headerimage: /img/160515-mms-python/header.jpg
headeralt: Twilio and Python logos. Copyright their respective owners.


Multimedia Message Service (MMS) picture and video messages are a common 
extension to the Short Message Service (SMS) system for sending text 
messages. Using a 
[web application programming interface (API)](/application-programming-interfaces.html)
with Python makes it easy to send MMS messages from a web application or
script. In this short tutorial we'll learn how to add MMS sending capability
to a new or existing Python application.


## Tools We Need
Either [Python 2 or 3](/python-2-or-3.html) works for the code in this 
tutorial. Just make sure you have one of those two versions installed on 
your system by going to the terminal and typing `python --version`.
The other dependencies for this tutorial include:

* [Python](https://www.python.org/) version [2 or 3](/python-2-or-3.html)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle one
  [application dependency](/application-dependencies.html)
* A free [Twilio account](https://www.twilio.com/try-twilio) to use their 
  [MMS web API](https://www.twilio.com/docs/api/rest/sending-messages)
* [Twilio Python helper library](https://pypi.org/project/twilio),
  [version 6.0.0](https://github.com/twilio/twilio-python/tree/6.0.0) 
  or later

If you are unsure of how to get pip and virtualenv installed, take a look
at the first few steps of the 
[how to set up Python 3, Flask and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)
guide.


## Twilio Web API
Our simple Python example application will use the Twilio web API to send
picture messages.
Go to the Twilio website
[sign up for a free trial account](https://www.twilio.com/try-twilio). If 
you already have a Twilio account (and you should because it makes it easy 
to add almost any type of communications to applications!) then sign into 
your existing account.

<img src="/img/160515-mms-python/try-twilio.png" width="100%" class="technical-diagram img-rounded">

In trial mode Twilio can send MMS to a validated phone number associated 
with the account. When you're ready to send MMS messages to any phone in 
any country then you will have to upgrade your account.

After signing up for a Twilio account, you will receive your own phone 
number that'll be used to send messages. That phone number can send outbound
MMS messages without any configuration. It can also receive messages but 
that requires 
[modifying the Request URL webhook](https://www.twilio.com/docs/quickstart/python/sms/hello-monkey) 
in the phone number details screen.


## Installing Our Dependency
We'll use the [twilio helper library](https://pypi.org/project/twilio) 
as a dependency for our Python code. The helper library can be installed
via the `pip` command, which pulls the code from 
[PyPI](https://pypi.python.org/pypi) into our local virtualenv. In this
tutorial we'll call our virtualenv `pymms` but you can name it whatever
you want for your application.

We have to create the virtualenv before using it. In your terminal enter:

    virtualenv pymms

If you need to install virtualenv take a look at the
[how to set up Python 3, Django and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html)
guide.

Activate the virtualenv with the `source` command.

    source pymms/bin/activate


The command prompt will change to look like this after it is activated:

<img src="/img/160515-mms-python/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded">


Now install the 
[Twilio Python helper library](https://www.twilio.com/docs/libraries/python). 
Make sure you install the
version 6.0.0 or later current version because the syntax for this
code changed a bit from earlier helper library versions before 6.0.0.

    pip install twilio>=6.0.0


Once the helper library installs we can use it in our Python code.


## Sending MMS From Python
Launch the the Python interpreter by executing the `python` command in
your terminal. You can also create a new file named `send_mms.py` if you
want to re-use the code after we give it a try. 


We need to grab our account credentials from the Twilio Console to connect 
our Python code to our Twilio account. Go to the 
[Twilio Console](https://www.twilio.com/console) and copy the Account SID
and Authentication Token into your Python code.

<img src="/img/160515-mms-python/console-tokens.png" width="100%" class="technical-diagram img-rounded">

Enter the following code into the new Python file, or copy it from
[this GitHub repository that contains all blog code examples](https://github.com/fullstackpython/blog-code-examples).

```python
# import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

# this is the URL to an image file we're going to send in the MMS
media = "https://raw.githubusercontent.com/mattmakai/fullstackpython.com/master/static/img/logos/f.png"

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send MMS to any phone number that MMS is available
client.api.account.messages.create(to="+19732644152",
                                   from_="+12023351278",
                                   body="MMS via Python? Nice!",
                                   media_url=media)
```

All the lines above that start with `#` are comments to give you some
context for what each line is doing. After entering that code into the
interpreter or running the Python script with `python send_mms.py`
Twilio will send your MMS.

In a few seconds you should see a message appear on your phone - note that
MMS can take a little longer because your phone has to download the image. 
I use an iPhone so here is what the message looked like when I received it:

<img src="/img/160515-mms-python/mms-result.jpg" width="100%" class="technical-diagram img-rounded">

That is everything need to send MMS to a phone. Pretty awesome result for 
a few lines of Python code, right? This code can be added to any Python 
program to send outbound MMS.

One final note: keep your Twilio Auth Token secret otherwise anyone who
gets it will be able to send and receive messages through your account.

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/160515-sending-mms-picture-messages-python.markdown)
and submit a pull request.
