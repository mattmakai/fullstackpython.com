title: Web Development
category: page
slug: web-development
sortorder: 0400
toc: True
sidebartitle: 4. Web Development
meta: Web development is the catch-all term for activities involved with websites and web apps. Learn more on Full Stack Python.


# Web Development
Web development is the umbrella term for conceptualizing, creating, 
[deploying](/deployment.html) and operating web applications and 
[application programming interfaces](/application-programming-interfaces.html)
for the Web.


## Why is web development important?
The Web has grown a mindboggling amount in the number of sites, users and
implementation capabilities since the 
[first website](http://info.cern.ch/hypertext/WWW/TheProject.html) went live
in [1989](http://home.cern/topics/birth-web). Web development is the concept
that encompasses all the activities involved with websites and web 
applications.

## How does Python fit into web development?
Python can be used to build server-side web applications. While a
[web framework](/web-frameworks.html) is not required to build web apps,
it's rare that developers would not use existing open source libraries to
speed up their progress in getting their application working.

Python is not used in a web browser. The language executed in browsers
such as Chrome, Firefox and Internet Explorer is 
[JavaScript](/javascript.html). Projects such as [pyjs](http://pyjs.org/) 
can compile from Python to JavaScript. However, most Python developers 
write their web applications using a combination of Python and JavaScript.
Python is executed on the server side while JavaScript is downloaded to
the client and run by the web browser.


### Web development resources
To become an experienced web developer you need to know the foundation
principles that the web is built with, such as HTTP requests and responses,
client (typically web browsers) and server ([web servers](/web-servers.html) 
such as [Nginx](/nginx.html) and [Apache](/apache-http-server.html) 
architectures, [HTML](/hypertext-markup-language-html.html), 
[CSS](/cascading-style-sheets.html) and [JavaScript](/javascript.html), among
many other topics. The following resources provide a range of perspectives
and when combined together should get you oriented in the web development
world.

* If you want to be a web developer it's important to know the foundational
  tools used to build websites and web applications. It is also important to
  understand that the core concepts such as 
  HTTP, URLs and [HTML](/hypertext-markup-language-html.html) were all there
  at the beginning and then were expanded with new specifications over time.
  This article on the
  [History of the Web](https://webfoundation.org/about/vision/history-of-the-web/)
  succinctly explains the origins of the web starting from Tim Berners-Lee's
  origin vision and release at CERN.

* The [Evolution of the Web](http://www.evolutionoftheweb.com/) visualizes 
  how web browsers and related technologies have changed over time as well as
  the overall growth of the Internet in the amount of data transferred. Note 
  that the visualization unfortunately stops around the beginning of 2013 but
  it's a good way to explore what happened in the first 24 years.

* [Web application development is different and better](http://radar.oreilly.com/2014/01/web-application-development-is-different-and-better.html)
  provides some context for how web development has evolved from writing
  static HTML files into the complex JavaScript client-side applications
  produced today.

* [The Browser Hacker's Guide to Instantly Loading Everything](https://www.youtube.com/watch?v=7vUs5yOuv-o)
  is a spectacular technical talk given by Addy Osmani at JSConf EU 2017
  that has great bits of developer knowledge for both beginner and 
  experienced web developers alike.

* [Build a web application from scratch](https://defn.io/2018/02/25/web-app-from-scratch-01/)
  and its follow on posts for 
  [request handling](https://defn.io/2018/03/04/web-app-from-scratch-02/)
  [middleware](https://defn.io/2018/03/20/web-app-from-scratch-03/) explores
  the fundamentals of web development. Learning these foundational concepts
  is critical for a web developer even though you should still plan to use an
  established [web framework](/web-frameworks.html) such as 
  [Django](/django.html) or [Flask](/flask.html) to build real-world 
  applications. The 
  [open source code](https://github.com/Bogdanp/web-app-from-scratch) 
  for these posts is available on GitHub.

* While not Python-specific, Mozilla put together a 
  [Learning the Web](https://developer.mozilla.org/en-US/Learn) tutorial
  for beginners and intermediate web users who want to build websites.
  It's worth a look for general web development learning.

* Web development involves HTTP communication between the server, hosting
  a website or web application, and the client, a web browser. Knowing
  how web browsers works is important as a developer, so take a look at
  this article on 
  [what's in a web browser](https://medium.com/@camaelon/what-s-in-a-web-browser-83793b51df6c).

* [Ping at the speed of light](http://blog.wesleyac.com/posts/ping-lightspeed)
  dives into the computer networking weeds with how fast packets travel through
  the internet plumbing. The author created a 
  [Python script that scrapes network speeds](https://github.com/WesleyAC/toybox/blob/42262bf81ac226ca83addea2c340017f8ea0e60f/misc/scrape_network_speeds.py)
  from disparate locations to see what the network speed is in fiber optic
  cables as a percentage of the speed of light.

* [Three takeaways for web developers after two weeks of painfully slow Internet](https://medium.com/@zengabor/three-takeaways-for-web-developers-after-two-weeks-of-painfully-slow-internet-9e7f6d47726e)
  is a must-read for every web developer. Not everyone has fast Internet
  service, whether because they are in a remote part of the world or they're
  just in a subway tunnel. Optimizing sites so they work in those situations
  is important for keeping your users happy.
