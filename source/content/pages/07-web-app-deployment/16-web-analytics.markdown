title: Web Analytics
category: page
slug: web-analytics
sortorder: 0716
toc: False
sidebartitle: Web Analytics
meta: Web analytics tools collect and visualize data from visitors so developers can better serve users. Learn more about web analytics on Full Stack Python.


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
as heatmaps and action funnels.


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

* [Clicky](http://clicky.com/) provides real-time analytics comparable to
  Google Analytics' real-time dashboard.

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


## Python-specific web analytics resources
* [Building an Analytics App with Flask](http://charlesleifer.com/blog/saturday-morning-hacks-building-an-analytics-app-with-flask/)
  is a detailed walkthrough for collecting and analyzing webpage
  analytics with your own Flask app.

* [Pandas and Google Analytics](http://blog.yhathq.com/posts/pandas-google-analytics.html)
  shows how to use pandas for data analysis with Google Analytics' API to
  perform calculations not available in the tool itself.

* [Build your own Google Analytics Dashboard in Excel](http://blog.zoomeranalytics.com/google-analytics/)
  show how to extract your Google Analytics data via their web API and Python
  helper library so it can be used in other tools such as Excel.


## General web analytics resources
* [Google Analytics for Developers](http://blog.arkency.com/2012/12/google-analytics-for-developers/)  

* This beginner's guide to 
  [math and stats behind web analytics](http://www.seotakeaways.com/beginners-guide-maths-stats-web-analytics/)
  provides some context for understanding and reasoning about web traffic. 

* [An Analytics Primer for Developers](https://hacks.mozilla.org/2015/03/an-analytics-primer-for-developers/)
  by Mozilla explains what to track, choosing an analytics platform and how
  to serve up the analytics JavaScript asynchronously.

* This post provides context for determining if a given metric is
  ["vanity" or actionable](http://fizzle.co/sparkline/vanity-vs-actionable-metrics).


## Web analytics learning checklist
1. Add Google Analytics or Piwik to your application. Both are free and while 
   Piwik is not as powerful as Google Analytics you can self-host the 
   application which is the only option in many environments.

1. Think critically about the factors that will make your application 
   successful. These factors will vary based on whether it's an internal 
   [enterprise](/enterprise-python.html) app, an e-commerce site or an 
   information-based application.

1. Add metrics generated from your web traffic based on the factors that 
   drive your application's success. You can add these metrics with either 
   some custom code or with a hosted web analytics service.

1. Continuously reevaluate whether the metrics you've chosen are still the 
   appropriate ones defining your application's success. Improve and refine 
   the metrics generated by the web analytics as necessary.

