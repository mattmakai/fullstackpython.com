title: Getting Started with AWS Lambda & Python 2.7
slug: aws-lambda-python-2-7
meta: Learn how to create and deploy your first Amazon Web Services (AWS) Lambda function with Python 2.7.
category: post
date: 2017-04-28
modified: 2017-04-29
newsletter: False
headerimage: /img/170428-aws-lambda-python-2-7/header.jpg
headeralt: AWS, AWS Lambda and Python logos, copyright their respective owners.


[Amazon Web Services (AWS) Lambda](/aws-lambda.html)
is a "serverless" compute service that executes arbitrary Python code in 
response to developer-defined events, such as inbound API calls or file 
uploads to [AWS S3](https://aws.amazon.com/s3/). Note that AWS Lambda has 
nothing to do with the `lambda` keyword in Python that is used to create 
anonymous functions, it's just the product name that happens to collide 
with an existing Python language feature name.

In this tutorial we'll learn how to quickly write and run a Lambda 
function that executes some simple Python 2.7 code and handles environment
variables. The code can then be modified to build far more complicated 
Python applications.


## Tools We Need
We do not need any local development environment tools to get through
this walkthrough other than a web browser because all the work will
happen on AWS.

Grab a new free tier [Amazon Web Services account](https://aws.amazon.com/) 
or use your existing AWS account.


## First Steps with Lambda
Head to the 
[AWS Lambda landing page](https://aws.amazon.com/lambda/) in your 
web browser. Sign into your account, or sign up for a new account which
comes with a free tier so you don't have to pay.

<img src="/img/170428-aws-lambda-python-2-7/aws-amazon-com.jpg" width="100%" class="shot rnd outl" alt="AWS Lambda landing page.">

If you're not taken directly to the 
[Lambda Console page](https://console.aws.amazon.com/lambda/home) after
logging in you'll see the main Console. AWS has a ridiculous number of
services (that seems to expand every week) so the best way to get around 
is to select the search text box and search for "lambda" as shown in the 
following screenshot.

<img src="/img/170428-aws-lambda-python-2-7/search-for-lambda.jpg" width="100%" class="shot rnd outl" alt="Search for lambda in the dashboard text box.">

Press the "Create a Lambda function" button and you'll see the 
"Select Blueprint" page.

<img src="/img/170428-aws-lambda-python-2-7/select-blueprint.jpg" width="100%" class="shot rnd outl" alt="The select blueprint Lambda screen, where you should select Blank Function.">

Choose "Blank Function". The next screen gives the option to select a
"trigger", which is how the Lambda function gets executed. A trigger is
some event that is integrated with other AWS services and can be exposed
externally via an API or device such as Alexa.

<img src="/img/170428-aws-lambda-python-2-7/configure-triggers.jpg" width="100%" class="shot rnd outl" alt="Configure trigger screen, which we will not use for now because we will manually kick off our Lambda.">

However, we aren't going to set up a trigger for this function because 
we can manually test the Lambda later before connecting it to a trigger.
Leave the trigger icon blank and click the "Next" button to move along 
to the next screen.

<img src="/img/170428-aws-lambda-python-2-7/blank-lambda.jpg" width="100%" class="shot rnd outl" alt="Blank Lambda configuration screen.">

Now we're on the screen where we can enter our specific configuration
and code for our new Lambda.


## Writing Our Python Code
Start by entering a name for your Lambda function, such as "my_first_python_lambda" and a description. The description field is optional but it's handy
when you start using Lambda regularly to keep all your functions straight. 
In the Runtime drop-down, select Python 2.7 as the execution language.

<img src="/img/170428-aws-lambda-python-2-7/first-python-lambda.jpg" width="100%" class="shot rnd outl" alt="Enter a name, description and select Python 2.7 on the Lambda configuration screen.">

Below the Runtime drop-down you'll see a large text box for writing code.
We can also choose to upload a ZIP file with our Python application which
is handy for more than simple test Lambdas. However, for our simple starter
Lambda application you can copy or type in the following code 
([or copy it from this GitHub repo](https://github.com/fullstackpython/blog-code-examples/blob/master/aws-lambda-python-2-7/lambda.py)). 
Make sure to replace what's already in the text box.


```python
import os


def lambda_handler(event, context):
    what_to_print = os.environ.get("what_to_print")
    how_many_times = int(os.environ.get("how_many_times"))

    # make sure what_to_print and how_many_times values exist
    if what_to_print and how_many_times > 0:
        for i in range(0, how_many_times):
            print(what_to_print)
        return what_to_print
    return None
```

The above code has the required `lambda_handler` function definition
that provides a hook for the Lambda service to know where to begin executing
the Python code. Think of `lambda_handler` as a `main` function when you're
using this service.

Our Python code expects and reads two environment variables and then the
code prints a message zero to many times, based on the amount defined in 
the `how_many_times` variable. If a message is printed then the function 
returns the `what_to_print` string, if nothing is printed then `None` is 
returned.

Just below the code input text box there are environment variable key-value
pairs that can be set. Our code will use two environment variables, named
`what_to_print` and `how_many_times`. 

Enter the keys named `what_to_print` and `how_many_times` then enter their 
values. Use a string message for `what_to_print`'s value and an integer 
whole number above 0 for `how_many_times`. Our Python code's error handling
is not very robust so a value other than a number in the `how_many_times`
variable will cause the script to throw an error when it is executed.

<img src="/img/170428-aws-lambda-python-2-7/environment-variables.jpg" width="100%" class="shot rnd outl" alt="Enter the exact keys of what_to_print and how_many_times along with corresponding values as environment variables.">

Our code and environment variables are in place and we just need to set
a few more AWS-specific settings before we can test the Lambda function.


## Executing the Lambda
Scroll down below the environment variables to the 
"Lambda function handler and role" section. This section contains the last 
few required configuration items. Keep the default handler, which should 
be `lambda_function.lambda_handler`. Select 
"Create a new Role from template(s)" from the drop-down then for the
"Role name" field enter "dynamodb_permissions". Under "Policy templates" 
select the "Simple Microservice permissions". 

<img src="/img/170428-aws-lambda-python-2-7/lambda-handler-and-role.jpg" width="100%" class="shot rnd outl" alt="For the final configuration, keep the default handler, create a new role from a template for Simple Microservice permissions and save it with a unique name.">

The "Simple Microservice permissions" gives our Lambda access to 
[AWS DynamoDB](https://aws.amazon.com/dynamodb/). We won't use DynamoDB in 
this tutorial but it's super useful as either permanent or temporary 
storage when working with Lambda.

Now that our code and configuration is in place, click the "Next" button
at the bottom right corner of the page.

<img src="/img/170428-aws-lambda-python-2-7/review-lambda.jpg" width="100%" class="shot rnd outl" alt="We can review the values set during our configuration.">

The review screen will show us our configuration settings. Scroll down
to the bottom and click the "Create function" button to continue.

<img src="/img/170428-aws-lambda-python-2-7/create-function.jpg" width="100%" class="shot rnd outl" alt="Click the create function button to continue.">

We should see a success message on the next page just below the 
"Save and test" button.

<img src="/img/170428-aws-lambda-python-2-7/save-and-test.jpg" width="100%" class="shot rnd outl" alt="Save and test button.">

Press the "Test" button to execute the Lambda. Lambda prompts us for
some data to simulate an event that would trigger our function. Select
the "Hello World" sample event template, which contains some example keys. 
Our Lambda will not those keys in its execution so it does not matter what
they are. Click the "Save and test" button at the bottom of the modal.

<img src="/img/170428-aws-lambda-python-2-7/sample-event-template.jpg" width="100%" class="shot rnd outl" alt="Sample event template for our Lambda execution.">

Scroll down to the "Execution result" section where we can see our output.

<img src="/img/170428-aws-lambda-python-2-7/execution-results.jpg" width="100%" class="" alt="Execution results from running our Lambda function.">

We get the log output that shows us the return value of our function. In
this case it is the string message from `what_to_print`. We can also see
down below that our print function produced output five times. 


## What's Next?
Awesome, you just configured, wrote and executed your first Python 2.7
code on AWS Lambda! The real power of Lambda comes in when you connect a
trigger to it so your code executes based on events. We'll take a look
at that in the next tutorial.

What else can you do with Python and Lambda? Take a look at the 
[AWS Lambda](/aws-lambda.html) page for more examples and tutorials. 

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I am also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170428-python-2-7-aws-lambda.markdown).

