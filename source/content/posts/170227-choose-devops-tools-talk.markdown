title: How to Choose the Right DevOps Tools for You and Your Team
slug: choose-right-devops-tools
meta: Talk slides, notes and more resources for a technical talk on choosing appropriate DevOps tools, by Matt Makai.
category: post
date: 2017-02-27
modified: 2017-02-27
headerimage: /source/static/img/170227-choose-devops-tools/header.jpg
headeralt: Comment bubble with code representing a technical talk-based blog post.


This blog post contains a loose transcript along with the slides and 
additional resources from my technical talk that will be given at 
[Oracle Code SF 2017](https://developer.oracle.com/code/sanfrancisco),
[Devoxx San Jose 2017](https://devoxx.us/) 
and [DC Continuous Delivery](https://www.meetup.com/DC-continuous-delivery/) 
within the next couple of months.

Additional resources to learn more about [deployments](/deployments.html),
[configuration management](/configuration-management.html) and 
[DevOps](/devops.html) are listed at the end of the post.

----


<img src="/source/static/img/170227-choose-devops-tools/title-slide.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Title slide for technical talk.">

Hey folks, my name is Matt Makai. I'm a 
[Developer Evangelist with Twilio](https://www.twilio.com/blog/2014/02/introducing-developer-evangelist-matt-makai.html)
and the creator of [Full Stack Python](https://www.fullstackpython.com/).


<img src="/source/static/img/170227-choose-devops-tools/python-swift-love.jpg" width="100%" class="technical-diagram img-rounded" alt="Python and Swift logos with the heart eyes emoji.">

...


<img src="/source/static/img/170227-choose-devops-tools/java-only.jpg" width="100%" class="technical-diagram img-rounded" alt="Java programming language logo.">

...


<img src="/source/static/img/170227-choose-devops-tools/dark-ages.jpg" width="100%" class="technical-diagram img-rounded" alt="2004, the dark ages of software development?">

...


<img src="/source/static/img/170227-choose-devops-tools/different-versions.jpg" width="100%" class="technical-diagram img-rounded" alt="Diff two commits on GitHub.">

...


<img src="/source/static/img/170227-choose-devops-tools/pat-on-back.jpg" width="100%" class="technical-diagram img-rounded" alt="Give yourself a pat on the back.">

...


<img src="/source/static/img/170227-choose-devops-tools/git-logo.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Git logo.">

...


<img src="/source/static/img/170227-choose-devops-tools/question-1.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Do you know a developer who strongly recommends a tool after 4+ years?">

...


<img src="/source/static/img/170227-choose-devops-tools/question-2.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="What is the difference between a concept and an implementation?">

...


<img src="/source/static/img/170227-choose-devops-tools/devops-1-layer.png" width="100%" class="technical-diagram img-rounded" alt="Source control (version control) as bottom layer in DevOps.">

...


<img src="/source/static/img/170227-choose-devops-tools/question-3.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Question 3: On a 0 (lowest) -> 10 scale, how amenable is your organization to improving the technical environment?">

...


<img src="/source/static/img/170227-choose-devops-tools/question-4.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Question 4: How many people on your team get stoked about making incremental fixes to your technical environment?">

...


<img src="/source/static/img/170227-choose-devops-tools/devops-2-layers.png" width="100%" class="technical-diagram img-rounded" alt="CI, automated tests and app dependencies as layer 2 in DevOps.">

...


<img src="/source/static/img/170227-choose-devops-tools/continuous-integration-implementations.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Open source and hosted versions of CI, such as Jenkins, GoCD, and StriderCI, along with CircleCI, Travis CI and CodeBuild.">

...


<img src="/source/static/img/170227-choose-devops-tools/test-automation.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Test automation concepts and their implementations in Python ecosystem as examples.">

...


<img src="/source/static/img/170227-choose-devops-tools/bash.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="$bash.">

...


<img src="/source/static/img/170227-choose-devops-tools/python-fabric-logo.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Python Fabric library logo.">

...


<img src="/source/static/img/170227-choose-devops-tools/ansible-logo.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Ansible logo.">

...


<img src="/source/static/img/170227-choose-devops-tools/devops-3-layers.png" width="100%" class="technical-diagram img-rounded" alt="Configuration management and automated deployments in layer 3 of DevOps.">

...


<img src="/source/static/img/170227-choose-devops-tools/configuration-management-tools.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Configuration management implementations such as Ansible, Chef, Puppet and SaltStack.">

...


<img src="/source/static/img/170227-choose-devops-tools/ansible-commands.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Example for Ansible YAML command to install packages through apt.">

...


<img src="/source/static/img/170227-choose-devops-tools/question-5.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="How many times per day does your team deploy to test? How about production?">

...


<img src="/source/static/img/170227-choose-devops-tools/question-6.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="How many times per day do you want to deploy to test? To production?">

...


<img src="/source/static/img/170227-choose-devops-tools/question-7.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="What are the top 5 specific impediments to completing automating your deployments?">

...


<img src="/source/static/img/170227-choose-devops-tools/question-8.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Who on your team gets excited about continuous delivery?">

...


<img src="/source/static/img/170227-choose-devops-tools/question-9.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Who on your team is responsible for improving automated deployments and continuous delivery?">

...


<img src="/source/static/img/170227-choose-devops-tools/django-logo.jpg" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Django logo.">

...


<img src="/source/static/img/170227-choose-devops-tools/devops-4-layers.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Monitoring, logging and measuring in layer 4 of DevOps.">

...


<img src="/source/static/img/170227-choose-devops-tools/question-10.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="What metrics do you collect that feed into every sprint?">

...


<img src="/source/static/img/170227-choose-devops-tools/question-11.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="How many days would it take to put a new code library into production?">

...


<img src="/source/static/img/170227-choose-devops-tools/deploys-2016.jpg" width="100%" class="technical-diagram img-rounded" alt="6,643 deploys per year for Twilio in 2015.">

...


<img src="/source/static/img/170227-choose-devops-tools/question-12.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="How much money, if any, can you spend to jump start monitoring your environment?">

...


<img src="/source/static/img/170227-choose-devops-tools/devops-4-layers.png" width="100%" class="technical-diagram img-rounded" alt="Repeat monitoring, loggin and measuring in 4 layer DevOps slide.">

...


<img src="/source/static/img/170227-choose-devops-tools/contact-info.png" width="100%" class="technical-diagram img-rounded" style="border: 1px solid #aaa" alt="Contact info end slide.">

My name is Matt Makai and I'm a Developer Evangelist with Twilio, a Python
and Swift developer, as well as the author of 
[Full Stack Python](https://www.fullstackpython.com/). You can get in
touch with me via these channels. Thank you!


