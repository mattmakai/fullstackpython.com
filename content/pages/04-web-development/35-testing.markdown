title: Testing
category: page
slug: testing
sortorder: 0435
toc: False
sidebartitle: Testing
meta: Testing code is a vital part of developing Python applications. Learn more about testing on Full Stack Python.


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


## Python testing tools
The Python ecosystem has a wealth of tools to make it easier to run
your tests and interpret the results. The following tools encompass
test runners, coverage reports and related libraries.

* [green](https://github.com/cleancut/green) is a test runner that has
  pretty printing on output to make the results easier to read and
  understand.

* [requestium](https://github.com/tryolabs/requestium) merges the
  Requests library with Selenium to make it easier to run automated
  browser tests.

* [coverage.py](https://coverage.readthedocs.io/) is a tool for
  measuring code coverage when running tests.


### Testing resources
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

* [Getting started with Pytest](https://jacobian.org/2016/nov/27/getting-started-with-pytest/)
  goes over some code challenges as examples for how to use Pytest in
  your own projects.

* [Good test, bad test](http://late.am/post/2015/04/20/good-test-bad-test.html)
  explains the difference between a "good" test case and one that is not
  as useful. Along the way the post breaks down some myths about common
  testing subjects such as code coverage, assertions and mocking.

* [Python Testing](http://pythontesting.net/) is a site devoted to testing
  in - you guessed it - the Python programming language.

* [In praise of property-based testing](https://increment.com/testing/in-praise-of-property-based-testing/)
  is an article by the author of the [Hypothesis](https://hypothesis.works/)
  testing tool written in Python. The article explains the shortcomings of 
  example-based tests and how property-based testing can augment or replace
  those example-based tests to find more defects in software. There is also
  a great 
  [introductory post on Hypothesis](https://hypothesis.works/articles/incremental-property-based-testing/)
  that goes into further detail about getting your first Hypothesis tests
  up and running.

* Google has a [testing blog](http://googletesting.blogspot.com/) where
  they write about various aspects of testing software at scale.

* [A beginner's guide to Python testing](https://miguelgfierro.com/blog/2018/a-beginners-guide-to-python-testing/)
  covers test-driven development for unit, integration and smoke tests.

* [Testing a Twilio Interactive Voice Response (IVR) System With Python and pytest](https://www.twilio.com/blog/testing-twilio-ivr-system-python-pytest)
  is an incredibly in-depth tutorial on testing a Python-powered IVR
  using pytest. There is also a tutorial on 
  [how to build the IVR before this testing tutorial](https://www.twilio.com/blog/building-interactive-voice-response-ivr-system-python-django-twilio),
  although you can just clone it to jump into the testing walkthrough.

* Still confused about the difference between unit, functional and 
  integration tests? Check out this 
  [top answer on Stack Overflow](http://stackoverflow.com/questions/4904096/whats-the-difference-between-unit-functional-acceptance-and-integration-test) 
  to that very question.

* [Testing Python applications with Pytest](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)
  walks through the basics of using Pytest and some more advanced
  ways to use it such as continuous testing through Semiphore CI.

* [The cleaning hand of Pytest](https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684)
  provides a couple of case studies for how companies set up their testing
  systems. It then gives the boilerplate code the author uses for Pytest
  and goes through a bunch of code samples for common situations. 

* [Using pytest with Django](http://engineroom.trackmaven.com/blog/using-pytest-with-django/)
  shows how to get a basic [pytest](https://docs.pytest.org/en/latest/) test
  case running for a Django project and explains why the author prefers 
  pytest over standard unittest testing.

* [Distributed Testing with Selenium Grid and Docker](https://testdriven.io/distributed-testing-with-selenium-grid) 
  shows how to distribute automated, browser tests with Selenium Grid and 
  Docker Swarm. It also looks at how to run tests against a number of 
  browsers and automate the provisioning and deprovisioning of machines to 
  keep costs down.

* [Principles of Automated Testing](http://www.lihaoyi.com/post/PrinciplesofAutomatedTesting.html)
  explains how to prioritize what to test, goes through some levels of
  testing from [unit](/unit-testing.html) to 
  [integration](/integration-testing.html) and examines when to use example
  and bulk tests.

* [How to run tests continuously while coding](https://www.blog.pythonlibrary.org/2017/03/14/how-to-run-python-tests-continuously-while-coding/)
  contains a Python script that uses the 
  [watchdog](https://pythonhosted.org/watchdog/) to check for changes
  to source code files in your project directory. If changes are detected 
  then your tests will be run to check that everything is still working
  as intended.

* [8 great pytest plugins](https://opensource.com/article/18/6/pytest-plugins)
  is a list of plugins that go with PyTest and help with tasks like reducing 
  the friction around testing [Django](/django.html), as well as running
  tests in parallel.

* This test-driven development series shows you how to write an interpreter
  in Python and contains a ton of great code samples to learn from:

    * [A game of tokens: write an interpreter in Python with TDD - Part 1](http://blog.thedigitalcatonline.com/blog/2017/05/09/a-game-of-tokens-write-an-interpreter-in-python-with-tdd-part-1/)
    * [A game of tokens - part 2](http://blog.thedigitalcatonline.com/blog/2017/10/01/a-game-of-tokens-write-an-interpreter-in-python-with-tdd-part-2/)
    * [A game of tokens - part 3](http://blog.thedigitalcatonline.com/blog/2017/10/31/a-game-of-tokens-write-an-interpreter-in-python-with-tdd-part-3/)
    * [A game of tokens - part 4](http://blog.thedigitalcatonline.com/blog/2018/06/02/a-game-of-tokens-write-an-interpreter-in-python-with-tdd-part-4/)

* [Pytest leaking](https://nvbn.github.io/2017/02/02/pytest-leaking/)
  examines situations where tests leak memory and can cause abnormal
  results if they are not fixed.


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

* [Better tests for Redis integrations with redislite](https://www.obeythetestinggoat.com/better-tests-for-redis-integrations-with-redislite.html)
  is a great example of how using the right mocking library can clean
  up existing hacky testing code and make it more straightforward for
  any developer that happens upon the tests in the future.
