title: Apache HTTP Server
category: page
slug: apache-http-server
sortorder: 0722
toc: False
sidebartitle: Apache HTTP Server
meta: Apache HTTP Server is a widely deployed web server and is often used with WSGI to serve Python web apps.


# Apache HTTP Server
The [Apache HTTP Server](https://httpd.apache.org/) is a widely deployed web server
that can be used in combination with a WSGI module, such as mod\_wsgi or a
stand-alone [WSGI server](/wsgi-servers.html) to run Python web applications.


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

* [Apache Web Server on Ubuntu 14.04 LTS](https://www.linode.com/docs/websites/apache/apache-web-server-on-ubuntu-14-04)
  explains how to install Apache on Ubuntu 14.04, which is still a supported
  release. Note however, do *not* install mod\_python because it is now insecure
  and made obsolete by [mod\_wsgi and WSGI servers](/wsgi-servers.html).

* [Deploy Django on Apache with Virtualenv and mod\_wsgi](http://thecodeship.com/deployment/deploy-django-apache-virtualenv-and-mod_wsgi/)
  provides instructions for what packages to install to get Apache up
  and running with mod\_wsgi on Ubuntu.

* [Apache and mod\_wsgi on Ubuntu 10.04](http://library.linode.com/web-servers/apache/mod-wsgi/ubuntu-10.04-lucid)
  is an older post that shows how to set up Apache on the now out-of-support
  Ubuntu 10.04 LTS release. This setup isn't recommended in 2016 and beyond
  but if you are already using 10.04 as your base operating system you might
  need to reference this material.

