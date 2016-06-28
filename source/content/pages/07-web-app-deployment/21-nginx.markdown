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

## Securing Nginx
Nginx's default configuration after a standard installation through a
system package manager or compiling from source is a good base for security.
However, setting up ciphers and redirects can be confusing the first few
times you try it. It's a really good idea to read some of these tutorials
to make sure you are avoiding the most common security errors that plague
HTTP(S) configurations.

* [Hacker News broke our site – how Nginx and PageSpeed fixed the problem](https://www.airport-parking-shop.co.uk/blog/hacker-news-broke-site-nginx-pagespeed-fixed-problem/)
  is primarily about optimizing Nginx's configuration for more efficient 
  SSL connections. The post also covers 
  [configuration management](/configuration-management.html) with Ansible
  as well as the Pagespeed module that Google released for both Nginx
  and the [Apache HTTP Server](/apache-http-server.html).

* [Secure Web Deployment with Let's Encrypt and Nginx](https://letsecure.me/secure-web-deployment-with-lets-encrypt-and-nginx/ )
  is a detailed walkthrough for setting up HTTPS under Ubuntu 14.04 with
  Nginx.

* [How To Secure Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-on-ubuntu-14-04)
  explains SSL configurations and IP address blacklisting then provides
  several other tutorials for more advanced security modules.

* [Strong SSL Security on Nginx](https://raymii.org/s/tutorials/Strong_SSL_Security_On_nginx.html)
  shows how to mitigate high profile SSL attacks like 
  [Logjam](https://weakdh.org/),
  [Heartbleed](http://heartbleed.com/)
  and [FREAK](https://freakattack.com/).


## General Nginx resources
* The [Nginx chapter](http://www.aosabook.org/en/nginx.html) in the
  [Architecture of Open Source Applications book](http://www.aosabook.org/en/index.html)
  has a great chapter devoted to why Nginx is built to scale a certain way
  and lessons learned along the development journey.

* [Inside Nginx: How we designed for performance and scale](http://nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
  is a blog post from the developers behind Nginx on why they believe their
  architecture model is more performant and scalable than other approaches
  used to build web servers.

* [Test-driving web server configuration](https://gdstechnology.blog.gov.uk/2015/03/25/test-driving-web-server-configuration/)
  is a good story for how to iteratively apply configuration changes, such
  as routing traffic to [Piwik](http://piwik.org/) for 
  [web analytics](/web-analytics.html), reverse proxying to backend
  application servers and terminately TLS connections appropriately.
  It is impressive to read a well-written softare development article like
  this from a government agency, although UK's Government Digital Service as
  well as USA's 18F and US Digital Service foster a far more credible
  culture than most typical agencies.

* [Nginx for Developers: An Introduction](http://carrot.is/coding/nginx_introduction)
  provides the first steps to getting an initial Nginx configuration up and
  running. 

* [A faster Web server: ripping out Apache for Nginx](http://arstechnica.com/business/2011/11/a-faster-web-server-ripping-out-apache-for-nginx/)
  explains how Nginx can be used instead of Apache in some cases for
  better performance.

* [Nginx vs Apache: Our view](https://www.nginx.com/blog/nginx-vs-apache-our-view/)
  is a first-party perspective written by the developers behind Nginx
  as to the differences between the web servers.

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

* [Nginx web server tutorials](http://articles.slicehost.com/nginx) are oldies
  but goodies on setting up previous versions of Nginx. 

* [Dynamic log formats in nginx](https://benwilber.github.io/nginx/syslog/logging/2015/08/26/dynamic-log-formats-in-nginx.html) 
  explains how to use the HttpSetMiscModule module to transform variables
  in Nginx and map input to controlled output in the logs. The author uses
  this technique for pixel tracking but there are other purposes this method
  could be used for such as advanced debugging. 


