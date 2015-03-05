title: WebSockets
category: page
slug: websockets
sort-order: 0413
meta: WebSockets are a protocol for full-duplex web communications. Learn about WebSockets on Full Stack Python.
choice1url: /wsgi-servers.html
choice1icon: fa-play fa-inverse
choice1text: How do I execute Python since the web server doesn't do that?
choice2url: /application-dependencies.html
choice2icon: fa-archive fa-inverse
choice2text: How should I install Python libraries on the server?
choice3url: /development-environments.html
choice3icon: fa-desktop
choice3text: What should I use to code my Python application?
choice4url: 
choice4icon: 
choice4text: 


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

<img src="theme/img/ajax-long-polling.png" width="100%" alt="Long polling via AJAX is incredibly inefficient for some applications." class="technical-diagram" />

Server push is more efficient and scalable than long polling because the 
web browser does not have to constantly ask for updates through a stream 
of AJAX requests.

<img src="theme/img/websockets-flow.png" width="100%" alt="WebSockets are more efficient than long polling for server sent updates." class="technical-diagram" />

While the above diagram shows a server pushing data to the client, WebSockets
is a full-duplex connection so the client can also push data to the server
as shown in the diagram below.

<img src="theme/img/websockets-flow-with-client-push.png" width="100%" alt="WebSockets also allow client push in addition to server pushed updates." class="technical-diagram" />

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
and WSGI implementations are found below.


## JavaScript client libraries
* [Socket.io](http://socket.io/)'s client side JavaScript library can be 
  used to connect to a server side WebSockets implementation.

* [web-socket-js](https://github.com/gimite/web-socket-js) is a Flash-based
  client-side WebSockets implementation.


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

* [websocketd](http://websocketd.com/) is a WebSockets server aiming to be
  the "CGI of WebSockets". Worth a look.


## Python-specific WebSockets resources
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

* [Async with Bottle](http://bottlepy.org/docs/dev/async.html) shows how to
  use greenlets to support WebSockets with the Bottle web framework.

* If you're deploying to Heroku, there is a 
  [specific WebSockets guide](https://devcenter.heroku.com/articles/python-websockets)
  for getting your Python application up and running.

* The 
  [Reddit thread for this page](http://www.reddit.com/r/Python/comments/2ujqd7/an_overview_of_using_websockets_in_python/)
  has some interesting comments on what's missing from the above content that
  I'm working to address.


### What's next for your web application after setting up WebSockets?
