title: Flask
category: page
slug: flask
sortorder: 0404
toc: False
sidebartitle: Flask
meta: Flask is a popular, extensible web microframework for building web applications with Python.


# Flask
[Flask](http://flask.pocoo.org/) is a Python web framework built with a 
[small core and easy-to-extend philosophy](http://flask.pocoo.org/docs/design/). 

<a href="http://flask.pocoo.org/" style="border: none;"><img src="/img/flask.jpg" width="100%" alt="Official Flask logo. Flask Artwork License." class="technical-diagram"></a>


## Why is Flask a good web framework choice?
Flask is considered more 
[Pythonic](http://blog.startifact.com/posts/older/what-is-pythonic.html)
than Django because Flask web application code is in most cases more explicit. 
Flask is easy to get started with as a beginner because there is little 
boilerplate code for getting a simple app up and running. 

For example, here's a valid "hello world" web application with Flask (the
equivalent in Django would be significantly more code):

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()

Flask was also written several years after Django and therefore
learned from the Python community's reactions as the framework evolved.
Jökull Sólberg wrote a great piece articulating to this effect in his 
[experience switching between Flask and Django](http://jokull.calepin.co/my-flask-to-django-experience.html).

<div class="well see-also">Flask is an implementation of the <a href="/web-frameworks.html">web frameworks</a> concept. Learn how these pieces fit together in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Flask resources
* The Flask mega tutorial by 
  [Miguel Grinberg](https://twitter.com/miguelgrinberg) is a perfect 
  starting resource for using this web framework. Each post focuses on a 
  single topic and builds on previous posts. The series includes 18 parts:
  [#1 Hello World](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), 
  [#2 Templates](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates),
  [#3 Web Forms](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms),
  [#4 Database](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database),
  [#5 User Logins](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins),
  [#6 Profile Page and Avatars](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars),
  [#7 Unit Testing](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing),
  [#8 Followers, Contacts, and Friends](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends),
  [#9 Pagination](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination),
  [#10 Full Text Search](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-full-text-search),
  [#11 Email Support](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support),
  [#12 Facelift](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-facelift),
  [#13 Dates and Times](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-dates-and-times),
  [#14 I18n and L10n](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-i18n-and-l10n),
  [#15 Ajax](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-ajax),
  [#16 Debugging, Testing and Profiling](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-debugging-testing-and-profiling),
  [#17 Deployment on Linux](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux-even-on-the-raspberry-pi)
  and 
  [#18 Deployment on the Heroku Cloud](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud). 
  Miguel also wrote the 
  [O'Reilly Flask Web Development](http://shop.oreilly.com/product/0636920031116.do)
  book which is also an excellent learning resource.

* If you're looking for a fun tutorial with Flask and WebSockets, check out
  my blog post on creating 
  [Choose Your Own Adventure Presentations with Reveal.js, Python and WebSockets](https://www.twilio.com/blog/2014/11/choose-your-own-adventure-presentations-with-reveal-js-python-and-websockets.html).
  Follow up that tutorial by 
  [building an admin interface in part 1](https://www.twilio.com/blog/2015/03/choose-your-own-adventures-presentations-wizard-mode-part-1-of-3.html),
  [part 2](https://www.twilio.com/blog/2015/05/choose-your-own-adventure-presentations-wizard-mode-part-2-of-3.html)
  and [part 3](https://www.twilio.com/blog/2015/07/choose-your-own-adventure-presentations-flask-reveal-js-websockets.html) 
  that'll show you how to use forms and SQLAlchemy. There is also a 
  companion open source 
  [GitHub repository](https://github.com/makaimc/choose-your-own-adventure-presentations) 
  for the app with 
  [tags for each step](https://github.com/makaimc/choose-your-own-adventure-presentations/releases) 
  in the blog posts.

* This [simple Flask app uses Twilio Voice](https://www.twilio.com/blog/2015/09/warm-phone-call-transfers-with-python-flask-and-twilio-voice.html)
  to do voice calling with three participants. It's a fun introduction
  to Python and Flask I wrote for the Twilio blog.

* [The Flask Extensions Registry](http://flask.pocoo.org/extensions/) is a
  curated list of the best packages that extend Flask. It's the first location
  to look through when you're wondering how to do something that's not in the
  core framework.

* [Explore Flask](http://exploreflask.com/) is a public domain book that
  was previously backed on Kickstarter and cost money for about a year before
  being open sourced. The book explains best practices and patterns for 
  building Flask apps.

* [How I Structure My Flask Application](http://mattupstate.com/blog/how-i-structure-my-flask-applications/)
  walks through how this developer organizes the components and architecture
  for his Flask applications.

* Nice post by Jeff Knupp on [Productionizing a Flask App](http://www.jeffknupp.com/blog/2014/01/29/productionizing-a-flask-application/).

* The Plank & Whittle blog has two posts, one on 
  [Packaging a Flask web app](http://www.plankandwhittle.com/packaging-a-flask-web-app/) 
  and another on 
  [Packaging a Flask app in a Debian package](http://www.plankandwhittle.com/packaging-a-flask-app-in-a-debian-package/)
  once you've built an app and want to deploy it.

* The Tuts+ [Flask tutorial](http://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822) 
  is another great walkthrough for getting started with the framework.

* [Create Your Own Obnoxiously Simple Messaging App Just Like Yo](http://readwrite.com/2014/07/11/one-click-messaging-app)
  is a silly walkthrough of very basic Flask web application that uses
  [Nitrous.io](https://www.nitrous.io/) to get started and 
  [Twilio](https://www.twilio.com/) for SMS.

* The blog post series "Things which aren't magic" covers how Flask's 
  ubiquitous @app.route decorator works under the covers. There are two 
  parts in the series,
  [part 1](http://ains.co/blog/things-which-arent-magic-flask-part-1.html)
  and 
  [part 2](http://ains.co/blog/things-which-arent-magic-flask-part-2.html).

* [Flask by Example: Part 1](http://www.realpython.com/blog/python/flask-by-example-part-1-project-setup/)
  shows the basic first steps for setting up a Flask project. 
  [Part 2](http://www.realpython.com/blog/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/) 
  explains how to use PostgreSQL, SQLAlchemy and Alembic. 
  [Part 3](https://realpython.com/blog/python/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/)
  describes text processing with BeautifulSoup and NLTK. 
  [Part 4](https://realpython.com/blog/python/flask-by-example-implementing-a-redis-task-queue/)
  shows how to build a task queue with Flask and Redis.

* [Branded MMS Coupon Generation with Python and Twilio](https://www.twilio.com/blog/2014/10/branded-mms-coupon-generation-with-python-and-twilio.html)
  is a Flask tutorial I wrote for building a web application that can send
  branded barcode coupons via MMS. The post goes through every step from
  a blank directory until you have a working app that you can deploy to
  Heroku.

* [How to Structure Large Flask Applications](https://www.digitalocean.com/community/articles/how-to-structure-large-flask-applications)
  covers a subject that comes up quickly once you begin adding significant
  functionality to your Flask application.

* [Flask Blueprint templates](http://fewstreet.com/2015/01/16/flask-blueprint-templates.html)
  shows a way of structuring your `__init__.py` file with 
  [blueprints](http://flask.pocoo.org/docs/0.10/blueprints/) for large
  projects.

* [Video streaming with Flask](http://blog.miguelgrinberg.com/post/video-streaming-with-flask)
  is another fantastic tutorial by Miguel Grinberg that covers video 
  streaming.

* [One line of code cut our Flask page load times by 60%](https://medium.com/@5hreyans/the-one-weird-trick-that-cut-our-flask-page-load-time-by-70-87145335f679)
  is an important note about optimizing Flask template cache size to 
  dramatically increase performance in some cases.

* [Unit Testing Your Twilio App Using Python’s Flask and Nose](https://www.twilio.com/blog/2014/03/unit-testing-your-twilio-app-using-pythons-flask-and-nose.html)
  covers integrating the Twilio API into a Flask application and how to test 
  that functionality with [nose](https://nose.readthedocs.org/en/latest/).

* The Flask documentation has some quick examples for how to deploy Flask
  with 
  [standalone WSGI containers](http://flask.pocoo.org/docs/deploying/wsgi-standalone/).

* [Handling Email Confirmation in Flask](https://realpython.com/blog/python/handling-email-confirmation-in-flask/)
  is a great walkthrough for a common use case of ensuring an email address
  matches with the user's login information.

* If you're not sure why `DEBUG` should be set to `False` in a production
  [deployment](/deployment.html), be sure to read this article on 
  [how Patreon got hacked](http://labs.detectify.com/post/130332638391/how-patreon-got-hacked-publicly-exposed-werkzeug).


## Open source Flask example projects
* [Choose Your Own Adventure Presentations](https://github.com/makaimc/choose-your-own-adventure-presentations)
  combines Flask with [Reveal.js](http://lab.hakim.se/reveal-js/) and text 
  messages to create presentations where the audience can vote on how the 
  story should proceed. The code is all open source under an MIT license
  and also uses the 
  [Flask-SocketIO](https://flask-socketio.readthedocs.org/en/latest/) and 
  [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/) projects to
  support voting and form input.

* [Skylines](https://github.com/skylines-project/skylines) is an open source 
  flight tracking web application built with Flask. You can check out a 
  [running version of the application](https://skylines.aero/).

* [Microblog](https://github.com/miguelgrinberg/microblog) is the companion
  open source project that goes along with Miguel Grinberg's O'Reilly Flask
  book.

* [Flaskr TDD](https://github.com/mjhea0/flaskr-tdd) takes the official Flask
  tutorial and adds test driven development and JQuery to the project. 

* Here is a 
  [note-taking app](http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/)
  along with the 
  [source code in Gists](https://gist.github.com/coleifer/632d3c9aa6b2ea519384).

* [Bean Counter](https://github.com/BouncyNudibranch/bean-counter) is an
  open source Flask app for tracking coffee.

* [FlaskBB](http://flaskbb.org/) is a Flask app for a discussion forum.

* [psdash](https://github.com/Jahaja/psdash) is an app built with Flask and
  psutils to display information about the computer it is running on.


## Flask project templates
* Use the 
  [Flask App Engine Template](https://github.com/kamalgill/flask-appengine-template)
  for getting set up on Google App Engine with Flask.

* [Flask Foundation](https://github.com/JackStouffer/Flask-Foundation) is a
  starting point for new Flask projects. There's also a 
  [companion website](https://jackstouffer.github.io/Flask-Foundation/) for
  the project that explains what extensions the base project includes.

* [Cookiecutter Flask](https://github.com/sloria/cookiecutter-flask) is a 
  project template for use with 
  [Cookiecutter](https://github.com/audreyr/cookiecutter).

* [Flask-Boilerplate](https://github.com/MaxHalford/Flask-Boilerplate) 
  provides another starting project with sign up, log in and password
  reset.


## Flask framework learning checklist
1. [Install Flask](http://flask.pocoo.org/docs/installation/) on
   your local development machine.

1. Work through the 18-part Flask tutorial listed first under "Flask 
   resources" above.
 
1. Read through 
   [Flask Extensions Registry](http://flask.pocoo.org/extensions/) to find 
   out what extensions you'll need to build your project.

1. Start coding your Flask app based on what you learned from the 18 part
   Flask tutorial plus open source example applications found below. 

1. Move on to the [deployment section](/deployment.html) to get your initial 
   Flask project on the web.

