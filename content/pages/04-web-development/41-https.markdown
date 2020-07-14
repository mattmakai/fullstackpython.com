title: HTTPS
category: page
slug: https
sortorder: 0441
toc: False
sidebartitle: HTTPS
meta: The HTTP Secure (HTTPS) protocol encyrpts data between a web server and the client web browser.


The HTTP Secure (HTTPS) protocol encyrpts data between a web server and the 
client web browser.


### HTTPS tutorials
* [How To Secure Nginx with Let's Encrypt on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)
  walks through how to configure your [Nginx](/nginx.html) server with
  HTTPS using a free [Let's Encrypt](https://letsencrypt.org/) domain 
  certificate.

* [Switching Your Site to HTTPS on a Shoestring Budget](https://css-tricks.com/switching-site-https-shoestring-budget/)
  shows the steps for moving a GitHub Pages-based site or any site that
  can be behind Cloudflare's free tier to HTTPS.


### Additional HTTPS resources
* [The 6-Step "Happy Path" to HTTPS](https://www.troyhunt.com/the-6-step-happy-path-to-https/)
  covers how to obtain a free SSL certificate, permanently redirect HTTP
  to HTTPS and fix insecure references to non-HTTPS resources.

* [HTTPS on Stack Overflow: the end of a long road](https://nickcraver.com/blog/2017/05/22/https-on-stack-overflow/)
  is a wonderfully in-depth post on transitioning from HTTP to HTTPS, 
  including redirecting all HTTP requests to HTTPS, for a very high
  trafficked website.

* [TLS stats from 1.6 billion connections to mozilla.org](https://jve.linuxwall.info/blog/index.php?post/2016/08/04/TLS-stats-from-1.6-billion-connections-to-mozilla.org)
  provides real-world data for which ciphersuites to use based on 
  mozilla.org connections.

* [HTTPS in the real world](https://robertheaton.com/2018/11/28/https-in-the-real-world/)
  is both an accesible read and gives the nitty gritty details beyond how
  the HTTPS handshake and transmission work, along the assumptions it breaks
  down about where the most likely attack vectors really come from.

* [How Let's Encrypt Works](https://letsencrypt.org/how-it-works/) is a 
  primer on how the free and now widely-used certificate service grants
  and revokes domain certificates.

* [Performing & Preventing SSL Stripping: A Plain-English Primer](https://blog.cloudflare.com/performing-preventing-ssl-stripping-a-plain-english-primer/)
  explains the KRACK Attack for stealing data despite an HTTPS connection
  and how your site needs to use HSTS to prevent the attack.

* [HTTPS adoption has reached the tipping point](https://www.troyhunt.com/https-adoption-has-reached-the-tipping-point/)
  shows data about the growth of HTTPS and how most sites now serve more
  than half their traffic via secure connections.

* Google's 
  [HTTPS transparency report card](https://transparencyreport.google.com/https/overview?hl=en)
  shows the growth of HTTPS connections across Google's properties.
  There is a clear upward trend but even some of Google's properties still
  are not 100% using HTTPS over unencrypted HTTP connections.

* [An overview of TLS 1.3](https://kinsta.com/blog/tls-1-3/) and
  [TLS 1.3 - enhanced performance, hardened security](https://www.cloudflare.com/learning-resources/tls-1-3/) 
  cover the high-level information on the latest approved version of
  Transport Security Layer (TLS) 1.3.

