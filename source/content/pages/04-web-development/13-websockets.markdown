title: WebSockets
category: page
slug: websockets
sortorder: 0413
toc: False
sidebartitle: WebSockets
meta: WebSockets are a protocol for full-duplex web communications. Learn about WebSockets on Full Stack Python.


# WebSockets
A WebSocket is a [standard protocol](http://tools.ietf.org/html/rfc6455) for 
two-way data transfer between a client and server. The WebSockets protocol 
does not run over HTTP, instead it is a separate implementation on top of 
[TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol).


## Why use WebSockets?
A WebSocket connection allows full-duplex communication between a client 
and server so that either side can push data to the other through an 
established connection. The reason why WebSockets, along with the related 
technologies of 
[Server-sent Events](http://en.wikipedia.org/wiki/Server-sent_events) (SSE) 
and 
[WebRTC data channels](https://tools.ietf.org/html/draft-ietf-rtcweb-data-channel-12), 
are important is that HTTP is not meant for keeping open a connection for
the server to frequently push data to a web browser. Previously, most web
applications would implement long polling via frequent
Asynchronous JavaScript and XML (AJAX) requests as shown in the below diagram. 

<img src="/img/ajax-long-polling.png" width="100%" alt="Long polling via AJAX is incredibly inefficient for some applications." class="technical-diagram" />

Server push is more efficient and scalable than long polling because the 
web browser does not have to constantly ask for updates through a stream 
of AJAX requests.

<img src="/img/websockets-flow.png" width="100%" alt="WebSockets are more efficient than long polling for server sent updates." class="technical-diagram" />

While the above diagram shows a server pushing data to the client, WebSockets
is a full-duplex connection so the client can also push data to the server
as shown in the diagram below.

<img src="/img/websockets-flow-with-client-push.png" width="100%" alt="WebSockets also allow client push in addition to server pushed updates." class="technical-diagram" />

The WebSockets approach for server- and client-pushed updates works well for 
certain categories of web applications such as chat room, which is why that's 
often an example application for a WebSocket library.


## Implementing WebSockets
Both the web browser and the server must implement the WebSockets protocol
to establish and maintain the connection. There are important implications for 
servers since WebSockets connections are long lived, unlike typical HTTP 
connections. 

A multi-threaded or multi-process based server cannot scale appropriately for
WebSockets because it is designed to open a connection, handle a request as 
quickly as possible and then close the connection. An asynchronous server such 
as [Tornado](http://www.tornadoweb.org/en/stable/) or 
[Green Unicorn](http://gunicorn.org/) monkey patched with 
[gevent](http://www.gevent.org/) is necessary for any practical WebSockets 
server-side implementation.

On the client side, it is not necessary to use a JavaScript library for 
WebSockets. Web browsers that implement WebSockets will expose all necessary
client-side functionality through the 
[WebSockets object](http://www.w3.org/TR/2011/WD-websockets-20110419/). 

However, a JavaScript wrapper library can make a developer's life easier by 
implementing graceful degradation (often falling back to long-polling when 
WebSockets are not supported) and by providing a wrapper around 
browser-specific WebSocket quirks. Examples of JavaScript client libraries 
and Python implementations are found below.


## JavaScript client libraries
* [Socket.io](http://socket.io/)'s client side JavaScript library can be 
  used to connect to a server side WebSockets implementation.

* [web-socket-js](https://github.com/gimite/web-socket-js) is a Flash-based
  client-side WebSockets implementation.


## Python implementations
* [Autobahn](http://autobahn.ws/python/) uses Twisted or asyncio to implement
  the WebSockets protocol.

* [Crossbar.io](http://crossbar.io/) builds upon Autobahn and includes a
  separate server for handling the WebSockets connections if desired by
  the web app developer.


## Nginx WebSocket proxying
Nginx officially supports WebSocket proxying as of 
[version 1.3](http://nginx.com/blog/websocket-nginx/). However, you have
to configure the Upgrade and Connection headers to ensure requests are
passed through Nginx to your WSGI server. It can be tricky to set this up
the first time. 

Here are the configuration settings I use in my Nginx file as part of my
WebSockets proxy.

    # this is where my WSGI server sits answering only on localhost
    # usually this is Gunicorn monkey patched with gevent
    upstream app_server_wsgiapp {
      server localhost:5000 fail_timeout=0;
    }

    server {

      # typical web server configuration goes here

      # this section is specific to the WebSockets proxying
      location /socket.io {
        proxy_pass http://app_server_wsgiapp/socket.io;
        proxy_redirect off;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 600;
      }
    }

Note if you run into any issues with the above example configuration
you'll want to scope out the 
[official HTTP proxy module documentation](http://nginx.org/en/docs/http/ngx_http_proxy_module.html).

The following resources are also helpful for setting up the configuration 
properly.

* Nginx has [an official page for WebSocket proxying](http://nginx.org/en/docs/http/websocket.html).

* [WebSockets in Nginx](http://blog.martinfjordvald.com/2013/02/websockets-in-nginx/)
  walks through the Nginx WebSockets configuration directives.

* [Proxying WebSockets with Nginx](https://chrislea.com/2013/02/23/proxying-websockets-with-nginx/)
  shows how to proxy with Socket.io.


## Open source Python examples with WebSockets
* The 
  [python-websockets-example](https://github.com/makaimc/python-websockets-example)
  contains code to create a simple web application that provides WebSockets
  using Flask, Flask-SocketIO and gevent.


* The Flask-SocketIO project has a 
  [chat web application](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example) 
  that demos sending server generated events as well as input from users
  via a text box input on a form.


## General WebSockets resources
* The official W3C 
  [candidate draft for WebSockets API](http://www.w3.org/TR/websockets/) 
  and the 
  [working draft for WebSockets](http://dev.w3.org/html5/websockets/) are 
  good reference material but can be tough for those new to the WebSockets
  concepts. I recommend reading the working draft after looking through some
  of the more beginner-friendly resources list below.

* [WebSockets 101](http://lucumr.pocoo.org/2012/9/24/websockets-101/) by
  Armin Ronacher provides a detailed assessment of the subpar state of HTTP
  proxying in regards to WebSockets. He also discusses the complexities of
  the WebSockets protocol including the packet implementation.

* The "Can I Use?" website has a 
  [handy WebSockets reference chart](http://caniuse.com/#feat=websockets) 
  for which web browsers and specific versions support WebSockets.

* Mozilla's 
  [Developer Resources for WebSockets](https://developer.mozilla.org/en-US/docs/WebSockets)
  is a good place to find documentation and tools for developing with 
  WebSockets.

* [WebSockets from Scratch](https://blog.pusher.com/websockets-from-scratch/) 
  gives a nice overview of the protocol then shows how the lower-level pieces
  work with WebSockets, which are often a black box to developers who only
  use libraries like Socket.IO.

* [websocketd](http://websocketd.com/) is a WebSockets server aiming to be
  the "CGI of WebSockets". Worth a look.


## Python-specific WebSockets resources
* The 
  "[Async Python Web Apps with WebSockets & gevent](https://youtu.be/L5YQbNrFfyw)"
  talk I gave at San Francisco Python in January 2015 is a live-coded example
  Flask web app implementation that allows the audience to interact with
  WebSockets as I built out the application.

* [Real-time in Python](http://mrjoes.github.io/2013/06/21/python-realtime.html)
  provides Python-specific context for how the server push updates were 
  implemented in the past and how Python's tools have evolved to perform
  server side updates.

* [websockets](https://github.com/aaugustin/websockets) is a WebSockets 
  implementation for Python 3.3+ written with the 
  [asyncio](https://docs.python.org/3.4/library/asyncio.html) module (or with 
  [Tulip](https://code.google.com/p/tulip/) if you're working with 
  Python 3.3).

* The [Choose Your Own Adventure Presentations](https://www.twilio.com/blog/2014/11/choose-your-own-adventure-presentations-with-reveal-js-python-and-websockets.html)
  tutorial uses WebSockets via gevent on the server and socketio.js for 
  pushing vote count updates from the server to the client. 

* [Adding Real Time to Django Applications](http://crossbar.io/docs/Adding-Real-Time-to-Django-Applications/)
  shows how to use Django and Crossbar.io to implement a publish/subscribe
  feature in the application.

* [Async with Bottle](http://bottlepy.org/docs/dev/async.html) shows how to
  use greenlets to support WebSockets with the Bottle web framework.

* If you're deploying to Heroku, there is a 
  [specific WebSockets guide](https://devcenter.heroku.com/articles/python-websockets)
  for getting your Python application up and running.

* The 
  [Reddit thread for this page](http://www.reddit.com/r/Python/comments/2ujqd7/an_overview_of_using_websockets_in_python/)
  has some interesting comments on what's missing from the above content that
  I'm working to address.

* [Creating Websockets Chat with Python](http://pawelmhm.github.io/python/websockets/2016/01/02/playing-with-websockets.html)
  shows code for a Twisted server that handles WebSockets connections
  on the server side along with the JavaScript code for the client side.

* [Synchronize clients of a Flask application with WebSockets](http://www.matthieuamiguet.ch/blog/synchronize-clients-flask-application-websockets)
  is a quick tutorial showing how to use Flask, the Flask-SocketIO extension 
  and Socket.IO to update values between web browser clients when changes
  occur.

* [Can WebSockets and HTTP/2 Co-exist?](http://www.infoq.com/articles/websocket-and-http2-coexist)
  compares and contrasts the two protocols and shows how they have 
  differences which will likely lead to WebSockets sticking around for
  awhile longer.

