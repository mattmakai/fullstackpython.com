title: Web Frameworks
category: page
slug: web-frameworks
sortorder: 0402
toc: False
sidebartitle: Web Frameworks
meta: Find out about Python web frameworks, which are code libraries that solve common web application creation challenges.


# Web frameworks
A web framework is a code library that makes a developer's life easier when 
building reliable, scalable and maintainable web applications.


## Why are web frameworks necessary?
Web frameworks encapsulate what developers have learned over the past twenty
years while programming sites and applications for the web. Frameworks make 
it easier to reuse code for common HTTP operations and to structure projects 
so other developers with knowledge of the framework can quickly build and
maintain the application.


## Common web framework functionality
Frameworks provide functionality in their code or through extensions to 
perform common operations required to run web applications. These common 
operations include:

1. URL routing
2. HTML, XML, JSON, and other output format templating
3. Database manipulation
4. Security against Cross-site request forgery (CSRF) and other attacks
5. Session storage and retrieval

Not all web frameworks include code for all of the above functionality. 
Frameworks fall on the spectrum from executing a single use case to providing 
every known web framework feature to every developer. Some frameworks take 
the "batteries-included" approach where everything possible comes bundled 
with the framework while others have a minimal core package that is amenable
to extensions provided by other packages.

For example, the [Django web application framework](/django.html) includes an 
Object-Relational Mapping (ORM) layer that abstracts relational database 
read, write, query, and delete operations. However, Django's ORM
cannot work without significant modification on non-relational databases 
such as [MongoDB](http://www.mongodb.org/).

Some other web frameworks such as [Flask](/flask.html) and 
[Pyramid](/pyramid.html) are easier to
use with non-relational databases by incorporating external Python libraries.
There is a spectrum between minimal functionality with easy extensibility on
one end and including everything in the framework with tight integration on
the other end.

## Comparing web frameworks
Are you curious about how the code in a Django project is structured compared 
with Flask? Check out 
[this Django web application tutorial](https://www.twilio.com/docs/howto/walkthrough/appointment-reminders/python/django) 
and then view [the same application built with Flask](https://www.twilio.com/docs/howto/walkthrough/appointment-reminders/python/flask).

There is also a repository called
[compare-python-web-frameworks](https://github.com/makaimc/compare-python-web-frameworks)
where the same web application is being coded with varying Python web 
frameworks, templating engines and 
[object-relational mappers](/object-relational-mappers-orms.html).


<div class="well see-also">While you're learning about web frameworks you should also study <a href="/deployment.html">web application deployment</a> and <a href="/application-programming-interfaces.html">web APIs</a>.</div>


## Do I have to use a web framework?
Whether or not you use a web framework in your project depends on your 
experience with web development and what you're trying to accomplish. If you 
are a beginner programmer and just want to work on a web application as a 
learning project then a framework can help you understand the concepts listed
above, such as URL routing, data manipulation and authentication that are
common to the majority of web applications.

On the other hand if you're an experienced programmer with significant 
web development experience you may feel like the existing frameworks do not
match your project's requirements. In that case, you can mix and match
open source libraries such as [Werkzeug](http://werkzeug.pocoo.org/) for
WSGI plumbing with your own code to create your own framework. There's 
still plenty of room in the Python ecosystem for new frameworks to satisfy 
the needs of web developers that are unmet by [Django](/django.html), 
[Flask](/flask.html), [Pyramid](/pyramid.html), [Bottle](/bottle.html) and 
[many others](/other-web-frameworks.html).

In short, whether or not you need to use a web framework to build a web 
application depends on your experience and what you're trying to accomplish. 
Using a web framework to build a web application certainly isn't required, 
but it'll make most developers' lives easier in many cases.


## Web framework resources
* "[What is a web framework?](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)"
  is an in-depth explanation of what web frameworks are and their relation
  to web servers.

* Check out the answer to the 
  "[What is a web framework and how does it compare to LAMP?](http://stackoverflow.com/questions/4507506/what-is-a-web-framework-how-does-it-compare-with-lamp)"
  question on Stack Overflow.

* [Frameworks](http://youtu.be/W6KCPXl6Zuc) is a really well done short video
  that explains how to choose between web frameworks. The author has some
  particular opinions about what should be in a framework. For the most part
  I agree although I've found sessions and database ORMs to be a helpful
  part of a framework when done well.

* [Django vs Flask vs Pyramid: Choosing a Python Web Framework](https://www.airpair.com/python/posts/django-flask-pyramid)
  contains background information and code comparisons for similar
  web applications built in these three big Python frameworks.

* This [Python web framework roundup](http://www.konstruktor.ee/blog/python-web-framework-roundup/)
  covers Django, Flask and Bottle as well as several other lesser known Python
  frameworks.

* This fascinating blog post takes a look at the 
  [code complexity of several Python web frameworks](http://grokcode.com/864/snakefooding-python-code-for-complexity-visualization/)
  by providing visualizations based on their code bases.

* [Python's web frameworks benchmarks](http://klen.github.io/py-frameworks-bench/)
  is a test of the responsiveness of a framework with encoding an object to
  JSON and returning it as a response as well as retrieving data from the 
  database and rendering it in a template. There were no conclusive results
  but the output is fun to read about nonetheless.

* [What web frameworks do you use and why are they awesome?](http://www.reddit.com/r/webdev/comments/2les4x/what_frameworks_do_you_use_and_why_are_they/)
  is a language agnostic Reddit discussion on web frameworks. It's interesting
  to see what programmers in other languages like and dislike about their
  suite of web frameworks compared to the main Python frameworks.

* This user-voted question & answer site asked "[What are the best general purpose Python web frameworks usable in production?](http://www.slant.co/topics/426/~what-are-the-best-general-purpose-python-web-frameworks-usable-in-production-sites)".
  The votes aren't as important as the list of the many frameworks
  that are available to Python developers.


## Web frameworks learning checklist
1. Choose a major Python web framework ([Django](/django.html) or 
   [Flask](/flask.html) are recommended) and stick with it. When you're just
   starting it's best to learn one framework first instead of bouncing around
   trying to understand every framework. 

1. Work through a detailed tutorial found within the resources links on the
   framework's page.

1. Study open source examples built with your framework of choice so you can 
   take parts of those projects and reuse the code in your application.

1. Build the first simple iteration of your web application then go to
   the [deployment](/deployment.html) section to make it accessible on the 
   web.

