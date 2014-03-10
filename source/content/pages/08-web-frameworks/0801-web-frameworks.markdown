title: Web Frameworks
category: page
slug: web-frameworks
sort-order: 08


# Web frameworks
A web application framework is a collection of libraries that 
provide functionality to accomplish common operations for the web. These
common operations include:

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


## Django
[Django](http://www.djangoproject.com/) is a widely used Python web 
application framework with a "batteries-included" philosophy. The principle
behind batteries-included is that the common functionality for building
web applications should come with the framework instead of as a separate
library. For example, 
[URL routing](https://docs.djangoproject.com/en/dev/topics/http/urls/), a 
[templating system](https://docs.djangoproject.com/en/dev/topics/templates/),
[object-relational mapper](https://docs.djangoproject.com/en/dev/topics/db/),
and [database schema migrations](https://docs.djangoproject.com/en/dev/topics/migrations/)
(as of version 1.7) are all included with the [Django framework](https://pypi.python.org/pypi/Django/1.6.2).


### Django resources
* [2 Scoops of Django](http://twoscoopspress.com/products/two-scoops-of-django-1-6) 
  by Daniel Greenfield and Audrey Roy is well worth the price of admission if
  you're serious about learning how to correctly develop Django websites.


* [Effective Django](http://effectivedjango.com/) and 
  [Tango with Django](http://www.tangowithdjango.com/book/) are a extensive 
  free introductions to using the most popular Python web framework.

* DjangoCon US videos from 
  [2013](http://www.youtube.com/user/TheOpenBastion/videos), 
  [2012](http://pyvideo.org/category/23/djangocon-2012), 
  [2011](http://pyvideo.org/category/3/djangocon-2011), as well as  
  [earlier US and DjangoCon EU conferences](http://pyvideo.org/category) are
  all available free of charge.

* The [Django subreddit](http://www.reddit.com/r/django) often has links to
  the latest resources for learning Django.

* Lincoln Loop wrote a 
  [Django Best Practices guide](http://lincolnloop.com/django-best-practices/)
  for the community.

* Steve Losh wrote an incredibly detailed [Django Advice guide](http://stevelosh.com/blog/2011/06/django-advice/).


## Flask
[Flask](http://flask.pocoo.org/) is a Python microframework deliberately 
built with a 
[small core and easy-to-extend philosophy](http://flask.pocoo.org/docs/design/). 
Flask is generally considered more 
[Pythonic](http://stackoverflow.com/questions/58968/what-defines-pythonian-or-pythonic) 
than Django because Flask web application code is often more
explicit. Flask was also written several years after Django and therefore
learned from the Python community's reactions as the framework evolved.
Jökull Sólberg wrote a great piece articulating to this effect in his 
[experience switching between Flask and Django](http://jokull.calepin.co/my-flask-to-django-experience.html).


### Flask resources
The 18-part Flask mega tutorial is an absolutely amazing starting 
resource for using the Flask framework. Yes, there are a lot of posts in 
the series. However, each post is focused on a single topic to contain 
the complexity while the reader is learning the framework. The whole 
series is well worth an in-depth read-through. The 
[author](https://twitter.com/miguelgrinberg) is also writing the 
[O'Reilly Flask Web Development](http://shop.oreilly.com/product/0636920031116.do)
book so consider picking that up as well.

  * [Part 1: Hello World](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
  * [Part 2: Templates](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
  * [Part 3: Web Forms](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
  * [Part 4: Database](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
  * [Part 5: User Logins](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
  * [Part 6: Profile Page and Avatars](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars)
  * [Part 7: Unit Testing](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing)
  * [Part 8: Followers, Contacts, and Friends](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends)
  * [Part 9: Pagination](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)
  * [Part 10: Full Text Search](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-full-text-search)
  * [Part 11: Email Support](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support)
  * [Part 12: Facelift](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-facelift)
  * [Part 13: Dates and Times](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-dates-and-times)
  * [Part 14: I18n and L10n](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-i18n-and-l10n)
  * [Part 15: Ajax](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-ajax)
  * [Part 16: Debugging, Testing and Profiling](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-debugging-testing-and-profiling)
  * [Part 17: Deployment on Linux](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux-even-on-the-raspberry-pi)
  * [Part 18: Deployment on the Heroku Cloud](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud)

* The [Flask Extensions Registry](http://flask.pocoo.org/extensions/) is a
  curated list of the best packages that extend Flask. It's the first location
  to look through when you're wondering how to do something that's not in the
  core framework.

* Great post by Jeff Knupp on [Productionizing a Flask App](http://www.jeffknupp.com/blog/2014/01/29/productionizing-a-flask-application/)

* The Plank & Whittle blog has two posts, one on 
  [Packaging a Flask web app](http://www.plankandwhittle.com/packaging-a-flask-web-app/) 
  and another on 
  [Packaging a Flask app in a Debian package](http://www.plankandwhittle.com/packaging-a-flask-app-in-a-debian-package/)
  once you've built an app and want to deploy it.

* The tuts+ [Flask tutorial](http://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822) 
  is another great walkthrough for getting started with the framework.


## Bottle
[Bottle](http://bottlepy.org/docs/dev/index.html) is a WSGI-compliant
[single source file](https://github.com/defnull/bottle/blob/master/bottle.py)
web framework with no external dependencies except for the standard library
included with Python.


### Bottle resources
* Digital Ocean provides an extensive [introductory post on Bottle](https://www.digitalocean.com/community/articles/how-to-use-the-bottle-micro-framework-to-develop-python-web-apps).

* This tutorial provides a walkthrough for
[getting started with Bottle](http://www.giantflyingsaucer.com/blog/?p=3598).

* Here's a short code snippet for 
  [creating a REST API with Bottle and MongoDB](http://myadventuresincoding.wordpress.com/2011/01/02/creating-a-rest-api-in-python-using-bottle-and-mongodb/).


## Web Framework Resources
* "[What is a web framework?](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)"
  by [Jeff Knupp](https://twitter.com/jeffknupp)
  is a in-depth explanation of what a web framework is and their relation
  to web servers.

* [Pyramid](http://www.pylonsproject.org/), 
  [Falcon](http://falconframework.org/),
  [web.py](http://webpy.org/) are the most common Python web frameworks other
  than Django, Flask and Bottle.

* This [roundup of 14 minimal Python frameworks](http://codecondo.com/14-minimal-web-frameworks-for-python/)
  contains both familiar and less known Python libraries.

