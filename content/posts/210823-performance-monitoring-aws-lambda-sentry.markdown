title: Application Performance Monitoring AWS Lambda Functions with Sentry
slug: application-performance-monitoring-aws-lambda-functions-sentry
meta: Learn how to use Sentry Application Performance Monitoring on AWS Lambda.
category: post
date: 2021-08-23
modified: 2021-08-26
newsletter: False
headerimage: /img/headers/python-lambda-sentry.jpg
headeralt: The Python, AWS Lambda and Sentry logos are copyright their respective owners.


[Amazon Web Services (AWS) Lambda](/aws-lambda.html) is a usage-based
computing infrastructure service that can execute 
[Python 3](/why-use-python.html) code. One of the challenges of this 
environment is ensuring efficient performance of your Lambda Functions. 
Application performance monitoring (APM) is particularly useful in these
situations because you are billed based on how long you use the
resources.

In this post we will install and configure 
[Sentry's APM](https://sentry.io/for/performance/) that works via a
[Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html).
Note that if you are looking for error monitoring rather than performance
monitoring, take a look at 
[How to Monitor Python Functions on AWS Lambda with Sentry](/blog/monitor-python-functions-aws-lambda-sentry.html)
rather than following this post.


## First steps with AWS Lambda
A local [development environment](/development-environments.html) is not
required to follow this tutorial because all of the coding and configuration
can happen in a web browser through the 
[AWS Console](https://console.aws.amazon.com/console/).

[Sign into your existing AWS account](https://aws.amazon.com/console)
or sign up for a [new account](https://aws.amazon.com/). Lambda
gives you the first 1 million requests for free so that you can execute 
basic applications without no or low cost.

<img src="/img/210406-python-sentry-aws-lambda/aws-lambda-landing.jpg" width="100%" class="shot rnd outl" alt="The AWS Lambda landing page.">

When you log into your account, use the search box to enter
"lambda" and select "Lambda" when it appears to get to the right
page.

<img src="/img/210406-python-sentry-aws-lambda/lambda-search-bar.png" width="100%" class="shot rnd outl" alt="Use the search bar to find AWS Lambda.">

If you have already used Lambda before, you will see your existing Lambda 
functions in a searchable table. We're going to create a new function so
click the "Create function" button.

<img src="/img/210406-python-sentry-aws-lambda/create-function.png" width="100%" class="shot rnd outl" alt="Click the create function button.">

The create function page will give you several options for building a
Lambda function.

<img src="/img/210406-python-sentry-aws-lambda/create-function-detail.png" width="100%" class="shot rnd outl" alt="The create function details page.">

Click the "Browse Serverless App Repository" selection box, then choose
the "hello-world-python3" starter app from within the 
"Public applications" section.

<img src="/img/210406-python-sentry-aws-lambda/create-function-detail.png" width="100%" class="shot rnd outl" alt="The create function details page.">

The hello-world-python3 starter app details page should look something
like the following screen:

<img src="/img/210406-python-sentry-aws-lambda/hello-world-python3.png" width="100%" class="shot rnd outl" alt="Hello world Python3 example app and Lambda function.">

Fill in some example text such as "test" under `IdentityNameParameter`
and click the "Deploy" button:

<img src="/img/210406-python-sentry-aws-lambda/deploy-starter-app.png" width="100%" class="shot rnd outl" alt="Click the deploy button to use the starter app.">

The function will now be deployed. As soon as it is ready we can
customize it and test it out before adding Sentry to capture any errors
that occur during execution.

Go back to the Lambda functions main page and select your new deployed
starter app from the list.

<img src="/img/210406-python-sentry-aws-lambda/functions-list.jpg" width="100%" class="shot rnd outl" alt="List of AWS Lambda functions you have created.">

Find the orange "Test" button with a down arrow next to it like you
see in the image below, and then click the down arrow. Select
"Configure Test Event".

<img src="/img/210406-python-sentry-aws-lambda/configure-test.jpg" width="100%" class="shot rnd outl" alt="Configure the test event.">

Fill in the Event name as "FirstTest" or something similar, then
press the "Create" button at the bottom of the modal window.

Click the "Test" button and it will run the Lambda function with
the parameters from that new test event. You should see something
like the following output:

```python
Response
"value1"

Function Logs
START RequestId: 62fa2f25-669c-47b7-b4e7-47353b0bd914 Version: $LATEST
value1 = value1
value2 = value2
value3 = value3
END RequestId: 62fa2f25-669c-47b7-b4e7-47353b0bd914
REPORT RequestId: 62fa2f25-669c-47b7-b4e7-47353b0bd914	Duration: 0.30 ms	Billed Duration: 1 ms	Memory Size: 128 MB	Max Memory Used: 43 MB	Init Duration: 1.34 ms

Request ID
62fa2f25-669c-47b7-b4e7-47353b0bd914
```

The code was successfully executed, so let's add Sentry's performance
monitoring and test some code that uses it.


## Performance monitoring with Sentry
Go to [Sentry.io's homepage](https://sentry.io).

<img src="/img/210406-python-sentry-aws-lambda/sentry-homepage.jpg" width="100%" class="shot rnd outl" alt="Sentry.io homepage where you can sign up for a free account.">

Sign into your account or sign up for a new free account. You will be at
the main account dashboard after logging in or completing the Sentry sign
up process.

Select "Performance" on the left navigation bar, it will take you to the
performance monitoring page.

<img src="/img/210823-sentry-apm-lambda/performance.jpg" width="100%" class="shot rnd outl" alt="Click the 'performance' button on the left side nav.">

Click "Start Setup" then go back over to AWS Lambda to complete the
steps for adding Sentry's Python layer to your Lambda function.

The easiest way to add Sentry to Lambda for this application
is to configure an 
[AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
with the necessary dependency for Sentry. Sentry has concise
[documentation on adding via Lambda Layers](https://docs.sentry.io/platforms/python/guides/aws-lambda/layer/)
so we will walk through that way to configure it and test it
out.

Scroll down to the "Layers" section while in your Lambda
function configuration. Click the "Add a layer" button":

<img src="/img/210406-python-sentry-aws-lambda/add-lambda-layer.png" width="100%" class="shot rnd outl" alt="Add Lambda layer.">

In the "Add layer" screen, select the "Specify an ARN" option.

<img src="/img/210406-python-sentry-aws-lambda/add-layer-specify-arn.jpg" width="100%" class="shot rnd outl" alt="Select Specify ARN in the Add Layer screen.">

Now to specify the Amazon Resource Name (ARN), we need to use
the Sentry documentation to get the right configuration string.

US-East-1 is the oldest and most commonly-used region so I'll
use that here in this tutorial but you should check which one
you are in if you are not certain.

<img src="/img/210823-sentry-apm-lambda/arn-region.png" width="100%" class="shot rnd outl" alt="Select the AWS for the ARN string.">

Copy that value into the Lambda Layer configuration, like this:

<img src="/img/210823-sentry-apm-lambda/layer-with-arn.png" width="100%" class="shot rnd outl" alt="Select the AWS for the ARN string.">

Then press the "Add" button. You now have the Sentry dependency
in your environment so code that relies upon that library can be 
used in the Lambda function.


## Testing performance monitoring
Let's change our Python code in the Lambda function and test out
the APM agent.

Make sure you are signed into your Sentry account and go to 
[this specific AWS Lambda set up guide](https://docs.sentry.io/platforms/python/guides/aws-lambda/).

You will see a "DSN string" that we need to set as an environment
variable on AWS Lambda to finish our setup. Copy the string that
matches your project as shown on that page in the highlighted green
section:

<img src="/img/210823-sentry-apm-lambda//sentry-dsn-string.png" width="100%" class="shot rnd outl" alt="Copy the Sentry DSN string so we can export it as an environment variable.">

We will
[use environment variables on AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html) 
to store and access values like this Sentry DSN key.

Go into the Lambda console to create a new environment variable. To do 
that, click the "Configuration" tab within Lambda like you see here:

<img src="/img/210406-python-sentry-aws-lambda/aws-lambda-configuration.jpg" width="100%" class="shot rnd outl" alt="Click the Lambda Configuration tab.">

Then click "Edit" and add a new environment variable with the key of `SENTRY_DSN`
and the value of the DSN string that you copied from the Sentry screen. 

<img src="/img/210406-python-sentry-aws-lambda/add-env-var.jpg" width="100%" class="shot rnd outl" alt="Add the environment variable in AWS Lambda.">

Click the "Save" button and go back to your Lambda function's code editor.

Replace the code in your Lambda function with the following code:

```python
import json
import os
import sentry_sdk
import time
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from sentry_sdk import start_transaction

SENTRY_DSN = os.environ.get('SENTRY_DSN')
sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    integrations=[AwsLambdaIntegration()]
)

print('Loading function')


def lambda_handler(event, context):
    calc = 1000

	# this is custom instrumentation, see docs: https://bit.ly/2WjT3AY
    with start_transaction(op="task", name="big calculation"):
        for i in range(1, 1000):
            calc = calc * i

    print(calc)
    return event['key1']  # Echo back the first key value
```

The above code imports the Sentry dependencies, and then runs both
[automatic instrumentation](https://docs.sentry.io/platforms/python/guides/aws-lambda/performance/instrumentation/automatic-instrumentation/) 
and [custom instrumentation](https://bit.ly/2WjT3AY) on the
code. Click the "Deploy" button and then "Test". The code will 
successfully execute and when we go back to our Sentry performance
monitoring dashboard we will see some initial results, like this
following screenshot.

<img src="/img/210823-sentry-apm-lambda/performance-results.jpg" width="100%" class="shot rnd outl" alt="APM results shown in the Sentry dashboard.">

Looks good, you have both the default and the specified transaction 
performance recordings in the dashboard, and you can toggle between
them (or other transactions you record) through the user interface.


## What's Next?
We just wrote and executed a Python 3 function on AWS Lambda that
used the basics of Sentry APM to get some initial performance
monitoring data.

Check out the [AWS Lambda section](/aws-lambda.html) for 
more tutorials by other developers.

Further questions? Contact me on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I am also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/210823-performance-monitoring-aws-lambda-sentry.markdown)
and submit a pull request.
