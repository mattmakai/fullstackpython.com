title: Caching
category: page
slug: caching
sortorder: 0718
toc: False
sidebartitle: Caching
meta: Caching reduces load on servers by pre-calculating the results of common operations. Learn more about caching on Full Stack Python.


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

* While caching is a useful technique in many situations, it's important
  to also note that there are 
  [downsides to caching](https://msol.io/blog/tech/2015/09/05/youre-probably-wrong-about-caching/)
  that many developers fail to take into consideration.


## Caching learning checklist
1. Analyze your web application for the slowest parts. It's likely there are
   complex database queries that can be precomputed and stored in an in-memory
   data store.

1. Leverage your existing in-memory data store already used for session data
   to cache the results of those complex database queries. A 
   [task queue](/task-queues.html) can often be used to precompute the results 
   on a regular basis and save them in the data store.

1. Incorporate a cache invalidation scheme so the precomputed results remain 
   accurate when served up to the user.

