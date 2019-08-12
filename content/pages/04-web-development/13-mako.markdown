title: Mako
category: page
slug: mako
sortorder: 0413
toc: False
sidebartitle: Mako
meta: Mako is a Python template engine used to generate HTML, XML or other output formats.


Mako is a [template engine built in Python](/template-engines.html) that is
used to generate output HTML, XML and similar formats.

<a href="http://www.makotemplates.org/" style="border: none;"><img src="/img/logos/mako.jpg" alt="Mako template engine logo." class="shot rnd outl" width="100%"></a>

<div class="well see-also">Mako is an implementation of the <a href="/template-engines.html">template engines</a> concept. Learn more in the <a href="/web-development.html">web development</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Mako resources
* [Exploring Mako](https://beachcoder.wordpress.com/2007/05/11/exploring-mako/)
  explains a bit about the template engines Myghty and Mason, which influenced
  Mako's design. The post then shows a few basic examples for how to use Mako.

* [Configuration Templates with Python and Mako](https://codingnetworker.com/2016/01/configuration-templates-python-mako/)
  shows some basic situations for how to use Mako in an example project.

* [Flask-Mako](https://pythonhosted.org/Flask-Mako/) is a [Flask](/flask.html) 
  extension that makes it easier to use Mako as the template engine in your
  Flask web app projects.

* The Stack Overflow question on 
  [What is the fastest template system for Python?](http://stackoverflow.com/questions/1324238/what-is-the-fastest-template-system-for-python)
   provides some basic benchmarks comparing Mako, Jinja and other template
   engines. Any benchmark should be taken as a data point rather than a 
   rule on which engine is actually the fastest in real world scenarios.
   In addition, if you are using Mako or any other template engine as part
   of a static website generator then it will not really matter which one
   is the fastest because the output is created before the website is 
   deployed rather than during the [web server](/web-servers.html)'s
   HTTP request-response cycle.
