==========
Monitoring
==========

:category: page
:slug: monitoring
:sort-order: 14

Capturing and analyzing data about your production environment is critical
to proactively deal with stability, performance, and errors in a web 
application.

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


Monitoring Third Party Services
-------------------------------
`New Relic <http://newrelic.com/>`_. Application and database monitoring as
well as plug ins for capturing and analyzing additional data about tools in
your stack.

`CopperEgg <http://copperegg.com/>`_ is lower-level monitoring on server and 
infrastructure. It's popular with DevOps shops that are making changes to
their production environments and want immediate feedback on the results
of those modifications.

`Status.io <http://status.io/>`_ focuses on uptime and response metrics 
transparency for your users.

`PagerDuty <http://www.pagerduty.com/>`_ alerts a designated person or group
if there are stability, performance, or uptime issues with an application.


Open Source Projects
--------------------
`statsd <https://github.com/etsy/statsd/>`_ is a node.js network daemon that
listens for metrics and aggregates them for transfer into another service
such as Graphite.

`Graphite <https://graphite.readthedocs.org/en/latest/overview.html>`_ stores
time-series data and displays them in graphs through a Django web application.

`Sensu <http://sensuapp.org/>`_ is an open source monitoring framework
written in Ruby but applicable to any programming language web application.

`Graph Explorer <http://vimeo.github.io/graph-explorer/>`_ by Vimeo is a
Graphite-based dashboard with added features and a slick design.


Monitoring Resources
--------------------
`The Virtues of Monitoring <http://www.paperplanes.de/2011/1/5/the_virtues_of_monitoring.html>`_

`Effortless Monitoring with collectd, Graphite, and Docker <http://blog.docker.io/2013/07/effortless-monitoring-with-collectd-graphite-and-docker/>`_

Bit.ly describes the "`10 Things We Forgot to Monitor <http://word.bitly.com/post/74839060954/ten-things-to-monitor>`_"
beyond the standard metrics such as disk & memory usage.

`Four Linux server monitoring tools <http://aarvik.dk/four-linux-server-monitoring-and-management-tools/>`_

`How to design useful monitoring and graphing visualizations <https://blog.serverdensity.com/how-to-design-useful-monitoring-graphs-and-visualizations/>`_
