title: Web Frameworks
category: page
slug: web-frameworks
sort-order: 021
choice1url: /django.html
choice1icon: fa-terminal fa-inverse
choice1text: Tell me more about the Django framework.
choice2url: /flask.html
choice2icon: fa-flask
choice2text: I want to learn more about the Flask web framework.
choice3url: /bottle.html
choice3icon: fa-tint fa-inverse
choice3text: Show me more information on Bottle.
choice4url: /other-web-frameworks.html
choice4icon: fa-question fa-inverse
choice4text: What other Python web frameworks exist?


# Web frameworks
A web application framework is a code library that makes a developer's life
easier when building reliable, scalable and maintainable web applications.


## Why are web frameworks necessary?
Web frameworks encapsulate what developers have learned over the past twenty
years while building dynamic web applications. Frameworks make it easier
to reuse code for common HTTP operations and to structure your code so that 
it is maintainable.


## Common web framework functionality
Frameworks provide functionality in their code or through extensions to 
perform common operations required to run web applications. These common 
operations include:

1. URL routing
2. HTML, XML, JSON, and other output format templating
3. Database manipulation
4. Security against Cross-site request forgery (CSRF) and other attacks

Not all web frameworks include code for all of the above 
functionality. Frameworks fall somewhere between simply executing a 
single use case and attempting to be everything to every developer with
increased complexity. Some frameworks take the "batteries-included" approach 
where everything possible comes bundled with the framework while others 
have a minimal code library that plays well with extensions.

For example, the Django web application framework includes an 
Object-Relational Mapping (ORM) layer that abstracts relational database 
read, write, query, and delete operations. However, Django's ORM
cannot work without significant modification on non-relational databases such 
[MongoDB](http://www.mongodb.org/).
Some other web frameworks such as Flask and Pyramid are easier to
use with non-relational databases by incorporating external Python libraries.
There is a spectrum between minimal functionality with easy extensibility and
including everything in the framework with tight integration.


## General web framework resources
* "[What is a web framework?](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)"
  by [Jeff Knupp](https://twitter.com/jeffknupp)
  is a in-depth explanation of what a web framework is and their relation
  to web servers.

* Check out the answer to the 
  "[What is a web framework and how does it compare to LAMP?](http://stackoverflow.com/questions/4507506/what-is-a-web-framework-how-does-it-compare-with-lamp)"
  question on Stack Overflow.

* This [Python web framework roundup](http://www.konstruktor.ee/blog/python-web-framework-roundup/)
  covers Django, Flask and Bottle as well as several other lesser known Python
  frameworks.


## Web frameworks learning checklist
<i class="fa fa-check-square-o"></i> 
Choose a major Python web framework ([Django](/django.html) or 
[Flask](/flask.html) are recommended) and stick with it. When you're just
starting it's best to learn one framework first instead of bouncing around
trying to understand every framework. 

<i class="fa fa-check-square-o"></i> 
Work through a detailed tutorial found within the resources links on the
framework's page.

<i class="fa fa-check-square-o"></i> 
Study open source examples built with your framework of choice so you can 
take parts of those projects and reuse the code in your application.

<i class="fa fa-check-square-o"></i> 
Build the first simple iteration of your web application then go to
the [deployment](/deployment.html) section to make it accessible on the 
web.


### Which web framework do you want to learn about?
