title: Generating Static Websites with Pelican, Jinja2 and Markdown
slug: generating-static-websites-pelican-jinja2-markdown
meta: Learn how to generate static websites with Python, the Pelican static site generator, Jinja2 and Markdown.
category: post
date: 2017-05-31
modified: 2017-05-31
headerimage: /img/170531-static-sites-pelican/header.jpg
headeralt: Pelican, Jinja2 and Markdown logos.


[Pelican](/pelican.html) is an incredibly well-built Python tool for 
[generating static sites](/static-site-generator.html). 

[Full Stack Python](https://www.fullstackpython.com/) is built with Pelican, 
[Jinja2 templates](/jinja2.html) and [Markdown](/markdown.html).
This site is deployed to Amazon S3 and currently handles over one hundred 
thousand readers per month. There are never scaling concerns because a static
site is pre-generated before deployment and a web server simply responds
with existing files rather than executing any code on the server during
the HTTP request-response cycle.

In this tutorial you will learn how to create a basic static site that you
can further customize and expand with your own design and content.


## Our Tools
This tutorial will with with either [Python 2 or 3](/python-2-or-3.html), 
but Python 3 is strongly recommended for new applications. I used
[Python 3.6.1](https://www.python.org/downloads/release/python-361/) to 
write this post. In addition to Python, throughout this tutorial we 
will also use the following 
[application dependencies](/application-dependencies.html): 

* [pelican](/pelican.html) 
  [static site generator](/static-site-generator.html), 
  [version 3.7.1](https://github.com/getpelican/pelican/releases/tag/3.7.1)
* [markdown](/markdown.html) parsing library to handle Markdown as a content 
  input format, version 
  [2.6.8](https://github.com/waylan/Python-Markdown/releases/tag/2.6.8-final)
* [jinja2](/jinja2.html), a Python [template engine](/template-engines.html), 
  version [2.9.6](https://github.com/pallets/jinja/releases/tag/2.9.6)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/), which come
  packaged with Python 3, to install and isolate the Pelican, Markdown,
  and Jinja2 libraries from any of your other Python projects

If you need help getting your 
[development environment](/development-environments.html) configured, take a 
look at
[this guide for setting up Python 3 and Flask on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)

All code in this blog post is available open source under the MIT license 
on GitHub under the 
[generating-static-websites-pelican-jinja2-markdown directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples). 
Use and abuse the source code as you like for your own applications.


## Install the Pelican and Markdown libraries
Start by creating a new virtual environment for your project.

```bash
python3 -m venv 
```
 
<img src="/img/170531-static-sites-pelican/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Create and activate the Python virtual environment.">

Install the appropriate dependencies after your virtualenv is activated. 
The text `(staticsite)` should be prepended to your command prompt. Install
the Pelican and Markdown Python libraries. Jinja2 will also be installed 
because Pelican specifies it as a dependency.

```bash
pip install pelican==3.7.1 markdown==2.6.8
```

Run the command and after everything is installed you should see output
similar to the following "Sucessfully installed" message.

```bash
Installing collected packages: pygments, pytz, six, feedgenerator, blinker, unidecode, MarkupSafe, jinja2, python-dateutil, docutils, pelican, markdown
  Running setup.py install for feedgenerator ... done
  Running setup.py install for blinker ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for markdown ... done
Successfully installed MarkupSafe-1.0 blinker-1.4 docutils-0.13.1 feedgenerator-1.9 jinja2-2.9.6 markdown-2.6.8 pelican-3.7.1 pygments-2.2.0 python-dateutil-2.6.0 pytz-2017.2 six-1.10.0 unidecode-0.4.20
```

Now that our dependencies are installed we can start building our
static site.


## Generate a Basic Site
Create a new directory for your project. My site will contain some of my
favorite [retro synthwave](https://www.youtube.com/watch?v=uYRZV8dV10w) 
artists as examples, but of course your site can contain whatever subjects 
that you want.



## What's next?
You just generated your first [Pelican](/pelican.html) static website using
[Markdown](/markdown.html) and [Jinja2](/jinja2.html). Next you can 
make additional modifications to the Jinja2 templates, build new pages and 
add more content via Markdown files.

Looking to get even more advanced with Pelican? Check out the open source
[Full Stack Python code](https://github.com/mattmakai/fullstackpython.com)
to see how a fairly large 100+ pages and 100,000+ words site can be built.

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

See something wrong in this blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170531-static-sites-pelican.markdown)
and submit a pull request.

