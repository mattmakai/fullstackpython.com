title: Web Application Security
category: page
slug: web-application-security
sortorder: 0455
toc: False
sidebartitle: Security
meta: Web applications can be attacked many ways by malicious actors. Learn more on Full Stack Python.


Website security must be thought about while building every level of the web 
stack. However, this section includes topics that deserve particular
treatment, such as cross-site scripting (XSS), SQL injection, cross-site 
request forgery and usage of public-private keypairs.


### Security tools
* [Bro](http://www.bro.org/) is a network security and traffic monitor.

* [lynis](https://cisofy.com/lynis/) 
  ([source code](https://github.com/CISOfy/lynis)) is a security 
  audit tool that can run as a shell script on a Linux system to find out
  its vulnerabilities so that you can fix them instead of allowing them
  to be exploited by malicious actors.

* [Charles](https://www.charlesproxy.com/) is an HTTP proxy for inspecting
  headers, requests and responses for all traffic that flows through it.

* [TLS Observatory](https://github.com/mozilla/tls-observatory) provides
  a suite of security tools for analyzing and inspecting Transport Layer
  Security (TLS) services. There is also a hosted version you can use
  at [observatory.mozilla.org](https://observatory.mozilla.org/).

* [WIG](https://github.com/6e726d/WIG) contains tools for gathering wireless
  data via Wifi protocols.

* [HTTP Evader](https://noxxi.de/research/http-evader.html) is an automated
  testing tool for checking firewalls to ensure they are protecting the
  appropriate ports and payloads.

* [Security monkey](https://github.com/Netflix/security_monkey) monitors for
  changes to AWS, Google Cloud, GitHub and other infrastructure systems.


### Specific vulnerabilities
* [httpoxy](https://httpoxy.org/) is a set of vulnerabilities that can affect
  Python web application servers via HTTP requests.

* [Heartbleed](http://heartbleed.com/) is a vulnerability in OpenSSL 
  implementations that must be patched for any systems you run otherwise
  you are at serious risk for data leakage.

* [Meltdown and Spectre](https://meltdownattack.com/) are x86 architecture
  problems caused by exploiting CPU branch-prediction implementations.


### HTTPS resources
SSL over HTTP (HTTPS) is mandatory for securing web data traffic in transit.
There is a [page dedicated to HTTPS](/https.html) and the following
resources can also give you a good overview of how HTTPS works.

* [How does HTTPS actually work?](http://robertheaton.com/2014/03/27/how-does-https-actually-work/)
  is a well-written overview of the protocol including certificates, 
  signatures, signing and related topics.

* These 
  [introduction to HTTPS](https://18f.gsa.gov/2015/07/16/introduction-to-https-webinar/)
  videos explain what HTTPS is and how to implement it.

* This question asking [what is the difference between TLS and SSL?](http://security.stackexchange.com/questions/5126/whats-the-difference-between-ssl-tls-and-https)
  explains that TLS is a newer version of SSL and should be used because
  SSL through version 3.0 is insecure.

* If you have wondered what all the SSL/TLS acronyms and settings mean,
  read the 
  [Security/Server Side TLS guide](https://wiki.mozilla.org/Security/Server_Side_TLS)
  which Mozilla uses to operationalize its servers.

* If you're having users submit sensitive information to your site you need
  to use SSL/TLS. Anything before TLS is now insecure. Check out this
  [handy guide](http://wingolog.org/archives/2014/10/17/ffs-ssl) that goes
  over some of the nuances of the subject.

* [The Sorry State of SSL](https://hynek.me/talks/tls/) details the 
  history and evolution of SSL/TLS. There are important differences between
  the versions and Hynek explains why TLS should always be used. The
  talk prompted work to improve Python's SSL in 2.7.9 based on the upgrades
  in Python 3 outlined in 
  [The not-so-sorry state of SSL in Python](https://developer.rackspace.com/blog/the-not-so-sorry-state-of-ssl-in-python/).

* [How HTTPS Secures Connections](http://blog.hartleybrody.com/https-certificates/)
  is a guide for what HTTPS does and does not secure against.

* [The first few milliseconds of an HTTPS connection](http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html)
  provides a detailed look at the SSL handshake process that is implemented
  by browsers based on the [RFC 2818](http://tools.ietf.org/html/rfc2818)
  specification.

* [Qualy SSL Server Test](https://www.ssllabs.com/ssltest/) can be used to
  determine what's in place and what is missing for your server's HTTPS 
  connection. Once you run the test read this article on 
  [Getting an A+ on Qualy's SSL Labs Tester](https://sethvargo.com/getting-an-a-plus-on-qualys-ssl-labs-tester/)
  to improve your situation.
  

## General security resources
* The Open Web Application Security Project (OWASP) has 
  [cheat sheets for security](https://www.owasp.org/index.php/Cheat_Sheets) 
  topics.

* [Stanford's CS253 class](https://web.stanford.edu/class/cs253/) is available
  for free online, including lecture slides, videos and course materials to
  learn about web browser internals, session attacks, fingerprinting, HTTPS
  and many other fundamental topics.

* [The SaaS CTO Security Checklist](https://cto-security-checklist.sqreen.io/)
  is an awesome list of steps for securing your infrastructure and employees
  as well as what stage and size company it is recommended that you put those
  procedures in place.

* [Reckon you've seen some stupid security things? Here, hold my beer...](https://www.troyhunt.com/reckon-youve-seen-some-stupid-security-things-here-hold-my-beer/)
  provides hilarious, and terribly sad, security vulnerabilities and weaknesses
  around encryption and password storage.

* This page contains a
  [fantastic curated list of security reading material](http://dfir.org/?q=node/8/)
  from beginning to advanced topics.

* [How to protect your infrastructure against the basic attacker](https://www.mailgun.com/blog/security-guide-basic-infrastructure-security)
  presents a good overview of what you need to think about when
  hardening your system against reasonablely competent malicious attackers.

* The [/r/netsec](http://www.reddit.com/r/netsec/) subreddit is one place to
  go to learn more about network and application security.

* [Hacking Tools Repository](http://gexos.github.io/Hacking-Tools-Repository/)
  is a great list of password cracking, scanning, sniffing and other security
  penetration testing tools.


* The EFF has a well written overview on 
  [what makes a good security audit](https://www.eff.org/deeplinks/2014/11/what-makes-good-security-audit). It's broad but contains some of their behind the
  scenes thinking on important considerations with security audits.

* [Ubuntu system hardening guide](https://linux-audit.com/ubuntu-server-hardening-guide-quick-and-secure/)
  provides step-by-step instructions for hardening the most recent 
  three [Ubuntu LTS](/ubuntu.html) releases.

* Ars Technica wrote posts on 
  [securing your website](http://arstechnica.com/security/2013/02/securing-your-website-a-tough-job-but-someones-got-to-do-it/)
  along with [how to set up a safe and secure web server: part 1](http://arstechnica.com/gadgets/2012/11/how-to-set-up-a-safe-and-secure-web-server/)
  and [part 2](http://arstechnica.com/information-technology/2012/11/securing-your-web-server-with-ssltls/)
  to explain HTTPS and SSL without much required pre-existing knowledge.

* [Crypto 101](https://www.crypto101.io/) is an introductory course on
  cryptography for programmers.

* The first answer to the question
  ["Why are salted hashes more secure for password storage?"](https://security.stackexchange.com/questions/51959/why-are-salted-hashes-more-secure-for-password-storage)
  on Stack Overflow gives a wonderful explanation for why this is an
  important technique to use to keep your database passwords and other
  secrets more secure if the hashed strings are leaked.

* [An in-depth analysis of SSH attacks on Amazon EC2](http://getprismatic.com/story/1409447605839)
  shows how important it is to secure your web servers, especially when they are
  hosted in IP address ranges that are commonly scanned by malicious actors.

* [Cloud Security Auditing: Challenges and Emerging Approaches](http://www.infoq.com/articles/cloud-security-auditing-challenges-and-emerging-approaches)
  is a high-level overview of some of security auditing problems that come
  with cloud deployments.

* Wondering how the common buffer overflow attack works? Check out this
  [article on buffer overflows](http://arstechnica.com/security/2015/08/how-security-flaws-work-the-buffer-overflow/)
  that explains the attack in layman's terms.

* [7 Security Measures to Protect Your Servers](https://www.digitalocean.com/community/tutorials/7-security-measures-to-protect-your-servers)
  provides a good overview of the fundamentals for how servers should be
  configured for baseline security.

* As you're developing on Linux, you'll want to read and follow this
  [Linux workstation security](https://github.com/lfit/itpol/blob/master/linux-workstation-security.md)
  document to make sure your code and environment are not compromised.
  If you're on Mac OS X, check out this 
  [securing Yosemite guide](https://github.com/drduh/OS-X-Yosemite-Security-and-Privacy-Guide)
  which covers that environment.

* [Timing attacks are one form of vulnerability](http://arstechnica.com/security/2015/10/new-attacks-on-network-time-protocol-can-defeat-https-and-create-chaos/) 
  that can be used to defeat HTTPS in certain configurations. Understanding
  how those attacks work is important in keeping your users' connections
  secure.

* [Let's Encrypt at Scale](https://engineering.autotrader.co.uk/2018/09/04/letsencrypt-at-scale.html)
  shows an implementation for securing thousands of sites with SSL 
  certificates to support HTTPS everywhere.


## Web security learning checklist
1. Read and understand the major web application security flaws that are
   commonly exploited by malicious actors. These include cross-site request 
   forgery (CSRF), cross-site scripting (XSS), SQL injection and session 
   hijacking. The 
   [OWASP top 10 web application vulnerabilities list](https://www.owasp.org/index.php/Top_10_2013-Top_10) 
   is a great place to get an overview of these topics.

1. Determine how the framework you've chosen mitigates these vulnerabilities.

1. Ensure your code implements the mitigation techniques for your framework. 

1. Think like an attacker and actively work to break into your own system. 
   If you do not have enough experience to confidently break the security 
   consider hiring a known white hat attacker. Have her break the 
   application's security, report the easiest vulnerabilities to exploit in 
   your app and help implement protections against those weaknesses.

1. Recognize that no system is ever totally secure. However, the more popular
   an application becomes the more attractive a target it is to attackers.
   Reevaluate your web application security on a frequent basis.

