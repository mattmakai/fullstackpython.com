title: Apache HTTP Server
category: page
slug: apache-http-server
sortorder: 0518
toc: False
sidebartitle: Apache HTTP Server
meta: Apache HTTP Server is a widely deployed web server and is often used with WSGI to serve Python web apps.


The [Apache HTTP Server](https://httpd.apache.org/) is a widely deployed web server
that can be used in combination with a WSGI module, such as mod\_wsgi or a
stand-alone [WSGI server](/wsgi-servers.html) to run Python web applications.

<a href="https://httpd.apache.org/" style="border: none;"><img src="/img/logos/apache-http-server.jpg" width="100%" alt="Apache HTTP Server logo." class="technical-diagram"></a>


## Why is the Apache HTTP Server important?
Apache remains the most commonly deployed web server with a reign of
20+ years. Its wide usage contributes to the large number of tutorials
and open source modules created by developers for anyone to use.

Apache's development began in mid-1994 as a fork of the
[NCSA HTTP Server](https://en.wikipedia.org/wiki/NCSA_HTTPd) project.
By early 1996, Apache overtook the previously dominant but suddenly stagnant 
NCSA server as NCSA's progress stalled due to signficantly reduced 
development attention.

<div class="well see-also">The Apache HTTP Server is an implementation of the <a href="/web-servers.html">web server</a> concept. Learn how these pieces fit together in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>



### Apache HTTP Server resources
* The 
  [official project documentation page](http://httpd.apache.org/docs/current/)
  contains a section with How-Tos and Tutorials to handle authentication,
  security and dynamic content.

* [Reverse proxies](http://www.apachetutor.org/admin/reverseproxies) shows
  how to set up Apache as a reverse proxy using `mod_proxy`.

* [Deploy Django on Apache with Virtualenv and mod\_wsgi](http://thecodeship.com/deployment/deploy-django-apache-virtualenv-and-mod_wsgi/)
  provides instructions for what packages to install to get Apache up
  and running with mod\_wsgi on Ubuntu.

* [Detecting Bots in Apache & Nginx Logs](http://tech.marksblogg.com/detect-bots-apache-nginx-logs.html)
  is a great tutorial for filtering out the significant traffic generated
  by web crawlers and bots when using Apache HTTP Server logs for traffic
  analytics.

* [Apache vs Nginx: Practical Considerations](https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations)
  is a good comparison post that covers the differences between Apache and
  [Nginx](/nginx.html) such as how they handle connections and serve content.

* [Monitoring Apache web server performance](https://www.datadoghq.com/blog/monitoring-apache-web-server-performance/)
  gives a really nice overview of metrics to watch when you are using
  Apache as your web server.

* [Web Performance 101: HTTP Headers](https://dzone.com/articles/web-performance-101-http-headers)
  covers the gamut of HTTP headers and shows how they can impact performance 
  based on your configuration.

* [Apache Web Server on Ubuntu 14.04 LTS](https://www.linode.com/docs/websites/apache/apache-web-server-on-ubuntu-14-04)
  explains how to install Apache on Ubuntu 14.04, which is still a supported
  release. Note however, do *not* install mod\_python because it is now insecure
  and made obsolete by [mod\_wsgi and WSGI servers](/wsgi-servers.html).

