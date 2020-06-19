title: Companies using Python
category: page
slug: companies-using-python
sortorder: 0107
toc: False
sidebartitle: Companies using Python
meta: A majority of companies around the world use the Python programming language throughout their organizations.


The Python programming language is widely used by companies around the world 
to [build web apps](/web-development.html), [analyze data](/data.html),
[automate operations via DevOps](/devops.html) and 
[create reliable, scalable enterprise applications](/enterprise-python.html).

There is also a fantastic list of 
[organizations using Python on the Python.org wiki](https://wiki.python.org/moin/OrganizationsUsingPython#Games)
as well as a detailed write-up of 
[several top Python-powered companies on Real Python's blog](https://realpython.com/world-class-companies-using-python/).

Many companies do not even realize they are using Python across their
organizations. For example, if a company is a "Java-only shop" but they
use IBM WebSphere as a web application server then they have to use
Python to script the server's configuration! Python has a habit of getting
in everywhere regardless of whether the usage is intentional.


## Financial institutions
Python is widely-used across financial institutions, whether they are
hedge funds, large banks or regulators (see "Government Agencies" section
below).

* [Goldman Sachs uses Python](https://www.quora.com/Why-does-Goldman-Sachs-ask-for-Python-language-as-a-skill-during-the-interview-for-an-analyst-role)
  and often asks candidates about their experience with the language
  during the interview process. 

* You can see publicly what companies are using internally by looking
  at job descriptions on sites like 
  [Glassdoor with "Python Goldman Sachs" keywords](https://www.glassdoor.com/Jobs/Goldman-Sachs-python-Jobs-EI_IE2800.0,13_KO14,20.htm)
  and
  [Indeed for JP Morgan Chase](https://www.indeed.com/salaries/Python-Developer-Salaries-at-JPMorgan-Chase).
  Salaries and responsibilities vary widely based on the role and whether
  Python is used for data analysis, 
  [web application development](/web-development.html) or DevOps.

* [PayPal](https://www.paypal-engineering.com/2016/09/07/python-packaging-at-paypal/)
  uses Python across their entire infrastructure and often writes great
  technical blog posts on packaging, 
  [optimization using C](https://www.paypal-engineering.com/2016/09/22/python-by-the-c-side/) 
  and [configuring DNS](https://www.paypal-engineering.com/2015/12/16/enterprise-overhaul-resolving-dns/).


## Large tech companies
Large technology companies tend to be polyglot (use many programming 
languages rather than standardizing on one), with Python either as a
primary language or the "glue" that helps all the other languages fit
together. The following articles explain how these leading large companies 
like Uber, Twilio, Netflix and Facebook uses Python in their development 
stacks.

* [Uber's tech stack](https://eng.uber.com/tech-stack-part-one/) contains
  a significant amount of Python, which they documented in a series of 
  engineering posts. Part one describes the lower backend levels, which are 
  written in Python, with Node.js, Go and Java mixed in. 
  [Part two](https://eng.uber.com/tech-stack-part-two/) explains the higher
  levels of the marketplace and user interfaces.

* [Twilio](https://www.twilio.com/) uses Python with [Django](/django.html)
  and the [Wagtail](https://wagtail.io/) content management system to power
  the amazing [Twilio documentation](https://www.twilio.com/) as well as
  [TwilioQuest](https://www.twilio.com/quest). They wrote a post about
  [how TwilioQuest was built](https://www.twilio.com/blog/2017/11/building-twilioquest-with-twilio-sync-django-and-vue-js.html) 
  that goes into detail on the code including the usage of the front-end 
  Vue.js framework. Twilio also uses [Flask](/flask.html) to run the 
  [REST API endpoints](https://www.twilio.com/docs/usage/api) and open sourced
  the [Flask-RESTful](https://github.com/flask-restful/flask-restful) 
  framework so other developers could cut down the boilerplate in their
  web APIs.

* [Netflix uses Python](https://talkpython.fm/episodes/show/16/python-at-netflix) 
  throughout their organization to run chaos engineering tests and generally
  glue together the code from their high-functioning polyglot teams. Netflix
  also wrote a 
  [2019 update for PyCon US](https://medium.com/netflix-techblog/python-at-netflix-bba45dae649e)
  to give more detail on what teams and projects work in Python.

* [Python 3 at Mozilla](https://ahal.ca/blog/2019/python-3-at-mozilla/)
  explains how their "build system, CI configuration, test harnesses, 
  command line tooling and countless other scripts, tools or Github projects 
  are all handled by Python". So just about everything a developer touches
  every day to build anything else needs Python to hook into the larger
  organization!

* [Google uses Python extensively](https://stackoverflow.com/questions/2560310/heavy-usage-of-python-at-google)
  and officially supports it internally as one of their three core languages,
  the other two being Java and Golang. While Google likely has every 
  programming language running somewhere in their infrastructure, Python 
  receives priority support due to its core language status.

* [Dropbox is well-known for using Python](https://techcrunch.com/2013/07/11/how-did-dropbox-scale-to-175m-users-a-former-engineer-details-the-early-days/)
  across their application development, infrastructure and operations. They
  also did a good job of cornering the market on hiring well-known Python 
  core contributors for a period of time, such as 
  [Guido van Rossum](https://blogs.dropbox.com/tech/2012/12/welcome-guido/) 
  and 
  [Jessica McKellar](https://opensource.com/business/16/7/red-hat-women-open-source-award-winner-jessica-mckellar) 
  (although Jessica is now at a new company that she co-founded). 

* [Facebook and Instagram use Python 3](https://thenewstack.io/instagram-makes-smooth-move-python-3/)
  at scale. They've been very vocal about successfully making the migration 
  from the [Python 2 world into Python 3](/python-2-or-3.html).

* A significant portion of [Reddit is built in Python](https://github.com/reddit?language=python)
  and it is one of the largest sites at scale to use the programming language.

* *Increment* covers usage of Python (and other programming languages) at
  Lyft, Digital Ocean, Sauce Labs, Slack and Fastly 
  [in this awesome overview post titled "What its like to be a developer at..."](https://increment.com/development/what-its-like-to-be-a-developer-at/).


## Government agencies
Python usage in government agencies is widespread despite the reputation of
agencies as stodgy late technology adopters. Organizations range from 
financial industry regulators like the SEC and CFPB, to intelligence agencies
like the CIA, FBI and NSA.

* The [Consumer Financial Protection Bureau (CFPB)](https://github.com/cfpb) 
  not only uses Python for running most of their applications but also open 
  sources many of those Python projects for other agencies (or any 
  organization) to use. For example, [collab](https://github.com/cfpb/collab)
  is a [Django](/django.html) project that provides an 
  [enterprise application](/enterprise-python.html) for storing and looking 
  up information on employees and contractors.

* [NASA uses Python extensively](https://www.python.org/about/success/usa/)
  and [open sources much of their software](https://code.nasa.gov/).

* The United States 
  [Central Intelligence Agency (CIA)](https://www.reddit.com/r/Python/comments/5y2boe/cia_uses_python_a_lot/)
  appears to be a huge fan of using Python in its state sponsored hacking 
  tools. They even published their own Python code conventions 
  documentation due to how many developers at the agency are using the
  language.

* The 
  [SEC uses Python and proposes organizations use Python to comply with regulations](http://jsdelfino.blogspot.com/2010/05/security-exchange-commission-python.html).

* A quick search for government jobs that require or recommend Python 
  [via USAJobs](https://www.usajobs.gov/Search/Results?k=python)
  turns up numerous listings at organizations such as the Smithsonian
  Institution, Department of Education, Department of the Navy and 
  National Institute of Standards and Technology (NIST).


## Industry-specific Python guides
Python is so widely used across various industries that developers have
written guides specific to their occupations for how to use Python. The
following resources are guides for using Python in astronomy, social
sciences and other fields rather than specific companies.

* [Practical Business Python](http://pbpython.com/) covers business-related
  topics such as how to automate generating large Excel spreadsheets or 
  perform analysis when your data is locked in Microsoft Office files.

* [Practical Python for Astronomers](https://python4astronomers.github.io/)
  gives open source workshop materials to teach astronomy students how to
  use Python for [data analysis](/data-analysis.html).

* [Python for the Humanities](http://fbkarsdorp.github.io/python-course/) is a
  textbook on the basics of text processing in Python. The material ramps 
  up quickly after the first chapter so you will likely want to combine 
  this walkthrough with other 
  [great Python learning resources](/best-python-resources.html).

* [Python for Social Scientists](http://www-rohan.sdsu.edu/~gawron/python_for_ss/)
  and 
  [Real Python's Python for Social Scientists](https://realpython.com/python-for-social-scientists/)
  walkthroughs are specific to fields that work with a lot of 
  [data](/data.html) gathered from studies such as psychology, sociology
  and economics.
