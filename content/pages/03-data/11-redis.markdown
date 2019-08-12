title: Redis
category: page
slug: redis
sortorder: 0311
toc: False
sidebartitle: Redis
meta: Redis is an in-memory key-value pair data store classified as a NoSQL database and used with Python applications.


<a href="https://redis.io/">Redis</a> is an in-memory key-value pair 
database typically classified as a [NoSQL database](/no-sql-datastore.html). 
Redis is commonly used for [caching](/caching.html), transient data storage
and as a holding area for data during analysis in Python applications.

<a href="https://redis.io/" style="border: none;"><img src="/img/logos/redis.jpg" width="100%" alt="Redis logo." class="shot" /></a>

<div class="well see-also">Redis is an implementation of the <a href="/no-sql-datastore.html">NoSQL database</a> concept. Learn more in the <a href="/data.html">data</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div> 


### Redis tutorials
Redis is easy to install and start using compared to most other persistent
backends, but it's useful to follow a walkthrough if you have never 
previously used Redis or any NoSQL data store.

* [How to Use Redis with Python 3 and redis-py on Ubuntu 16.04](/blog/install-redis-use-python-3-ubuntu-1604.html)
  contains detailed steps to install and start using Redis in Python.

* [How To Install and Use Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis)
  is a straightforward starter guide that includes installation instructions.


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

* [Write your own miniature Redis with Python](http://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)
  doesn't actually use Redis but shows how you can write a simplified
  version of Redis' in-memory data store with Python. It's a good article
  to understand more about how NoSQL data stores can work under the covers.

* [Introduction to Redis streams with Python](http://charlesleifer.com/blog/redis-streams-with-python/)
  shows how to use the new (as of Redis version 5.0) append-only streams 
  functionality via Python code.


### Redis tools and examples
Redis' wide applicability can be a downside if you don't know what to start
using it for in your application. The following code and posts provide common
use cases for Redis.

* [redis-labs-use-cases](https://github.com/Altoros/redis-labs-use-cases)
  has a couple of examples of using Redis to analyze geospatial data and
  tweets.

* [redis-migrate-tool](https://github.com/vipshop/redis-migrate-tool)
  is a library to make it easier to move data between redis clusters
  and groups.

* [redis-rdb-tools](https://github.com/sripathikrishnan/redis-rdb-tools)
  parses the Redis' database storage files and can dump the contents to
  JSON files.


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

* [For God’s sake, secure your Mongo/Redis/etc!](https://medium.com/@shahinism/for-gods-sake-secure-your-mongo-redis-etc-4f310cf1bed2)
  digs into the unfortunate default security settings that come with many
  NoSQL databases which can be used to compromise your systems. Make sure
  to not only install your dependencies such as Redis, but automate modifying
  default settings to lock them down against attackers.


### Specific Redis topics
Once you have configured Redis, become comfortable using it and locked it
down against malicious actors, you will want to learn more about operating,
scaling and collecting metrics. The following resources should help you
get started in those areas.

* [A Key Expired In Redis, You Won't Believe What Happened Next](https://engineering.grab.com/a-key-expired-in-redis-you-wont-believe-what-happened-next)
  is a well-written post on issues one team found with their configuration
  when they were using Redis for a lot of data caching.

* [Redis-playbook](https://github.com/mikeblum/redis-playbook) is an Ansible
  playbook for installing, configuring and securing a Redis instance.

* [Monitoring Redis](http://www.mikeperham.com/2017/04/20/monitoring-redis/)
  shows common commands for accessing meta data about your Redis databases,
  such as `info` and `slowlog`.

* GitHub wrote a retrospective on 
  [moving persistent data out of Redis](http://githubengineering.com/moving-persistent-data-out-of-redis/)
  and into [MySQL](/mysql.html) that is worth a read as you scale up your
  Redis usage.

* [Learn Redis the hard way (in production)](https://tech.trivago.com/2017/01/25/learn-redis-the-hard-way-in-production/)
  investigates problems found with a development team's Redis 
  infrastructure, how they went about debugging them and ultimately fixing
  some of the issues, while being aware of limitations that could cause
  them issues in the future.

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

* [Better tests for Redis integrations with redislite](https://www.obeythetestinggoat.com/better-tests-for-redis-integrations-with-redislite.html)
  shows how to mock out a Redis instance using the 
  [redislite](https://github.com/yahoo/redislite) library and clean up
  existing hacks you may be using to test your Redis usage.

* [Our journey from Redis 2 to Redis 3 while not taking the site down](https://engineering.skybettingandgaming.com/2017/09/25/redis-2-to-redis-3/)
  explains their infrastructure and uptime demands in the gambling industry,
  and how they were able to roll their upgraded Redis versions.
