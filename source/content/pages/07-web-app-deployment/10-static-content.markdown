title: Static Content
category: page
slug: static-content
sortorder: 0710
toc: False
sidebartitle: Static Content
meta: Serving static and media files are an important part of Python deployments. Learn about static content on Full Stack Python.


# Static content
Some content on a website does not change and therefore should be served
up either directly through the web server or a content delivery network (CDN).
Examples include JavaScript, image, and CSS files.


## Types of static content
Static content can be either assets created as part of your development
process such as images on your landing page or user-generated content. The 
Django framework calls these two categories *assets* and *media*.


## Content delivery networks
A content delivery network (CDN) is a third party that stores and serves 
static files. [Amazon CloudFront](http://aws.amazon.com/cloudfront/),
[Akamai](http://www.akamai.com/), and 
[Rackspace Cloud Files](http://www.rackspace.com/cloud/public/files/) 
are examples of CDNs. The purpose of a CDN is to remove the load of static
file requests from web servers that are handling dynamic web content. For
example, if you have an nginx server that handles both static files and 
acts as a front for a Green Unicorn WSGI server on a 512 megabyte 
virtual private server, the nginx server will run into resource 
constraints under heavy traffic. A CDN can remove the need to serve static
assets from that nginx server so it can purely act as a pass through for 
requests to the Green Unicorn WSGI server.

CDNs send content responses from data centers with the closest proximity to the requester.


## Static Content Resources
* [The super stupid idiot's guide to getting started with Django, Pipeline, and S3](http://blog.iambob.me/the-super-stupid-idiots-guide-to-getting-started-with-django-pipeline-and-s3/)
  shows how to host static content on S3 and use those files with Django.

* [Crushing, caching and CDN deployment in Django](http://tech.marksblogg.com/crushing-caching-cdn-django.html)
  shows how to use django-compressor and a CDN to scale static and media
  file serving.

* [Uploading with Django and Amazon S3](http://pritishc.com/blog/2015/09/06/uploading-with-django-and-amazon-s3/)
  walks through each step in getting buckets set up so you can upload
  files to them via Django.

* [Using Amazon S3 to host your Django static files](http://blog.doismellburning.co.uk/2012/07/14/using-amazon-s3-to-host-your-django-static-files/)

* [CDNs fail, but your scripts don't have to](http://www.hanselman.com/blog/CDNsFailButYourScriptsDontHaveToFallbackFromCDNToLocalJQuery.aspx)

* [django-storages](http://django-storages.readthedocs.org/en/latest/) is 
a Django library for managing static and media files on services such as
Amazon S3 and other content delivery networks.

* RevSys has a nice article on a range of 
  [important static file optimizations](http://www.revsys.com/12days/front-end-performance/)
  such as setting cache headers, optimizing JavaScript and reducing the
  size of images.

* Twelve folks with significant experience working on and with CDNs
  provide their perspectives in this piece: 
  [CDN experts on CDNs](https://www.maxcdn.com/blog/cdn-experts-on-cdns/).


## Static content learning checklist
1. Identify a content delivery network to offload serving static content 
   files from your local web server. I recommend using Amazon S3 with 
   CloudFront as it's easy to set up and will scale to high bandwidth demands.

1. Update your web application deployment process so updated static files are
   uploaded to the CDN. 

1. Move static content serving from the www subdomain to a static (or 
   similarly named) subdomain so browsers will load static content in 
   parallel to www HTTP requests.

