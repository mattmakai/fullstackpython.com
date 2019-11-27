title: Django REST Framework
category: page
slug: django-rest-framework-drf
sortorder: 0450
toc: False
sidebartitle: Django REST Framework
meta: Django REST Framework (DRF) is a Python library for building web application programming interfaces (APIs).


[Django REST Framework](http://www.django-rest-framework.org/)
([source code](https://github.com/encode/django-rest-framework)), 
typically abbreviated "DRF", is a Python library for building web
[application programming interfaces (APIs)](/application-programming-interfaces.html).

<a href="http://www.django-rest-framework.org/" style="border:none"><img src="/img/logos/django-rest-framework.png" width="100%" alt="Django REST Framework logo." class="shot rnd" style="padding: 10px 0 10px 0"></a>


### Django REST Framework resources
* [How to Developer APIs with Django REST Framework](https://djangostars.com/blog/rest-apis-django-development/)
  covers the steps for creating a development environment for your Django+DRF
  project then creating API endpoints with the test-driven development (TDD)
  approach.

* The 
  [official DRF tutorial](http://www.django-rest-framework.org/tutorial/quickstart/)
  is one of the best first-party pieces of documentation on any open source
  project. The 
  [rest of the DRF docs are spectacular as well](http://www.django-rest-framework.org/).

* [Django: Building REST APIs](http://polyglot.ninja/django-building-rest-apis/)
  is the first part in an excellent multi-part series on DRF:

    * [Getting started with DRF](http://polyglot.ninja/django-rest-framework-getting-started/)
    * [Serializers](http://polyglot.ninja/django-rest-framework-serializers/)
    * [ModelSerializer and Generic Views](http://polyglot.ninja/django-rest-framework-modelserializer-generic-views/)
    * [ViewSet, ModelViewSet and Router](http://polyglot.ninja/django-rest-framework-viewset-modelviewset-router/)
    * [Authentication and Permissions](http://polyglot.ninja/django-rest-framework-authentication-permissions/)
    * [JSON Web Tokens (JWT)](http://polyglot.ninja/django-rest-framework-json-web-tokens-jwt/)

* [How to optimize your Django REST Viewsets](http://concisecoder.io/2018/12/23/how-to-optimize-your-django-rest-viewsets/)
  provides a good step-by-step example about using `select_related` and 
  `prefetch_related` in the [Django ORM](/django-orm.html) layer to avoid
  large numbers of unnecessary queries in your views. Also, props to the
  author for wearing a UVA t-shirt in his picture when his blog says he
  works as a developer in Blacksburg, Virginia (where Virginia Tech is 
  located).

* [How to Save Extra Data to a Django REST Framework Serializer](https://simpleisbetterthancomplex.com/tutorial/2019/04/07/how-to-save-extra-data-to-a-django-rest-framework-serializer.html)
  is a concise, handy tutorial for combining additional data
  with the already-defined DRF serializer fields before saving 
  everything to a database or similar action.

* [Django polls api using Django REST Framework](https://www.agiliq.com/blog/2019/04/drf-polls/)
  gives a great walkthrough for creating a question polling application 
  backend with code and the explanation as you build it.

* [Django REST Framework Permissions in Depth](https://nezhar.com/blog/django-rest-framework-permissions-in-depth/)
  has code examples and explains permission classes versus authentication
  classes in DRF.

* [Optimizing slow Django REST Framework performance](https://ses4j.github.io/2015/11/23/optimizing-slow-django-rest-framework-performance/)

* [TLT: Serializing Authenticated User Data With Django REST Framework](http://gregblogs.com/tlt-serializing-authenticated-user-data-with-django-rest-framework/)

* [Building an API with Django REST Framework and Class-Based Views](https://codeburst.io/building-an-api-with-django-rest-framework-and-class-based-views-75b369b30396)

* [Simple Nested API Using Django REST Framework](https://blog.apptension.com/2017/09/13/rest-api-using-django-rest-framework/)

* [Building APIs with Django and Django Rest Framework](https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/)


