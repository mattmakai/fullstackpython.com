title: Unit Testing
category: page
slug: unit-testing
sortorder: 0436
toc: False
sidebartitle: Unit Testing
meta: Unit testing exercises one function isolated from a program. Learn more about unit testing on Full Stack Python.


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


## Unit testing tools
There are many tools for creating tests in Python. Some of these tools, such
as pytest, replace the built-in unittest framework. Other tools, such as
nose, are extensions that ease test case creation. Note that many of these
tools are also used for [integration testing](/integration-testing.html)
by writing the test cases to exercise multiple parts of code at once.

* [unittest](https://docs.python.org/3/library/unittest.html)
  is the built-in standard library tool for testing Python code.

* [pytest](https://docs.pytest.org/en/latest) is a complete testing tool 
  that emphasizes backwards-compatibility and minimizing boilerplate code.

* [nose](https://nose.readthedocs.org/en/latest/) is an extension to
  unittest that makes it easier to create and execute test cases.

* [Hypothesis](http://hypothesis.readthedocs.io/en/latest/index.html) is a 
  unit test-generation tool that assists developers in creating tests that
  exercise edge cases in code blocks. The best way to get started using 
  Hypothesis is by going through the well-written
  [quickstart](http://hypothesis.readthedocs.io/en/latest/quickstart.html).

* [mimesis](https://github.com/lk-geimfari/mimesis) generates synthetic test 
  data which is useful to apply in your tests.

* [testify](https://github.com/Yelp/Testify/) was a testing framework
  meant to replace the common unittest+nose combination. However, the team
  behind testify is transitioning to pytest so it's recommended you do
  not use testify for new projects.


### Unit testing resources
Unit tests are useful in every project regardless of programming language.
The following resources provide a good overview of unit testing from
several viewpoints and follow up with additional depth in testing 
Python-specific applications.

* [Introduction to Unit Testing](https://qunitjs.com/intro/)
  provides a broad introduction to unit testing, its importance and
  how to get started in your projects.

* [Unit Testing Your Twilio App Using Python’s Flask and Nose](https://www.twilio.com/blog/2014/03/unit-testing-your-twilio-app-using-pythons-flask-and-nose.html)
  is a detailed tutorial for using the nose test runner for ensuring a
  Flask application is working properly.

* [Understanding unit testing](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)
  explains why testing is important and shows how to do it effectively in
  your applications.

* [Unit testing with Python](http://www.drdobbs.com/testing/unit-testing-with-python/240165163)
  provides a high-level overview of testing and has diagrams to demonstrate
  what's going on in the testing cycle.

* The Python wiki has a page with a list of 
  [Python testing tools and extensions](https://wiki.python.org/moin/PythonTestingToolsTaxonomy).

* [An Extended Introduction to the nose Unit Testing Framework](http://ivory.idyll.org/articles/nose-intro.html)
  shows how this test runner can be used to write basic test suites.
  While the article is from 2006, it remains relevant today for learning
  how to use nose with your projects.

* [Revisiting Unit Testing and Mocking in Python](https://blog.fugue.co/2017-07-18-revisiting-unit-testing-and-mocking-in-python.html)
  is a wonderful post with many code examples showing how and
  why to use dependency injection and `@property` to mock unit
  tests.

* [Unit Testing Doesn’t Affect Codebases the Way You Would Think](https://blog.ndepend.com/unit-testing-affect-codebases/)
  presents research on how unit testing impacts project code and
  ways that it does not. It is only one research report but the findings
  on more unit tests leading to higher Cyclomatic Complexity per method
  are interesting. Perhaps more tests are needed to keep a project
  running due to the increased complexity.

* [Python unittest with Robert Collins](http://pythontesting.net/transcripts/19-python-unittest-robert-collins-2/)
  is the transcript of an interview with Robert Collins who is a core
  committer of `unittest`.

* [Precise Unit Tests with PyHamcrest](https://orbifold.xyz/pyhamcrest.html)
  is a short tutorial on using the 
  [PyHamcrest](https://github.com/hamcrest/PyHamcrest) assertion tool for
  unit testing.

* [Why most unit testing is a waste](https://rbcs-us.com/documents/Why-Most-Unit-Testing-is-Waste.pdf)
  discusses how low risk unit tests rarely fail even as the code
  changes and why they do not matter as much to a project's health as
  many developers are led to believe based on the test-driven development
  dogma.

* [Writing Unit Tests for Django Migrations](https://www.caktusgroup.com/blog/2016/02/02/writing-unit-tests-django-migrations/)
  digs into code examples for testing Django data migrations.

* [The business case for unit testing](https://www.typemock.com/business-case-unit-testing/)
  makes arguments for management should buy into unit testing,
  including risk management and faster development timelines. 

* Unit testing often requires a bunch of fake data to use as inputs that
  otherwise are generated by users or oother parts of a system not
  under test. Fake data generation tools can help create data instead
  of having too write it all yourself. This post on 
  [generating fake data with Faker](https://semaphoreci.com/community/tutorials/generating-fake-data-for-python-unit-tests-with-faker)
  shows how to use the Faker tool with various seeds and outputs into
  your tests.

* [Unit Testing Applications that use Flask-Login and Flask-SocketIO](https://blog.miguelgrinberg.com/post/unit-testing-applications-that-use-flask-login-and-flask-socketio)
  explains how to set up a [WebSockets](/websockets.html) unit test
  with a couple of common [Flask](/flask.html) libraries.
