title: Data analysis
category: page
slug: data-analysis
sortorder: 0315
toc: False
sidebartitle: Data analysis
meta: Data analysis is a broad set of activities that involves cleaning, processing, transforming and understanding a data collection.


Data analysis involves a broad set of activities to clean, process and
transform a data collection to learn from it. Python is commonly used
as a programming language to perform data analysis because many tools,
such as [Jupyter Notebook](/jupyter-notebook.html), 
[pandas](/pandas.html) and [Bokeh](/bokeh.html), are written in Python 
and can be quickly applied rather than coding your own data analysis
libraries from scratch.


### Data analysis resources
* The following series on data exploration uses Python as the 
  implementation language while walking through various stages of
  how to analyze a data set.

    * [Part 1](https://www.districtdatalabs.com/data-exploration-with-python-1)
      gives insight into how you should think about data and clarify
      what you are looking to learn.
    * [Part 2](https://www.districtdatalabs.com/data-exploration-with-python-2)
      explains categorization and transforming a data set into one that
      is easier to analyze.
    * [Part 3](https://www.districtdatalabs.com/data-exploration-with-python-3)
      shows how to visualize the results of your data exploration.

* [PyData 101](https://speakerdeck.com/jakevdp/pydata-101) presents the
  slides for one of the leading developers in the Python ecosystem on how
  to orient yourself if you are new to data science.

* [The Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
  is available to read for free online, although I also recommend
  buying the book as it is a great resource for learning the topic.

* [PyData TV](https://www.youtube.com/user/PyDataTV) contains all the
  videos from the PyData conference series. The conference talks are
  often given by professional data scientists and the developers who
  write these analysis libraries, so there is a wealth of information
  not necessarily captured anywhere else.

* [Python Plotting for Exploratory Data Analysis](http://pythonplot.com/)
  is a great tutorial on how to use simple data visualizations to bootstrap
  your understanding of a data set. The walkthrough covers histograms, time
  series analysis, scatter plots and various forms of bar charts.

* This series entitled "Agile Analytics" has three parts that cover how to
  work in a data science team and how to operate one if you are a manager:
  
    * [Part 1: The Good Stuff](https://www.locallyoptimistic.com/post/agile-analytics-p1/)
    * [Part 2: The Bad Stuff](https://www.locallyoptimistic.com/post/agile-analytics-p2/)
    * [Part 3: The Adjustments](https://www.locallyoptimistic.com/post/agile-analytics-p3/)

* [Learning Seattle's Work Habits from Bicycle Counts](https://jakevdp.github.io/blog/2015/07/23/learning-seattles-work-habits-from-bicycle-counts/)
  provides a great example of using open data, in this case 
  [from the city of Seattle](https://data.seattle.gov/), messing with it
  using Python and [pandas](/pandas.html), then charting it using
  skikit-learn. You can do this type of analysis on almost any data set
  to find out its patterns.

* [Exploring the shapes of stories using Python and sentiment APIs](https://indico.io/blog/plotlines/)
  is a wonderful read with context for the problem being solved, plenty of
  insight into how to reproduce the results with your own code and a good
  number of charts that show how sentiment analysis can extract information
  from blocks of text.

* [How to automate creating high end virtual machines on AWS for data science projects](https://tsaprailis.com/2017/09/11/How-to-automate-creating-a-virtual-machine-for-data-science/)
  walks through setting up a 
  [development environment](/development-environments.html) on Amazon Web 
  Services so that you can perform data analysis without owning a 
  high-end computer. Also check out the 
  [Introduction to AWS for Data Scientists](https://www.dataquest.io/blog/introduction-to-aws-for-data-scientists/)
  for another tutorial that shows you how to set up additional commonly-used
  data science tools on AWS.

* [Analyzing bugs.python.org](https://tirkarthi.github.io/python/2018/06/26/analyzing-python-bug-tracker.html)
  uses 
  [extracted data from CPython development](https://github.com/tirkarthi/cpython-bugs)
  to show the most-commented issues and issues by version number
  throughout the project's history.

* [Divergent and Convergent Phases of Data Analysis](https://simplystatistics.org/2018/09/14/divergent-and-convergent-phases-of-data-analysis/)
  examines the flow most people doing data science and analysis projects 
  go through during the exploration, synthesis, modeling and narration
  phases.

* [Forget privacy: you're terrible at targeting anyway](https://apenwarr.ca/log/20190201)
  is a different type of article. It is a strong piece of commentary rather
  than a tutorial on a specific data analysis topic. The author argues that
  *collecting* data is typically easy but doing the dirty analysis work often
  yields little in the way of definitive, actionable insight. Overall it's
  a well-written thought piece that will make you at least stop and ask 
  yourself, "do we *really* need to collect this user data?"

* [Gender Distribution in North Korean Posters with Convolutional Neural Networks](http://digitalnk.com/blog/2017/09/30/gender-distribution-in-north-korean-posters/)
  is a fascinating post that uses convolutional neural networks as a 
  mechanism to identify gender by faces in North Korean posters. The 
  article's analysis on this messy data set and the results it produces
  using some Python glue code with various open source libraries is
  a great example of how data analysis can answer questions that would
  be very time consuming for a person to figure out without a computer.

* [Time Series Analysis in Python: An Introduction](https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a)
  shows how to use the open source 
  [Prophet](https://research.fb.com/prophet-forecasting-at-scale/) library
  to perform time series analysis on a data set.

* [Python Data Wrangling Tutorial: Cryptocurrency Edition](https://elitedatascience.com/python-data-wrangling-tutorial)
  uses the [pandas](/pandas.html) library to clean up a messy 
  cryptocurrency data set and shift the data into a structure that
  is useful for analysis the author wantds to perform.

* [Handy Python Libraries for Formatting and Cleaning Data](https://mode.com/blog/python-data-cleaning-libraries)
  provides a short overview of the libraries such as 
  [Arrow](https://arrow.readthedocs.io/en/latest/) and 
  [Dora](https://github.com/NathanEpstein/Dora) that make it easier to 
  wrangle your data before doing analysis.

* [Analyzing one million robots.txt files](https://intoli.com/blog/analyzing-one-million-robots-txt-files/)
  explains what a `robots.txt` file is, why it matters, how to download
  a bunch of them and then perform some analysis with NumPy.

* [Safely Analyzing Popular Licenses on GitHub Projects](https://www.kaggle.com/mrisdal/safely-analyzing-github-projects-popular-licenses/notebook)
  uses a 
  [Google BigQuery Python helper library](https://github.com/SohierDane/BigQuery_Helper/blob/master/bq_helper.py)
  to work with a massive 3 terabyte data set provided by GitHub.

* [Cleaning and Preparing Data in Python](https://towardsdatascience.com/cleaning-and-preparing-data-in-python-494a9d51a878)
  shows how to uses [pandas](/pandas.html) to do the "boring" part of
  a data analysis job and convert dirty data into a more consistent,
  structured format.

* [9 obscure Python libraries for data science](https://opensource.com/article/18/11/python-libraries-data-science)
  presents several lesser-known but still very useful libraries for 
  performing data analysis such as 
  [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)
  and
  [gym](https://github.com/openai/gym).

* Nvidia's series on defining data analysis, machine learning and deep 
  learning are worth reading for the background and how they break down
  the problem domains:
    
    * [What’s the Difference Between Artificial Intelligence, Machine Learning, and Deep Learning?](https://blogs.nvidia.com/blog/2016/07/29/whats-difference-artificial-intelligence-machine-learning-deep-learning-ai/)
    * [Deep Learning in a Nutshell: History and Training](https://devblogs.nvidia.com/deep-learning-nutshell-history-training/)
    * [Deep Learning in a Nutshell: Core Concepts](https://devblogs.nvidia.com/deep-learning-nutshell-core-concepts/)
