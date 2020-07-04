title: API Integration
category: page
slug: api-integration
sortorder: 0451
toc: False
sidebartitle: API Integration
meta: Integrating web APIs into an application is necessary for both mobile and web applications. Learn more about API integration on Full Stack Python.


The majority of production Python web applications rely on several
externally hosted application programming interfaces (APIs). APIs are also
commonly referred to as third party services or external platforms. 
Examples include [Twilio](https://www.twilio.com/docs/) for messaging and 
voice services, [Stripe](https://stripe.com/docs/api) for payment processing 
and [Disqus](https://disqus.com/api/docs/) for embedded webpage comments.

There are many articles about proper API design but best practices for 
integrating APIs is less commonly written about. However, this subject 
continuously grows in importance because APIs provide critical functionality
across many implementation areas.


## API Integration Resources
* [APIs for Beginners](https://www.freecodecamp.org/news/apis-for-beginners-full-course/)
  is an awesome free video course that shows how to use APIs and
  add them to applications with a bunch of useful code examples.

* Some developers prefer to use 
  [Requests](https://requests.readthedocs.io/en/master/) instead of an API's 
  helper library. In that case check out this 
  [tutorial on using requests to access web APIs](http://engineering.hackerearth.com/2014/08/21/python-requests-module/).

* [How to Debug Common API Errors](https://blog.runscope.com/posts/how-to-debug-common-api-errors)
  talks about the 1xx through 5xx status codes you will receive when working
  with HTTP requests and what to do when you get some of the more common 
  ones such as 403 Forbidden and 502 Bad Gateway.

* Product Hunt lists many commonly used 
  [commercial and free web APIs](https://www.producthunt.com/e/an-api-for-everything)
  to show "there's an API for everything".

* There's a list of all government web APIs at 
  [18F's API-All-the-X list](http://18f.github.io/API-All-the-X/). The list
  is updated whenever a new API comes online.

* [The Only Type of API Services I'll Use](https://www.rdegges.com/2020/the-only-type-of-api-services-ill-use/)
  explains how alignment between usage and pricing is crucial to a solid,
  long-lasting API experience. Other models such as tiered usage and 
  enterprise upsells typically lead to terrible developer experiences and
  should generally be avoided when building applications with APIs.

* John Sheehan's 
  "[Zen and the Art of API Maintenance](https://speakerdeck.com/johnsheehan/zen-and-the-art-of-api-maintenance)"
  slides are relevant for API integration.

* This post on 
  "[API Driven Development](https://stormpath.com/blog/api-driven-development/)"
  by Randall Degges explains how using APIs in your application cuts down
  on the amount of code you have to write and maintain so you can launch your
  application faster.

* [Retries in Requests](http://www.coglib.com/~icordasc/blog/2014/12/retries-in-requests.html)
  is a nice tutorial for easily re-executing failed HTTP requests with the
  Requests library.

* My DjangoCon 2013 talk dove into 
  "[Making Django Play Nice With Third Party Services](http://www.youtube.com/watch?v=iGP8DQIqxXs)."

* If you're looking for a fun project that uses two web APIs within a 
  Django application, try out this tutorial to 
  [Build your own Pokédex with Django, MMS and PokéAPI](https://www.twilio.com/blog/2014/11/build-your-own-pokedex-with-django-mms-and-pokeapi.html).

* [vcr.py](https://www.brianthicks.com/2014/12/01/test-apis-properly-with-vcr-py/)
  is a way to capture and replay HTTP requests with mocks. It's extremely
  useful for testing API integrations.

* [Caching external API requests](https://realpython.com/blog/python/caching-external-api-requests/)
  is a good post on how to potentially limit the number of HTTP calls 
  required when accessing an external web API via the Requests library.

* [Working with APIs the Pythonic way](https://medium.com/@hakibenita/working-with-apis-the-pythonic-way-484784ed1ce0)
  does a nice job walking through creating a naive web API client, building on
  it with better error handling and then explaining how to test it by mocking
  out the service.


## API integration learning checklist
1. Pick an API known for top notch documentation. Here's a list of 
   [ten APIs that are a good starting point for beginners](https://medium.com/she-hacks-hacker-academy/4d3c43be9386).

1. Read the API documentation for your chosen API. Figure out a simple 
   use case for how your application could be improved by using that API.

1. Before you start writing any code, play around with the API through the 
   commandline with [cURL](http://curl.haxx.se/) or in the browser with 
   [Postman](http://www.getpostman.com/). This exercise will help you get 
   a better understanding of API authentication and the data required for 
   requests and responses.

1. Evaluate whether to use a helper library or work with 
   [Requests](https://requests.readthedocs.io/en/master/). Helper libraries 
   are usually easier to get started with while Requests gives you more 
   control over the HTTP calls.

1. Move your API calls into a [task queue](/task-queues.html) so they do not 
   block the HTTP request-response cycle for your web application.

