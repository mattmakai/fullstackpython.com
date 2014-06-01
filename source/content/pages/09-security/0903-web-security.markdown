title: Web Application Security
category: page
slug: web-application-security
sort-order: 092
choice1url: /web-analytics.html
choice1icon: fa-dashboard
choice1text: I want to learn more about the users of my app with analytics.
choice2url: /api-integration.html
choice2icon: fa-link fa-inverse
choice2text: How do I integrate external APIs into my app?
choice3url: /logging.html
choice3icon: fa-align-left fa-inverse
choice3text: How can I log events that occur while the app is running?
choice4url: /about-author.html
choice4icon: fa-user
choice4text: Who created Full Stack Python?


# Web Application Security
Website security must be thought about while building every level of the web 
stack. However, this section includes topics that deserve particular
treatment, such as cross-site scripting (XSS), SQL injection, cross-site 
request forgery and usage of public-private keypairs.


## Security Resources
* [Securing an Ubuntu Server](http://www.andrewault.net/2010/05/17/securing-an-ubuntu-server/)

* [Securing Ubuntu](http://joshrendek.com/2013/01/securing-ubuntu/)

* [quick NIX secure script](https://github.com/marshyski/quick-secure) for
securing Linux distributions.

* [Security Tips from Apache](http://httpd.apache.org/docs/current/misc/security_tips.html)

* [When and How to Deploy HTTPS](http://erik.io/blog/2013/06/08/a-basic-guide-to-when-and-how-to-deploy-https/)

* [Securing a Linux Server](http://spenserj.com/blog/2013/07/15/securing-a-linux-server/)

* [Securing Your Website](http://arstechnica.com/security/2013/02/securing-your-website-a-tough-job-but-someones-got-to-do-it/)

* [How HTTPS Secures Connections: What Every Web Dev Should Know](http://blog.hartleybrody.com/https-certificates/)

* The Open Web Application Security Project (OWASP) has 
  [cheat sheets for security](https://www.owasp.org/index.php/Cheat_Sheets) 
  topics.

* [How HTTPS Secures Connections](http://blog.hartleybrody.com/https-certificates/)
  is a guide for what HTTPS does and does not secure against.

* [Crypto 101](https://www.crypto101.io/) is an introductory course on
  cryptography for programmers.

* [The first few milliseconds of an HTTPS connection](http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html)
  provides a detailed look at the SSL handshake process that is implemented
  by browsers based on the [RFC 2818](http://tools.ietf.org/html/rfc2818)
  specification.


## Web security learning checklist
<i class="fa fa-check-square-o"></i>
Read and understand the major web application security flaws that are
commonly exploited by malicious actors. These include cross-site request 
forgery (CSRF), cross-site scripting (XSS), SQL injection and session 
hijacking. The 
[OWASP top 10 web application vulnerabilities list](https://www.owasp.org/index.php/Top_10_2013-Top_10) 
is a great place to get an overview of these topics.

<i class="fa fa-check-square-o"></i>
Determine how the framework you've chosen mitigates these vulnerabilities.

<i class="fa fa-check-square-o"></i>
Ensure your code implements the mitigation techniques for your framework. 

<i class="fa fa-check-square-o"></i>
Think like an attacker and actively work to break into your own system. If
you do not have enough experience to confidently break the security consider
hiring a known white hat attacker. Have her break the application's security,
report the easiest vulnerabilities to exploit in your app and help implement
protections against those weaknesses.

<i class="fa fa-check-square-o"></i>
Recognize that no system is ever totally secure. However, the more popular
an application becomes the more attractive a target it is to attackers.
Reevaluate your web application security on a frequent basis.


### What topic do you want to learn about next?
