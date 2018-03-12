title: Developing Flask Apps in Docker Containers on macOS
slug: develop-flask-web-apps-docker-containers-macos
meta: Learn how to set up and develop a new Flask web application within a Docker container.
category: post
date: 2018-03-09
modified: 2018-03-09
newsletter: False
headerimage: /img/180309-flask-docker/header.jpg
headeralt: Flask, Docker and Apple logos, copyright their respective owners.


Adding [Docker](/docker.html) to your [Python](/why-use-python.html) and 
[Flask](/flask.html) [development environment's](/development-environments.html) 
workflow can be a bit confusing when you are just getting started working with
containers. Let's quickly get Docker configured for developing Flask web 
applications on your local system.


## Our Tools
This tutorial is written for [Python 3](/python-2-or-3.html). It may work with
Python 2 but I have not tested it with the 
[soon-to-be deprecated 2.7 version](https://pythonclock.org/). 

[Docker for Mac](https://docs.docker.com/docker-for-mac/install/) is necessary.
I recommend the stable release unless you have an explicit purpose for the edge 
channel.

Within the Docker contain we will use:

* Python 3, specifically the
  [slim-3.6.4 version](https://hub.docker.com/r/library/python/tags/3.6-slim/)
  from Docker Hub
* [Flask](/flask.html) version 0.12.2

All of the code for the Dockerfile and the Flask app are available open source
under the MIT license on GitHub under the 
[docker-flask-mac directory](https://github.com/fullstackpython/blog-code-examples/tree/master/docker-flask-mac)
of the
[blog-code-examples](https://github.com/fullstackpython/blog-code-examples)
repository. Use the code for your own purposes as much as you like.


## Installing Docker on macOS
We need to install Docker before we can spin up our Docker containers. If you
already have Docker for Mac installed and working, feel free to jump to the
next section.

On your Mac, 
[download the Docker Community Edition (CE) for Mac](https://www.docker.com/community-edition#/download)
installer.

Install Docker.

Open Terminal.

Test your Docker installation with the `docker --version` command.

```
Docker version 17.12.0-ce, build c97c6d6
```


## Dockerfile

```
FROM python:3.6.4-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV DEBUG True

CMD ["python", "app.py"]
```

```
docker build -t flaskdock .
```


## Running the Container
Make sure to replace the absolute path for the volume to your own directory. 
```
docker run -p 4000:80 --volume=/Users/matt/devel/py/flaskdocker:/app flaskdock
```

## What's Next?
We just installed Docker and configured a Flask application to run inside a 
container. That is just the beginning of how you can integrate Docker into 
your workflow. Next up take a look at the [Docker](/docker.html) and 
[deployment](/deployment.html) pages for more related tutorials.

Questions? Let me know via a GitHub
[issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

Do you see a typo, syntax issue or just something that's confusing in this 
blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/180309-flask-docker-macos.markdown)
and submit a pull request with a fix or 
[file an issue ticket on GitHub](https://github.com/mattmakai/fullstackpython.com/issues).
