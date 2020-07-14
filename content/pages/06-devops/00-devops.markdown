title: DevOps
category: page
slug: devops
sortorder: 0600
toc: True
sidebartitle: 6. DevOps
meta: DevOps combines software development and application operations. Python is often used in the DevOps toolchain.


DevOps is the combination of [application development](/web-development.html)
and operations, which minimizes or eliminates the disconnect between 
software developers who build applications and systems administrators 
who keep infrastructure running.


## Why is DevOps important?
When the Agile methodology is properly used to develop software, a new
bottleneck often appears during the frequent [deployment](/deployment.html) 
and operations phases. New updates and fixes are produced so fast in each 
sprint that infrastructure teams can be overwhelmed with deployments and 
push back on the pace of delivery. To alleviate some of these issues, 
application developers are asked to work closely with operations folks to
automate the delivery of code from development to production. 


## DevOps tooling resources
DevOps cannot be performed with tools alone, but having the right tools
to augment the culture and processes is important to successful software
delivery. The following resources discuss both Python-specific and general
tools and services for DevOps environments.

* [DevOps: Python tools to get started](https://speakerdeck.com/victorneo/devops-python-tools-to-get-started)
  is a presentation slideshow that explains that while DevOps is a culture, 
  it can be supported by tools such as Fabric, Jenkins, BuildBot and Git
  which when used properly can enable continuous software delivery.

* For an Atlassian-centric perspective on tooling, take a look at 
  this post on how to
  [choose the right DevOps tools](http://blogs.atlassian.com/2016/03/how-to-choose-devops-tools/)
  which is biased towards their tools but still has some good insight
  such as using automated testing to provide immediate awareness of 
  defects that require fixing.


## General DevOps resources
The following resources give advice and approaches for building the right
teams, culture, processes and tools into software development organizations.

* [DevOps vs. Platform Engineering](https://alexgaynor.net/2015/mar/06/devops-vs-platform-engineering/)
  considers DevOps an ad hoc approach to developing software while building
  a platform is a strict contract. I see this as "DevOps is a process", 
  while a "platform is code". Running code is better than any organizational 
  process.

* The open source 
  [PagerDuty Incident Response guide](https://response.pagerduty.com/) is the
  amazing result from their company taking the practices they use to keep
  their services running and putting them out for other developers to consume.
  Highly recommended.

* [Operations for software developers for beginners](https://jvns.ca/blog/2016/10/15/operations-for-software-developers-for-beginners/)
  gives advice to developers who have never done operations work and
  been on call for outages before in their career. The advantage of DevOps
  is greater ownership for developers who built the applications running
  in production. The disadvantage of course is the greater ownership
  also leads to much greater responsibility when something breaks!

* Google's 
  [Site Reliability Engineering (SRE) book](https://landing.google.com/sre/book/index.html)
  is free online and required reading for understanding the practices and
  principles behind keeping the largest websites alive. Note though that
  some of the advice in the book will be considered controversial at more
  stodgy traditional organizations that have done operations differently
  for a long time. There is also 
  [a wonderful interview with Ben Treynor](https://landing.google.com/sre/interview/ben-treynor/), 
  one of the authors of the book, that contains additional information.

* [The Increment](https://increment.com/), Stripe's fantastic digital and
  print magazine, has 
  [an issue dedicated to being on-call](https://increment.com/on-call/)
  which discusses many DevOps-related topics such as what happens when
  your pager goes off, ownership and how startups can be different from
  large companies with their incident responses.

* [Bing: Continuous Delivery](http://engineering.microsoft.com/bing-continuous-delivery/)
  is an impressive visual story that explains the practices for how their
  team delivers updates to the search engine.

* [Why are we racing to DevOps?](http://www.cio.com/article/3015237/application-development/why-are-we-racing-to-devops.html)
  is a very high level summary of the benefits of DevOps to IT organizations.
  It's not specific to Python and doesn't dive into the details, but it's 
  a decent start for figuring out why IT organizations consider DevOps the
  hot new topic after adopting an Agile development methodology.

* [SRE vs. DevOps: competing standards or close friends?](https://cloudplatform.googleblog.com/2018/05/SRE-vs-DevOps-competing-standards-or-close-friends.html)
  covers Google's take on how Site Reliability Engineering (SRE) fits
  with the DevOps world. Roughly speaking, SRE is more closely aligned with
  metrics and how to operate infrastructure and applications, rather than
  the broader principles embodied by the DevOps philosophy.
