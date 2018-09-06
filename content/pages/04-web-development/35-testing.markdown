title: Testing
category: page
slug: testing
sortorder: 0435
toc: False
sidebartitle: Testing
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

* [BDD Testing a Restful Web Application in Python](https://semaphoreci.com/community/tutorials/bdd-testing-a-restful-web-application-in-python)
  is an introduction to behavior-driven development (BDD) and uses
  a [Flask](/flask.html) web application as an example project for
  learning.

* [Testing, for people who hate testing](https://eev.ee/blog/2016/08/22/testing-for-people-who-hate-testing/)
  provides examples for how to improve your testing environment such
  as using a new test harness and getting your test suite to run fast.

* [Getting started with Pytest](https://jacobian.org/writing/getting-started-with-pytest/)
  goes over some code challenges as examples for how to use Pytest in
  your own projects.

* [Good test, bad test](http://late.am/post/2015/04/20/good-test-bad-test.html)
  explains the difference between a "good" test case and one that is not
  as useful. Along the way the post breaks down some myths about common
  testing subjects such as code coverage, assertions and mocking.

* [Python Testing](http://pythontesting.net/) is a site devoted to testing
  in - you guessed it - the Python programming language.

* Google has a [testing blog](http://googletesting.blogspot.com/) where
  they write about various aspects of testing software at scale.

* [A beginner's guide to Python testing](https://miguelgfierro.com/blog/2018/a-beginners-guide-to-python-testing/)
  covers test-driven development for unit, integration and smoke tests.

* Still confused about the difference between unit, functional and 
  integration tests? Check out this 
  [top answer on Stack Overflow](http://stackoverflow.com/questions/4904096/whats-the-difference-between-unit-functional-acceptance-and-integration-test) 
  to that very question.

* [Using pytest with Django](http://engineroom.trackmaven.com/blog/using-pytest-with-django/)
  shows how to get a basic [pytest](http://pytest.org/latest/) test
  running for a Django project and explains why the author prefers pytest 
  over standard unittest testing.
  
* [Distributed Testing with Selenium Grid and Docker](https://testdriven.io/distributed-testing-with-selenium-grid) shows how to distribute automated, browser tests with Selenium Grid and Docker Swarm. It also looks at how to run tests against a number of browsers and automate the provisioning and deprovisioning of machines to keep costs down.

* [Principles of Automated Testing](http://www.lihaoyi.com/post/PrinciplesofAutomatedTesting.html)
  explains how to prioritize what to test, goes through some levels of
  testing from [unit](/unit-testing.html) to 
  [integration](/integration-testing.html) and examines when to use example
  and bulk tests.


### Mocking resources
Mocking allows you to isolate parts of your code under test and avoid
areas that are not critical to the tests you are writing. For example,
you may want to test how you handle text message responses but do not
want to actually receive text messages in your application. You can
mock a part of the code that would provide a happy-path scenario so
you can run your tests properly. The following resources show you how to
use mocks in your test cases.

* [Getting Started with Mocking in Python](https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python)
  provides a whole code example based on a blog project that shows
  how to use `mock` when testing.

* [Python Mocking 101: Fake It Before You Make It](https://blog.fugue.co/2016-02-11-python-mocking-101.html)
  explains what mocking is and is not, and shows how to use the `patch`
  function to accomplish it in your project. 
  [Revisiting Unit Testing and Mocking in Python](https://blog.fugue.co/2017-07-18-revisiting-unit-testing-and-mocking-in-python.html)
  is a follow-up post that expands upon using the `patch` function
  along with dependency injection.

* [Mocks and Monkeypatching in Python](https://semaphoreci.com/community/tutorials/mocks-and-monkeypatching-in-python)
  uses the `mock` and `monkeypatch` tools to show how to mock your
  test cases.

* [Mock yourself, not your tests](http://hernantz.github.io/mock-yourself-not-your-tests.html)
  examines when mocks are necessary and when they are not as useful
  so you can avoid them in your test cases.

* [Mocking Redis & Expiration in Python](http://malexandre.fr/2017/10/08/mocking-redis--expiration-in-python/)
  is a specific scenario where you would want to test your
  [Redis](/redis.html)-dependent code but prefer to mock it rather than
  ensure an installation and connection are present whenever you run
  your tests.
