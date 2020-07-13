title: Django
category: page
slug: django
sortorder: 0402
toc: False
sidebartitle: Django
meta: Learn more about Django, the popular batteries-included Python web framework, on Full Stack Python.


[Django](http://www.djangoproject.com/) is a widely-used Python web 
application framework with a "batteries-included" philosophy. The principle
behind batteries-included is that the common functionality for building
web applications should come with the framework instead of as separate
libraries.

<a href="http://www.djangoproject.com/" style="border: none;"><img src="/img/logos/django.png" width="100%" alt="Official Django logo. Trademark Django Software Foundation." class="shot"></a>

For example, 
[authentication](https://docs.djangoproject.com/en/dev/topics/auth/),
[URL routing](https://docs.djangoproject.com/en/dev/topics/http/urls/), a 
[template engine](/django-templates.html),
an [object-relational mapper](/object-relational-mappers-orms.html) (ORM),
and [database schema migrations](https://docs.djangoproject.com/en/dev/topics/migrations/)
are all included with the [Django framework](https://pypi.org/project/Django/). 
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
There are a slew of free or low cost resources out there for Django. Make
sure to check the version numbers used in each post you read because 
Django was released over 10 years ago and has had a huge number of updates
since then. These resources are geared towards beginners. If you are already
experienced with Django you should take a look at the next section of
resources for more advanced tutorials.

* [Tango with Django](http://www.tangowithdjango.com/) is an extensive 
  set of free introductions to using the most popular Python web framework. 
  Several current developers said this book really helped them get over the 
  initial framework learning curve.

* The [Django Girls Tutorial](http://tutorial.djangogirls.org/en/index.html)
  is a great tutorial that doesn't assume any prior knowledge of Python or
  Django while helping you build your first web application.

* [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)
  is a wonderful seven-part series that incrementally builds out a Django
  project and handles [deploying the app](/deployment.html) in the final 
  post. The seven parts are:

    * [Getting Started](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)
    * [Fundamentals](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)
    * [Advanced Concepts](https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html)
    * [Authentication](https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html)
    * [Django ORM](https://simpleisbetterthancomplex.com/series/2017/10/02/a-complete-beginners-guide-to-django-part-5.html)
    * [Class-Based Views](https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html)
    * [Deployment](https://simpleisbetterthancomplex.com/series/2017/10/16/a-complete-beginners-guide-to-django-part-7.html)

* [Test-Driven Development with Python](http://www.obeythetestinggoat.com/) 
  focuses on web development using Django and JavaScript. This book uses 
  the development of a website using the Django web framework as a real
  world example of how to perform test-driven development (TDD). There is
  also coverage of NoSQL, WebSockets and asynchronous responses. The book can
  be read online for free or purchased in hard copy via O'Reilly.

* [Django OverIQ](https://overiq.com/django/1.10/intro-to-django) is a 
  project-based tutorial for beginners that covers the required features
  such as the [Django ORM](/django-orm.html) and 
  [Django Templates](/django-templates.html).

* The [Django subreddit](http://www.reddit.com/r/django) often has links to
  the latest resources for learning Django and is also a good spot to ask 
  questions about it.

* This Django tutorial shows how to 
  [build a project from scratch using Twitter Bootstrap, Bower, Requests and the Github API](http://drksephy.github.io/2015/07/16/django/).

* The [recommended Django project layout](http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/)
  is helpful for developers new to Django to understand how to structure
  the directories and files within apps for projects.

* [Django for Beginners: Build websites with Python and Django](https://www.amazon.com/Django-Beginners-Learn-web-development/dp/1983172669)
  by [William S. Vincent](https://wsvincent.com/) is perfect if you are 
  just getting started with Django and web development, taking you from 
  total beginner to confident web developer with Django and Python.


### Django videos
Are you looking for Django videos in addition to articles? There is a special 
section for Django and web development on the 
[best Python videos](/best-python-videos.html) page.


### Intermediate and advanced Django topics
These books and tutorials assume that you know the basics of building
Django and want to go further to become much more knowledgeable about
the framework.

* [2 Scoops of Django](https://www.twoscoopspress.com/collections/django/products/two-scoops-of-django-1-11)
  by Daniel Greenfeld and Audrey Roy is well worth the price of admission if
  you're serious about learning how to correctly develop Django websites.
  
* The [Test-Driven Development with Django, Django REST Framework, and Docker](https://testdriven.io/courses/tdd-django/?utm_source=fsp)
  course details how to set up a development environment with Docker in
  order to build and deploy a RESTful API powered by Python, Django,
  and Django REST Framework.

* [User Interaction With Forms](https://www.mattlayman.com/understand-django/user-interaction-forms/)
  explains general web form input, how Django handles forms via POST requests,
  different types of input such as CharFields, DateFields and EmailFields,
  and validating that input.

* This 3-part Django project optimization guide covers a wide range of
  advanced topics such as 
  [Profiling and Django settings](https://dizballanze.com/django-project-optimization-part-1/),
  [working with databases](https://dizballanze.com/django-project-optimization-part-2/)
  and [caching](https://dizballanze.com/django-project-optimization-part-3/).

* [Caching in Django](https://testdriven.io/blog/django-caching/) is a detailed
  look at the configuration required for caching and how to measure the 
  performance improvements once you have it in place.

* [Mental Models for Class Based Views](https://djangodeconstructed.com/2020/01/03/mental-models-for-class-based-views/)
  provides some comparison points between class based views (CBVs) and 
  function based views and the author's opinions for how you can better
  understand CBVs.

* Working with time zones is necessary for every web application. This 
  [blog post on pytz and Django](http://tommikaikkonen.github.io/timezones/) is a
  great start for figuring out what you need to know.

* [A Guide to ASGI in Django 3.0 and its Performance](https://arunrocks.com/a-guide-to-asgi-in-django-30-and-its-performance/)
  covers the new Asynchronous Server Gateway Interface (ASGI) that was
  introduced in Django 3.0 and explains some of the nuances and gotchas
  that you should consider if you decide to use it for your web apps.

* [REST APIs with Django: Build powerful web APIs with Python and Django](https://www.amazon.com/dp/198302998X) 
  by [William S. Vincent](https://wsvincent.com/) is the book for you 
  if you are just moving beyond the basics of Django and looking to get 
  up speed with [Django REST Framework (DRF)](/django-rest-framework-drf.html) 
  and service-oriented architecture (SOA). It also dives into more advanced 
  topics like token-based authentication and permissions.

* [Django Stripe Tutorial](https://testdriven.io/django-stripe-tutorial) 
  details how to quickly add Stripe to accept payments in a Django web app.

* This [Python Social Auth for Django tutorial](https://github.com/davisfreeman1015/SocialAuthDjangoTutorial)
  will show you how to integrate social media sign in buttons into your Django
  application.

* [Upgrading Django](http://thosecleverkids.com/thoughts/posts/upgrading-django)
  provides a version-by-version guide for updating your Django projects'
  code.

* The [Django Admin Cookbook](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)
  and 
  [Building Multi Tenant Applications with Django](https://books.agiliq.com/projects/django-multi-tenant/en/latest/)
  are two solid "code recipe-style" free open source books that will teach
  you more about the admin interface as well as building projects that
  will be used by more than a single customer so their data needs to be
  properly separated.

* [How to Create Custom Django Management Commands](https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html)
  explains how to expand the default `manage.py` commands list with your
  own custom commands in your projects. The tutorial has a bunch of great
  examples with expected output to make it easy to follow along and learn
  while you work through the post.

* Luke Plant writes about 
  [his approach to class based views](http://lukeplant.me.uk/blog/posts/my-approach-to-class-based-views/) (CBVs),
  which often provoke heated debate in the Django community for whether they
  are a time saver or "too much magic" for the framework.

* [Django Apps Checklist](https://devchecklists.com/django-apps-checklist/en/)
  gives some good practices rules for building reusable Django apps.


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

* [How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
  presents four main ways to expand upon the built-in `User` model that
  is packaged with Django. This scenario is very common for all but the
  simplest Django projects.

* [Creating a Custom User Model in Django](https://testdriven.io/blog/django-custom-user-model/)
  looks at how to create a custom User model in Django so that an email
  address can be used as the primary user identifier instead of a
  username for authentication.


## Django Channels
Channels are a new mechanism in Django 1.9 provided as a standalone app. 
They may be incorporated into the core framework in 2.0+. Channels provide 
"real-time" full-duplex communication between the browser and the server 
based on [WebSockets](/websockets.html). 
  
* This 
  [tutorial shows how to get started with Django Channels in your project](https://blog.heroku.com/archives/2016/3/17/in_deep_with_django_channels_the_future_of_real_time_apps_in_django).

* The 
  [channels examples repository](https://github.com/andrewgodwin/channels-examples)
  contains a couple of good starter projects such as a live blog and a 
  chat application to use as base code.
  
* The [Developing a Real-Time Taxi App with Django Channels and Angular](https://testdriven.io/courses/real-time-app-with-django-channels-and-angular/?utm_source=fsp)
  course details how to create a ride-sharing app with Django Channels,
  Angular, and Docker. Along the way, you'll learn how to manage
  client/server communication with Django Channels, control flow and
  routing with Angular, and build a RESTful API with Django REST
  Framework.

## Django testing
* [Integrating Front End Tools with Django](https://lincolnloop.com/blog/integrating-front-end-tools-your-django-project/)
  is a good post to read for figuring out how to use [Gulp](http://gulpjs.com/)
  for handling front end tools in development and production Django sites.

* [Django Testing Cheat Sheet](https://www.valentinog.com/blog/testing-django/)
  covers many common scenarios for Django applications such as testing
  POST requests, request headers, authentication, and large numbers of
  model fields in the [Django ORM](/django-orm.html).

* [Getting Started with Django Testing](http://howchoo.com/g/mjkwmtu5zdl/getting-started-with-django-testing)
  will help you stop procrastinating on testing your Django projects if you're
  uncertain where to begin.

* [Testing in Django](https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/)
  provides numerous examples and explanations for how to test your Django
  project's code.

* [Django views automated testing with Selenium](https://medium.com/@unary/django-views-automated-testing-with-selenium-d9df95bdc926)
  gives some example code to get up and running with 
  [Selenium](http://www.seleniumhq.org) browser-based tests.


### Django with JavaScript MVC frameworks
There are resources for JavaScript MVC frameworks such as
[Angular](/angular.html), [React](/react.html) and [Vue.js](/vuejs.html) 
on their respective pages.


### Django ORM tutorials
Django comes with its own custom object-relational mapper (ORM) typically
referred to as "the Django ORM". Learn more about the 
[Django ORM](/django-orm.html) on the its own page and more broadly about
ORMs on the 
[Python object-relational mappers page](/object-relational-mappers-orms.html).


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

* [Storing Django Static and Media Files on Amazon S3](https://testdriven.io/storing-django-static-and-media-files-on-amazon-s3)
  shows how to configure Django to load and serve up static and media files, public and private, via an Amazon S3 bucket.


## Django project templates
Project templates, not to be confused with a 
[template engine](/template-engines.html), generate boilerplate code for
a base Django project plus optional libraries that are often used when 
developing web applications.

* [Caktus Group's Django project template](https://github.com/caktus/django-project-template) 
  is Django 2.2+ ready.

* [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django) is a 
  project template from Daniel Greenfeld, for use with Audrey Roy's 
  [Cookiecutter](https://github.com/audreyr/cookiecutter). The template results
  are Heroku deployment-ready.

* [Two Scoops Django project template](https://github.com/twoscoops/django-twoscoops-project)
  is also from the PyDanny and Audrey Roy. This one provides a quick scaffold
  described in the Two Scoops of Django book.

* [Sugardough](https://github.com/mozilla/sugardough) is a Django project
  template from Mozilla that is compatible with cookiecutter.


## Open source Django example projects
Reading open source code can be useful when you are trying to figure
out how to build your own projects. This is a short list of some
real-world example applications, and many more can be found on the
[Django example projects and code](/django-code-examples.html) page.

* [Browser calls with Django and Twilio](https://www.twilio.com/docs/howto/walkthrough/browser-calls/python/django)
  shows how to build a web app with Django and 
  [Twilio Client](https://www.twilio.com/client) to turn a user's web 
  browser into a full-fledged phone. Pretty awesome!

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

* [Chowist](https://github.com/huangsam/chowist) is a web application
  that replicates core features of Yelp and adds a couple more bells
  and whistles.


## Open source code to learn Django
There are many open source projects that rely on Django.
One of the best ways to learn how to use this framework is to read
how other projects use it in real-world code. This section lists
these code examples by class and method in Django's code base.
