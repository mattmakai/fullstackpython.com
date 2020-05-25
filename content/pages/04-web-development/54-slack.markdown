title: Slack
category: page
slug: slack
sortorder: 0454
toc: False
sidebartitle: Slack
meta: Slack has an application programming interface (API) for building bots and programmatically interacting with its messaging service.


Slack provides a web
[application programming interface (API)](/application-programming-interfaces.html) 
for programmatically interacting with its messaging service.

<a href="https://api.slack.com/" style="border:none"><img src="/img/logos/slack.jpg" width="100%" alt="Slack logo." class="shot" style="padding:12px 0 12px 0"></a>


<div class="well see-also">The Slack API is an implementation of the <a href="/application-programming-interfaces.html">web application programming interfaces</a> concept. Learn how these pieces fit together in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


### Slack resources
* [How to Build Your First Slack Bot with Python](/blog/build-first-slack-bot-python.html)
  contains all the code for getting a Slack bot up and running with Python
  even if you have not previously worked with their API or built other 
  [bots](/bots.html).

* [Use a Slack bot to deploy your app](https://tech-blog.serenytics.com/deploy-your-saas-with-a-slack-bot-f6d1fc764658)
  gives the sample code to a simplified bot that you can engage with in 
  your chat channels to perform application deployments.

* [How I built a Slack bot to help me find an apartment in San Francisco](https://www.dataquest.io/blog/apartment-finding-slackbot/)
  is a story about how the author had issues finding an apartment while 
  moving from Boston to San Francisco. He started scraping Craigslist to
  gather apartment data and built a Slack bot to message him as soon as
  something that matched his criteria became available so he could take
  a look at it.

* [Slack on an SNES](https://bert.org/2018/10/18/slack-on-a-snes/) is not
  a Python tutorial but it provides a crazy hack for communicating
  with Slack using a Super Nintendo.

* [Hacking Slack accounts: As easy as searching GitHub](https://arstechnica.com/information-technology/2016/04/hacking-slack-accounts-as-easy-as-searching-github/)
  explains how secret Slack API keys are often committed to public GitHub 
  repositories which allows malicious actors to easily break into an 
  organization's messaging systems. Secret credentials in public repositories
  is a problem for any API and it is a particular problem for ones that are
  critical to a business' private communications.

* [Serverless Slash Commands with Python](https://renzo.lucioni.xyz/serverless-slash-commands-with-python/)
  shows how to build a [serverless](/serverless.html) [Flask](/flask.html)
  plus Zappa framework web app that is hosted on [AWS Lambda](/aws-lambda.html)
  and can use the Slack API.

* [Hacking Slack using postMessage and WebSocket-reconnect to steal your precious token](https://labs.detectify.com/2017/02/28/hacking-slack-using-postmessage-and-websocket-reconnect-to-steal-your-precious-token/)
  examines a bug that the author found in Slack's WebSockets reconnection 
  operation that he reported to Slack. Slack fixed the issue and paid him a
  bug bounty for his work.

* [Posting messages to Slack using incoming webhooks and Python3 Requests API](https://notes.ayushsharma.in/2017/09/posting-messages-to-slack-using-incoming-webhooks-and-python-requests-api)
  is a short script that uses the [Requests](https://pypi.org/project/requests/) 
  library instead of the Slack-provided Python helper libraries to interact
  with the API.

* [Build a Google Analytics Slack Bot with Python](https://www.twilio.com/blog/2018/03/google-analytics-slack-bot-python.html)
  walks through creating a bot that posts Google Analytics data into
  Slack channels by combining the Slack and Google APIs.


### Example Slack bots
* [python-rtmbot](https://github.com/slackapi/python-rtmbot) is the 
  Slack-provided library for working with the Slack API and 
  [WebSockets](/websockets.html) connection.

* [slackify](https://github.com/Ambro17/slackify) is a lightweight
  framework for building bots and the quickstart walks you through
  how to create a simple example bot.

* [slack-starterbot](https://github.com/mattmakai/slack-starterbot)

* [slack-api-python-examples](https://github.com/mattmakai/slack-api-python-examples)
  contains the example code from several Slack bot blog posts.
 
* [slackbot](https://github.com/lins05/slackbot) another popular
  Slack bot implementation.
