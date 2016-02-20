title: Nginx
category: page
slug: nginx
sortorder: 0721
toc: False
sidebartitle: Nginx
meta: Nginx is a commonly deployed web server that also functions well as a reverse proxy for WSGI Python web apps.


# Nginx
Nginx is the 
[second most common web server among the top 100,000 websites](http://w3techs.com/technologies/cross/web_server/ranking). Nginx also functions well as a 
reverse proxy to handle requests and pass back responses for Python 
[WSGI servers](/wsgi-servers.html) or even other web servers such as Apache.

<img src="/img/web-servers-map.png" width="100%" alt="Python web application deployments rely on Nginx either as a web server or reverse proxy for WSGI servers." class="technical-diagram" />


<div class="well see-also">Nginx is an implementation of the <a href="/web-servers.html">web server</a> concept. Learn how these pieces fit together in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Should I use Nginx or the Apache HTTP Server?
Let's be clear about these two "competing" servers: they are both fantastic
open source projects and either will serve your web application deployment 
well. In fact, many of the top global web applications use both servers in
their deployments to function in many steps throughout the HTTP 
request-response cycle.

I personally use Nginx more frequently than Apache because Nginx's 
configuration feel easier to write, with less boilerplate than alternatives.

There's also a bit of laziness in the usage: Nginx works well, it never causes
me problems. So I stick with my battle-tested 
Ansible [configuration management](/configuration-management.html) files
that set up Nginx with HTTPS and SSL/TLS certificates 


## Nginx resources
* The [Nginx chapter](http://www.aosabook.org/en/nginx.html) in the
  [Architecture of Open Source Applications book](http://www.aosabook.org/en/index.html)
  has a great chapter devoted to why Nginx is built to scale a certain way
  and lessons learned along the development journey.

* [Inside Nginx: How we designed for performance and scale](http://nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
  is a blog post from the developers behind Nginx on why they believe their
  architecture model is more performant and scalable than other approaches
  used to build web servers.

* [Nginx web server tutorials](http://articles.slicehost.com/nginx) are oldies
  but goodies on setting up previous versions of Nginx. 

* [Nginx for Developers: An Introduction](http://carrot.is/coding/nginx_introduction)

* An example of an [Nginx security configuration](http://tautt.com/best-nginx-configuration-for-security/).

* [A faster Web server: ripping out Apache for Nginx](http://arstechnica.com/business/2011/11/a-faster-web-server-ripping-out-apache-for-nginx/)
  explains how Nginx can be used instead of Apache in some cases for
  better performance.

* [Rate Limiting with Nginx](http://lincolnloop.com/blog/rate-limiting-nginx/)
  covers how to mitigate against brute force password guessing attempts using
  Nginx rate limits.

* [Nginx with dynamic upstreams](http://tenzer.dk/nginx-with-dynamic-upstreams/)
  is an important note for setting up your upstream WSGI server(s) if you're
  using Nginx as a reverse proxy with hostnames that change.

* [Nginx Caching](https://serversforhackers.com/nginx-caching/) shows how
  to set up Nginx for caching HTTP requests, which is often done by Varnish
  but can also be handled by Nginx with the `proxy_cache` and related
  directives.

