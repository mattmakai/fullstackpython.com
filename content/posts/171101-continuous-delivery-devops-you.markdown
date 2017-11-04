title: DevOps, Continuous Delivery... and You
slug: devops-continuous-delivery-you
meta: Talk slides, notes and more resources for a technical talk on basic DevOps and continuous delivery concepts, by Matt Makai.
category: post
date: 2017-11-01
modified: 2017-11-04
headerimage: /img/visuals/talk-header.jpg
headeralt: Comment bubble with code representing a technical talk-based blog post.


This blog post contains the slides along with a loose transcript and 
additional resources from my technical talk on DevOps and Continuous
Delivery concepts given at my alma mater, the University of Virginia,
to the [M.S. in Management of Information Technology program](https://www.commerce.virginia.edu/ms-mit) on November 2nd and 4th of 2017.

Links to learn more about the concepts presented in this talk can
be found in the sidebar and at the bottom of this page.

----


<img src="/img/171101-devops-cd-you/devops-cd-you.001.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Title slide for technical talk.">
Hey folks, my name is [Matt Makai](/about-author.html). I am a 
[software developer at Twilio](https://www.twilio.com/blog/2014/02/introducing-developer-evangelist-matt-makai.html)
and the creator of [Full Stack Python](https://www.fullstackpython.com/),
which over 125,000 developers read each month to learn how to 
[build](/web-development.html), [deploy](/deployment.html) and 
[operate](/devops.html) [Python-based applications](/why-use-python.html).


<img src="/img/171101-devops-cd-you/devops-cd-you.004.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="What's the point of Agile?">
You've talked about using the Agile software development methodology
on your teams, but what's the purpose? Why does Agile development matter 
to you and your organization?


<img src="/img/171101-devops-cd-you/devops-cd-you.005.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Cargo ship with containers.">
Agile matters because it allows you to ship more code, faster than 
traditional "waterfall" methodology approaches. 

Shipping is a common allegory in software development nowadays, because 
code that is not in production, in the hands of your users, doesn't create
value for anyone.

If code is not running in production, it's not creating value. New
code created by your Agile development teams every couple of weeks does
not create more value until it is executing in production.


<img src="/img/171101-devops-cd-you/devops-cd-you.006.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Docker logo.">
Shipping code is so important to high functioning companies that the
maritime theme is used across all sorts of projects, including in the Docker
logo.


<img src="/img/171101-devops-cd-you/devops-cd-you.007.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Kubernetes logo.">
As well as in the Kubernetes logo in the form of a ship steering wheel.


<img src="/img/171101-devops-cd-you/devops-cd-you.008.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Agile sprints need to ship code into production to create anything of value.">
Here is a super high-level diagram of the ideal scenario we need for
Agile development teams. Create working code and get it shipped as soon
as possible into production.


<img src="/img/171101-devops-cd-you/devops-cd-you.009.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Move fast and break things.">
Facebook's internal motto used to be "Move fast and break things." They 
thought that if you aren't breaking things then you aren't moving fast 
enough. 


<img src="/img/171101-devops-cd-you/devops-cd-you.010.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="If you do not have the right processes and tools in place eventually production will break.">
And eventually if you're constantly shipping to production and you do not
have the appropriate processes and tools in place, your applications
will break. The breakage has nothing to do with the Agile methodology
itself.

Your team and organization will come to a fork in the road when you
end up with a broken environment.


<img src="/img/171101-devops-cd-you/devops-cd-you.011.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Fight the urge to put manual processes in place that slow you down. You must automate.">
Traditionally, organizations have tried to prevent breakage by putting
more manual tools and processes in place. Manual labor slows... down...
your... ability... to... execute.

This is one path provided by the fork in the road. Put your "Enterprise
Change Review Boards" in place. Require production sign-offs by some 
Executive Vice President who has never written a line of code in his life.
Put several dozen "technical architects" in a room together to argue over
who gets to deploy their changes to production that month.

The manual path is insanity. Eventually the best developers in your
organization will get frustrated and leave. Executives will ask why
nothing ever gets done. Why does it take our organization three years
to ship a small change to a critical application?


<img src="/img/171101-devops-cd-you/devops-cd-you.012.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Some teams try to get around the production problem by shipping to dev, but they still are not creating value.">
Some development teams try to get around the manual production challenges
by shipping everything to a development environment. The dev environment is
under their control.

But what's the huge glaring problem in this situation?

If you are not shipping to production, then you are not creating any value
for your users. The teams have made a rational decision to ship to development
but the organization still suffers due to the manual controls.


<img src="/img/171101-devops-cd-you/devops-cd-you.013.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="This session is about DevOps and Continuous Delivery.">
The problems we are talking about are created by the Agile methodology
because they become acute when your development team is producing code at
high velocity. Once code is created faster, you need a way to reliably,
consistently put the code into production so that it can create value for
its users.

DevOps and Continuous Delivery are the broad terms that encompass how to
reliably ship code to production and operate it when the code is running in 
production.


<img src="/img/171101-devops-cd-you/devops-cd-you.014.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="What DevOps is NOT.">
We are going to use the terms "DevOps" and "Continuous Delivery" a lot today,
so let's start by defining what they mean. In fact, the term "DevOps" has 
already accumulated a lot of buzzword baggage, so we'll start by defining
what DevOps is *not*.

First,DevOps is not a new role. If you go hire a bunch of people and call them
"DevOps engineers" then sit them in the middle of your developers and system
admin/ops folks, you are going to have a bad time. You just added a new layer
between the two groups you need to pull closer together.

Second, DevOps is not a specific tool or application. You do not need to
use Docker or Puppet to do DevOps in your organization. The processes that
make DevOps work are made much easier by some tools such as cloud platforms
where infrastructure is transient, but even those platforms are not required
to do DevOps right.

Third, DevOps is not tied to a specific programming language ecosystem. You
do not need to use Node.js or Ruby on Rails. You can still use DevOps
in a COBOL- or J2EE-only organization.


<img src="/img/171101-devops-cd-you/devops-cd-you.015.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="What DevOps IS.">
With those misconceptions out of the way, let's talk about what DevOps IS.
First, at the risk of being way too obvious, DevOps is the combination of the
two words Development and Operations. This combination is not a random
pairing, it's an intentional term. 

Second, DevOps means your application developers handle operations. Not 
necessarily *all* operations work, but ops work that deals with the code they
write and deploy as part of their sprints. The developers also will likely
become intimately familiar with the underlying infrastructure such as the
web application servers, [web servers](/web-servers.html) and 
[deployment](/deployment.html) code for 
[configuration management](/configuration-management.html) tools.

Third, DevOps allows your organization to be more efficient in handling
issues by ensuring the correct person is handling errors and application
failures.


<img src="/img/171101-devops-cd-you/devops-cd-you.016.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="What Continuous Delivery is.">
We are not going to go through Continuous Delivery (CD) by defining what it is
not, but there are a couple bits to say about it. First, CD is a collection of 
engineering practices aimed at automating the delivery of code from 
version control check-in until it is running in a production environment.

The benefit of the automation CD approach is that your organization will have
far greater confidence in the code running in production even as the code
itself changes more frequently with every deployment.


<img src="/img/171101-devops-cd-you/devops-cd-you.017.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Move fast and BUILD things.">
Facebook's original motto changed a few years ago to "Move Fast and Build 
Things" because they realized that breaking production was not a byproduct
of moving fast, it was a result of immature organizational processes and
tools. DevOps and Continuous Delivery are why organizations can now deploy
hundreds or thousands of times to production every day but have increasing,
not decreasing, confidence in their systems as they continue to move faster.

Let's take a look at a couple of example scenarios that drive home what
DevOps and CD are all about, as well as learn about some of the processes, 
concepts and tools that fall in this domain.


<img src="/img/171101-devops-cd-you/devops-cd-you.018.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="San Francisco skyline at night.">
Here is a beautiful evening picture of the city I just moved away from, San 
Francisco.


<img src="/img/171101-devops-cd-you/devops-cd-you.019.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Twilio billboard, ask your developer!">
The company I work for, [Twilio](https://www.twilio.com/) is located in
San Francisco. If you ever fly into the SFO airport and catch a ride towards
downtown, you will see our billboard on the right side of the road. 

Twilio makes it easy for software developers to add communications, such as
phone calling, messaging and video, into their applications. We are a 
telecommunications company built with the power of software that eliminates
the need for customers to buy all the expensive legacy hardware that they
used to have to acquire. As a telecomm company, we can never go down, or
our customers are hosed and then our business is hosed.

However, we have had challenges in our history that have forced us to 
confront the fork in the road between manual processes and moving faster via 
trust in our automation.


<img src="/img/171101-devops-cd-you/devops-cd-you.020.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="August 2013.">
In August 2013, Twilio faced an infrastructure failure.


<img src="/img/171101-devops-cd-you/devops-cd-you.021.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="How customers pay for Twilio.">
First, some context. When a developer signs up for Twilio, she puts some 
credit on their account and the credit is drawn upon by making phone calls,
sending messages and such. When credit runs low we can re-charge your card
so you get more credit.


<img src="/img/171101-devops-cd-you/devops-cd-you.022.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Hacker News post on Twilio not billing correctly.">
There was a major production issue with the recurring charges in August 2013.
Our engineers were alerted to the errors and the issue blew up on the top of
[Hacker News](https://news.ycombinator.com/), drawing widespread atttention.

So now there is a major production error... what do we do?


<img src="/img/171101-devops-cd-you/devops-cd-you.023.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Billing incident update blog post.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.024.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Redis logo.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.025.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'Root cause?'">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.026.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Billing incident response from Twilio developer evangelist.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.027.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Twilio status page.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.028.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Twilio number of production deployments.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.029.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'tools and concepts'.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.030.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Eventually you ship code into production that breaks your application.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.031.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'automated testing' with example code coverage in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.032.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Automated tests in dev only deploy to production when they are successful.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.033.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Bugs can still occur in production.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.034.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'monitoring and alerting' with New Relic dashboard in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.035.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="When something breaks in prod, your developers know about it and can fix the problem.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.036.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="When production is running smoothly with many tests, do that increase the chance of black swan-type events?">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.037.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'Chaos engineering' with the chaos engineering monkey logo in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.038.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Chaos engineering introduces intentional failures in your infrastructure both on a scheduled and unschedule basis.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.039.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads '1. other peoples money' with money in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.040.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads '2. other peoples lives' with people in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.041.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'War on Terror' with an exploded vehicle in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.042.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="U.S. military and civilian casualties in Iraq.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.043.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Biometrics devices.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.044.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Eclipse IDE.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.045.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="The situation did not have reasonable deployments to dev or to production.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.046.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Start somewhere, automate your deployments to dev environment.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.047.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Some environments have tricky issues with automated prod deployments like disconnected networks.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.048.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'Tools and concepts'.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.049.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Several development teams commit to a Git repository.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.050.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'continuous integration' with a screenshot of Jenkins dashboard in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.051.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Add a continuous integration server to build the code that is committed to your source control repository.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.052.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="How do we automate the building of these environments and the deployments themselves?">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.053.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Text that reads 'configuration management' with a screenshot of Ansible AWX in the background.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.054.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Agile sprints deliver code to a development environment and then automate the deployment into production.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.055.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Review list of continuous delivery tools.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.056.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="A list of more concepts and tools for continuous delivery.">

...


<img src="/img/171101-devops-cd-you/devops-cd-you.057.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Thank you slide.">

That's all for today. My name is [Matt Makai](/about-author.html)
and I'm a software developer at [Twilio](/twilio.html) and the
author of [Full Stack Python](https://www.fullstackpython.com/),
thank you very much.


----

Additional resources to learn more about the following topics can be found
on their respective pages:

* [Deployments](/deployments.html)
* [Continuous integration](/continuous-integration.html)
* [Serverless computing](/serverless.html)
* [AWS Lambda](/aws-lambda.html)
* [Static site generators](/static-site-generator.html)
* [Monitoring](/monitoring.html)
* [DevOps](/devops.html)
* [Configuration management](/configuration-management.html)
* [Platform-as-a-Service (PaaS)](/platform-as-a-service.html)
* [Docker](/docker.html)
* [Web application security](/web-application-security.html)
* [Testing](/testing.html)
* [Source control](/source-control.html)
* [Git](/git.html)
* [Hosted source control services](/hosted-source-control-services.html)
* [GitHub](/github.html)
* [Code metrics](/code-metrics.html)
* [NoSQL](/no-sql-datastore.html)
