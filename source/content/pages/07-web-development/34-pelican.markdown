title: Pelican
category: page
slug: pelican
sortorder: 0734
toc: False
sidebartitle: Pelican
meta: Pelican is a static site generator implemented in Python that uses Markdown or reStructuredText to produce websites.


# Pelican
[Pelican](http://docs.getpelican.com/en/3.6.3/) is a 
[static site generator](/static-site-generator.html) implemented in Python 
that combines [Jinja](/jinja2.html) templates with content written in 
Markdown or reStructuredText to produce websites. 

Pelican's 
[source code is available on GitHub](https://github.com/getpelican/pelican)
under the 
[GPL 3 license](https://www.gnu.org/licenses/quick-guide-gplv3.html).

<a href="http://docs.getpelican.com/en/3.6.3/" style="border: none;"><img src="/img/pelican-logo.png" width="100%" alt="Pelican static website generator logo." class="technical-diagram" /></a>

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


## Pelican resources
* [The Long Road to Building a Static Blog with Pelican](http://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html)
  is a fantastic read that really gets into the details throughout the 
  walkthrough. 

* [How I built this website, using Pelican](http://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1-setup/)
  walks through getting your first Pelican site generated and running.

* [Setting up a blog with Pelican and Amazon S3](http://lexual.com/blog/setup-pelican-blog-on-s3/)
  lays out the basic steps for installing Pelican, creating your first 
  site and then uploading the generated results to S3. A good next 
  exercise not covered in the post is using 
  [CloudFront](https://aws.amazon.com/cloudfront/) or 
  [CloudFlare](https://www.cloudflare.com/) as a 
  [content delivery network (CDN) to server the static content](/static-content.html).

* [Creating your own blog with Pelican](http://chdoig.github.io/create-pelican-blog.html)
  covers the decision-making process with building a static versus dynamic
  website. The post then dives into using Pelican as a static site 
  generator with a blog structure and basic theme.

* [Using Pelican to generate and manage static websites](http://www.ifnamemain.com/posts/2014/May/30/pelican_python/)
  explains how to use the `pelican-quickstart` command to generate
  an initial site then adds the Tipue Search plugin to provide content
  search despite the static site limitations.

* [Pelican's official Plugin creation documentation](http://docs.getpelican.com/en/3.7.1/plugins.html)
  gives a great starting point for building your own plugins that can
  take in new input markup formats, modify the generator process and
  add handy features such as a custom table of contents.

* [Getting started with Pelican and GitHub pages](http://www.mattmakai.com/introduction-to-pelican.html)
  is a tutorial I wrote to use the Full Stack Python source code to create
  and deploy your first static site.

