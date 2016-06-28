title: Static Site Generators
category: page
slug: static-site-generator
sortorder: 0416
toc: False
sidebartitle: Static Site Generators
meta: A static site generator combines a markup language with a templating engine to produce HTML files. Learn more on Full Stack Python.


# Static Site Generator
A static website generator combines a markup language, such as Markdown 
or reStructuredText, with a templating engine such as 
[Jinja](http://jinja.pocoo.org/), to produce HTML 
files. The HTML files can be hosted and served by a 
[web server](/web-servers.html) or 
[content delivery network (CDN)](/static-content.html) 
*without* any additional dependencies such as a 
[WSGI server](/wsgi-servers.html).


## Why are static site generators useful?
[Static content files](/static-content.html) such as HTML, CSS and JavaScript 
can be served from a content delivery network (CDN) for high scale and low 
cost. If a statically generated website is hit by high concurrent traffic it 
will be easily served by the CDN without dropped connections. 

For example, when 
[Full Stack Python was on the top of Hacker News](https://news.ycombinator.com/item?id=7985692) 
for a weekend, [GitHub Pages](https://pages.github.com/) was used as a CDN
to serve the site and didn't have any issues even with close to 400 
concurrent connections at a time, as shown in the following Google Analytics 
screenshot captured during that traffic burst.

<img src="/img/hacker-news-traffic.jpg" width="100%" alt="Example of how static websites scale with a CDN based on Full Stack Python on Hacker News front page traffic." class="technical-diagram">


## How do static website generators work?
Static site generators allow a user to create HTML files by writing in a
markup language and coding template files. The static site generator then
combines the markup language and templates to produce HTML. The output HTML 
does not need to be maintained by hand because it is regenerated every time
the markup or templates are modified.

For example, as shown in the diagram below, the Pelican static site 
generator can take in reStructuredText files and Jinja2 template files 
as input then combine them to output a set of static HTML files.

<img src="/img/pelican-flow.jpg" width="100%" alt="Example of how static site generators work with a markup language and templates." class="technical-diagram">


## What's the downside to using static site generators?
The major downside is that code cannot be executed after a site is created. 
You are stuck with the output files so if you're used to building web 
applications with a traditional [web framework](/web-frameworks.html) you'll
have to change your expectations. 

Content that is typically powered by a database, such as comments, sessions 
and user data can only be handled through third party services. For example, 
if you want to have comments on a static website you'd need to 
[embed Disqus's form](https://disqus.com/) and be completely reliant upon
their service.

Many web applications simply cannot be built with only a static site generator.
However, a static website generator can create part of a site that will be
served up by a web server while other pages are handled by the WSGI server. 
If done right, those web applications have the potential to scale better than
if every page is rendered by the WSGI server. The complexity may or may not be
worth it for your specific application.


## Python implementations
Numerous static website generators exist in many different languages. The
ones listed here are primarily coded in Python.

* [Pelican](http://blog.getpelican.com/) 
  ([source code](https://github.com/getpelican/pelican)) 
  is a commonly used Python static website generator which is used to create 
  [Full Stack Python](https://github.com/makaimc/fullstackpython.com). The
  primary templating engine is Jinja and Markdown, reStructuredText and
  AsciiDoc are supported with the default configuration.

* [MkDocs](http://www.mkdocs.org/) 
  ([source code](https://github.com/mkdocs/mkdocs/)) uses a YAML configuration
  file to take Markdown files and an optional theme to output a documentation
  site. The templating engine is Jinja, but a user doesn't have to create her
  own templates unless a custom site is desired at which point it might make
  more sense to use a different static site generator instead.

* [Nikola](https://getnikola.com/) 
  ([source code](https://github.com/getnikola/nikola)) takes in 
  reStructuredText, Markdown or Jupyter (IPython) Notebooks and combines 
  the files with Mako or Jinja2 templates to output static sites. It is 
  compatible with both Python 2.7 and 3.3+. Python 2.7 will be dropped 
  in early 2016 while Python 3.3+ will continue to be supported.

* [Acrylamid](http://posativ.org/acrylamid/) 
  ([source code](https://github.com/posativ/acrylamid)) uses incremental 
  builds to generate static sites faster than recreating every page after
  each change is made to the input files.

* [Hyde](http://hyde.github.io/) 
  ([source code](https://github.com/hyde/hyde)) started out as a Python 
  rewrite of the popular Ruby-based 
  [Jekyll static site generator](http://jekyllrb.com/). Today the project
  has moved past those "clone Jekyll" origins. Hyde supports Jinja as well
  as other templating languages and places more emphasis on metadata within
  the markup files to instruct the generator how to produce the output files.
  Check out the 
  [Hyde-powered websites](https://github.com/hyde/hyde/wiki/Hyde-Powered)
  page to see live examples created with Hyde.

* [Grow SDK](http://growsdk.org/) ([source code](http://growsdk.org/)) 
  uses projects, known as pods, which contain a specific file and directory 
  structure so the site can be generated. The project remains in the
  "experimental" phase.

* [Lektor](https://www.getlektor.com/) 
  ([source code](https://github.com/lektor/lektor)) is a Python static 
  content management system that can deploy to any webserver. It uses 
  [Jinja2](/jinja2.html) as a [template engine](/template-engines.html).

* [Complexity](http://complexity.readthedocs.org/en/latest/)
  ([source code](https://github.com/audreyr/complexity)) is a site generator
  for users who like to work in HTML. It uses HTML for templating but
  has some functionality from Jinja for inheritance. Works with 
  Python 2.6+, 3.3+ and PyPy.

* Cactus ([source code](https://github.com/koenbok/Cactus/)) uses the Django
  templating engine that was originally built with front-end designers in
  mind. It works with both Python 2.x and 3.x.


### Open source Python static site generator examples
* This site is 
  [all open source in its own GitHub repository](https://github.com/makaimc/fullstackpython.com) 
  under the MIT license. Fork away!

* [Django REST Framework](https://github.com/tomchristie/django-rest-framework/tree/master/docs)
  uses MkDocs to create its documentation site. Be sure to take a look at the
  [mkdocs.yml file](https://github.com/tomchristie/django-rest-framework/blob/master/mkdocs.yml)
  to see how large, well-written docs are structured for that project.

* [Practicing web development](https://www.vlent.nl/) uses Acrylamid to create
  its site. The code is 
  [open source on GitHub](https://github.com/markvl/www.vlent.nl).

* [Linux Open Admin Days (Loadsys)](http://loadays.org/) has their 
  [site open source and available for viewing](https://github.com/loadays/pelican-site). 

* The [Pythonic Perambulations](http://jakevdp.github.io/) blog has a fairly
  standard theme but is 
  [also open source on GitHub](https://github.com/jakevdp/PythonicPerambulations).


### Static site generator resources
* [The Long Road to Building a Static Blog with Pelican](http://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html)
  is a fantastic read that really gets into the details throughout the 
  walkthrough. 

* [Staticgen](https://www.staticgen.com/) lists static website generators
  of all programming languages sorted by various attributes such as the
  number of GitHub stars, forks and issues.

* [Static site hosting with S3 and Cloudflare](https://wsvincent.com/static-site-hosting-with-s3-and-cloudflare/)
  shows how to set up an S3 bucket with Cloudflare in front as a CDN that
  serves the content with HTTPS. You should be able to accomplish roughly 
  the same situation with Amazon Cloudfront, but as a Cloudflare user I
  like their service for these static site configurations.

* [Getting Started with Pelican and GitHub Pages](http://www.mattmakai.com/introduction-to-pelican.html)
  is a tutorial I wrote for getting up and running with Full Stack Python's
  source code, which uses Pelican to generate the site.

* The title is a big grandiose, but there's some solid detail in this article
  on 
  [why static website generators are the next big thing](http://www.smashingmagazine.com/2015/11/modern-static-website-generators-next-big-thing/).
  I'd argue static website generators have been big for a long time now.

* Static site generators can be used for a range of websites from side
  projects up to big sites. This blog post by 
  [WeWork on why they use a static site generator](http://engineering.wework.com/engineering/2015/12/08/why-wework-com-uses-a-static-generator-and-why-you-should-too/)
  explains it from the perspective of a large business.

* [Getting started with Pelican and GitHub pages](http://www.mattmakai.com/introduction-to-pelican.html)
  is a tutorial I wrote to use the Full Stack Python source code to create
  and deploy your first static site.

* [Ditching Wordpress and becoming one of the cool kids](http://razius.com/articles/ditching-wordpress-and-becoming-one-of-the-cool-kids/)
  is one developer's experience moving away from Wordpress and onto
  Pelican with reStructuredText for his personal blog.

