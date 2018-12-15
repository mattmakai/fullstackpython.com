title: AWS Lambda
category: page
slug: aws-lambda
sortorder: 0539
toc: False
sidebartitle: AWS Lambda
meta: AWS Lambda is a serverless compute service that can execute arbitrary Python 2.7 and 3.6 code.


# AWS Lambda
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
* [Going Serverless with AWS Lambda and API Gateway](http://blog.ryankelly.us/2016/08/07/going-serverless-with-aws-lambda-and-api-gateway.html)

* [Zappa](https://github.com/Miserlou/Zappa) is a serverless framework
  for deploying Python web applications. It's a really slick project
  and used even by internal AWS developers for their own application 
  deployments. Be sure to [read the Zappa blog](https://blog.zappa.io/)
  as well for walkthroughs and new feature announcements.

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


### General AWS Lambda resources
* [AWS Lambda Serverless Reference Architectures](http://www.allthingsdistributed.com/2016/06/aws-lambda-serverless-reference-architectures.html)
  provides blueprints with diagrams of common architecture patterns that
  developers use for their mobile backend, file processing, stream
  processing and web application projects.

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
