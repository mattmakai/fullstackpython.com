title: Cascading Style Sheets (CSS)
category: page
slug: cascading-style-sheets
sortorder: 0417
toc: False
sidebartitle: Cascading Style Sheets (CSS)
meta: Learn how to use Cascading Style Sheets (CSS) to create your web application's user interface design on Full Stack Python.


Cascading Style Sheet (CSS) files contain rules for how to display and 
lay out the HTML content when it is rendered by a web browser.

<img src="/img/logos/css.jpg" width="100%" alt="CSS3 logo." class="shot">


## Why is CSS necessary?
CSS separates the content contained in HTML files from how the content 
should be displayed. It is important to separate the content from the rules
for how it should be rendered primarily because it is easier to reuse those
rules across many pages. CSS files are also much easier to maintain on large
projects than styles embedded within the HTML files.


## How is CSS retrieved from a web server?
The HTML file sent by the web server contains a reference to the CSS file(s)
needed to render the content. The web browser requests the CSS file after the
HTML file as shown below in a screenshot captured of the Chrome Web Developer 
Tools network traffic.

<img src="/img/visuals/css-chrome-dev-tools.jpg" width="100%" alt="Google Chrome Web Developer Tools shows how CSS is separate from the HTML content." class="shot rnd outl">

That request for the fsp.css file is made because the HTML file for Full 
Stack Python contains a reference to ``theme/css/fsp.css`` which is shown
in the view source screenshot below.

<img src="/img/visuals/fsp-css-source.jpg" width="100%" alt="View source screenshot for the fsp.css file in index.html." class="shot rnd outl" />


## CSS preprocessors
A CSS preprocessor compiles a processed language into plain CSS code. CSS 
preprocessing languages add syntax such as variables, mixins and functions
to reduce code duplication. The additional syntax also makes it possible for
designers to use these basic programming constructs to write maintainable
front end code.

