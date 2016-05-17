title: Bots
category: page
slug: bots
sortorder: 0901
toc: False
sidebartitle: Bots
meta: Bots are applications that combine text input with contextual data to handle and respond to requests.


# Bots
Bots are software programs that combine requests, which are typically 
provided as text, with contextual data, such as geolocation and payment 
information, to appropriately handle the request and respond. Bots are
often also called "chatbots", "assistants" or "agents."


## Python-specific Bots resources
* [How to Buid an SMS Slack Bot](https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html)
  is a tutorial on using 
  [SMS text messages](http://www.fullstackpython.com/blog/send-sms-text-messages-python.html) 
  to communicate with a Slack bot that can post and receive messages. The
  bot is a good base for a more complicated Slack bot that could use
  natural language processing or other more advanced parsing techniques.
  Either Python 2 or 3 can be used 
  [with the code which is also available on GitHub](https://github.com/makaimc/slack-api-python-examples).

* [How to write a Slack bot in Python](https://medium.com/@julianmartinez/how-to-write-a-slack-bot-with-python-code-examples-4ed354407b98)
  is a solid code tutorial for building your first bot on the Slack
  platform.

* [A Slack bot with Python’s 3.5 asyncio](https://medium.com/@greut/a-slack-bot-with-pythons-3-5-asyncio-ad766d8b5d8f)
  shows how to connect a bot to Slack via the web API using the Python 3
  [asyncio standard library](https://docs.python.org/3/library/asyncio.html).

* [Facebook-Message-Bot](https://github.com/enginebai/Facebook-Message-Bot)
  is an open source Facebook Messenger bot written in Python.


## Additional Bots resources
* [Slack bot token leakage exposing business critical information](https://labs.detectify.com/2016/04/28/slack-bot-token-leakage-exposing-business-critical-information/)
  is a detailed look at a search on GitHub for Slack tokens that are used
  mostly for bots but must be kept secret. Otherwise those tokens expose 
  the entire Slack team's messaging to outside parties.

* The Economist wrote a general piece on 
  [why bots look like they'll gain adoption in various market segments](http://www.economist.com/news/business-and-finance/21696477-market-apps-maturing-now-one-text-based-services-or-chatbots-looks-poised).
  The piece doesn't have much technical depth but it's a good overview of
  how some businesses are looking at the opportunity.

* [Bots won't replace apps](http://dangrover.com/blog/2016/04/20/bots-wont-replace-apps.html)
  is a fantastic piece by WeChat's product manager on how text-based bots 
  alone typically do not provide a good user experience. Instead, chat
  apps with automated responses, user data and basic web browser 
  functionality are what has allowed bot concepts to bloom in Asian markets.
  There's a lot of good information in this post to unpack.

