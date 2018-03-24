title: Creating Bar Chart Visuals with Bokeh, Bottle and Python 3
slug: python-bottle-bokeh-bar-charts
meta: Learn to create responsive bar charts using Bokeh, Bottle and Python 3.
category: post
date: 2017-07-25
modified: 2017-07-30
newsletter: False
headerimage: /img/170725-bottle-bokeh-bar-charts/header.jpg
headeralt: Python, Bottle and Bokeh logos.


The [Bokeh](/bokeh.html) open source Python visualization library assists 
developers with creating web browser visuals. You can build charts for 
web applications *without coding any JavaScript*, like you'd need to do
to use libraries such as [d3.js](https://d3js.org/) and plotly.

Bokeh can create many common and custom visualizations using only
Python, such as this bar chart we will create in this tutorial:

<img src="/img/170725-bottle-bokeh-bar-charts/chart-example-48.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Responsive Bokeh bar chart with 48 bars.">

Let's use the 
[Bottle](/bottle.html) [web framework](/web-frameworks.html) with Bokeh to 
build custom Python web app bar charts.


## Our Tools
This tutorial works with either [Python 2 or 3](/python-2-or-3.html), 
but Python 3 is strongly recommended for new applications. I used
[Python 3.6.2](https://www.python.org/downloads/release/python-362/) while 
writing this post. In addition to Python throughout this tutorial we 
will also use the following 
[application dependencies](/application-dependencies.html): 

* [Bottle](/bottle.html) web framework, 
  [version 0.12.13](https://github.com/bottlepy/bottle/tree/0.12.13)
* [Bokeh](/bokeh.html) data visualization library, 
  [version 0.12.6](https://github.com/bokeh/bokeh/releases/tag/0.12.6)
* [pandas](/pandas.html) data structures and analysis library, 
  [version 0.20.3](https://github.com/pandas-dev/pandas/releases/tag/v0.20.3)
* [pip](https://pip.pypa.io/en/stable/) and 
  [virtualenv](https://virtualenv.pypa.io/en/latest/), which come
  packaged with Python 3, to install and isolate the Bottle, Bokeh,
  and pandas libraries from other Python projects you are working on

If you need help getting your 
[development environment](/development-environments.html) configured
before running this code, take a look at
[this guide for setting up Python 3 and Bottle on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html).

All code in this blog post is available open source under the MIT license 
on GitHub under the 
[bar-charts-bokeh-bottle-python-3 directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples). 
Use the source code as you want to for your own projects.


## Installing Bottle and Bokeh
Create a new virtual environment for this project to isolate our 
dependencies using the following command in the terminal. I usually run the 
venv command within a separate `venvs` directory where all my virtualenvs
are store.

```bash
python3 -m venv bottlechart
```

Activate the virtualenv.

```bash
source bottlechart/bin/activate
```

The command prompt will change after activating the virtualenv:

<img src="/img/170725-bottle-bokeh-bar-charts/activate-virtualenv.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Activating our Python virtualenv for this project on the command line.">

Keep in mind that you need to activate the virtualenv in every new terminal 
window where you want to use the virtualenv to run the project.

Bokeh and Bottle are installable into the now-activated virtualenv
using pip. Run this command to get the appropriate Bokeh and Bottle
versions.

```
pip install bokeh==0.12.6 bottle==0.12.13 pandas==0.20.3
```

Our required dependencies will be installed within our virtualenv after
a brief download and installation period.

```
Installing collected packages: bottle, six, chardet, certifi, idna, urllib3, requests, PyYAML, python-dateutil, MarkupSafe, Jinja2, numpy, tornado, bkcharts, bokeh, pytz, pandas
  Running setup.py install for bottle ... done
  Running setup.py install for PyYAML ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for tornado ... done
  Running setup.py install for bkcharts ... done
  Running setup.py install for bokeh ... done
Successfully installed Jinja2-2.9.6 MarkupSafe-1.0 PyYAML-3.12 bkcharts-0.2 bokeh-0.12.6 bottle-0.12.13 certifi-2017.7.27.1 chardet-3.0.4 idna-2.5 numpy-1.13.1 pandas-0.20.3 python-dateutil-2.6.1 pytz-2017.2 requests-2.18.2 six-1.10.0 tornado-4.5.1 urllib3-1.22
```

We can now begin coding our web app.


## Building the Bottle App
First we'll code a basic Bottle application and then we will add the
bar charts to the rendered page.

Create a folder for your project named `bottle-bokeh-charts`. Within
`bottle-bokeh-charts` create a new file named `app.py` with the following
code: 

```python
import os
import bottle
from bottle import route, run, template


app = bottle.default_app()

TEMPLATE_STRING = """
<html>
 <head>
  <title>Bar charts with Bottle and Bokeh</title>
 </head>
 <body>
  <h1>Bugs found over the past {{ bars_count }} days</h1>
 </body>
</html>
"""


@route('/<num_bars:int>/')
def chart(num_bars):
    """Returns a simple template stating the number of bars that should
    be generated when the rest of the function is complete.
    """
    if num_bars <= 0:
        num_bars = 1
    return template(TEMPLATE_STRING, bars_count=num_bars)


if __name__ == '__main__':
    run(host='127.0.0.1', port=8000, debug=False, reloader=True)
```

The code shown above provides a short [Bottle](/bottle.html) application
with a single route, defined with the `chart` function. `chart` receives
an arbitrary integer value as input. The `template` function within 
`chart` uses the HTML template defined in `TEMPLATE_STRING` to render
an HTML page as a response to incoming requests.

The last two lines in the allow us to run the Bottle application 
in debug mode on port 8000. 
**Never use debug mode for production deployments!**
[WSGI servers](/wsgi-servers.html) like 
[Gunicorn](/green-unicorn-gunicorn.html) are built for handling real
traffic and will be easier to configure without major security
holes.

We can now test out our application.

Make sure your virtualenv is still activated and that you are in the 
base directory of your project where `app.py` is located. Run `app.py`
using the `python` command.

```
(bottlechart)$ python app.py
```

Go to [localhost:8000/16/](http://localhost:8000/16/) in your web browser.
You should see a header message about the number of bugs found over the
past 16 days. However, there's no bar chart to accompany that message
just yet.

<img src="/img/170725-bottle-bokeh-bar-charts/basic-app-no-chart.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="A simple Bottle app without the bar chart.">

Our single Bottle route is in place but it is not very exciting. Time
to create a nice-looking bar chart.


## Creating A Bar Chart with Bokeh
We'll build on our basic Bottle app foundation using some new Python code 
to engage the [Bokeh](/bokeh.html) library. 

Open `app.py` back up and add the following highlighted import lines.

```python
import os
import bottle
~~import random
~~from bokeh.models import (HoverTool, FactorRange, Plot, LinearAxis, Grid,
~~                          Range1d)
~~from bokeh.models.glyphs import VBar
~~from bokeh.plotting import figure
~~from bokeh.charts import Bar
~~from bokeh.embed import components
~~from bokeh.models.sources import ColumnDataSource
from bottle import route, run, template
```

The rest of our application will use these imports to generate random
data and the bar chart.

Our bar chart will have "software bugs found" for its theme. The data will
randomly generate each time the page is generated. In a real application
you would of course likely have a more stable and useful data source.

Continue modifying `app.py` so the section after the imports looks like
the following code. 

```python
app = bottle.default_app()

TEMPLATE_STRING = """
<html>
 <head>
  <title>Bar charts with Bottle and Bokeh</title>
~~  <link href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.css" 
~~        rel="stylesheet">
~~  <link href="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.css" 
~~        rel="stylesheet">
 </head>
 <body>
  <h1>Bugs found over the past {{ bars_count }} days</h1>
~~  {{ !the_div }}
~~  <script src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.js"></script>
~~  <script src="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.js"></script>
~~  {{ !the_script }}
 </body>
</html>
"""


@route('/<num_bars:int>/')
def chart(num_bars):
    """Returns a simple template stating the number of bars that should
    be generated when the rest of the function is complete.
    """
    if num_bars <= 0:
        num_bars = 1
~~    data = {"days": [], "bugs": [], "costs": []}
~~    for i in range(1, num_bars + 1):
~~        data['days'].append(i)
~~        data['bugs'].append(random.randint(1,100))
~~        data['costs'].append(random.uniform(1.00, 1000.00))

~~    hover = create_hover_tool()
~~    plot = create_bar_chart(data, "Bugs found per day", "days",
~~                            "bugs", hover)
~~    script, div = components(plot)
~~    return template(TEMPLATE_STRING, bars_count=num_bars,
~~                    the_div=div, the_script=script)
```

The `chart` function gains three new lists that are randomly generated by 
[Python 3's super-handy random module](https://docs.python.org/3/library/random.html).

`chart` calls two functions, `create_hover_tool` and `create_bar_chart`.
We haven't written those functions yet, so let's do that now. Add these
two new functions below the `chart` function, but before the 
`if __name__ == '__main__':` line.

```python
def create_hover_tool():
    # we'll code this function in a moment
    return None


def create_bar_chart(data, title, x_name, y_name, hover_tool=None,
                     width=1200, height=300):
    """Creates a bar chart plot with the exact styling for the centcom
       dashboard. Pass in data as a dictionary, desired plot title,
       name of x axis, y axis and the hover tool HTML.
    """
    source = ColumnDataSource(data)
    xdr = FactorRange(factors=data[x_name])
    ydr = Range1d(start=0,end=max(data[y_name])*1.5)

    tools = []
    if hover_tool:
        tools = [hover_tool,]

    plot = figure(title=title, x_range=xdr, y_range=ydr, plot_width=width,
                  plot_height=height, h_symmetry=False, v_symmetry=False,
                  min_border=10, toolbar_location="above", tools=tools,
                  responsive=True, outline_line_color="#666666")

    glyph = VBar(x=x_name, top=y_name, bottom=0, width=.8,
                 fill_color="#6599ed")
    plot.add_glyph(source, glyph)

    xaxis = LinearAxis()
    yaxis = LinearAxis()

    plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))
    plot.toolbar.logo = None
    plot.min_border_top = 0
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = "#999999"
    plot.yaxis.axis_label = "Bugs found"
    plot.ygrid.grid_line_alpha = 0.1
    plot.xaxis.axis_label = "Days after app deployment"
    plot.xaxis.major_label_orientation = 1
    return plot
```

That's a lot of new code. The `create_hover_tool` function does not do 
anything just yet other than returning.  `None`, which is used when no
hover tool is desired for the graph.

Within the `create_bar_chart` function we take in our randomly-generated 
data source and convert it into a `ColumnDataSource` object that is one 
type of input object we can pass to Bokeh functions. We specify two ranges 
for the chart's x and y axes.

The `tools` list will remain empty because we do not yet have a hover tool.
A lot of the magic happens in the lines where we create `plot` using the 
`figure` function. We specify all the parameters we want our graph to have
such as the size, toolbar, borders and whether or not the graph should be
responsive upon changing the web browser size.

The `VBar` object creates vertical bars to add them to the plot with
the `add_glyph` function.

The last lines of the function change the graph's appearance. For
example, we took away the `Bokeh` logo by specifying 
`plot.toolbar.logo = None` and added labels to both axes. I recommend 
keeping the 
[bokeh.plotting](http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh-plotting)
documentation open so you know what your options are for customizing the
charts and visualizations.

Let's test our app by trying a 6-bar chart. The Bottle app should 
automatically reload when you save `app.py` with the new code. If you shut 
down the development server, start it back up using `python app.py`.

When you start up the development server you will receive the following 
warning because we are using the latest (at the time of this writing) 0.12.6 
Bokeh release. 

```
/Users/matt/Envs/bottlechart/lib/python3.6/site-packages/bokeh/util/deprecation.py:34: BokehDeprecationWarning: 
The bokeh.charts API has moved to a separate 'bkcharts' package.

This compatibility shim will remain until Bokeh 1.0 is released.
After that, if you want to use this API you will have to install
the bkcharts package explicitly.
```

Eventually a separate `bkcharts` project will be required but for now 
we can keep our code as is.

Open your browser to [localhost:8000/6/](http://localhost:8000/6/).

<img src="/img/170725-bottle-bokeh-bar-charts/chart-example-6.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Responsive Bokeh bar chart with 6 bars.">

That one looks a bit sparse, so we can crank it up by 3x to 18 bars
by going to [localhost:5000/18/](http://localhost:5000/18/).

<img src="/img/170725-bottle-bokeh-bar-charts/chart-example-18.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Responsive Bokeh bar chart with 18 bars.">

Now another 5x to 90 bars with 
[localhost:5000/90/](http://localhost:8000/90/).

<img src="/img/170725-bottle-bokeh-bar-charts/chart-example-90.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Responsive Bokeh bar chart with 90 bars.">

Looking good so far! What about that hover tool we skipped over though?
We can add the hover tool with just a few more lines of code in the 
`create_hover_tool` function.


## Creating a Hover Tool
Add these highlighted lines to `app.py` within the `create_hover_tool`
function.

```python
def create_hover_tool():
~~    """Generates the HTML for the Bokeh's hover data tool on our graph."""
~~    hover_html = """
~~      <div>
~~        <span class="hover-tooltip">$x</span>
~~      </div>
~~      <div>
~~        <span class="hover-tooltip">@bugs bugs</span>
~~      </div>
~~      <div>
~~        <span class="hover-tooltip">$@costs{0.00}</span>
~~      </div>
~~    """
~~    return HoverTool(tooltips=hover_html)
```

Embedding HTML within your Python application isn't usually a great
idea but it works for small snippets like this hover tool.
The hover tool uses `$x` to show the bar's x axis, `@bugs` to show the 
"bugs" field from our data source, and `$@costs{0.00}` to show the "costs" 
field formatted as a dollar amount with exactly 2 decimal places.

Ensure that you changed `return None` to 
`return HoverTool(tooltips=hover_html)` in your function so the results of 
the new code are reflected in the refreshed graph.

Go back to the browser and reload the 
[localhost:8000/122/](http://localhost:8000/122) page.

<img src="/img/170725-bottle-bokeh-bar-charts/chart-example-122.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Responsive Bokeh bar chart with 122 bars.">

Well done! Try playing around with the number of bars in the URL and the
window size to see what the graph looks like under different conditions.

The chart gets crowded with more than 100. However, you can try to create
as many bars as you want if your computer can handle the rendering.
This screenshot shows what the completely impractical amount of 40,000
bars looks like:

<img src="/img/170725-bottle-bokeh-bar-charts/chart-example-40000.png" width="100%" class="technical-diagram img-rounded" style="border:1px solid #ccc" alt="Responsive Bokeh bar chart with 40000 bars.">

You may need to do some more work to get the chart to be useful for displaying
more than a couple hundred bars at a time.


## What now?
We created a nice little configurable bar chart using the Bokeh code library. 

Next you can change the input data source, work with other types of charts
or modify the chart color scheme.

There is a lot more than Bokeh can do. Take a look at the 
[official project documentation](http://bokeh.pydata.org/en/latest/) , 
[GitHub repository](https://github.com/bokeh/bokeh), 
the [Full Stack Python Bokeh page](/bokeh.html) or take a look at 
[other topics on Full Stack Python](/table-of-contents.html).

Questions? Let me know via 
[a GitHub issue ticket on the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues), 
on Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).

Do you see something wrong in this blog post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/170725-bar-charts-bottle-bokeh.markdown)
and submit a pull request with a fix.
