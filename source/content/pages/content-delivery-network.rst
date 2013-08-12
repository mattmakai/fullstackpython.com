CDN
===

:category: page
:slug: content-delivery-network
:sort-order: 08

A content delivery network (CDN) serves static file assets. 
`Amazon CloudFront <http://aws.amazon.com/cloudfront/>`_,
`Akamai <http://www.akamai.com/>`_, and 
`Rackspace Cloud Files <http://www.rackspace.com/cloud/public/files/>`_ 
are examples of CDNs. The purpose of a CDN is to remove the load of static
file requests from web servers that are handling dynamic web content. For
example, if you have an nginx server that handles both static files and 
acts as a front for a Green Unicorn WSGI server on a 512 megabyte 
virtual private server, the nginx server will run into resource 
constraints under heavy traffic. A CDN can remove the need to serve static
assets from that nginx server so it can purely act as a pass through for 
requests to the Green Unicorn WSGI server.

CDNs distribute request load globally by using data centers in different 
locations.


CDN Resources
-------------
`Using Amazon S3 to host your Django static files <http://blog.doismellburning.co.uk/2012/07/14/using-amazon-s3-to-host-your-django-static-files/>`_

`CDNs fail, but your scripts don't have to <http://www.hanselman.com/blog/CDNsFailButYourScriptsDontHaveToFallbackFromCDNToLocalJQuery.aspx>`_

