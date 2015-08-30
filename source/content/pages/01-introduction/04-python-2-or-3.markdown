title: Python 2 or 3?
category: page
slug: python-2-or-3
sort-order: 0104
meta: Learn about whether you should use Python version 2 or 3 to build your applications.


# Python 2 or 3?
The Python programming language is currently in the midst of a long-term
transition from version 2 to version 3. New programmers typically have many
questions about which version they should learn. It's confusing to hear
that Python 3, which was originally released in 2008, is still not the default
installation on many operating systems.

Here's the good news: you can't go wrong starting with either version. While 
there are differences in unicode and syntax, for the most part if you 
start with Python 2 and then learn Python 3 you won't be starting from 
scratch. Likewise, you'll be able to read and write Python 2 code if you 
started with Python 3.

My personal recommendation for new programmers as of right now is to start
with Python 3. There are enough [great resources](/best-python-resources.html)
out there that teach version 3 from the ground up.

However, if you are interested in DevOps-type work with 
[configuration management tools](/configuration-management.html) such as 
Ansible or Fabric, then you'll have to stick to Python 2 because they have
yet to upgrade to support Python 3. If you know there are libraries you must
use in a project, check the 
[Python Walls of Superpowers](https://python3wos.appspot.com/). If you're
using Django, there is also a wall specifically for 
[Python 3 compatibility of popular Django packages](http://djangowos.com/).


### Python 2 to 3 resources
* The official 
  [porting code to Python 3](https://wiki.python.org/moin/PortingToPy3k/)
  page links to resources on porting Python code as well as underlying C
  implementations. There is also a 
  [quick reference for writting code with Python 2 and 3 compatibility](https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef).

* [Porting to Python 3 is like eating your vegetables](http://nothingbutsnark.svbtle.com/porting-to-python-3-is-like-eating-your-vegetables)
  explains that there are treats in Python 3 that are worth porting for and
  has some tips on making the transition easier.

* [Moving from Python 2 to Python 3](http://ptgmedia.pearsoncmg.com/imprint_downloads/informit/promotions/python/python2python3.pdf)
  is a PDF cheatsheet for porting your Python code.

* [Django and Python 3 How to Setup pyenv for Multiple Pythons](https://godjango.com/96-django-and-python-3-how-to-setup-pyenv-for-multiple-pythons/)
  is a screencast showing how to run both Python 2 and 3 for different
  projects using pyenv.

* [Scrapy on the road to Python 3 support](http://blog.scrapinghub.com/2015/08/19/scrapy-on-the-road-to-python-3-support/)
  explains from the perspective of a widely used Python project what their
  plan is for supporting Python 3 and why it has taken so long to make it 
  happen.

