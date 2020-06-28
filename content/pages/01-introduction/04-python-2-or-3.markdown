title: Python 2 or 3?
category: page
slug: python-2-or-3
sortorder: 0104
toc: False
sidebartitle: Python 2 or 3?
meta: Learn about whether you should use Python version 2 or 3 to build your applications.


The Python programming language is almost finished with a long-term transition
from version 2 to version 3. New programmers often have questions about which 
version they should learn. It can be confusing to hear that Python 3, which was 
originally released in 2008, is still not the default installation on some 
operating systems such as macOS. However, that situation is rapidly changing 
as the final version 2 release, Python 2.7, is approaching its end-of-life
that is definitively scheduled for 
[January 1, 2020](https://mail.python.org/pipermail/python-dev/2018-March/152348.html).

The simple answer right now is: *learn Python 3*, specifically the latest 
version which as of October 2019 is 
[Python 3.7](https://www.python.org/downloads/). If for some reason you 
absolutely have to learn Python 2, for example because your employer is 
working on a bunch of legacy code, you will be able to transfer the majority
of your knowledge from Python 2 right into Python 3. Likewise, you will 
still be able to read and write Python 2 code if you start with Python 3.

There are enough [great resources](/best-python-resources.html)
out there that will teach you to code in version 3 without any prior
version 2 experience. Python 3 is the future and you will not regret 
starting with the latest version of the 
[programming language](/learning-programming.html).

There is one small caveat to the recommendation to go full-on Python 3. 
You may infrequently come across lesser-used open source code libraries
that were originally written in Python 2 that do not completely support
Python 3. That was the case before 2019 with [DevOps](/devops.html) 
[configuration management tools](/configuration-management.html) such as 
[Fabric](http://www.fabfile.org/) or [Ansible](/ansible.html). However,
those libraries now support Python 3 and the usage problems that were
frequent in years past are now typically not a concern. Knowing how
to upgrade Python 2 libraries to 3.x is still a useful skill to apply
at the edges of the Python open source community.


## Visualizations and Projects
Since upgrading from Python 2 to 3 has been such a huge undertaking within
the community, many projects have sprung up to make the transition easier.

* [six](https://pypi.org/project/six/) is a 2/3 compatibility library that
  is a dependency for many popular Python projects to make it easier to
  support both Python 2 and 3 at the same time.

* [Python 3 Readiness](http://py3readiness.org/) is a visualization of
  which most popular 360 libraries (by downloads) are ready to be
  used with Python 3.

* The [Python clock](https://pythonclock.org/) counts down the time until
  Python 2.x is no longer maintained. While Python 2's retirement
  may still seem a long time away, it can take a lot of time and effort to 
  migrate existing application to the modified syntax in 3.x.


### Porting to Python 3 resources
Moving an existing codebase to Python 3 from 2 can be a daunting task,
These resources were created by fellow developers who've previously
gone through the process and have advice for making it less painful.

* [Python 3 Porting](http://python3porting.com/) is an entire book with
  details for how to upgrade your existing projects and libraries to 
  Python 3.x.
  
* [Moving from Python 2 to Python 3](http://ptgmedia.pearsoncmg.com/imprint_downloads/informit/promotions/python/python2python3.pdf)
  is a PDF cheatsheet for porting your Python code.

* The official 
  [porting code to Python 3](https://wiki.python.org/moin/PortingToPy3k/)
  page links to resources on porting Python code as well as underlying C
  implementations. There is also a 
  [quick reference for writting code with Python 2 and 3 compatibility](https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef).

* [Upgrading to Python 3 with Zero Downtime](https://tech.yplanapp.com/2016/08/24/upgrading-to-python-3-with-zero-downtime/)
  supplies advice on transitioning a large existing Python 2 web application 
  to Python 3. Their process involved upgrading dependencies, testing and
  deploying the new version before going back to clean up unnecessary code
  created by the transition.

* [Migrating to Python 3 with pleasure](https://github.com/arogozhnikov/python3_with_pleasure)
  is a porting guide that focuses on code that data scientists would 
  typically use in their programs.

* [Instagram Makes a Smooth Move to Python 3](https://thenewstack.io/instagram-makes-smooth-move-python-3/)
  explains their upgrade process for getting all of their code over to
  Python 3 compatibility over a period of about a year.

* [Practical steps for moving to Python 3](https://talkpython.fm/episodes/show/155/practical-steps-for-moving-to-python-3)
  is a podcast episode that goes over migrating a large existing application's 
  codebase to Python 3 from Python 2.

* [Lessons learned from migrating to Python 3](https://able.bio/rhett/lessons-learned-from-migrating-to-python-3--27jsj82)
  covers how a development team with a large e-commerce site built on 
  [Django](/django.html) was able to upgrade their project.


### Python 2 to 3 resources
The following resources will give you more context on how the community
feels the transition from Python 2 to 3 is going, as well as why you
should upgrade as soon as possible.

* [Why should I use Python 3?](https://eev.ee/blog/2016/07/31/python-faq-why-should-i-use-python-3/)
  is a detailed FAQ on important topics such as unicode support, iteration
  improvements and async upgrades provided by 3.x. There is also a great
  follow up post by the author titled 
  [A Rebuttal For Python 3](https://eev.ee/blog/2016/11/23/a-rebuttal-for-python-3/)
  that counters some arguments made by other community members who are
  unhappy about various features in Python 3.

* Want to know all of the advantages and what's changed in Python 3 
  compared to Python 2? There's 
  [an official guide to Python 3 changes](https://docs.python.org/3/whatsnew/index.html)
  you'll want to read.

* [Python 3 is winning](https://blogs.msdn.microsoft.com/pythonengineering/2016/03/08/python-3-is-winning/)
  presents data and graphs from PyPI to show that at the current rate,
  by mid-2016 overall Python 3 library support will overtake Python 2 
  support.

* [Python 3 Retrospective from the Benevolent Dictator for Life ](https://www.youtube.com/watch?v=Oiw23yfqQy8)
  is a talk by Guido van Rossum on what is working, not working and still
  needs to be done before the changover can be considered complete.

* [The stages of the Python 3 transition](http://www.snarky.ca/the-stages-of-the-python-3-transition)
  provides perspective from a core Python developer on how the transition from
  Python 2 to 3 is going as of the end of 2015.

* [How Dropbox rolled out one of the largest Python 3 migrations ever](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/)
  explains how their transition began in 2015 and was successfully completed
  in 2018. There is also a follow up post on
  [incrementally migrating over one million lines of code from Python 2 to Python 3](https://blogs.dropbox.com/tech/2019/02/incrementally-migrating-over-one-million-lines-of-code-from-python-2-to-python-3/)
  that has more details on how hack weeks were able to help make enough
  progress so the engineers could better estimate the scope of work when 
  the transition from 2 to 3 became critical to their development toolchain.

* [Zato: A successful Python 3 migration story](https://zato.io/blog/posts/python-3-migration-success-story.html)
  examines the background, preparation, execution and testing of moving
  an existing Python 2 code base over to Python 3.

* [Why Python 3?](http://whypy3.com/) randomly outputs valid reasons to
  use Python 3 over 2.x.

* [Rules for Radicals: Changing the Culture of Python at Facebook](https://www.youtube.com/watch?v=nRtp9NgtXiA)
  is a fascinating look at how Facebook moved from primarily Python 2
  up to Python 3 due to the efforts of a small passionate group of
  developers within the company. Definitely worth watching to understand
  how to shift a large organization with an established codebase.

* [Porting to Python 3 is like eating your vegetables](http://nothingbutsnark.svbtle.com/porting-to-python-3-is-like-eating-your-vegetables)
  explains that there are treats in Python 3 that are worth porting for and
  has some tips on making the transition easier.

* [Scrapy on the road to Python 3 support](http://blog.scrapinghub.com/2015/08/19/scrapy-on-the-road-to-python-3-support/)
  explains from the perspective of a widely used Python project what their
  plan is for supporting Python 3 and why it has taken so long to make it 
  happen.

* All major scientific Python libraries have 
  [pledged to drop Python 2 support](https://python3statement.github.io/)
  no later than 2020, when Python 2's maintenance life is over. The pledge 
  strongly encourages Python 3 adoption by publicly stating their
  intentions. 

* [10 awesome features of Python that you can't use because you refuse to upgrade to Python 3](http://www.asmeurer.com/python3-presentation/slides.html)
  is a great slideshow with code snippets that show useful new features
  of Python 3 that are not available in 2.x such as keyword-only
  arguments, chained exceptions and the `yield from` keyword.

* [Python 2 vs 3, what's different?](https://python-commandments.org/python-2-vs-3/) 
  goes over some of the differences between Python 2 and Python 3
  
