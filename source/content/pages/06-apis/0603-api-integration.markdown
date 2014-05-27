title: API Integration
category: page
slug: api-integration
sort-order: 063
choice1url: /api-creation.html
choice1icon: fa-cubes
choice1text: How do I create an API for my own web application?
choice1url: /logging.html
choice2icon: fa-align-left fa-inverse 
choice2text: How do I use logging with my app?
choice3url: /web-application-security.html
choice3icon: fa-lock fa-inverse
choice3text: Where can I learn about web application security?
choice4url: /task-queues.html
choice4icon: fa-tasks
choice4text: How can I invoke APIs outside the HTTP request-response cycle?


# API Integration
The majority of production Python web applications rely on several
externally hosted application programming interfaces (APIs). APIs are also
commonly referred to as third party services or external platforms. 
Examples include [Twilio](https://www.twilio.com/) for messaging and voice
services, [Stripe](https://stripe.com/) for payment processing, and
[Disqus](https://disqus.com/) for embedded webpage comments.

There are many articles about proper API design but best practices for 
integrating APIs is less commonly written about. However, this subject 
continuously grows in importance because APIs provide critical functionality
across many implementation areas.


## Hosted API services
* [Runscope](https://www.runscope.com/) is a service specifically designed
  for APIs that assists developers with automated testing and traffic
  inspection.

* [Apiary](http://apiary.io/) provides a blueprint for creating APIs so
  they are easier to test and generate clean documentation.


## API Integration Resources
* John Sheehan's 
  "[Zen and the Art of API Maintenance](https://speakerdeck.com/johnsheehan/zen-and-the-art-of-api-maintenance)"
  slides are relevant for API integration.

* This post on 
  "[API Driven Development](https://stormpath.com/blog/api-driven-development/)"
  by Randall Degges explains how using APIs in your application cuts down
  on the amount of code you have to write and maintain so you can launch your
  application faster.

* [Safe Sex with Third Party APIs](http://www.slideshare.net/SmartBear_Software/safe-sex-with-thirdparty-apis)
  is a funny high level overview of what you should do to protect your 
  application when relying on third party services.

* My DjangoCon 2013 talk dove into 
  "[Making Django Play Nice With Third Party Services](http://www.youtube.com/watch?v=iGP8DQIqxXs)."


### What's next after integrating APIs into your app?
