title: Content Delivery Networks (CDNs)
category: page
slug: content-delivery-networks-cdns
sortorder: 0504
toc: False
sidebartitle: CDNs
meta: Content delivery networks (CDNs) serve static assets via globally distributed servers to improve web app loading speed.


Content delivery networks (CDNs) serve static assets via globally distributed 
servers to improve web app loading speed.


### CDN resources
* [The 5 hour CDN](https://fly.io/blog/the-5-hour-content-delivery-network/)
  explains the basics of what CDNs are and how they are a combination of
  many standard web server components, but used globally and at scale.

* [MaxCDN vs CloudFlare vs Amazon CloudFront vs Akamai Edge vs Fastly](https://www.codeinwp.com/blog/maxcdn-vs-cloudflare-vs-cloudfront-vs-akamai-edge-vs-fastly/)
  compares and contrasts the most popular CDN services based on features,
  performance and pricing. Note
  that [Full Stack Python](https://www.fullstackpython.com/) uses Cloudflare
  to serve all content.

* [Crushing, caching and CDN deployment in Django](https://tech.marksblogg.com/crushing-caching-cdn-django.html)
  explains how to use the 
  [django-compressor](https://github.com/django-compressor/django-compressor/) 
  package with the
  [django-storages](https://django-storages.readthedocs.io/en/latest/) library
  to deploy static assets for a [Django](/django.html) application to a CDN.

* [Do not let your CDN betray you: Use Subresource Integrity](https://hacks.mozilla.org/2015/09/subresource-integrity-in-firefox-43/)
  describes the security implications for CDNs with unexpectedly modified
  content and how Subresource Integrity in modern web browsers can mitigate
  this vulnerability if used properly.
