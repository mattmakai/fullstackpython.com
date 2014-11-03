title: Django
category: page
slug: django
sort-order: 0202
choice1url: /cascading-style-sheets.html
choice1icon: fa-css3 fa-inverse
choice1text: My user interface looks terrible. How do I style a web application?
choice2url: /api-integration.html
choice2icon: fa-link fa-inverse
choice2text: I want to integrate external APIs into my Django project.
choice3url: /deployment.html
choice3icon: fa-share fa-inverse
choice3text: How do I deploy a Django web app once it's coded?
choice4url: /source-control.html
choice4icon: fa-code-fork fa-inverse
choice4text: How can I version and store my source code so I don't lose it?


# Django
[Django](http://www.djangoproject.com/) is a widely used Python web 
application framework with a "batteries-included" philosophy. The principle
behind batteries-included is that the common functionality for building
web applications should come with the framework instead of as separate
libraries. 


<a href="http://www.djangoproject.com/" style="border: none;"><img src="theme/img/django-logo-positive.png" width="100%" alt="Official Django logo. Trademark Django Software Foundation." class="technical-diagram" /></a>


For example, 
[authentication](https://docs.djangoproject.com/en/dev/topics/auth/),
[URL routing](https://docs.djangoproject.com/en/dev/topics/http/urls/), a 
[templating system](https://docs.djangoproject.com/en/dev/topics/templates/),
an [object-relational mapper](https://docs.djangoproject.com/en/dev/topics/db/),
and [database schema migrations](https://docs.djangoproject.com/en/dev/topics/migrations/)
(as of version 1.7) are all included with the [Django framework](https://pypi.python.org/pypi/Django/1.6.2). 
Compare that included functionality to the Flask framework which requires a 
separate library such as 
[Flask-Login](https://flask-login.readthedocs.org/en/latest/)
to perform user authentication. 

The batteries-included and extensibility philosophies are simply two different 
ways to tackle framework building.  Neither philosophy is inherently better 
than the other.


## Why is Django a good web framework choice?
The Django project's stability, performance and community have grown 
tremendously over the past decade since the framework's creation. Detailed
tutorials and best practices are readily available on the web and in books.
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


## Django tutorials
* [Tango with Django](http://www.tangowithdjango.com/book/) is an extensive 
  set of free introductions to using the most popular Python web framework. Several
  current developers said this book really helped them get over the initial
  framework learning curve.

* [2 Scoops of Django](http://twoscoopspress.com/products/two-scoops-of-django-1-6) 
  by Daniel Greenfeld and Audrey Roy is well worth the price of admission if
  you're serious about learning how to correctly develop Django websites.

* [Effective Django](http://effectivedjango.com/) is another free introduction
  to the web framework.

* The [Django subreddit](http://www.reddit.com/r/django) often has links to
  the latest resources for learning Django and is also a good spot to ask 
  questions about it.

* Lincoln Loop wrote a 
  [Django Best Practices guide](http://lincolnloop.com/django-best-practices/)
  for the community.

* Steve Losh wrote an incredibly detailed [Django Advice guide](http://stevelosh.com/blog/2011/06/django-advice/).

* [Lightweight Django](http://programming.oreilly.com/2014/04/simplifying-django.html)
  has several nice examples for breaking Django into smaller simplier 
  components.

* The [Definitive Guide to Django Deployment](https://github.com/rogueleaderr/definitive_guide_to_django_deployment)
  explains the architecture of the resulting set up and includes Chef scripts
  to automate the deployment.

* [Deploying a Django app on Amazon EC2 instance](http://agiliq.com/blog/2014/08/deploying-a-django-app-on-amazon-ec2-instance/)
  is a detailed walkthrough for deploying an example Django app to Amazon
  Web Services.

* This [step-by-step guide for Django](http://aliteralmind.wordpress.com/2014/09/21/jquery_django_tutorial/)
  shows how to transmit data via AJAX with JQuery.

* [Deploying Django on AWS](http://www.nickpolet.com/blog/deploying-django-on-aws/1/)
  is another walkthrough for deploying Django to AWS.

* [django-awesome](https://github.com/rosarior/awesome-django) is a curated
  list of Django libraries and resources.

* [Starting a Django Project](https://realpython.com/learn/start-django/) answers the question, “How do I set up a Django (1.5, 1.6, or 1.7) project from scratch?”


## Django videos
* Kate Heddleston and I gave a talk at DjangoCon 2014 called
  [Choose Your Own Django Deployment Adventure](https://www.youtube.com/watch?v=QrFEKghISEI)
  which walked through many of the scenarios you'd face when deploying your
  first Django website.

* [GoDjango](https://godjango.com/) screencasts and tutorials are free short
  videos for learning how to build Django applications.

* [Getting Started with Django](http://gettingstartedwithdjango.com/) is a
  series of video tutorials for the framework.

* DjangoCon US videos from 
  [2014](https://www.youtube.com/playlist?list=PLE7tQUdRKcybbNiuhLcc3h6WzmZGVBMr3), 
  [2013](http://www.youtube.com/user/TheOpenBastion/videos), 
  [2012](http://pyvideo.org/category/23/djangocon-2012), 
  [2011](http://pyvideo.org/category/3/djangocon-2011), as well as  
  [earlier US and DjangoCon EU conferences](http://pyvideo.org/category) are
  all available free of charge.


## Django 1.7-specific resources
* Paul Hallett wrote a 
  [detailed Django 1.7 app upgrade guide](https://www.twilio.com/blog/2014/10/upgrading-your-django-reusable-app-to-support-django-1-7.html) 
  on the Twilio blog from his experience working with the django-twilio 
  package.

* [Designing Django's Migrations](http://pyvideo.org/video/2630/designing-djangos-migrations)
  covers Django 1.7's new migrations from the main programmer 
  of South and now Django's built-in migrations, Andrew Godwin.

* Real Python's [migrations primer](https://realpython.com/blog/python/django-migrations-a-primer/)
  explores the difference between South's migrations and the built-in
  Django 1.7 migrations as well as how you use them.

* Andrew Pinkham's "Upgrading to Django 1.7" series is great learning
  material for understanding what's changed in this major release and
  how to adapt your Django project.
  [Part 1](http://andrewsforge.com/article/upgrading-django-to-17/part-1-introduction-and-django-releases/),
  [part 2](http://andrewsforge.com/article/upgrading-django-to-17/part-2-migrations-in-django-16-and-17/) and
  [part 3](http://andrewsforge.com/article/upgrading-django-to-17/part-3-django-17-new-features/)
  are currently available with further parts coming in the future.


## Django ORM resources
The [Django ORM](https://docs.djangoproject.com/en/dev/topics/db/) works well
for simple and medium-complexity database operations. However, there are often
complaints that the ORM makes complex queries much more complicated than
writing straight SQL or using [SQLAlchemy](http://www.sqlalchemy.org/). 

It's technically possible to drop down to SQL but it ties the queries to a 
specific database implementation. The ORM is coupled closely with Django so
replacing the default ORM with SQLAlchemy is currently a hack workaround. Note
though that some of the Django core committers believe it is only a matter of
time before the default ORM is replaced with SQLAlchemy. It will be a large
effort to get that working though so it's likely to come in Django 1.9 or 
later.

Since the majority of Django projects are tied to the default ORM, it's best to
read up on advanced use cases and tools for doing your best work within the
existing framework.

* [Django models, encapsulation and data integrity](http://www.dabapps.com/blog/django-models-and-encapsulation/)
  is a detailed article by Tom Christie on encapsulating Django models for
  data integrity.

* [Django Debug Toolbar](http://django-debug-toolbar.readthedocs.org/en/1.2/) 
  is a powerful Django ORM database query inspection tool. Highly recommended
  during development to ensure you're writing reasonable query code. 
  [Django Silk](http://mtford.co.uk/blog/2/) is another inspection tool and
  has capabilities to do more than just SQL inspection.

* [Making a specific Django app faster](http://reinout.vanrees.org/weblog/2014/05/06/making-faster.html)
  is a Django performance blog post with some tips on measuring performance
  and optimizing based on the measured results.

* [Why I Hate the Django ORM](https://speakerdeck.com/alex/why-i-hate-the-django-orm)
  is Alex Gaynor's overview of the bad designs decisions, some of which he
  made, while building the Django ORM.

* [Going Beyond Django ORM with Postgres](https://speakerdeck.com/craigkerstiens/going-beyond-django-orm-with-postgres)
  is specific to using PostgreSQL with Django.


## Open source Django example projects
* [Txt 2 React](https://github.com/makaimc/txt2react) is a full Django web
  app that allows audiences to text in during a presentation with feedback
  or questions.

* [Openduty](https://github.com/ustream/openduty) is a website status checking
  and alert system similar to PagerDuty.

* [Courtside](https://github.com/myusuf3/courtside) is a pick up sports web 
  application written and maintained by the author of PyCoder's Weekly.

* These two Django Interactive Voice Response (IVR) system web application
  repositorities [part 1](https://github.com/phalt/twilio-django-part-1) and
  [part 2](https://github.com/phalt/twilio-django-part-2) show you how to
  build a really cool Django application. There's also an accompanying 
  [blog post](https://www.twilio.com/blog/2014/07/build-an-ivr-system-with-twilio-and-django.html)
  with detailed explanations of each step.


## Django project templates
* [Caktus Group's Django project template](https://github.com/caktus/django-project-template) 
  is Django 1.6+ ready.

* [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django) is a 
  project template from Daniel Greenfeld, for use with Audrey Roy's 
  [Cookiecutter](https://github.com/audreyr/cookiecutter). Heroku 
  deployment-ready.

* [Two Scoops Django project template](https://github.com/twoscoops/django-twoscoops-project)
  is also from the PyDanny and Audrey Roy. This one provides a quick scaffold
  described in the Two Scoops of Django book.


## Django learning checklist
<i class="fa fa-check-square-o"></i> 
[Install Django](https://docs.djangoproject.com/en/dev/topics/install/) on
your local development machine.

<i class="fa fa-check-square-o"></i> 
Work through the initial 
["polls" tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/).
 
<i class="fa fa-check-square-o"></i> 
Build a few more simple applications using the tutorial resources found
in the "Django resources" section.

<i class="fa fa-check-square-o"></i> 
Start coding your own Django project with help from the 
[official documentation](https://docs.djangoproject.com/en/dev/) and 
resource links below. You'll make plenty of mistakes which is critical
on your path to learning the right way to build applications.

<i class="fa fa-check-square-o"></i> 
Read [2 Scoops of Django](http://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/098146730X/ref=sr_1_2?ie=UTF8&qid=1391562062&sr=8-2&tag=mlinar-20) 
to understand Django best practices and learn better ways of building 
Django web applications.

<i class="fa fa-check-square-o"></i> 
Move on to the [deployment section](/deployment.html) to get your Django 
project on the web.


### What do you need to learn next for your Django app?
