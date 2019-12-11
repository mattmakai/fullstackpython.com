title: Monitoring
category: page
slug: monitoring
sortorder: 0601
toc: False
sidebartitle: Monitoring
meta: Monitoring tools capture and visualize data from an application's execution. Learn more about monitoring on Full Stack Python.


Monitoring tools capture, analyze and display information for a web 
application's execution. Every application has issues arise throughout
all levels of the web stack. Monitoring tools provide transparency so
developers and operations teams can respond and fix problems.


## Why is monitoring necessary?
Capturing and analyzing data about your production environment is critical
to proactively deal with stability, performance, and errors in a web 
application.


## Difference between monitoring and logging
Monitoring and logging are very similar in their purpose of helping to 
diagnose issues with an application and aid the debugging process. One way
to think about the difference is that logging happens based on explicit events
while monitoring is a passive background collection of data. 

For example, when an error occurs, that event is explicitly logged through
code in an exception handler. Meanwhile, a monitoring agent instruments the
code and gathers data not only about the logged exception but also the 
performance of the functions.

This distinction between logging and monitoring is vague and not necessarily
the only way to look at it. Pragmatically, both are useful for maintaining a
production web application.


## Monitoring layers
There are several important resources to monitor on the operating system 
and network level of a web stack.

1. CPU utilization
2. Memory utilization
3. Persistence storage consumed versus free
4. Network bandwidth and latency

Application level monitoring encompasses several aspects. The amount of time
and resources dedicated to each aspect will vary based on whether an 
application is read-heavy, write-heavy, or subject to rapid swings in traffic.

1. Application warnings and errors (500-level HTTP errors)
2. Application code performance
3. Template rendering time
4. Browser rendering time for the application
5. Database querying performance


## Open source monitoring projects

