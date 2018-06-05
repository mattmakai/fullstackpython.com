title: Running Bottle Apps in Docker Containers on macOS
slug: first-steps-bottle-web-apps-docker-containers
meta: Learn how to set up and develop a new Bottle web application within a Docker container.
category: post
date: 2018-06-04
modified: 2018-06-05
newsletter: False
headerimage: /img/180604-bottle-docker/header.jpg
headeralt: Bottle, Docker and Apple logos, copyright their respective owners.


It can be confusing to figure out how to use [Docker](/docker.html) 
containers in your [Python](/why-use-python.html) and 
[Bottle](/flask.html) 
[development environment](/development-environments.html) workflow.
This tutorial will quickly show you the exact steps to get Docker
up and running on macOS with a working Bottle 
[web application](/web-development.html)


## Our Tools
This tutorial is written for [Python 3](/python-2-or-3.html). It may work with
Python 2 but it has not been testing with that soon-to-be deprecated
[2.7 version](https://pythonclock.org/). You should really be using Python 3,
preferrably the latest release which is currently 
[3.6.5](https://www.python.org/downloads/release/python-365/).

[Docker for Mac](https://docs.docker.com/docker-for-mac/install/) is necessary
to run Docker containers. I recommend that you use the stable release unless 
you have an explicit purpose for the 
[edge channel](https://docs.docker.com/docker-for-mac/edge-release-notes/).

Within the Docker container we will use:

* Python 3, specifically the
  [slim-3.6.5 version](https://hub.docker.com/r/library/python/tags/)
  from [Docker Hub](https://hub.docker.com/)
* [Bottle](/bottle.html) version 0.12.13

All for the Dockerfile and the Bottle project are available open source
under the MIT license on GitHub under the 
[docker-bottle-mac directory](https://github.com/fullstackpython/blog-code-examples/tree/master/docker-bottle-mac)
of the
[blog-code-examples](https://github.com/fullstackpython/blog-code-examples)
repository.


## Installing Docker on macOS
We must install Docker before we can spin up our containers. Jump to
the next section if you already have Docker for Mac installed and working
on your computer.

On your Mac, 
[download the Docker Community Edition (CE) for Mac](https://www.docker.com/community-edition#/download)
installer.

<img src="/img/180604-bottle-docker/docker-ce.jpg" width="100%" 
 class="shot rnd" alt="Download the Docker Community Edition for Mac.">

Open Finder and go to the downloads folder where the installation file is located.
Follow the installation steps and open Terminal when the installer finishes. 

Test your Docker installation by running the `docker` command along with the 
`--version` flag:

```
docker --version
```

If Docker is installed correctly you should see the following output:

```
Docker version 18.03.1-ce, build 9ee9f40
```

Note that Docker runs through a system agent you can find in the menu bar.

<img src="/img/180604-bottle-docker/docker-agent.png" width="100%" 
     class="shot rnd" alt="Docker agent in the menu bar.">

Docker is now installed so we can run a container and write a simple
Bottle application to test running an app within the container. 


## Dockerfile
Docker needs to know what we want in our container so we specify an
image using a `Dockerfile`.

```
# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Bottle app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "app.py"]
```

Save the Dockerfile and then on the commandline run:

```
docker build -t bottledock .
```

The above `docker build` file uses the `-t` flag to tag the image with
the name of `bottledock`.

If the build worked successfully the [shell](/shells.html) will show 
some completed output like the following:

```
$ docker build -t bottledock .
Sending build context to Docker daemon  16.38kB
Step 1/6 : FROM python:3.6.5-slim
3.6.5-slim: Pulling from library/python
f2aa67a397c4: Pull complete 
19cc085bc22b: Pull complete 
83bd7790bc68: Pull complete 
8b3329adba1b: Pull complete 
d0a8fd6eb5d0: Pull complete 
Digest: sha256:56100f5b5e299f4488f51ea81cc1a67b5ff13ee2f926280eaf8e527a881afa61
Status: Downloaded newer image for python:3.6.5-slim
 ---> 29ea9c0b39c6
Step 2/6 : WORKDIR /app
Removing intermediate container 627538eb0d39
 ---> 26360255c163
Step 3/6 : ADD . /app
 ---> 9658b91b29db
Step 4/6 : RUN pip install --trusted-host pypi.python.org -r requirements.txt
 ---> Running in f0d0969f3066
Collecting bottle==0.12.13 (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/bd/99/04dc59ced52a8261ee0f965a8968717a255ea84a36013e527944dbf3468c/bottle-0.12.13.tar.gz (70kB)
Building wheels for collected packages: bottle
  Running setup.py bdist_wheel for bottle: started
  Running setup.py bdist_wheel for bottle: finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/76/a0/b4/2a3ee1a32d0506931e558530258de1cc04b628eff1b2f008e0
Successfully built bottle
Installing collected packages: bottle
Successfully installed bottle-0.12.13
Removing intermediate container f0d0969f3066
 ---> 0534575c8067
Step 5/6 : EXPOSE 80
 ---> Running in 14e49938d3be
Removing intermediate container 14e49938d3be
 ---> 05e087d2471d
Step 6/6 : CMD ["python", "app.py"]
 ---> Running in ca9738bfd06a
Removing intermediate container ca9738bfd06a
 ---> 9afb4f01e0d3
Successfully built 9afb4f01e0d3
Successfully tagged bottledock:latest
```

We can also see the image with the `docker image ls` command. Give that 
a try now:

```
docker image ls
```

Our tag name should appear in the images list:

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
bottledock          latest              9afb4f01e0d3        About a minute ago   145MB
```

Our image is ready to load as a container so we can code a short
Bottle web app for testing and then further development.


## Coding A Bottle Web App
It is time to code a simple "Hello, World!"-style Bottle app to test
running Python code within our Docker container. Within the current
project directory, create a file named `app.py` with the following contents:

```python
import bottle
from bottle import route, run


app = bottle.default_app()


@route('/')
def hello_world():
	return "Hello, world! (From Full Stack Python)"


if __name__ == "__main__":
	run(host="0.0.0.0", port=8080, debug=True, reloader=True)
```

The above code returns a simple "Hello, world!" message when
executed by the Bottle development server and contacted by a client.

We need just one more file to specify our `bottle` dependency. Create 
a `requirements.txt` file within the same directory as `app.py`:

```
bottle==0.12.13
```

Make sure both the `app.py` and `requirements.txt` file are saved then
we can give the code a try.


## Running the Container
Now that we have our image in hand along with the Python code in a file 
we can run the image as a container with the `docker run` command. Execute 
the following command, making sure to replace the absolute path for the 
volume to your own directory.

```
docker run -p 5000:8080 --volume=/Users/matt/devel/py/blog-code-examples/docker-bottle-macapp bottledock
```

If you receive the error 
`python: can't open file 'app.py': [Errno 2] No such file or directory` then
you likely did not change `/Users/matt/devel/py/bottledocker` to the 
directory where your project files, especially `app.py`, are located.


<img src="/img/180604-bottle-docker/bottle-app-response.png" width="100%" 
 class="shot rnd" alt="Bottle web app responding to requests from within a Docker container.">

Everything worked when you see a simple text-based HTTP response like what
is shown above in the screenshot of my Chrome browser.


## What's Next?
We just installed Docker and wrote a Bottle web app to run inside a 
container. That is just the beginning of how you can integrate Docker into 
your workflow.

Next up take a look at the [Bottle](/bottle.html), [Docker](/docker.html) 
and [deployment](/deployment.html) pages for more tutorials.

Questions? Let me know via a GitHub
[issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

Do you see a typo, syntax issue or just something that's confusing in this 
blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/180604-bottle-docker-macos.markdown)
and submit a pull request with a fix or 
[file an issue ticket on GitHub](https://github.com/mattmakai/fullstackpython.com/issues).
