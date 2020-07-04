title: Bots
category: page
slug: bots
sortorder: 0447
toc: False
sidebartitle: Bots
meta: Bots are applications that combine text input with contextual data to handle and respond to requests.


Bots are software programs that combine requests, which are typically 
provided as text, with contextual data, such as geolocation and payment 
information, to appropriately handle the request and respond. Bots are
often also called "chatbots", "assistants" or "agents."


### Open source bot examples
* [Limbo](https://github.com/llimllib/limbo) is an awesome Slack chatbot 
  that provides a base for Python code that otherwise would require 
  boilerplate to handle the Slack API events firehose.

* [python-rtmbot](https://github.com/slackhq/python-rtmbot) is the bot
  framework for building Slack bots with the Real Time Messaging (RTM) API
  over [WebSockets](/websockets.html).

* The 
  [GitHub bots search results](https://github.com/search?utf8=%E2%9C%93&q=bots)
  and the [bots GitHub topic](https://github.com/topics/bots) contain tens of
  thousands of example bots you take analyze to see how they are built.

* [Errbot](http://errbot.io/en/latest/) can work with 
  [multiple backends](http://errbot.io/en/latest/features.html) such
  as Hipchat, Discord, Slack and Telegram. It's designed to be deployed
  "as is" except for your credentials but the 
  [Python source code](https://github.com/errbotio/errbot) 
  can also be customized.


### Python-specific bot resources
* [How to Buid an SMS Slack Bot](https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html)
  is a tutorial on using 
  [SMS text messages](/blog/send-sms-text-messages-python.html) 
  to communicate with a Slack bot that can post and receive messages. The
  bot is a good base for a more complicated Slack bot that could use
  natural language processing or other more advanced parsing techniques.
  Either Python 2 or 3 can be used 
  [with the code which is also available on GitHub](https://github.com/mattmakai/slack-api-python-examples).

* [Dropbox open sourced their security Slack bot](https://blogs.dropbox.com/tech/2017/02/meet-securitybot-open-sourcing-automated-security-at-scale/),
  which is [built in Python](https://github.com/dropbox/securitybot).
  The bot converses with a user when backend systems detect strange behavior on
  one of their accounts to check if there has been a security breach.

* [Making a Reddit + Facebook Messenger Bot](https://pythontips.com/2017/04/13/making-a-reddit-facebook-messenger-bot/)
  builds a bot for two platforms and shows how to deploy it to Heroku.

* [Build a Slack Bot that Mimics Your Colleagues with Python](https://hirelofty.com/blog/software-development/how-build-slack-bot-mimics-your-colleague/)
  is a humorous post that uses the 
  [markovify](https://github.com/jsvine/markovify) Markov Chains library to 
  generate responses that are similar to ones other Slack users have said.

* [A Slack bot with Python's asyncio](https://medium.com/@greut/a-slack-bot-with-pythons-3-5-asyncio-ad766d8b5d8f)
  shows how to connect a bot to Slack via the web API using the Python 3
  [asyncio standard library](https://docs.python.org/3/library/asyncio.html).

* [Facebook-Message-Bot](https://github.com/enginebai/Facebook-Message-Bot)
  is an open source Facebook Messenger bot written in Python.

* [Build a Reddit bot](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/)
  is a four part tutorial series that starts with reading posts, continues
  with 
  [replying to posts](https://www.pythonforengineers.com/build-a-reddit-bot-part-2-reply-to-posts/),
  [automating the bot](https://www.pythonforengineers.com/build-a-reddit-bot-part-3-automate-your-bot/)
  and finally
  [adding behavior and a personality to the bot](https://www.pythonforengineers.com/build-marvin-the-depressed-reddit-bot-in-python/).


### Additional Bots resources
* [Bots: An introduction for developers](https://core.telegram.org/bots)
  explains the technical details of how to create 
  [Telegram](https://telegram.org/) bots.

* [Building better bots with AWS Lex: Part 1](https://aws.amazon.com/blogs/machine-learning/building-better-bots/)
  and 
  [part 2](https://aws.amazon.com/blogs/machine-learning/building-better-bots-part-2/)
  show how to use Amazon's service offering for better natural language
  processing in your bots.

* [Slack bot token leakage exposing business critical information](https://labs.detectify.com/2016/04/28/slack-bot-token-leakage-exposing-business-critical-information/)
  is a detailed look at a search on GitHub for Slack tokens that are used
  mostly for bots but must be kept secret. Otherwise those tokens expose 
  the entire Slack team's messaging to outside parties.

* The Economist wrote a general piece on 
  [why bots look like they'll gain adoption in various market segments](http://www.economist.com/news/business-and-finance/21696477-market-apps-maturing-now-one-text-based-services-or-chatbots-looks-poised).
  The piece doesn't have much technical depth but it's a good overview of
  how some businesses are looking at the opportunity.

* [Three challenges you’re going to face when building a chatbot](https://blog.infermedica.com/three-challenges-youre-going-to-face-when-building-a-chatbot/)
  provides insightful thoughts on problems to anticipate based on the
  author's experience building, deploying and scaling chatbots.

* [Bots won't replace apps](http://dangrover.com/blog/2016/04/20/bots-wont-replace-apps.html)
  is a fantastic piece by WeChat's product manager on how text-based bots 
  alone typically do not provide a good user experience. Instead, chat
  apps with automated responses, user data and basic web browser 
  functionality are what has allowed bot concepts to bloom in Asian markets.
  There's a lot of good information in this post to unpack.

* [Principles of bot design](https://www.intercom.com/blog/principles-bot-design/)
  contains some general, common-sense ideas to keep in mind when building
  bots such as do not pretend to be a human (because it will be quickly 
  discovered that your bot is not a human) and keep it as simple as possible
  so people can actually use the damn thing.

* [6 things I learned creating my own Messenger chatbot](https://kilianvalkhof.com/2017/chatbots/6-things-i-learned-creating-my-own-messenger-chatbot/)
  contains some solid general advice for building your custom bots.
