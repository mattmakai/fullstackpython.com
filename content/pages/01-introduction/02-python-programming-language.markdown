title: Python Programming Language
category: page
slug: python-programming-language
sortorder: 0102
toc: False
sidebartitle: Core Language
meta: The core Python programming language includes a combination of features not found in many other languages.


The Python programming language is an 
[open source](https://www.python.org/downloads/source/), 
[widely-used](/why-use-python.html) tool for 
creating software applications.


## What is Python used for?
Python is often used to [build](/web-frameworks.html) and [deploy](/deployment.html) 
[web applications](/web-development.html) and 
[web APIs](/application-programming-interfaces.html). Python
can also analyze and visualize [data](/data.html) 
and [test software](/testing.html), even if the software being
tested was not written in Python.


## Language concepts
Python has several useful programming language concepts that are less 
frequently found in other languages. These concepts include:

* generators
* comprehensions
* [application dependency](/application-dependencies.html) handling via 
  the built-in [venv](https://www.python.org/dev/peps/pep-0405/) 
  ([as of Python 3.3](https://docs.python.org/3/whatsnew/3.3.html)) and
  [pip](https://www.python.org/dev/peps/pep-0453/) 
  ([as of Python 3.4](https://docs.python.org/3/whatsnew/3.4.html))
  commands


## Generators
Generators are a Python core language construct that allow a function's return
value to behave as an iterator. A generator can allow more efficient 
memory usage by allocating and deallocating memory during the context of a 
large number of iterations. Generators are defined in 
[PEP255](https://www.python.org/dev/peps/pep-0255/) and included in the
language as of Python 2.2 in 2001.


## Comprehensions
Comprehensions are a Python language construct for concisely creating data
in lists, dictionaries and sets. List comprehensions are included in Python 2
while dictionary and set comprehensions were introduced to the language in
Python 3.


## Why are comprehensions important?
Comprehensions are a more clear syntax for populating conditional data in the 
core Python data structures. Creating data without comprehensions often 
involves nested loops with conditionals that can be difficult for code
readers to properly evaluate.


## Example comprehensions code
List comprehension:

    >>> double_digit_evens = [e*2 for e in range(5, 50)]
    >>> double_digit_evens
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


Set comprehension:

    >>> double_digit_odds = {e*2+1 for e in range(5, 50)}
    {11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99}

Dictionary comprehension:
    
    >>> {e: e*10 for e in range(1, 11)}
    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}


### General Python language resources
* The [online Python tutor](http://www.pythontutor.com/) visually walks
  through code and shows how it executes on the Python interpreter.

* [Python Module of the Week](http://pymotw.com/2/index.html) is a tour
  through the Python standard library.

* [A Python interpreter written in Python](http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
  is incredibly meta but really useful for wrapping your head around some
  of the lower level stuff going on in the language.

* [A few things to remember while coding in Python](http://satyajit.ranjeev.in/2012/05/17/python-a-few-things-to-remember.html)
  is a nice collection of good practices to use while building programs
  with the language. 

* [Python internals: adding a new statement to Python](http://eli.thegreenplace.net/2010/06/30/python-internals-adding-a-new-statement-to-python/)

* [Python tricks that you can't live without](http://www.slideshare.net/audreyr/python-tricks-that-you-cant-live-without)
  is a slideshow by Audrey Roy that goes over code readability, linting,
  dependency isolation, and other good Python practices.

* [Python innards introduction](http://tech.blog.aknin.name/2010/04/02/pythons-innards-introduction/)
  explains how some of Python's internal execution happens.

* [What is a metaclass in Python](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)
  is one of the best Stack Overflow answers about Python.

* Armin Roacher presented [things you didn't know about Python](https://speakerdeck.com/mitsuhiko/didntknow)
  at PyCon South Africa in 2012.

* [Writing idiomatic Python](http://www.jeffknupp.com/blog/2012/10/04/writing-idiomatic-python/)
  is a guide for writing Pythonic code.


### Python ecosystem resources
There's an entire page on [best Python resources](/best-python-resources.html)
with links but the following resources are a better fit for when you're past 
the very beginner topics.

* The [Python Subreddit](http://www.reddit.com/r/python) rolls up great
  Python links and has an active community ready to answer questions from
  beginners and advanced Python developers alike.

* The blog [Free Python Tips](http://freepythontips.wordpress.com/) provides
  posts on Python topics as well as news for the Python ecosystem.

* [Python Books](http://pythonbooks.revolunet.com/) is a collection of freely
  available books on Python, Django, and data analysis.

* [Python IAQ: Infrequently Asked Questions](http://norvig.com/python-iaq.html)
  is a list of quirky queries on rare Python features and why certain syntax
  was or was not built into the language.

* [A practical introduction to Functional Programming for Python coders](https://codesachin.wordpress.com/2016/04/03/a-practical-introduction-to-functional-programming-for-python-coders/)
  is a good starter for developers looking to learn the functional 
  programming paradigm side of the language.

* [Getting Started with the Python Internals](http://akaptur.com/blog/2014/08/03/getting-started-with-python-internals/)
  takes a slice of the huge CPython codebase and deconstructs some of
  it to see what we can learn about how Python itself is built.


### Comprehension resources
* [Comprehending Python’s Comprehensions](https://dbader.org/blog/list-dict-set-comprehensions-in-python#intro)
  is an awesome post by Dan Bader with a slew of examples that explain
  how list, dictionary and set comprehensions should be used.

* [Python List Comprehensions: Explained Visually](http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)
  explains how the common idiom for iteration became syntactic sugar in
  the language itself and how you can use it in your own programs.

* The Python 3 Patterns and Idioms site has an overview of 
  [comprehensions](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Comprehensions.html)
  including code examples and diagrams to explain how they work.

* [Comprehensions in Python the Jedi way](https://gist.github.com/mjhea0/1c0031bd6fcd9263f844)
  shows off comprehensions with a Star Wars theme to walk through the nuts
  and bolts. All examples use Python 3.5.

* [Idiomatic Python: Comprehensions](https://blogs.msdn.microsoft.com/pythonengineering/2016/03/14/idiomatic-python-comprehensions/)
  explains how Python's comprehensions were inspired by Haskell's list
  comprehensions. It also provides clear examples that show how comprehensions
  are shorthand for common iteration code, such as copying one list into
  another while performing some operation on the contained elements.

* [List comprehensions in Python](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
  covers what the code for list comprehensions looks like and gives some
  example code to show how they work.

* [An Introduction to Python Lists](http://effbot.org/zone/python-list.htm)
  is a solid overview of Python lists in general and tangentially covers 
  list comprehensions.


### Python generator resources
* This blog post entitled 
  [Python Generators](http://rdrewd.blogspot.com/2014/02/python-generators.html)
  specifically focuses on generating dictionaries. It provides a good 
  introduction for those new to Python.

* [Generator Expressions in Python: An Introduction](https://dbader.org/blog/python-generator-expressions#intro)
  is the best all-around introduction to how to use generators and
  provides numerous code examples to learn from.

* [Python 201: An Intro to Generators](http://www.blog.pythonlibrary.org/2014/01/27/python-201-an-intro-to-generators/)
  is another short but informative read with example generators code.

* [Iterators & Generators](http://anandology.com/python-practice-book/iterators.html)
  provides code examples for these two constructs and some simple explanations
  for each one.

* [Python: Generators - How to use them and the benefits you receive](https://www.youtube.com/watch?v=bD05uGo_sVI)
  is a screencast with code that walks through generators in Python.

* The question to [Understanding Generators in Python?](http://stackoverflow.com/questions/1756096/understanding-generators-in-python)
  on Stack Overflow has an impressive answer that clearly lays out the
  code and concepts involved with Python generators.

* [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/)
  provides code examples for using generators. The material was originally
  presented in a PyCon workshop for systems programmers but is relevant to
  all Python developers working to understand appropriate ways to use
  generators.

