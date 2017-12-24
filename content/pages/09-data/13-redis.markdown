title: Redis
category: page
slug: redis
sortorder: 0913
toc: False
sidebartitle: Redis
meta: Redis is an in-memory key-value pair data store classified as a NoSQL database and used with Python applications.


# Redis
<a href="https://redis.io/">Redis</a> is an in-memory key-value pair 
database typically classified as a [NoSQL database](/no-sql-datastore.html). 
Redis is commonly used for [caching](/caching.html), transient data storage
and as a holding area for data during analysis in Python applications.

<a href="https://redis.io/" style="border: none;"><img src="/img/logos/redis.jpg" width="100%" alt="Redis logo." class="technical-diagram" /></a>

<div class="well see-also">Redis is an implementation of the <a href="/no-sql-datastore.html">NoSQL database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### Redis tutorials
Redis is easy to install and start using compared to most other persistent
backends, but it's useful to follow a walkthrough if you have never 
previously used Redis or any NoSQL data store.

* [How to Use Redis with Python 3 and redis-py on Ubuntu 16.04](/blog/install-redis-use-python-3-ubuntu-1604.html)
  contains detailed steps to install and start using Redis in Python.

* [How To Install and Use Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis)
  is a Redis starter guide.


### Redis with Python
Redis is easier to use with Python if you have a code library client that
bridges from your code to your Redis instace. The following libraries and
resources provide more information on handling data in a Redis instance
with your Python code.

* [Redis-py](https://github.com/andymccurdy/redis-py) is a solid
  Python client to use with Redis.

* [Walrus](http://charlesleifer.com/blog/walrus-lightweight-python-utilities-for-working-with-redis/)
  is a higher-level Python wrapper for Redis with some caching, querying
  and data structure components build into the library.

* [Writing Redis in Python with Asyncio](http://jamesls.com/writing-redis-in-python-with-asyncio-part-1.html)
  shows a detailed example for how to use the new Asyncio standard library in
  Python 3.4+ for working with Redis. There is also a 
  [EuroPython video of the talk](https://www.youtube.com/watch?v=CF8zt8l6SeI) 
  that goes along with the code.

* [Cache_deco](https://github.com/alexk307/cache_deco) is a generic Python
  caching decorator library.


### Redis examples
Redis' wide applicability can be a downside if you don't know what to start
using it for in your application. The following code and posts provide common
use cases for Redis.

* [redis-labs-use-cases](https://github.com/Altoros/redis-labs-use-cases)
  has a couple of examples of using Redis to analyze geospatial data and
  tweets.


### Redis Security
Redis should be customized out of its default configuration to secure it
against unauthorized and unauthenticated users. These resources provide
some advice on Reids security and guarding against data breaches.

* [Pentesting Redis servers](http://averagesecurityguy.info/2015/09/17/pentesting-redis-servers/)
  shows that security is important not only on your application but also
  the databases you're using as well.

* Redis, just as with any relational or NoSQL database, needs to be secured
  based on [security guidelines](http://www.antirez.com/news/96). There is
  also a post where the main author of Redis
  [cracks its security](http://www.antirez.com/news/96) to show the tradeoffs
  purposely made between ease of use and security in the default settings.

* [Is your Redis server safe?](https://www.isredisallsafe.com/) is a tool
  to test that your Redis instances are locked down. The tool is based on
  the blog post
  [a few things about Redis security](http://www.antirez.com/news/96).

* [For God’s sake, secure your Mongo/Redis/etc!](https://medium.com/@shahinism/for-gods-sake-secure-your-mongo-redis-etc-4f310cf1bed2)
  digs into the unfortunate default security settings that come with many
  NoSQL databases which can be used to compromise your systems. Make sure
  to not only install your dependencies such as Redis, but automate modifying
  default settings to lock them down against attackers.


### General Redis resources
Once you have configured Redis, become comfortable using it and locked it
down against malicious actors, you will want to learn more about operating,
scaling and collecting metrics. The following resources should help you
get started in those areas.

* [Redis-playbook](https://github.com/mikeblum/redis-playbook) is an Ansible
  playbook for installing, configuring and securing a Redis instance.

* GitHub wrote a retrospective on 
  [moving persistent data out of Redis](http://githubengineering.com/moving-persistent-data-out-of-redis/)
  and into [MySQL](/mysql.html) that is worth a read as you scale up your
  Redis usage.

* This video on
  [Scaling Redis at Twitter](https://www.youtube.com/watch?v=rP9EKvWt0zo) is
  a detailed look behind the scenes with a massive Redis deployment.

* [Real World Redis Tips](https://blog.heroku.com/real-world-redis-tips)
  provides some guidance from Heroku's engineers from deploying Redis at
  scale. The tips include setting an explicit idle connection timeout,
  using a connection pooler and avoiding using `KEYS` in favor of `SCAN`.

* [How to collect Redis metrics](https://www.datadoghq.com/blog/how-to-collect-redis-metrics/)
  shows how to use the Redis CLI client to grab key metrics on latency.

* [You should revise your Redis max connections setting](https://medium.com/appaloosa-store-engineering/you-should-revise-your-redis-max-connections-setting-8136f063c916)
  is a retrospective from a hard web application failure due to Redis
  connections maxing out on Heroku, and how to avoid this in your own
  applications by modifying your `redis.conf` settings.

* [A Speed Guide To Redis Lua Scripting](https://www.compose.com/articles/a-quick-guide-to-redis-lua-scripting/)
  shows how to use the Lua programming language to create extensions
  for Redis.
