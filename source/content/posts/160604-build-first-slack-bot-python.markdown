title: How to Build Your First Slack Bot with Python
slug: build-first-slack-bot-python
meta: Learn how to build a simple Slack bot in Python, no prior bot experience needed. 
category: post
date: 2016-06-04


Bots are a useful way to interact with chat services such as 
[Slack](https://slack.com/). If you have never built a bot before, this 
post provides an easy starter tutorial for combining the 
[Slack API](https://api.slack.com/) with Python to create your first bot.

We will walk through setting up your development environment, obtaining a
Slack API bot token and coding our simple bot in Python.


## Tools We Need
Our bot, which we will name "StarterBot", requires Python and the Slack API.
To run our Python code we need:

* Either [Python 2 or 3](/python-2-or-3.html)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/stable/) to handle Python 
  [application dependencies](/application-dependencies.html)
* [Free Slack account](https://slack.com/) with a team on which you have 
  API access or sign up for the 
  [Slack Developer Hangout team](http://dev4slack.xoxco.com/)
* Official Python 
  [slackclient](https://github.com/slackhq/python-slackclient) code 
  library built by the Slack team
* [Slack API testing token](https://api.slack.com/tokens)

It is also useful to have the [Slack API docs](https://api.slack.com/) handy 
while you're building this tutorial.

All the code for this tutorial is available open source under the MIT license
in the [slack-starterbot](https://github.com/makaimc/slack-starterbot) public
repository.


## Establishing Our Environment
We now know what tools we need for our project so let's get our development
environment set up. Go to the terminal (or Command Prompt on Windows) and 
change into the directory where you want to store this project. Within 
that directory, create a new virtualenv to isolate our application 
dependencies from other Python projects.

    virtualenv starterbot

Activate the virtualenv:

    source starterbot/bin/activate

Your prompt should now look like the one in this screenshot.

<img src="/source/static/img/160604-simple-python-slack-bot/virtualenv-activate.png" width="100%" class="technical-diagram img-rounded">

The official slackclient API helper library built by Slack can send and 
receive messages from a Slack channel. Install the slackclient library with 
the `pip` command:

    pip install slackclient

When `pip` is finished you should see output like this and you'll be
back at the prompt.

<img src="/source/static/img/160604-simple-python-slack-bot/pip-install-slackclient.png" width="100%" class="technical-diagram img-rounded">

We also need to obtain an access token for our Slack team so our bot can
use it to connect to the Slack API.


## Slack Real Time Messaging (RTM) API
Slack grants programmatic access to their messaging channels via a
[web API](/application-programming-interfaces.html). Go to the 
[Slack web API page](https://api.slack.com/) and sign up to create your own 
Slack team. You can also sign into an existing account where you have 
administrative privileges.

<img src="/source/static/img/160604-simple-python-slack-bot/sign-in-slack.png" width="100%" class="technical-diagram img-rounded">

After you have signed in go to the 
[Bot Users page](https://api.slack.com/bot-users).

<img src="/source/static/img/160604-simple-python-slack-bot/custom-bot-users.png" width="100%" class="technical-diagram img-rounded">

Name your bot "starterbot" then click the “Add bot integration” button.

<img src="/source/static/img/160604-simple-python-slack-bot/starterbot.jpg" width="100%" class="technical-diagram img-rounded">

The page will reload and you will see a newly-generated access token. You 
can also change the logo to a custom design. For example, I gave this bot
the Full Stack Python logo.

<img src="/source/static/img/160604-simple-python-slack-bot/slack-token.png" width="100%" class="technical-diagram img-rounded">

Click the "Save Integration" button at the bottom of the page. Your bot is 
now ready to connect to Slack's API.

A common practice for Python developers is to export secret tokens as 
environment variables. Export the Slack token with the name 
`SLACK_BOT_TOKEN`:

    export SLACK_BOT_TOKEN='your slack token pasted here'

Nice, now we are authorized to use the Slack API as a bot.

There is one more piece of information we need to build our bot: our bot's 
ID. Next we will write a short script to obtain that ID from the Slack API.


## Obtaining Our Bot’s ID
It is *finally* time to write some Python code! We'll get warmed up by coding 
a short Python script to obtain StarterBot's ID. The ID varies based on the 
Slack team. 

We need the ID because it allows our application to determine if messages 
parsed from the Slack RTM are directed at StarterBot. Our script also 
tests that our `SLACK_BOT_TOKEN` environment variable is properly set. 

Create a new file named `print_bot_id.py` and fill it with the following 
code.


    import os
    from slackclient import SlackClient


    BOT_NAME = 'starterbot'

    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


    if __name__ == "__main__":
        api_call = slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == BOT_NAME:
                    print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
        else:
            print("could not find bot user with the name " + BOT_NAME)


Our code imports the SlackClient and instantiates it with our 
`SLACK_BOT_TOKEN`, which we set as an environment variable. When the 
script is executed by the `python` command we call the Slack API to list
all Slack users and get the ID for the one that matches the name "starterbot".

We only need to run this script once to obtain our bot’s ID.

    python print_bot_id.py

The script prints a single line of output when it is run that provides
us with our bot's ID.

<img src="/source/static/img/160604-simple-python-slack-bot/printed-bot-id.png" width="100%" class="technical-diagram img-rounded">

Copy the unique ID that your script prints out. Export the ID as an 
environment variable named `BOT_ID`.


    (starterbot)$ export BOT_ID='bot id returned by script'


The script only needs to be run once to get the bot ID. We can now use
that ID in our Python application that will run StarterBot.


## Coding Our StarterBot
We've got everything we need to write the StarterBot code. Create a new file 
named `starterbot.py` and include the following code in it.


    import os
    import time
    from slackclient import SlackClient


The `os` and `SlackClient` imports will look familiar because we used them 
in the `print_bot_id.py` program.

With our dependencies imported we can use them to obtain the environment 
variable values and then instantiate the Slack client.


    # starterbot's ID as an environment variable
    BOT_ID = os.environ.get("BOT_ID")

    # constants
    AT_BOT = "<@" + BOT_ID + ">:"
    EXAMPLE_COMMAND = "do"

    # instantiate Slack & Twilio clients
    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


The code instantiates the `SlackClient` client with our `SLACK_BOT_TOKEN` 
exported as an environment variable. 


    if __name__ == "__main__":
        READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
        if slack_client.rtm_connect():
            print("StarterBot connected and running!")
            while True:
                command, channel = parse_slack_output(slack_client.rtm_read())
                if command and channel:
                    handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")


The Slack client connects to the Slack RTM API WebSocket then constantly 
loops while parsing messages from the firehose. If any of those messages are 
directed at StarterBot, a function named `handle_command` determines what 
to do.

Next add two new functions to parse Slack output and handle commands.

    def handle_command(command, channel):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.
        """
        response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
                   "* command with numbers, delimited by spaces."
        if command.startswith(EXAMPLE_COMMAND):
            response = "Sure...write some more code then I can do that!"
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)


    def parse_slack_output(slack_rtm_output):
        """
            The Slack Real Time Messaging API is an events firehose.
            this parsing function returns None unless a message is
            directed at the Bot, based on its ID.
        """
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(AT_BOT)[1].strip().lower(), \
                           output['channel']
        return None, None


The `parse_slack_output` function takes messages from Slack and determines 
if they are directed at our StarterBot. Messages that start with a direct
command to our bot ID are then handled by our code - which is currently
just posts a message back in the Slack channel telling the user to write
some more Python code!

Here is how the entire program should look when it's all put together
(you can also 
[view the file in GitHub](https://github.com/makaimc/slack-starterbot/blob/master/starterbot.py)):

```python
import os
import time
from slackclient import SlackClient


# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
```


Now that all of our code is in place we can run our StarterBot on the 
command line with the `python starterbot.py` command.

<img src="/source/static/img/160604-simple-python-slack-bot/starterbot-running.png" width="100%" class="technical-diagram img-rounded">

In Slack, create a new channel and invite StarterBot or invite it to an
existing channel.

<img src="/source/static/img/160604-simple-python-slack-bot/create-channel.png" width="100%" class="technical-diagram img-rounded">

Now start giving StarterBot commands in your channel.

<img src="/source/static/img/160604-simple-python-slack-bot/working-starterbot.png" width="100%" class="technical-diagram img-rounded">


## Wrapping Up
Alright, now you've got a simple StarterBot with a bunch of places in the 
code you can add whatever features you want to build. 

There is a whole lot more that could be done using the Slack RTM API and Python.
Check out these posts to learn what you could do:

* Attach a persistent [relational database](/databases.html) or 
  [NoSQL back-end](/no-sql-datastore.html) such as 
  [PostgreSQL](/postgresql.html), [MySQL](/mysql.html) or [SQLite](/sqlite.html)
  to save and retrieve user data
* Add another channel to interact with the bot 
  [via SMS](https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html) 
  or 
  [phone calls](https://www.twilio.com/blog/2016/05/add-phone-calling-slack-python.html)
* [Integrate other web APIs](/api-integration.html) such as 
  [GitHub](https://developer.github.com/v3/), 
  [Twilio](https://www.twilio.com/docs) or [api.ai](https://docs.api.ai/)


Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [makaimc](https://github.com/makaimc).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/makaimc/fullstackpython.com/blob/gh-pages/source/content/posts/160604-build-first-slack-bot-python.markdown).

