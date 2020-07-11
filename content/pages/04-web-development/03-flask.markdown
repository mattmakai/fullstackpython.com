title: Flask
category: page
slug: flask
sortorder: 0403
toc: False
sidebartitle: Flask
headerimage: /img/pages/flask-python-fsp.jpg
meta: Flask is a popular, extensible web microframework for building web applications with Python.


[Flask](http://flask.pocoo.org/) ([source code](https://github.com/pallets/flask))
is a Python [web framework](/web-frameworks.html) built with a 
[small core and easy-to-extend philosophy](http://flask.pocoo.org/docs/design/). 

<a href="http://flask.pocoo.org/" style="border: none;"><img src="/img/logos/flask.jpg" width="100%" alt="Official Flask logo. Flask Artwork License." class="technical-diagram"></a>


### Why is Flask a good web framework choice?
Flask is considered more 
[Pythonic](http://blog.startifact.com/posts/older/what-is-pythonic.html)
than the [Django](/django.html) web framework because in common situations the
equivalent Flask web application is more explicit. Flask is also easy to get 
started with as a beginner because there is little boilerplate code for getting a 
simple app up and running. 

For example, here is a valid "Hello, world!" web application with Flask:

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```


The above code shows "Hello, World!" on localhost port 5000 in a web browser 
when run with the `python app.py` command and the Flask library installed.

The equivalent "Hello, World!" web application using the [Django](/django.html)
[web framework](/web-frameworks.html) would involve significantly more boilerplate
code.

Flask was also written several years after Django and therefore
learned from the Python community's reactions as the framework evolved.
Jökull Sólberg wrote a great piece articulating to this effect in his 
[experience switching between Flask and Django](http://web.archive.org/web/20160305145017/http://jokull.calepin.co/my-flask-to-django-experience.html).

<div class="well see-also">Flask is an implementation of the <a href="/web-frameworks.html">web frameworks</a> concept. Learn how these parts fit together in the <a href="/web-development.html">web development</a> chapter or <a href="/table-of-contents.html">view all topics</a>.</div>


### How does Flask relate to the Pallets Projects?
Flask was originally designed and developed by Armin Ronacher as an 
[April Fool's Day joke in 2010](http://lucumr.pocoo.org/2010/4/3/april-1st-post-mortem/).
Despite the origin as a joke, the Flask framework became wildly popular as 
an alternative to Django projects with their monolithic structure and 
dependencies.

Flask's success created a lot of additional work in issue tickets and pull 
requests. Armin eventually created 
[The Pallets Projects](https://www.palletsprojects.com/) collection of open
source code libraries after he had been managing Flask under his own GitHub 
account for several years. The Pallets Project now serves as the 
community-driven organization that handles Flask and other related Python
libraries such as [Lektor](/lektor.html), [Jinja](/jinja2.html) and
several others.


### Flask tutorials
The "Hello, World!" code for Flask is just seven lines of code but learning how
to build full-featured web applications with any framework takes a lot of work.
These resources listed below are the best up-to-date tutorials and references
for getting started.

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
  Miguel also wrote and recorded numerous
  [Flask Web Development content including a great book and video](https://flaskbook.com/)
  book that are excellent resources worth the price, especially to support
  his continuous revisions to the content. 

* Armin Ronacher, the creator of Flask, presented the technical talk
  [Flask for Fun and Profit](https://www.youtube.com/watch?v=1ByQhAM5c1I)
  at PyBay 2016 where he discusses using the framework to build web apps
  and [APIs](/application-programming-interfaces.html).

* [Explore Flask](http://exploreflask.com/) is a public domain book that
  was previously backed on Kickstarter and cost money for about a year before
  being open sourced. The book explains best practices and patterns for 
  building Flask apps.

* [Learn to Build Web Applications with Flask and Docker](https://buildasaasappwithflask.com/)
  is a video course by [Nick Janetakis](https://github.com/nickjj)
  that shows how to build a Software-as-a-Service (SaaS) application that
  he [open sourced](https://github.com/nickjj/build-a-saas-app-with-flask)
  which uses Flask for the [web framework](/web-frameworks.html) and 
  [Docker](/docker.html) for the local 
  [development environment](/development-environments.html).

* [Flask by Example: Part 1](http://www.realpython.com/blog/python/flask-by-example-part-1-project-setup/)
  shows the basic first steps for setting up a Flask project. 
  [Part 2](http://www.realpython.com/blog/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/) 
  explains how to use PostgreSQL, SQLAlchemy and Alembic. 
  [Part 3](https://realpython.com/blog/python/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/)
  describes text processing with BeautifulSoup and NLTK. 
  [Part 4](https://realpython.com/blog/python/flask-by-example-implementing-a-redis-task-queue/)
  shows how to build a task queue with Flask and Redis.

* The blog post series "Things which aren't magic" covers how Flask's 
  ubiquitous @app.route decorator works under the covers. There are two 
  parts in the series,
  [part 1](https://ains.co/blog/things-which-arent-magic-flask-part-1.html)
  and 
  [part 2](https://ains.co/blog/things-which-arent-magic-flask-part-2.html).

* [How to Structure Large Flask Applications](https://www.digitalocean.com/community/articles/how-to-structure-large-flask-applications)
  covers a subject that comes up quickly once you begin adding significant
  functionality to your Flask application.

* [Flask Blueprint templates](http://fewstreet.com/2015/01/16/flask-blueprint-templates.html)
  shows a way of structuring your `__init__.py` file with 
  [blueprints](http://flask.pocoo.org/docs/latest/blueprints/) for expanding
  projects into many files and modules.

* If you're not sure why `DEBUG` should be set to `False` in a production
  [deployment](/deployment.html), be sure to read this article on 
  [how Patreon got hacked](http://labs.detectify.com/post/130332638391/how-patreon-got-hacked-publicly-exposed-werkzeug).

* [Developing a Single Page App with Flask and Vue.js](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs) step-by-step walkthrough of how to set up a basic CRUD app with Vue and Flask.


### Intermediate to advanced Flask resources
Once you move past the beginner tutorials and have created a few Flask
projects you will want to learn how to use Flask extensions, 
[deploy](/deployment.html) your code and integrate 
[web APIs](/application-programming-interfaces.html) to build more
extensive functionality. The following tutorials will guide you through
more advanced topics and provide solid learning materials, especially when 
combined with the example real-world projects listed in the next section.

* [Microservices with Docker, Flask, and React](https://testdriven.io/courses/microservices-with-docker-flask-and-react/?utm_source=fsp)
  is an awesome course for beyond-the-basics work with Flask. There are 
  a couple of free chapters and the rest of the course is well worth paying
  for to learn a bunch of valuable tools such as [Docker](/docker.html),
  [React](/react.html) and [microservices architectures](/microservices.html).

* [Visualize your trip with Flask and Mapbox](http://kazuar.github.io/visualize-trip-with-flask-and-mapbox/)
  along with the 
  [open source flask_mapbox GitHub repository](https://github.com/kazuar/flask_mapbox)
  provides a fantastic example visualization of a trip to Iceland with 
  Flask as the backend web framework.

* [Microservices with Flask, Docker, and React](https://testdriven.io/) 
  teaches how to spin up a reproducible Flask development environment with 
  [Docker](/docker.html). It shows how to [deploy](/deployment.html) it to an 
  Amazon EC2 instance then scale the services on Amazon EC2 Container Service (ECS).

* [Build a Video Chat Application with Python, JavaScript and Twilio Programmable Video](https://www.twilio.com/blog/build-video-chat-application-python-javascript-twilio-programmable-video)
  shows how to use [Twilio](/twilio.html) 
  [Programmable Video](https://www.twilio.com/video) to build cross-platform
  (web, iOS and Android) video into Flask applications.

* [Why and how to handle exceptions in Python Flask](https://opensource.com/article/17/3/python-flask-exceptions)
  has some great example code and reasons why you should code defensively
  by anticipating and handling the unhappy path exceptions in your Flask
  applications. The examples are relevant to any web framework you will use
  and are easy to copy and paste to test in your own applications.

* [The Flask Extensions Registry](http://flask.pocoo.org/extensions/) is a
  curated list of the best packages that extend Flask. It's the first location
  to look through when you're wondering how to do something that's not in the
  core framework.

* [How I Structure My Flask Application](http://mattupstate.com/blog/how-i-structure-my-flask-applications/)
  walks through how this developer organizes the components and architecture
  for his Flask applications.

* [Adding phone calling to your web application](https://www.twilio.com/docs/tutorials/walkthrough/browser-calls/python/flask)
  is a killer Flask tutorial with all the code needed to create a
  web app that can dial phones and receive inbound calls.

* Jeff Knupp provides some solid advice on how to 
  [productionize a Flask app](http://www.jeffknupp.com/blog/2014/01/29/productionizing-a-flask-application/).

* If you're looking for a fun tutorial with Flask and WebSockets, check out
  my blog post on creating 
  [Choose Your Own Adventure Presentations with Reveal.js, Python and WebSockets](https://www.twilio.com/blog/2014/11/choose-your-own-adventure-presentations-with-reveal-js-python-and-websockets.html).
  Follow up that tutorial by 
  [building an admin interface in part 1](https://www.twilio.com/blog/2015/03/choose-your-own-adventures-presentations-wizard-mode-part-1-of-3.html),
  [part 2](https://www.twilio.com/blog/2015/05/choose-your-own-adventure-presentations-wizard-mode-part-2-of-3.html)
  and [part 3](https://www.twilio.com/blog/2015/07/choose-your-own-adventure-presentations-flask-reveal-js-websockets.html) 
  that'll show you how to use forms and SQLAlchemy. There is also a 
  companion open source 
  [GitHub repository](https://github.com/mattmakai/choose-your-own-adventure-presentations) 
  for the app with 
  [tags for each step](https://github.com/mattmakai/choose-your-own-adventure-presentations/releases) 
  in the blog posts.

* [One line of code cut our Flask page load times by 60%](https://medium.com/@5hreyans/the-one-weird-trick-that-cut-our-flask-page-load-time-by-70-87145335f679)
  is an important note about optimizing Flask template cache size to 
  dramatically increase performance in some cases.

* [Unit Testing Your Twilio App Using Python’s Flask and Nose](https://www.twilio.com/blog/2014/03/unit-testing-your-twilio-app-using-pythons-flask-and-nose.html)
  covers integrating the Twilio API into a Flask application and how to test 
  that functionality with [nose](https://nose.readthedocs.org/en/latest/).

* The Flask documentation has some quick examples for how to deploy Flask
  with 
  [standalone WSGI containers](http://flask.pocoo.org/docs/deploying/wsgi-standalone/).

* [Serverless Python Web Applications With AWS Lambda and Flask](https://spiegelmock.com/2018/09/06/serverless-python-web-applications-with-aws-lambda-and-flask/)
  is a spectacular post that walks through how to run Flask applications
  on AWS Lambda's [serverless](/serverless.html) offering. The tutorial
  has instructions on how to include 
  [application dependencies](/application-dependencies.html) and handle 
  your [deployment](/deployment.html) workflow.

* [Visualize your trip with Flask and Mapbox](http://kazuar.github.io/visualize-trip-with-flask-and-mapbox/)
  uses geographic GeoJSON data and presents it in a Flask application
  that uses [Mapbox](https://www.mapbox.com/).

* [Handling Email Confirmation in Flask](https://realpython.com/blog/python/handling-email-confirmation-in-flask/)
  is a great walkthrough for a common use case of ensuring an email address
  matches with the user's login information.

* [Static websites with Flask](http://www.dougalmatthews.com/2017/Jan/13/static-websites-with-flask/) 
  shows how to use Flask with 
  [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/) to generate a
  static website from a backend data source.

* [Running Flask on Docker Swarm](https://testdriven.io/running-flask-on-docker-swarm) details how to run a Flask app on Docker Swarm.
  
* [Running Flask on Kubernetes](https://testdriven.io/running-flask-on-kubernetes) step-by-step walkthrough of how to deploy a Flask-based microservice (along with Postgres and Vue.js) to a Kubernetes cluster.

* [Dynamic Secret Generation with Vault and Flask](https://testdriven.io/dynamic-secret-generation-with-vault-and-flask) looks at how to use Hashicorp's Vault and Consul to create dynamic Postgres credentials for a Flask web app.


### Open source Flask example projects
Flask's lack of standard boilerplate via a commandline interface for
setting up your project structure is a double edged sword. When you
get started with Flask you will have to figure out how to scale the 
files and modules for the code in your application. The following open 
source projects range from simple to complex and can give you ideas 
about how to working on your codebase.

* [Skylines](https://github.com/skylines-project/skylines) is an open source 
  flight tracking web application built with Flask. You can check out a 
  [running version of the application](https://skylines.aero/).

* [Flask JSONDash](https://github.com/christabor/flask_jsondash) is a Flask
  blueprint that creates JavaScript Object Notiation (JSON) 
  [APIs](/application-programming-interfaces.html) for [data](/data.html)
  dashboards.

* [Microblog](https://github.com/miguelgrinberg/microblog) is the companion
  open source project that goes along with Miguel Grinberg's O'Reilly Flask
  book.

* [Flaskr TDD](https://github.com/mjhea0/flaskr-tdd) takes the official Flask
  tutorial and adds test driven development and JQuery to the project. 

* Charles Leifer (author of [Peewee](/peewee.html) and [Pony ORM](/pony-orm.html)) 
  built a 
  [note-taking app](http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/)
  along with the 
  [source code in Gists](https://gist.github.com/coleifer/632d3c9aa6b2ea519384).

* [Reddit Job Search](https://github.com/anis-coding/Reddit-Job-Search)
  uses the [Reddit API](https://www.reddit.com/dev/api/) for a jobs data set
  and presents them via a Flask web app.

* [Bean Counter](https://github.com/BouncyNudibranch/bean-counter) is an
  open source Flask app for tracking coffee.

* [FlaskBB](http://flaskbb.org/) is a Flask app for a discussion forum.

* [psdash](https://github.com/Jahaja/psdash) is an app built with Flask and
  psutils to display information about the computer it is running on.


### Flask project templates
Flask's wide array of extension libraries comes at the cost of having a more
complicated project setup. The following project templates provide a starter
base that you can either use for your own applications or just learn various
ways to structure your code.

* Use the 
  [Flask App Engine Template](https://github.com/kamalgill/flask-appengine-template)
  for getting set up on Google App Engine with Flask.

* [Flask Foundation](https://github.com/JackStouffer/Flask-Foundation) is a
  starting point for new Flask projects. There's also a 
  [companion website](https://jackstouffer.github.io/Flask-Foundation/) for
  the project that explains what extensions the base project includes.

* [Cookiecutter Flask](https://github.com/cookiecutter-flask/cookiecutter-flask) is a 
  project template for use with 
  [Cookiecutter](https://github.com/audreyr/cookiecutter).

* [Flask-Boilerplate](https://github.com/MaxHalford/Flask-Boilerplate) 
  provides another starting project with sign up, log in and password
  reset.

* The company Sunscrapers provides this 
  [Flask boilerplate project with SQLAlchemy, py.test and Celery](https://github.com/sunscrapers/flask-boilerplate)
  baked into the Flask project structure.

* [flask-webpack-cookiecutter](https://github.com/mattfinnell/flask-webpack-cookiecutter/)
  combines a Flask framework project structure with 
  [Webpack](https://webpack.js.org/), a module bundler frequently used
  in the JavaScript world.


## Open source code for learning Flask
There are many open source projects that rely on Flask to operate.
One of the best ways to learn how to use this framework is to read
how other projects use it in real-world code. This section lists
these code examples by class and method in Flask.
