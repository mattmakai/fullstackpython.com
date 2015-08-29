title: Unit Testing
category: page
slug: unit-testing
sort-order: 0802
meta: Unit testing exercises one function isolated from a program. Learn more about unit testing on Full Stack Python.


# Unit testing
Unit testing is a method of determining the correctness of a single function 
isolated from a larger codebase. The idea is that if all the atomic units
of an application work as intended in isolation, then integrating them 
together as intended is much easier.


## Why is unit testing important?
Unit testing is just one form of [testing](/testing.html) that works in
combination with other testing approaches to wring out the bugs from a
piece of software being developed. When several functions and classes are
put together it's often difficult to determine the source of a problem if
several bugs are occurring at the same time. Unit testing helps eliminate
as many of the individual bugs as possible so when the application comes
together as a whole the separate parts work as correct as possible. Then
when issues arise they can often be tracked down as unintended consequences
of the disparate pieces not fitting together properly.


### Unit testing resources
* [The Minimum Viable Test Suite](https://realpython.com/blog/python/the-minimum-viable-test-suite/)
  shows how to set unit tests and integration tests for a Flask example
  application.

* [Dive into Python 3's chapter on unit testing](http://www.diveintopython3.net/unit-testing.html)
  has a complete example with code and a detailed explanation for creating
  unit testing with the unittest module.

* [unittest](https://docs.python.org/3/library/unittest.html) is the 
  built-in standard library tool for testing Python code.
