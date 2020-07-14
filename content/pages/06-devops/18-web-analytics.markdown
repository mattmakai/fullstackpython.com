title: Web Analytics
category: page
slug: web-analytics
sortorder: 0618
toc: False
sidebartitle: Web Analytics
meta: Web analytics tools collect and visualize data from website visitors. Learn more on Full Stack Python.


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

* [Shynet](https://github.com/milesmcc/shynet) is a lightweight, privacy-friendly 
  cookie-free web analytics application written in Python.

* [Open Web Analytics](http://www.openwebanalytics.com/) is another 
  self-hosted platform that integrates through a JavaScript snippet that
  tracks users' interactions with the webpage.


## Hosted web analytics services
* [Google Analytics](http://www.google.com/analytics/) is a widely used
  free analytics tool for website traffic.

* [Clicky](https://clicky.com/) provides real-time analytics comparable to
  Google Analytics' real-time dashboard.

* [MixPanel](https://mixpanel.com/)'s analytics platform focuses on mobile
  and sales funnel metrics. A developer builds what data points need to be
  collected into the server side or client side code. MixPanel captures that
  data and provides metrics and visualizations based on the data.

* [Heap](https://heapanalytics.com/) is a recently founded analytics service
  with a free introductory tier to get started.

* [CrazyEgg](https://www.crazyegg.com/) is tool for understanding a
  user's focus while using a website based on heatmaps generated from mouse 
  movements. 


### Python-specific web analytics resources
* [Building an Analytics App with Flask](http://charlesleifer.com/blog/saturday-morning-hacks-building-an-analytics-app-with-flask/)
  is a detailed walkthrough for collecting and analyzing webpage
  analytics with your own Flask app.

* [Build a Google Analytics Slack Bot with Python](https://www.twilio.com/blog/2018/03/google-analytics-slack-bot-python.html)
  explains how to connect the Google Analytics API to a [Slack](/slack.html) 
  bot, with all the code in Python, so you can query for Google Analytics 
  data from your Slack channels.

* [Automating web analytics through Python](https://rrighart.github.io/GA/)
  is a tutorial for interacting with your Google Analytics data using 
  [pandas](/pandas.html) and related [data analysis](/data-analysis.html) 
  tools.

* The official 
  [Google Analytics Python quickstart](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py)
  isn't really the easiest tutorial to follow due to all of the configuration
  required to make your first API call, but it is still the right place to go
  to get started.

* [How Accurately Can Prophet Project Website Traffic?](https://pbpython.com/prophet-accuracy.html)
  uses the data forecasting tool 
  [Prophet](https://facebook.github.io/prophet/) to see if it is possible
  to predict future trends in website traffic based on historical data.


### General web analytics resources
* [The Google Analytics Setup I Use on Every Site I Build](https://philipwalton.com/articles/the-google-analytics-setup-i-use-on-every-site-i-build/)
  is a tutorial written for developers to better understand the scope
  of what Google Analytics can tell you about your site and how
  to configure it for better output.

* [Roll your own analytics](https://www.pcmaffey.com/roll-your-own-analytics/)
  shows you how to use [AWS Lambda](/aws-lambda.html) and some custom 
  JavaScript to create your own replacement for Google Analytics. This route
  is not for everyone but it is really useful if you want to avoid the Google
  data trap.

* [An Analytics Primer for Developers](https://hacks.mozilla.org/2015/03/an-analytics-primer-for-developers/)
  by Mozilla explains what to track, choosing an analytics platform and how
  to serve up the analytics JavaScript asynchronously.

* [Options for Hosting Your Own Non-JavaScript-Based Analytics](https://css-tricks.com/options-for-hosting-your-own-non-javascript-based-analytics/)
  has a few non-Google Analytics web analytics tools that mostly rely
  on server-side rather than client-side tracking.

* This post provides context for determining if a given metric is
  ["vanity" or actionable](http://fizzle.co/sparkline/vanity-vs-actionable-metrics).

* This series on measuring your technical content has a bunch of advice
  for figuring out why you want to gather metrics, how to do the
  instrumentation and determining your success factors.

    * [Part 1 covers "why"](https://docsbydesign.com/2017/08/24/measuring-your-technical-content-part-1/)
    * [Part 2 examines success factors](https://docsbydesign.com/2017/08/27/measuring-your-technical-content-part-2/)
    * [Part 3 digs further into measurement](https://docsbydesign.com/2017/08/29/measuring-your-technical-content-part-3/)

* [awesome-analytics](https://github.com/onurakpolat/awesome-analytics) 
  aggregates analytics tools for both web and mobile applications.

* [10 red flags signaling your analytics program will fail](https://www.mckinsey.com/business-functions/mckinsey-analytics/our-insights/ten-red-flags-signaling-your-analytics-program-will-fail)
  is a more business-focused piece but it has sosme good information and
  visualization on broader themes that developers who work in larger
  organizations should think about when it comes to analytics.


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

