title: Monitoring
category: page
slug: monitoring
sortorder: 0715
toc: False
sidebartitle: Monitoring
meta: Monitoring tools capture and visualize data from an application's execution. Learn more about monitoring on Full Stack Python.


# Monitoring
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
* [statsd](https://github.com/etsy/statsd/) is a node.js network daemon that
  listens for metrics and aggregates them for transfer into another service
  such as Graphite.

* [Graphite](https://graphite.readthedocs.org/en/latest/overview.html) stores
  time-series data and displays them in graphs through a Django web application.

* [Bucky](http://github.hubspot.com/bucky/) measures the performance of a
  web application from end user's browsers and sends that data back to the
  server for collection.

* [Sensu](http://sensuapp.org/) is an open source monitoring framework
  written in Ruby but applicable to any programming language web application.

* [Graph Explorer](http://vimeo.github.io/graph-explorer/) by Vimeo is a
  Graphite-based dashboard with added features and a slick design.

* [PacketBeat](http://packetbeat.com/) sniffs protocol packets. Elasticsearch
  then allows developers to search the collected data and visualize what's 
  happening inside their web application using the Kibana user interface.

* [Munin](http://munin-monitoring.org/) is a client plugin-based monitoring 
  system that sends monitoring traffic to the Munin node where the data can
  be analyzed and visualized. Note this project is written in Perl so Perl 5
  must be installed on the node collecting the data.


## Hosted monitoring services
* [New Relic](http://newrelic.com/). Application and database monitoring as
  well as plug ins for capturing and analyzing additional data about tools in
  your stack.

* [CopperEgg](http://copperegg.com/) is lower-level monitoring on server and 
  infrastructure. It's popular with DevOps shops that are making changes to
  their production environments and want immediate feedback on the results
  of those modifications.

* [Status.io](http://status.io/) focuses on uptime and response metrics 
  transparency for web applications.

* [StatusPage.io](https://www.statuspage.io/) (yes, there's both a Status and
  StatusPage.io) provides easy set up status pages for monitoring application
  up time.

* [PagerDuty](http://www.pagerduty.com/) alerts a designated person or group
  if there are stability, performance, or uptime issues with an application.

* [App Enlight](https://appenlight.com/) provides performance, exception and 
  error monitoring and is currently specific to Python web applications.

* [Opbeat](https://opbeat.com) Built for django. Opbeat combines performance metrics, release tracking, and error logging into a single simple service.


## Monitoring resources
* [The Virtues of Monitoring](http://www.paperplanes.de/2011/1/5/the_virtues_of_monitoring.html)

* [Effortless Monitoring with collectd, Graphite, and Docker](http://blog.docker.io/2013/07/effortless-monitoring-with-collectd-graphite-and-docker/)

* [Practical Guide to StatsD/Graphite Monitoring](http://matt.aimonetti.net/posts/2013/06/26/practical-guide-to-graphite-monitoring/) 
  is a detailed guide with code examples for monitoring infrastructure.

* Bit.ly describes the 
  "[10 Things They Forgot to Monitor](http://word.bitly.com/post/74839060954/ten-things-to-monitor)"
  beyond the standard metrics such as disk & memory usage.

* [Four Linux server monitoring tools](http://aarvik.dk/four-linux-server-monitoring-and-management-tools/)

* [How to design useful monitoring and graphing visualizations](https://blog.serverdensity.com/how-to-design-useful-monitoring-graphs-and-visualizations/)

* [5 years of metrics and monitoring](https://speakerdeck.com/auxesis/5-years-of-metrics-and-monitoring)
  is a great presentation highlighting that visualization so humans can
  understand measurements is a hard problem. Line graphs are often not
  the best solution and they are overused.

* The Collector Highlight Series has an article on [StatsD](http://blog.librato.com/posts/statsd)
  that explains how to install it and how it works.

* This [survey on monitoring tools](http://kartar.net/2014/11/monitoring-survey---tools/)
  has some nice data and graphs on what developers and operations folks use
  in their environments.

* Ryan Frantz wrote a nice post on 
  [Solving Monitoring](http://ryanfrantz.com/posts/solving-monitoring/)
  with a new definition of what monitoring means based on today's complex
  systems and how the practice should evolve going forward.


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

