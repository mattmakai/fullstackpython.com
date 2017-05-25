title: Responsive Bar Charts with Bokeh, Flask and Python 3
slug: responsive-bar-charts-bokeh-flask-python-3
meta: How to build responsive bar charts with the Bokeh data visualization library, Flask and Pyton 3.
category: post
date: 2017-05-26
modified: 2017-05-26
headerimage: /img/170526-bar-charts-bokeh-flask/header.jpg
headeralt: Python, Flask and Bokeh logos.


[Bokeh](/bokeh.html) is a powerful open source Python library that allows 
developers to generate JavaScript data visualizations for their web 
applications *without writing any JavaScript*. While learning a 
JavaScript-based data visualization library like [d3.js](https://d3js.org/)
can be useful, it's often far easier to knock out a few lines of Python
code that get the job done.

With Bokeh we can create incredibly detailed interactive visualizations, 
or just traditional ones like the following bar chart.

<img src="/img/170526-bar-charts-bokeh-flask/chart-example-64.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Responsive bar chart with 64 bars.">


Let's use the 
[Flask](/flask.html) [web framework](/web-frameworks.html) with Bokeh to 
create custom bar charts in a Python web app.


## Our Tools
This tutorial works with either [Python 2 or 3](/python-2-or-3.html), 
but Python 3 is strongly recommended for new applications. In addition
to Python throughout this tutorial we will also use the following 
[application dependencies](/application-dependencies.html): 

* [Flask](/flask.html) web framework, 
  [version 0.12.2](https://github.com/pallets/flask/releases/tag/0.12.2)
* [Bokeh](/bokeh.html) data visualization library, 
  [version 0.12.5](https://github.com/bokeh/bokeh/releases/tag/0.12.5)
* [pandas](/pandas.html) data structures and analysis library, 
  [version 0.20.1](https://github.com/pandas-dev/pandas/releases/tag/v0.20.1)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/), which come
  packaged with Python 3, to install and isolate the Flask, Bokeh,
  and pandas libraries from any other Python projects you might be 
  working on

If you need help getting your 
[development environment](/development-environments.html) configured
before running this code, take a look at
[this guide for setting up Python 3 and Flask on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)

All code in this blog post is available open source under the MIT license 
on GitHub under the 
[bar-charts-bokeh-flask-python-3 directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples). 
Use the source code and abuse it as you like for your own applications.


## Installing Bokeh and Flask
Create a fresh virtual environment for this project to isolate our 
dependencies using the following command in the terminal. I typically run 
this command within a separate `venvs` directory where all my virtualenvs
are store.

```bash
python3 -m venv barchart
```

Activate the virtualenv.

```bash
source barchart/bin/activate
```

The command prompt will change after activating the virtualenv:

<img src="/img/170526-bar-charts-bokeh-flask/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Activating our Python virtual environment on the command line.">

Keep in mind that you need to activate the virtualenv in every new terminal 
window that you want this virtualenv to be used for your project.

Bokeh and Flask are installable into the now-activated virtualenv
using pip. Run this command to get the appropriate Bokeh and Flask
versions.

```
pip install bokeh==0.12.5 flask==0.12.2 pandas==0.20.1
```

After a brief download and installation period our required dependencies
should be installed within our virtualenv. Look for output like the 
following to confirm everything worked.

```
Installing collected packages: six, requests, PyYAML, python-dateutil, MarkupSafe, Jinja2, numpy, tornado, bokeh, Werkzeug, itsdangerous, click, flask, pytz, pandas
  Running setup.py install for PyYAML ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for tornado ... done
  Running setup.py install for bokeh ... done
  Running setup.py install for itsdangerous ... done
Successfully installed Jinja2-2.9.6 MarkupSafe-1.0 PyYAML-3.12 Werkzeug-0.12.2 bokeh-0.12.5 click-6.7 flask-0.12.2 itsdangerous-0.24 numpy-1.12.1 pandas-0.20.1 python-dateutil-2.6.0 pytz-2017.2 requests-2.14.2 six-1.10.0 tornado-4.5.1
```

Now we can start building our web application.


## Starting Our Flask App
We are going to first code a basic Flask application then add our bar 
chart to the rendered page.


`app.py`:

```python
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/<int:bars_count>/")
def chart(bars_count):
    if bars_count <= 0:
        bars_count = 1
    return render_template("chart.html", bars_count=bars_count)


if __name__ == "__main__":
    app.run(debug=True)
```

...explain code...

`templates/chart.html`:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Bar charts with Bokeh!</title>
  </head>
  <body>
    <h1>Bugs found over the past {{ bars_count }} days</h1>
  </body>
</html>
```

Short explanation of above HTML.

```
$(barchart) python app.py
```

Go to "localhost:5000" in your web browser. 

...Screenshots of it working...


## Generating the Bar Chart



## What's next?
Nice work creating a nifty configurable bar chart in Bokeh! Next
up you can modify the color scheme, change the input data source or try 
to create other types of charts.

There is a lot more than Bokeh can do, so be sure to check out the 
[official project documentation](http://bokeh.pydata.org/en/latest/) , 
[GitHub repository](https://github.com/bokeh/bokeh), 
the [Full Stack Python Bokeh page](/bokeh.html) or take a look at 
[other topics on Full Stack Python](/table-of-contents.html).

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

See something wrong in this blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170526-bar-charts-bokeh.markdown)
and submit a pull request.

