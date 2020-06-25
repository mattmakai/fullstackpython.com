title: JavaScript
category: page
slug: javascript
sortorder: 0423
toc: False
sidebartitle: JavaScript
meta: Learn about JavaScript and MVC frameworks for web applications on Full Stack Python.


JavaScript is a scripting programming language interpretted by web 
browsers that enables dynamic content and interactions in web applications. 


## Why is JavaScript necessary?
JavaScript executes in the client and enables dynamic content and interaction
that is not possible with HTML and CSS alone. Every modern Python web 
application uses JavaScript on the front end. 


## Front end frameworks
Front end JavaScript frameworks move the rendering for most of a web 
application to the client side. Often these applications are informally 
referred to as "one page apps" because the webpage is not reloaded upon every
click to a new URL. Instead, partial HTML pages are loaded into the 
document object model or data is retrieved through an API call then displayed
on the existing page.

Examples of these front end frameworks include:

* [React](https://reactjs.org/)

* [Angular.js](https://angularjs.org/)

* [Vue.js](https://vuejs.org/)

* [Backbone.js](http://backbonejs.org/)

* [Ember.js](http://emberjs.com/)

Front end frameworks are rapidly evolving. Over the next several years 
consensus about good practices for using the frameworks will emerge.


## How did JavaScript originate?
JavaScript is an implementation of 
[the ECMAScript specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/JavaScript_Overview) 
which is defined by the 
[Ecma International Standards Body](http://www.ecma-international.org/default.htm).
Read this paper on 
[the first 20 years of JavaScript](https://zenodo.org/record/3710954)
by Brendan Eich, the original creator of the programming language, and 
Allen Wirfs-Brock for more context on the language's evolution.


### JavaScript resources
* [How Browsers Work](http://www.html5rocks.com/en/tutorials/internals/howbrowserswork/)
  is a great overview of both JavaScript and CSS as well as how pages are 
  rendered in a browser.

* This 
  [step-by-step tutorial to build a modern JavaScript stack](https://github.com/verekia/js-stack-from-scratch)
  is useful to understanding how front-end JS frameworks such as Angular
  and Ember.js work.

* [A re-introduction to JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)
  by Mozilla walks through the basic syntax and operators.

* [The Cost of Javascript Frameworks](https://timkadlec.com/remembers/2020-04-21-the-cost-of-javascript-frameworks/)
  presents a balanced view of how JavaScript libraries and frameworks impact
  web performance on both desktop and mobile. The author acknowledges that
  these libraries are useful for developers but in extreme cases there are 
  significant downsides to including so much JavaScript in pages.

* [The State of JavaScript report](https://stateofjs.com/) contains a wealth
  of data on what libraries developers are using in the JavaScript 
  ecosystem. There are also reports from previous years which show how the 
  community's preferences have changed over time.

* [Coding tools and JavaScript libraries](http://www.smashingmagazine.com/2011/10/28/useful-coding-workflow-tools-for-web-designers-developers/)
  is a huge list by Smashing Magazine with explanations for each tool and 
  library for working with JavaScript.

* [Superhero.js](http://superherojs.com/) is an incredibly well designed list
  of resources for how to test, organize, understand and generally work with
  JavaScript.

* [Unheap](http://www.unheap.com/) is an amazing collection of reusable JQuery 
  plugins for everything from navigation to displaying media.

* [The Modern JavaScript Developer's Toolbox](http://www.infoq.com/articles/modern-javascript-toolbox)
  provides a high-level overview of tools frequently used on the client and
  server side for developers using JavaScript in their web applications.

* [Front-end Walkthrough: Designing a Single Page Application Architecture](https://blog.poki.com/front-end-walkthrough-building-a-single-page-application-from-scratch-d47c35fdc830)
  covers what a single page app (SPA) architecture looks like, what the 
  tools are that you can use and some comparisons when deciding between 
  Angular and React.

* [Developing a Single Page App with Flask and Vue.js](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs) 
  is a step-by-step walkthrough of how to set up a basic CRUD app with 
  [Vue.js](/vuejs.html) and [Flask](/flask.html).

* [A Guide to Console Commands](https://css-tricks.com/a-guide-to-console-commands/)
  shows off what JavaScript commands you can use in your browser's console,
  which is a typical debugging pattern for JavaScript development.

* [is-website-vulnerable](https://github.com/lirantal/is-website-vulnerable)
  is an open source tool that identifies security vulnerabilities based on 
  the front end JavaScript code a web application runs.

* [SPAs are harder, and always will be](http://wgross.net/essays/spas-are-harder)
  talks about the inherent complexity in building client-side user
  interfaces with JavaScript.

* [The Deep Roots of Javascript Fatigue](https://segment.com/blog/the-deep-roots-of-js-fatigue/)
  starts by covering the non-stop library churn in the JavaScript ecosystem
  and then relates JavaScript evolution since the mid-90s to explain the
  history of the problem.

* [How JavaScript works: the rendering engine and tips to optimize its performance](https://blog.sessionstack.com/how-javascript-works-the-rendering-engine-and-tips-to-optimize-its-performance-7b95553baeda)
  is one particularly relevant post in a multi-part series that explains
  how you can optimize slower JavaScript code to better suit the JS engines
  in common web browsers.

* [How to reduce the impact of JavaScript on your page load time](https://engineering.gosquared.com/improve-javascript-page-load-time)
  provides insight into minimizing the size and improving the download
  and execution speed for JavaScript libraries, especially ones that are
  used at scale by many websites.

* [Learn JS data](http://learnjsdata.com/) teaches how to manipulate data
  using JavaScript in a browser or on the server using Node.js. 

* [A Beginner's Guide to JavaScript's Prototype](https://ui.dev/beginners-guide-to-javascript-prototype/)
  explains the fundamentals of JavaScript's object system, which is
  a prototype-based model and different from many other common
  programming languages' object models.

* [Understanding Data Types in JavaScript](https://www.digitalocean.com/community/tutorials/understanding-data-types-in-javascript)
  examines JavaScript's dynamic data type model and how it manifests
  in the way numbers, string, Booleans and arrays are used.


### JavaScript learning checklist
1. Create a simple HTML file with basic elements in it. Use the
   ``python -m SimpleHTTPServer`` command to serve it up. Create a 
   ``<script type="text/javascript"></script>`` 
   element at the end of the ``<body>`` section in the HTML page. Play
   with JavaScript within that element to learn the basic syntax.

1. Download [JQuery](http://jquery.com/) and add it to the page above your 
   JavaScript element. Start working with JQuery and learning how it makes 
   basic JavaScript easier.

1. Work with JavaScript on the page. Incorporate examples from open source 
   projects listed below as well as JQuery plugins. Check out 
   [Unheap](http://www.unheap.com/) to find a large collection of categorized 
   JQuery plugins.

1. Check out the JavaScript resources below to learn more about advanced 
   concepts and open source libraries.

1. Integrate JavaScript into your web application and check the 
   [static content](/static-content.html) section for how to host the 
   JavaScript files.

