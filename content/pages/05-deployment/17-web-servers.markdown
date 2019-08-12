title: Web Servers
category: page
slug: web-servers
sortorder: 0517
toc: False
sidebartitle: Web Servers
meta: Web servers respond to HTTP requests for static content and serve as reverse proxies for Python web applications.


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


## Web server implementations
The conceptual web server idea can be implemented in various ways. The 
following web server implementations each have varying features, extensions
and configurations.

* The [Apache HTTP Server](/apache-http-server.html) has been the most 
  commonly deployed web server on the Internet for 20+ years.

* [Nginx](/nginx.html) is the second most commonly used server for the
  top 100,000 websites and often serves as a reverse proxy for 
  [Python WSGI servers](/wsgi-servers.html).

* [Caddy](/caddy.html) is a newcomer to the web server scene
  and is focused on serving the HTTP/2 protocol with HTTPS. 

* [rwasa](https://2ton.com.au/rwasa/) is a newer web server written
  in Assembly with no external dependencies that tuned to be faster than Nginx.
  The benchmarks are worth taking a look at to see if this server could fit
  your needs if you need the fastest performance trading off for as of yet
  untested web server.


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

<img src="/img/visuals/web-browser-server-requests.png" width="100%" class="technical-diagram" alt="Web server and web browser request-response cycle" />

A web server sends files to a web browser based on the web browser's 
request. In the first request, the browser accessed the 
"www.fullstackpython.com"
address and the server responded with the index.html HTML-formatted file. 
That HTML file contained references to other files, such as style.css and 
script.js that the browser then requested from the server.

Sending static assets (such as CSS and JavaScript files) can eat up a 
large amount of bandwidth which is why using a Content Delivery Network 
(CDN) to [serve static assets](/static-content.html) is important when 
possible.


### Building web servers
* [A Simple Web Server in less than 500 lines of code](http://aosabook.org/en/500L/a-simple-web-server.html)
  from the Architecture of Open Source book provides a great example 
  with Python as the implementation language..

* If you're looking to learn about web servers by building one, here's
  [part one](http://ruslanspivak.com/lsbaws-part1/),
  [part two](http://ruslanspivak.com/lsbaws-part2/) and [part three](http://ruslanspivak.com/lsbaws-part3/) 
  of a great tutorial that shows how to code a web server in Python.

* [Building a basic HTTP Server from scratch in Python](http://joaoventura.net/blog/2017/python-webserver/)
  ([source code](https://gist.github.com/joaoventura/824cbb501b8585f7c61bd54fec42f08f)
  builds a very simple but insecure web server to show you how HTTP works.


### Web server references
* [HTTP/1.1](http://www.w3.org/Protocols/rfc2616/rfc2616.html)
  and [HTTP/2](https://tools.ietf.org/html/rfc7540) specifications are the
  source for how web servers implement the modern web.

* A reference with the full list of 
  [HTTP status codes](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
  is provided by W3C.

* [Usage of web servers broken down by ranking](https://w3techs.com/technologies/cross/web_server/ranking)
  shows how popular [Apache](/apache-http-server.html), [Nginx](/nginx.html) 
  and other websites are among the top million through the top 1,000 sites
  in the world.

* [Apache vs Nginx: practical considerations](https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations)
  gives an an overview of each project, explains how each one handles
  connections, how it is configured and the differences between the
  two web servers in how it can use custom modules.

* [Optimizing web servers for high throughput and low latency](https://blogs.dropbox.com/tech/2017/09/optimizing-web-servers-for-high-throughput-and-low-latency/)
  is a wonderful read that shows how detailed knowledge at every layer of 
  the stack is necessary to optimize web server connections at scale.

* [Implementing a tiny web server in a single printf call](https://tinyhack.com/2014/03/12/implementing-a-web-server-in-a-single-printf-call/)
  is an absurd C language hack that you would never want to use in any 
  real project but still an amazing little application and wonderful 
  explanation that you can learn a bit more about web servers by reading.

* [Top 5 open source web servers](https://opensource.com/business/16/8/top-5-open-source-web-servers)
  is a short overview of [Apache](/apache-http-server.html), 
  [Nginx](/nginx.html), Lighttpd and two programming language specific
  servers, Node.js for JavaScript and Tomcat for Java.


### Web servers learning checklist
1. Choose a web server. [Nginx](http://nginx.org/en/) is often recommended 
   although [Apache](http://httpd.apache.org/) is also a great choice.

1. Create an SSL certificate via [Let's Encrypt](https://letsencrypt.org/). 
   You will need SSL for serving HTTPS traffic and preventing myriad 
   security issues that occur with unencrypted user input.

1. Configure the web server to serve up static files such as 
   [CSS](/cascading-style-sheets.html), [JavaScript](/javascript.html)
   and images.

1. Once you set up the [WSGI server](/wsgi-servers.html) you'll need to 
   configure the web server as a pass through for dynamic content.

