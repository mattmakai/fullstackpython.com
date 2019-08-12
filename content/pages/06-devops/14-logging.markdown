title: Logging
category: page
slug: logging
sortorder: 0614
toc: False
sidebartitle: Logging
meta: Logging saves error, warning and event output to storage for debugging purposes. Learn about logging on Full Stack Python.


Logging saves output such as errors, warnings and event information to 
persistent storage for debugging purposes. 


## Why is logging important?
Runtime exceptions that prevent code from running are important to log to 
investigate and fix the source of the problems. Informational and debugging 
logging also helps to understand how the application is performing even if 
code is working as intended.


## Logging levels
Logging is often grouped into several categories:

1. Information
1. Debug
1. Warning
1. Error

Logging errors that occur while a web framework is running is crucial to
understanding how your application is performing. 


## Logging aggregators
When you are running your application on several servers, it is helpful
to have a monitoring tool called a "logging aggregator". You can configure 
your application to forward your system and application logs to one location 
that provides tools for viewing, searching, and monitoring logging events 
across your cluster. 

Another advantage of log aggregation tools is they allow you to set up 
custom alerts and alarms so you can get notified when error rates breach a 
certain threshold.


### Open source log aggregators
* [Sentry](https://github.com/getsentry/sentry) started as a Django-only
  exception handling service but now has separate logging clients to cover 
  almost all major languages and frameworks. It still works really well for 
  Python-powered web applications and is often used in conjunction with other 
  monitoring tools. [Raven](http://raven.readthedocs.org/en/latest/) is open
  source Python client for Sentry.

* [Graylog2](http://graylog2.org/) provides a central server for log 
  aggregation as well as a GUI for browsing and searching through log events. 
  There are libraries for most major languages, including python. Saves data 
  in Elasticache.

* [Logstash](http://logstash.net/) Similar to Graylog2, logstash offers 
  features to programmatically configure log data workflows.

* [Scribe](https://github.com/facebook/scribe) A project written by Facebook 
  to aggregate logs. It's designed to run on multiple servers and scale with 
  the rest of your cluster. Uses the Thrift messaging format so it can be 
  used with any language. 


### Hosted logging services
* [Loggly](https://www.loggly.com/) is a third party cloud based 
  application that aggregates logs. They have instructions for every major 
  language, including python. It includes email alerting on custom searches. 

* [Splunk](http://www.splunk.com/) offers third party cloud and self 
  hosted solutions for event aggregation. It excels at searching and data 
  mining any text based data. 

* [Papertrail](https://papertrailapp.com/) is similar to both 
  Loggly and Splunk and provides integration with S3 for long term storage.

* [Raygun](http://raygun.io/) logs errors and provides immediate notification
  when issues arise.

* [Scalyr](https://www.scalyr.com/) provides log aggregation, dashboards,
  alerts and search in a user interface on top of standard logs.

* There is a [hosted version of Sentry](https://www.getsentry.com/welcome/)
  in case you do not have the time to set up the open source project yourself.


## Logging resources
* This 
  [intro to logging](http://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/)
  presents the Python logging module and how to use it.

* [Understanding Python's logging module](https://www.electricmonk.nl/log/2017/08/06/understanding-pythons-logging-module/)
  clears up some misconceptions about how pattern matching with logging
  hierarchies works and provides a few clear diagrams to visually explain
  logging handlers.

* [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
  contains useful code snippets to easily add logging to your own applications.

* [Logging in Python](https://realpython.com/python-logging/) explains 
  the logging module in the Python standard library, configuration 
  settings, handlers and how to log data.

* [A Brief Digression About Logging](https://lukasa.co.uk/2014/05/A_Brief_Digression_About_Logging/)
  is a short post that gets Python logging up and running quickly.

* [Taking the pain out of Python logging](https://hynek.me/articles/taking-some-pain-out-of-python-logging/)
  provides a logging set up with uWSGI.

* [Good logging practice in Python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
  shows how to use the standard library to log data from your application.
  Definitely worth a read as most applications do not log nearly enough
  output to help debuggin when things go wrong, or to determine if something
  is going wrong.

* [Structured Logging: The Best Friend You’ll Want When Things Go Wrong](https://engineering.grab.com/structured-logging)
  explains how Grab (a large ridesharing platform in Asia) uses
  structured logging to reduce Mean Time To Resolve (MTTR) and how they
  arranged their log levels to support their scale.

* [How to collect, customize, and centralize Python logs](https://www.datadoghq.com/blog/python-logging-best-practices/)
  covers the standard library `logging` module and how to configure
  it for various ways you are likely to use it with one or more 
  Python applications.

* [A guide to logging in Python](https://opensource.com/article/17/9/python-logging)
  has some clear, simple diagrams to explain how logging works in Python
  applications.

* [Django Logging, the Right Way](https://lincolnloop.com/blog/django-logging-right-way/)
  covers a few Python logging techniques and then goes into how you use them
  with your [Django](/django.html) projects.

* Django's 1.3 release brought unified logging into project configurations. 
  This [post shows how to set up logging](http://www.djm.org.uk/how-to-log-file-django-13-and-above/)
  in a project's settings.py file. Caktus Group also has a nice tutorial on
  [central logging with graypy and Graylog2](http://www.caktusgroup.com/blog/2013/09/18/central-logging-django-graylog2-and-graypy/).

* [Django Logging Configuration: How the Default Settings Interfere with Yours](http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)
  explains a problem with the default Django logging configuration and what
  to do about in your project.

* [The Pythonic Guide To Logging](https://timber.io/blog/the-pythonic-guide-to-logging/)
  provides a quick introduction to log levels in Python code.

* [Exceptional Logging of Exceptions in Python](https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/)
  shows how to log errors more accurately to pinpoint the problem instead of
  receiving generic exceptions in your logs.

* [Python and Django logging in plain English](https://djangodeconstructed.com/2018/12/18/django-and-python-logging-in-plain-english/)
  is a wonderful overview of how to configure logging in 
  [Django](/django.html) projects.


## Logging learning checklist
1. Read how to integrate logging into your web application framework. 

1. Ensure errors and anomalous results are logged. While these logs can be 
   stored in [monitoring](/monitoring.html) solutions, it's best to have your 
   own log storage location to debug issues as they arise to complement other 
   monitoring systems.

1. Integrate logging for system events you may need to use for debugging 
   purposes later. For example, you may want to know the return values on 
   functions when they are above a certain threshold. 

