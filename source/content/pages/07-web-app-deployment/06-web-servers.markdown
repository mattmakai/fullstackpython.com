title: Web Servers
category: page
slug: web-servers
sort-order: 0706
meta: A web server handles HTTP requests and responses. Learn how web servers work with Python web apps on Full Stack Python.


# Web servers
Web servers respond to 
[Hypertext Transfer Protocol](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (HTTP)
requests from clients and send back a response containing a status code and
often content such as HTML, XML or JSON as well.

## Why are web servers necessary?
Web servers are the ying to the web client's yang. The server and client speak
the standardized language of the World Wide Web. This standard language
is why an old Mozilla Netscape browser can still talk to a modern Apache or
Nginx web server, even if it cannot properly render the page design like a 
modern web browser can. 

The basic language of the Web with the request and response cycle from 
client to server then server back to client remains the same as it was when
the Web was invented by 
[Tim Berners-Lee](http://www.w3.org/People/Berners-Lee/) at CERN in 1989.
Modern browsers and web servers have simply extended the language of the Web
to incorporate new standards.


## Client requests
A client that sends a request to a web server is usually a browser such 
as Internet Explorer, Firefox, or Chrome, but it can also be a

* headless browser, commonly use for testing, such as 
  [phantomjs](http://phantomjs.org/)
* commandline utility, for example [wget](https://www.gnu.org/software/wget/)
  and [cURL](http://curl.haxx.se/)
* text-based web browser such as 
  [Lynx](http://lynx.browser.org/)
* web crawler. 

Web servers process requests from the above clients. The result of the web
server's processing is a 
[response code](https://developer.mozilla.org/en-US/docs/HTTP/Response_codes)
and commonly a content response. Some status codes, such as 204 (No content) 
and 403 (Forbidden), do not have content responses.

In a simple case, the client will request a static asset such as a picture
or JavaScript file. The file sits on the file system in a location the
web server is authorized to access and the web server sends the file
to the client with a 200 status code. If the client already requested the
file and the file has not changed, the web server will pass back a 304 
"Not modified" response indicating the client already has the latest version
of that file.

<img src="theme/img/web-browser-server-requests.png" width="100%" class="technical-diagram" alt="Web server and web browser request-response cycle" />

A web server sends files to a web browser based on the web browser's 
request. In the first request, the browser accessed the 
"www.fullstackpython.com"
address and the server responded with the index.html HTML-formatted file. 
That HTML file contained references to other files, such as style.css and 
script.js that the browser then requested from the server.

Sending static assets (such as CSS and JavaScript files) can eat up a 
large amount of bandwidth which is why using a Content Delivery Network 
(CDN) is important when possible (see the content delivery network 
section for a more detailed explanation).


## Web server resources
* [HTTP/1.1 Specification](http://www.w3.org/Protocols/rfc2616/rfc2616.html)

* [How to set up a safe and secure Web server](http://arstechnica.com/gadgets/2012/11/how-to-set-up-a-safe-and-secure-web-server/)

* [Apache and mod\_wsgi on Ubuntu 10.04](http://library.linode.com/web-servers/apache/mod-wsgi/ubuntu-10.04-lucid)

* A reference with the full list of 
[HTTP status codes](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
is provided by W3C.

* [4 HTTP Security Headers You Should Always Be Using](http://ibuildings.nl/blog/2013/03/4-http-security-headers-you-should-always-be-using)

* If you're looking to learn about web servers by building one, here's
  [part one](http://ruslanspivak.com/lsbaws-part1/),
  [part two](http://ruslanspivak.com/lsbaws-part2/) and [part three](http://ruslanspivak.com/lsbaws-part3/) 
  of a great tutorial that shows how to code a web server in Python.


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

* [rwasa](https://2ton.com.au/rwasa/) is a newly released web server written
  in Assembly with no external dependencies that tuned to be faster than Nginx.
  The benchmarks are worth taking a look at to see if this server could fit
  your needs if you need the fastest performance trading off for as of yet
  untested web server.

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


## Web servers learning checklist
1. Choose a web server. [Nginx](http://nginx.org/en/) is often recommended 
   although [Apache](http://httpd.apache.org/) is also a great choice.

1. Create an SSL certificate. For testing use a self-signed certificate 
   and for a production app buy one from [Digicert](http://www.digicert.com/). 
   Configure the web server to serve traffic over SSL. You'll need SSL for 
   serving only HTTPS traffic and preventing security issues that occur with 
   unencrypted user input.

1. Configure the web server to serve up static files such as CSS, JavaScript
   and images.

1. Once you set up the [WSGI server](/wsgi-servers.html) you'll need to 
   configure the web server as a pass through for dynamic content.

