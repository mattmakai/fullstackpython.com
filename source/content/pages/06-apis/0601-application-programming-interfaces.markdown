title: Application Programming Interfaces
category: page
slug: application-programming-interfaces
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
choice4url: /api-creation.html
choice4icon: fa-cubes
choice4text: How do I create an API for my own web application?


# Application Programming Interfaces
Application programming interfaces (APIs) provide machine-readable
data transfer and signaling between applications.


## Why are APIs important?
HTML, CSS and JavaScript create human-readable webpages. However, those 
webpages are not easily consumable by other machines. Numerous scraping
programs and libraries exist to rip data out of HTML but it's simpler
to consume data through APIs.


## Webhooks
A webhook is a user-defined HTTP callback to a URL that executes when a 
system condition is met. The call alerts the second system via a POST or GET
request and often passes data as well.

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


## CSS learning checklist
<i class="fa fa-check-square-o"></i> 
Learn the API concepts of machine-to-machine communication with JSON and XML,
endpoints and webhooks.

<i class="fa fa-check-square-o"></i> 
Integrate an API such as Twilio or Stripe into your web application. Read the
[API integration](/api-integration.html) section for more information.

<i class="fa fa-check-square-o"></i> 
Use a framework to create an API for your own application. 

<i class="fa fa-check-square-o"></i> 
Expose your web application's API so other applications can consume data you
want to share.


### What's next after learning about APIs?
