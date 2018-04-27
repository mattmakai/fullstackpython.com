title: Monitoring Python 3.6 Functions on AWS Lambda
slug: monitor-python-3-6-example-code-aws-lambda-rollbar
meta: Monitor your Python 3.6 application code on Amazon Web Services (AWS) Lambda functions using Rollbar.
category: post
date: 2018-04-20
modified: 2018-04-25
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

Click the "Create function" button.

<img src="/img/180420-monitor-aws-lambda/create-function.png" width="100%" class="shot rnd outl" alt="The create Lambda function screen.">

Select "Author from Scratch". Fill in a name so you can easily recognize this
function for future reference. I chose "monitorPython3". Select "Python 3.6"
for Runtime.

Select "Create new role from template(s)", input a Role name, for example
"basicEdgeLambdaRole". For Policy templates choose "Basic Edge Lambda 
Permissions".

Then click "Create function."

<img src="/img/180420-monitor-aws-lambda/monitorpython3.png" width="100%" class="shot rnd outl" alt="Blank AWS Lambda function named monitorPython3.">

Ok, finally we have arrived at the configuration screen where we can write
our code.


## Coding a Python Function
Scroll down to the "Function code" user interface section.

Paste or type in the following code, replacing what is already in the 
text box.


```python
import os
import rollbar


ROLLBAR_KEY = os.getenv('ROLLBAR_SECRET_KEY', 'missing Rollbar secret key')
rollbar.init(ROLLBAR_KEY, 'production')


@rollbar.lambda_function
def lambda_handler(event, context):
    message = os.getenv("message")
    print_count = int(os.getenv("print_count"))

    # check if message exists and how many times to print it
    if message and print_count > 0:
        for i in range(0, print_count):
            # formatted string literals are new in Python 3.6
            print(f"message: {message}.")
        return print_count
    return None
```

The code contains the required `lambda_handler` function. `lambda_handler` 
is Lambda's hook for where to start execution the code.

The Python code expects two environment variables that are read by the
`os` module with the `getenv` function. The `message` and
`print_count` variables are set by the environment variables.

Below the code input text box on this function configuration screen there 
is a section to set environment variable key-value pairs.

<img src="/img/180420-monitor-aws-lambda/lambda-coded.png" width="100%" class="shot rnd outl" alt="Python 3.6 code within a Lambda function.">

Next we need to input two environment variables and then we can run
our code.

Enter the keys named `message` and `print_count`, then enter their values.
Use a string message for `message`'s value and an integer whole number 
above 0 for `print_count`. Our Python code's error handling is not very 
robust so a value other than a number in the `print_count` variable will 
cause the script to throw an error when it is executed due to the forced 
casting of `print_count` via the `int()` function. That is how we will 
test Rollbar's error monitoring for the Lambda function.

(execute, show with errors)


## Monitoring our Lambda Function
Head over to the [Rollbar homepage](https://rollbar.com/) 
to add their monitoring serving into our Lambda application.

<img src="/img/180420-monitor-aws-lambda/rollbar-home.jpg" width="100%" class="shot rnd outl" alt="Rollbar homepage.">

Click "Sign Up" in the upper right-hand corner. Enter your 
email address, username and desired password.

<img src="/img/180420-monitor-aws-lambda/sign-up-rollbar.jpg" width="100%" class="shot rnd outl" alt="Signing up for a Rollbar account in your browser.">

After the sign up page you will see the onboarding flow where you can
enter a project name and select a programming language. For the project
name type in "Full Stack Python" and then select that you are monitoring 
a Python-based application.

<img src="/img/180420-monitor-aws-lambda/create-project.jpg" width="100%" class="shot rnd outl" alt="Name your project 'Full Stack Python' and select Python as your language.">

Press "Continue" at the bottom of the screen. The next
page shows us a few instructions on how to add monitoring.

<img src="/img/180202-monitor-django/configure-project.jpg" width="100%" class="shot rnd outl" alt="Configure project using your server-side access token.">

We can now update our AWS Lambda Pyton function to collect and aggregate
the errors that occur in our application. Add the following highlighted
lines to your Lambda code:


```python
import os
~~import rollbar
~~
~~
~~ROLLBAR_KEY = os.getenv('ROLLBAR_SECRET_KEY', 'missing Rollbar secret key')
~~rollbar.init(ROLLBAR_KEY, 'production')


~~@rollbar.lambda_function
def lambda_handler(event, context):
    message = os.getenv("message")
    print_count = int(os.getenv("print_count"))

    # check if message exists and how many times to print it
    if message and print_count > 0:
        for i in range(0, print_count):
            # formatted string literals are new in Python 3.6
            print(f"message: {message}.")
        return print_count
    return None
```

(explain new lines of code)

(add ROLLBAR env var)

(re-run code)


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
