title: How to Make Phone Calls in Python
slug: make-phone-calls-python
meta: This tutorial shows how to use a Python program and the Twilio API to dial phone calls.
category: post
date: 2016-11-23
modified: 2017-07-22
newsletter: False
headerimage: /img/161123-python-phone-calls/header.jpg
headeralt: Python and Twilio logos. Copyright their respective owners.


Good old-fashioned phone calls remain one of the best forms of communication
despite the slew of new smartphone apps that have popped up over the past
several years. With just a few lines of Python code plus a 
[web application programming interface](/application-programming-interfaces.html) 
we can make and receive phone calls from any application. 

Our example calls will say a snippet of text and put all incoming callers 
into a recorded conference call. You can modify the instructions using 
[Twilio's TwiML verbs](https://www.twilio.com/docs/api/twiml) when you 
perform different actions in your own application's phone calls.


## Our Tools
You should have either [Python 2 or 3](/python-2-or-3.html) installed to
build this application. Throughout the post we will also use:

* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/) to handle
  [application dependencies](/application-dependencies.html)
* A free [Twilio account](https://www.twilio.com/try-twilio) to use their 
  [phone calling web API](https://www.twilio.com/docs/api/rest/making-calls)
* Twilio's 
  [Python helper library](https://www.twilio.com/docs/libraries/python),
  version 5.7.0, which is 
  [available on PyPI](https://pypi.org/project/twilio)

You can snag all the open source code for this tutorial in the 
[python-twilio-example-apps](https://github.com/mattmakai/python-twilio-example-apps/tree/master/no-framework/phone-calls)
GitHub repository under the 
[no-framework/phone-calls](https://github.com/mattmakai/python-twilio-example-apps/tree/master/no-framework/phone-calls) directory.
Use and copy the code for your own applications. Everything in that 
repository and in this blog post are open source under the MIT license.


## Install App Dependencies
Our application will use the [Twilio](/twilio.html) 
[Python helper library](https://www.twilio.com/docs/libraries/python)
to create an HTTP POST request to Twilio's API. The Twilio helper library is 
installable from [PyPI](https://pypi.python.org/pypi) into a virtual 
environment. Open your terminal and use the `virtualenv` command to create 
a new virtualenv:

```
virtualenv phoneapp
```

Invoke the `activate` script within the virtualenv `bin/` directory to make 
this virtualenv the active Python executable. Note that you will need to 
perform this step in every terminal window that you want the virtualenv to 
be active.

```
source phoneapp/bin/activate
```

The command prompt will change after activating the virtualenv
to something like `(phoneapp) $`. 

Next use the `pip` command to install the 
[Twilio Python](https://www.twilio.com/docs/libraries/python) package
into the virtualenv.

```
pip install twilio==5.7.0
```

We will have the required dependency ready for project as soon as the 
installation script finishes. Now we can write and execute Python code to 
dial phone numbers.


## Our Python Script
Create a new file named `phone_calls.py` and copy or type in the following
lines of code.

```python
from twilio.rest import TwilioRestClient


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = ""

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["",]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient("ACxxxxxxxxxx", "yyyyyyyyyy")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)
```

There are a few lines that you need to modify in this application before it
will run. First, insert one or more phone numbers you wish to dial into the 
DIAL_NUMBERS list. Each one should be a string, separated by a comma. For
example, `DIAL_NUMBERS = ["+12025551234", "+14155559876", "+19735551234"]`.

Next, `TWILIO_PHONE_NUMBER` and the Account SID and Authentication Token,
found on the `client = TwilioRestClient("ACxxxxxxxxxx", "yyyyyyyyyy")` 
line, need to be set. We can get these values from the 
[Twilio Console](https://www.twilio.com/console).

In your web browser go to the
[Twilio website and sign up for a free account](https://www.twilio.com/try-twilio) 
or sign into your existing Twilio account.

<img src="/img/161123-python-phone-calls/try-twilio.png" width="100%" class="technical-diagram img-rounded" alt="Twilio sign up screen.">

Copy the Account SID and Auth Token from the Twilio Console and paste them 
into your application's code: 

<img src="/img/161123-python-phone-calls/twilio-console-tokens.png" width="100%" class="technical-diagram img-rounded" alt="Obtain the Account SID and Auth Token from the Twilio Console.">

The Twilio trial account allows you to dial and receive phone calls to 
your own validated phone number. To handle calls from any phone 
number then you need to upgrade your account (hit the upgrade button on the
top navigation bar). 

Once you are signed into your Twilio account, go to the 
[manage phone numbers screen](https://www.twilio.com/console/phone-numbers).
On this screen you can 
[buy one or more phone numbers](https://www.twilio.com/console/phone-numbers/search)
or click on an existing phone number in your account to configure it.

<img src="/img/161123-python-phone-calls/manage-numbers.jpg" width="100%" class="technical-diagram img-rounded" alt="Manage phone numbers screen.">

After clicking on a number you will reach the phone number configuration
screen. Paste in the URL with TwiML instructions and change the dropdown from
"HTTP POST" to "HTTP GET". In this post we'll use 
`http://static.fullstackpython.com/phone-calls-python.xml`, but that URL 
can be more than just a static XML file. 

<img src="/img/161123-python-phone-calls/twiml-url-number-screen.jpg" width="100%" class="technical-diagram img-rounded" alt="Twilio phone number configuration screen.">

The power of Twilio really comes in when that URL is handled by your web 
application so it can dynamically respond with TwiML instructions based on 
the incoming caller number or other properties stored in your database.

Under the Voice webhook, paste in 
`http://static.fullstackpython.com/phone-calls-python.xml` and change the
drop-down to the right from "HTTP POST" to "HTTP GET". Click the "Save" 
button at the bottom of the screen.

Now try calling your phone number. You should hear the snippet of text
read by the Alice voice and then you will be placed into a conference call.
If no one else calls the number then hold music should be playing.


## Making Phone Calls
We just handled inbound phone calls to our phone number. Now it's time to 
dial outbound phone calls. Make sure your `phone_calls.py` file is saved 
and that your virtualenv is still activated and then execute the script:

```
python phone_calls.py
```

In a moment all the phone numbers you write in the `DIAL_NUMBERS` list
should light up with calls. Anyone that answers will hear our message read
by the "Alice" voice and then they'll be placed together into a recorded 
conference call, just like when someone dials into the number. 

Here is my inbound phone call:

<img src="/img/161123-python-phone-calls/inbound-call.png" width="100%" class="technical-diagram img-rounded" alt="Receiving an incoming phone call on the iPhone.">

Not bad for just a few lines of Python code!


## Next Steps
Now that we know how to make and receive phone calls from a Twilio number 
that follows programmatic instructions we can do a whole lot more in our
applications. Next you can use one of these tutorials to do more with 
your phone number:

* [Build a phone-calling Slack bot](https://www.twilio.com/blog/2016/05/add-phone-calling-slack-python.html)
* [Mask phone numbers for anonymous communication](https://www.twilio.com/docs/tutorials/walkthrough/masked-numbers/python/flask)
* [Add call tracking to see metrics for phone calls](https://www.twilio.com/docs/tutorials/walkthrough/call-tracking/python/django)
  

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub as
[mattmakai](https://github.com/mattmakai).

See something wrong in this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/161123-make-phone-calls.markdown)
and submit a pull request.
