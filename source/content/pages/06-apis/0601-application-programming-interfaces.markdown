title: Application Programming Interfaces
category: page
slug: application-programming-intefaces
sort-order: 061
choice1url: /api-integration.html
choice1icon: fa-link
choice1text: How do I integrate external APIs into my application?
choice2url: /task-queues.html
choice2icon: fa-tasks
choice2text: How can I invoke APIs outside the HTTP request-response cycle?
choice3url: /web-application-security.html
choice3icon: fa-lock fa-inverse
choice3text: Where can I learn about web application security?
choice4url:
choice4icon:
choice4text: 


# Application Programming Interfaces
Application programming interfaces (APIs) provide machine-readable
data transfer and signaling between applications.


## Why are APIs important?
HTML, CSS and JavaScript create human-readable webpages. However, those 
webpages are not easily consumable by other machines. Numerous scraping
programs and libraries exist to rip data out of HTML but it's simpler
to consume data through APIs.


## Webhook
A webhook is a user-defined HTTP callback to a URL that executes when on a 
system condition is met. The call alerts the second system and often passes
data as well.

Webhooks are important because they enable two-way communication initiation 
for APIs. Webhook flexibility comes in from their definition by the API user
instead of the API itself.

For example, in the [Twilio API](https://www.twilio.com/api) when a text 
message is sent to a Twilio phone number Twilio sends an HTTP POST request 
webhook to the URL specified by the user. The URL is defined in a text box
on the number's page on Twilio as shown below.

<img src="theme/img/twilio-webhook-definition.jpg" width="100%" alt="Webhook definition in the Twilio API." class="technical-diagram" />



## API open source projects
* [Swagger](https://github.com/wordnik/swagger-core) is an open source project 
  written in Scala that defines a standard interface for RESTful APIs.


## API resources
* [Zapier](https://zapier.com/) has an
  [APIs 101](https://zapier.com/blog/apis-101/) free guide for what APIs 
  are, why they are valuable and how to use them properly. 



### What's next after learning about APIs?
