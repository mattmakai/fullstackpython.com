title: Best Python Videos
category: page
slug: best-python-videos
sortorder: 0109
toc: False
sidebartitle: Best Python Videos
meta: Watch the best videos to learn Python programming from developer experts in the community.


If you prefer to learn Python programming by watching videos then this is the
resource for you. I've watched hundreds of live technical talks and combed
through videos to pick out the ones with great speakers who'll teach you the
most about the language and ecosystem. 

This page links to the best free videos as well as other video lists so you 
can do your own searching through the huge backlog of conference and meetup 
talks from the past several years. 

<div class="well see-also">Check out the <a href="/best-python-resources.html">best Python resources</a> for links to great books and articles as well as <a href="/best-python-podcasts.html">must-listen Python podcasts</a> for audio-only shows.</div>


## Web development videos
The following [web development](/web-development.html) videos cover the broad
topics of using [web frameworks](/web-frameworks.html) like 
[Django](/django.html), [Flask](/flask.html), [Pyramid](/pyramid.html) and 
[other frameworks](/other-web-frameworks.html), as well as 
[web design](/web-design.html) and [deployments](/deployment.html).

* My [EuroPython 2014 "Full Stack Python"](https://www.youtube.com/watch?v=s6NaOKD40rY)
  talk goes over each topic from this guide and provides context for how the
  pieces fit together. 
  The [talk slides](http://www.mattmakai.com/presentations/2014-full-stack-python-berlin.html) are also available. Even though the talk is from 2014, almost all
  of the general web development principles remain consistent in 2018.

* [Kate Heddleston](https://twitter.com/heddle317) gave a talk at PyCon 2014 
  called 
  "[Full-stack Python Web Applications](http://pyvideo.org/video/2591/so-you-want-to-be-a-full-stack-developer-how-to)"
  with clear visuals for how numerous layers of the Python web
  stack fit together. There are also [slides available from the talk](https://speakerdeck.com/pycon2014/so-you-want-to-be-a-full-stack-developer-how-to-build-a-full-stack-python-web-application-by-kate-heddleston)
  with all the diagrams.

* [Taking Django Async](https://www.youtube.com/watch?v=-7taKQnndfo) is
  a great overview by [Andrew Godwin](https://github.com/andrewgodwin),
  who created South (now Django Migrations as part of the core framework)
  and [Django Channels](https://channels.readthedocs.io/en/latest/). He
  discusses the synchronous blocking worker design of 
  [WSGI](/wsgi-servers.html) and why it is incompatible with asynchronous
  protocols like [WebSockets](/websockets.html). A potential solution
  could be a new protocol like Asynchronous Server Gateway Interface (ASGI),
  but how far would the integration into Django need to go and would it
  be worth the pain? Andrew does a great job of mixing the philosophical
  questions with technical implementation details throughout the talk.

* [Design 101 for Developers](https://academy.realm.io/posts/christopher-downer-design-101-for-developers/)
  covers a difficult topic for many analytic-minded developers to learn:
  design. The talk is not specific to [web development](/web-development.html) 
  or [web design](/web-design.html) but instead explains general design
  principles such as spacing, consistency and making interactions obvious
  for a user.

* [How Netflix does failovers in 7 minutes flat](https://www.youtube.com/watch?v=iQI56-up3Yk)
  by Amjith Ramanujam at PyCon US was an excellent talk on handling
  network outages and predicting the reliability of failover routes.
  This talk is worth watching even for the data visualizations alone!

* Kate Heddleston and I gave a talk at DjangoCon 2014 called
  [Choose Your Own Django Deployment Adventure](https://www.youtube.com/watch?v=QrFEKghISEI)
  which walked through many of the scenarios you'd face when deploying your
  first Django website.

* The [Discover Flask](https://github.com/realpython/discover-flask) series is
  a detailed Flask tutorial on video with corresponding code examples on 
  GitHub.

* [Designing Django's Migrations](http://pyvideo.org/video/2630/designing-djangos-migrations)
  covers Django 1.7's new migrations from the main programmer 
  of South and now Django's built-in migrations, Andrew Godwin.

* DjangoCon US videos from 
  [2019](https://www.youtube.com/playlist?list=PL2NFhrDSOxgXXUMIGOs8lNe2B-f4pXOX-),
  [2018](https://www.youtube.com/watch?v=pY-oje5b5Qk&list=PL2NFhrDSOxgW5tKoKmUyuubsbTfRgvT6z),
  [2017](https://www.youtube.com/playlist?list=PL2NFhrDSOxgXmA215-fo02djziShwLa6T),
  [2016](https://www.youtube.com/playlist?list=PL2NFhrDSOxgX-A4qpaf3rRaEnEe7166Ac),
  [2015](https://www.youtube.com/playlist?list=PL2NFhrDSOxgWvzf40lYJ8gohFciQqRx3K),
  [2014](https://www.youtube.com/playlist?list=PLE7tQUdRKcybbNiuhLcc3h6WzmZGVBMr3), are all available
  free of charge.

* DjangoCon EU videos are also available from 
  [2017](https://www.youtube.com/user/djangoconeurope/videos),
  [2016](http://pyvideo.org/events/djangocon-europe-2016.html),
  and [2015](https://vimeo.com/channels/952478/videos).

* [GoDjango](https://godjango.com/) screencasts and tutorials are free short
  videos for learning how to build Django applications.

* The videos and slides from 
  [Django: Under the Hood 2015](https://www.youtube.com/channel/UC9T1dhIlL_8Va9DxvKRowBw)
  are from Django core committers and provide insight into the 
  [ORM](/django-orm.html), internationalization, 
  [templates](/django-templates.html) and other important 
  [web framework](/web-frameworks.html) topics.


## Core Python language videos
The core Python programming language has many new features now that almost
all [community](/python-community.html) resources are working on 
[Python 3](/python-2-or-3.html) instead of split across legacy 2.x branches.
The following videos cover topics within the core Python language primarily
relevant to Python 3 features although some can be used with Python 2 as 
well.

* Jessica McKellar's 
  [Building and breaking a Python sandbox](https://www.youtube.com/watch?v=sL_syMmRkoU)
  is a fascinating walk through the lower layers of the Python interpreter.

* Brandon Rhodes' 
  [All Your Ducks In A Row: Data Structures in the Std Lib and Beyond](https://www.youtube.com/watch?v=fYlnfvKVDoM)
  goes through how data structures are implemented, how to select a
  data structure appropriate to your application and how the list and 
  dictionary can be used in many situations.

* Guido van Rossum's 
  [Python Language](https://www.youtube.com/watch?v=YgtL4S7Hrwo) keynote
  talk from PyCon 2016 reinforced that there would be no Python version 2.8
  and that development on backported security releases into the Python 2
  branch would end by January 1, 2020. Guido also covered many topics
  important to the Python language community like expanding the number and
  backgrounds of core committers.

* The talk [Python Descriptors](https://www.youtube.com/watch?v=ZdvpNaWwx24) 
  by Simeon Franklin explains the what and why of this core Python language 
  feature.

* David Beazley gives an amazing live coded performance to show
  [Python concurrency](https://www.youtube.com/watch?v=MCs5OvhV9S4)
  using threads, event loops and coroutines. David makes the live coding
  look easy but a whole lot of work must've gone into that talk.

* [What is a Python Core Developer?](https://www.youtube.com/watch?v=hhj7eb6TrtI)
  explains the responsibilities, projects, repositories and expectations of
  core Python committers as well as how to become one.

* [Google's Python Class](https://developers.google.com/edu/python/) contains
  lecture videos and exercises for learning Python.


## Video compilations
All major Python conferences, as well as most regional ones, release 
technical talk videos for free. These sites either aggregate the thousands
of videos that have been released or are lists from specific conferences
like [PyCon US](https://us.pycon.org/) and 
[EuroPython](https://europython.eu/).

* [PyVideo](http://pyvideo.org/) organizes and indexes thousands of Python
  videos from both major conferences and meetups.

* [Incredible Technical Speakers](https://github.com/mattmakai/incredible-technical-speakers)
  is a repository I put together that features software developer speakers
  talking about programming language agnostic topics. The list is intended
  to emphasize professional software developers who also have the ability to
  engage an audience of peers with an exciting talk. These talks are relevant
  to all software developers even though not every talk is specific to the
  Python language.

* PyCon US videos from 
  [2019](https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ/videos),
  [2018](https://www.youtube.com/channel/UCsX05-2sVSH7Nx3zuk3NYuQ/videos),
  [2017](https://www.youtube.com/channel/UCrJhliKNQ8g0qoE_zvL8eVg/videos),
  [2016](https://www.youtube.com/channel/UCwTD5zJbsQGJN75MwbykYNw/videos),
  [2015](https://www.youtube.com/channel/UCgxzjK6GuOHVKR_08TT4hJQ/videos)
  and [2014](https://www.youtube.com/user/PyCon2014/videos)
  are all available online for free.

* All of the talk videos are available on YouTube for 
  [EuroPython 2019](https://www.youtube.com/playlist?list=PL8uoeex94UhHFRew8gzfFJHIpRFWyY4YW),
  [EuroPython 2018](https://www.youtube.com/watch?v=LoRq9yGeBWY&list=PL8uoeex94UhFrNUV2m5MigREebUms39U5),
  [EuroPython 2017](https://www.youtube.com/watch?v=OCHrzW-R3QI&list=PL8uoeex94UhG9QAoRICebFpeKK2M0Herh),
  [EuroPython 2016](https://www.youtube.com/playlist?list=PL8uoeex94UhE3FDvjacSlHFffoNEoPzzm),
  [EuroPython 2015](https://www.youtube.com/watch?v=bp3mCgrdMxU&list=PL8uoeex94UhGGUH0mFb-StlZ1WYGWiJfP),
  [EuroPython 2014](https://www.youtube.com/watch?v=8xHd3JkhWd4&list=PL8uoeex94UhEomMao7wuOrOGuj3jxJYlz)
  and [earlier years](https://www.youtube.com/user/PythonItalia/playlists).

