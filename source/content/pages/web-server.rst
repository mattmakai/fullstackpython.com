Web Server
==========

:category: page
:slug: web-server
:sort-order: 04

A web server handles Hypertext Transfer Protocol (HTTP) requests from
clients. The client is usually a browser such as Internet Explorer, Firefox,
and Chrome, but it can also be a headless browser like 
`phantomjs <http://phantomjs.org/>`_ (commonly used for testing), a
commandline utility like wget or curl, or a web crawler. The web server
processes the request and sends a status code and depending on the
status code a content response as well.

In a simple case, the client will request a static asset such as a picture
or JavaScript file. The file sits on the file system in a location the
web server is authorized to access and the web server sends the file
to the clinet with a 200 status code. If the client already requested the
file and the file has not changed, the web server will pass back a 304 
"Not modified" response indicating the client already has the latest version
of that file.


.. image:: ../img/web-server-web-browser.jpg
  :alt: Web server and web browser request-response cycles

A web server sends files to a web browser based on the web browser's 
request. In the first request, the browser accessed the "www.example.com"
address and the server responded with the index.html HTML-formatted file. 
That HTML file contained references to other files, such as style.css and 
script.js that the browser then requested from the server.

Sending static assets (such as CSS and JavaScript files) can eat up a 
large amount of bandwidth which is why using a Content Delivery Network 
(CDN) is important when possible (see the content delivery network 
section for a more detailed explanation).


Web Server Resources
--------------------
`Apache and mod_wsgi on Ubuntu 10.04 <http://library.linode.com/web-servers/apache/mod-wsgi/ubuntu-10.04-lucid>`_

`HTTP Status Codes <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>`_
