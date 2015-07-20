title: Static Site Generator
category: page
slug: static-site-generator
sort-order: 0416
meta: A static site generator combines a markup language with a templating engine to produce HTML files. Learn more on Full Stack Python.


# Static Site Generator
A static website generator combines a markup language, such as Markdown 
or reStructuredText, with a templating engine such as 
[Jinja](http://jinja.pocoo.org/), to produce HTML 
files. The HTML files can be hosted and served by a 
[web server](/web-server.html) or 
[content delivery network (CDN)](/static-content.html) 
without any additional dependencies such as a 
[WSGI server](/wsgi-server.html).


## Why are static site generators useful?
Static site generators allow a user to create HTML files by writing in a
markup language and coding template files. HTML does not need to be 
maintained by hand other than what is in the template files.

For example, as shown in the diagram below, the Pelican static site 
generator can take in reStructuredText files and Jinja2 template files 
as input then combine them to output a set of static HTML files.

<img src="theme/img/pelican-flow.jpg" width="100%" alt="Example of how static site generators work with a markup language and templates." class="technical-diagram"></a>


## Python static site generators
Numerous static website generators exist in many different languages. The
ones listed here are primarily coded in Python.

* [Pelican](http://blog.getpelican.com/) 
  ([source code](https://github.com/getpelican/pelican)) 
  is a commonly used Python static website generator which is used to create 
  [Full Stack Python](https://github.com/makaimc/fullstackpython.com). The
  primary templating engine is Jinja and Markdown, reStructuredText and
  AsciiDoc are supported with the default configuration.

* [Acrylamid](http://posativ.org/acrylamid/) 
  ([source code](https://github.com/posativ/acrylamid)) uses incremental 
  builds to generate static sites faster than recreating every page after
  each change is made to the input files.

* [Grow SDK](http://growsdk.org/) ([source code](http://growsdk.org/)) 
  uses projects, known as pods, which contain a specific file and directory 
  structure so the site can be generated. The project remains in the
  "experimental" phase.


### Static site generator resources
* [The Long Road to Building a Static Blog with Pelican](http://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html)
  is a fantastic read that really gets into the details throughout the 
  walkthrough. 

* [Getting Started with Pelican and GitHub Pages](http://www.mattmakai.com/introduction-to-pelican.html)
  is a tutorial I wrote for getting up and running with Full Stack Python's
  source code, which uses Pelican to genereate the site.

