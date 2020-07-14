title: Data Visualization
category: page
slug: data-visualization
sortorder: 0318
toc: False
sidebartitle: Data visualization
meta: Data visualization transforms raw numbers into a graphic medium that allows humans to better understand patterns and trends.


Data visualizations transform raw numbers into graphic formats that make it
easier for humans to see patterns, trends and other useful information.


### Python data visualization tools
* [Bokeh](https://bokeh.pydata.org/en/latest/)

* [HoloViews](http://holoviews.org/)

* [Matplotlib](https://matplotlib.org/)

* [Chartify](https://labs.spotify.com/2018/11/15/introducing-chartify-easier-chart-creation-in-python-for-data-scientists/) 
  ([source code](https://github.com/spotify/chartify/))

* [Graphviz](https://pypi.org/project/graphviz/)


### Python-specific data viz resources
* [Python Data Visualization 2018: Why So Many Libraries?](https://www.anaconda.com/blog/developer-blog/python-data-visualization-2018-why-so-many-libraries/)
  is an in-depth article on the Python data visualization tools landscape.
  A must-read whether you are new to the space or have been using one or
  more of these libraries for awhile.

* The [Python Graph Gallery](https://python-graph-gallery.com/) has a slew 
  of visualizations created with Python and includes the code used to 
  produced each one.

* [Python & OpenGL for Scientific Visualization](https://www.labri.fr/perso/nrougier/python-opengl/)
  is a free book that shows how to combine open source tools such as 
  [PyOpenGL](http://pyopengl.sourceforge.net/) with Python 
  [data analysis](/data-analysis.html) libraries to generate interactive
  scientific data visualizations.

* [10 Useful Python Data Visualization Libraries for Any Discipline](https://blog.modeanalytics.com/python-data-visualization-libraries/)
  is a straightforward overview of Python packages that create Python
  visualizations.

* [Introduction to Data Visualization with Altair](http://pbpython.com/altair-intro.html)
  is a starter post for the wonderful 
  [Altair](https://altair-viz.github.io/) visualization tool written in
  Python.

* [The Next Level of Data Visualization in Python](https://towardsdatascience.com/the-next-level-of-data-visualization-in-python-dd6e99039d5e)
  uses the [Plotly](https://plot.ly/python/) graphing library to draw
  more complex visualizations.

* [An introduction to Altair](http://vallandingham.me/altair_intro.html) 
  provides another wonderful tutorial on this data visualization tool.

* [A Dramatic Tour through Python’s Data Visualization Landscape](https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/)
  provides examples with the ggplot and Altair libraries. The 
  question-and-answer format for what you can do with the data is a really
  good model that keeps your attention throughout the post.

* [How to Generate FiveThirtyEight Graphs in Python](https://www.dataquest.io/blog/making-538-plots/)
  gives a great tutorial on generating a specific style graph with
  [pandas](/pandas.html) and [Matplotlib](/matplotlib.html) that is
  similar to [FiveThirtyEight](https://fivethirtyeight.com/)'s plots.

* [Intro to pdvega - Plotting for Pandas using Vega-Lite](http://pbpython.com/pdvega.html)
  shows how to generate plots from your 
  [pandas](/pandas.html)-structured data using 
  [pdvega](https://github.com/altair-viz/pdvega).

* [Sorting Algorithms Visualized in Python](https://www.makeartwithpython.com/blog/visualizing-sort-algorithms-in-python/)
  uses Python, numpy and scikit-image to animate how sorting algorithms 
  work.

* [How to Build a Reporting Dashboard using Dash and Plotly](https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f)
  explains how to use the Dash library to take a bunch of data and
  turn it into a nice-looking dashboard.

* [The reason I am using Altair for most of my visualization in Python](http://fernandoi.cl/blog/posts/altair/)
  explains why this wrapper for [Vega-lite](https://vega.github.io/vega-lite/)
  is awesome and that the author uses Altair because 
  [Matplotlib](/matplotlib.html) can be very complicated for whipping up 
  quick visualizations.


### Beautiful example visualizations
Sometimes you need inspiration from other sources to figure out what
you want to build. The following links have made me excited about data
visualization and gave me ideas for what to build.

* [Roads to Rome](http://roadstorome.moovellab.com/) is a beautiful
  visualization showing the data behind the expression "all roads lead 
  to Rome" and whether or not there is a "Rome" central city in every 
  country.

* [Monarchs](https://thebackend.dev/monarchs/) is a wonderful 1,000 year
  history visual of European rulers. The developer also wrote an in-depth
  article on 
  [how Monarchs was created](https://thebackend.dev/building-monarchs)
  using [d3.js](/d3-js.html).

* [Star Wars: The Force Accounted](https://www.bloomberg.com/graphics/2015-star-wars-the-force-accounted/)
  is Bloomberg's way of breaking down on-screen action between light
  and dark sides, the main characters, various bits about the Force
  and other data extracted from the movies.

* [What do numbers look like?](https://johnhw.github.io/umap_primes/index.md.html)
  is a Python 3 dimensional visualization of millions of integers, colored
  by special factors such as prime and Fibonacci numbers.

* [Bay Area Housing Marketing Analysis: Part 1](https://blog.checkyo.tech/2018/08/06/bay-area-housing-market-analysis/)
  and
  [Part 2](https://blog.checkyo.tech/2018/08/15/bay-area-housing-market-analysis-part-2/)
  are a combination of inspiration and tutorial. These posts contain a 
  ton of data analysis and graphing and show numerous ways to slice and 
  present information.

* [How We Animated Trillions of Tons of Flowing Ice](http://dwtkns.com/posts/flowing-ice.html)
  breaks down the process that the NY Times data team used to create the
  beautiful 
  [Antarctic Dispatches](https://www.nytimes.com/interactive/2017/05/18/climate/antarctica-ice-melt-climate-change.html)
  articles that show how glaciers and ice are moving.

* Who knew good old histograms could be so fascinating? Check out this
  post titled 
  [What's so hard about histograms?](http://tinlizzie.org/histograms/)
  and scroll through to learn a ton about the details you can think about
  when creating these types of data visuals.

* [Optimized Brewery Road Trip, With Genetic Algorithm](https://flowingdata.com/2019/02/08/optimized-brewery-road-trip-with-genetic-algorithm/)
  shows how a heuristic solving approach such as a genetic algorithm can be
  used to handle a version of the Traveling Salesman Problem (TSP), but
  with the more fun Top 100 American brewery locations.


### Data visualization resources
* [Guides for visualizing data](https://flowingdata.com/2020/06/01/guides-for-visualizing-reality/)
  provides the thought processes that you can use when you are
  showing uncertainty, incompletet data, differences, outliers,
  and other common scenarios that occur when your data is messy -
  and it usually is!

* [Data visualization, from 1987 to today](https://medium.economist.com/data-visualisation-from-1987-to-today-65d0609c6017)
  is a wonderful reference about the pre-computer age era of visualization
  which was a combination of cartography, art and statistics rather than
  any cohesive field as it is often seen today. The images showing how
  people worked with paper to build their visuals add fantastic context to
  the story.

* [Xenographics](https://xeno.graphics/) presents uncommon and unusual
  visualization formats such as the 
  [Manhattan Plot](https://xeno.graphics/manhattan-plot/) and
  [Time Curve](https://xeno.graphics/time-curve/).

* [Engineering Intelligence Through Data Visualization at Uber](https://eng.uber.com/data-viz-intel/)
  explains how Uber's data visualization team grew from 1 person to 15
  and the output they created along the way, including the open source
  tool [react-vis](https://uber.github.io/react-vis/).

* The Practitioner's Guide to System Dashboard Design series covers a
  lot of ground for what you should consider when building one form
  of visualization, the data dashboard:
  
    * [Part 1: Structure and Layout](http://onemogin.com/observability/dashboards/practitioners-guide-to-system-dashboard-design.html)
    * [Part 2: Presentation and Accessibility](http://onemogin.com/observability/dashboards/practitioners-guide-to-system-dashboard-design-p2.html)
    * [Part 3: What Charts to Use](http://onemogin.com/observability/dashboards/practitioners-guide-to-system-dashboard-design-p3.html)
    * [Part 4: Context Improvement](http://onemogin.com/observability/dashboards/practitioners-guide-to-system-dashboard-design-p4.html)

* [Truncating the Y-Axis: Threat or Menace?](https://engineering.tableau.com/truncating-the-y-axis-threat-or-menace-d0bce66d4d08)
  is a great in-indepth explanation of why something that seems as 
  straightforward as laying out the Y-Axis requires thought and
  care otherwise the visualization could end up being misleading.

