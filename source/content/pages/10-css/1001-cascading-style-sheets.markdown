title: Cascading Style Sheets
category: page
slug: cascading-style-sheets
sort-order: 10


# Cascading Style Sheets (CSS)
A Cascading Style Sheet (CSS) files contain rules for how to display and 
lay out the HTML content when it is rendered by a web browser.

## Why is CSS necessary?
CSS separates content contained in the HTML file from how the content 
should be displayed. That separation between content and how to display it 
enables devices to render the content differently based on factors such as
screen size. For example, a mobile device does not have as much space to
display a navigation bar on the side of a page so it is often pushed down 
below the main content. The 
[Bootstrap Blog example](http://getbootstrap.com/examples/blog/) 
shows that scenario when you resize the browser width.


## How is CSS retrieved from the web server?
The HTML file sent by the web server contains a reference to the CSS file(s)
needed to render the content. The web browser requests the CSS file after the
HTML file as shown below in a screenshot captured of the Chrome Web Developer 
Tools network traffic.

<img src="theme/img/css-chrome-dev-tools.jpg" width="100%" alt="Google Chrome Web Developer Tools shows how CSS is separate from the HTML content." class="technical-diagram" />

That request for the fsp.css file is made because the HTML file for Full 
Stack Python contains a reference to ``theme/css/fsp.css`` which is shown
in the view source screenshot below.

<img src="theme/img/fsp-css-source.jpg" width="100%" alt="View source screenshot for the fsp.css file in index.html." class="technical-diagram" />


## Responsive design
Responsive design is an approach for creating CSS that lays out content 
differently based on screen attributes. The responsiveness is accomplished 
by implementing
[media queries](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Media_queries)
in the CSS. 


## CSS preprocessors
* [SASS](http://sass-lang.com/)

* [LESS](http://lesscss.org/)


## CSS frameworks
CSS frameworks provide structure and a boilerplate base for building a
web application's design.

* [Bootstrap](http://getbootstrap.com/)

* [Foundation](http://foundation.zurb.com/)

* [Gumby](http://gumbyframework.com/)

* [Skeleton](http://www.getskeleton.com/)

* [HTML5 Boilerplate](http://html5boilerplate.com/)


## Design resources
* The [Bootstrapping Design](http://bootstrappingdesign.com/) book is one of 
  the clearest and concise resources for learning design that I've ever read. 
  Highly recommended especially if you feel you have no design skills but 
  need to learn them.


## CSS resources
* [Mozilla Developer Network's CSS page](https://developer.mozilla.org/en-US/docs/Web/CSS)
  contains an extensive set of resources, tutorials and demos for learning
  CSS.

* [CSS Positioning 101](http://alistapart.com/article/css-positioning-101)
  is a detailed guide for learning how to do element positioning correctly
  with CSS.


