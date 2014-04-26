title: Logging
category: page
slug: logging
sort-order: 081
choice1url: 
choice1icon: 
choice1text: 
choice2url: 
choice2icon: 
choice2text: 
choice3url: 
choice3icon: 
choice3text: 
choice4url:
choice4icon:
choice4text:


# Logging
Logging is a mechanism for monitoring web applications written with a
web framework. Runtime exceptions that prevent code from running are 
important to log to investigate and fix the source of the problems. 
Informational and debugging logging also helps to understand how the 
application is performing even if code is working as intended.

Logging is often grouped into several categories:

1. Information
2. Debug
3. Warning
4. Error

Logging errors that occur while a web framework is running is crucial to
understanding how your application is performing. 
[Raven](http://raven.readthedocs.org/en/latest/) is a Python client for the
[Sentry](https://github.com/getsentry/sentry) exception logging and 
aggregation application. Raven provides the way to send exceptions to
Sentry, which should be deployed on a separate server from your production
infrastructure. Raven can also be used by Python scripts to send other
log data to Sentry for aggregation. Sentry provides a clean web application
interface for viewing the exceptions. Sentry can also be configured with a
mail plugin to send emails when exceptions occur.


## Logging Aggregators
When you are running your application on several servers, it is helpful
to have a monitoring tool called a "logging aggregator". You can configure your
application to forward your system and application logs to one location that 
provides tools for viewing, searching, and monitoring logging events across your cluster. 

Another advantage of log aggregatortion tools is they allow you to set up custom alerts
and alarms so you can get notified when error rates breach a certain threshold.


### Log Aggregator Third Party Services
* [loggly](https://www.loggly.com/) Loggly is a third party cloud based application that
aggregates logs. They have instructions for every major language, including python. It includes email
alerting on custom searches. 
* [papertrail](https://papertrailapp.com/) Paper trail is similar to both loggly and splunk and provides
integration with S3 for 
* [splunk](http://www.splunk.com/) Splunk offers third party cloud and self hosted solutions 
for event aggregation. It excells at searching and data mining any text based data. 


### Open Source Log Aggregators
* [Graylog2](http://graylog2.org/) Provides a central server for log aggregation as well as a GUI for
browsing and searching through log events. There are libraries for most major languages, including python.
Saves data in elasicache.
* [Logstash](http://logstash.net/) Similar to Graylog2, logstash offers features to programatically
configure log data workflows.
* [Scribe](https://github.com/facebook/scribe) A project written by Facebook to aggregate logs. It's designed
to run on multiple servers and scale with the rest of your cluster. Uses the Thrift messagaing format so it can
be used with any language. 


## Logging resources
* This [intro to logging](http://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/)
  presents the Python logging module and how to use it.

* [Logging as Storytelling](http://www.hybridcluster.com/blog/logging-storytelling/)
  is a multi-part series working the analogy that logs should read like
  a story so you can better understand what's taking place in your web
  application. 
  [Part 2 describes actions](http://www.hybridcluster.com/blog/logging-storytelling-lets-add-action/)
  and 
  [part 3 talks about types](http://www.hybridcluster.com/blog/logging-storytelling-3-types/).


### Logging isn't enough. How do I analyze more data about the app?
