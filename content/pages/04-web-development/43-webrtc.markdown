title: WebRTC
category: page
slug: webrtc
sortorder: 0443
toc: False
sidebartitle: WebRTC
meta: Web Real-Time Communications (WebRTC) is a protocol for web apps to transmit video, audio and data streams between client and server.


[Web Real-Time Communications (WebRTC)](https://tools.ietf.org/html/rfc7478) 
is a specification for a protocol implementation that enables web apps to 
transmit video, audio and data streams between client (typically a web
browser) and server (usually a [web server](/web-servers.html)).


### WebRTC tutorials
* [How to Get Started Learning WebRTC Development](https://bloggeek.me/started-learning-webrtc-development/)
  explains what you do and do not need to know as prerequisites for
  building with WebRTC along with some sources for learning.

* This post titled 
  [WebRTC: a working example](http://pfertyk.me/2020/03/webrtc-a-working-example/)
  and the
  [companion open source repository](https://github.com/pfertyk/webrtc-working-example)
  provides a simple working example of WebRTC technology, without any 3rd party 
  dependencies. It allows 2 web browsers to exchange audio and video streams by
  using the `aiohttp` and `python-socketio` modules.

* [A real world guide to WebRTC](https://deepstream.io/tutorials/webrtc/webrtc-intro/)
  goes through WebRTC fundamentals such as data channels, audio and video,
  screen sharing and file transfers with the JavaScript code provided
  for each concept.

* The 
  [Introduction to WebRTC video series](https://www.youtube.com/watch?v=ujpIAWmK2Vo)
  ([part 2](https://www.youtube.com/watch?v=cw2iTgIW-uk) and 
  [part 3](https://www.youtube.com/watch?v=ZeO6HgzF1jY)) can be a bit dry
  at points but overall has a ton of good information that gives a solid
  overview of the technology.

* [Building a Snapchat-like app with WebRTC in the browser](https://tokbox.com/blog/building-a-snapchat-like-app-with-webrtc-in-the-browser/)
  walks through the front end JavaScript for building a photo filter
  application using the WebRTC browser APIs.

* [WebRTC issues and how to debug them](https://blog.codeship.com/webrtc-issues-and-how-to-debug-them/)
  explains the various ways that implementations can go wrong and where
  to start looking when you run into errors.


### Other WebRTC resources
* [A Study of WebRTC Security](https://webrtc-security.github.io/) gives a
  great overview of WebRTC and the new security concerns it can bring as it
  is integrated into more web applications.

* [How Discord Handles Two and Half Million Concurrent Voice Users using WebRTC](https://blog.discordapp.com/how-discord-handles-two-and-half-million-concurrent-voice-users-using-webrtc-ce01c3187429)
  provides detailed insight into the what and why of the highly scalable
  [Discord](https://discordapp.com/) technical architecture that relies
  upon WebRTC for communication. There are a bunch of great examples here
  for why some of the service must be centralized (to prevent client IP 
  addresses from leaking to other clients) while others are decentralized
  to assist with scaling the number of possible connections.

* [Architectures for a kickass WebRTC application](https://www.youtube.com/watch?v=m9QxBc0OeoI)
  is a video of a technical talk that covers some of the tools and protocols 
  that can be used to create your WebRTC projects and why you would choose 
  one tool other another.

* [WebRTC connection times and the power of playing around with data](https://medium.com/the-making-of-appear-in/webrtc-connection-times-and-the-power-of-playing-around-with-data-ab11312737e9)
  provides data on connection times and potential reasons for WebRTC 
  connection quality suffers in some cases.

* [A closer look into WebRTC](https://webkit.org/blog/7763/a-closer-look-into-webrtc/)
  covers the Safari WebRTC implementation in WebKit and explains some of the
  nuances for that specific web browser's implementation.

* STUN/TURN servers are used to relay data to a non-public IP address in a
  WebRTC application. This blog post on
  [Do you still need TURN if your media server has a public IP address?](https://bloggeek.me/turn-public-ip-address/)
  answers some frequently asked questions about when a TURN server is
  truly required.

* [An Intro to WebRTC and Accessing a User’s Media Devices](https://medium.com/@sebastianpatron/an-intro-to-webrtc-and-accessing-a-users-media-devices-76ca2e2edc73)
  goes into the JavaScript needed to use a computer's media devices such as
  the microphone and video camera through the web browser's APIs.

* [AIORTC: An Asynchronous WebRTC Framework](https://www.podcastinit.com/aiortc-with-jeremy-laine-episode-191/)
  is an interview with the developer of an async WebRTC framework that is
  built upon asyncio.
