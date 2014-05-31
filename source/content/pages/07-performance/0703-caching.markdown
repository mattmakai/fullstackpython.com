title: Caching
category: page
slug: caching
sort-order: 072
choice1url: /task-queues.html
choice1icon: fa-tasks
choice1text: How do I run Python outside the HTTP request-response cycle?
choice2url: /web-analytics.html
choice2icon: fa-dashboard
choice2text: What can I learn about my users through web analytics?
choice3url: /web-application-security.html
choice3icon: fa-lock fa-inverse
choice3text: What should I know about security to protect my app?
choice4url: /configuration-management.html
choice4icon: fa-gears fa-inverse
choice4text: How do I automate the server configuration that I set up?


# Caching
Caching can reduce the load on servers by storing the results of common 
operations and serving the precomputed answers to clients. 

For example, instead of retrieving data from database tables that rarely 
change, you can store the values in-memory. Retrieving values from an 
in-memory location is far faster than retrieving them from a database (which
stores them on a persistent disk like a hard drive.) When the cached values 
change the system can invalidate the cache and re-retrieve the updated values
for future requests.

A cache can be created for multiple layers of the stack. 


## Caching backends
* [memcached](http://memcached.org/) is a common in-memory caching system.

* [Redis](http://redis.io/) is a key-value in-memory data store that can
  easily be configured for caching with libraries such as 
  [django-redis-cache](https://github.com/sebleier/django-redis-cache).


## Caching resources
* "[Caching: Varnish or Nginx?](https://bjornjohansen.no/caching-varnish-or-nginx)"
  reviews some considerations such as SSL and SPDY support when choosing
  reverse proxy Nginx or Varnish.

* [Caching is Hard, Draw me a Picture](http://bizcoder.com/caching-is-hard-draw-me-a-picture)
  has diagrams of how web request caching layers work. The post is relevant
  reading even though the author is describing his Microsoft code as the 
  impetus for writing the content.


## Caching learning checklist
<i class="fa fa-check-square-o"></i>
Analyze your web application for the slowest parts. It's likely there are
complex database queries that can be precomputed and stored in an in-memory
data store.

<i class="fa fa-check-square-o"></i>
Leverage your existing in-memory data store already used for session data
to cache the results of those complex database queries. 
A [task queue](/task-queues.html) can often be used to precompute the results 
on a regular basis and save them in the data store.

<i class="fa fa-check-square-o"></i>
Incorporate a cache invalidation scheme so the precomputed results remain 
accurate when served up to the user.



### What do you want to learn now that your app is responding faster?
