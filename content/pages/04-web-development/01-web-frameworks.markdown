title: Web Frameworks
category: page
slug: web-frameworks
sortorder: 0401
toc: False
sidebartitle: Web Frameworks
meta: Find out about Python web frameworks, which are code libraries that solve common web application creation challenges.


A web framework is a code library that makes 
[web development](/web-development.html) faster and easier by providing 
common patterns for building reliable, scalable and maintainable web
applications. After the early 2000s, professional web development projects
always use an existing web framework except in very unusual situations.

<img src="/img/visuals/web-frameworks.jpg" width="100%" alt="Django, Bottle, Flask, Pyramid, Falcon and Sanic logos, copyright their respective owners." class="shot rnd outl">


### Why are web frameworks useful?
Web frameworks encapsulate what developers have learned over the past twenty
years while programming sites and applications for the web. Frameworks make 
it easier to reuse code for common HTTP operations and to structure projects 
so other developers with knowledge of the framework can quickly build and
maintain the application.

<div class="well see-also">Web frameworks are a concept implemented by <a href="/django.html">Django</a>, <a href="/flask.html">Flask</a>, <a href="/bottle.html">Bottle</a>, <a href="/pyramid.html">Pyramid</a>, <a href="/morepath.html">Morepath</a>, <a href="/turbogears.html">TurboGears</a> and <a href="/other-web-frameworks.html">several other libraries</a>. Learn how the parts fit together in the <a href="/web-development.html">web development</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


### Common web framework functionality
Frameworks provide functionality in their code or through extensions to 
perform common operations required to run web applications. These common 
operations include:

1. URL routing
1. Input form handling and validation
1. [HTML](/hypertext-markup-language-html.html), XML, JSON, and other output 
   formats with a [templating engine](/template-engines.html)
1. Database connection configuration and persistent data manipulation through
   an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
1. [Web security](/web-application-security.html) against 
   Cross-site request forgery (CSRF), SQL Injection, 
   Cross-site Scripting (XSS) and other common malicious attacks
1. Session storage and retrieval

Not all web frameworks include code for all of the above functionality. 
Frameworks fall on the spectrum from executing a single use case to providing 
every known web framework feature to every developer. Some frameworks take 
the "batteries-included" approach where everything possible comes bundled 
with the framework while others have a minimal core package that is amenable
to extensions provided by other packages.

For example, the [Django web application framework](/django.html) includes
[the Django ORM](/django-orm.html) layer that allows a developer to write
[relational database](/databases.html)
read, write, query, and delete operations in Python code rather than SQL. 
However, Django's ORM cannot work without significant modification on 
[non-relational (NoSQL) databases](/no-sql-datastore.html) such as 
[MongoDB](/mongodb.html) or [Cassandra](/apache-cassandra.html).

Some other web frameworks such as [Flask](/flask.html) and 
[Pyramid](/pyramid.html) are easier to
use with non-relational databases by incorporating external Python libraries.
There is a spectrum between minimal functionality with easy extensibility on
one end and including everything in the framework with tight integration on
the other end.


### Do I have to use a web framework?
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


### Comparing web frameworks
Are you curious about how the code in a Django project is structured compared 
with Flask? Check out 
[this Django web application tutorial](https://www.twilio.com/docs/sms/tutorials/appointment-reminders-python-django)
and then view [the same application built with Flask](https://www.twilio.com/docs/sms/tutorials/appointment-reminders-python-flask).

[Talk Python to Me had a podcast episode](https://talkpython.fm/episodes/show/149/4-python-web-frameworks-compared) 
with a detailed comparison of the [Django](/django.html), 
[Flask](/flask.html), Tornado and [Pyramid](/pyramid.html) frameworks.

There is also a repository called
[compare-python-web-frameworks](https://github.com/mattmakai/compare-python-web-frameworks)
where the same web application is being coded with varying Python web 
frameworks, templating engines and 
[object-relational mappers](/object-relational-mappers-orms.html).


### Web framework resources
* [Building Your Own Python Web Framework](https://testdriven.io/courses/python-web-framework/?utm_source=fsp)
  is an awesome way to learn how the [WSGI](/wsgi-servers.html) works
  and the many other pieces that combine to make web frameworks useful
  to web developers.

* When you are learning how to use one or more web frameworks it's helpful
  to have an idea of what the code under the covers is doing. This post on
  building a 
  [simple Python framework from scratch](http://mattscodecave.com/posts/simple-python-framework-from-scratch.html)
  shows how HTTP connections, routing, and requests can work in just 
  320 lines of code. This post is awesome even though the resulting framework
  is a simplification of what frameworks such as [Django](/django.html), 
  [Flask](/flask.html) and [Pyramid](/pyramid.html) allow developers to 
  accomplish.

* There is also another, more recent multi-part tutorial about 
  building your own web framework in Python. This series is based on the
  [alcazar](https://github.com/rahmonov/alcazar) project the author is
  coding for learning purposes:

    * [Part 1: Handling requests](http://rahmonov.me/posts/write-python-framework-part-one/)
    * [Part 2: Routes, Class-Based Handlers and Unit Testing](http://rahmonov.me/posts/write-python-framework-part-two/)
    * [Part 3: Test Client and Templating Support](http://rahmonov.me/posts/write-python-framework-part-three/)
    * [Part 4: Exception Handling, Static Files and Middleware](http://rahmonov.me/posts/write-python-framework-part-four/)

* Check out the answer to the 
  "[What is a web framework and how does it compare to LAMP?](http://stackoverflow.com/questions/4507506/what-is-a-web-framework-how-does-it-compare-with-lamp)"
  question on Stack Overflow.

* Another great series that digs behind the web framework magic is
  "Web Application from Scratch". The four parts are:

    * [Part 1: handling HTTP requests and responses](https://defn.io/2018/02/25/web-app-from-scratch-01/)
    * [Part 2: abstracting Requests, Responses and Servers](https://defn.io/2018/03/04/web-app-from-scratch-02/)
    * [Part 3: request handlers and middleware](https://defn.io/2018/03/20/web-app-from-scratch-03/)
    * [Part 4: abstracting applications](https://defn.io/2018/05/12/web-app-from-scratch-04/)
   
* [Frameworks](http://youtu.be/W6KCPXl6Zuc) is a really well done short video
  that explains how to choose between web frameworks. The author has some
  particular opinions about what should be in a framework. For the most part
  I agree although I've found sessions and database ORMs to be a helpful
  part of a framework when done well.

* "[What is a web framework?](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)"
  is an in-depth explanation of what web frameworks are and their relation
  to web servers.

* [Django vs Flask vs Pyramid: Choosing a Python Web Framework](https://www.airpair.com/python/posts/django-flask-pyramid)
  contains background information and code comparisons for similar
  web applications built in these three big Python frameworks.

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

* [Django vs. Flask in 2019: Which Framework to Choose](https://testdriven.io/blog/django-vs-flask/)
  looks at the best use cases for Django and Flask along with what 
  makes them unique, from an educational and development standpoint.

* [11 new Python web frameworks](https://deepsource.io/blog/new-python-web-frameworks/)
  has a quick blurb on several newer frameworks that are still emerging,
  such as [Sanic](/sanic.html), [Masonite](https://docs.masoniteproject.com/)
  and [Molten](https://moltenframework.com/).


### Web frameworks learning checklist
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

