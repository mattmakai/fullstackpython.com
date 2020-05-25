title: Data
category: page
slug: data
sortorder: 0300
toc: True
sidebartitle: 3. Data
meta: Python make it possible to work with data through analysis, visualization and persistence. Learn more about data on Full Stack Python.


Data is an incredibly broad topic but it can be broken down into many
subsections, including (in no particular order):

* data processing / wrangling
* machine learning
* data analysis
* [visualization](/data-visualization.html)
* geospatial mapping
* persistence via [relational databases](/databases.html) and 
  [NoSQL data stores](/no-sql-datastore.html)
* [object-relational mappers](/object-relational-mappers-orms.html)
* natural language processing (NLP)
* indexing, search and retrieval

The Python community has built and continues to create open source libraries 
and tutorials for all of the above topics.


## Why is Python a great language choice for data tasks?
Python has a wide array of open source code libraries available and a
diverse community of people with different backgrounds who contribute to
make those libraries better each day.

In addition, Python data manipulation code can be combined with 
[web frameworks](/web-frameworks.html) and
[web APIs](/application-programming-interfaces.html) to build software
that would be difficult to create with a single other language. For example,
Ruby is a fantastic language for building web applications but its data
analysis and visualization libraries are very limited compared to what
is currently available in the Python ecosystem.


## How did Python become so widely used for working with data?
Python is a general purpose programming language and can be applied to
many problem areas. Over the past couple of decades, Python has become 
increasingly popular in the scientific and financial communities. Projects
such as [pandas](http://pandas.pydata.org/) grew out of a hedge-fund while
[NumPy](http://www.numpy.org/) and [SciPy](http://www.scipy.org/) were
created in academic environments then improved by the broader open source
community.

The question is: why Python was used to created these projects? The answer
is a mix of luck, the growth of the open source community as Python was
maturing and wide adoption by people not formally trained as computer 
scientists. The pragmatic syntax and explicit style helped very intelligent
people without programming backgrounds to pick up the language and get their
work done with less fuss than other programming languages. Over time the
code used in the financial world and scientific community was shared at the
same time global open source communities were developing, further spreading
their usage among a broader base of software developers.

There's no doubt some of the momentum behind Python's wide adoption for all 
types of data manipulation was that it happened to be the right language in
the right place at the right time. Nevertheless, it was ultimately the hard 
work of a massive number of engineers and scientists around the world who
created the incredible mix of data code libraries available today.


### Data inspiration
Sometimes you just need to see it to understand how data analysis,
visualization and storytelling can intersect in a meaningful way. The
following resources do a great job of telling stories with data. There
are more links to stories listed on the [data analysis](/data-analysis.html) 
and [data visualization](/data-visualization.html) pages.

* [Data — from objects to assets](https://www.nature.com/articles/d41586-019-03062-w)
  covers the history of data collection and usage, from 150 years ago to
  today. The article covers how initial steps by individual scientists
  sponsored by wealthy patrons in the 1800s gave way to systematic collection
  by governments and businesses in the 20th century. A significant amount
  of personal data is now held by a few dozen large corporations worldwide
  such as Google, Amazon and Facebook. The article covers some of the
  implications of data as a valuable asset and in general is a great read
  as a high-level overview of on this topic.

* [Metadata Investigation : Inside Hacking Team](https://labs.rs/en/metadata/)
  presents what metadata is and how it can be used to track people even though
  it is often thought of as less of a problem than typical stored data.

* [A visual introduction to machine learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
  is a spectacular example of 
  [data visualization](/data-visualization.html) to explain what a machine
  learning model does on a San Francisco and New York housing data set.

* [Earthquake recurrence and survival analysis: How long should we wait for an overdue earthquake?](http://rocksandwater.net/blog/2016/07/wrightwood-recurrence/)
  combines earthquake data with questions around earthquake recurrence
  probabilities to tell its story.

* [Data Science Project: Profitable App Profiles for App Store and Google Play](https://www.dataquest.io/blog/basic-data-science-portfolio-project-tutorial/)
  is a tutorial that shows you how to use iOS and Android app store data
  for business analysis. This post is part of a larger series on 
  [how to get your first job as a data scientist](https://www.dataquest.io/blog/how-to-get-your-first-data-science-job/)
  which is all worth your time reading to understand the intersection of
  working with data to figure out its value to companies sand organizations.


### Example data sets
Looking for freely-available data to use in your projects but aren't 
sure where to get it? The following links have large free, open data
sets. 

* Check out the 
  [awesome public datasets](https://github.com/awesomedata/awesome-public-datasets)
  project repository for data in many different categories ranging from
  finance to museums.

* [Kickstarter datasets](https://webrobots.io/kickstarter-datasets/)
  are scraped JSON and CSV structured monthly data from Kickstarter 
  projects.

* [Data is Plural](https://tinyletter.com/data-is-plural) is a weekly
  newsletter that highlights open data that you can use for your projects.
  I have been a subscriber to the newsletter for a couple of years now and
  love seeing the wide variety of data sources that are freely available.

* [Data analysis and machine learning projects](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects)
  provides more than just the data, it also includes instructions and
  code for working with the data in your own development environment.

* [Discovering millions of datasets on the web](https://blog.google/products/search/discovering-millions-datasets-web/)
  introduces Google's 
  [dataset search](https://datasetsearch.research.google.com/)
  and explains what they learned from iterating on earlier versions
  of it before they released this one.


### General Python data resources
* [PyData](http://pydata.org/) is a community for developer and users of 
  Python data tools. They put on fantastic conferences around the world and fund 
  the continued development of open source data-related libraries.

* [Anaconda](https://www.anaconda.com/) is one of the leading Python
  companies that pours a tremendous amount of time and funding into
  the data community.

* [A crash course in Python for scientists](http://nbviewer.ipython.org/gist/rpmuller/5920182)
  provides an overview of the Python language with iPython Notebook for those 
  in scientific fields.

* The videos of Travis Oliphant on 
  [Python's Role in Big Data Analytics: Past, Present, and Future](https://www.youtube.com/watch?v=oXRvpBJ-Dkc)
  and 
  [Building the PyData Community](https://www.youtube.com/watch?v=d9Qm3PPoYNQ)
  give historical perspective on how the Python data tools
  have evolved over the past 20ish years based on his first-hand experience
  as a leader and member in that community.

* The [Open Source Data Science Masters](http://datasciencemasters.org/)
  is a well-crafted free curriculum and set of resources for students who
  want to learn both the theory and technologies for working with data.

* [Reproducible research: Stripe’s approach to data science](https://stripe.com/blog/reproducible-research)
  goes through the workflow and tools such as 
  [Jupyter Notebook](/jupyter-notebook.html) that [Stripe](/stripe.html)
  for their data analysis across the company.

* [The Definitive Data Scientist Environment Setup](https://davidadrian.cc/definitive-data-scientist-setup/)
  explains how to set up both a hardware and software configuration that
  is conducive to data science research and analysis.

