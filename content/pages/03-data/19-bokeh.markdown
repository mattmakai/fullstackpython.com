title: Bokeh
category: page
slug: bokeh
sortorder: 0319
toc: False
sidebartitle: Bokeh
meta: Bokeh is a data visualization library that builds visuals in Python and outputs them in JavaScript.


[Bokeh](https://bokeh.pydata.org/en/latest/) is a data visualization
library that allows a developer to code in Python and output 
[JavaScript](/javascript.html) charts and visuals in web browsers.

<img src="/img/logos/bokeh.jpg" width="100%" alt="Bokeh logo on a dark background." class="shot rnd outl">


## Why is Bokeh a useful library?
Web browsers are ideal clients for consuming interactive visualizations.
However, libraries such as [d3.js](https://d3js.org/) can be
difficult to learn and time consuming to connect to your Python backend
web app. Bokeh instead generates the JavaScript for your application while
you write all your code in Python. The removal of context switching between
the two programming languages can make it easier and faster to create 
charts and visualizations. 


## What do Bokeh visualizations look like?
Bokeh can create any type of custom graph or visualization. For example,
here is a screenshot of a bar chart created with the 
[figure](http://bokeh.pydata.org/en/latest/docs/reference/plotting.html)
plot:

<img src="/img/170526-bar-charts-bokeh-flask/chart-example-64.png" width="100%" class="shot img rnd" alt="Responsive Bokeh bar chart with 64 bars.">

For more references, including interactive live demonstrations, check out
these sites:

* The 
  [official Bokeh gallery](http://bokeh.pydata.org/en/latest/docs/gallery.html)
  has many example Bokeh visual formats.

* [Bokeh Applications](https://demo.bokeh.org/) hosts numerous
  data visualizations built with Bokeh.


### Bokeh resources
Bokeh is under heavy development ahead of the upcoming 1.0 release. Note that
while all of the following tutorials are useful, it is possible some of the
basic syntax will change as the library's API is not yet stable.

* [Integrating Bokeh Visualisations Into Django Projects](https://hackernoon.com/integrating-bokeh-visualisations-into-django-projects-a1c01a16b67a)
  does a nice job of walking through how to use Bokeh to render
  visualizations in [Django](/django.html) projects.

* [Responsive Bar Charts with Bokeh, Flask and Python 3](/blog/responsive-bar-charts-bokeh-flask-python-3.html) is my recommended
  tutorial for those new to Bokeh who want to try out the library and get
  an example project running quickly with [Flask](/flask.html).

* [Fun with NFL Stats, Bokeh, and Pandas](https://j253.github.io/blog/fun-with-nfl-stats.html)
  takes an NFL play-by-play data set, shows how to wrangle the data into 
  an appropriate format then explains the code that uses Bokeh to visualize
  it.

* [Data is beautiful: Visualizing Roman imperial dynasties](http://machineloveus.com/data-is-beautiful-visualizing-roman-imperial-dynasties/)
  provides a walkthrough for creating a gorgeous visualization based on
  historical Roman data. The post is about more than just the visual, it also
  goes into the ideation, data wrangling and analysis phases that came
  before using Bokeh to show the results.

* [Visualizing with Bokeh](https://programminghistorian.org/en/lessons/visualizing-with-bokeh)
  gives a detailed explanation with the code for number Bokeh visuals
  you can output while working with a [pandas](/pandas.html) data set.

* [Interactive Data Visualization in Python With Bokeh](https://realpython.com/python-data-visualization-bokeh/)
  is a great beginners tutorial that shows you how to structure your data,
  draw your first figures and add interactivity to the visualizations.

* [Creating Bar Chart Visuals with Bokeh, Bottle and Python 3](/blog/python-bottle-bokeh-bar-charts.html)
  is a tutorial that combines the [Bottle](/bottle.html) 
  [web framework](/web-frameworks.html)

* [Building Bullet Graphs and Waterfall Charts with Bokeh](http://pbpython.com/bokeh-bullet-waterfall.html)
  covers buildings two types of useful visualizations into your applications
  using Bokeh.

* [Interactive Visualization of Australian Wine Ratings](http://pbpython.com/wine_visualization.html)
  builds a non-trivial visualization with a nice sample set of data based
  on wine ratings.

* [Visualization with Bokeh](http://www.blog.pythonlibrary.org/2016/07/27/python-visualization-with-bokeh/)

* [Drawing a Brain with Bokeh](http://merqur.io/2015/10/02/drawing-a-brain-with-bokeh/)
  is a fun example of a chord diagram that represents neural connections in
  the brain.

* [Bryan Van de Ven on Bokeh](https://pythonpodcast.com/episode-22-bryan-van-de-ven-on-bokeh/)
  is a podcast episode by one of the main Bokeh maintainers.

* [The Python Visualization Landscape](https://www.youtube.com/watch?v=FytuB8nFHPQ)
  by Jake VanderPlas at PyCon 2017 covers many Python data visualization
  tools, including Bokeh.

* This 
  [flask-bokeh-example](https://github.com/realpython/flask-bokeh-example/blob/master/tutorial.md)
  project has the code to create a simple chart with Bokeh and 
  [Flask](/flask.html).

* [Bokeh vs Dash — Which is the Best Dashboard Framework for Python?](https://blog.sicara.com/bokeh-dash-best-dashboard-framework-python-shiny-alternative-c5b576375f7f)
  contains a single project that was written in both Dash and Bokeh. The
  author gives his subjective view on the implementation difficulty 
  although the web application only contained a single type of data 
  visualization so it is hard to drawn any real conclusions from his
  opinion.

* [Realtime Flight Tracking with Pandas and Bokeh](https://www.geodose.com/2019/01/realtime-flight-tracking-pandas-bokeh-python.html)
  provides a great example of combining [pandas](/pandas.html) for structuring
  data with Bokeh for visualization.

* [How to Create an Interactive Geographic Map Using Python and Bokeh](https://towardsdatascience.com/how-to-create-an-interactive-geographic-map-using-python-and-bokeh-12981ca0b567)
  shows how to use a `GeoJSONDataSource` as input for Bokeh and draw a
  map with the data.

