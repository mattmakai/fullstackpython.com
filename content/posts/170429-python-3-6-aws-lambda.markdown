title: How to Create Your First Python 3.6 AWS Lambda Function
slug: aws-lambda-python-3-6
meta: Code, create and execute your first Amazon Web Services (AWS) Lambda function with Python 3.6.
category: post
date: 2017-04-29
modified: 2017-04-29
headerimage: /img/170429-aws-lambda-python-3-6/header.jpg
headeralt: AWS, AWS Lambda and Python logos are copyright their respective owners.


[Amazon Web Services (AWS) Lambda](/aws-lambda.html)
provides a usage-based compute service for running Python code in response 
to developer-defined events. For example, if an inbound HTTP POST
comes in to API Gateway or a new file is uploaded to 
[AWS S3](https://aws.amazon.com/s3/) then AWS Lambda can execute a function
to respond to that API call or manipulate the file on S3.

AWS Lambda is not related in any way to Python's `lambda` syntax. The 
`lambda` keyword in Python is used to create anonymous functions within the 
programming language and AWS Lambda's name just happens to collide with
the existing Python feature.

Let's learn how to quickly write and run a Lambda function to execute 
basic Python 3.6 code which uses environment variables as input.
This code, which is also [available on GitHub under the blog-post-examples repository](https://github.com/fullstackpython/blog-code-examples) can be 
changed so that you can build much more complicated Python programs.


## Our Tools
No local [development environment](/development-environments.html) tools 
are required for this tutorial, other than a web browser. All the work will
happen on AWS via their Console. All of these steps can also be completed
from the command line via the [boto3](https://boto3.readthedocs.io/en/latest/)
library, but we won't cover that in this post.

Sign up for a new [Amazon Web Services account](https://aws.amazon.com/) 
(which provides a generous free tier), or use your existing AWS account.


## First Steps with AWS Lambda
In your web browser go to the 
[AWS Lambda landing page](https://aws.amazon.com/lambda/).
Log in to your account, or sign up for a new account which
comes with a free tier so you don't have to pay.

<img src="/img/170429-aws-lambda-python-3-6/aws-amazon-com.jpg" width="100%" class="technical-diagram img-rounded" alt="AWS Lambda landing and sign in screen.">

After signing up a few tutorials may pop up, but skip past them and
go to the main Console. AWS has tons of services, with more being added
every month, so using the search box is the best way to get around. 
Select the search text box, enter "lambda" and select "Lambda" to get to
the right starting page.

<img src="/img/170429-aws-lambda-python-3-6/search-for-lambda.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Search for lambda in the dashboard text box.">

Click the "Create a Lambda function" button. The "Select Blueprint" page
will appear.

<img src="/img/170429-aws-lambda-python-3-6/select-blueprint.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="The Select Blueprint Lambda screen.">

Select "Blank Function" and the "Configure triggers" page will come up. 
It's non-obvious at first, but you don't actually need to configure a 
trigger to move on. A trigger is how the Lambda function typically knows 
when to execute based on an event from another AWS service such as API 
Gateway or Cloudwatch.

<img src="/img/170429-aws-lambda-python-3-6/configure-triggers.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Configure Lambda trigger screen.">

We won't configure a trigger for this function because we can manually 
kick off the Lambda later to test it. Leave the trigger icon blank and 
click the "Next" button to move along. 

<img src="/img/170429-aws-lambda-python-3-6/blank-lambda.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="The Lambda configuration screen.">

Next we get to the "Configure function" screen where we can finally write
some code!


## Python Code for Our Lambda Function
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
variable will cause the script to throw an error when it is executed.

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
"Role name" field enter "dynamodb_permissions". Under "Policy templates" 
select the "Simple Microservice permissions". 

The "Simple Microservice permissions" allows our Lambda to access
[AWS DynamoDB](https://aws.amazon.com/dynamodb/). We will not use DynamoDB in 
this tutorial but the service is commonly used either as permanent or 
temporary storage for Lambda functions.

<img src="/img/170429-aws-lambda-python-3-6/lambda-handler-and-role.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="For the final configuration, keep the default handler, create a new role from a template for Simple Microservice permissions and save it with a unique name.">

Now that our code and configuration is in place, click the "Next" button
at the bottom right corner of the page.

<img src="/img/170428-aws-lambda-python-2-7/review-lambda.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="We can review the values set during our configuration.">

The review screen will show us our configuration settings. Scroll down
to the bottom and click the "Create function" button to continue.

<img src="/img/170428-aws-lambda-python-2-7/create-function.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Click the create function button to continue.">

We should see a success message on the next page just below the 
"Save and test" button.

<img src="/img/170428-aws-lambda-python-2-7/save-and-test.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Save and test button.">

Click that "Save and test" button to execute the Lambda. At first it
may appear that nothing happened but scroll down to the "Execution result"
section where we can see our output.

<img src="/img/170428-aws-lambda-python-2-7/execution-results.jpg" width="100%" class="technical-diagram img-rounded bordered" alt="Execution results from running our Lambda function.">

We get the log output that shows us the return value of our function. In
this case it is the string message from `what_to_print`. We can also see
down below that our print function produced output five times. 


## Next Steps
Awesome, you just configured, wrote and executed your first Python 3.6
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

