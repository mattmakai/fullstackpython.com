title: Twilio
category: page
slug: twilio
sortorder: 0452
toc: False
sidebartitle: Twilio
meta: Twilio is an API for developers to add communications such as phone calling, messaging and video to Python applications.


[Twilio](https://www.twilio.com/docs/quickstart/python/twiml) is a 
[web application programming interface (API)](/application-programming-interfaces.html)
that software developers can use to add communications such as 
[phone calling](https://www.twilio.com/docs/tutorials/walkthrough/browser-calls/python/django), 
[messaging](https://www.twilio.com/docs/tutorials/walkthrough/server-notifications/python/django), 
[video](https://www.twilio.com/docs/api/video/guide/quickstart-js) and 
[two-factor authentication](https://www.twilio.com/docs/tutorials/walkthrough/two-factor-authentication/python/flask)
into their [Python](/learning-programming.html) applications.

<img src="/img/logos/twilio.png" width="100%" alt="Twilio logo." class="shot" style="padding: 10px 0 10px 0;"/>


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

```python
# import the Twilio helper library (installed with pip install twilio)
from twilio.rest import TwilioRestClient

# replace the placeholder strings in the following code line with 
# your Twilio Account SID and Auth Token from the Twilio Console
client = TwilioRestClient("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

# change the "from_" number to your Twilio number and the "to" number
# to any phone number you want to send the message to 
client.messages.create(to="+19732644152", from_="+12023358536", 
                       body="Hello from Python!")

```

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

* [Build a Simpsons Quote-Bot with Twilio MMS, Frinkiac, and Python](https://www.pluralsight.com/guides/build-a-simpsons-quote-bot-with-twilio-mms-frinkiac-and-python)
  combines picture messages sent via Twilio MMS with 
  [Frinkiac](https://frinkiac.com/) to create and sent Simpsons cartoon
  quotes to any phone number. 

* [Finding free food with Python](http://jamesbvaughan.com/python-twilio-scraping/)
  is a fun web scraping tutorial that uses Beautiful Soup 4 to obtain
  some data from websites then uses the 
  [Twilio SMS API via some Python code](https://www.twilio.com/docs/quickstart/python/sms) 
  to send a text message with the results.

* IBM's Bluemix blog contains a nice tutorial on building an 
  [IoT Python app with a Raspberry Pi and Bluemix](https://developer.ibm.com/bluemix/2015/04/02/tutorial-using-a-raspberry-pi-python-iot-twilio-bluemix/)
  that uses Twilio to interact with the Raspberry Pi.

* The [Python tag on the Twilio blog](https://www.twilio.com/blog/tag/python)
  provides walkthroughs for 
  [Django](https://www.twilio.com/blog/2015/12/city-chat-with-python-django-and-twilio-ip-messaging.html), 
  [Flask](https://www.twilio.com/blog/2015/11/international-space-station-notifications-with-python-redis-queue-and-twilio-copilot.html) 
  and [Bottle](https://www.twilio.com/blog/2016/08/getting-started-python-bottle-twilio-sms-mms.html) 
  apps to learn from while building your own projects.

* [Serverless Phone Number Validation with AWS Lambda, Python and Twilio](https://www.twilio.com/blog/serverless-phone-number-validation-aws-lambda-python-twilio)
  walks through using the Python runtime on [AWS Lambda](/aws-lambda.html) 
  and Twilio's APIs for validating phone number information.

* [Receive Flask Error Alerts by Email with Twilio SendGrid](https://www.twilio.com/blog/receive-flask-error-alerts-email-twilio-sendgrid)
  shows how to use Twilio to add email error reports to [Flask](/flask.html)
  web applications.

* [Google Cloud recommends developers use Twilio](https://cloud.google.com/appengine/docs/standard/python/sms/twilio)
  for communications in their apps and provides a short walkthrough for
  Python developers.

* [SMS Tracking Notifications](https://www.easypost.com/sms-tracking-tutorial)
  is a fun tutorial that combines two APIs together - Twilio and 
  [Easypost](https://www.easypost.com) to track packages sent through the
  Easypost service. There is also another tutorial on 
  [shipment notifications specifically for Flask](https://www.twilio.com/blog/build-shipment-notification-service-python-flask-twilio-easypost).

* [Build a Video Chat Application with Python, JavaScript and Twilio Programmable Video](https://www.twilio.com/blog/build-video-chat-application-python-javascript-twilio-programmable-video)
  shows how to use [Flask](/flask.html) and the 
  [Twilio Programmable Video API](https://www.twilio.com/docs/video) to
  build cross-platform video into new and existing applications.

* This video titled 
  "[We're No Strangers to VoIP: Building the National Rick Astley Hotline)](https://www.youtube.com/watch?v=LgKshQoGh64)"
  presents a hilarious hack that uses Python and 
  [AWS Lambda](/aws-lambda.html) as a [serverless](/serverless.html) 
  backend to power thousands of Rick Rolling calls in several countries 
  with Twilio.

* [Stripe SMS Notifications via Twilio, Heroku, and Python](https://www.twilio.com/blog/2017/02/stripe-sms-notifications-via-twilio-heroku-and-python.html)
  is a quick tutorial that demonstrates how to combine multiple services
  to receive helpful notifications via SMS.


#### Disclaimer
I [currently work at Twilio](/about-author.html) on the
[Developer Network](https://www.twilio.com/blog/2014/02/introducing-developer-evangelist-matt-makai.html)
and run the [Developer Voices](http://www.twiliovoices.com/) team.

