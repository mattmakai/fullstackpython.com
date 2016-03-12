title: Testing
category: page
slug: testing
sortorder: 0801
toc: True
sidebartitle: 8. Testing
meta: Testing code is a vital part of developing Python applications. Learn more about testing on Full Stack Python.


# Testing
Testing determines whether software runs correctly based on specific inputs 
and identifies defects that need to be fixed.


## Why is testing important?
As software scales in codebase size, it's impossible for a person or even 
a large team to keep up with all of the changes and
the interactions between the changes. Automated testing is the only proven
method for building reliable software once they grow past the point of a
simple prototype. Many major software program development failures can be
traced back to inadequate or a complete lack of testing.

It's impossible to know whether software works properly unless it is tested.
While testing can be done manually, by a user clicking buttons or typing in 
input, it should be performed automatically by writing software programs that
test the application under test.

There are many forms of testing and they should all be used together. When 
a single function of a program is isolated for testing, that is called
[unit testing](/unit-testing.html). Testing more than a single function 
in an application at the same time is known as 
[integration testing](/integration-testing.html). 
*User interface testing* ensures the correctness of how a user would 
interact with the software. There are even more forms of testing that large
programs need, such as *load testing*, *database testing*, and
*browser testing* (for web applications).


## Testing in Python
Python software development culture is heavy on software testing. Because
Python is a dynamically-typed language as opposed to a statically-typed
language, testing takes on even greater importance for ensuring program
correctness.


## Testing resources
* [The Minimum Viable Test Suite](https://realpython.com/blog/python/the-minimum-viable-test-suite/)
  shows how to set unit tests and integration tests for a Flask example
  application.

* [Good test, bad test](http://late.am/post/2015/04/20/good-test-bad-test.html)
  explains the difference between a "good" test case and one that is not
  as useful. Along the way the post breaks down some myths about common
  testing subjects such as code coverage, assertions and mocking.

* [Python Testing](http://pythontesting.net/) is a site devoted to testing
  in - you guessed it - the Python programming language.

* [The case for test-driven development](http://michaeldehaan.net/post/120522567217/the-case-for-test-driven-development)
  by Michael DeHaan explains how automation is the only way to build software
  at a large scale.

* Google has a [testing blog](http://googletesting.blogspot.com/) where
  they write about various aspects of testing software at scale.

* Still confused about the difference between unit, functional and 
  integration tests? Check out this 
  [top answer on Stack Overflow](http://stackoverflow.com/questions/4904096/whats-the-difference-between-unit-functional-acceptance-and-integration-test) 
  to that very question.

* [Using pytest with Django](http://engineroom.trackmaven.com/blog/using-pytest-with-django/)
  shows how to get a basic [pytest](http://pytest.org/latest/) test
  running for a Django project and explains why the author prefers pytest 
  over standard unittest testing.

