title: Monitoring Python 3.6 Functions on AWS Lambda
slug: monitor-python-3-6-example-code-aws-lambda-rollbar
meta: Monitor your Python 3.6 application code on Amazon Web Services (AWS) Lambda functions using Rollbar.
category: post
date: 2018-04-20
modified: 2018-04-20
newsletter: False
headerimage: /img/180420-monitor-aws-lambda/header.jpg
headeralt: Python, AWS Lambda and Rollbar logos are copyright their respective owners.


[Amazon Web Services (AWS) Lambda](/aws-lambda.html) is a usage-based
execution environment that can run Python 3.6 code. If you have never
previously used AWS Lambda then you can read  
[How to Create Your First Python 3.6 AWS Lambda Function](/blog/aws-lambda-python-3-6.html).
However, this tutorial will give you every step to follow even if you
are completely new to AWS.

In this post we are going to monitor Python code that is running on AWS 
Lambda by using a hosted [monitoring](/monitoring.html) service, 
[Rollbar](/rollbar.html).


## Required Tools and Code
A local [development environment](/development-environments.html) is not
required to follow this tutorial. All the work will happen in a web
browser through the [AWS Console](https://console.aws.amazon.com/console/).

The example code can be copy and pasted from this blog post or you
can access it on GitHub under the
[Full Stack Python blog-post-examples](https://github.com/fullstackpython/blog-code-examples)
repository within the 
[monitor-aws-lambda-python-3-6 directory](https://github.com/fullstackpython/blog-code-examples/monitor-aws-lambda-python-3-6).


## Accessing the AWS Lambda Service
[Sign into your existing AWS account](https://aws.amazon.com/console) 
or sign up for a [new account](https://aws.amazon.com/). AWS Lambda
comes with a free tier so you can test code and execute basic 
applications without cost.

<img src="/img/180420-monitor-aws-lambda/aws-amazon-com.jpg" width="100%" class="shot rnd outl" alt="AWS Lambda landing page.">

AWS has a boatload of services so use the search box to enter
"lambda" and select "Lambda" when it appears to get to the appropriate
starting page.

<img src="/img/180420-monitor-aws-lambda/search-for-lambda.jpg" width="100%" class="shot rnd outl" alt="Search for lambda in the dashboard text box.">

Click "Create a Lambda function" and the "Select Blueprint" page should
appear.

<img src="/img/180420-monitor-aws-lambda/select-blueprint.jpg" width="100%" class="shot rnd outl" alt="The Select Blueprint Lambda screen.">

Select "Blank Function". The "Configure triggers" page should appear next.
A trigger is how the Lambda function typically knows 
when to execute based on an event from another AWS service like
[Cloudwatch](https://aws.amazon.com/cloudwatch/) or
[API Gateway](https://aws.amazon.com/api-gateway/). 

<img src="/img/180420-monitor-aws-lambda/configure-triggers.jpg" width="100%" class="shot rnd outl" alt="Screen for configuring the AWS Lambda trigger.">

You do not need to configure a trigger to move to the next screen so
we will not configure a trigger for this function. We can manually 
kick off the Lambda to test it when we are done with configuring it. Leave 
the trigger icon blank and click "Next" to continue.

<img src="/img/180420-monitor-aws-lambda/blank-lambda.jpg" width="100%" class="shot rnd outl" alt="Blank AWS Lambda function.">

Ok, finally we arrive at the "Configure function" screen where we can write
our code.


## Lambda Function Python Example Code
Enter a name for the Lambda function, such as "python_3_6_lambda_test",
as well as a description. A description is optional but it is useful
when you have a dozens or hundreds of different Lambda functions and
need to keep them straight. In the Runtime drop-down, select Python 3.6 for 
the programming language.

<img src="/img/170429-aws-lambda-python-3-6/python-3-6-lambda.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Enter a name, description and use Python 3.6 for the Lambda.">

Beneath the Runtime drop-down there is a large text box for code, 
prepopulated with a `lambda_handler` function definition. The 
"Code entry type" drop-down can also be changed to allow uploading a ZIP
file or inputing a file from an S3 bucket. For our simple first
Lambda function we will stick to the "Edit code inline" option. Copy or type 
in the following code, replacing what is already in the text box. This
code is also available on [this open source GitHub repository](https://github.com/fullstackpython/blog-code-examples/blob/master/aws-lambda-python-3-6/).


```python
import os


def lambda_handler(event, context):
    what_to_print = os.environ.get("what_to_print")
    how_many_times = int(os.environ.get("how_many_times"))

    # make sure what_to_print and how_many_times values exist
    if what_to_print and how_many_times > 0:
        for i in range(0, how_many_times):
            # formatted string literals are new in Python 3.6
            print(f"what_to_print: {what_to_print}.")
        return what_to_print
    return None
```

The code above contains a required `lambda_handler` function, which is 
AWS Lambda's defined hook so it knows where to begin execution. Think of 
`lambda_handler` as a `main` function, like the  
`if __name__ == "__main__":` conditional line commonly used in Python files 
to ensure a block of code is executed when a script is run from the 
command line.

The Python code expects two environment variables that are read by the
`os` module with the `environ.get` function. With the `what_to_print` and
`how_many_times` variables set by the environment variables, our code then
then prints a message zero or more times, based on the amount defined in 
the `how_many_times` variable. If a message is printed at least once then 
the function returns the `what_to_print` string, if nothing is printed 
then `None` is returned.

Below the code input text box on this function configuration screen there 
is a section to set environment variable key-value pairs.

Enter the keys named `what_to_print` and `how_many_times` then enter their 
values. Use a string message for `what_to_print`'s value and an integer 
whole number above 0 for `how_many_times`. Our Python code's error handling
is not very robust so a value other than a number in the `how_many_times`
variable will cause the script to throw an error when it is executed due
to the forced casting of `how_many_times` via the `int()` function.

<img src="/img/170429-aws-lambda-python-3-6/environment-variables.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Section to set environment variables for the Lambda function.">

The Python 3.6 code and the environment variables are now in place. We 
just need to handle a few more AWS-specific settings before we can test the 
Lambda function.


## Executing our Lambda Function
Scroll past the environment variables to the 
"Lambda function handler and role" section, which contains a few more 
required function configuration items. 

Keep the default handler set to `lambda_function.lambda_handler`. Select 
"Create a new Role from template(s)" from the drop-down then for the
"Role name" field enter "dynamodb_access". Under "Policy templates" 
select the "Simple Microservice permissions". 

The "Simple Microservice permissions" allows our Lambda to access
[AWS DynamoDB](https://aws.amazon.com/dynamodb/). We will not use DynamoDB in 
this tutorial but the service is commonly used either as permanent or 
temporary storage for Lambda functions.

<img src="/img/170429-aws-lambda-python-3-6/lambda-handler-and-role.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="For the final configuration, keep the default handler, create a new role from a template for Simple Microservice permissions and save it with a unique name.">

Our code and configuration is in place so click the "Next" button
at the bottom right corner of the page.

<img src="/img/170429-aws-lambda-python-3-6/review-lambda.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Review Lambda configuration.">

The review screen shows us our configuration settings to make sure we 
selected the appropriate values for our new Lambda function. Scroll down
press "Create function".

<img src="/img/170429-aws-lambda-python-3-6/create-function.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Click the create function button to continue.">

Success message should appear on the next page below the "Test" button.

<img src="/img/170429-aws-lambda-python-3-6/test.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Test button on the execution screen.">

Click the "Test" button to execute the Lambda. Lambda will prompt us for
some data to simulate an event that would kick off our function. Select
the "Hello World" sample event template, which contains some keys but our
Lambda will not use that in its execution. Click the "Save and test" button
at the bottom of the modal.

<img src="/img/170429-aws-lambda-python-3-6/sample-event-template.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Sample event template for Lambda execution.">

Scroll down to the "Execution result" section where we can see our output.

<img src="/img/170429-aws-lambda-python-3-6/execution-results.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Results from executing our new Lambda function.">

The log output shows us the return value of our function, which in this 
execution was the string message from `what_to_print`. We can also see
our print function produced output five times as expected based on the
amount set in the `how_many_times` environment variable.


## What's Next?
We just wrote and executed a Python 3.6 function on AWS Lambda then
captured the exception message into our Rollbar logs. Now you can
continue building out your Python code knowing that when something
goes wrong you will have full visibility on what happened.

Check out the [AWS Lambda section](/aws-lambda.html) for 
more tutorials by other developers.

Further questions? Contact me on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I am also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/180420-monitor-aws-lambda-python-3-6.markdown)
and submit a pull request.
