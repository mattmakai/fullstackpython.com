title: Web Servers
category: page
slug: web-servers
sort-order: 04


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
  and [curl](http://curl.haxx.se/)
* text-based web browser such as 
  [Lynx](http://lynx.browser.org/)
* web crawler. 

Web server process requests from the above clients. The result of the web
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

* [Nginx web server tutorials](http://articles.slicehost.com/nginx)

* [Nginx for Developers: An Introduction](http://carrot.is/coding/nginx_introduction)

* An example of an [Nginx security configuration](http://tautt.com/best-nginx-configuration-for-security/).

* A reference with the full list of 
[HTTP status codes](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
is provided by W3C.

* An optimization guide for 
"[battle ready Nginx](http://blog.zachorr.com/nginx-setup/)."

* [A faster Web server: ripping out Apache for Nginx](http://arstechnica.com/business/2011/11/a-faster-web-server-ripping-out-apache-for-nginx/)

* [4 HTTP Security Headers You Should Always Be Using](http://ibuildings.nl/blog/2013/03/4-http-security-headers-you-should-always-be-using)


### What do you want to learn after setting up a web server?
