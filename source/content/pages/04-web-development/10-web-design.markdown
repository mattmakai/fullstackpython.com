title: Web Design
category: page
slug: web-design
sort-order: 0410
meta: Web design creates a compelling user experience for your Python web app. Learn more about web design on Full Stack Python.


# Web Design
Web design is the creation of a web application's style and user interaction
using CSS and JavaScript.


## Why is web design important?
You don't really expect users to use your 2014 web application if it looks
like this, do you?

<img src="theme/img/no-style-webpage.png" width="100%" alt="HTML with no CSS or JavaScript." class="technical-diagram" /> 

Creating web pages with their own style and interactivity so users can easily
accomplish their tasks is a major part of building modern web applications.


## Responsive design
Separating the content from the rules for how to display the content allows 
devices to render the output differently based on factors such as screen size
and device type. Displaying content differently based on varying screen 
attributes is often called *responsive design*. The responsiveness is 
accomplished by implementing
[media queries](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Media_queries)
in the [CSS](/cascading-style-sheets.html). 

For example, a mobile device does not have as much space to display a 
navigation bar on the side of a page so it is often pushed down 
below the main content. The 
[Bootstrap Blog example](http://getbootstrap.com/examples/blog/) 
shows that navigation bar relocation scenario when you resize the browser 
width.


## Design resources
* The [Bootstrapping Design](http://bootstrappingdesign.com/) book is one of 
  the clearest and concise resources for learning design that I've ever read. 
  Highly recommended especially if you feel you have no design skills but 
  need to learn them.

* [Kuler](https://kuler.adobe.com/create/color-wheel/) is a complementary
  color picker by Adobe that helps choose colors for your designs.

* If you want to learn more about how browsers work behind the scenes, 
  here's a 
  [blog post series on building a browser engine](http://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
  that will show you how to build a simple rendering engine.

