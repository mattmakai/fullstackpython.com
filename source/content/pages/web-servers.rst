===========
Web Servers
===========

:category: page
:slug: web-servers
:sort-order: 04

Web servers respond to 
`Hypertext Transfer Protocol (HTTP) <http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ 
requests from
clients. A client is usually a browser such as Internet Explorer, Firefox,
or Chrome, but it can also be a

* headless browser, which is commonly use for testing, such as 
  `phantomjs <http://phantomjs.org/>`_ 
* commandline utility like `wget <https://www.gnu.org/software/wget/>`_ 
  or `curl <http://curl.haxx.se/>`_
* a text-based web browser such as 
  `Lynx <http://en.wikipedia.org/wiki/Lynx_(web_browser)>`_
* web crawler. 

Web server process requests from the above clients. The result of the web
server's processing is a 
`response code <https://developer.mozilla.org/en-US/docs/HTTP/Response_codes>`_
and commonly a content response. Some status codes, such as 204 (No content) 
and 403 (Forbidden), do not have content responses.

In a simple case, the client will request a static asset such as a picture
or JavaScript file. The file sits on the file system in a location the
web server is authorized to access and the web server sends the file
to the client with a 200 status code. If the client already requested the
file and the file has not changed, the web server will pass back a 304 
"Not modified" response indicating the client already has the latest version
of that file.


.. image:: theme/img/web-browser-server-requests.png
  :alt: Web server and web browser request-response cycles
  :width: 100%
  :class: technical-diagram

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


Web Server Resources
--------------------
`How to set up a safe and secure Web server <http://arstechnica.com/gadgets/2012/11/how-to-set-up-a-safe-and-secure-web-server/>`_ 

`Apache and mod_wsgi on Ubuntu 10.04 <http://library.linode.com/web-servers/apache/mod-wsgi/ubuntu-10.04-lucid>`_

`Nginx web server tutorials <http://articles.slicehost.com/nginx>`_

`Nginx for Developers: An Introduction <http://carrot.is/coding/nginx_introduction>`_

`Nginx security configuration example <http://tautt.com/best-nginx-configuration-for-security/>`_

`HTTP Status Codes <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>`_

`Battle ready Nginx - an optimization guide <http://blog.zachorr.com/nginx-setup/>`_

`A faster Web server: ripping out Apache for Nginx <http://arstechnica.com/business/2011/11/a-faster-web-server-ripping-out-apache-for-nginx/>`_

`4 HTTP Security Headers You Should Always Be Using <http://ibuildings.nl/blog/2013/03/4-http-security-headers-you-should-always-be-using>`_
