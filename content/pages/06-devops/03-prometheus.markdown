title: Prometheus
category: page
slug: prometheus
sortorder: 0603
toc: False
sidebartitle: Prometheus
meta: Prometheus is an open source monitoring tool that can be used to instrument and report on Python web apps.


[Prometheus](https://prometheus.io/) 
([source code](https://github.com/prometheus/prometheus))  is an open
source [monitoring](/monitoring.html) tool that can be used to instrument 
and report on Python [web applications](/web-development.html).

<a href="https://prometheus.io/" style="border: none;"><img src="/img/logos/prometheus.jpg" width="100%" alt="Prometheus project logo." class="shot"></a>


### Prometheus resources
* [Prometheus-Basics](https://github.com/yolossn/Prometheus-Basics)
  is a newbie's introduction to this tool. It covers what Prometheus
  is, the tool's architecture, types of metrics and contains a
  walkthrough of how to get it configured.

* This primer on [Prometheus](https://www.kartar.net/2017/10/prometheus/) 
  walks through installation, configuration and metrics collection.

* [Monitoring synchronous Python web apps with Prometheus](https://blog.codeship.com/monitoring-your-synchronous-python-web-applications-using-prometheus/)
  and its
  [asynchronous monitoring](https://blog.codeship.com/monitoring-your-asynchronous-python-web-applications-using-prometheus/)
  counterpart are two tutorials that show how to add middleware
  to your web apps that allows Prometheus metrics collection.

* [Monitoring with Prometheus](https://kjanshair.github.io/2018/02/20/prometheus-monitoring/)
  provides an overview of the tool and explains how to combine it
  with [Grafana](https://grafana.com/) to visualize the metrics
  that are collected.

* [Monitor your applications with Prometheus](https://blog.alexellis.io/prometheus-monitoring/)
  is a getting started guide with a walkthrough of how to instrument
  a simple Golang application.

* [Custom Application Metrics with Django, Prometheus, and Kubernetes](https://labs.meanpug.com/custom-application-metrics-with-django-prometheus-and-kubernetes/)
  shows how to handle the initial configuration with `django-prometheus`,
  deploys the [Django](/django.html) web app using 
  [Helm](https://helm.sh/) and configures Prometheus to scrape metrics
  from the application running on Kubernetes.

* [A gentle introduction to the wonderful world of metrics](https://tech.showmax.com/2019/10/prometheus-introduction/)
  has a quick summary that compares Prometheus with Nagios, then digs
  into the logging format and what you can visualize with this tool.

* [From Graphite to Prometheus](https://engineering.nanit.com/from-graphite-to-prometheus-things-ive-learned-e1d1e4b97fc)
  explains some of the differences between using a StatsD / Graphite 
  monitoring stack and Prometheus, such as how Prometheus scrapes data
  instead of the applications pushing data to a metrics aggregator,
  and the query languages for each tool.
