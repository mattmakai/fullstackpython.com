title: Lektor
category: page
slug: lektor
sortorder: 0433
toc: False
sidebartitle: Lektor
meta: Lektor is a static website generator with content management system (CMS) and web framework features for creating websites.


[Lektor](https://www.getlektor.com/) is a static website generator with 
content management system (CMS) and [web framework](/web-frameworks.html) 
features for creating websites. 

Lektor's
[source code is available on GitHub](https://github.com/lektor/lektor) 
under the 
[BSD 3-clause license](https://opensource.org/licenses/BSD-3-Clause).

<a href="https://www.getlektor.com/"><img src="/img/logos/lektor.jpg" width="100%" alt="Lektor static website generator logo." class="shot rnd outl"></a>


## How is Lektor different from other static site generators?
Most static site generators such as [Pelican](/pelican.html) are built with
programmers as the primary user. Lektor tries to be more accessible to
non-programmers by providing an admin panel for creating and updating
site content similar to Django or Wordpress.

<div class="well see-also">Lektor is an implementation of the <a href="/static-site-generator.html">static site generators</a> concept. Learn how the parts fit together in the <a href="/web-development.html">web development</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


### Lektor example projects
* [PyCon Colombia's 2018 site](https://github.com/PyConColombia/website-2018)
  was built with Lektor and is freely available on GitHub.

* [freedombox.org](https://github.com/freedombox/freedombox.org) is also
  available for reference.


### Lektor resources
Lektor is a young project and therefore has a nascent community compared with
[Pelican](/pelican.html) and Jekyll (the most popular Ruby-based static 
site generator). However, the official documentation and initial quickstarts 
for the project are wonderful so getting a basic site up and running is 
painless.

* [Introducing Lektor](http://lucumr.pocoo.org/2015/12/21/introducing-lektor/)
  is the background story for what motivated 
  [Armin Ronacher](https://github.com/mitsuhiko) to start hacking on his own
  static site generator project after jumping around from Django to Wordpress
  for hosting content. The post also includes details on the differences 
  in the project compared to other static site generators.

* [Hello, Lektor](https://zerokspot.com/weblog/2016/09/16/hello-lektor/) is
  a wonderful getting started and overview post. The post walks through the
  files Lektor generates, the admin content management system and pulling
  data into pages from the Meetup API.

* The [official Lektor quickstart](https://www.getlektor.com/docs/quickstart/)
  contains the first commands to use to generate a new project scaffold.
  There is also a getting started screencast that walks through installing
  and initial steps for getting set up with the project.

* [Lektor Static CMS, put the fun back into Content Management](https://blog.liip.ch/archive/2016/09/21/lektor-static-cms-put-fun-back-content-management.html)
  is a short overview as the first part in what aims to be a continuing
  series on how to use Lektor as a content management system.

* In 
  [Experiences Migrating to Lektor](https://emptysqua.re/blog/experience-migrating-to-lektor/)
  the author gives his impression of Lektor after moving his 400+ articles
  over from a home-grown blogging engine. He talks a bit about how he went
  from deploying on GitHub Pages to surge.sh and finally over to Netlify.

* [Automating deployment of Lektor blog sites](http://blog.dscpl.com.au/2016/01/automating-deployment-of-lektor-blog.html)
  covers using OpenShift to deploy a static site. Seems like a lot of work
  when [AWS S3](https://aws.amazon.com/s3/) deployments are a lot easier but 
  OpenShift has its own ecosystem to keep you away from AWS world if that's 
  your thing.
