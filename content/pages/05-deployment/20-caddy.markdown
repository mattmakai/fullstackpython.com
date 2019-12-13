title: Caddy
category: page
slug: caddy
sortorder: 0520
toc: False
sidebartitle: Caddy
meta: Caddy is an HTTP server written in Go that emphasizes modern security standards and encryption.


[Caddy](https://caddyserver.com/) is a relatively new HTTP server created 
in 2015 and written in [Go](https://golang.org/). The server's philosophy
and design emphasize HTTPS-everywhere along with the HTTP/2 protocol.


## How can Caddy be used with Python deployments?
Caddy can be used both for testing during local development or as part
of a production deployment as an HTTP server and a reverse proxy with
the [proxy directive](https://caddyserver.com/docs/proxy).

<div class="well see-also">Caddy is an implementation of the <a href="/web-servers.html">web server</a> concept. Learn how these pieces fit together in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>



### General Caddy resources
* [A look inside Caddy](https://blog.gopheracademy.com/caddy-a-look-inside/)
  shows and explains some of the Go code written to build the server.

* The [official Caddy server docs](https://caddyserver.com/docs) are the
  spot to look for what directives can be placed into a Caddy configuration
  file

* [Caddy a modern web server supporting HTTP/2](http://engineeredweb.com/blog/2015/caddy-web-server/)
  is a quick synopsis on installing Caddy along with a short example
  configuration file.

* [HTTP 2.0 on localhost with Caddy](https://tobias.is/blogging/test-http2-localhost-caddy-ssl/)
  shows how to use a self-signed certificate with Caddy to do local 
  development with an HTTP/2 web server.


