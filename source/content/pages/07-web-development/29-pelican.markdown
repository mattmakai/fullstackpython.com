title: Pelican
category: page
slug: pelican
sortorder: 0729
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
  lays out the basic steps for installing Pelican, creating your first site and
  then uploading the generated results to S3. A good next exercise not covered in
  the post is using [CloudFront](https://aws.amazon.com/cloudfront/) or 
  [CloudFlare](https://www.cloudflare.com/) as a 
  [content delivery network (CDN) to server the static content](/static-content.html).

* [Getting started with Pelican and GitHub pages](http://www.mattmakai.com/introduction-to-pelican.html)
  is a tutorial I wrote to use the Full Stack Python source code to create
  and deploy your first static site.


