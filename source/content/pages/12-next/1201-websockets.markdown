title: WebSockets
category: page
slug: websockets
sort-order: 1201
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
two-way communication between servers and clients. The WebSockets protocol does
not run over HTTP, instead it is a separate implementation on top of 
[TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol).


## Why use WebSockets?
WebSockets allow two-way communication between the client and server. 
A WebSockets-enabled application allows a web server to push data to a web 
browser without the browser having to poll for updates via HTTP. Allowing 
push from the server to the client and vice versa is much more efficient than 
having the client constantly ask the server "are there any updates?".

Previous approaches for for keeping a connection alive between client and 
server over HTTP, such as 
[Comet](http://en.wikipedia.org/wiki/Comet_(programming), have either used 
long polling or were not implemented by all browsers.


## JavaScript client libraries
* [Socket.io](http://socket.io/)'s client side JavaScript library can be 
  used to connect to a server side WebSockets implementation.

* [web-socket-js](https://github.com/gimite/web-socket-js) is a Flash-based
  client-side WebSockets implementation.


## Websockets with Nginx
Nginx officially supports WebSocket proxying as of 
[version 1.3](http://nginx.com/blog/websocket-nginx/). However, you have
to configure the Upgrade and Connection headers to ensure requests are
passed through Nginx to your WSGI server. It can be tricky to set this up
the first time. The following resources are helpful for setting up the
configuration properly.

* Nginx has [an official page for WebSocket proxying](http://nginx.org/en/docs/http/websocket.html).

* [WebSockets in Nginx](http://blog.martinfjordvald.com/2013/02/websockets-in-nginx/)
  walks through the Nginx WebSockets configuration directives.

* [Proxying WebSockets with Nginx](https://chrislea.com/2013/02/23/proxying-websockets-with-nginx/)
  shows how to proxy with Socket.io.


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


## Python-specific WebSockets resources
* [Real-time in Python](http://mrjoes.github.io/2013/06/21/python-realtime.html)
  provides Python-specific context for how the server push updates were 
  implemented in the past and how Python's tools have evolved to perform
  server side updates.

* The [Choose Your Own Adventure Presentations](https://www.twilio.com/blog/2014/11/choose-your-own-adventure-presentations-with-reveal-js-python-and-websockets.html)
  tutorial uses WebSockets via gevent on the server and socketio.js for 
  pushing vote count updates from the server to the client. 

* [Async with Bottle](http://bottlepy.org/docs/dev/async.html) shows how to
  use greenlets to support WebSockets with the Bottle web framework.

* If you're deploying to Heroku, there is a 
  [specific WebSockets guide](https://devcenter.heroku.com/articles/python-websockets)
  for getting your Python application up and running.


### What's next for your web application after setting up WebSockets?
