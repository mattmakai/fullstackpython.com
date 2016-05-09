title: Django
category: page
slug: django
sortorder: 0403
toc: False
sidebartitle: Django
meta: Learn more about Django, the popular batteries-included Python web framework, on Full Stack Python.


# Django
[Django](http://www.djangoproject.com/) is a widely-used Python web 
application framework with a "batteries-included" philosophy. The principle
behind batteries-included is that the common functionality for building
web applications should come with the framework instead of as separate
libraries.


<a href="http://www.djangoproject.com/" style="border: none;"><img src="/img/django-logo-positive.png" width="100%" alt="Official Django logo. Trademark Django Software Foundation." class="technical-diagram" /></a>


For example, 
[authentication](https://docs.djangoproject.com/en/dev/topics/auth/),
[URL routing](https://docs.djangoproject.com/en/dev/topics/http/urls/), a 
[templating system](https://docs.djangoproject.com/en/dev/topics/templates/),
an [object-relational mapper](/object-relational-mappers-orms.html) (ORM),
and [database schema migrations](https://docs.djangoproject.com/en/dev/topics/migrations/)
(as of version 1.7) are all included with the [Django framework](https://pypi.python.org/pypi/Django/). 
Compare that included functionality to the Flask framework which requires a 
separate library such as 
[Flask-Login](https://flask-login.readthedocs.org/en/latest/)
to perform user authentication. 

The batteries-included and extensibility philosophies are simply two different
ways to tackle framework building. Neither philosophy is inherently better 
than the other one.

<div class="well see-also">Django is an implementation of the <a href="/web-frameworks.html">web frameworks</a> concept. Learn how these pieces fit together in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Why is Django a good web framework choice?
The Django project's stability, performance and community have grown 
tremendously over the past decade since the framework's creation. Detailed
tutorials and good practices are readily available on the web and in books.
The framework continues to add significant new functionality such as 
[database migrations](https://docs.djangoproject.com/en/dev/topics/migrations/)
with each release. 

I highly recommend the Django framework as a starting place for new Python web 
developers because the official documentation and tutorials are some of the 
best anywhere in software development. Many cities also have Django-specific
groups such as [Django District](http://www.meetup.com/django-district/),
[Django Boston](http://www.meetup.com/djangoboston/) and 
[San Francisco Django](http://www.meetup.com/The-San-Francisco-Django-Meetup-Group/) 
so new developers can get help when they are stuck.

There's some debate on whether 
[learning Python by using Django is a bad idea](http://www.jeffknupp.com/blog/2012/12/11/learning-python-via-django-considered-harmful/). 
However, that criticism is invalid if you take the time to learn the Python
syntax and language semantics first before diving into web development.


## Django books and tutorials
There are a slew of free or low cost resources out there for Django. Since
Django was released over 10 years ago and has had a huge number of updates
since then, when you're looking for an up-to-date Django book check out the
list below or read this post showing [current Django books](http://twoscoopspress.org/pages/current-django-books)
as of Django 1.7.

* [Test-Driven Development with Python](http://www.obeythetestinggoat.com/) 
  focuses on web development using Django and JavaScript. This book uses 
  the development of a website using the Django web framework as a real
  world example of how to perform test-driven development (TDD). There is
  also coverage of NoSQL, websockets and asynchronous responses. The book can
  be read online for free or purchased in hard copy via O'Reilly.

* [Tango with Django](http://www.tangowithdjango.com/book17/) is an extensive 
  set of free introductions to using the most popular Python web framework. 
  Several current developers said this book really helped them get over the 
  initial framework learning curve. It's recently been updated for Django 1.7!

* The [Django Girls Tutorial](http://tutorial.djangogirls.org/en/index.html)
  is a great tutorial that doesn't assume any prior knowledge of Python or
  Django while helping you build your first web application.

* [2 Scoops of Django](http://twoscoopspress.com/products/two-scoops-of-django-1-8) 
  by Daniel Greenfeld and Audrey Roy is well worth the price of admission if
  you're serious about learning how to correctly develop Django websites.

* [Effective Django](http://effectivedjango.com/) is another free introduction
  to the web framework.

* The [Django subreddit](http://www.reddit.com/r/django) often has links to
  the latest resources for learning Django and is also a good spot to ask 
  questions about it.

* Steve Losh wrote an incredibly detailed [Django Advice guide](http://stevelosh.com/blog/2011/06/django-advice/).

* [Lightweight Django](http://programming.oreilly.com/2014/04/simplifying-django.html)
  has several nice examples for breaking Django into smaller simpler 
  components.

* The [Definitive Guide to Django Deployment](https://github.com/rogueleaderr/definitive_guide_to_django_deployment)
  explains the architecture of the resulting set up and includes Chef scripts
  to automate the deployment.

* [Deploying a Django app on Amazon EC2 instance](http://agiliq.com/blog/2014/08/deploying-a-django-app-on-amazon-ec2-instance/)
  is a detailed walkthrough for deploying an example Django app to Amazon
  Web Services.

* This [step-by-step guide for Django](http://aliteralmind.wordpress.com/2014/09/21/jquery_django_tutorial/)
  shows how to transmit data via AJAX with JQuery.

* [django-awesome](https://github.com/rosarior/awesome-django) is a curated
  list of Django libraries and resources.

* [Starting a Django Project](https://realpython.com/learn/start-django/) 
  answers the question, “How do I set up a Django (1.5, 1.6, or 1.7) project 
  from scratch?”

* This Django tutorial shows how to 
  [build a project from scratch using Twitter Bootstrap, Bower, Requests and the Github API](http://drksephy.github.io/2015/07/16/django/).

* The [recommended Django project layout](http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/)
  is helpful for developers new to Django to understand how to structure
  the directories and files within apps for projects.

* This [Python Social Auth for Django tutorial](https://github.com/davisfreeman1015/SocialAuthDjangoTutorial)
  will show you how to integrate social media sign in buttons into your Django
  application.

* Luke Plant writes about 
  [his approach to class based views](http://lukeplant.me.uk/blog/posts/my-approach-to-class-based-views/) (CBVs),
  which often provoke heated debate in the Django community for whether they
  are a time saver or "too much magic" for the framework.

* [How to serve Django apps with uWSGI and Nginx on 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)
  and 
  [how to set up Django with PostgreSQL, Nginx and Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-centos-7) 
  are detailed tutorials that walk through each step in the deployment process.

* Working with time zones is necessary for every web application. This 
  [blog post on pytz and Django](http://tommikaikkonen.github.io/timezones/) is a
  great start for figuring out what you need to know.


## Django videos
Are you looking for Django videos in addition to articles? There is a special section
for Django and web development on the [best Python videos](/best-python-videos.html) page.


## Django migrations
* Paul Hallett wrote a 
  [detailed Django 1.7 app upgrade guide](https://www.twilio.com/blog/2014/10/upgrading-your-django-reusable-app-to-support-django-1-7.html) 
  on the Twilio blog from his experience working with the django-twilio 
  package.

* Real Python's [migrations primer](https://realpython.com/blog/python/django-migrations-a-primer/)
  explores the difference between South's migrations and the built-in
  Django 1.7 migrations as well as how you use them.

* Andrew Pinkham's "Upgrading to Django 1.7" series is great learning
  material for understanding what's changed in this major release and
  how to adapt your Django project.
  [Part 1](http://andrewsforge.com/article/upgrading-django-to-17/part-1-introduction-and-django-releases/),
  [part 2](http://andrewsforge.com/article/upgrading-django-to-17/part-2-migrations-in-django-16-and-17/) and
  [part 3](http://andrewsforge.com/article/upgrading-django-to-17/part-3-django-17-new-features/)
  and
  [part 4](http://andrewsforge.com/article/upgrading-django-to-17/part-4-upgrade-strategies/)
  are now all available to read.

* [Django migrations without downtimes](http://pankrat.github.io/2015/django-migrations-without-downtimes/)
  shows one potential way of performing on-line schema migrations with
  Django.


## Channels in 1.9+
Channels are a new mechanism in Django 1.9 (as a standalone app, later
for incorporation into the core framework) for real-time full-duplex
communication between the browser and the server based on 
[WebSockets](/websockets.html). 
  
* This 
  [tutorial shows how to get started with Django Channels in your project](https://blog.heroku.com/archives/2016/3/17/in_deep_with_django_channels_the_future_of_real_time_apps_in_django).

* The 
  [channels examples repository](https://github.com/andrewgodwin/channels-examples)
  contains a couple of good starter projects such as a live blog and a 
  chat application to use as base code.

* Channnels currently use Django's existing authentication scheme, but
  this blog post [JSON Web Tokens authentication on Django Channels](http://www.machinalis.com/blog/jwt-django-channels/)
  shows how to use a custom [JSON Web Token (JWT)](https://jwt.io/)
  implementation in Django Channels instead.


## Django testing
* [Integrating Front End Tools with Django](https://lincolnloop.com/blog/integrating-front-end-tools-your-django-project/)
  is a good post to read for figuring out how to use [Gulp](http://gulpjs.com/)
  for handling front end tools in development and production Django sites.

* [Getting Started with Django Testing](http://howchoo.com/g/mjkwmtu5zdl/getting-started-with-django-testing)
  will help you stop procrastinating on testing your Django projects if you're
  uncertain where to begin.

* [Testing in Django](https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/)
  provides numerous examples and explanations for how to test your Django
  project's code.

* [Django views automated testing with Selenium](https://medium.com/@unary/django-views-automated-testing-with-selenium-d9df95bdc926)
  gives some example code to get up and running with 
  [Selenium](http://www.seleniumhq.org) browser-based tests.


## Django with Angular (Djangular) resources
* [Getting Started with Django Rest Framework and AngularJS](http://blog.kevinastone.com/getting-started-with-django-rest-framework-and-angularjs.html)
  is a very detailed introduction to Djangular with example code. 

* [Building Web Applications with Django and AngularJS](https://thinkster.io/brewer/angular-django-tutorial/)
  is a very detailed guide for using Django as an API layer and AngularJS
  as the MVC front end in the browser.

* This [end to end web app with Django-Rest-Framework & AngularJS part 1](http://mourafiq.com/2013/07/01/end-to-end-web-app-with-django-angular-1.html)
  tutorial along with 
  [part 2](http://mourafiq.com/2013/07/15/end-to-end-web-app-with-django-angular-2.html),
  [part 3](http://mourafiq.com/2013/08/01/end-to-end-web-app-with-django-angular-3.html)
  and
  [part 4](http://mourafiq.com/2013/08/15/end-to-end-web-app-with-django-angular-4.html)
  creates an example blog application with Djangular. There is also a
  corresponding [GitHub repo](https://github.com/mouradmourafiq/django-angular-blog)
  for the project code.

* [Django-angular](https://github.com/jrief/django-angular) is a code 
  library that aims to make it easier to pair Django with AngularJS on
  the front end.


## Django ORM resources
Django comes with its own custom object-relational mapper (ORM) typically
referred to as "the Django ORM". Learn more about the Django ORM on the
[Python object-relational mappers page](/object-relational-mappers-orms.html) 
that includes a section specifically for the Django ORM as well as additional
resources and tutorials.


## Static and media files
Deploying and handling static and media files can be confusing for new
Django developers. These resources along with the 
[static content](/static-content.html) page are useful for figuring out how 
to handle these files properly.

* [Using Amazon S3 to Store your Django Site's Static and Media Files](http://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)
  is a well written guide to a question commonly asked about static and
  media file serving.

* [Loading Django FileField and ImageFields from the file system](http://www.revsys.com/blog/2014/dec/03/loading-django-files-from-code/)
  shows how to load a model field with a file from the file system.

* [Restricting access to user-uploaded files in Django](http://blog.wearefarm.com/2015/02/09/contact-form-uploads/)
  provides a protection mechanism for media files.



## Open source Django example projects
* [Browser calls with Django and Twilio](https://www.twilio.com/docs/howto/walkthrough/browser-calls/python/django)
  shows how to build a web app with Django and 
  [Twilio Client](https://www.twilio.com/client) to turn a user's web 
  browser into a full-fledged phone. Pretty awesome!

* [Txt 2 React](https://github.com/makaimc/txt2react) is a full Django web
  app that allows audiences to text in during a presentation with feedback
  or questions.

* [Openduty](https://github.com/ustream/openduty) is a website status checking
  and alert system similar to PagerDuty.

* [Courtside](https://github.com/myusuf3/courtside) is a pick up sports web 
  application written and maintained by the author of PyCoder's Weekly.

* These two Django Interactive Voice Response (IVR) system web application
  repositories [part 1](https://github.com/phalt/twilio-django-part-1) and
  [part 2](https://github.com/phalt/twilio-django-part-2) show you how to
  build a really cool Django application. There's also an accompanying 
  [blog post](https://www.twilio.com/blog/2014/07/build-an-ivr-system-with-twilio-and-django.html)
  with detailed explanations of each step.

* [Taiga](https://github.com/taigaio/taiga-back) is a project management
  tool built with Django as the backend and AngularJS as the front end.


## Django project templates
* [Caktus Group's Django project template](https://github.com/caktus/django-project-template) 
  is Django 1.6+ ready.

* [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django) is a 
  project template from Daniel Greenfeld, for use with Audrey Roy's 
  [Cookiecutter](https://github.com/audreyr/cookiecutter). The template results
  are Heroku deployment-ready.

* [Two Scoops Django project template](https://github.com/twoscoops/django-twoscoops-project)
  is also from the PyDanny and Audrey Roy. This one provides a quick scaffold
  described in the Two Scoops of Django book.

* [Sugardough](https://github.com/mozilla/sugardough) is a Django project
  template from Mozilla that is compatible with cookiecutter.


## Django learning checklist
1. [Install Django](https://docs.djangoproject.com/en/dev/topics/install/) on
   your local development machine.

1. Work through the initial 
   ["polls" tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/).
 
1. Build a few more simple applications using the tutorial resources found
   in the "Django resources" section.

1. Start coding your own Django project with help from the 
   [official documentation](https://docs.djangoproject.com/en/dev/) and 
   resource links below. You'll make plenty of mistakes which is critical
   on your path to learning the right way to build applications.

1. Read [2 Scoops of Django](http://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342) 
   to understand Django good practices and learn better ways of building 
   Django web applications.

1. Move on to the [deployment section](/deployment.html) to get your Django 
   project on the web.

