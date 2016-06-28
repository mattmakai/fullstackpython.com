title: Integration Testing
category: page
slug: integration-testing
sortorder: 0803
toc: False
sidebartitle: Integration Testing
meta: Integration testing determines the correctness for several parts of a system under test at once. Learn more on Full Stack Python.


# Integration Testing
Integration testing exercises two or more parts of an application at once, 
including the interactions between the parts, to determine if they function
as intended. This type of [testing](/testing.html) identifies defects in 
the interfaces between disparate parts of a codebase as they invoke 
each other and pass data between themselves.


## How is integration testing different from unit testing?
While [unit testing](/unit-testing.html) is used to find bugs in individual
functions, integration testing tests the system as a whole. These two
approaches should be used together, instead of doing just one approach over
the other. When a system is comprehensively unit tested, it makes 
integration testing far easier because many of the bugs in the individual
components will have already been found and fixed. 

As a codebase scales up, both unit and integration testing allow 
developers to quickly identify breaking changes in their code. Many times
these breaking changes are unintended and wouldn't be known about until
later in the development cycle, potentially when an end user discovers 
the issue while using the software. Automated unit and integration tests
greatly increase the likelihood that bugs will be found as soon as possible
during development so they can be addressed immediately.


### Integration testing resources
* [Integration testing with Context Managers](http://eigenhombre.com/2013/04/13/integration-testing-in-python-with-context-managers/)
  gives an example of a system that needs integration tests and shows how
  context managers can be used to address the problem. There are a couple
  other useful posts in this series on testing including 
  [thoughts on integration testing](http://eigenhombre.com/2013/04/18/thoughts-on-integration-testing/)
  and [processes vs. threads for integration testing](http://eigenhombre.com/2013/04/19/processes-vs-threads-for-testing/).

* Pytest has a page on [integration good practices](https://pytest.org/latest/goodpractices.html)
  that you'll likely want to follow when testing your application.

* [Integration testing, or how to sleep well at night](http://enterprisecraftsmanship.com/2015/07/13/integration-testing-or-how-to-sleep-well-at-nights/)
  explains what integration tests are and gives an example. The example is 
  coded in Java but still relevant when you're learning about integration
  testing.

