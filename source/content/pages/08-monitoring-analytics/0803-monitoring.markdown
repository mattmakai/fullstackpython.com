title: Monitoring
category: page
slug: monitoring
sort-order: 082
choice1url: /web-analytics.html
choice1icon: fa-dashboard
choice1text: How do I learn more about the users of my app with web analytics?
choice2url: /web-application-security.html
choice2icon: fa-lock fa-inverse
choice2text: What should I learn about web application security?
choice3url: /configuration-management.html
choice3icon: fa-gears fa-inverse
choice3text: How do I automate the server configuration I've set up?
choice4url: /logging.html
choice4icon: fa-align-left fa-inverse
choice4text: How should I log events in my application outside monitoring?


# Monitoring
Monitoring tools capture, analyze and display information for a web 
application's execution. Every application has issues arise throughout
all levels of the web stack. Monitoring tools provide transparency so
developers and operations teams can respond and fix problems.


## Why is monitoring necessary?
Capturing and analyzing data about your production environment is critical
to proactively deal with stability, performance, and errors in a web 
application.

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


## Monitoring Third Party Services
* [New Relic](http://newrelic.com/). Application and database monitoring as
  well as plug ins for capturing and analyzing additional data about tools in
  your stack.

* [CopperEgg](http://copperegg.com/) is lower-level monitoring on server and 
  infrastructure. It's popular with DevOps shops that are making changes to
  their production environments and want immediate feedback on the results
  of those modifications.

* [Status.io](http://status.io/) focuses on uptime and response metrics 
  transparency for your users.

* [PagerDuty](http://www.pagerduty.com/) alerts a designated person or group
  if there are stability, performance, or uptime issues with an application.


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

* The Collector Highlight Series has an article on [StatsD](http://blog.librato.com/posts/statsd)
  that explains how to install it and how it works.


### What topic do you want to learn next?
