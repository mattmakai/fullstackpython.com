title: Pelican
category: page
slug: pelican
sortorder: 0432
toc: False
sidebartitle: Pelican
meta: Pelican is a static site generator implemented in Python that uses Markdown or reStructuredText to produce websites.


[Pelican](http://docs.getpelican.com/en/3.6.3/) is a 
[static site generator](/static-site-generator.html) implemented in Python 
that combines [Jinja](/jinja2.html) [templates](/template-engines.html) 
with content written in [Markdown](/markdown.html) or reStructuredText to 
produce websites. 

Pelican's 
[source code is available on GitHub](https://github.com/getpelican/pelican)
under the 
[AGPL 3 license](https://www.gnu.org/licenses/why-affero-gpl.html).

<a href="http://docs.getpelican.com/en/3.6.3/" style="border: none;"><img src="/img/logos/pelican.png" width="100%" alt="Pelican static website generator logo." class="shot" /></a>

<div class="well see-also">Pelican is an implementation of the <a href="/static-site-generator.html">static site generators</a> concept. Learn how the parts fit together in the <a href="/web-development.html">web development</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


## Why is Pelican a useful tool?
Static websites are easier to [deploy](/deployment.html) than full web 
applications built with a [web framework](/web-frameworks.html) that rely 
on a [persistent database backend](/databases.html). In addition, static
sites are typically much faster to load because there are no database 
queries or middleware code to execute during the HTTP request-response
cycle. 

A web server that hosts a static website simply responds to inbound HTTP 
requests with the file being requests - no dynamic data is populated on the
server during the response.


### Pelican resources
Static site generators like Pelican are a simple compared to 
[web frameworks](/web-frameworks.html) so most tutorials focus on
creating simple sites that you can style yourself, as well as deploying
to hosting services such as Amazon S3 and GitHub Pages.

* [How to Create Your First Static Site with Pelican and Jinja2](/blog/generating-static-websites-pelican-jinja2-markdown.html)
  walks through installing, generating the boilerplate and customizing
  your first static site using Pelican.

* [How I built this website, using Pelican](http://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1-setup/)
  walks through getting your first Pelican site generated and running.

* [A Pelican Tutorial to Build A Static, Python-Powered Blog with Search & Comments](https://snipcart.com/blog/pelican-blog-tutorial-search-comments)
  provides a walkthrough for how to build a great combination of useful 
  features into your static site such as search and comments with the
  [Staticman](https://github.com/eduardoboucas/staticman) library. Bonus 
  points at the end for showing how to deploy to 
  [Netlify](https://www.netlify.com/) as an alternative to GitHub Pages
  or S3.

* [Creating your own blog with Pelican](http://chdoig.github.io/create-pelican-blog.html)
  covers the decision-making process with building a static versus dynamic
  website. The post then dives into using Pelican as a static site 
  generator with a blog structure and basic theme.

* [Using Pelican to generate and manage static websites](http://www.ifnamemain.com/posts/2014/May/30/pelican_python/)
  explains how to use the `pelican-quickstart` command to generate
  an initial site then adds the Tipue Search plugin to provide content
  search despite the static site limitations.

* [Pelican Folder Structure](http://archerimagine.com/articles/pelican/pelican-folder-structure.html)
  explains how the `pages` and `posts` structure under `content`
  works when using Pelican.

* [Pelican's official Plugin creation documentation](http://docs.getpelican.com/en/3.7.1/plugins.html)
  gives a great starting point for building your own plugins that can
  take in new input markup formats, modify the generator process and
  add handy features such as a custom table of contents.

* [Pelican Sitemap and Pagination](http://www.vcheng.org/2014/02/22/pelican-sitemap-pagination/)
  explains how to generate a `sitemap.xml` file for your static site that 
  includes all pages instead of just auto-included top-level pages.

* [Getting started with Pelican and GitHub pages](http://www.mattmakai.com/introduction-to-pelican.html)
  is a tutorial I wrote to use the Full Stack Python source code to create
  and deploy your first static site.

* [Moving blogs to Pelican](http://arunrocks.com/moving-blogs-to-pelican/)
  talks about one developer's transition from Jekyll to Pelican for his
  own sites.

* [Using Travis & GitHub to deploy static sites](http://www.gregreda.com/2015/03/26/static-site-deployments/)
  shows how to automate deployments of a Pelican-based static site using
  Travis CI.

