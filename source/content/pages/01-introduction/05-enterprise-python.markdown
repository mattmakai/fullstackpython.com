title: Enterprise Python
category: page
slug: enterprise-python
sortorder: 0105
toc: False
sidebartitle: Enterprise Python
meta: Python is widely used to build enterprise application in large organizations around the world.


# Enterprise Python
One of the misconceptions around Python and other dynamically-typed languages 
is that they cannot be reliably used to build enterprise-grade software. 
However, almost all commercial and government enterprises already use 
Python in some capacity, either as glue code between disparate applications 
or to build the applications themselves. 


## What is enterprise software?
Enterprise software is built for the requirements of an organization rather 
than the needs of an individual. Software written for enterprises often 
needs to integrate with legacy systems, such as existing databases and 
non-web applications. There are often requirements to integrate with 
authentication systems such as the 
[Lightweight Directory Access Protocol (LDAP)](http://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) 
and 
[Active Directory (AD)](https://msdn.microsoft.com/en-us/library/aa746492%28v=vs.85%29.aspx).

Organizations develop enterprise software with numerous custom requirements 
to fit the specific needs of their operating model. Therefore the software
development process often becomes far more complicated due to disparate 
factions within an organization vying for the software to handle their 
needs at the expense of other factions.

The complexity due to the many stakeholders involved in the building of 
enterprise software leads to large budgets and extreme scrutiny by 
non-technical members of an organization. Typically those non-technical 
people place irrational emphasis on the choice of programming language and 
frameworks when otherwise they should not make technical design decisions.


## Why are there misconceptions about Python in enterprise environments?
Traditionally large organizations building enterprise software have used 
statically typed languages such as C++, .NET and Java. Throughout the 1980s 
and 1990s large companies such as Microsoft, Sun Microsystems and Oracle 
marketed these languages as "enterprise grade". The inherent snub to other
languages was that they were not appropriate for CIOs' difficult technical 
environments. Languages other than Java, C++ and .NET were seen as risky and
therefore not worthy of investment.

In addition, "scripting languages" such as Python, Perl and Ruby were not
yet robust enough in the 1990s because their core standard libraries were
still being developed. Frameworks such as [Django](/django.html), 
[Flask](/flask.html) and Rails (for Ruby) did not yet exist. The Web was
just beginning and most enterprise applications were desktop apps built
for Windows. Python simply wasn't made for such environments.


## Why is Python now appropriate for building enterprise software?
From the early 2000s through today the languages and ecosystems for many
dynamically typed languages have greatly improved and often surpassed some
aspects of other ecosystems. Python, Ruby and other previously derided 
languages now have vast, well-maintained open source ecosystems backed by 
both independent developers and large companies including Microsoft, IBM, 
Google, Facebook, Dropbox, Twilio and many, many others.

Python's open source libraries, especially for
[web development](/web-frameworks.html) and data analysis, are some of the 
best maintained and fully featured pieces of code for any language.

Meanwhile, some of the traditional enterprise software development languages 
such as Java have languished due to underinvestment by their major corporate 
backers. When [Oracle purchased Sun Microsystems in 2009](http://www.oracle.com/us/corporate/press/018363)
there was a long lag time before Java was enhanced with new language features
in Java 7.  Oracle also 
[bundles unwanted adware with the Java installation](http://www.engadget.com/2015/03/06/java-adware-mac/),
whereas the Python community would never put up with such a situation because
the language is open source and does not have a single corporate controller.

Other ecosystems, such as the .NET platform by Microsoft have fared much 
better. Microsoft continued to invest in moving the .NET platform along
throughout the early part of the new millennium.

However, Microsoft's enterprise products often have expensive licensing fees 
for their application servers and associated software. In addition, Microsoft 
is also a major backer of open source, [especially Python](http://www.hanselman.com/blog/OneOfMicrosoftsBestKeptSecretsPythonToolsForVisualStudioPTVS.aspx),
and their 
[Python tools for Visual Studio](https://www.visualstudio.com/en-us/features/python-vs.aspx) 
provide a top-notch [development environment](/development-environments.html).

The end result is that enterprise software development has changed 
dramatically over the past couple of decades. CIOs and technical executives
can no longer ignore the progress of Python and the great open source 
community in the enterprise software development landscape if they want to
continue delivering business value to their business side customers.

## Open source enterprise Python projects
* [Collab](https://github.com/cfpb/collab) by the 
  U.S. government's 
  [Consumer Financial Protection Bureau](http://www.consumerfinance.gov/) 
  (CFPB) agency is a corporate intranet and collaboration platform for large
  organizations. The project is currently running and in-use by thousands of
  CFPB employees.

* [Pants](https://github.com/twitter/pants) is a build system for software
  projects with many distinct parts and built with many different programming
  languages as is often the case in large organizations.


## Enterprise Python software development resources
* There are a couple of solid demystifying articles in CIO magazine including
  [this broad overview of Python in enterprises](http://www.cio.com/article/2437137/developer/you-used-python-to-write-what-.html)
  and this article on
  [why dynamic languages are gaining share for enterprise development](http://www.cio.com/article/2431212/developer/dynamic-languages--not-just-for-scripting-any-more.html).

* JavaWorld wrote an interesting article about 
  [Python's inroads into enterprise software development](http://www.javaworld.com/article/2078655/scripting-jvm-languages/python-coming-to-the-enterprise--like-it-or-not.html).

* I gave a talk at DjangoCon 2014 on 
  [How to Solve the Top 5 Headaches with Django in the Enterprise](https://www.youtube.com/watch?v=aMtiCX38w20)
  which covered both Python and Django in large organizations.

* This [StackExchange answer](http://programmers.stackexchange.com/questions/141411/what-is-enterprise-software-exactly)
  contains a solid explanation what differentiates enterprise software
  from traditional software.

* There was a 
  [Python subreddit thread about Python in the enterprise](https://www.reddit.com/r/Python/comments/3myppd/everyone_who_encounters_it_seems_to_love_python/)
  that's worth a look for broader opinions on Python compared to Java and
  .NET in enterprise environments.

