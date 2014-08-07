title: Web Analytics
category: page
slug: web-analytics
sort-order: 083
choice1url: /web-application-security.html
choice1icon: fa-lock fa-inverse
choice1text: What should I know about web application security?
choice2url: /api-integration.html
choice2icon: fa-link fa-inverse
choice2text: How do I integrate external APIs into my web application?
choice3url: /configuration-management.html
choice3icon: fa-gears
choice3text: I want to learn how to automate setting up my app.
choice4url: /task-queues.html
choice4icon: fa-tasks
choice4text: How do I run code outside the HTTP request-response cycle?


# Web analytics
Web analytics involves collecting, processing, visualizing web data to enable
critical thinking about how users interact with a web application.


## Why is web analytics important?
User clients, especially web browsers, generate significant data while users
read and interact with webpages. The data provides insight into 
how visitors use the site and why they stay or leave. The key concept to
analytics is *learning* about your users so you can improve your web 
application to better suit their needs. 


## Web analytics concepts
It's easy to get overwhelmed at both the number of analytics services and
the numerous types of data points collected. Focus on just a handful of
metrics when you're just starting out. As your application scales and you 
understand more about your users add additional analytics services 
to gain further insight into their behavior with advanced visualizations such
as heatmaps and action funnels. The
[seven stages of startup analytics grief](http://spenczar.com/posts/2013/Sep/07/seven-stages-analytics-grief/) 
post is an amusing read and provides context for how to begin and then grow 
tracked metrics over time.


### User funnels
If your application is
selling a product or service you can ultimately build a 
[user funnel](http://moz.com/blog/building-your-marketing-funnel-with-google-analytics) (often called "sales funnel" prior to a user becoming a customer)
to better understand why people buy or don't buy what you're selling. With
a funnel you can visualize drop-off points where visitors leave your 
application before taking some action, such as purchasing your service.


## Open source web analytics projects
* [Piwik](http://piwik.org/) is a web analytics platform you can host yourself.
  Piwik is a solid choice if you cannot use Google Analytics or want to 
  customize your own web analytics platform.

* [Open Web Analytics](http://www.openwebanalytics.com/) is another 
  self-hosted platform that integrates through a JavaScript snippet that
  tracks users' interactions with the webpage.


## Hosted web analytics services
* [Google Analytics](http://www.google.com/analytics/) is a widely used
  free analytics tool for website traffic.

* [MixPanel](https://mixpanel.com/)'s analytics platform focuses on mobile
  and sales funnel metrics. A developer builds what data points need to be
  collected into the server side or client side code. MixPanel captures that
  data and provides metrics and visualizations based on the data.

* [KISSmetrics](https://www.kissmetrics.com/)' analytics provides context
  for who is visiting a website and what actions they are taking while on
  the site.

* [Heap](https://heapanalytics.com/) is a recently founded analytics service
  with a free introductory tier to get started.

* [CrazyEgg](http://www.crazyegg.com/) is tool for understanding a
  user's focus while using a website based on heatmaps generated from mouse 
  movements. 


## Web analytics resources
* [Google Analytics for Developers](http://blog.arkency.com/2012/12/google-analytics-for-developers/)  

* [Pandas and Google Analytics](http://blog.yhathq.com/posts/pandas-google-analytics.html)
  shows how to use pandas for data analysis with Google Analytics' API to
  perform calculations not available in the tool itself.

* This beginner's guide to 
  [math and stats behind web analytics](http://www.seotakeaways.com/beginners-guide-maths-stats-web-analytics/)
  provides some context for understanding and reasoning about web traffic. 

* This post provides context for determining if a given metric is
  ["vanity" or actionable](http://fizzle.co/sparkline/vanity-vs-actionable-metrics).

* Read this post on [how your analytics software actually works](http://www.bayesianwitch.com/blog/2013/howyouranalyticswork.html)
  to get a better understanding of what's going on behind the scenes from
  a technical perspective.

* [Heap vs MixPanel](http://substantial.com/blog/2014/04/03/heap-analytics-vs-mixpanel/)
  compares the two analytics services.


## Web analytics learning checklist
<i class="fa fa-check-square-o"></i>
Add Google Analytics or Piwik to your application. Both are free and while 
Piwik is not as powerful as Google Analytics you can self-host the application
which is the only option in many environments.

<i class="fa fa-check-square-o"></i>
Think critically about the factors that will make your application successful.
These factors will vary based on whether it's an internal enterprise app, 
an e-commerce site or an information-based application.

<i class="fa fa-check-square-o"></i>
Add metrics generated from your web traffic based on the factors that drive
your application's success. You can add these metrics with either some custom
code or with a hosted web analytics service.

<i class="fa fa-check-square-o"></i>
Continuously reevaluate whether the metrics you've chosen are still the 
appropriate ones defining your application's success. Improve and refine the
metrics generated by the web analytics as necessary.


### What's the next topic you want to learn about?
