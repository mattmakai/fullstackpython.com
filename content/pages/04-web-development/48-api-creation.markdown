title: API Creation
category: page
slug: api-creation
sortorder: 0448
toc: False
sidebartitle: API Creation
meta: Web APIs enable machine-to-machine communication. Learn more about creating web APIs on Full Stack Python.


Creating and exposing APIs allows your web application to interact with other
applications through machine-to-machine communication.


## API creation frameworks
* [Django REST framework](http://www.django-rest-framework.org/) and
  [Tastypie](https://django-tastypie.readthedocs.org/en/latest/) are 
  the two most widely used API frameworks to use with Django. The edge
  currently goes to Django REST framework based on rough community sentiment.
  Django REST framework continues to knock out great releases after the
  3.0 release mark when Tom Christie ran a 
  [successful Kickstarter campaign](https://www.kickstarter.com/projects/tomchristie/django-rest-framework-3).

* [Flask-RESTful](http://flask-restful.readthedocs.org/en/latest/) is
  widely used for creating web APIs with Flask. It was originally 
  open sourced by [Twilio](https://www.twilio.com/) then moved into its
  [own GitHub organization](https://github.com/flask-restful/flask-restful)
  so engineers from outside the company could be core contributors.

* [Sandman](http://www.github.com/jeffknupp/sandman) is a widely used tool to
  automatically generate a RESTful API service from a legacy database without
  writing a line of code (though it's easily extensible through code).

* [Cornice](https://cornice.readthedocs.org/en/latest/) is a REST framework
  for Pyramid.

* [Restless](https://github.com/toastdriven/restless) is a lightweight API
  framework that aims to be framework agnostic. The general concept is that
  you can use the same API code for Django, Flask, Bottle, Pyramid or any
  other WSGI framework with minimal porting effort.

* [Eve](http://python-eve.org/) is a Python REST framework built with Flask,
  MongoDB and Redis. The framework's primary author 
  [Nicola Iarocci](https://twitter.com/nicolaiarocci) gave a great talk at 
  [EuroPython 2014](https://www.youtube.com/watch?v=9sUsLvG72_o) that 
  introduced the main features of the framework.

* [Falcon](https://falconframework.org/) is a fast and lightweight framework
  well suited for creating RESTful APIs. 

* [Hug](https://github.com/timothycrosley/hug) built on-top of Falcon and Python3 with an aim to make developing Python driven APIs as simple as possible, but no simpler. Hug leverages Python3 annotations to automatically validate and convert incoming and outgoing API parameters.

* [Pycnic](http://pycnic.nullism.com) is a JSON-API-only framework designed 
  with REST in mind. 


## API testing projects
Building, running and maintaining APIs requires as much effort as building,
running and maintaining a web application. API testing frameworks are the 
equivalent of browser testing in the web application world.

* [zato-apitest](https://github.com/zatosource/zato-apitest) invokes HTTP 
  APIs and provides hooks for running through other testing frameworks.

* [Tavern](https://taverntesting.github.io/) is a pytest plugin for 
  automated API testing.


### Hosted API testing services
* [Runscope](https://www.runscope.com/) is an API testing SaaS application
  that can test both your own APIs and external APIs that your application
  relies upon.

* [API Science](https://www.apiscience.com/) is focused on deep API testing,
  including multi-step API calls and monitoring of external APIs.


### API creation resources
* [An API is only as good as its documentation](https://rocketeer.be/blog/2015/03/api-quality/)
  is a strongly held mantra in the web API world because so many APIs have
  poor documentation that prevents ease-of-use. If an API is not well 
  documented then developers who have options to use something else will
  just skip it.

* [8 Open-Source Frameworks for Building APIs in Python](https://nordicapis.com/8-open-source-frameworks-for-building-apis-in-python/)
  presents a high-level overview of the options for building APIs in
  Python.

* [Adventures in running a free, public API](http://www.cambus.net/adventures-in-running-a-free-public-api/)
  is a quick story of a developer's geolocation API being abused and his 
  lack of resources for preventing further abuse. Eventually he had to shut
  down the free plan and only provide a paid plan in addition to allowing
  others to host the open source code. Fraud and malware prevention are 
  difficult problems so keep an eye on server utilization and endpoint calls 
  growth to separate legitimate from illegitimate traffic. 

* [API versioning](https://stripe.com/blog/api-versioning) is a wonderful
  article on the tradeoffs between including an API version in the URL
  compared to other common ways to version APIs.

* [API Doc JS](http://apidocjs.com/) allows a developer to embed markup
  in their documentation that will generate a site based on the endpoints
  available in the API.

* [10 Reasons Why Developers Hate Your API (And what to do about it)](http://www.slideshare.net/jmusser/ten-reasons-developershateyourapi)
  goes through the top difficulties and annoyances developers face when
  working with APIs and how you can avoid your API falling into the same
  traps.

* Versioning of RESTful APIs is a difficult and contentious topic in the 
  web API community. This two-part series covers 
  [various ways to version your API](http://urthen.github.io/2013/05/09/ways-to-version-your-api/) 
  and [how to architect a version-less API](http://urthen.github.io/2013/05/16/ways-to-version-your-api-part-2/).

* [NARWHL](http://www.narwhl.com/) is a practical API design site for 
  developers confused about what is appropriate for RESTful APIs.

* [18F](https://18f.gsa.gov/)'s 
  [API standards](https://github.com/18f/api-standards) explains the details
  behind their design decisions on creating modern RESTful APIs.

* [Design a beautiful REST API](https://medium.com/@zwacky/design-a-beautiful-rest-api-901c73489458)
  reviews common design decisions regarding endpoints, versioning, errors and
  pagination. There is also a 
  [source material YouTube video](https://www.youtube.com/watch?v=5WXYw4J4QOU)
  where this blog post derives its recommendations from.

* [Move Fast, Don't Break Your API](http://amberonrails.com/move-fast-dont-break-your-api/)
  are slides and a detailed blog post from Amber Feng at Stripe about 
  building an API, separating layers of responsibility, hiding backwards
  compatibility and a whole slew of other great advice for developers
  and API designers.

* [Designing the Artsy API](http://artsy.github.io/blog/2014/09/12/designing-the-public-artsy-api/)
  has their recommendations list for building an API based on their 
  experiences.

* Hacker News had a discussion on 
  [what's the best way to write an API spec?](https://news.ycombinator.com/item?id=8912897)
  that provides a few different viewpoints on this topic.

* [Apigee's Web API Design ebook](https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf)
  is free and contains a wealth of practical advice for what design
  decisions to make for your web API.

* [Documenting APIs: A guide for technical writers and engineers](https://idratherbewriting.com/learnapidoc/)
  is a guide that covers good practices for thinking like a developer who
  will use your API, as well as what the documentation for endpoints
  and other important pieces should look like.

* [How many status codes does your API need?](https://blogs.dropbox.com/developers/2015/04/how-many-http-status-codes-should-your-api-use/)
  gives an answer from a Dropbox API developer as to their decision making
  process.

* These two Stack Overflow questions and answers on 
  [Is it better to place a REST API on a subdomain or in a subfolder?](http://stackoverflow.com/questions/14554943/is-it-better-to-place-a-rest-api-on-a-subdomain-or-in-a-subfolder) 
  and
  [subdomain vs. subdirectory in web programming](http://stackoverflow.com/questions/1965609/subdomain-vs-subdirectory-in-web-programming)
  provide reasons and opinions on the debate around using a subdomain,
  for example api.fullstackpython.com versus www.fullstackpython.com/api/.
  There is also a nice summary of endpoint configurations in 
  [this article from ProgrammableWeb](http://www.programmableweb.com/news/api-endpoint-versioning-methods-sub-domain-or-directory/2013/08/21).

* This [API Design Guide](https://github.com/interagent/http-api-design) 
  is based on Heroku's best practices for the platform's API.


### Python-specific API creation resources
* [Deploying a Machine Learning Model as a REST API](https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166)

* [Choosing an API framework for Django](https://www.pydanny.com/choosing-api-framework-for-django.html)
  by [PyDanny](https://twitter.com/pydanny) contains questions and insight
  into what makes a good API framework and which one you should currently
  choose for Django.

* [Creating Web APIs with Python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
  is a free book on building APIs with [Flask](/flask.html) as the
  core [web framework](/web-frameworks.html).

* [RESTful web services with Python](http://www.slideshare.net/Solution4Future/python-restful-webservices-with-python-flask-and-django-solutions)
  is an interesting overview of the Python API frameworks space.

* [Implementing a RESTful Web API with Python & Flask](http://blog.luisrei.com/articles/flaskrest.html)
  is a good walkthrough for coding a Flask app that provides standard 
  web API functionality such as proper HTTP responses, authentication
  and logging.

* [REST Hooks](http://resthooks.org/) is an open source Python project that 
  makes it easier to implement subscription-based "REST hooks". These REST
  hooks are similar to webhooks, but provide a different mechanism for 
  subscribing to updates via a REST interface. Both REST hooks and webhooks
  are far more efficient than polling for updates and notifications.

* [Rate limiters](https://stripe.com/blog/rate-limiters) provides a great
  overview of how limiting access in both the number of requests per
  second as well as the number of concurrent open connections can help
  keep your API alive during times of heavy traffic.

* [Writing HTTP files to test HTTP APIs](https://renato.athaydes.com/posts/writing-http-files-for-testing.html)
  shows how to perform automated testing of APIs using HTTP file formats
  provided by 
  [VS Code REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) 
  and the 
  [JetBrains HTTP Client Editor](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html).

* Serialization is common for transforming objects into web API JSON
  results. One company found the serialization performance of Django REST 
  framework was lacking so they created 
  [Serpy](https://github.com/clarkduvall/serpy) and 
  [wrote a blog post with the results of its performance](https://engineering.betterworks.com/2015/09/04/ditching-django-rest-framework-serializers-for-serpy/).

* Microsoft's 
  [REST API Guidelines](https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md)
  are a detailed set of considerations for when you are building your own
  APIs that you want to be easily-consumable by other developers.

* [Designing Good Static REST API Documentation](https://www.moesif.com/blog/technical/documentation/Designing-Good-Static-REST-API-Documentation/)
  is about documentation not APIs themselves, but it covers a critical topic
  if you want your API to succeed: how to use the damn thing.

* [Building better API docs](https://engineering.gosquared.com/building-better-api-docs)
  shows how Square used Swagger with React to create more helpful docs.

* [Best Practices For Creating Useful API Documentation](https://nordicapis.com/best-practices-for-creating-useful-api-documentation/)
  covers standard but important topics such as knowing your audience, 
  ensuring your documentation covers the error codes, and providing
  a changelog as well as terms of service.


## Django REST Framework resources
* This multi-part series on 
  [getting started with Django REST framework and AngularJS (part 1)](http://engineroom.trackmaven.com/blog/getting-started-drf-angularjs-part-1/)
  along with its [second part](http://engineroom.trackmaven.com/blog/getting-started-drf-angularjs-part-2/)
  do a good job of showing how a RESTful API can serve as the backend for
  a client front end built with a JavaScript MVC framework.

* If you're looking for a working example of a Django REST 
  framework project, check out the 
  [PokeAPI](https://github.com/phalt/pokeapi), open sourced under the BSD 
  license.


## API creation learning checklist
1. Pick an API framework appropriate for your web framework. For Django I 
   recommend Django REST framework and for Flask I recommend Flask-RESTful.

1. Begin by building out a simple use case for the API. Generally the use 
   case will either involve data that users want in a machine-readable 
   format or a backend for alternative clients such as an iOS or Android 
   mobile app.

1. Add an authentication mechanism through OAuth or a token scheme.

1. Add rate limiting to the API if data usage volume could be a performance 
   issue. Also add basic metrics so you can determine how often the API is 
   being accessed and whether it is performing properly.

1. Provide ample documentation and a walkthrough for how the API can be 
   accessed and used.

1. Figure out other use cases and expand based on what you learned with the 
   initial API use case.

