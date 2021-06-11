title: AWS Lambda
category: page
slug: aws-lambda
sortorder: 0539
toc: False
sidebartitle: AWS Lambda
meta: AWS Lambda is a serverless compute service that can execute arbitrary Python 2.7, 3.6 or 3.7 code.


[Amazon Web Services (AWS) Lambda](https://aws.amazon.com/lambda/) 
is a compute service that executes arbitrary Python code in response 
to developer-defined AWS events, such as inbound API calls or file 
uploads to [AWS' Simple Storage Service (S3)](https://aws.amazon.com/s3/).

<a href="https://aws.amazon.com/lambda/" style="border:none"><img src="/img/logos/aws-lambda.jpg" width="100%" alt="AWS Lambda logo." class="shot outl rnd"></a>


## Why is Lambda useful?
Lambda is often used as a "serverless" compute architecture, which 
allows developers to upload their Python code instead of spinning and
configuring servers, deploying their code and scaling based on traffic. 

<div class="well see-also">Lambda is an implementation of the <a href="/serverless.html">serverless</a> concept. Learn how these pieces fit together in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Python on AWS Lambda
Lambda only had support for JavaScript, specifically Node.JS, when it was 
first released in late 2014. Python 2 developers were welcomed to the 
platform less than a year after its release, in October 2015. Lambda now 
has support for both Python 2.7, 3.6 and 3.7.


### Python-specific AWS Lambda resources
* [Serverless Slash Commands with Python](https://renzo.lucioni.xyz/serverless-slash-commands-with-python/)
  shows how to use the [Slack](/slack.html) API to build *slash* commands
  that run with an AWS Lambda backend.

* [Zappa](https://github.com/Miserlou/Zappa) is a serverless framework
  for deploying Python web applications. It's a really slick project
  and used even by internal AWS developers for their own application 
  deployments.

* [How to Setup a Serverless URL Shortener With API Gateway Lambda and DynamoDB on AWS](https://blog.ruanbekker.com/blog/2018/11/30/how-to-setup-a-serverless-url-shortener-with-api-gateway-lambda-and-dynamodb-on-aws/)
  builds a non-trivial URL shortener application as an example Python 
  application that runs on Lambda.

* [How we built Hamiltix.net for less than $1 a month on AWS](https://blog.badsectorlabs.com/how-we-built-hamiltixnet-for-less-than-1-a-month-on-aws.html)
  walks through setting up a full website that runs on AWS and scales
  with the Lambda free tier to minimize spend despite large traffic spikes.

* [Deploying a serverless Flask app to AWS Lambda using Zappa](https://asciinema.org/a/98560)
  provides a screen capture of one developer deploying their
  application to Lambda.

* [Automated SQL Injection Testing of Serverless Functions On a Shoestring Budget (and Some Good Music)](https://www.puresec.io/blog/automated-sql-injection-testing-of-serverless-functions-on-a-shoestring-budget-and-some-good-music)
  is an awesome operational security post that uses Python to test
  for SQL injection vulnerabilities in serverless functions on AWS Lambda.

* [Building Scikit-Learn For AWS Lambda](https://serverlesscode.com/post/scikitlearn-with-amazon-linux-container/)
  follows up on the 
  [Using Scikit-Learn In AWS Lambda](https://serverlesscode.com/post/deploy-scikitlearn-on-lamba/)
   post which shows how to perform scientific computing with Python
   packages on AWS Lambda.

* [Creating Serverless Functions with Python and AWS Lambda](https://hackernoon.com/creating-serverless-functions-with-python-and-aws-lambda-901d202d45dc)
  explains how to use the [Serverless framework](https://serverless.com/)
  to build Python applications that can be deployed to AWS Lambda.

* [Code Evaluation With AWS Lambda and API Gateway](https://realpython.com/blog/python/code-evaluation-with-aws-lambda-and-api-gateway/) 
  shows how to develop a code evaluation API, to execute arbitrary code, with AWS Lambda and API Gateway.

* [Crawling thousands of products using AWS Lambda](https://engineering.21buttons.com/crawling-thousands-of-products-using-aws-lambda-80332e259de1)
  gives a real-world example of where using Python, Selenium and 
  [headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)
  on AWS Lambda could crawl thousands of pages to collect data
  with each crawler running within its own Lambda Function.

* [Going Serverless with AWS Lambda and API Gateway](http://blog.ryankelly.us/2016/08/07/going-serverless-with-aws-lambda-and-api-gateway.html)


### General AWS Lambda resources
* [Getting started with serverless on AWS](https://emshea.com/post/serverless-getting-started)
  is a wonderful tutorials, example projects and additional resources
  guide created by a developer who used all of these bits to learn
  AWS services herself.

* [AWS Lambda Serverless Reference Architectures](http://www.allthingsdistributed.com/2016/06/aws-lambda-serverless-reference-architectures.html)
  provides blueprints with diagrams of common architecture patterns that
  developers use for their mobile backend, file processing, stream
  processing and web application projects.

* [Security Overview of AWS Lambda](https://d1.awsstatic.com/whitepapers/Overview-AWS-Lambda-Security.pdf)
  (PDF file) covers their "Shared Responsibility Model" for security and
  compliance. Although the paper bills itself as an in-depth look at 
  AWS Lambda security it is really more of a high-level overview, but still
  worth the read.

* [Reverse engineering AWS Lambda](https://www.denialof.services/lambda/)
  is an incredible, in-depth analysis of the author's work investigating
  the black box of how Lambda works and what he learned from it.

* The 
  [AWS Lambda tag](https://aws.amazon.com/blogs/aws/category/aws-lambda/)
  on the official AWS blog contains all the related first-party tutorials 

* [Serverless Cost Calculator](http://serverlesscalc.com/) estimates
  the amount that AWS would charge based on Lambda exeuctions, 
  average execution time and memory needed per execution. 

* [Serverless at Nordstrom](https://www.youtube.com/watch?v=8HHdEMWcvMI&index=9&list=PLnwBrRU5CSTmruZzR8Z06j3pGglBZcdDr)
  is an awesome real-world story with the architecture behind a serverless
  AWS Lambda application deployment at Nordstrom.

* [How was your experience with AWS Lambda in production?](https://news.ycombinator.com/item?id=14601809)
  has a good discussion of some of the benefits and issues that developers
  had as of mid-2017 with using Lambda for production applications.

* [Passwordless database authentication for AWS Lambda](https://cloudonaut.io/passwordless-database-authentication-for-aws-lambda/)
  shows how to use a MySQL backend from your Lambda functions.

* [How does language, memory and package size affect cold starts of AWS Lambda?](https://read.acloud.guru/does-coding-language-memory-or-package-size-affect-cold-starts-of-aws-lambda-a15e26d12c76)
  investigates the performance implications of various Lambda settings.

* [Best Practices for AWS Lambda Timeouts](https://epsagon.com/blog/best-practices-for-aws-lambda-timeouts/)
  explains some of the current hard upper limits on AWS timeouts, such
  as 5 minutes for Lambdas, when explicitly set that high, as well as
  29 seconds for API Gatway requests. There is also good advice on 
  how the circuit breaker pattern should be applied to your Lambdas
  and ultimately why low time outs are likely the best way to go to
  prevent your application from becoming entirely unresponsive.

* [X-rays for Flask and Django Serverless Applications](https://aws.amazon.com/blogs/developer/introducing-aws-x-ray-support-for-python-web-frameworks-used-in-serverless-applications/)
  is an instrumentation, monitoring and debugging service built into AWS
  Lambda specifically for Python [web frameworks](/web-frameworks.html) 
  running on the service.

* [Cutting Through the Layers: AWS Lambda Layers Explained](https://read.iopipe.com/cutting-through-the-layers-aws-lamba-layers-explained-28e8a8d7bda8)
  explains how AWS Lambda now offer a "Bring Your Own Runtime" by exposing
  the layers that were previously controlled exclusively by Amazon. There
  is an overview of the layers and why they matter for customizing your
  functions.