* [Sentry](https://github.com/getsentry/sentry) started life as a 
  Python-only monitoring project but can now be used for any programming
  language.

* [Service Canary](https://servicecanary.com/)

* [ping.gg](https://ping.gg/) ([source code](https://github.com/pinggg/pingd))

* [glances](https://nicolargo.github.io/glances/) 
  ([source code](https://github.com/nicolargo/glances))

* [statsd](https://github.com/etsy/statsd/) is a node.js network daemon that
  listens for metrics and aggregates them for transfer into another service
  such as Graphite.

* [Graphite](https://graphite.readthedocs.org/en/latest/overview.html) stores
  time-series data and displays them in graphs through a Django web application.

* [Sensu](http://sensuapp.org/) is an open source monitoring framework
  written in Ruby but applicable to any programming language web application. 

* [Graph Explorer](http://vimeo.github.io/graph-explorer/) by Vimeo is a
  Graphite-based dashboard with added features and a slick design.

* [Munin](http://munin-monitoring.org/) is a client plugin-based monitoring 
  system that sends monitoring traffic to the Munin node where the data can
  be analyzed and visualized. Note this project is written in Perl so Perl 5
  must be installed on the node collecting the data.

* [Bucky](https://github.com/HubSpot/BuckyClient) measures the performance of a
  web application from end user's browsers and sends that data back to the
  server for collection.


## Hosted monitoring services
Hosted monitoring software takes away the burden of deploying and operating
the software yourself. However, hosted monitoring costs (often a significant 
amount of) money and take your application's data out of your hands so
these services are not the right fit for every project.

Error Tracking

* [Rollbar](https://rollbar.com/) instruments both the server side and
  client side to capture and report exceptions. The 
  [pyrollbar](https://rollbar.com/docs/notifier/pyrollbar/) code library
  provides quick integration for Python web applications. There are also
  specific instructions for common [web frameworks](/web-frameworks.html)
  such as [Django](/django.html) and [Pyramid](/pyramid.html).
* [Sentry](https://sentry.io/welcome/) is the hosted version of the open
  source tool that is used to monetize and support further development.

Application Performance Monitoring (APM)

* [New Relic](http://newrelic.com/) provides application and database 
  monitoring as well as plug ins for capturing and analyzing data about 
  other devleoper tools in your stack, such as [Twilio](/twilio.html).
* [Opbeat](https://opbeat.com) Built for django. Opbeat combines performance 
  metrics, release tracking, and error logging into a single simple service.
* [Scout](https://scoutapp.com/python-monitoring) monitors the performance of Django and Flask apps, auto-instrumenting views, SQL queries, templates, and more.

Status Pages

* [Status.io](http://status.io/) focuses on uptime and response metrics 
  transparency for web applications.
* [StatusPage.io](https://www.statuspage.io/) (yes, there's both a Status and
  StatusPage.io) provides easy set up status pages for monitoring application
  up time.

Incident Management

* [PagerDuty](http://www.pagerduty.com/) alerts a designated person or group
  if there are stability, performance, or uptime issues with an application.


## Monitoring resources
* [How to Add Hosted Monitoring to Flask Web Applications](/blog/hosted-monitoring-flask-web-apps.html)
  and
  [How to Monitor Bottle Web Applications](/blog/monitor-python-web-applications.html)
  are a couple of posts in a series showing how to add hosted monitoring to
  Python web apps built with any of the major Python 
  [web frameworks](/web-frameworks.html).

* [Stack Overflow: How We Do Monitoring - 2018 Edition](https://nickcraver.com/blog/2018/11/29/stack-overflow-how-we-do-monitoring/)
  is a detailed, long read about how Stack Overflow handles their 
  monitoring, health checks, alerting and dashboarding of their
  infrastructure.

* [The Virtues of Monitoring](http://www.paperplanes.de/2011/1/5/the_virtues_of_monitoring.html)

* [Effortless Monitoring with collectd, Graphite, and Docker](http://blog.docker.io/2013/07/effortless-monitoring-with-collectd-graphite-and-docker/)

* [Practical Guide to StatsD/Graphite Monitoring](http://matt.aimonetti.net/posts/2013/06/26/practical-guide-to-graphite-monitoring/) 
  is a detailed guide with code examples for monitoring infrastructure.

* Bit.ly describes the 
  "[10 Things They Forgot to Monitor](http://word.bitly.com/post/74839060954/ten-things-to-monitor)"
  beyond the standard metrics such as disk & memory usage.

* The videos from [Monitorama](https://vimeo.com/monitorama), a conference 
  that's all about monitoring and observability, are recordings of fantastic
  technical talks from their events.

* [Four Linux server monitoring tools](http://aarvik.dk/four-linux-server-monitoring-and-management-tools/)

* [How to design useful monitoring and graphing visualizations](https://blog.serverdensity.com/how-to-design-useful-monitoring-graphs-and-visualizations/)

* [5 years of metrics and monitoring](https://speakerdeck.com/auxesis/5-years-of-metrics-and-monitoring)
  is a great presentation highlighting that visualization so humans can
  understand measurements is a hard problem. Line graphs are often not
  the best solution and they are overused.

* [Keeping an eye on our network](https://githubengineering.com/keeping-an-eye-on-our-network/)
  explains how GitHub uses tagged metrics to keep better tabs on its
  infrastructure and network connections.

* [10 monitoring talks every developer should watch](https://techbeacon.com/devops/10-monitoring-talks-every-developer-should-watch)
  contains a great collection of relevant monitoring presentations.

* The Collector Highlight Series has an article on [StatsD](http://blog.librato.com/posts/statsd)
  that explains how to install it and how it works.

* OpenCensuss, OpenTracing and OpenMetrics are three projects that are trying
  to create standards for application monitoring metrics.
  [This article on the 3 projects](https://www.datadoghq.com/blog/instrument-opencensus-opentracing-and-openmetrics/)
  is a helpful overview to understand what each one is trying to do and how
  they compare to each other.


## Monitoring learning checklist
1. Review the software-as-a-service and open source monitoring tools below. 
   Third party services tend to be easier to set up and host the data for 
   you. Open source projects give you more control but you'll need to have 
   additional servers ready for the monitoring.

1. My recommendation is to install [New Relic](http://newrelic.com/)'s free 
   option with the trial period to see how it works with your app. It'll give 
   you a good idea of the capabilities for application-level monitoring tools.

1. As your app scales take a look at setting up one of the the open source 
   monitoring projects such as StatsD with Graphite. The combination of those
   two projects will give you fine-grained control over the system metrics 
   you're collecting and visualizing.

