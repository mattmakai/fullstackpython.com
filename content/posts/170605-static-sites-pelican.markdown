title: How to Create Your First Static Website with Pelican and Jinja2 
slug: generating-static-websites-pelican-jinja2-markdown
meta: Learn how to generate static websites with Python, the Pelican static site generator, Jinja2 and Markdown.
category: post
date: 2017-06-05
modified: 2017-06-05
headerimage: /img/170605-static-sites-pelican/header.jpg
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

In this tutorial you will learn how to create a 
[basic static website](/static-site-generator.html) that you can further 
customize and expand with your own design and content.


## Our Tools
This tutorial should work with either [Python 2 or 3](/python-2-or-3.html), 
but Python 3 is strongly recommended for all new applications. I used
[Python 3.6.1](https://www.python.org/downloads/release/python-361/) to 
write this post. In addition to Python, throughout this tutorial we 
will also use the following 
[application dependencies](/application-dependencies.html): 

* [Pelican](/pelican.html) 
  [static site generator](/static-site-generator.html), 
  [version 3.7.1](https://github.com/getpelican/pelican/releases/tag/3.7.1)
* [Markdown](/markdown.html) parsing library to handle Markdown as a content 
  input format, version 
  [2.6.8](https://github.com/waylan/Python-Markdown/releases/tag/2.6.8-final)
* [Jinja2](/jinja2.html), a Python [template engine](/template-engines.html), 
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
Start by creating a new virtual environment for your project. My virtualenv
is named `staticsite` with the following command but you can name yours
whatever matches the project you are creating.

```bash
python3 -m venv staticsite
```

Activate the virtualenv.

```
source staticsite/bin/activate
```

When activated the virtualenv should prepend its name to your command prompt,
as shown in the following screenshot of my terminal.

<img src="/img/170605-static-sites-pelican/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Create and activate the Python virtual environment.">

Install the appropriate dependencies after your virtualenv is activated. 
Use the `pip` command to install Pelican and Markdown, which will also 
install Jinja2 because Pelican specifies it as a dependency.


```bash
pip install pelican==3.7.1 markdown==2.6.8
```

Run the `pip` command and after everything is installed you should see output
similar to the following "Successfully installed" message.

```bash
Installing collected packages: pygments, pytz, six, feedgenerator, blinker, unidecode, MarkupSafe, jinja2, python-dateutil, docutils, pelican, markdown
  Running setup.py install for feedgenerator ... done
  Running setup.py install for blinker ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for markdown ... done
Successfully installed MarkupSafe-1.0 blinker-1.4 docutils-0.13.1 feedgenerator-1.9 jinja2-2.9.6 markdown-2.6.8 pelican-3.7.1 pygments-2.2.0 python-dateutil-2.6.0 pytz-2017.2 six-1.10.0 unidecode-0.4.20
```

Now that our dependencies are installed into the virtualenv we can start 
building our static site.


## Generate a Basic Site
Create a new directory for your project. My site will contain some of my
favorite [retro synthwave](https://www.youtube.com/watch?v=uYRZV8dV10w) 
artists as examples, but of course your site can contain whatever subjects 
that you want.

Create a new directory for our static site project and change into the
directory.

```
mkdir retrosynth
cd retrosynth
```

Run the `pelican-quickstart` command within the new project directory.

```bash
(staticsite) $ pelican-quickstart
```

The quickstart script will rattle off a bunch of questions. Follow
along with the answers below or modify them for your own site name and
desired configuration.

```bash
Welcome to pelican-quickstart v3.7.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

    
> Where do you want to create your new web site? [.]  
> What will be the title of this web site? RetroSynthwave
> Who will be the author of this web site? Matt Makai
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) n
> What is your time zone? [Europe/Paris] America/New_York
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) y
> What is the name of your S3 bucket? [my_s3_bucket] 
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) n
Done. Your new project is available at /Users/matt/devel/py/retrosynth
(staticsite) $ 
```

What did we just create using the Pelican quickstart script? Check out
the new files in the directory.

```bash
(staticsite) $ ls
Makefile        develop_server.sh   pelicanconf.py
content         fabfile.py          publishconf.py
```

The quickstart created five files and one new directory:

* `Makefile`: `make` command convenience tasks for common operations such as 
  running a development server, building a site and cleaning extraneous 
  build files
* `fabfile.py`: A Fabric file that has some of the same types of commands
  as the `Makefile`. Fabric is a wonderful code library but for now I 
  recommend skipping the Fabric file because unfortunately Fabric does not 
  yet support Python 3.
* `develop_server.sh`: shell script for running the development server
* `pelicanconf.py`: settings file for your Pelican project. If you are used
  to earlier versions of Pelican this file was instead named `settings.py`
* `publishconf.py`: another (optional) settings file that can be considered 
  as a "production" settings file when you move past the development phase
  and want to deploy your site
* `content`: location for your markup files, which should be stored under
  `pages` and `posts` directories

We can use these files as the base for our new static site. Let's see what
it looks like by default by running it via the `devserver` task in the 
Makefile.

```bash
make devserver
```

The Pelican development server will start serving up your site with a 
daeman process. Go to [localhost:8000](http://localhost:8000) in your web 
browser and you will see the first version of your static site.

<img src="/img/170605-static-sites-pelican/default-style.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Default styling on the Pelican static site.">

What if you don't have `make` installed on your system? Change into the
`output` directory and use the `python -m http.server` command to use the
built-in Python 3 HTTP server for your generated files.

When you want to kill the development server look for a file named 
`pelican.pid`under your project directory. The `pelican.pid` file is created
by Pelican and contains the process ID for your development server.

```
(staticsite) $ cat pelican.pid 
1365
```

Use the `ps` and `grep` commands to view the process then stop the process
with the `kill` command as follows. Remember that your process ID will almost
definitely be different from the `1365` ID for my process.

```
(staticsite) $ ps -A | grep 1365
 1365 ttys003    0:01.43 /Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python /Users/matt/Envs/staticsite/bin/pelican --debug --autoreload -r /Users/matt/devel/py/retrosynth/content -o /Users/matt/devel/py/retrosynth/output -s /Users/matt/devel/py/retrosynth/pelicanconf.py
 1411 ttys003    0:00.00 grep 1365
(staticsite) $ kill 1365
(staticsite) $ ps -A | grep 1365
 1413 ttys003    0:00.00 grep 1365
```

It is up to you whether you want to use the development server or not
while creating your site. Every time I want to view my changes for 
Full Stack Python I actually regenerate the site using my own Makefile that 
wraps the `pelican` command. The `python -m http.server` command constantly 
serves up each build's changes.

Alright, now that we have our starter files we can get to work creating
some initial content.


## Write Some Content
Pelican can accept both [Markdown](/markdown.html) and reStructureText
markup files as input.

Create a new subdirectory under the `content` named `posts`. Change into
the `posts` directory. Create a new file named `first_post.markdown` with
the following content.

```markdown
...
```

What does our server look like now that we wrote our first post?

We used the `make devserver` command earlier, but what other commands are
available to us via the `Makefile`?


```bash
make
```

```
Makefile for a pelican Web site                                           
                                                                          
Usage:                                                                    
   make html                           (re)generate the web site          
   make clean                          remove the generated files         
   make regenerate                     regenerate files upon modification 
   make publish                        generate using production settings 
   make serve [PORT=8000]              serve site at http://localhost:8000
   make serve-global [SERVER=0.0.0.0]  serve (as root) to :80    
   make devserver [PORT=8000]          start/restart develop_server.sh    
   make stopserver                     stop local server                  
   make ssh_upload                     upload the web site via SSH        
   make rsync_upload                   upload the web site via rsync+ssh  
   make dropbox_upload                 upload the web site via Dropbox    
   make ftp_upload                     upload the web site via FTP        
   make s3_upload                      upload the web site via S3         
   make cf_upload                      upload the web site via Cloud Files
   make github                         upload the web site via gh-pages   
                                                                          
Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   
Set the RELATIVE variable to 1 to enable relative urls
```

```
make html

pelican /Users/matt/devel/py/retrosynth/content -o /Users/matt/devel/py/retrosynth/output -s /Users/matt/devel/py/retrosynth/pelicanconf.py 
WARNING: No valid files found in content.
Done: Processed 0 articles, 0 drafts, 0 pages and 0 hidden pages in 0.07 seconds.
```

If you used the `make devserver` command earlier then give Python's built-in
HTTP server a shot with the following command.

```
python -m http.server
```

You can change the port binding by adding a number after the command, if you 
want to serve more than one static site at a time or you already have an 
application bound to port 8000.

```
python -m http.server 8005
```

Note that if you are using Python 2 the equivalent HTTP server command is
`python -m SimpleHTTPServer`.



## Edit the Configuration
Pelican's quickstart assumes a bunch of defaults that may or may not be
applicable to your site. Open up the `pelicanconf.py` file to change some
of the defaults.

Look for the `TIMEZONE` variable. If it's not right for your location
then modify it to your zone. Wikipedia has a handy
[table of valid time zones values](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).


## Modify the Site Theme



## What's next?
You generated your first [Pelican](/pelican.html) static website using
[Markdown](/markdown.html) and [Jinja2](/jinja2.html). You can 
now make additional modifications to the Jinja2 templates, build new pages 
and add more content via Markdown files.

Do you want to deploy your new static website to GitHub Pages or an S3 bucket?
Well, that's a story for another Full Stack Python tutorial...

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).  

See something wrong in this blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170605-static-sites-pelican.markdown)
and submit a pull request.
