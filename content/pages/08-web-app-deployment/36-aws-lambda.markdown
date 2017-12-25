title: AWS Lambda
category: page
slug: aws-lambda
sortorder: 0836
toc: False
sidebartitle: AWS Lambda
meta: AWS Lambda is a serverless compute service that can execute arbitrary Python 2.7 and 3.6 code.


# AWS Lambda
[Amazon Web Services (AWS) Lambda](https://aws.amazon.com/lambda/) 
is a compute service that executes arbitrary Python code in response 
to developer-defined AWS events, such as inbound API calls or file 
uploads to [AWS' Simple Storage Service (S3)](https://aws.amazon.com/s3/).

<a href="https://aws.amazon.com/lambda/" style="border:none"><img src="/img/logos/aws-lambda.jpg" width="100%" alt="AWS Lambda logo." class="technical-diagram" style="border-radius:6px"></a>


## Why is Lambda useful?
Lambda is often used as a "serverless" compute architecture, which 
allows developers to upload their Python code instead of spinning and
configuring servers, deploying their code and scaling based on traffic. 

<div class="well see-also">Lambda is an implementation of the <a href="/serverless.html">serverless</a> concept. Learn how these pieces fit together in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


## Python on AWS Lambda
Lambda only had support for JavaScript, specifically Node.JS, when it was 
first released in late 2014. Python 2 developers were welcomed to the 
platform less than a year after its release, in October 2015. Lambda now 
has support for both Python 2.7 and 3.6.


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

* [Building Scikit-Learn For AWS Lambda](https://serverlesscode.com/post/scikitlearn-with-amazon-linux-container/)

* [Code Evaluation With AWS Lambda and API Gateway](https://realpython.com/blog/python/code-evaluation-with-aws-lambda-and-api-gateway/) shows how to develop a code evaluation API, to execute arbitrary code, with AWS Lambda and API Gateway.


### General AWS Lambda resources
* [The Serverless Start-Up - Down With Servers!](http://highscalability.com/blog/2015/12/7/the-serverless-start-up-down-with-servers.html)

* [AWS Lambda Serverless Reference Architectures](http://www.allthingsdistributed.com/2016/06/aws-lambda-serverless-reference-architectures.html)

* The 
  [AWS Lambda tag](https://aws.amazon.com/blogs/aws/category/aws-lambda/)
  on the official AWS blog contains all the related first-party tutorials 

* [Serverless Cost Calculator](http://serverlesscalc.com/) estimates
  the amount that AWS would charge based on Lambda exeuctions, 
  average execution time and memory needed per execution. 

* [Serverless at Nordstrom](https://www.youtube.com/watch?v=8HHdEMWcvMI&index=9&list=PLnwBrRU5CSTmruZzR8Z06j3pGglBZcdDr)
  is an awesome real-world story with the architecture behind a serverless
  AWS Lambda application deployment at Nordstrom.