* [Sass](http://sass-lang.com/) is currently the favored preprocessor in
  the design community. Sass is considered the most powerful CSS preprocessor
  in terms of advanced language features.

* [LESS](http://lesscss.org/) is right up there with Sass and has an ace up
  its sleeve in that the [Bootstrap Framework](http://getbootstrap.com/) is
  written in LESS which brings up its popularity.

* [Stylus](http://learnboost.github.io/stylus/) is often cited as the third
  most popular CSS preprocessing language.


### CSS preprocessor resources
* The Advanced Guide to HTML and CSS book has a well-written chapter on 
  [preprocessors](http://learn.shayhowe.com/advanced-html-css/preprocessors).

* [Sass vs LESS](http://css-tricks.com/sass-vs-less/) provides a short answer
  on which framework to use then a longer more detailed response for those
  interested in understanding the details.

* [How to choose the right CSS preprocessor](http://blog.teamtreehouse.com/how-to-choose-the-right-css-preprocessor)
  has a comparison of Sass, LESS and Stylus.

* [Musings on CSS preprocessors](http://css-tricks.com/musings-on-preprocessing/)
  contains helpful advice ranging from how to work with preprocessors in a
  team environment to what apps you can use to aid your workflow.


## CSS libraries and frameworks
CSS frameworks provide structure and a boilerplate base for building a
web application's design.

* [Bootstrap](http://getbootstrap.com/)

* [Foundation](http://foundation.zurb.com/)

* [Gumby](http://gumbyframework.com/)

* [Compass](http://compass-style.org/)

* [Profound Grid](http://www.profoundgrid.com/)

* [Skeleton](http://www.getskeleton.com/)

* [HTML5 Boilerplate](http://html5boilerplate.com/)

* [Spectre](https://picturepan2.github.io/spectre/)


## CSS resources
* [The languages which were almost CSS](https://eager.io/blog/the-languages-which-almost-were-css/) 
  contains the history of what might have been if other styling
  proposals were adopted instead of CSS, such as RRP, PWP, FOSI, DSSSL, 
  PSL96 and CHSS. Many of those proposals came before CSS was first published
  as a specification in 1996 so the article is a wonderful view into the
  Web in its infancy.

* [Frontend Development Bookmarks](https://github.com/dypsilon/frontend-dev-bookmarks)
  is one of the largest collections of valuable resources for frontend
  learning both in CSS as well as JavaScript.

* This series on how CSS works including
  [How CSS works: Parsing & painting CSS in the critical rendering path](https://blog.logrocket.com/how-css-works-parsing-painting-css-in-the-critical-rendering-path-b3ee290762d3)
  and 
  [How CSS works: Understanding the cascade](https://blog.logrocket.com/how-css-works-understanding-the-cascade-d181cd89a4d8)
  examines the rendering methods browsers use to display web pages along
  with details of the algorithms they use to cascade style rules.

* [CSS Reference](https://cssreference.io/) provides much-needed visual 
  examples for every CSS property to show you what they are actually going 
  to look like on your pagee when you use them.

* [CSS coding techniques](https://hacks.mozilla.org/2016/05/css-coding-techniques/)
  provides advice on how to write simpler, easier-to-maintain CSS code
  to reduce your need to rely on CSS preprocessors and build pipelines.

* [CSS refresher notes](https://github.com/vasanthk/css-refresher-notes) is
  incredibly helpful if you've learned CSS in bits and pieces along the way
  and you now want to fill in the gaps in your knowledge.

* [Mozilla Developer Network's CSS page](https://developer.mozilla.org/en-US/docs/Web/CSS)
  contains an extensive set of resources, tutorials and demos for learning
  CSS.

* [CSS Positioning 101](http://alistapart.com/article/css-positioning-101)
  is a detailed guide for learning how to do element positioning correctly
  with CSS.

* [Did CSS get more complicated since the late nineties?](https://hiddedevries.nl/en/blog/2017-07-03-did-css-get-more-complicated-since-the-late-nineties)
  is a solid look back at how CSS evolved and where it has ended up today
  compared to its origins.

* [Using feature queries in CSS](https://hacks.mozilla.org/2016/08/using-feature-queries-in-css/)
  covers the `@supports` rule and how to use it in your stylesheets.

* [Learn CSS layout](http://learnlayout.com/toc.html) is a simple guide that
  breaks CSS layout topics into chapters so you can learn each part one
  at a time.

* [How well do you know CSS display?](https://www.chenhuijing.com/blog/how-well-do-you-know-display/)
  zooms into a single CSS property, `display`, to teach the reader about it
  in-depth.

* [Google's Web Fundamentals class](https://developers.google.com/web/fundamentals/)
  shows how to create responsive designs and performant websites.

* [Tailoring CSS for performance](http://programming.oreilly.com/2014/04/tailoring-css-for-performance.html)
  is an interesting read since many developers do not consider the 
  implications of CSS complexity in browser rendering time.

* [Can I Use...](http://caniuse.com/) is a compatibility table that shows
  which versions of browsers implement specific CSS features.

* [How do you remove unused CSS from a site?](https://css-tricks.com/how-do-you-remove-unused-css-from-a-site/)
  covers tools for identifying unnecessary CSS and the process for eliminating
  rules that are overwritten by other rules and therefore do not need to
  be sent to the client.

* The [Web Design Museum](https://www.webdesignmuseum.org/) is an amazing
  look back at how web design has evolved over the past 25+ years. Some of 
  the designs can still be seen in their current site's presentation such
  as the top navigation of Apple's 2001 site.

* [The invisible parts of CSS](https://www.madebymike.com.au/writing/the-invisible-parts-of-css/)
  asks the question "can you describe what the `display:block` property
  and value do? Most developers would have some sense of what it is for
  but could not explain it to someone else beyond that. The article helps
  fix this situation with `display` as well as other less visible properties
  such as floats and `auto` width.

* [A brief history of CSS until 2016](https://www.w3.org/Style/CSS20/history.html)
  explains how CSS originated at CERN in 1994 as a solution to the
  problem of HTML not having reasonable styling features
  (in-line `style` attributes on elements don't count).

* [Old CSS, New CSS](https://eev.ee/blog/2020/02/01/old-css-new-css/) tells
  the wonderful and painful story of web design in the early days of the
  Web, when inline styling was required, HTML CAPS were mandatory, and
  most websites wished they had design styles like the amazing
  [Space Jam](https://www.spacejam.com/) pages. Oh also, lots and lots of
  talk about tables, because that was the only way to position anything
  back in the day.

* [30 seconds of CSS](https://30-seconds.github.io/30-seconds-of-css/)
  provides short useful code snippets for you to learn from and use for
  building your own web applications.

* [CSS: The bad bits](https://www.joeforshaw.com/blog/css-the-bad-bits-and-how-to-avoid-them)
  examines global scope, implicit percentage styling rules and the z-index
  which can be difficult to use and require some restraint to ensure they
  do not cause issues for the rest of your stylesheet rules as you create
  and maintain your frontend.

* [Improving Your CSS with Parker](https://csswizardry.com/2016/06/improving-your-css-with-parker/)
  shows how to use the static CSS analysis tool 
  [Parker](https://github.com/katiefenn/parker/) to improve your stylesheets.

* [CSS and network performance](https://csswizardry.com/2018/11/css-and-network-performance/)
  analyzes how splitting your CSS can affect browser render times and how
  you can improve your site loading performance by changing how you
  structure your CSS files. My recommendation: there's a lot you can do
  with these techniques but it is probably a better idea to make your CSS
  simpler and cut down the massive bloat that can accumulate as you build
  your site as a first step to improving your performance.

* [A Guide To CSS Support In Browsers](https://www.smashingmagazine.com/2019/02/css-browser-support/)
  analyzes features versus bugs in different browser versions and how
  to test for support so that issues are less likely to hit your web app.

* [That Time I Tried Browsing the Web Without CSS](https://css-tricks.com/that-time-i-tried-browsing-the-web-without-css/)
  is an enlightening look at how crucial CSS is to the modern web. You can
  view examples of what it is like to use Amazon, DuckDuckGo, GitHub
  and several other sites.

* [Third party CSS is not safe](https://jakearchibald.com/2018/third-party-css-is-not-safe/)
  is a good reminder that any code you did not write yourself, especially
  code served through 3rd party sources not under your control can contain
  potentially malicious applications, such as the experimental CSS keylogger
  hack that made the rounds in early 2018.

* [Understanding specificity in CSS](https://alligator.io/css/understanding-specificity-in-css/)
  provides some wonderful detail on the various ways to select elements
  via CSS selectors, including type selectors, pseudo-elements, class 
  selectors, attribute selectors and ID selectors.

* [Realistic Water Effect without JavaScript - HTML/CSS Only](https://www.youtube.com/watch?v=q-i0rZBZvBk)
  is one of the coolest tutorials I have seen that uses CSS to create
  a water effect over an image. This video provides an example of how
  there are so many incredible ways to use CSS and web development  
  technologies.


## CSS learning checklist
1. Create a simple HTML file with basic elements in it. Use the
   ``python -m SimpleHTTPServer`` command to serve it up. Create a 
   ``<style></style>`` element within the ``<head>`` section in the HTML
   markup. Play with CSS within that style element to change the look and 
   feel of the page.

1. Check out front end frameworks such as Bootstrap and Foundation and integrate
   one of those into the HTML page.

1. Work through the framework's grid system, styling options and customization
   so you get comfortable with how to use the framework.

1. Apply the framework to your web application and tweak the design until you
   have something that looks much better than generic HTML.

