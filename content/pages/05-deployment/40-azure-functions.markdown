title: Azure Functions
category: page
slug: azure-functions
sortorder: 0540
toc: False
sidebartitle: Azure Functions
meta: Azure Functions is a serverless compute service that can execute Python 3.6 code.


[Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/)
is a compute service created by Microsoft that can execute Python code in 
response to pre-defined events, such as API calls or database transactions
in other Azure services.

<a href="https://docs.microsoft.com/en-us/azure/azure-functions/" style="border:none"><img src="/img/logos/azure.png" width="100%" alt="Microsoft Azure logo." class="shot"></a>

<div class="well see-also">Azure Functions is an implementation of the <a href="/serverless.html">serverless</a> concept. Learn how these pieces fit together in the <a href="/deployment.html">deployment</a> chapter or view the <a href="/table-of-contents.html">table of contents</a> for all topics.</div>


### Azure Functions resources
* [An introduction to Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview)
  is the official quickstart guide by Microsoft and has some good high-level
  information on their platform's services as well.

* [Deploy Python to Azure Functions](https://code.visualstudio.com/docs/python/tutorial-azure-functions)
  provides the step-by-step instructions needed to get Python code running 
  on Azure Functions.

* [Azure Functions vs AWS Lambda – Scaling Face Off](https://www.azurefromthetrenches.com/azure-functions-vs-aws-lambda-scaling-face-off/)
  contains metrics from comparing AWS Lambda with Azure Functions in
  response time, user load, requests per second and error rate
  over various periods of time.

* [How to build a serverless report server with Azure Functions and SendGrid](https://medium.freecodecamp.org/how-to-build-a-serverless-report-server-with-azure-functions-and-sendgrid-3c063a51f963)
  combines the [Sendgrid email API](https://sendgrid.com/) with some 
  configuration code to have Azure Functions kick off email jobs.

* [azure-cli](https://github.com/Azure/azure-cli) are the command line
  tools for using all of Azure, not just Functions.

* [My (Rough) Start with Azure Functions](https://www.raymondcamden.com/2018/07/06/my-rough-start-with-azure-functions)
  painstakingly details signing up for Azure, accessing Functions and
  finally coding a Function. The author has some really great points on
  what is confusing to newcomers that hopefully will be addressed
  as Microsoft continues to work on their Azure platform.

* [Azure in Plain English](https://www.expeditedssl.com/azure-in-plain-english)
  covers all of the Azure services and explains them because their
  default names are often too vague to understand their purpose.
