title: Twilio
category: page
slug: twilio
sortorder: 0604
toc: False
sidebartitle: Twilio
meta: Twilio is an API for developers to add communications such as phone calling, messaging and video to Python applications.


# Twilio
[Twilio](https://www.twilio.com/docs/quickstart/python/twiml) is a 
[web application programming interface (API)](/application-programming-interfaces.html)
that software developers can use to add communications such as 
[phone calling](https://www.twilio.com/docs/tutorials/walkthrough/browser-calls/python/django), 
[messaging](https://www.twilio.com/docs/tutorials/walkthrough/server-notifications/python/django), 
[video](https://www.twilio.com/docs/api/video/guide/quickstart-js) and 
[two-factor authentication](https://www.twilio.com/docs/tutorials/walkthrough/two-factor-authentication/python/flask)
into their [Python](/learning-programming.html) applications.

<img src="/img/twilio-logo.png" width="100%" alt="Twilio logo." class="technical-diagram" style="padding: 10px 0 10px 0;"/>


## Why is Twilio a good API choice?
Interacting with the standard telephone networks to send and receive
phone calls and text messages without Twilio is extremely difficult 
if you do not know the unique telecommunications protocols such as 
Session Initiation Protocol (SIP). Twilio's API abstracts the 
telecommunications pieces so as a developer you can simply use your 
favorite programming languages and frameworks in your application.
For example, here's how you can send an 
[outbound SMS](https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest) 
using a few lines of Python code:

    # import the Twilio helper library (installed with pip install twilio)
    from twilio.rest import TwilioRestClient

    # replace the placeholder strings in the following code line with 
    # your Twilio Account SID and Auth Tokenfrom the Twilio Console
    client = TwilioRestClient("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

    # change the "from_" number to your Twilio number and the "to" number
    # to any phone number you want to send the message to 
    client.messages.create(to="+19732644152", from_="+12023358536", 
                           body="Hello from Python!")


Learn more about the above code in the 
[How to Send SMS Text Messages with Python tutorial](/blog/send-sms-text-messages-python.html).


## How is Twilio's documentation for Python developers?
Twilio is a developer-focused company, rather than a traditional 
"enterprise company", so their tutorials and 
[documentation](https://www.twilio.com/docs) are written by developers 
for fellow developers.


### More Twilio resources
* Most [Twilio Tutorials](https://www.twilio.com/docs/tutorials) have 
  idiomatic Python versions with entire open source applications in
  [Django](/django.html) and [Flask](/flask.html).

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
  includes 
  [a chapter on sending text messages](https://automatetheboringstuff.com/chapter16/) 
  that uses Twilio to get the job done.

* IBM's Bluemix blog contains a nice tutorial on building an 
  [IoT Python app with a Raspberry Pi and Bluemix](https://developer.ibm.com/bluemix/2015/04/02/tutorial-using-a-raspberry-pi-python-iot-twilio-bluemix/)
  that uses Twilio to interact with the Raspberry Pi.

* The [Python tag on the Twilio blog](https://www.twilio.com/blog/tag/python)
  provides walkthroughs for 
  [Django](https://www.twilio.com/blog/2015/12/city-chat-with-python-django-and-twilio-ip-messaging.html), 
  [Flask](https://www.twilio.com/blog/2015/11/international-space-station-notifications-with-python-redis-queue-and-twilio-copilot.html) 
  and [Bottle](https://www.twilio.com/blog/2016/08/getting-started-python-bottle-twilio-sms-mms.html) 
  apps to learn from while building your own projects.

* [Google Cloud recommends developers use Twilio](https://cloud.google.com/appengine/docs/python/sms/twilio)
  for communications in their apps and provides a short walkthrough for
  Python developers.

* [SMS Tracking Notifications](https://www.easypost.com/sms-tracking-tutorial)
  is a fun tutorial that combines two APIs together - Twilio and 
  [Easypost](https://www.easypost.com) to track packages sent through the
  Easypost service.


#### Disclaimer
I [currently work at Twilio](/about-author.html) as a 
[Developer Evangelist](https://www.twilio.com/blog/2014/02/introducing-developer-evangelist-matt-makai.html).

