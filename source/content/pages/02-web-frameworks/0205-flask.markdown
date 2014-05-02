title: Flask
category: page
slug: flask
sort-order: 023
choice1url: /deployment.html
choice1icon: fa-share fa-inverse
choice1text: How do I deploy Flask web application when I'm ready to put it on the web?
choice2url: /web-frameworks.html
choice2icon: fa-code fa-inverse
choice2text: I'd like to go back to reviewing other web frameworks.
choice3url: /cascading-style-sheets.html
choice3icon: fa-css3 fa-inverse
choice3text: The user interface looks terrible. How do I style my web app?
choice4url: /source-control.html
choice4icon: fa-code-fork fa-inverse
choice4text: How can I version and store my source code so I don't lose it?


# Flask
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


## Flask framework learning checklist
<i class="fa fa-check-square-o"></i> 
[Install Flask](http://flask.pocoo.org/docs/installation/) on
your local development machine.

<i class="fa fa-check-square-o"></i> 
Work through the 18-part Flask tutorial listed first under "Flask resources"
below.
 
<i class="fa fa-check-square-o"></i> 
Read through [Flask Extensions Registry](http://flask.pocoo.org/extensions/)
to find out what extensions you'll need to build your project.

<i class="fa fa-check-square-o"></i> 
Start coding your Flask app based on what you learned from the 18 part
Flask tutorial plus open source example applications found below. 

<i class="fa fa-check-square-o"></i> 
Move on to the [deployment section](/deployment.html) to get your initial 
Flask project on the web.


## Flask resources
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

* [The Flask Extensions Registry](http://flask.pocoo.org/extensions/) is a
  curated list of the best packages that extend Flask. It's the first location
  to look through when you're wondering how to do something that's not in the
  core framework.

* Randall Degges wrote a detailed walkthrough for 
  [building a Flask app in 30 minutes](https://stormpath.com/blog/build-a-flask-app-in-30-minutes/).

* Nice post by Jeff Knupp on [Productionizing a Flask App](http://www.jeffknupp.com/blog/2014/01/29/productionizing-a-flask-application/).

* [Building Websites in Python with Flask](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/#.U06EZ-ZdW4J)
  is another walkthrough tutorial from first steps through 
  [getting bigger with Flask](http://maximebf.com/blog/2012/11/getting-bigger-with-flask/).


* The Plank & Whittle blog has two posts, one on 
  [Packaging a Flask web app](http://www.plankandwhittle.com/packaging-a-flask-web-app/) 
  and another on 
  [Packaging a Flask app in a Debian package](http://www.plankandwhittle.com/packaging-a-flask-app-in-a-debian-package/)
  once you've built an app and want to deploy it.

* The Tuts+ [Flask tutorial](http://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822) 
  is another great walkthrough for getting started with the framework.

* [Flask by Example: Part 1](http://www.realpython.com/blog/python/flask-by-example-part-1-project-setup/)
  shows the basic first steps for setting up a Flask project.

* [How to Structure Large Flask Applications](https://www.digitalocean.com/community/articles/how-to-structure-large-flask-applications)
  covers a subject that comes up quickly once you begin adding significant
  functionality to your Flask application.


## Open source Flask example projects
* [Flask Foundation](https://github.com/JackStouffer/Flask-Foundation) is a
  starting point for new Flask projects.

* [Flaskr TDD](https://github.com/mjhea0/flaskr-tdd) takes the official Flask
  tutorial and adds test driven development and JQuery to the project. 

* Use the [Flask App Engine Template](https://github.com/kamalgill/flask-appengine-template)
  for getting set up on Google App Engine with Flask.

* Here is a 
  [note-taking app](http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/)
  along with the 
  [source code in Gists](https://gist.github.com/coleifer/632d3c9aa6b2ea519384).


### What do you need to learn about web frameworks next?
