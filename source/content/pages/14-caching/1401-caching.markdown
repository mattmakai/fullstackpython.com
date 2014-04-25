title: Caching
category: page
slug: caching
sort-order: 14

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


### What do you want to learn now that your app is responding faster?
