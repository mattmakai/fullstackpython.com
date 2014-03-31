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


## Caching Resources
[memcached](http://memcached.org/) is a common in-memory caching system.

[Redis](http://redis.io/) is a key-value in-memory data store that can
easily be configured for caching with libraries such as 
[django-redis-cache](https://github.com/sebleier/django-redis-cache).

